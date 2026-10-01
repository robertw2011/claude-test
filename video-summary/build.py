# -*- coding: utf-8 -*-
"""生成 video-summary/index.html。内容数据在 data.py，截图在 img/。"""
import html, os
from data import META, PARTS, CHAPTERS, TAKEAWAYS, GLOSSARY

VID = "mpALXah_PBg"


def secs(ts):
    p = [int(x) for x in ts.split(":")]
    while len(p) < 3:
        p.insert(0, 0)
    return p[0] * 3600 + p[1] * 60 + p[2]


def fmt(s):
    h, m, sec = s // 3600, s % 3600 // 60, s % 60
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m:02d}:{sec:02d}"


def yt(s):
    return f"https://youtu.be/{VID}?t={s}"


def dur(a, b):
    m = (b - a) // 60
    return f"{m // 60} 小时 {m % 60} 分" if m >= 60 else f"{m} 分钟"


starts = [secs(c["start"]) for c in CHAPTERS] + [META["duration"]]

toc = []
body = []
for pi, part in enumerate(PARTS):
    toc.append(f'<li class="toc-part">{html.escape(part["name"])}</li>')
    body.append(
        f'<section class="part" id="part-{pi + 1}"><div class="part-head">'
        f'<span class="part-no">第 {pi + 1} 部分</span>'
        f'<h2>{html.escape(part["name"])}</h2>'
        f'<p>{part["blurb"]}</p></div>'
    )
    for c in [c for c in CHAPTERS if c["part"] == pi]:
        i = CHAPTERS.index(c)
        s, e = starts[i], starts[i + 1]
        cid = f"ch{i + 1}"
        toc.append(
            f'<li><a href="#{cid}"><span class="toc-t">{fmt(s)}</span>'
            f'<span class="toc-n">{i + 1}. {html.escape(c["cn"])}</span></a></li>'
        )
        secs_html = []
        for h, items in c["sections"]:
            lis = "".join(f"<li>{it}</li>" for it in items)
            secs_html.append(f'<div class="block"><h4>{h}</h4><ul>{lis}</ul></div>')
        figs = []
        for ts, cap in c["imgs"]:
            t = secs(ts)
            figs.append(
                f'<figure><a href="{yt(t)}" target="_blank" rel="noopener" '
                f'aria-label="在 YouTube 打开 {fmt(t)}">'
                f'<img src="img/t{t:05d}.jpg" width="320" height="180" loading="lazy" '
                f'alt="{html.escape(cap)}"></a>'
                f'<figcaption><a class="ts" href="{yt(t)}" target="_blank" rel="noopener">{fmt(t)}</a> '
                f'{html.escape(cap)}</figcaption></figure>'
            )
        terms = ""
        if c.get("terms"):
            terms = '<p class="terms"><span>关键术语</span>' + "".join(
                f'<em lang="en">{html.escape(t)}</em>' for t in c["terms"]
            ) + "</p>"
        body.append(
            f'<article class="chapter" id="{cid}">'
            f'<header><div class="ch-meta"><span class="ch-no">{i + 1:02d}</span>'
            f'<a class="ts big" href="{yt(s)}" target="_blank" rel="noopener">▶ {fmt(s)}</a>'
            f'<span class="ch-dur">{dur(s, e)}</span></div>'
            f'<h3>{html.escape(c["cn"])} <small lang="en">{html.escape(c["en"])}</small></h3>'
            f'<p class="lede">{c["lede"]}</p></header>'
            f'<div class="figs">{"".join(figs)}</div>'
            f'{"".join(secs_html)}{terms}</article>'
        )
    body.append("</section>")

takeaways = "".join(
    f"<li><b>{html.escape(t)}</b><span>{d}</span></li>" for t, d in TAKEAWAYS
)
gloss = "".join(
    f'<tr><td lang="en">{html.escape(en)}</td><td>{html.escape(cn)}</td><td>{d}</td></tr>'
    for en, cn, d in GLOSSARY
)
parts_overview = "".join(
    f'<li><a href="#part-{i + 1}"><b>{i + 1}</b><span>{html.escape(p["name"])}</span>'
    f'<small>{p["range"]}</small></a></li>'
    for i, p in enumerate(PARTS)
)

tpl = open(os.path.join(os.path.dirname(__file__), "template.html"), encoding="utf-8").read()
out = (
    tpl.replace("{{TOC}}", "".join(toc))
    .replace("{{BODY}}", "".join(body))
    .replace("{{TAKEAWAYS}}", takeaways)
    .replace("{{GLOSSARY}}", gloss)
    .replace("{{PARTS}}", parts_overview)
    .replace("{{YT}}", f"https://youtu.be/{VID}")
)
open(os.path.join(os.path.dirname(__file__), "index.html"), "w", encoding="utf-8").write(out)
print("ok", len(out))
