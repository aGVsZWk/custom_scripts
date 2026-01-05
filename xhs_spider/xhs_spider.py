# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2026/1/4 00:04
# @File    : xhs_spider.py
from xhshow import Xhshow
from curl_cffi import requests as curl_requests
import requests
from loguru import logger
import os
import tenacity
import time
import random
import json


def sleep_random():
    time.sleep(random.random() * 4)


def init_log():
    # 确保日志目录存在（可选，但推荐）
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 1. 基础用法：将日志写入单个文件
    # 添加文件输出，指定日志文件路径
    logger.add(os.path.join(log_dir, "xhy_spider.log"))
    logger.add(
        os.path.join(log_dir, "xhy_spider_rotate.log"),
        rotation="500 MB",    # 按大小分割
        # rotation="00:00",    # 可选：按时间分割（每天0点新建文件）
        retention="3 days",   # 日志保留7天
        compression="zip",    # 压缩过期日志
        encoding="utf-8",     # 确保中文正常显示
        enqueue=True,         # 异步写入，提升性能
        backtrace=True,       # 记录完整的异常堆栈信息
        diagnose=True         # 记录变量诊断信息（开发环境推荐）
    )


class XhsSpider(object):
    def __init__(self):
        init_log()
        self.client = Xhshow()
        self.cookies = {
            'gid': 'yjy84W4i0JUWyjy84W4i4dWUDjESSx2D99FJUVKECEKkiKq8D7IUKU888qyWjKJ802Ydi2qj',
            'abRequestId': '474e74b307482128590630db1e1c6297',
            'a1': '1987fed663bkp9rq3vlogxvaq65my2jongac98drz30000243059',
            'webId': '0b75119b9f8ea6a0b1a4066068e6c1d4',
            'x-user-id-creator.xiaohongshu.com': '68e5ec9500000000320252c5',
            'customerClientId': '456689191186799',
            'acw_tc': '0a0bb36c17674604978907996e63ffeb822f73b4e16092f463b59013c7ff29',
            'xsecappid': 'xhs-pc-web',
            'websectiga': 'f3d8eaee8a8c63016320d94a1bd00562d516a5417bc43a032a80cbf70f07d5c0',
            'sec_poison_id': '048c1350-6cda-47f6-a34d-50540ed27733',
            'webBuild': '5.4.0',
            'loadts': '1767461988968',
            'web_session': '040069b22c5ab730a0431f186c3b4ba384fb77',
            'id_token': 'VjEAAC0vlRDL+300NsEcoInVAdxBhWhm5U31E0WZewoEyHnnNoKCdaBFOlrv/TdxkuEgPoJNGbGdsFY4flUUD9Ik/JqEv3w/WVxJUEhvCiVNGs6ss1sXTggyNPoQdu0hph9UC60n',
            'unread': '{%22ub%22:%22694ce11f000000002200bf4d%22%2C%22ue%22:%2269561c52000000001e02c8ac%22%2C%22uc%22:30}',
        }

    def get_headers(self, uri, data, method='GET'):
        if method == 'GET':
            sign_headers = self.client.sign_headers_get(
                uri=uri,  # 完整 URL（推荐）
                # uri="/api/sns/web/v1/user_posted",  # 或者只传 URI 路径
                cookies=self.cookies,  # 传入完整 cookies
                params=data
            )
        else:
            sign_headers = self.client.sign_headers_post(
                uri=uri,
                cookies=self.cookies,
                payload=data
            )
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://www.xiaohongshu.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.xiaohongshu.com/',
            'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        }
        headers.update(sign_headers)
        return headers

    @tenacity.retry(stop=tenacity.stop_after_attempt(3), wait=tenacity.wait_fixed(1))
    def search_video_notes(self, keyword, page):
        json_data = {
            'keyword': f'{keyword}',
            'page': page,
            'page_size': 20,
            'search_id': '2fsxlpboog86cfa3oorqs@2fsxn1yhzge9epxwvqqnr',
            'sort': 'general',
            'note_type': 0,
            'ext_flags': [],
            'filters': [
                {
                    'tags': [
                        'popularity_descending',
                    ],
                    'type': 'sort_type',
                },
                {
                    'tags': [
                        '视频笔记',
                    ],
                    'type': 'filter_note_type',
                },
                {
                    'tags': [
                        '不限',
                    ],
                    'type': 'filter_note_time',
                },
                {
                    'tags': [
                        '不限',
                    ],
                    'type': 'filter_note_range',
                },
                {
                    'tags': [
                        '不限',
                    ],
                    'type': 'filter_pos_distance',
                },
            ],
            'geo': '',
            'image_formats': [
                'jpg',
                'webp',
                'avif',
            ],
        }
        url = "https://edith.xiaohongshu.com/api/sns/web/v1/search/notes"
        response = requests.post(url, json=json_data, headers=self.get_headers(url, json_data), cookies=self.cookies)
        resp_data = response.json()
        if resp_data["code"] != 0:
            logger.error(f"搜索视频笔记失败, {resp_data}")
            raise Exception(resp_data["msg"])
        ret = []
        for item in resp_data['data']["items"]:
            t = {
                "id": item.get("id", ""),  # 笔记id
                "model_type": item.get("model_type", ""),  # 分享数
                "xsec_token": item.get("xsec_token", ""),
                "nick_name": item.get("note_card", {}).get("user", {}).get("nick_name", ""),  # 用户昵称
                "title": item.get("note_card", {}).get("display_title", ""),  # 标题
                "liked_count": item.get("note_card", {}).get("interact_info", {}).get("liked_count", "-1"),  # 点赞数
                "collected_count": item.get("note_card", {}).get("interact_info", {}).get("collected_count", "-1"),  # 收藏数
                "comment_count": item.get("note_card", {}).get("interact_info", {}).get("comment_count", "-1"),  # 评论数
                "shared_count": item.get("note_card", {}).get("interact_info", {}).get("shared_count", "-1"),  # 分享数
            }
            for t in item.get("corner_tag_info", []):
                if t.get("type") == "publish_time":
                    t["publish_time"] = t["publish_time"]
            ret.append(t)
        logger.info(f"keyword: {keyword}, page: {page}, data: {ret}")
        sleep_random()
        return ret

    def feed_video_detail(self, note_id, xsec_token):
        json_data = {
          # "source_note_id": f"{note_id}",
          "source_note_id": f"6906ec0a0000000003013c0d",
          "image_formats": [
            "jpg",
            "webp",
            "avif"
          ],
          "extra": {
            "need_body_topic": "1"
          },
          "xsec_source": "pc_search",
          # "xsec_token": f"{xsec_token}"
          "xsec_token": f"ABbXyMtxjSFgxobE5CoO4AxzebmctogxH5ENg2FHkJz88="
        }
        sorted(json_data)
        url = "https://edith.xiaohongshu.com/api/sns/web/v1/feed"
        # headers = self.get_headers(url, json_data)
        headers = self.get_headers(url, data=json_data, method="POST")
        headers["xy-direction"] = "23"
        response = curl_requests.post(url, json=json_data, headers=headers, cookies=self.cookies, impersonate="chrome")
        resp_data = response.json()
        if resp_data["code"] != 0:
            logger.error(f"获取视频笔记详情失败, {resp_data}")
            raise Exception(resp_data["msg"])
        result = resp_data["data"]["items"][0]["note_card"]
        current_time = resp_data["data"]["current_time"]
        if not result:
            raise Exception(f"解析视频详情失败, {resp_data}")
        ret = {
            "desc": result.get("desc", ""),
            "image": result.get("image_list", [{}])[0].get("url_default", ""),
            "height": result.get("image_list", [{}])[0].get("height", -1),
            "width": result.get("image_list", [{}])[0].get("width", -1),
            "tags": "|".join(map(lambda x: x["name"], result.get("tag_list", []))),
            "master_url": result.get("video", {}).get("media", {}).get("stream", {}).get("h264", [{}])[0].get("master_url", ""),
            # "backup_urls": "|".join(result.get("video", {}).get("media", {}).get("stream", {}).get("h264", [{}])[0].get("backup_urls", [])),
            "size": result.get("video", {}).get("media", {}).get("stream", {}).get("h264", [{}])[0].get("size", -1),
            "duration": result.get("video", {}).get("media", {}).get("stream", {}).get("h264", [{}])[0].get("duration", -1),
            "user_id": result.get("user", {}).get("user_id", ""),
            "user_nick_name": result.get("user", {}).get("nickname", ""),
            "avatar": result.get("user", {}).get("avatar", ""),
            "time": result.get("time", -1),
            "last_update_time": result.get("last_update_time", -1),
            "crawl_time": current_time,
        }
        logger.info(f"video detail:{ret}")
        sleep_random()
        return ret

    def _get_video_comment(self, note_id, xsec_token, cursor=None):
        url = 'https://edith.xiaohongshu.com/api/sns/web/v2/comment/page'
        params = {
            "note_id": note_id,
            "cursor": cursor,
            "top_comment_id": None,
            "image_formats": "jpg,webp,avif",
            "xsec_token": xsec_token,
        }
        response = requests.get(url, params=params, cookies=self.cookies, headers=self.get_headers(url, params))
        resp_data = response.json()
        if resp_data["code"] != 0:
            logger.error(f"获取视频笔记评论失败, {resp_data}")
            raise Exception(resp_data["msg"])
        has_more = resp_data["data"]["has_more"]
        next_cursor = resp_data["data"]["cursor"]
        comments = resp_data["data"]["comments"]
        ret = []
        for comment in comments:
            sub_comments = comment["sub_comments"]
            sub_contents = []
            for sub_comment in sub_comments:
                sub_contents.append(sub_comment["content"])
            t = {
                "content": comment["content"],
                "sub_comments": sub_contents,
            }
            ret.append(t)
        sleep_random()
        return has_more, next_cursor, ret

    def get_video_comment(self, note_id, xsec_token):
        ret = []
        next_cursor = None
        while True:
            has_more, next_cursor, comments = self._get_video_comment(note_id, xsec_token, next_cursor)
            logger.info(f"comments: {comments}")
            if not has_more:
                break
            ret += comments
        return ret

    def run(self):
        keyword = "解压"
        end_page = 10
        ret = []
        for i in range(1, end_page + 1):
            video_notes = self.search_video_notes(keyword, i)
            for video_note in video_notes:
                if int(video_note["liked_count"]) > 1000 or int(video_note["collected_count"]) > 1000 or int(video_note["comment_count"]) > 1000:
                    video_detail = self.feed_video_detail(video_note["id"], video_note["xsec_token"])
                    video_commens = self.get_video_comment(video_note["id"], video_note["xsec_token"])
                    video_note.update(video_detail)
                    video_note["comments"] = video_commens
                    ret.append(video_note)
        print(ret)


if __name__ == '__main__':
    spider = XhsSpider()
    spider.run()
