function(e, a) {
                    if (null == e)
                        throw Error("Illegal argument " + e);
                    var c = r.wordsToBytes(i(e, a));
                    return a && a.asBytes ? c : a && a.asString ? s.bytesToString(c) : r.bytesToHex(c)
                }



function seccore_signv2(e, r) {
    var a = window.toString
      , c = e;
    "[object Object]" === a.call(r) || "[object Array]" === a.call(r) || (void 0 === r ? "undefined" : (0,
    m._)(r)) === "object" && null !== r ? c += JSON.stringify(r) : "string" == typeof r && (c += r);
    var d = (0,
    h.Pu)([c].join(""))
      , s = (0,
    h.Pu)(e)
      , f = window.mnsv2(c, d, s)
      , l = {
        x0: u.i8,
        x1: "xhs-pc-web",
        x2: window[u.mj] || "PC",
        x3: f,
        x4: r ? void 0 === r ? "undefined" : (0,
        m._)(r) : ""
    };
    return "XYS_" + (0,
    h.xE)((0,
    h.lz)(JSON.stringify(l)))
}



