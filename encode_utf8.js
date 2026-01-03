for (var c = [], d = "ZmserbBoHQtNP+wOcza/LpngG8yJq42KWYj0DSfdikx3VT16IlUAFM97hECvuRX5", s = 0, f = d.length; s < f; ++s)
    c[s] = d[s];
function tripletToBase64(e) {
    return c[e >> 18 & 63] + c[e >> 12 & 63] + c[e >> 6 & 63] + c[63 & e]
}

function encodeChunk(e, r, a) {
    for (var c, d = [], s = r; s < a; s += 3)
        c = (e[s] << 16 & 0xff0000) + (e[s + 1] << 8 & 65280) + (255 & e[s + 2]),
        d.push(tripletToBase64(c));
    return d.join("")
}

function b64Encode(e) {
    for (var r, a = e.length, d = a % 3, s = [], f = 16383, u = 0, l = a - d; u < l; u += f)
        s.push(encodeChunk(e, u, u + f > l ? l : u + f));
    return 1 === d ? (r = e[a - 1],
    s.push(c[r >> 2] + c[r << 4 & 63] + "==")) : 2 === d && (r = (e[a - 2] << 8) + e[a - 1],
    s.push(c[r >> 10] + c[r >> 4 & 63] + c[r << 2 & 63] + "=")),
    s.join("")
}

function encodeUtf8(e) {
    for (var r = encodeURIComponent(e), a = [], c = 0; c < r.length; c++) {
        var d = r.charAt(c);
        if ("%" === d) {
            var s = parseInt(r.charAt(c + 1) + r.charAt(c + 2), 16);
            a.push(s),
            c += 2
        } else
            a.push(d.charCodeAt(0))
    }
    return a
}

function seccore_signv2(e, r) {
    l = {
    "x0": "4.3.0",
    "x1": "xhs-pc-web",
    "x2": "Mac OS",
    "x3": "mns0301_goaKqP2qZsWVDJj+Dt0id1TMpiifR85Vv7jxYidI2j517I4dBl16NOnRTy/QypUZt8vZbViD1AnNyQH4ePH5PzAVvoepLT70FhF7LE4VoAWR4OwL+qVU0JHKXS08L8WC5+MCnpsRzRJPUaT3l14KSndVZlciE0JRIk0OHNRRTawNMeuoYzN4",
    "x4": ""
}

    return "XYS_" + b64Encode(encodeUtf8(JSON.stringify(l)))
}






c = '/api/sns/web/v1/search/filter?keyword=%E8%A7%A3%E5%8E%8B%E7%8E%A9%E5%85%B7&search_id=2fsudkot3vhhx5lijvnt7'
r = {
    "keyword": "解压玩具",
    "search_id": "2fsu9c9fre6waume3orh3",
    "biz_type": "web_search_user",
    "request_id": "549305242-1767371625353"
}

var d = md5([c].join(""))
var s = md5(c)

f = window.mnsv2(c, d, s)

console.log(d)
console.log(s)