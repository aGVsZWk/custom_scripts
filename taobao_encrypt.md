

var eS = "//" + (em.prefix ? em.prefix + "." : "") + (em.subDomain ? em.subDomain + "." : "") + em.mainDomain + "/h5/" + ep.api.toLowerCase() + "/" + ep.v.toLowerCase() + "/"
  , eC = ep.appKey || ("waptest" === em.subDomain ? "4272" : "12574478")
  , eT = (new Date).getTime()
  , eM = eE(em.token + "&" + eT + "&" + eC + "&" + ep.data)
  , eL = {
    jsv: ez,
    appKey: eC,
    t: eT,
    sign: eM
};

eM = eE(em.token + "&" + eT + "&" + eC + "&" + ep.data)


```js
eE = function(eo) {
    function eu(eo, eu) {
        return eo << eu | eo >>> 32 - eu
    }
    function ep(eo, eu) {
        var ep, em, e_, ew, eS;
        return e_ = 2147483648 & eo,
        ew = 2147483648 & eu,
        ep = 1073741824 & eo,
        em = 1073741824 & eu,
        eS = (1073741823 & eo) + (1073741823 & eu),
        ep & em ? 2147483648 ^ eS ^ e_ ^ ew : ep | em ? 1073741824 & eS ? 3221225472 ^ eS ^ e_ ^ ew : 1073741824 ^ eS ^ e_ ^ ew : eS ^ e_ ^ ew
    }
    function em(eo, eu, ep) {
        return eo & eu | ~eo & ep
    }
    function e_(eo, eu, ep) {
        return eo & ep | eu & ~ep
    }
    function ew(eo, eu, ep) {
        return eo ^ eu ^ ep
    }
    function eS(eo, eu, ep) {
        return eu ^ (eo | ~ep)
    }
    function eC(eo, e_, ew, eS, eC, eE, eT) {
        return eo = ep(eo, ep(ep(em(e_, ew, eS), eC), eT)),
        ep(eu(eo, eE), e_)
    }
    function eE(eo, em, ew, eS, eC, eE, eT) {
        return eo = ep(eo, ep(ep(e_(em, ew, eS), eC), eT)),
        ep(eu(eo, eE), em)
    }
    function eT(eo, em, e_, eS, eC, eE, eT) {
        return eo = ep(eo, ep(ep(ew(em, e_, eS), eC), eT)),
        ep(eu(eo, eE), em)
    }
    function eM(eo, em, e_, ew, eC, eE, eT) {
        return eo = ep(eo, ep(ep(eS(em, e_, ew), eC), eT)),
        ep(eu(eo, eE), em)
    }
    function eL(eo) {
        var eu, ep = "", em = "";
        for (eu = 0; 3 >= eu; eu++)
            ep += (em = "0" + (eo >>> 8 * eu & 255).toString(16)).substr(em.length - 2, 2);
        return ep
    }
    var eI, eA, eP, eO, eD, eN, eR, eF, eB, eZ = [], eY = 7, eH = 12, eW = 17, ez = 22, eU = 5, eV = 9, eQ = 14, eG = 20, eX = 4, eK = 11, eJ = 16, e$ = 23, e0 = 6, e2 = 10, e5 = 15, e8 = 21;
    for (eZ = function(eo) {
        for (var eu, ep = eo.length, em = ep + 8, e_ = (em - em % 64) / 64, ew = 16 * (e_ + 1), eS = Array(ew - 1), eC = 0, eE = 0; ep > eE; )
            eu = (eE - eE % 4) / 4,
            eC = eE % 4 * 8,
            eS[eu] = eS[eu] | eo.charCodeAt(eE) << eC,
            eE++;
        return eu = (eE - eE % 4) / 4,
        eC = eE % 4 * 8,
        eS[eu] = eS[eu] | 128 << eC,
        eS[ew - 2] = ep << 3,
        eS[ew - 1] = ep >>> 29,
        eS
    }(eo = function(eo) {
        eo = eo.replace(/\r\n/g, "\n");
        for (var eu = "", ep = 0; ep < eo.length; ep++) {
            var em = eo.charCodeAt(ep);
            128 > em ? eu += String.fromCharCode(em) : em > 127 && 2048 > em ? eu += String.fromCharCode(em >> 6 | 192) + String.fromCharCode(63 & em | 128) : eu += String.fromCharCode(em >> 12 | 224) + String.fromCharCode(em >> 6 & 63 | 128) + String.fromCharCode(63 & em | 128)
        }
        return eu
    }(eo)),
    eN = 1732584193,
    eR = 4023233417,
    eF = 2562383102,
    eB = 271733878,
    eI = 0; eI < eZ.length; eI += 16)
        eA = eN,
        eP = eR,
        eO = eF,
        eD = eB,
        eN = eC(eN, eR, eF, eB, eZ[eI + 0], eY, 3614090360),
        eB = eC(eB, eN, eR, eF, eZ[eI + 1], eH, 3905402710),
        eF = eC(eF, eB, eN, eR, eZ[eI + 2], eW, 606105819),
        eR = eC(eR, eF, eB, eN, eZ[eI + 3], ez, 3250441966),
        eN = eC(eN, eR, eF, eB, eZ[eI + 4], eY, 4118548399),
        eB = eC(eB, eN, eR, eF, eZ[eI + 5], eH, 1200080426),
        eF = eC(eF, eB, eN, eR, eZ[eI + 6], eW, 2821735955),
        eR = eC(eR, eF, eB, eN, eZ[eI + 7], ez, 4249261313),
        eN = eC(eN, eR, eF, eB, eZ[eI + 8], eY, 1770035416),
        eB = eC(eB, eN, eR, eF, eZ[eI + 9], eH, 2336552879),
        eF = eC(eF, eB, eN, eR, eZ[eI + 10], eW, 4294925233),
        eR = eC(eR, eF, eB, eN, eZ[eI + 11], ez, 2304563134),
        eN = eC(eN, eR, eF, eB, eZ[eI + 12], eY, 1804603682),
        eB = eC(eB, eN, eR, eF, eZ[eI + 13], eH, 4254626195),
        eF = eC(eF, eB, eN, eR, eZ[eI + 14], eW, 2792965006),
        eR = eC(eR, eF, eB, eN, eZ[eI + 15], ez, 1236535329),
        eN = eE(eN, eR, eF, eB, eZ[eI + 1], eU, 4129170786),
        eB = eE(eB, eN, eR, eF, eZ[eI + 6], eV, 3225465664),
        eF = eE(eF, eB, eN, eR, eZ[eI + 11], eQ, 643717713),
        eR = eE(eR, eF, eB, eN, eZ[eI + 0], eG, 3921069994),
        eN = eE(eN, eR, eF, eB, eZ[eI + 5], eU, 3593408605),
        eB = eE(eB, eN, eR, eF, eZ[eI + 10], eV, 38016083),
        eF = eE(eF, eB, eN, eR, eZ[eI + 15], eQ, 3634488961),
        eR = eE(eR, eF, eB, eN, eZ[eI + 4], eG, 3889429448),
        eN = eE(eN, eR, eF, eB, eZ[eI + 9], eU, 568446438),
        eB = eE(eB, eN, eR, eF, eZ[eI + 14], eV, 3275163606),
        eF = eE(eF, eB, eN, eR, eZ[eI + 3], eQ, 4107603335),
        eR = eE(eR, eF, eB, eN, eZ[eI + 8], eG, 1163531501),
        eN = eE(eN, eR, eF, eB, eZ[eI + 13], eU, 2850285829),
        eB = eE(eB, eN, eR, eF, eZ[eI + 2], eV, 4243563512),
        eF = eE(eF, eB, eN, eR, eZ[eI + 7], eQ, 1735328473),
        eR = eE(eR, eF, eB, eN, eZ[eI + 12], eG, 2368359562),
        eN = eT(eN, eR, eF, eB, eZ[eI + 5], eX, 4294588738),
        eB = eT(eB, eN, eR, eF, eZ[eI + 8], eK, 2272392833),
        eF = eT(eF, eB, eN, eR, eZ[eI + 11], eJ, 1839030562),
        eR = eT(eR, eF, eB, eN, eZ[eI + 14], e$, 4259657740),
        eN = eT(eN, eR, eF, eB, eZ[eI + 1], eX, 2763975236),
        eB = eT(eB, eN, eR, eF, eZ[eI + 4], eK, 1272893353),
        eF = eT(eF, eB, eN, eR, eZ[eI + 7], eJ, 4139469664),
        eR = eT(eR, eF, eB, eN, eZ[eI + 10], e$, 3200236656),
        eN = eT(eN, eR, eF, eB, eZ[eI + 13], eX, 681279174),
        eB = eT(eB, eN, eR, eF, eZ[eI + 0], eK, 3936430074),
        eF = eT(eF, eB, eN, eR, eZ[eI + 3], eJ, 3572445317),
        eR = eT(eR, eF, eB, eN, eZ[eI + 6], e$, 76029189),
        eN = eT(eN, eR, eF, eB, eZ[eI + 9], eX, 3654602809),
        eB = eT(eB, eN, eR, eF, eZ[eI + 12], eK, 3873151461),
        eF = eT(eF, eB, eN, eR, eZ[eI + 15], eJ, 530742520),
        eR = eT(eR, eF, eB, eN, eZ[eI + 2], e$, 3299628645),
        eN = eM(eN, eR, eF, eB, eZ[eI + 0], e0, 4096336452),
        eB = eM(eB, eN, eR, eF, eZ[eI + 7], e2, 1126891415),
        eF = eM(eF, eB, eN, eR, eZ[eI + 14], e5, 2878612391),
        eR = eM(eR, eF, eB, eN, eZ[eI + 5], e8, 4237533241),
        eN = eM(eN, eR, eF, eB, eZ[eI + 12], e0, 1700485571),
        eB = eM(eB, eN, eR, eF, eZ[eI + 3], e2, 2399980690),
        eF = eM(eF, eB, eN, eR, eZ[eI + 10], e5, 4293915773),
        eR = eM(eR, eF, eB, eN, eZ[eI + 1], e8, 2240044497),
        eN = eM(eN, eR, eF, eB, eZ[eI + 8], e0, 1873313359),
        eB = eM(eB, eN, eR, eF, eZ[eI + 15], e2, 4264355552),
        eF = eM(eF, eB, eN, eR, eZ[eI + 6], e5, 2734768916),
        eR = eM(eR, eF, eB, eN, eZ[eI + 13], e8, 1309151649),
        eN = eM(eN, eR, eF, eB, eZ[eI + 4], e0, 4149444226),
        eB = eM(eB, eN, eR, eF, eZ[eI + 11], e2, 3174756917),
        eF = eM(eF, eB, eN, eR, eZ[eI + 2], e5, 718787259),
        eR = eM(eR, eF, eB, eN, eZ[eI + 9], e8, 3951481745),
        eN = ep(eN, eA),
        eR = ep(eR, eP),
        eF = ep(eF, eO),
        eB = ep(eB, eD);
    return (eL(eN) + eL(eR) + eL(eF) + eL(eB)).toLowerCase()
}
```


hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _uetvid=92934100122a11f0b8691788df53f4da; cna=tU3xIBs7LEYBASQIhOFUwexK; miid=5053485135987502608; t=62e22151b58a0d3245d9e82c477cd1fb; xlly_s=1; mtop_partitioned_detect=1; 
_m_h5_tk=5430919098ab09c9169817736915e3bd_1767343742006; 
_m_h5_tk_enc=45fbe8e1fd034ac63e651148ccc9446c; cookie2=1c6f3a314dfc504f24501e94cf97d840; _tb_token_=803b6e4e1e1b; sca=2d2d21a2; _samesite_flag_=true; 3PcFlag=1767334390247; sgcookie=E100zeTriUGhXBmRHnyA1e9TT1GUh1xcjPaPsChvvs5Irz%2BndPzQtmBeXN4xcqnmYF9g1Nqpj%2BWHu5S6VqXIaWM1CtYcOjfGawNmygjofBjL8RVZXIYSqjWueHIP4SUY6cwl; wk_cookie2=174e059652abf947e65abfdc3ac79c21; wk_unb=UoYenbpK0tDNlQ%3D%3D; unb=1708738501; uc1=cookie21=VT5L2FSpde4B3ovLtqW%2FuQ%3D%3D&existShop=false&cookie15=UtASsssmOIJ0bQ%3D%3D&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&pas=0&cookie14=UoYY5M2uIBaaLg%3D%3D; uc3=id2=UoYenbpK0tDNlQ%3D%3D&vt3=F8dD2kak3jwE44P7Qik%3D&nk2=F5QBWjue9Nk%3D&lg2=UtASsssmOIJ0bQ%3D%3D; csg=23174fbb; lgc=tbtb8924; cancelledSubSites=empty; cookie17=UoYenbpK0tDNlQ%3D%3D; dnk=tbtb8924; skt=75f29462e9db6e91; existShop=MTc2NzMzNDQzNg%3D%3D; uc4=nk4=0%40FY5KTDyWnHT%2Bs9YQZt7EfBliVg%3D%3D&id4=0%40UO6XfIpzuXHzKit%2BpvXsromxkFJm; tracknick=tbtb8924; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=41a; _nk_=tbtb8924; cookie1=ACO2nvQqzNr%2FBl3EE%2BfglwIzn8JdlJIxAON%2FssBBmkw%3D; tfstk=gr-ZLNYJUiAIXockULjqYVZxJcsOdilSbn1fnKvcC1fG1KXc0BAjB19m6I-VtKLsBZGT3RKeaoZs6Vp00ismNbiSVd3ODic5flBJ3PBlQSmbSNjOxN2KdDiSVdpTCODWK0T_OtzOErqDiNfHKTfhIrXcmv7hFtj0jZqg-WfdnijcoOjHKtBGIlq0jvJh9tjciIbiLwfdnifDiicB1a_qat_ipgJPgOmma95kI6r0q8BNSk9aloZXAO7wIuf3mx-FQN5kQ308FAW2r379ZXa1sU8JaTOsxlRyIC8lrhVnTipBzIWyjY4PgCpHfwxihzBdDFYljnlzspAw6hLkIXaFLev6Ywtoao79-CLRunGI2GTWFnQkjcPROaB2aGYEtlRl43NAKfMeDFP0uNXdL_MELbmVSpbuYRB_krQT_95SIE4YkNbNL_MELrUAWDBFNA8V.; isg=BGFhXdbDrGcL2w6dpvb5PFuwcCt7DtUArKx5V8M2XGjHKoH8C1wB0BLsjV6s3204
