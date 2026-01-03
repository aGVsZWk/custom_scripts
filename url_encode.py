# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2026/1/2 19:22
# @File    : url_encode.py
from urllib.parse import quote, unquote


print(quote("你是二傻子"))

var = [
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
    "appid=1014",
    "bitrate=0",
    "callback=callback123",
    "clienttime=1767357258512",
    "clientver=1000",
    "dfid=34fWfx1rK2Og22op9T4HJM9U",
    "filter=10",
    "inputtype=0",
    "iscorrection=1",
    "isfuzzy=0",
    "keyword=周杰伦",
    "mid=1c5d9125ac58e29910ade23e3c39a135",
    "page=1",
    "pagesize=30",
    "platform=WebFilter",
    "privilege_filter=0",
    "srcappid=2919",
    "token=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33",
    "userid=2420213294",
    "uuid=1c5d9125ac58e29910ade23e3c39a135",
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
]
print(var)

print("https://webfs.tx.kugou.com/202601022103/f4d6ddcc358736e10ae77c32b8c193d7/v3/c6b5a741051fcbc1af7531ca2ceecc15/yp/p_0_960123/ap1014_us2420213294_mii0w1iw8z2ai2iphcu80ooo2ki81120_pi406_mx32179991_s2064702562.mp3")

# curl 'https://www.kugou.com/yy/html/search.html' \
#   -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'KuGooRandom=66311767356471219; kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=0, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: document' \
#   -H 'sec-fetch-mode: navigate' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-fetch-user: ?1' \
#   -H 'upgrade-insecure-requests: 1' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://m3ws.kugou.com/static/js/share/npm/sentry5.6.1.min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/js/PCToMoblie.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/css/cmdialog.css?20220113' \
#   -H 'accept: text/css,*/*;q=0.1' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=0' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: style' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/css/cmhead_v20.css?20220113' \
#   -H 'accept: text/css,*/*;q=0.1' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=0' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: style' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_logo_v20.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2, i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://m.kugou.com/static/js/share/npm/sentry5.6.1.min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/js/jquery.min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/js/lib.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/js/utility.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/common/js/min/login/kguser.v2.min.js?20190111' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/common/js/repalceHttpsImg.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/common/js/min/npm/getBaseInfo.min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/common/js/min/infSign.min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/verify/static/js/registerDev.v1.min.js?appid=1014&20190408' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/js/cmhead.min.js?20220119' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/css/search.src.css' \
#   -H 'accept: text/css,*/*;q=0.1' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: style' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/html/images/singer.jpg' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'KuGooRandom=66311767356471219; kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2, i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/css/cmfoot.css?20220127' \
#   -H 'accept: text/css,*/*;q=0.1' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: style' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/common/js/min/inf_public-min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/js/search/search.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'chrome-extension://aefehdhdciieocakfobpaaolhipkcpgc/content_scripts/copy.js' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://www.kugou.com/common/images/icon_search_white.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/common/css/cmhead_v20.css?20220113' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_arrow_down_black.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/common/css/cmhead_v20.css?20220113' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzYiIGhlaWdodD0iMzYiPjxkZWZzPjxmaWx0ZXIgaWQ9ImRhcmtyZWFkZXItaW1hZ2UtZmlsdGVyIj48ZmVDb2xvck1hdHJpeCB0eXBlPSJtYXRyaXgiIHZhbHVlcz0iMC4yMTggLTAuNzQxIC0wLjg5NCAwLjAwMCAxLjMzNSAtMC44MjYgMC4zMjIgLTAuODczIDAuMDAwIDEuMjk4IC0wLjc5OSAtMC43MzAgMC4yMjIgMC4wMDAgMS4yMzIgMC4wMDAgMC4wMDAgMC4wMDAgMS4wMDAgMC4wMDAiIC8+PC9maWx0ZXI+PC9kZWZzPjxpbWFnZSB3aWR0aD0iMzYiIGhlaWdodD0iMzYiIGZpbHRlcj0idXJsKCNkYXJrcmVhZGVyLWltYWdlLWZpbHRlcikiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2UvcG5nO2Jhc2U2NCxpVkJPUncwS0dnb0FBQUFOU1VoRVVnQUFBQ1FBQUFBa0NBTUFBQURXM21pcUFBQUFBWE5TUjBJQXJzNGM2UUFBQUh0UVRGUkZBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQXZYZ2NzQUFBQUNoMFVrNVRBQUVDQlFrT0ZCb2lNelErU1ZWV1kzRnpkNENFaVl1UHFyYTN3c3pRMGRYZTVlZng5dnI5L3ZOMXlETUFBQUIvU1VSQlZCZ1o3Y0h0RG9FQUFJYlJOeFZSaEZDRXZ1dTUveXZVekxBb3YyMmRvOUhvWlpPSEU3MlpIUEt0dWpLSVREMlpFZVRxMmdGSFN3L1dDZGlyeXdpQjJOYWRIUU9ob1U4QmNKNnFOVDBEZ2I1YU41RE1wRmtDelZvOS9CcFN4MG1oOXRWclZVR1dRYlhVQUsra1ZYb2E1QlpRdVBwaGNiM01OZm9ITjQrcUM3V3J5VDgrQUFBQUFFbEZUa1N1UW1DQyIgLz48L3N2Zz4=' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://hm.baidu.com/hm.js?aedee6983d4cfc62f509129360d6bb3d' \
#   -H 'Accept: */*' \
#   -H 'Accept-Language: zh-CN,zh;q=0.9' \
#   -H 'Cache-Control: no-cache' \
#   -H 'Connection: keep-alive' \
#   -b 'HMACCOUNT_BFESS=84D34B87DD623F16; H_WISE_SIDS_BFESS=63147_65592_66584_66592_66690_66806_66852_66962_67003_67042_67046_67089_67044_67108_67131_67140_67146_67152_67164_67178_67180; BAIDUID_BFESS=56578A9E53F7360E8F9F231CFEA48923:FG=1; ZFY=gscUrcX4wpH5C3R1eetT8K2SU1Ad3RaF6H:ALElA5E58:C; BDUSS_BFESS=FhMElYREdxZHlZWjUtRFdzdGp0RjNOYm41Vk12RDBaZXBrMDh0MnlWZkVPWDlwRVFBQUFBJCQAAAAAAAAAAAEAAACLFupLzfXP~szSMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMSsV2nErFdpaT; ab_sr=1.0.1_MjQyMTQxMDVjNWM4MGQzZGRmOGEyMmQxMjdkMGQ1NTk2YmYwNGIyZWUyM2ZhNDA3NzFlMTcyOWE5YjQ0ZmM5M2QyMmMxY2E1NjA1OWM3MDJmNDgxMmRhZjNkMmI2YTAxM2I1MzE1ZTExMGZlNWI1MmQ0OGM3NDQ5MzgyOGM5NTgwNDQ1NDNlZTFhMTU1N2U3ODMwNWRlYzg3YzkzNjJlOTUyMjU2MDQyM2EwNDM3MTY0MDgxYmQzNTQwNjkxY2U0' \
#   -H 'Pragma: no-cache' \
#   -H 'Referer: https://www.kugou.com/' \
#   -H 'Sec-Fetch-Dest: script' \
#   -H 'Sec-Fetch-Mode: no-cors' \
#   -H 'Sec-Fetch-Site: cross-site' \
#   -H 'Sec-Fetch-Storage-Access: active' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' ;
# curl 'https://www.kugou.com/yy/static/images/search/search.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/static/css/search.src.css' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_tme_new.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/common/css/cmfoot.css?20220127' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i2.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/common/css/cmfoot.css?20220127' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i3.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/common/css/cmfoot.css?20220127' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i4.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/common/css/cmfoot.css?20220127' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i5.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/common/css/cmfoot.css?20220127' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i7.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/common/css/cmfoot.css?20220127' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i8.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/common/css/cmfoot.css?20220127' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'chrome-extension://ibdfeimkglcmdejppabkaidpippniiob/content/windowDataMessage.js' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://gateway.kugou.com/ads.gateway/v1/search_no_focus_word?srcappid=2919&clientver=1000&clienttime=1767356872&mid=1c5d9125ac58e29910ade23e3c39a135&uuid=1767356872021&dfid=34fWfx1rK2Og22op9T4HJM9U&appid=1014&signature=51989fddcb8233711cef6f671309e8b9' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw '{"userid":"2420213294","plat":103,"m_type":0,"vip_type":0,"own_ads":{}}' ;
# curl 'https://searchrecommend.kugou.com/v1/word_nofocus?platform=pc&callback=jQuery19102848953104205496_1767356871983&_=1767356871984' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://imgessl.kugou.com/kugouicon/165//' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/qrcode4home_download.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/coinsFloat/icon_coins_float.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/coinsFloat/icon_coins_float_text.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/coinsFloat/icon_close.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/coinsFloat/icon_coins_popup.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/coinsFloat/coins_qrcode.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_rs_i1.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/common/css/cmhead_v20.css?20220113' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_rs_i3.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/common/css/cmhead_v20.css?20220113' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_rs_i4.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/common/css/cmhead_v20.css?20220113' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxmaWx0ZXIgaWQ9ImRhcmtyZWFkZXItaW1hZ2UtZmlsdGVyIj48ZmVDb2xvck1hdHJpeCB0eXBlPSJtYXRyaXgiIHZhbHVlcz0iMC4yMTggLTAuNzQxIC0wLjg5NCAwLjAwMCAxLjMzNSAtMC44MjYgMC4zMjIgLTAuODczIDAuMDAwIDEuMjk4IC0wLjc5OSAtMC43MzAgMC4yMjIgMC4wMDAgMS4yMzIgMC4wMDAgMC4wMDAgMC4wMDAgMS4wMDAgMC4wMDAiIC8+PC9maWx0ZXI+PC9kZWZzPjxpbWFnZSB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbHRlcj0idXJsKCNkYXJrcmVhZGVyLWltYWdlLWZpbHRlcikiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2UvcG5nO2Jhc2U2NCxpVkJPUncwS0dnb0FBQUFOU1VoRVVnQUFBRUFBQUFCQUNBTUFBQUNkdDRIc0FBQUFBWE5TUjBJQXJzNGM2UUFBQWRGUVRGUkZBQUFBLy8vL2dJQ0FWYXFxZ0lDQVptYVpWWUNBYlcyU1lJQ0FWWEdPWm1hQVhYU0xWV3FBWW5hSlcyMS9ZSENBWG10NVdXYUFWVzE1VldxQVhHWjZWV2g3V0dwN1ZXWjNWV3g4VjJaOFZXcDRXbWQ4V1daNVZXZDVXV2w2VjJkM1ZXcDZXR2g0VldoN1YybDdWV2Q1V0dwN1ZXWjNWV2w1V0doNFZXZDZWV1ozVm1oNFZXZDRWMmg2Vm1kNFZXWjNWMmg0VldoNVZtWjVWbWg0VldkNVZtaDVWbVozVldoNFYyZDNWbVo1VjJaNVZtaDRWV2Q1Vm1kNVZXWjRWV1ozVm1kNFZtWjNWbVo0VldkM1ZtaDRWV2Q1Vm1aNFZtZDVWV1o0Vm1oNVZXWjNWbWQ0Vm1aNFZXZDNWbVo0Vm1kM1ZXZDRWbVo0VldaNFZtZDVWbWQ0VldaM1ZtZDRWV2Q0Vm1aNFZXZDRWV1o0Vm1kNFZXWjNWbWQ0Vm1aM1ZXZDRWbVo0VldkM1ZtWjRWV2Q0Vm1aM1ZXZDRWV1o0Vm1kNFZtZDRWV1ozVm1kM1ZXZDNWV2QzVldkNFZtZDRWV1ozVm1kNFZXWjNWbWQzVldaNFZXZDNWbVo0VldkM1ZtWjNWV1o0VldkNFZXWjNWV1ozVm1kNFZXWjNWbVozVldkM1ZXZDRWbWQ0VldaNFZXWjNWV2Q0Vm1aNFZXZDNWV1o0Vm1aM1ZXZDRWbWQ0VldaM1ZXWjNWV1ozVldkNFZtWjNWV1o0Vm1aNFZXWjNWV2QzVldaNFZtWjNWV2Q0VldaM1ZtZDRWV1ozVldaM2gvYWtYUUFBQUpwMFVrNVRBQUVDQXdRRkJnY0lDUW9MREEwT0VCTVVGUmdaR3gwZUlTTWtKU2dxTGk4d01UWTRPVG84UDBCRlMxTlhXRmxhVzExZlltTmxhMnh0Ym5CeGNuUjFlSGw2Zlg2QWdZS0RoSVdIaUl5TmpvK1FrWk9VbFphWG1aMmZvcVNscHFlb3FxdXNycSt3c2JLMXRyaTZ2TDNCdzhURng4akp5c3ZOenM3UDB0UFUxdGpkMytEajVPanA2dXZzN3Uvdzh2UDA5ZmY0K1BuNisvejkvbVhyTEs4QUFBTlVTVVJCVkZqRDdaZFpXeE14RkliVHFnV3FMYUpRUVZrVUYxeEEzRVZRQVVFVXdSVlVWRUJCY0VkUVVheWlDRm9XWlNrQ3RYMS9yUmNaMm1RNm5ZNjNQdVNxNTN6NTNubWFuSlBKQ0xFMi9zdFIwSHgxWnp6WWRybDFWendvYVcwdVNPOC9FWWFsdlVZUStBbVJmVWF3ZXhIQ0o5TFlOM1VCOE5BSUd3RjZqS0FiZ0s2TmR2N3N0d0RRWjhRZEFPK000TEhVM21hbjltLzVKT2ZFRGxvQkRzYWsrbWxMS3I4M0tHZk1sd3NyZ0NpZmwzclFhKzEzUFRMMEhjSWFJSFlZVDNoa0RhaVQ2a3VGYndJSTcwczVwODdLWDdRTXdOTU1rUm9nTXA0Q3NGeGs4UWVHQUJqSkVuWUE0UjBCWU1pVkJEZ0d3R1JBMkFORVlCS0FZMmEvZXd5QWNwRU9JTW9CR0hPYkFJY0FlQ2JTQThRekFBNlpza01Bc1NJbmdLSVl3S0NleklzQjlBc25BTkVQRU12VGNsVUE3SGNHMkE5QWxaWjdCUkJ5T3dPNFF3Q3Z0Q0tZQmJnam5BSEVIWUJadFJRS0FEanNGSEFZZ0lLa1RTeDBDaWhNMnNncWdHVzNVNEI3MmJ5S0RRQWg0UlFnUWdBWGxNUTFnTEZFdkw2bTYzeW1DbkFkNzd6b1QraGpBTmNVUUJ2QTEwVGNEYnpmbkFCa1BBYUM2K0w2VjRBMkJYQUY0RmZpYkFUZ1MrNHF3RGNBUUZsOHdpekFGUVZRRDBDV0R1QmJ2Z1RrZkVBSFpBRlFyd0NPbWpiMm9YVDg2QVg0S0R1ZGtRMTYyUnhWQUtVQUhFaWNPeStrWnhIZ3QvejlPVGN1SHdDZ1ZBSDRvd0RYRXdsUEw2YnhSbm1mM0FDSSt0V05EUUtNSzRsMTkzVC9jL1ZkTUE0UTFDcWpGWUJpdGI5dXF2N09EWXBVREVDckJpZ0RvRVhMWFVyNGIybUhjSXRwVTRVUXdqVUJzSkNySmMrdCtodTFkRzRZWU1KMHNEY0FjRmRQbm93Q3hFN3IyYnNBTkpqYXd6OE5FREYxZE1VS3JGU2FlamtDTU8wM045Z1pBSVl6OVd6Sjdkc2xlaVp6R0lBelNSM3ErUWJBZzNSWG9BZXl5ajNKU29WY3NGcDdmNjJjVldGMVBlZ0JJRnB0NTYrT0F0RGpzcnVnZEhoUzJUMGQ5bGVVUUVqcWczbldldDZnMUVPQlZFL1lzeVJuaEp2OXlhSy9PU3pWcFQycC8yTFp0RkY3MHpVNXVwSlRFNWZLN0JZcGYzUzFmUCs4UHJ2ZFdDclg5ck92LzZ6bVIvUHR0OG4zUk9uQnlQZmh2cjdoN3hFbDljU1hybERjcDZaSU9hWk91UjFjMTMxTkM5YjJoU2FmY0RhMnRzOGwyK2ZhdC83RFI0TzNzbmRHZGMvMFZuci85Y1BEVlh5azZYNy93RUQvL2FZanhhNjFEN0gvZS93Rll4aEhOMXN1bW1jQUFBQUFTVVZPUks1Q1lJST0iIC8+PC9zdmc+' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxmaWx0ZXIgaWQ9ImRhcmtyZWFkZXItaW1hZ2UtZmlsdGVyIj48ZmVDb2xvck1hdHJpeCB0eXBlPSJtYXRyaXgiIHZhbHVlcz0iMC4yMTggLTAuNzQxIC0wLjg5NCAwLjAwMCAxLjMzNSAtMC44MjYgMC4zMjIgLTAuODczIDAuMDAwIDEuMjk4IC0wLjc5OSAtMC43MzAgMC4yMjIgMC4wMDAgMS4yMzIgMC4wMDAgMC4wMDAgMC4wMDAgMS4wMDAgMC4wMDAiIC8+PC9maWx0ZXI+PC9kZWZzPjxpbWFnZSB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbHRlcj0idXJsKCNkYXJrcmVhZGVyLWltYWdlLWZpbHRlcikiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2UvcG5nO2Jhc2U2NCxpVkJPUncwS0dnb0FBQUFOU1VoRVVnQUFBRUFBQUFCQUNBTUFBQUNkdDRIc0FBQUFBWE5TUjBJQXJzNGM2UUFBQVM5UVRGUkZBQUFBLy8vL2dJQ0FWYXFxZ0lDQVptYVpWWUNBYlcyU1lJQ0FWWEdPWm1hQVZXcUFWWEdBV1dhQVZXMTVXVzk2VldxQVdHeC9WV2g3V210N1ZXeDhXbWw0VjJaOFdtZDhWV2w4VjJwOFZXZDVWMmg2V0doNFZXaDdWMmw3VldsNVZtaDZWV2Q0VldsNVZXaDRWMmQ1Vm1oNFYyWjRWMmg2VldaM1YyaDRWbWQzVjJkNVZtaDRWV2Q1VldkNFYyaDVWbVozVjJkM1ZXZDNWMlo1VldaM1ZtWjRWbVo0VldaNFZtaDVWbWQ1VldaM1ZtWjRWV2QzVm1kNFZtZDRWV2Q0Vm1kM1ZtWjRWbVo0VldkNFZXWjRWbWQ0VldaM1ZtZDRWV2QzVldaNFZtZDRWbWQ0Vm1kM1ZXZDNWbVo0VldkNFZXZDRWV1o0Vm1aM1ZtWjRWV2Q0VldaM1ZXWjNWbVo0VldkM1ZtZDRWV1ozVm1kNFZXWjNWV1o0VldkM1ZtWjRWbVozVldkNFZXWjNWbWQ0VldaM1lNS0s5QUFBQUdSMFVrNVRBQUVDQXdRRkJnY0lDUW9NRWhRVkZ4Z2FHeDhoSWlNbEp5a3FMREUyT0Q5SFNFNVJVbE5WV0ZwYlhHRmlZMlpuYTIxdmNIaDlnb1NGbEphYm5LR2txS21xcks2eHNyUzF1c0RCeE1mSnlzek8wZGJaM2Q3aDZPbnU3L0h5OWZiMyt2djgvVkpvbFVvQUFBSWFTVVJCVkZqRDdaZnBVc0l3RklYckJxSWlpRHZ1aXFpNDc0SXJpN2hBQVJVRVJCUm8zLzhaTkFrRFNWcVNheDFuR0lmejgvUitwOW5hM2lwS1IrMG4xMVlrazlkMG81NVhJTGczYXNZUzFXYWx1RDFVMHdVNmxmRWVWUmZxaUtvZEdETHk3bGN4WHh5aGhxcnA5OE1jNzBnMUpwdE5HcFc0bUdqeWNWUjJ3d1VFNi9pajN5R1pxdTBPRjVhNDlTZnI5eEdRTHJVdFR1NzB3dHEzMkN6UHk3ZnFyajdVZGNaMlZyRUp2Nzkrd1BxNzJFekErVVB1UWhpN1BzdThra1p1WmRBeXJ4U1JuYlBPSzloWHJmTWtJR21kWndQNjl5OHVtenFiSXU2MWlHY0MrcmluOG5NT3VUTkNuZ2xZNVovREdISVhoVHdUc01jSHBKQTdWQkx4VE1CMGxRczR3ZlpTUVgvZlZDQUJ5c1liald0WC9jVHVHYmMxNnNlODNhSnQ3QjZiYk1ya2VOcGp1djQwK3ROelFPa1lWY2QvRWZDQTN4Mi9DRWppOHY4ZHdHd2pwZEV1V0FCN2tHZ1ZsaUVCaHFOTXFld0JCT3lKdnBCcmdJQlZVY0FDSUtCUDhKbS83NElzSXZ0S28zUyswL3RuNTBEN1VZQnFETWdqSndzTnlPR09oYkV5dURWeHdQakJDcXBPTTE0RUQ4b1BDL0RoNGpEamJaUDJCaGFRd01VN2JJT3FBUnVNYndWd2FkWEp1bEhTSXNsYkhHVyszUHphR0p1c3NuUU1nUTh5QUM5L0lWUS9yQW1mb00xdytCL3JaVUhqdTc3eEJGUnlhdEpjMlVZdm5UTFpjWStrMWFYMTZqWWJuenNGNVZWUGl4a0dheEM4RnJLMy91R0lWV1c0RnZVS2Q4bTVHMDRYVzdINVRHVGIxZmt0YkVOOUFiOGN5SjAzdjdndkFBQUFBRWxGVGtTdVFtQ0MiIC8+PC9zdmc+' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiPjxkZWZzPjxmaWx0ZXIgaWQ9ImRhcmtyZWFkZXItaW1hZ2UtZmlsdGVyIj48ZmVDb2xvck1hdHJpeCB0eXBlPSJtYXRyaXgiIHZhbHVlcz0iMC4yMTggLTAuNzQxIC0wLjg5NCAwLjAwMCAxLjMzNSAtMC44MjYgMC4zMjIgLTAuODczIDAuMDAwIDEuMjk4IC0wLjc5OSAtMC43MzAgMC4yMjIgMC4wMDAgMS4yMzIgMC4wMDAgMC4wMDAgMC4wMDAgMS4wMDAgMC4wMDAiIC8+PC9maWx0ZXI+PC9kZWZzPjxpbWFnZSB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbHRlcj0idXJsKCNkYXJrcmVhZGVyLWltYWdlLWZpbHRlcikiIHhsaW5rOmhyZWY9ImRhdGE6aW1hZ2UvcG5nO2Jhc2U2NCxpVkJPUncwS0dnb0FBQUFOU1VoRVVnQUFBRUFBQUFCQUNBTUFBQUNkdDRIc0FBQUFBWE5TUjBJQXJzNGM2UUFBQVRoUVRGUkZBQUFBLy8vL2dJQ0FnSUNBWm1hWlZZQ0FZSUNBVlhHT1ptYUFWV3FBVzIxL1ZXWjNWWEdBWG10NVdXYUFWVzE1WFdpQVcyMS9XR3A3VldaM1ZXeDhWV3A0VjJ0NVZXbDhXV2w2VldwNldHaDRWMlo2VjJwNFZXaDdWMmw3VldkNVZXWjNXR2w1Vm1kM1YyWjRWMmw2Vm1kNVZXWjNWbWQzVldkNVYyaDZWMmg0VldkNVYyWjRWbWQ0VjJkNFZtWjNWMmQzVldkM1ZtZDVWbWg1VldaM1ZtZDRWV2QzVm1oNFZtZDVWbWg1Vm1kNFZXZDRWV2QzVm1kM1ZtZDVWV1ozVm1kNFZtWjRWbWQzVm1kNFZtZDRWbWQ0Vm1aM1ZtWjRWV2Q0VldaM1ZtZDRWV1o0Vm1kNFZXZDRWV2Q0Vm1aM1ZXZDRWV1o0VldkM1ZtWjRWV1o0VldaM1ZtZDRWbVozVldkM1ZXWjRWV1ozVldaM1ZXWjNWbWQ0VldaM1ZtWjNWV1o0VldkM1ZXWjRWbVozVldkNFZXWjNWbWQ0VldaM3BNb1NKZ0FBQUdkMFVrNVRBQUVDQkFVR0NBa0tEQTRQRWhNVUZSWWNIUjRoSkNZbkxqQXhNalUyT0RrOFBUNUdTVXBMVFZSWVcyTmthR3ByYlc5MGRuaDVmb0NEaFlhS2pZK1VscGVibnFPa3BxZXFzN1Mxd01IQ3pNM08xOWpaNE9IaTVlbnE3ZS93OGZMMDlmYjUrdnY4L1J5U0lzUUFBQUZVU1VSQlZCZ1o3Y0YzUDBKaEdBYmcyeEdSdmJlUWxTMTdaa1IyTmttb2RPN3YvdzJzOS9IamREcWQrdnU5TG1pYXBybFJ1eHg3U2NaVzZsQ2kwU2QrUzR5aEpNRXNGWE1DSlJqSjhOZjdLSW8ybU9JZnFTRVVxVHZKZjVJOUtFcEhuQmJ4RGhTaCtaNDU3bHZnV3NNMXhkb3F4VTBqWFBKZFVvU0JiWXJMR3JqaVBhYzRNSUN5Q01XNUZ5NTRUaWlPUGZoVWZrUng0a0ZCeGdIRm1SZmZLazhwRGcwVUVxYUkrYUQ0TGloMlVNQWF4WFVEZnRWZlVhekRVWWppcmhsL05OMVJoT0Jna2lMZWpuL2FIeW1ta05lNFNlVzVHeFpkejFUTWNlUVJTRk5KRFNMSFFJcEtPZ0JiL2xjcW1SSFlHTTVRZWZQRFJtZUNpaG1FcmFCSkpkR0pITlVQRk5QSVk1cml0Z3BXSVlvbDVMVkVFWUpWaE1vR0hHeFFpY0JxaXo5MjRXaVhQelpoMVpmbGw2Z0JSMGFVWDdLOXlER2ZKcmxYZ1FJcTlrbW1aMkNqZFc2eEh5NzRGMmJib0dtYXB0bjRBQjByd2EyNllRcERBQUFBQUVsRlRrU3VRbUNDIiAvPjwvc3ZnPg==' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://www.kugou.com/yy/static/images/search/search.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_tme_new.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i2.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i3.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i4.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i5.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i7.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_cmfoot_i8.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/coinsFloat/icon_coins_popup-bg.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/collect/common/dist/js/collect-2400.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/content-all.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/fonts/fonts.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://webcollects.kugou.com/v2/web/time.js?appid=1000&_t=1767356872595&_r=0.3140275292446272&sign=5e091aaa70989e17e1786bf40560397c' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/js/reportStat.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/yy/html/search.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1767356872598&mid=1c5d9125ac58e29910ade23e3c39a135&uuid=1c5d9125ac58e29910ade23e3c39a135&dfid=34fWfx1rK2Og22op9T4HJM9U&keyword=%E6%99%B4%E5%A4%A9&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=2420213294&iscorrection=1&privilege_filter=0&filter=10&token=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&appid=1014&signature=f4e28ce129a610a3586da04132c19235' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'chrome-extension://cgenfommofedogdmkmjdndijcilplkmg/content-scripts/inject-all.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://cofdbpoegempjloogbagkncekinflcnj/build/content.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://webcollects.kugou.com/v2/web/post?appid=1000&business=30032&_t=1767356873&sign=9505a2de8386d3717fadf6a676bc5a06' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; _WCMID=164b4ceb6957b87a2ffb8444; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522a%2522%253A5%252C%2522b%2522%253A%2522%25E6%2590%259C%25E7%25B4%25A2%2522%252C%2522action%2522%253A%2522index%2522%252C%2522uid%2522%253A%25222420213294%2522%252C%2522os%2522%253A%2522Mac%2522%252C%2522browser%2522%253A%2522chrome%2520143.0.0.0%2522%252C%2522flash%2522%253A%2522null%2522%252C%2522ivar4%2522%253A%2522%25E6%2599%25B4%25E5%25A4%25A9%2522%252C%2522lvt%2522%253A%25222026-01-02%252020%253A27%253A52%2522%252C%2522fo%2522%253A%2522%25E5%25A4%25B4%25E9%2583%25A8%25E5%25AF%25BC%25E8%2588%25AA%25E6%25A0%258F%2522%252C%2522o%2522%253A%2522%25E7%259B%25B4%25E6%258E%25A5%25E8%25AE%25BF%25E9%2597%25AE%2522%252C%2522ivar5%2522%253A%2522%25E6%25AD%258C%25E6%259B%25B2%2522%257D' ;
# curl 'https://searchrecommend.kugou.com/get/complex?callback=jQuery19102848953104205496_1767356871983&word=%E6%99%B4%E5%A4%A9&_=1767356871985' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356873' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://rtwebcollects.kugou.com/v2/web/post?appid=1000&business=12&_t=1767356873&sign=c7b19e8aa1c9f4bbd04c52c7614deade' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356873' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522ua%2522%253A%2522%257B%255C%2522v%255C%2522%253A%255C%2522143.0.0.0%255C%2522%252C%255C%2522type%255C%2522%253A%255C%2522chrome%255C%2522%257D%2522%252C%2522typeid%2522%253A10009%252C%2522transaction%2522%253A%2522%25E6%2599%25B4%25E5%25A4%25A9%2522%252C%2522fanxid%2522%253A%25222420213294%2522%252C%2522state%2522%253A1%252C%2522timelength%2522%253A428%257D' ;
# curl 'https://staticssl.kugou.com/common/images/pc_temp_v2/icon_splice.png?20150814' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356873' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://hm.baidu.com/hm.gif?hca=84D34B87DD623F16&cc=1&ck=1&cl=24-bit&ds=2560x1440&vl=755&ep=187363%2C16732&et=3&ja=0&ln=zh-cn&lo=0&lt=1767356464&rnd=1851620855&si=aedee6983d4cfc62f509129360d6bb3d&su=https%3A%2F%2Fwww.kugou.com%2Fsonglist%2Fgcid_3zjqldbcz1lz077%2F&v=1.3.2&lv=2&sn=8804&r=0&ww=2560&u=https%3A%2F%2Fwww.kugou.com%2Fmixsong%2Fb6kuxya6.html' \
#   -H 'Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'Accept-Language: zh-CN,zh;q=0.9' \
#   -H 'Cache-Control: no-cache' \
#   -H 'Connection: keep-alive' \
#   -b 'HMACCOUNT_BFESS=84D34B87DD623F16; H_WISE_SIDS_BFESS=63147_65592_66584_66592_66690_66806_66852_66962_67003_67042_67046_67089_67044_67108_67131_67140_67146_67152_67164_67178_67180; BAIDUID_BFESS=56578A9E53F7360E8F9F231CFEA48923:FG=1; ZFY=gscUrcX4wpH5C3R1eetT8K2SU1Ad3RaF6H:ALElA5E58:C; BDUSS_BFESS=FhMElYREdxZHlZWjUtRFdzdGp0RjNOYm41Vk12RDBaZXBrMDh0MnlWZkVPWDlwRVFBQUFBJCQAAAAAAAAAAAEAAACLFupLzfXP~szSMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMSsV2nErFdpaT; ab_sr=1.0.1_MjQyMTQxMDVjNWM4MGQzZGRmOGEyMmQxMjdkMGQ1NTk2YmYwNGIyZWUyM2ZhNDA3NzFlMTcyOWE5YjQ0ZmM5M2QyMmMxY2E1NjA1OWM3MDJmNDgxMmRhZjNkMmI2YTAxM2I1MzE1ZTExMGZlNWI1MmQ0OGM3NDQ5MzgyOGM5NTgwNDQ1NDNlZTFhMTU1N2U3ODMwNWRlYzg3YzkzNjJlOTUyMjU2MDQyM2EwNDM3MTY0MDgxYmQzNTQwNjkxY2U0' \
#   -H 'Pragma: no-cache' \
#   -H 'Referer: https://www.kugou.com/' \
#   -H 'Sec-Fetch-Dest: image' \
#   -H 'Sec-Fetch-Mode: no-cors' \
#   -H 'Sec-Fetch-Site: cross-site' \
#   -H 'Sec-Fetch-Storage-Access: active' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' ;
# curl 'https://hm.baidu.com/hm.gif?hca=84D34B87DD623F16&cc=1&ck=1&cl=24-bit&ds=2560x1440&vl=557&et=0&ja=0&ln=zh-cn&lo=0&lt=1767356464&rnd=73808130&si=aedee6983d4cfc62f509129360d6bb3d&su=https%3A%2F%2Fwww.kugou.com%2Fmixsong%2Fb6kuxya6.html&v=1.3.2&lv=2&sn=8993&r=0&ww=2560&u=https%3A%2F%2Fwww.kugou.com%2Fyy%2Fhtml%2Fsearch.html%23searchType%3Dsong%26searchKeyWord%3D%25E6%2599%25B4%25E5%25A4%25A9&tt=%E9%85%B7%E7%8B%97%E9%9F%B3%E4%B9%90%20-%20%E5%B0%B1%E6%98%AF%E6%AD%8C%E5%A4%9A' \
#   -H 'Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'Accept-Language: zh-CN,zh;q=0.9' \
#   -H 'Cache-Control: no-cache' \
#   -H 'Connection: keep-alive' \
#   -b 'HMACCOUNT_BFESS=84D34B87DD623F16; H_WISE_SIDS_BFESS=63147_65592_66584_66592_66690_66806_66852_66962_67003_67042_67046_67089_67044_67108_67131_67140_67146_67152_67164_67178_67180; BAIDUID_BFESS=56578A9E53F7360E8F9F231CFEA48923:FG=1; ZFY=gscUrcX4wpH5C3R1eetT8K2SU1Ad3RaF6H:ALElA5E58:C; BDUSS_BFESS=FhMElYREdxZHlZWjUtRFdzdGp0RjNOYm41Vk12RDBaZXBrMDh0MnlWZkVPWDlwRVFBQUFBJCQAAAAAAAAAAAEAAACLFupLzfXP~szSMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMSsV2nErFdpaT; ab_sr=1.0.1_MjQyMTQxMDVjNWM4MGQzZGRmOGEyMmQxMjdkMGQ1NTk2YmYwNGIyZWUyM2ZhNDA3NzFlMTcyOWE5YjQ0ZmM5M2QyMmMxY2E1NjA1OWM3MDJmNDgxMmRhZjNkMmI2YTAxM2I1MzE1ZTExMGZlNWI1MmQ0OGM3NDQ5MzgyOGM5NTgwNDQ1NDNlZTFhMTU1N2U3ODMwNWRlYzg3YzkzNjJlOTUyMjU2MDQyM2EwNDM3MTY0MDgxYmQzNTQwNjkxY2U0' \
#   -H 'Pragma: no-cache' \
#   -H 'Referer: https://www.kugou.com/' \
#   -H 'Sec-Fetch-Dest: image' \
#   -H 'Sec-Fetch-Mode: no-cors' \
#   -H 'Sec-Fetch-Site: cross-site' \
#   -H 'Sec-Fetch-Storage-Access: active' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' ;
# curl 'chrome-extension://jgjaeacdkonaoafenlfkkkmbaopkbilf/content.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/fonts/DM-Sans-regular.woff2' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Origin: https://www.kugou.com' \
#   -H 'Referer;' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/i18n/zh_CN.json' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/assets/logo-O35E636P.png' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/fonts/Noto-Sans-Regular.woff2' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Origin: https://www.kugou.com' \
#   -H 'Referer;' ;
# curl 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCAyOCAyOCI+PHBhdGggZmlsbD0iIzU5NTk1OSIgZD0iTTUuOTQ1IDEwLjA5MWEuNzgxLjc4MSAwIDAgMSAxLjEwNS0uMDA2bDYuNCA2LjMzNWEuNzgxLjc4MSAwIDAgMCAxLjEgMGw2LjQtNi4zMzVhLjc4MS43ODEgMCAxIDEgMS4xIDEuMTFsLTYuNDAxIDYuMzM1YTIuMzQ0IDIuMzQ0IDAgMCAxLTMuMjk4IDBsLTYuNC02LjMzNGEuNzgxLjc4MSAwIDAgMS0uMDA2LTEuMTA1WiIgY2xpcC1ydWxlPSJldmVub2RkIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGRhdGEtZm9sbG93LWZpbGw9IiM1OTU5NTkiLz48L3N2Zz4=' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iMTAiIHZpZXdCb3g9IjAgMCAxMiAxMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4gPHBhdGggZD0iTTExLjI1MDUgMS41TDQuMjUwMTYgOC41TDAuNzUgNS4wMDAxNiIgc3Ryb2tlPSJ1cmwoI3BhaW50MF9saW5lYXJfMTI4Ml84NjU5KSIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPiA8ZGVmcz4gPGxpbmVhckdyYWRpZW50IGlkPSJwYWludDBfbGluZWFyXzEyODJfODY1OSIgeDE9IjYuMDAwMjMiIHkxPSIxLjUiIHgyPSI2LjAwMDIzIiB5Mj0iOC41IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+IDxzdG9wIHN0b3AtY29sb3I9IiMyQjkwRkYiLz4gPHN0b3Agb2Zmc2V0PSIwLjU1NSIgc3RvcC1jb2xvcj0iIzAxN0FGRiIvPiA8L2xpbmVhckdyYWRpZW50PiA8L2RlZnM+IDwvc3ZnPg==' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://staticssl.kugou.com/common/js/min/hijacked-min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356873' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'



