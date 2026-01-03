    function getSigCount(e) {
        var r = Number(sessionStorage.getItem(u.DY)) || 0;
        return e && (r++,
        sessionStorage.setItem(u.DY, r.toString())),
        r
    }

function xsCommon(e, r) {
            var a, c;
            try {
                var d = e.platform
                  , l = r.url;
                if (u.yl.map(function(e) {
                    return new RegExp(e)
                }).some(function(e) {
                    return e.test(l)
                }),
                !(0,
                f.hF)(l))
                    return r;
                var _ = ""
                  , b = ""
                  , x = r.headers["X-Sign"] || ""
                  , p = _ && b || x
                  , v = getSigCount(p)
                  , g = localStorage.getItem(u.q2)
                  , m = localStorage.getItem(u.z7) || u.fI
                  , y = {
                    s0: (0,
                    f.SW)(d),
                    s1: "",
                    x0: m,
                    x1: u.i8,
                    x2: d || "PC",
                    x3: "xhs-pc-web",
                    x4: "5.4.0",
                    x5: s.Z.get(u.o4),
                    x6: _,
                    x7: b,
                    x8: g,
                    x9: (0,
                    h.tb)("".concat(_).concat(b).concat(g)),
                    x10: v,
                    x11: "normal"
                }
                  , E = u.LN.map(function(e) {
                    return new RegExp(e)
                }).some(function(e) {
                    return e.test(l)
                });
                (null === (a = window.xhsFingerprintV3) || void 0 === a ? void 0 : a.getCurMiniUa) && E ? null === (c = window.xhsFingerprintV3) || void 0 === c || c.getCurMiniUa(function(e) {
                    y.x8 = e,
                    y.x9 = (0,
                    h.tb)("".concat(_).concat(b).concat(e)),
                    r.headers["X-S-Common"] = (0,
                    h.xE)((0,
                    h.lz)(JSON.stringify(y)))
                }) : r.headers["X-S-Common"] = (0,
                h.xE)((0,
                h.lz)(JSON.stringify(y)))
            } catch (e) {}
            return r
        }