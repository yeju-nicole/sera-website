# -*- coding: utf-8 -*-
"""Builds the bilingual SERA site.

python3 build.py <out_dir>
  writes <out_dir>/index.html      full standalone page for hosting / embedding
  writes <out_dir>/preview.html    the same page without the document wrapper
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import *  # noqa: F401,F403
from sections import build_sections

SDX = "https://www.sdxfoundation.org"
CIRCLED = "①②③④⑤⑥⑦⑧⑨"
SHADE = {"S": "s", "E": "e", "R": "r", "A": "a", "SERA": "all"}
NAME = {"S": "Story", "E": "Empathy", "R": "Resilience", "A": "Achievement", "SERA": "S·E·R·A"}


def e(s):
    return html.escape(s, quote=False)


def L(t, tag="span", cls="", attrs=""):
    """Both languages of one text, as two sibling elements."""
    ko, en = t
    c = (" " + cls) if cls else ""
    a = (" " + attrs) if attrs else ""
    return (f'<{tag} class="l-ko{c}" lang="ko"{a}>{e(ko)}</{tag}>'
            f'<{tag} class="l-en{c}" lang="en"{a}>{e(en)}</{tag}>')


def first_sentence(t):
    ko, en = t
    m = re.search(r"^(.+?다\.)\s", ko + " ")
    n = re.search(r"^(.+?\.)\s", en + " ")
    return (m.group(1) if m else ko, n.group(1) if n else en)


def blocks(body):
    out = []
    for kind, val in body:
        if kind == "p":
            out.append(L(val, "p"))
        elif kind == "h":
            out.append(L(val, "h4", "blk-h"))
        elif kind in ("ul", "ol"):
            items = "".join(f"<li>{L(i)}</li>" for i in val)
            out.append(f"<{kind}>{items}</{kind}>")
        elif kind == "cl":
            items = "".join(f'<li><span class="cnum" aria-hidden="true">{CIRCLED[n]}</span><span>{L(i)}</span></li>'
                            for n, i in enumerate(val))
            out.append(f'<ol class="clauses">{items}</ol>')
    return "".join(out)


def article(prefix, num, title, body):
    no = (f"제{num}조", f"Article {num}")
    return (f'<article class="art" id="{prefix}-{num}"><header class="art-head">'
            f'{L(no, "span", "art-no")}{L(title, "h3", "art-title")}</header>'
            f'<div class="art-body">{blocks(body)}</div></article>')


def toc(prefix, chapters, extra=()):
    out = []
    for ch in chapters:
        links = "".join(f'<li><a href="#{prefix}-{n}"><span class="toc-n">{n}</span>{L(t)}</a></li>'
                        for n, t, _ in ch["articles"])
        out.append(f'<li class="toc-ch"><span class="toc-ch-label">{L(ch["label"])} · {L(ch["title"])}</span><ol>{links}</ol></li>')
    for href, t in extra:
        out.append(f'<li class="toc-ch"><a class="toc-extra" href="#{href}">{L(t)}</a></li>')
    return f'<ol class="toc">{"".join(out)}</ol>'


def chapters(prefix, chs):
    out = []
    for ch in chs:
        intro = L(ch["intro"], "p", "ch-intro") if ch.get("intro") else ""
        arts = "".join(article(prefix, n, t, b) for n, t, b in ch["articles"])
        out.append(f'<section class="chapter"><h2 class="ch-title">{L(ch["label"], "span", "ch-label")}{L(ch["title"])}</h2>{intro}{arts}</section>')
    return "".join(out)


# ------------------------------------------------------------------ pieces
def mark(size=28):
    # four dots in four shades, small to large: the ripening motif
    return (f'<svg class="mark" width="{size}" height="{size}" viewBox="0 0 32 32" aria-hidden="true">'
            '<circle cx="9" cy="9" r="4.2" fill="var(--s)"/><circle cx="23" cy="9" r="5" fill="var(--e)"/>'
            '<circle cx="9" cy="23" r="5.8" fill="var(--r)"/><circle cx="23" cy="23" r="6.6" fill="var(--a)"/></svg>')


NAV = [
    ("about", ("소개", "About")),
    ("four", ("S·E·R·A", "S·E·R·A")),
    ("way", ("SERA Way", "SERA Way")),
    ("promises", ("약속", "Promises")),
    ("records", ("기록", "Records")),
    ("together", ("함께하기", "Get involved")),
    ("salimist", ("살림가", "Salimist")),
]


def header():
    links = "".join(f'<a href="#{h}" data-nav="{h}">{L(t)}</a>' for h, t in NAV)
    return f'''
<div class="sdxbar"><div class="wrap sdxbar-in">
  <span>{L(("SDX재단이 만들어 가는 성장 프레임워크", "A growth framework from SDX Foundation"))}</span>
  <a href="{SDX}/" target="_top" rel="noopener">{L(("SDX재단 홈페이지", "SDX Foundation home"))} <span aria-hidden="true">↗</span></a>
</div></div>
<header class="site"><div class="wrap site-in">
  <a class="brand" href="#home" aria-label="SERA home">{mark()}<span class="brand-word">SERA</span><span class="brand-by">by SDX Foundation</span></a>
  <nav class="nav" id="nav" aria-label="Main">{links}</nav>
  <div class="tools">
    <div class="lang" role="group" aria-label="Language / 언어">
      <button type="button" id="lang-ko" data-lang-btn="ko" aria-pressed="true">한국어</button>
      <button type="button" id="lang-en" data-lang-btn="en" aria-pressed="false">EN</button>
    </div>
    <button type="button" class="menu-btn" id="menu-btn" aria-controls="nav" aria-expanded="false">
      <span class="sr">Menu</span><svg width="22" height="22" viewBox="0 0 22 22" aria-hidden="true"><path d="M3 6h16M3 11h16M3 16h16" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
    </button>
  </div>
</div></header>'''


def footer():
    return f'''
<footer class="foot"><div class="wrap foot-in">
  <div class="foot-brand">{mark(34)}<div><p class="foot-word">SERA</p>{L(("SDX재단(Sustainable Development eXperience Foundation)의 성장 동반자", "A growth companion from SDX Foundation (Sustainable Development eXperience Foundation)"), "p")}</div></div>
  <nav class="foot-links" aria-label="SDX Foundation">
    <p class="foot-h">{L(("SDX재단", "SDX Foundation"))}</p>
    <a href="{SDX}/" target="_top" rel="noopener">{L(("홈", "Home"))}</a>
    <a href="{SDX}/16" target="_top" rel="noopener">{L(("재단 소개", "About"))}</a>
    <a href="{SDX}/21" target="_top" rel="noopener">{L(("GX · SX · DX 전환", "GX · SX · DX Themes"))}</a>
    <a href="{SDX}/36" target="_top" rel="noopener">{L(("후원", "Sponsor"))}</a>
    <a href="{SDX}/33" target="_top" rel="noopener">{L(("문의", "Contact"))}</a>
  </nav>
  <div class="foot-contact">
    <p class="foot-h">{L(("연락처", "Contact"))}</p>
    {L(("(13488) 경기도 성남시 분당구 판교로289번길 20, 경기스타트업캠퍼스 3동 4층", "4F, Bldg. 3, Gyeonggi Startup Campus, 20 Pangyo-ro 289beon-gil, Bundang-gu, Seongnam-si, Gyeonggi-do 13488, Korea"), "p")}
    <p class="mail">sdx@sdxfoundation.org</p>
  </div>
</div>
<div class="wrap foot-base"><span>Copyright © 2026 SDX Foundation. All rights reserved.</span><a href="#home">{L(("맨 위로", "Back to top"))} ↑</a></div>
</footer>'''


CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site.css"), encoding="utf-8").read()
JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site.js"), encoding="utf-8").read()
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=IBM+Plex+Sans+KR:wght@300;400;500;600&family=Noto+Serif+KR:wght@400;500;600&display=swap">')


def body():
    return (header()
            + '<main id="top"><div class="view active" id="home">'
            + build_sections(L, e, mark)
            + '</div></main>' + footer())


def main(out):
    os.makedirs(out, exist_ok=True)
    head = (f'<title>SERA · SDX Foundation</title>'
            '<meta name="claude:viewport-fit-sides" content="cover">' + FONTS + f"<style>{CSS}</style>")
    tail = f"<script>{JS}</script>"
    b = body()
    with open(os.path.join(out, "preview.html"), "w", encoding="utf-8") as fh:
        fh.write(head + b + tail)
    fav = ("data:image/svg+xml," + "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Ccircle cx='9' cy='9' r='4.2' fill='%23B79CE0'/%3E%3Ccircle cx='23' cy='9' r='5' fill='%239370CC'/%3E"
           "%3Ccircle cx='9' cy='23' r='5.8' fill='%237048AE'/%3E%3Ccircle cx='23' cy='23' r='6.6' fill='%234E2A85'/%3E%3C/svg%3E")
    full = f'''<!doctype html>
<html lang="ko" data-lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>SERA · SDX Foundation</title>
<meta name="description" content="SERA는 Story, Empathy, Resilience, Achievement를 바탕으로 한 SDX재단의 성장 프레임워크입니다. SERA is SDX Foundation's growth framework built on Story, Empathy, Resilience and Achievement.">
<meta property="og:title" content="SERA · SDX Foundation">
<meta property="og:description" content="자기주도적 삶을 안내하는 성장 동반자. 나를 발견하고, 함께 성장하며, 나의 삶을 이루다.">
<meta property="og:type" content="website">
<meta name="theme-color" content="#4E2A85">
<link rel="icon" href="{fav}">
{FONTS}
<style>{CSS}</style>
</head>
<body>
{b}
<script>{JS}</script>
</body>
</html>
'''
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(full)


if __name__ == "__main__":
    main(sys.argv[1])
