        function useShareNote(e) {
            var n, t, o, i, a = (0,
            e5.dw)(), r = (0,
            l.iH)(""), u = (0,
            w.dv)(), c = (0,
            l.Fl)(function() {
                return u.query.xsec_token
            }), getRawNoteUrl = function(n) {
                return (0,
                C.Nv)("https://www.xiaohongshu.com".concat(eI.Z.DiscoveryItemPath, "/").concat(e.noteId), (0,
                L._)((0,
                g._)({}, n), {
                    xsec_token: c.value,
                    xsec_source: "pc_share"
                }), {
                    keep: !1
                })
            };
            var s = (n = (0,
            f._)(function() {
                var n, t, o, i;
                return (0,
                h.Jh)(this, function(r) {
                    return n = (null == e ? void 0 : e.noteId) ? a.getTrackDataByNoteId(e.noteId) : {},
                    (0,
                    I.uk)(37875, (0,
                    L._)((0,
                    g._)({}, n), {
                        channelType: "note"
                    }), e.noteId),
                    t = getRawNoteUrl({
                        source: "webshare"
                    }),
                    i = (0,
                    C.Nv)("https://connect.qq.com/widget/shareqq/index.html", {
                        url: encodeURIComponent(t),
                        title: encodeURIComponent(null !== (o = null == e ? void 0 : e.title) && void 0 !== o ? o : "")
                    }, {
                        keep: !1
                    }),
                    window.open(i, "_blank"),
                    [2]
                })
            }),
            function gotoQQ() {
                return n.apply(this, arguments)
            }
            );
            var d = (t = (0,
            f._)(function() {
                var n, t, o, i;
                return (0,
                h.Jh)(this, function(r) {
                    return n = (null == e ? void 0 : e.noteId) ? a.getTrackDataByNoteId(e.noteId) : {},
                    (0,
                    I.uk)(37876, (0,
                    L._)((0,
                    g._)({}, n), {
                        channelType: "note"
                    }), e.noteId),
                    t = getRawNoteUrl({
                        source: "webshare"
                    }),
                    i = (0,
                    C.Nv)("https://service.weibo.com/share/share.php", {
                        url: encodeURIComponent(t),
                        title: encodeURIComponent(null !== (o = null == e ? void 0 : e.title) && void 0 !== o ? o : "")
                    }, {
                        keep: !1
                    }),
                    window.open(i, "_blank"),
                    [2]
                })
            }),
            function gotoWB() {
                return t.apply(this, arguments)
            }
            );
            var v = (o = (0,
            f._)(function() {
                var n, t, o, i, a, r, l;
                function getRandomInt() {
                    return Math.floor(99 * Math.random()) + 1
                }
                return (0,
                h.Jh)(this, function(u) {
                    switch (u.label) {
                    case 0:
                        return [4, Promise.all([fetchShareCode(null !== (n = null == e ? void 0 : e.noteId) && void 0 !== n ? n : "")])];
                    case 1:
                        return o = null !== (t = u.sent()[0]) && void 0 !== t ? t : "",
                        i = getRawNoteUrl({
                            source: "webshare",
                            xhsshare: "pc_web"
                        }),
                        a = "",
                        [2, a = e.title && e.title.length > 0 ? "".concat(getRandomInt(), " 【").concat(e.title, " - ").concat(null === (r = e.user) || void 0 === r ? void 0 : r.nickname, " | 小红书 - 你的生活兴趣社区】 \uD83D\uDE06 ").concat(o, " \uD83D\uDE06 ").concat(i) : "".concat(getRandomInt(), " 【 ").concat(null === (l = e.user) || void 0 === l ? void 0 : l.nickname, " | 小红书 - 你的生活兴趣社区】 \uD83D\uDE06").concat(o, " \uD83D\uDE06").concat(i)]
                    }
                })
            }),
            function getShareToken() {
                return o.apply(this, arguments)
            }
            );
            var m = (i = (0,
            f._)(function() {
                var n, t;
                return (0,
                h.Jh)(this, function(o) {
                    switch (o.label) {
                    case 0:
                        n = getRawNoteUrl({
                            type: e.type
                        }),
                        o.label = 1;
                    case 1:
                        return o.trys.push([1, 3, , 4]),
                        [4, nX.toDataURL(n, {
                            margin: 0
                        })];
                    case 2:
                        return r.value = o.sent(),
                        [3, 4];
                    case 3:
                        throw t = o.sent(),
                        (0,
                        y.Am)(t.message),
                        t;
                    case 4:
                        return [2]
                    }
                })
            }),
            function drawQrCode() {
                return i.apply(this, arguments)
            }
            );
            return (0,
            l.wF)(m),
            {
                qrCodeImgSrc: r,
                gotoQQ: s,
                gotoWB: d,
                getShareToken: v,
                copyNoteShareUrl: function(n, t) {
                    var o = (null == e ? void 0 : e.noteId) ? a.getTrackDataByNoteId(e.noteId) : {};
                    t ? (0,
                    I.sq)(51013, o) : (0,
                    I.uk)(37873, (0,
                    L._)((0,
                    g._)({}, o), {
                        channelType: "note"
                    }), e.noteId),
                    (0,
                    (0,
                    n$.h)(n, "复制成功，快去分享给好友吧", "复制未成功，请检查剪贴板权限").copyText)()
                }
            }
        }