# curl 'https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=0, i' \
#   -H 'referer: https://www.kugou.com/songlist/gcid_3zjqldbcz1lz077/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: document' \
#   -H 'sec-fetch-mode: navigate' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-fetch-user: ?1' \
#   -H 'upgrade-insecure-requests: 1' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/css/play.src.css?201505211743' \
#   -H 'accept: text/css,*/*;q=0.1' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=0' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: style' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/css/cmdialog.css?20220113' \
#   -H 'accept: text/css,*/*;q=0.1' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=0' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: style' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/css/cmhead_v20.css?20220113' \
#   -H 'accept: text/css,*/*;q=0.1' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=0' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: style' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_logo_v20.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://m.kugou.com/static/js/share/npm/sentry5.6.1.min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/js/jquery.min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/js/lib.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/js/utility.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/common/js/min/login/kguser.v2.min.js?20190111' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/common/js/repalceHttpsImg.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/common/js/min/npm/getBaseInfo.min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/common/js/min/infSign.min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/verify/static/js/registerDev.v1.min.js?appid=1014&20190408' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/js/cmhead.min.js?20220119' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/js/PCToMoblie.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://imge.kugou.com/stdmusic/20251124/20251124234711666365.jpg' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/collect/common/dist/js/collect-2400.js?v=2' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/js/play/lib/play_common.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://staticssl.kugou.com/common/js-lib/min/kg-play-stat-report.es5.min.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=2' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'chrome-extension://aefehdhdciieocakfobpaaolhipkcpgc/content_scripts/copy.js' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://www.kugou.com/common/images/icon_search_white.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/common/css/cmhead_v20.css?20220113' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_arrow_down_black.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/common/css/cmhead_v20.css?20220113' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_search_white.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_arrow_down_black.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/bg_userinfo_select.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_setting_gray.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_logout.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/images/play/default.jpg' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/static/css/play.src.css?201505211743' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/images/play/downlaod_bg.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/static/css/play.src.css?201505211743' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/images/play/btn.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/static/css/play.src.css?201505211743' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/images/progress_bg_middle.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/static/css/play.src.css?201505211743' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/images/progress_bar_middle.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/static/css/play.src.css?201505211743' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/images/play/line.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/yy/static/css/play.src.css?201505211743' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/images/shbar.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/static/css/play.src.css?201505211743' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/images/play/logo.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/yy/static/css/play.src.css?201505211743' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/content-all.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/fonts/fonts.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://webcollects.kugou.com/v2/web/time.js?appid=1000&_t=1767356683586&_r=0.8088375237427767&sign=ce72f7646bb9cc28f125d4cf28321ce1' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/yy/static/js/play/playbyAudio.js?now=1767356683590' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://hm.baidu.com/hm.js?aedee6983d4cfc62f509129360d6bb3d' \
#   -H 'Accept: */*' \
#   -H 'Accept-Language: zh-CN,zh;q=0.9' \
#   -H 'Cache-Control: no-cache' \
#   -H 'Connection: keep-alive' \
#   -b 'HMACCOUNT_BFESS=84D34B87DD623F16; H_WISE_SIDS_BFESS=63147_65592_66584_66592_66690_66806_66852_66962_67003_67042_67046_67089_67044_67108_67131_67140_67146_67152_67164_67178_67180; BAIDUID_BFESS=56578A9E53F7360E8F9F231CFEA48923:FG=1; ZFY=gscUrcX4wpH5C3R1eetT8K2SU1Ad3RaF6H:ALElA5E58:C; BDUSS_BFESS=FhMElYREdxZHlZWjUtRFdzdGp0RjNOYm41Vk12RDBaZXBrMDh0MnlWZkVPWDlwRVFBQUFBJCQAAAAAAAAAAAEAAACLFupLzfXP~szSMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMSsV2nErFdpaT; ab_sr=1.0.1_MjQyMTQxMDVjNWM4MGQzZGRmOGEyMmQxMjdkMGQ1NTk2YmYwNGIyZWUyM2ZhNDA3NzFlMTcyOWE5YjQ0ZmM5M2QyMmMxY2E1NjA1OWM3MDJmNDgxMmRhZjNkMmI2YTAxM2I1MzE1ZTExMGZlNWI1MmQ0OGM3NDQ5MzgyOGM5NTgwNDQ1NDNlZTFhMTU1N2U3ODMwNWRlYzg3YzkzNjJlOTUyMjU2MDQyM2EwNDM3MTY0MDgxYmQzNTQwNjkxY2U0' \
#   -H 'Pragma: no-cache' \
#   -H 'Referer: https://www.kugou.com/' \
#   -H 'Sec-Fetch-Dest: script' \
#   -H 'Sec-Fetch-Mode: no-cors' \
#   -H 'Sec-Fetch-Site: cross-site' \
#   -H 'Sec-Fetch-Storage-Access: active' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' ;
# curl 'https://m3ws.kugou.com/static/js/common/mobilecall_3.0.js' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; musicwo17=kugou; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'chrome-extension://ibdfeimkglcmdejppabkaidpippniiob/content/windowDataMessage.js' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://gateway.kugou.com/ads.gateway/v1/search_no_focus_word?srcappid=2919&clientver=1000&clienttime=1767356684&mid=1c5d9125ac58e29910ade23e3c39a135&uuid=1767356683610&dfid=34fWfx1rK2Og22op9T4HJM9U&appid=1014&signature=d7360e750e1246120b200b34e0dc4932' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw '{"userid":"2420213294","plat":103,"m_type":0,"vip_type":0,"own_ads":{}}' ;
# curl 'https://imgessl.kugou.com/kugouicon/165//' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/qrcode4home_download.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/coinsFloat/icon_coins_popup.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/coinsFloat/coins_qrcode.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_rs_i1.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_rs_i3.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_rs_i4.png' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://webcollects.kugou.com/v2/web/post?appid=1000&business=30050&_t=1767356683&sign=877b25d5b5b6a3c5a52843e6fb71b5de' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; _WCMID=164b4ceb6957b87a2ffb8444; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522r%2522%253A%2522%25E9%2585%25B7%25E7%258B%2597%25E7%2594%25B5%25E8%2584%2591%25E7%25AB%25AF%25E5%25AE%2598%25E7%25BD%2591-%25E6%2599%25B4%25E5%25A4%25A9%2520-%2520%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6%2520-%2520hjt_hjt_%25E9%25AB%2598%25E9%259F%25B3%25E8%25B4%25A8%25E5%259C%25A8%25E7%25BA%25BF%25E8%25AF%2595%25E5%2590%25AC_%25E6%2599%25B4%25E5%25A4%25A9%2520-%2520%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6%2520-%2520hjt%25E6%25AD%258C%25E8%25AF%258D%257C%25E6%25AD%258C%25E6%259B%25B2%25E4%25B8%258B%25E8%25BD%25BD_%25E9%2585%25B7%25E7%258B%2597%25E9%259F%25B3%25E4%25B9%2590%2522%252C%2522a%2522%253A%252220537%2522%252C%2522svar1%2522%253A%2522%25E6%25AD%258C%25E6%259B%25B2%2522%252C%2522mid%2522%253A%2522%2522%252C%2522b%2522%253A%2522H5%25E6%2592%25AD%25E6%2594%25BE%25E7%25BB%259F%25E8%25AE%25A1%2522%252C%2522fo%2522%253A%2522%25E5%2585%25B6%25E4%25BB%2596%2522%252C%2522userid%2522%253A%2522%2522%252C%2522timestamp%2522%253A1767356683600%252C%2522svar2%2522%253A%2522%2522%252C%2522hash%2522%253A%2522%2522%252C%2522ft%2522%253A%2522%25E9%259F%25B3%25E9%25A2%2591%25E6%2592%25AD%25E6%2594%25BE%2522%252C%2522svar3%2522%253A%2522%2522%252C%2522fs%2522%253A%2522%25E6%2592%25AD%25E6%2594%25BE%25E5%25A4%25B1%25E8%25B4%25A5%2522%257D' ;
# curl 'https://webcollects.kugou.com/v2/web/post?appid=1000&business=30050&_t=1767356683&sign=e5641210fd435ae437aebac099b73dd3' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; _WCMID=164b4ceb6957b87a2ffb8444; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356656' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522a%2522%253A28548%252C%2522b%2522%253A%2522%25E6%259B%259D%25E5%2585%2589%2522%252C%2522r%2522%253A%2522web%25E6%2592%25AD%25E6%2594%25BE%25E9%25A1%25B5%2522%252C%2522ft%2522%253A%2522pc%2522%252C%2522userid%2522%253A%25222420213294%2522%252C%2522mid%2522%253A%25221c5d9125ac58e29910ade23e3c39a135%2522%252C%2522uuid%2522%253A%25221c5d9125ac58e29910ade23e3c39a135%2522%252C%2522fo%2522%253A%2522https%253A%252F%252Fwww.kugou.com%252Fsonglist%252Fgcid_3zjqldbcz1lz077%252F%2522%252C%2522svar1%2522%253A%2522https%253A%252F%252Fwww.kugou.com%252Fmixsong%252Fb6kuxya6.html%2522%252C%2522svar2%2522%253A%2522https%253A%252F%252Fwww.kugou.com%2522%252C%2522svar3%2522%253A%2522Mozilla%252F5.0%2520(Macintosh%253B%2520Intel%2520Mac%2520OS%2520X%252010_15_7)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F143.0.0.0%2520Safari%252F537.36%2522%252C%2522svar4%2522%253Anull%252C%2522svar5%2522%253A0%257D' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/content-all.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/fonts/fonts.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://aefehdhdciieocakfobpaaolhipkcpgc/content_scripts/copy.js' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://hm.baidu.com/hm.gif?hca=84D34B87DD623F16&cc=1&ck=1&cl=24-bit&ds=2560x1440&vl=1328&ep=26199%2C15187&et=3&ja=0&ln=zh-cn&lo=0&lt=1767356464&rnd=636961097&si=aedee6983d4cfc62f509129360d6bb3d&su=https%3A%2F%2Fwww.kugou.com%2Fsonglist%2Fgcid_3zjqldbcz1lz077%2F&v=1.3.2&lv=2&sn=8776&r=0&ww=2560&u=https%3A%2F%2Fwww.kugou.com%2Fmixsong%2Fb6kuxya6.html' \
#   -H 'Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'Accept-Language: zh-CN,zh;q=0.9' \
#   -H 'Cache-Control: no-cache' \
#   -H 'Connection: keep-alive' \
#   -b 'HMACCOUNT_BFESS=84D34B87DD623F16; H_WISE_SIDS_BFESS=63147_65592_66584_66592_66690_66806_66852_66962_67003_67042_67046_67089_67044_67108_67131_67140_67146_67152_67164_67178_67180; BAIDUID_BFESS=56578A9E53F7360E8F9F231CFEA48923:FG=1; ZFY=gscUrcX4wpH5C3R1eetT8K2SU1Ad3RaF6H:ALElA5E58:C; BDUSS_BFESS=FhMElYREdxZHlZWjUtRFdzdGp0RjNOYm41Vk12RDBaZXBrMDh0MnlWZkVPWDlwRVFBQUFBJCQAAAAAAAAAAAEAAACLFupLzfXP~szSMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMSsV2nErFdpaT; ab_sr=1.0.1_MjQyMTQxMDVjNWM4MGQzZGRmOGEyMmQxMjdkMGQ1NTk2YmYwNGIyZWUyM2ZhNDA3NzFlMTcyOWE5YjQ0ZmM5M2QyMmMxY2E1NjA1OWM3MDJmNDgxMmRhZjNkMmI2YTAxM2I1MzE1ZTExMGZlNWI1MmQ0OGM3NDQ5MzgyOGM5NTgwNDQ1NDNlZTFhMTU1N2U3ODMwNWRlYzg3YzkzNjJlOTUyMjU2MDQyM2EwNDM3MTY0MDgxYmQzNTQwNjkxY2U0' \
#   -H 'Pragma: no-cache' \
#   -H 'Referer: https://www.kugou.com/' \
#   -H 'Sec-Fetch-Dest: image' \
#   -H 'Sec-Fetch-Mode: no-cors' \
#   -H 'Sec-Fetch-Site: cross-site' \
#   -H 'Sec-Fetch-Storage-Access: active' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' ;
# curl 'https://hm.baidu.com/hm.gif?hca=84D34B87DD623F16&cc=1&ck=1&cl=24-bit&ds=2560x1440&vl=755&et=0&ja=0&ln=zh-cn&lo=0&lt=1767356464&rnd=410102353&si=aedee6983d4cfc62f509129360d6bb3d&su=https%3A%2F%2Fwww.kugou.com%2Fsonglist%2Fgcid_3zjqldbcz1lz077%2F&v=1.3.2&lv=2&sn=8804&r=0&ww=2560&u=https%3A%2F%2Fwww.kugou.com%2Fmixsong%2Fb6kuxya6.html&tt=%E6%99%B4%E5%A4%A9%20-%20%E5%91%A8%E6%9D%B0%E4%BC%A6%20-%20hjt_hjt_%E9%AB%98%E9%9F%B3%E8%B4%A8%E5%9C%A8%E7%BA%BF%E8%AF%95%E5%90%AC_%E6%99%B4%E5%A4%A9%20-%20%E5%91%A8%E6%9D%B0%E4%BC%A6%20-%20hjt%E6%AD%8C%E8%AF%8D%7C%E6%AD%8C%E6%9B%B2%E4%B8%8B%E8%BD%BD_%E9%85%B7%E7%8B%97%E9%9F%B3%E4%B9%90' \
#   -H 'Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'Accept-Language: zh-CN,zh;q=0.9' \
#   -H 'Cache-Control: no-cache' \
#   -H 'Connection: keep-alive' \
#   -b 'HMACCOUNT_BFESS=84D34B87DD623F16; H_WISE_SIDS_BFESS=63147_65592_66584_66592_66690_66806_66852_66962_67003_67042_67046_67089_67044_67108_67131_67140_67146_67152_67164_67178_67180; BAIDUID_BFESS=56578A9E53F7360E8F9F231CFEA48923:FG=1; ZFY=gscUrcX4wpH5C3R1eetT8K2SU1Ad3RaF6H:ALElA5E58:C; BDUSS_BFESS=FhMElYREdxZHlZWjUtRFdzdGp0RjNOYm41Vk12RDBaZXBrMDh0MnlWZkVPWDlwRVFBQUFBJCQAAAAAAAAAAAEAAACLFupLzfXP~szSMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMSsV2nErFdpaT; ab_sr=1.0.1_MjQyMTQxMDVjNWM4MGQzZGRmOGEyMmQxMjdkMGQ1NTk2YmYwNGIyZWUyM2ZhNDA3NzFlMTcyOWE5YjQ0ZmM5M2QyMmMxY2E1NjA1OWM3MDJmNDgxMmRhZjNkMmI2YTAxM2I1MzE1ZTExMGZlNWI1MmQ0OGM3NDQ5MzgyOGM5NTgwNDQ1NDNlZTFhMTU1N2U3ODMwNWRlYzg3YzkzNjJlOTUyMjU2MDQyM2EwNDM3MTY0MDgxYmQzNTQwNjkxY2U0' \
#   -H 'Pragma: no-cache' \
#   -H 'Referer: https://www.kugou.com/' \
#   -H 'Sec-Fetch-Dest: image' \
#   -H 'Sec-Fetch-Mode: no-cors' \
#   -H 'Sec-Fetch-Site: cross-site' \
#   -H 'Sec-Fetch-Storage-Access: active' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' ;
# curl 'https://webcollects.kugou.com/v2/web/post?appid=1000&business=30032&_t=1767356684&sign=d67a07ae1b95db4f7d0041a45abcd093' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; _WCMID=164b4ceb6957b87a2ffb8444; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522lvt%2522%253A%25222026-01-02%252020%253A24%2522%252C%2522os%2522%253A%2522Mac%2522%252C%2522browser%2522%253A%2522chrome%2522%252C%2522uid%2522%253A%25222420213294%2522%252C%2522fo%2522%253A%2522%25E6%2592%25AD%25E6%2594%25BE%25E9%25A1%25B5%2522%252C%2522ivar1%2522%253A%2522%25E6%2599%25AE%25E9%2580%259A%25E7%2589%2588%2522%252C%2522action%2522%253A%2522index%2522%252C%2522b%2522%253A%2522%25E6%2592%25AD%25E6%2594%25BE%25E9%25A1%25B5%25E8%25AE%25BF%25E9%2597%25AE%2522%252C%2522a%2522%253A2%252C%2522o%2522%253A%2522%25E7%259B%25B4%25E6%258E%25A5%25E8%25AE%25BF%25E9%2597%25AE%2522%257D' ;
# curl 'https://www.kugou.com/yy/static/images/play/paly_add.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1767356684140&mid=1c5d9125ac58e29910ade23e3c39a135&uuid=1c5d9125ac58e29910ade23e3c39a135&dfid=34fWfx1rK2Og22op9T4HJM9U&appid=1014&platid=4&encode_album_audio_id=b6kuxya6&token=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&userid=2420213294&signature=167a276f9fdafe20fc29573ee0ba53e0' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'chrome-extension://cgenfommofedogdmkmjdndijcilplkmg/content-scripts/inject-all.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://cofdbpoegempjloogbagkncekinflcnj/build/content.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://webcollects.kugou.com/v2/web/post?appid=1000&business=30050&_t=1767356684&sign=70a2b1ac65807bf98f6c0cabc12707fe' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; _WCMID=164b4ceb6957b87a2ffb8444; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522a%2522%253A1133917%252C%2522b%2522%253A%2522%25E6%259B%259D%25E5%2585%2589%2522%252C%2522r%2522%253A%2522%25E9%2587%2591%25E5%25B8%2581%25E6%25B5%25AE%25E7%25AA%2597%2522%252C%2522ft%2522%253A%2522%25E9%25A6%2596%25E9%25A1%25B5%25E9%2587%2591%25E5%25B8%2581%25E6%25B5%25AE%25E7%25AA%2597%25E4%25BA%258C%25E7%25BB%25B4%25E7%25A0%2581%2522%252C%2522userid%2522%253A%25222420213294%2522%252C%2522mid%2522%253A%25221c5d9125ac58e29910ade23e3c39a135%2522%252C%2522uuid%2522%253A%25221c5d9125ac58e29910ade23e3c39a135%2522%252C%2522ivar1%2522%253A%2522%25E6%2592%25AD%25E6%2594%25BE%25E9%25A1%25B5%2522%257D' ;
# curl 'https://webcollects.kugou.com/v2/web/post?appid=1000&business=30050&_t=1767356684&sign=3970e7f3c95738f54f82b54f41bb8980' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; _WCMID=164b4ceb6957b87a2ffb8444; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522a%2522%253A1133582%252C%2522b%2522%253A%2522%25E6%259B%259D%25E5%2585%2589%2522%252C%2522r%2522%253A%2522%25E9%2585%25B7%25E7%258B%2597%25E5%25AE%2598%25E7%25BD%2591%2522%252C%2522ft%2522%253A%2522%25E5%25AE%2598%25E7%25BD%2591%25E9%25A1%25B5%25E9%259D%25A2%25E6%259B%259D%25E5%2585%2589%2522%252C%2522userid%2522%253A%25222420213294%2522%252C%2522mid%2522%253A%25221c5d9125ac58e29910ade23e3c39a135%2522%252C%2522uuid%2522%253A%25221c5d9125ac58e29910ade23e3c39a135%2522%252C%2522svar1%2522%253A%2522%25E6%2592%25AD%25E6%2594%25BE%25E9%25A1%25B5%2522%257D' ;
# curl 'https://imgessl.kugou.com/stdmusic/480/20251124/20251124234711666365.jpg' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://fxsong.kugou.com/fxmusic/pcad/lrcV1?jsonCallBack&songName=hjt&callback=jsonphttpsfxsongkugoucomfxmusicpcadlrcV1jsonCallBacksongNamehjtcallback' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://mips.kugou.com/check/iscn?&format=jsonp&callback=jQuery19102818566838364811_1767356683132&_=1767356683133' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://webfs.kugou.com/202601022024/ca89c1c204b30891ec1f457b7b4c52d3/v3/f9b77b451f6df0bfbcb8df349e720db4/yp/full/ap1014_us0_mii0w1iw8z2ai2iphcu80ooo2ki81120_pi406_mx676178854_s700002234.mp3' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'range: bytes=0-' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: audio' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://webcollects.kugou.com/v2/web/post?appid=1000&business=30032&_t=1767356684&sign=a742e73dacb606a89aeeacddac3dcc0d' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; _WCMID=164b4ceb6957b87a2ffb8444; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522lvt%2522%253A%25222026-01-02%252020%253A24%2522%252C%2522os%2522%253A%2522Mac%2522%252C%2522browser%2522%253A%2522chrome%2522%252C%2522uid%2522%253A%25222420213294%2522%252C%2522fo%2522%253A%2522%25E5%2585%25B6%25E4%25BB%2596%2522%252C%2522ivar1%2522%253A%2522%25E9%259F%25B3%25E9%25A2%2591%2522%252C%2522action%2522%253A%2522index%2522%252C%2522a%2522%253A6%252C%2522b%2522%253A%2522%25E6%2592%25AD%25E6%2594%25BE%2522%252C%2522ivar2%2522%253A%2522%2522%252C%2522ivar3%2522%253A%2522%25E6%2599%25B4%25E5%25A4%25A9%2520-%2520%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6%2520-%2520hjt%2522%252C%2522ivar4%2522%253A%2522%257B%255C%2522album_id%255C%2522%253A104699224%252C%255C%2522recommend_album_id%255C%2522%253A104699224%257D%2522%252C%2522ivar5%2522%253A%2522web%2522%257D' ;
# curl 'https://rtwebcollects.kugou.com/v2/web/post?appid=1000&business=12&_t=1767356684&sign=5fa4ae209843263350808875fcecd7c4' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522ua%2522%253A%2522%257B%255C%2522v%255C%2522%253A%255C%2522143.0.0.0%255C%2522%252C%255C%2522type%255C%2522%253A%255C%2522chrome%255C%2522%257D%2522%252C%2522typeid%2522%253A10005%252C%2522Hash%2522%253A%2522%2522%252C%2522state%2522%253A1%252C%2522timelength%2522%253A806%252C%2522para%2522%253A436%252C%2522transaction%2522%253A%257B%2522songname%2522%253A%2522hjt%2520-%2520%25E6%2599%25B4%25E5%25A4%25A9%2520-%2520%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6%2520-%2520hjt%2522%252C%2522playsource%2522%253A%2522Jay%2522%257D%252C%2522fanxid%2522%253A%25222420213294%2522%252C%2522para2%2522%253A360%257D' ;
# curl 'chrome-extension://jgjaeacdkonaoafenlfkkkmbaopkbilf/content.css' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://www.kugou.com/favicon.ico' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/fonts/DM-Sans-regular.woff2' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Origin: https://www.kugou.com' \
#   -H 'Referer;' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/i18n/zh_CN.json' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/assets/logo-O35E636P.png' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/fonts/Noto-Sans-Regular.woff2' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Origin: https://www.kugou.com' \
#   -H 'Referer;' ;
# curl 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCAyOCAyOCI+PHBhdGggZmlsbD0iIzU5NTk1OSIgZD0iTTUuOTQ1IDEwLjA5MWEuNzgxLjc4MSAwIDAgMSAxLjEwNS0uMDA2bDYuNCA2LjMzNWEuNzgxLjc4MSAwIDAgMCAxLjEgMGw2LjQtNi4zMzVhLjc4MS43ODEgMCAxIDEgMS4xIDEuMTFsLTYuNDAxIDYuMzM1YTIuMzQ0IDIuMzQ0IDAgMCAxLTMuMjk4IDBsLTYuNC02LjMzNGEuNzgxLjc4MSAwIDAgMS0uMDA2LTEuMTA1WiIgY2xpcC1ydWxlPSJldmVub2RkIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGRhdGEtZm9sbG93LWZpbGw9IiM1OTU5NTkiLz48L3N2Zz4=' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iMTAiIHZpZXdCb3g9IjAgMCAxMiAxMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4gPHBhdGggZD0iTTExLjI1MDUgMS41TDQuMjUwMTYgOC41TDAuNzUgNS4wMDAxNiIgc3Ryb2tlPSJ1cmwoI3BhaW50MF9saW5lYXJfMTI4Ml84NjU5KSIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPiA8ZGVmcz4gPGxpbmVhckdyYWRpZW50IGlkPSJwYWludDBfbGluZWFyXzEyODJfODY1OSIgeDE9IjYuMDAwMjMiIHkxPSIxLjUiIHgyPSI2LjAwMDIzIiB5Mj0iOC41IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+IDxzdG9wIHN0b3AtY29sb3I9IiMyQjkwRkYiLz4gPHN0b3Agb2Zmc2V0PSIwLjU1NSIgc3RvcC1jb2xvcj0iIzAxN0FGRiIvPiA8L2xpbmVhckdyYWRpZW50PiA8L2RlZnM+IDwvc3ZnPg==' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb/assets/logo-O35E636P.png' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'Referer;' ;
# curl 'https://www.kugou.com/yy/static/js/jslib/base.js?1767356686&_=1767356683134' \
#   -H 'accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   -H 'x-requested-with: XMLHttpRequest' ;
# curl 'https://webcollects.kugou.com/v2/web/post?appid=1000&business=30050&_t=1767356686&sign=69c33c39c2f557f9e424e5fd4b08498c' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; _WCMID=164b4ceb6957b87a2ffb8444; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522a%2522%253A%252224585%2522%252C%2522b%2522%253A%2522%25E6%259B%259D%25E5%2585%2589%2522%252C%2522ft%2522%253A%2522%25E4%25B8%25BB%25E9%25A1%25B5%25E9%259D%25A2%2522%252C%2522r%2522%253A%2522%25E6%25AD%258C%25E6%2589%258BH5%25E9%25A1%25B5%25E9%259D%25A2%2522%252C%2522userid%2522%253A%25222420213294%2522%252C%2522mid%2522%253A%25221c5d9125ac58e29910ade23e3c39a135%2522%252C%2522svar1%2522%253A%25229286426%2522%252C%2522svar2%2522%253A%2522%25E6%2592%25AD%25E6%2594%25BE%25E9%25A1%25B5%2522%252C%2522svar3%2522%253A%2522F9B77B451F6DF0BFBCB8DF349E720DB4%2522%252C%2522hreffrom%2522%253Anull%257D' ;
# curl 'https://www.kugou.com/favicon.ico' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/mixsong/b6kuxya6.html' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://webcollects.kugou.com/v2/web/post?appid=1000&business=30050&_t=1767356693&sign=bfa3e1dfc315f7c4f8467298f39890d5' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; _WCMID=164b4ceb6957b87a2ffb8444; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522r%2522%253A%2522%25E9%2585%25B7%25E7%258B%2597%25E7%2594%25B5%25E8%2584%2591%25E7%25AB%25AF%25E5%25AE%2598%25E7%25BD%2591-%25E6%2599%25B4%25E5%25A4%25A9%2520-%2520%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6%2520-%2520hjt_hjt_%25E9%25AB%2598%25E9%259F%25B3%25E8%25B4%25A8%25E5%259C%25A8%25E7%25BA%25BF%25E8%25AF%2595%25E5%2590%25AC_%25E6%2599%25B4%25E5%25A4%25A9%2520-%2520%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6%2520-%2520hjt%25E6%25AD%258C%25E8%25AF%258D%257C%25E6%25AD%258C%25E6%259B%25B2%25E4%25B8%258B%25E8%25BD%25BD_%25E9%2585%25B7%25E7%258B%2597%25E9%259F%25B3%25E4%25B9%2590%2522%252C%2522a%2522%253A%252220537%2522%252C%2522svar1%2522%253A%2522%25E6%25AD%258C%25E6%259B%25B2%2522%252C%2522mid%2522%253A%2522%2522%252C%2522b%2522%253A%2522H5%25E6%2592%25AD%25E6%2594%25BE%25E7%25BB%259F%25E8%25AE%25A1%2522%252C%2522fo%2522%253A%2522%25E5%2585%25B6%25E4%25BB%2596%2522%252C%2522userid%2522%253A%2522%2522%252C%2522timestamp%2522%253A1767356693862%252C%2522svar2%2522%253A%2522%2522%252C%2522hash%2522%253A%2522F9B77B451F6DF0BFBCB8DF349E720DB4%2522%252C%2522ft%2522%253A%2522%25E9%259F%25B3%25E9%25A2%2591%25E6%2592%25AD%25E6%2594%25BE%2522%252C%2522svar3%2522%253A%2522%2522%252C%2522fs%2522%253A%2522%25E6%2592%25AD%25E6%2594%25BE%25E6%2588%2590%25E5%258A%259F%2522%257D' ;
# curl 'https://webcollects.kugou.com/v2/web/post?appid=1000&business=30050&_t=1767356694&sign=9245c6ee639ff408c9d10947c5d996f3' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; _WCMID=164b4ceb6957b87a2ffb8444; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'origin: https://www.kugou.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
#   --data-raw 'content=%257B%2522a%2522%253A27812%252C%2522b%2522%253A%2522%25E7%25BB%259F%25E8%25AE%25A1%2522%252C%2522r%2522%253A%2522%25E5%25AE%2598%25E7%25BD%2591%25E6%2592%25AD%25E6%2594%25BE%25E7%25BB%259F%25E8%25AE%25A1%2522%252C%2522ft%2522%253A1%252C%2522userid%2522%253A%25222420213294%2522%252C%2522mid%2522%253A%25221c5d9125ac58e29910ade23e3c39a135%2522%252C%2522uuid%2522%253A%25221c5d9125ac58e29910ade23e3c39a135%2522%252C%2522fo%2522%253A%2522https%253A%252F%252Fwww.kugou.com%252Fsonglist%252Fgcid_3zjqldbcz1lz077%252F%2522%252C%2522svar1%2522%253A%2522https%253A%252F%252Fwww.kugou.com%252Fmixsong%252Fb6kuxya6.html%2522%252C%2522svar2%2522%253A1000%252C%2522svar3%2522%253A676178854%252C%2522svar4%2522%253A0%252C%2522savr5%2522%253A%2522Mozilla%252F5.0%2520(Macintosh%253B%2520Intel%2520Mac%2520OS%2520X%252010_15_7)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F143.0.0.0%2520Safari%252F537.36%2522%257D' ;
# curl 'https://fxsong.kugou.com/fxmusic/pcad/lrcV1?jsonCallBack&songName=hjt&callback=jsonphttpsfxsongkugoucomfxmusicpcadlrcV1jsonCallBacksongNamehjtcallback' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://fxsong.kugou.com/fxmusic/pcad/lrcV1?jsonCallBack&songName=hjt&callback=jsonphttpsfxsongkugoucomfxmusicpcadlrcV1jsonCallBacksongNamehjtcallback' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_search_white.png' -H 'Referer;' ;
# curl 'https://fxsong.kugou.com/fxmusic/pcad/lrcV1?jsonCallBack&songName=hjt&callback=jsonphttpsfxsongkugoucomfxmusicpcadlrcV1jsonCallBacksongNamehjtcallback' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://fxsong.kugou.com/fxmusic/pcad/lrcV1?jsonCallBack&songName=hjt&callback=jsonphttpsfxsongkugoucomfxmusicpcadlrcV1jsonCallBacksongNamehjtcallback' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_arrow_down_white.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.kugou.com/common/css/cmhead_v20.css?20220113' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://fxsong.kugou.com/fxmusic/pcad/lrcV1?jsonCallBack&songName=hjt&callback=jsonphttpsfxsongkugoucomfxmusicpcadlrcV1jsonCallBacksongNamehjtcallback' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://www.kugou.com/common/images/icon_setting_v20.png' \
#   -H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'priority: i' \
#   -H 'referer: https://www.kugou.com/common/css/cmhead_v20.css?20220113' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: image' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://fxsong.kugou.com/fxmusic/pcad/lrcV1?jsonCallBack&songName=hjt&callback=jsonphttpsfxsongkugoucomfxmusicpcadlrcV1jsonCallBacksongNamehjtcallback' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' ;
# curl 'https://fxsong.kugou.com/fxmusic/pcad/lrcV1?jsonCallBack&songName=hjt&callback=jsonphttpsfxsongkugoucomfxmusicpcadlrcV1jsonCallBacksongNamehjtcallback' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b 'kg_mid=1c5d9125ac58e29910ade23e3c39a135; kg_dfid=34fWfx1rK2Og22op9T4HJM9U; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1767356464; HMACCOUNT=84D34B87DD623F16; kg_mid_temp=1c5d9125ac58e29910ade23e3c39a135; KuGoo=KugooID=2420213294&KugooPwd=5E81268AD18659C4A1116665346C2F00&NickName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034&Pic=&RegState=1&RegFrom=&t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33&t_ts=1767356586&t_key=&a_id=1014&ct=1767356586&UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; KugooID=2420213294; t=e7de5051cf78a6c27a2e2318c9272561bab693fd12456d46c1fb7524f710ad33; a_id=1014; UserName=%u0032%u0034%u0032%u0030%u0032%u0031%u0033%u0032%u0039%u0034; mid=1c5d9125ac58e29910ade23e3c39a135; dfid=34fWfx1rK2Og22op9T4HJM9U; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1767356684' \
#   -H 'pragma: no-cache' \
#   -H 'referer: https://www.kugou.com/' \
#   -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: script' \
#   -H 'sec-fetch-mode: no-cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'


