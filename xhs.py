# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2026/1/2 23:13
# @File    : xhs.py
import requests
import json
import re
import time
import execjs


class Spider(object):
    def __init__(self):
        self.url = "https://www.xiaohongshu.com/search_result?keyword=%25E8%25A7%25A3%25E5%258E%258B&source=unknown"
        self.headers = {
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
            'x-b3-traceid': '6a3c5c78a20822ed',
            'x-s': 'XYS_2UQhPsHCH0c1PUhIHjIj2erjwjQhyoPTqBPT49pjHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHfM1qAZAPebK89RYa7bjJpr9ndSa80mdtFzFPBSD+ApIcdkk8SHh+p86a9khnnSDa/QxPnP720zD8fzAyo4H8FQQ4b8z2gmpndch4SkjpfSrPLb1/dSzaezSLrWMLokmpd868gmPpeqIzfYB+Flb+b86cp4a+rR7/sTlpSLIaDYNnbPIwrIhpFPMtFMeJdmALdkaaSmpGpcAJrQiaM+18b8yJB+kz/mtLDS8PrRH/SQapbzgyDPlwoD7cDT3HjIj2ecjwjQ6GfkSG7cjKc==',
            'x-s-common': '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',
            'x-t': str(int(time.time() * 1000)),
            'x-xray-traceid': 'cdbfad91650d5e20bdde44379290c9cc',
            # 'cookie': 'gid=yjy84W4i0JUWyjy84W4i4dWUDjESSx2D99FJUVKECEKkiKq8D7IUKU888qyWjKJ802Ydi2qj; abRequestId=474e74b307482128590630db1e1c6297; a1=1987fed663bkp9rq3vlogxvaq65my2jongac98drz30000243059; webId=0b75119b9f8ea6a0b1a4066068e6c1d4; x-user-id-creator.xiaohongshu.com=68e5ec9500000000320252c5; customerClientId=456689191186799; webBuild=5.4.0; xsecappid=xhs-pc-web; acw_tc=0a0b12d717673664984223012e68843b53cd9fa8e036f54632ce209b7b4007; web_session=040069b36cea6812b248fd97623b4b993a25cf; id_token=VjEAAKP83XCyePnQUsx0Xsq15zX02xS+KgKb6LK2iqpLrcpmemqO50Dwg5rJm5C9yERO5rcUc966+x3GZryZ73Zvgo35oDc4vdXzzgHkbfTDvzjDNvNWfIwzfmGFJ0v7XNNocSl/; unread={%22ub%22:%22695725d2000000002202e4b5%22%2C%22ue%22:%22694c3c5c000000001e004caf%22%2C%22uc%22:23}; loadts=1767368103864; websectiga=7750c37de43b7be9de8ed9ff8ea0e576519e8cd2157322eb972ecb429a7735d4; sec_poison_id=c22d7ce3-6a99-49ba-aeca-6bde1fd0efb8',
        }

        self.cookies = {
            'gid': 'yjy84W4i0JUWyjy84W4i4dWUDjESSx2D99FJUVKECEKkiKq8D7IUKU888qyWjKJ802Ydi2qj',
            'abRequestId': '474e74b307482128590630db1e1c6297',
            'a1': '1987fed663bkp9rq3vlogxvaq65my2jongac98drz30000243059',
            'webId': '0b75119b9f8ea6a0b1a4066068e6c1d4',
            'x-user-id-creator.xiaohongshu.com': '68e5ec9500000000320252c5',
            'customerClientId': '456689191186799',
            'webBuild': '5.4.0',
            'xsecappid': 'xhs-pc-web',
            'acw_tc': '0a0b12d717673664984223012e68843b53cd9fa8e036f54632ce209b7b4007',
            'web_session': '040069b36cea6812b248fd97623b4b993a25cf',
            'id_token': 'VjEAAKP83XCyePnQUsx0Xsq15zX02xS+KgKb6LK2iqpLrcpmemqO50Dwg5rJm5C9yERO5rcUc966+x3GZryZ73Zvgo35oDc4vdXzzgHkbfTDvzjDNvNWfIwzfmGFJ0v7XNNocSl/',
            'unread': '{%22ub%22:%22695725d2000000002202e4b5%22%2C%22ue%22:%22694c3c5c000000001e004caf%22%2C%22uc%22:23}',
            'loadts': '1767368103864',
            'websectiga': '7750c37de43b7be9de8ed9ff8ea0e576519e8cd2157322eb972ecb429a7735d4',
            'sec_poison_id': 'c22d7ce3-6a99-49ba-aeca-6bde1fd0efb8',
        }

    def parse_headers(self):
        pass


