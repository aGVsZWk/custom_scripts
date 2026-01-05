# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2026/1/3 14:52
# @File    : xhsshowdemo.py
from xhshow import Xhshow  # pip install xhshow
import requests

client = Xhshow()

# 准备 cookies（支持字典或字符串格式）
# cookies = {
#     "a1": "your_a1_value",
#     "web_session": "your_web_session",
#     "webId": "your_web_id"
# }
# 或使用 Cookie 字符串格式:
# cookies = "a1=your_a1_value; web_session=your_web_session; webId=your_web_id"
cookies = {
    'abRequestId': '850d90b5-088f-5c8d-9d09-8bedd7d79bb7',
    'xsecappid': 'xhs-pc-web',
    'a1': '197530f42b91km63vowhjcwl1p6u9yl6utqw3o0mf30000975580',
    'webId': '19e3c349629c22e7450b215a0ad11578',
    'webBuild': '5.4.0',
    'gid': 'yjDYyidddf7SyjW2q8i4J9l8DjyT6KqhlExVA6iSE1yUKEq87jv1Kq888jW22Y88SJjqSWJ0',
    'web_session': '040069b991afdd98029388db6d3b4b29107fa4',
    'id_token': 'VjEAALU3bDrpa6ZLxzrqnNNusgcujmEeDfGC/gud5U+BsWS66ytrgQxT5y2u8fvy49RfCdYtObDNLscSfyUsZw78RjrImlVGvPi+jciIJo/Hdq8ZZj2wChesDeSQn9vW+rsx4Xrj',
    'unread': '{%22ub%22:%2269565f42000000001e035e40%22%2C%22ue%22:%2269563c5a000000001f0058c8%22%2C%22uc%22:22}',
    'loadts': '1767423408076',
    'acw_tc': '0a4acac317674234085848636e0dd2b05772029ed20eb590440af53d49eada',
    'websectiga': '634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a',
    'sec_poison_id': '83892626-81c6-4e42-a489-f206f263b37c',
}
# 注意: uri 参数可以传递完整 URL 或 URI 路径，会自动提取 URI
headers = client.sign_headers_get(
    uri="https://edith.xiaohongshu.com/api/sns/web/v1/user_posted",  # 完整 URL（推荐）
    # uri="/api/sns/web/v1/user_posted",  # 或者只传 URI 路径
    cookies=cookies,  # 传入完整 cookies
    params={"num": "30", "cursor": "", "user_id": "123"}
)
print(headers)
{'x-s': 'XYS_2UQhPsHCH0c1Pjh9HjIj2erjwjQhyoPTqBPT49pjHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQTJdPIPAZlg98yGLTl4rIMcDhMznlkt9z1JUR9pFFF2dmn+n8awepnzaRx2bD3cDWUyfEy+FDF8r4wJrMEpUVI4/SFLgSIpnzFLo+kG0Z3adbOyL4FP7iE+omaLSQkwBVInD8D4FEc+LRVprSnyd8YaB4gab8lyfznN9QpPrkHaMY/ySkn4/86Ppz+c9EIqMQCLDkcpnbLP9IUJsRDPBTnGFQP4gqMwepC//YHJeDROaHVHdWFH0ijHdF=', 'x-s-common': '2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0c1Pjh9HjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHFN0W9N0ZjNsQh+aHCH0rE+ALAPBGFPfHEPnTT+0+9J74iyf+7JebI+dLE2nI94gzl4A+6PBMfPAZIPeZE+ALMweZjNsQh+jHCHjHVHdW7H0ijHjIj2eWjwjQQPAYUaBzdq9k6qB4Q4fpA8b878FSet9RQzLlTcSiM8/+n4MYP8F8LagY/P9Ql4FpUzfpS2BcI8nT1GFbC/L88JdbFyrSiafp/8bQhqgb78rS9cg+gcf+i4MmF4B4T+e8NpgkhanWIqAmPa7+xqg412/4rnDS9J7+hGSmx2pkMcLSia9prG/4A8fkLprkl4bH3qg4mqBzI/DSe4nMwa/YN2S87LFSe89p34gzH47b7zrSbzdbQzaRAprSyyLShqDMQ4f4S8ob7LjV7qbmCnDEA8bDA8n8l4rbQyFESPM8787bl4omI4gzha7kdqAbgqBpQcM8ganYzPsRc4bbNpd4ma/+yPfRT8Bpkqg4faL+m8pzn4oQQzaV3aLpTJf+f8Bpx87k8qfR6q98l4FRyp9RS8rlrzrQ687+xndmsagYNq9zn4BbQy78S8db7LfQ+/rSo80zsa/P7q7Yl4rL6pFRS2emV+rSiLg+Qz/YN49hFyLDAngrhJrpdanTP2rQn49TQcMknPfcA8nkQ87Pl4g4aag8d8/mfPBpx8gpcaLp98/8+JLzE4g4ManSN8pzfPo+hJaRSPp8F+rlAafp84g4bag8LqoiIcnpDqg4bqeSmqM+n494Q2bbUag83y9Rn4F4Cpdq3+rIFzDQY/fpkqrESzb87PrS9cgPlqApAyM+QzDS3J7+/q04ApfE+zLS9+d+rqg4UaLPhcdmn4er6Lo4SaLL7qFzl47YQyLEAP7p7+LS34d+DqgzV47p7/BRn4b4Q2ezDaL++8/zdarr3aLESygbFyDSiqdzQyAmSydb7J9E8Lgk0GnpAzrQnpLSb/nH3qgz62p8F/rSea7+hLo43+BlS8/bI/7+k/nMPanSmq7W7J7+L4gzEGMm7qLSePBpfpdzpanSw8pzp4pmQcFTSnnuA8p4n4ApQ2e+APgp74LksngbQyrD3a/PMqM8P+fp3JDkS8o+tqM+n4FEQy9Y9aL+/+aRc4F+QcF4iaLptq9TjnSQ7JSGRHjIj2eDjw0WM+/LE+AcU+jIj2erIH0iINsQhP/rjwjQ1J7QTGnIjKc==', 'x-t': '1767455522096', 'x-b3-traceid': '1b0807e2f16bf538', 'x-xray-traceid': 'cdc2477e984f12c7d9722169551051dd'}