json_data = {
    'keyword': '解压',
    'page': 1,
    'page_size': 20,
    'search_id': '2fsu1eun18mk90gncjtgg@2fsu1hlhpne9a8ehvcdtx',
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
                '不限',
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

x = "/api/sns/web/v1/search/filter?keyword=%E8%A7%A3%E5%8E%8B%E7%8E%A9%E5%85%B7&search_id=2fsu9c9fre6waume3orh3"
s = None


x = "/api/sns/web/v1/search/notes"
s = {
    "keyword": "解压玩具",
    "page": 1,
    "page_size": 20,
    "search_id": "2fsu9c9fre6waume3orh3",
    "sort": "general",
    "note_type": 0,
    "ext_flags": [],
    "filters": [
        {
            "tags": [
                "general"
            ],
            "type": "sort_type"
        },
        {
            "tags": [
                "不限"
            ],
            "type": "filter_note_type"
        },
        {
            "tags": [
                "不限"
            ],
            "type": "filter_note_time"
        },
        {
            "tags": [
                "不限"
            ],
            "type": "filter_note_range"
        },
        {
            "tags": [
                "不限"
            ],
            "type": "filter_pos_distance"
        }
    ],
    "geo": "",
    "image_formats": [
        "jpg",
        "webp",
        "avif"
    ]
}


s = {
    "keyword": "解压玩具",
    "search_id": "2fsu9c9fre6waume3orh3",
    "biz_type": "web_search_user",
    "request_id": "549305242-1767371625353"
}

#    var _ = "X-s"
#      , b = "X-t"
#      , x = getRealUrl(a, c, d)
#      , p = seccore_signv2;
#    p && (r.headers[_] = p(x, s),
#    r.headers[b] = +new Date + "")


#   r.headers["X-S-Common"] = (0,
#                     h.xE)((0,
#                     h.lz)(JSON.stringify(y)))
#                 })


# X-S  p(x, s),
# X-S  seccore_signv2('/api/sns/web/v1/search/recommend?keyword=%E8%A7%A3%E5%8E%8B', s),

# url = '/api/sns/web/v1/search/recommend?keyword=%E8%A7%A3%E5%8E%8B'
# with open("seccore_signv2.js", "r", encoding="utf-8") as f:
#     js_code = f.read()
# ctx = execjs.compile(js_code)
# ret = ctx.call(url, "")
# print(ret)

# X-S
l = {
    "x0": "4.3.0",
    "x1": "xhs-pc-web",
    "x2": "Mac OS",
    "x3": "mns0301_goaKqP2qZsWVDJj+Dt0id1TMpiifR85Vv7jxYidI2j517I4dBl16NOnRTy/QypUZt8vZbViD1AnNyQH4ePH5PzAVvoepLT70FhF7LE4VoAWR4OwL+qVU0JHKXS08L8WC5+MCnpsRzRJPUaT3l14KSndVZlciE0JRIk0OHNRRTawNMeuoYzN4",
    "x4": ""
}
data = json.dumps(l)
with open("encode_utf8.js", "r", encoding="utf-8") as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
ret = ctx.call("")
print(ret)
# base64(utf8(json(l)))


# response = requests.post(
#     'https://edith.xiaohongshu.com/api/sns/web/v1/search/notes',
#     cookies=cookies,
#     headers=headers,
#     json=json_data,
# )
#