# 返回的 headers 包含以下字段:
# {
#     "x-s": "XYS_...",
#     "x-s-common": "...",
#     "x-t": "1234567890",
#     "x-b3-traceid": "...",
#     "x-xray-traceid": "..."
# }

base_headers = {
    "User-Agent": "Mozilla/5.0...",
    "Content-Type": "application/json"
}
base_headers.update(headers)

json_data = {
    'keyword': '解压',
    'page': 2,
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


response = requests.post(
    "https://edith.xiaohongshu.com/api/sns/web/v1/search/notes",
    json=json_data,
    headers=base_headers,
    cookies=cookies
)
resp = response.json()
print(resp)
items = resp['data']["items"]
result = []
for item in items:
    t = {
        "id": item.get("model_type", ""),   # 分享数
        "xsec_token": item.get("xsec_token", ""),
        "model_type": item.get("model_type", ""),   # 分享数
        "nick_name": item.get("node_card", {}).get("user", {}).get("nick_name", ""),
        "liked_count": item.get("note_card", {}).get("interact_info", {}).get("liked_count", ""),   # 点赞数
        "collected_count": item.get("note_card", {}).get("interact_info", {}).get("collected_count", ""),   # 收藏数
        "comment_count": item.get("note_card", {}).get("interact_info", {}).get("comment_count", ""),   # 评论数
        "shared_count": item.get("note_card", {}).get("interact_info", {}).get("shared_count", ""),   # 分享数
        "title": item.get("note_card", {}).get("display_title", ""),   # 分享数
    }
    for t in item.get("corner_tag_info", []):
        if t.get("type") == "publish_time":
            t["publish_time"] = t["publish_time"]
    result.append(t)
print(result)
# 方式1: 使用 update 方法更新现有 headers（推荐）
# base_headers = {
#     "User-Agent": "Mozilla/5.0...",
#     "Content-Type": "application/json"
# }
# base_headers.update(headers)
# response = requests.get(
#     "https://edith.xiaohongshu.com/api/sns/web/v1/user_posted",
#     params={"num": "30", "cursor": "", "user_id": "123"},
#     headers=base_headers,
#     cookies=cookies
# )

# 方式2: 使用 ** 解包创建新 headers
response = requests.get(
    "https://edith.xiaohongshu.com/api/sns/web/v1/user_posted",
    params={"num": "30", "cursor": "", "user_id": "123"},
    headers={
        "User-Agent": "Mozilla/5.0...",
        "Content-Type": "application/json",
        **headers  # 解包签名 headers（会创建新字典）
    },
    cookies=cookies
)

# POST 请求示例：使用 sign_headers_post
headers_post = client.sign_headers_post(
    uri="https://edith.xiaohongshu.com/api/sns/web/v1/login",
    cookies=cookies,
    payload={"username": "test", "password": "123456"}
)

response = requests.post(
    "https://edith.xiaohongshu.com/api/sns/web/v1/login",
    json={"username": "test", "password": "123456"},
    headers={**base_headers, **headers_post},
    cookies=cookies
)

# 构建符合xhs平台的GET请求链接
full_url = client.build_url(
    base_url="https://edith.xiaohongshu.com/api/sns/web/v1/user_posted",
    params={"num": "30", "cursor": "", "user_id": "123"}
)
response = requests.get(full_url, headers=headers, cookies=cookies)

# 构建符合xhs平台的POST请求body
json_body = client.build_json_body(
    payload={"username": "test", "password": "123456"}
)
response = requests.post(url, data=json_body, headers=headers, cookies=cookies)