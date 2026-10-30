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
from content import (CHARTER, CHARTER_ADDENDA, CHARTER_META, CHARTER_PREAMBLE, CYCLE,
                     DECLARATION, DECLARATION_CLOSE, FOUR, GLOSSARY, GLOSSARY_INTRO,
                     P_META, PRINCIPLES)

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
    ("seraship", ("SERAship", "SERAship")),
    ("records", ("기록", "Records")),
    ("charter", ("기본헌장", "Charter")),
    ("principles", ("기본원칙", "Principles")),
]


def header():
    links = "".join(f'<a href="#{h}" data-nav="{h}">{L(t)}</a>' for h, t in NAV)
    return f'''
<div class="sdxbar"><div class="wrap sdxbar-in">
  <span>{L(("SDX재단이 연구하고 확산하는 성장 프레임워크", "A growth framework researched and shared by SDX Foundation"))}</span>
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


def hero():
    letters = "".join(
        f'<li class="hl hl-{f["key"].lower()}"><span class="hl-letter">{f["key"]}</span>'
        f'<span class="hl-name">{f["name"]}</span>{L((f["charter"][0].split(" — ")[1], f["charter"][1].split(": ")[1]), "span", "hl-line")}</li>'
        for f in FOUR)
    return f'''
<section class="hero"><div class="wrap">
  <p class="eyebrow">Story · Empathy · Resilience · Achievement</p>
  <h1 class="hero-title">{L(("자신을 이해하고, 서로를 공감하며, 함께 영글어 가는 삶", "Understand yourself, empathize with one another, ripen together"))}</h1>
  {L(CHARTER[0]["articles"][1][2][0][1], "p", "hero-lede")}
  <div class="cta">
    <a class="btn btn-solid" href="#charter">{L(("기본헌장 읽기", "Read the Charter"))}</a>
    <a class="btn btn-line" href="#principles">{L(("기본원칙 읽기", "Read the Principles"))}</a>
  </div>
  <ol class="hero-letters" aria-label="SERA">{letters}</ol>
  <p class="ripen-note">{L(("영글다", "yeonggeulda (영글다)"), "b")} {L(("곡식이나 열매가 알이 차서 단단하게 익다. SERA의 네 가지 보랏빛은 옅은 꽃빛에서 무르익은 열매빛까지, 각자의 속도로 영글어 가는 과정을 담았습니다.", "to ripen, as grain fills out and fruit matures. SERA's four shades of purple run from pale blossom to ripe fruit, for growth that happens at each person's own pace."))}</p>
</div></section>'''


def about():
    art1 = PRINCIPLES[0]["articles"][0][2]
    purposes = PRINCIPLES[0]["articles"][1][2][0][1]
    keys = ["S", "E", "R", "A"]
    plist = "".join(
        f'<li class="purpose"><span class="chip chip-{SHADE[k]}">{k}</span>'
        f'<div>{L((p[0].split(": ")[0], p[1].split(": ")[0]), "strong")}{L((p[0].split(": ", 1)[1], p[1].split(": ", 1)[1][:1].upper() + p[1].split(": ", 1)[1][1:]), "p")}</div></li>'
        for k, p in zip(keys, purposes))
    person = PRINCIPLES[0]["articles"][2][2]
    traits = "".join(f"<li>{L(t)}</li>" for t in person[1][1])
    return f'''
<section class="sec" id="about"><div class="wrap">
  <div class="sec-head"><p class="kicker">{L(("SERA란", "What SERA is"))}</p>
  <h2>{L(("스스로 관찰하고 질문하며, 자신만의 의미를 찾아가는 성장 프레임워크", "A growth framework for observing, questioning and finding your own meaning"))}</h2></div>
  <div class="split">
    <div class="prose">{L(art1[0][1], "p")}{L(art1[1][1], "p")}
      <p class="src">{L(("SERA 기본원칙 제1조", "SERA Principles, Article 1"))}</p></div>
    <div><h3 class="h-sm">{L(("SERA의 네 가지 목적", "Four purposes"))}</h3><ul class="purposes">{plist}</ul>
      {L(PRINCIPLES[0]["articles"][1][2][1][1], "p", "note")}</div>
  </div>
  <div class="person">
    <h3 class="h-sm">{L(("SERA가 지향하는 인간상", "The person SERA envisions"))}</h3>
    {L(person[0][1], "p", "person-lede")}
    <ul class="traits">{traits}</ul>
    {L(person[2][1], "p", "note")}
  </div>
</div></section>'''


def four():
    panels = []
    for f in FOUR:
        qs = "".join(f"<li>{L(q)}</li>" for q in f["questions"])
        pr = "".join(f"<li>{L(p)}</li>" for p in f["practice"])
        cl = [b for b in CHARTER[1]["articles"][f["art"] - 5][2][0][1]]
        cls = "".join(f'<li><span class="cnum" aria-hidden="true">{CIRCLED[i]}</span><span>{L(c)}</span></li>' for i, c in enumerate(cl))
        panels.append(f'''
  <article class="pp pp-{f["key"].lower()}" id="four-{f["key"].lower()}">
    <div class="pp-side"><span class="pp-letter" aria-hidden="true">{f["key"]}</span>
      <h3 class="pp-name">{f["name"]}</h3>
      {L((f["charter"][0].split(" — ")[1], f["charter"][1].split(": ")[1]), "p", "pp-motto")}
      <p class="pp-ref">{L((f"헌장 제{f['art'] - 1}조 · 원칙 제{f['art']}조", f"Charter Art. {f['art'] - 1} · Principles Art. {f['art']}"))}</p>
    </div>
    <div class="pp-main">
      {L(f["title"], "p", "pp-title")}
      {L(f["concept"], "p", "pp-concept")}
      <div class="pp-q"><h4 class="blk-h">{L(("핵심 질문", "Key questions"))}</h4><ul class="qlist">{qs}</ul></div>
      <div class="pp-change"><h4 class="blk-h">{L(("기대하는 변화", "Expected change"))}</h4>{L(f["change"], "p")}</div>
      <details class="more"><summary>{L(("실천 원칙과 헌장 조항 보기", "Practice and Charter clauses"))}</summary>
        <div class="more-in"><div><h4 class="blk-h">{L(("실천 원칙", "Practice"))}</h4><ul>{pr}</ul></div>
        <div><h4 class="blk-h">{L(("기본헌장", "Charter"))}</h4><ol class="clauses">{cls}</ol></div></div>
      </details>
    </div>
  </article>''')
    return f'''
<section class="sec sec-tint" id="four"><div class="wrap">
  <div class="sec-head"><p class="kicker">{L(("네 가지 원칙", "The four principles"))}</p>
  <h2>{L(("Story, Empathy, Resilience, Achievement", "Story, Empathy, Resilience, Achievement"))}</h2>
  {L(CHARTER_PREAMBLE[3], "p", "sec-lede")}</div>
  <div class="pps">{"".join(panels)}</div>
</div></section>'''


def cycle():
    steps = "".join(
        f'<li class="step"><span class="step-n">{i + 1}</span>{L(t, "h3", "step-t")}{L(d, "p")}'
        f'<span class="chip chip-{SHADE[k]}">{NAME[k]}</span></li>'
        for i, (t, d, k) in enumerate(CYCLE))
    art = PRINCIPLES[3]["articles"][0][2]
    return f'''
<section class="sec" id="cycle"><div class="wrap">
  <div class="sec-head"><p class="kicker">{L(("기본 순환 과정", "The SERA cycle"))}</p>
  <h2>{L(("경험에서 시작해 다시 새로운 경험으로", "From experience, back into new experience"))}</h2>
  {L(art[0][1], "p", "sec-lede")}</div>
  <ol class="steps">{steps}</ol>
  <p class="loop"><b class="loop-i" aria-hidden="true">↻</b> {L(("6단계는 다시 새로운 경험으로 이어집니다. 단계 아래 표시는 두드러지는 요소일 뿐, 모든 단계에서 네 요소가 함께 작동합니다.", "Step 6 leads into a new experience. The tag under each step marks the most prominent element; all four work together at every step."))}</p>
</div></section>'''


def common():
    items = "".join(
        f'<li class="cp"><a href="#p-{n}"><span class="cp-n">{n}</span>{L(t, "h3")}{L(first_sentence(b[0][1]), "p")}</a></li>'
        for n, t, b in PRINCIPLES[2]["articles"])
    return f'''
<section class="sec sec-tint" id="common"><div class="wrap">
  <div class="sec-head"><p class="kicker">{L(("SERA를 관통하는 기본원칙", "Principles running through SERA"))}</p>
  <h2>{L(("모든 프로그램이 함께 지키는 열두 가지 원칙", "Twelve principles every program shares"))}</h2>
  {L(PRINCIPLES[2]["intro"], "p", "sec-lede")}</div>
  <ol class="cps">{items}</ol>
</div></section>'''


def seraship():
    ch = PRINCIPLES[4]["articles"]
    examples = PRINCIPLES[3]["articles"][1][2][1][1]
    ex = "".join(
        f'<li class="ex">{L((x[0].split(": ")[0], x[1].split(": ")[0]), "h3")}{L((x[0].split(": ", 1)[1], x[1].split(": ", 1)[1]), "p")}</li>'
        for x in examples)
    q = PRINCIPLES[3]["articles"][2][2][1][1]
    qs = "".join(f'<li>{L((x[0].split(": ")[0], x[1].split(": ")[0]), "b")}{L((x[0].split(": ", 1)[1], x[1].split(": ", 1)[1]))}</li>' for x in q)
    mentor = "".join(f"<li>{L(x)}</li>" for x in ch[2][2][1][1])
    return f'''
<section class="sec" id="seraship"><div class="wrap">
  <div class="sec-head"><p class="kicker">SERAship</p>
  <h2>{L(("콘텐츠가 아니라, 콘텐츠를 활용하는 방식", "It is not the content. It is how the content is used."))}</h2>
  {L(ch[0][2][0][1], "p", "sec-lede")}</div>
  <ul class="exs">{ex}</ul>
  <div class="split split-even">
    <div class="panel"><h3 class="h-sm">{L(("활동 전후를 잇는 질문: 미술 SERAship의 예", "Questions before and after: an art SERAship"))}</h3><ul class="beforeafter">{qs}</ul>
      {L(PRINCIPLES[3]["articles"][2][2][2][1], "p", "note")}</div>
    <div class="panel"><h3 class="h-sm">{L(("퍼실리테이터와 멘토의 역량", "What facilitators and mentors practice"))}</h3><ul class="ticks">{mentor}</ul>
      {L(ch[2][2][2][1], "p", "note")}</div>
  </div>
  <aside class="safety"><h3 class="h-sm">{L(("심리적 안전", "Psychological safety"))}</h3>{L(first_sentence(ch[3][2][0][1]), "p")}
    {L(("운영기관은 위기 대응 절차와 전문기관 연계 체계를 미리 갖추고, 퍼실리테이터는 역할 범위를 넘는 개입 대신 전문기관에 연계합니다.", "Operating organizations prepare crisis procedures and referral links in advance, and facilitators refer people to specialist services rather than intervening beyond their role."), "p")}
    <a href="#p-27">{L(("제27조 전문 보기", "Read Article 27"))} →</a></aside>
</div></section>'''


def records():
    ch = PRINCIPLES[5]["articles"]
    nbp = ch[1][2][0][1]
    tags = [("기록", "Record"), ("서사화", "Narrate"), ("활용", "Apply")]
    cards = "".join(
        f'<li class="rec rec-{i}"><span class="rec-tag">{L(tags[i])}</span><h3>{e(x[0].split(": ")[0])}</h3>'
        f'{L((re.sub(r"\(.+?\)$", "", x[0].split(": ", 1)[1]).strip(), re.sub(r" \(.+?\)$", "", x[1].split(": ", 1)[1])), "p")}</li>'
        for i, x in enumerate(nbp))
    ai = "".join(f"<li>{L(x)}</li>" for x in ch[3][2][1][1])
    sdx = "".join(f"<li>{L(x)}</li>" for x in ch[4][2][1][1])
    return f'''
<section class="sec sec-tint" id="records"><div class="wrap">
  <div class="sec-head"><p class="kicker">{L(("SERA 기록", "SERA records"))}</p>
  <h2>{L(("기록의 주인은 언제나 참여자 자신입니다", "The participant always owns the record"))}</h2>
  {L(PRINCIPLES[2]["articles"][9][2][0][1], "p", "sec-lede")}</div>
  <ol class="recs">{cards}</ol>
  {L(ch[1][2][1][1], "p", "note center")}
  <div class="split split-even">
    <div class="panel"><h3 class="h-sm">{L(("디지털 기록과 AI 활용", "Digital records and AI"))}</h3>{L(ch[3][2][0][1], "p")}<ul class="ticks">{ai}</ul></div>
    <div class="panel panel-sdx"><h3 class="h-sm">{L(("SDX재단의 역할", "The role of SDX Foundation"))}</h3>{L(ch[4][2][0][1], "p")}<ol class="nums">{sdx}</ol>
      {L(ch[4][2][2][1], "p", "note")}
      <a class="sdx-link" href="{SDX}/16" target="_top" rel="noopener">{L(("SDX재단 소개", "About SDX Foundation"))} ↗</a></div>
  </div>
</div></section>'''


def declaration():
    lines = "".join(f"<li>{L(d)}</li>" for d in DECLARATION)
    return f'''
<section class="decl" id="declaration"><div class="wrap">
  <p class="kicker kicker-light">{L(("SERA의 핵심 선언", "The SERA declaration"))}</p>
  <ol class="decl-list">{lines}</ol>
  {L(DECLARATION_CLOSE, "p", "decl-close")}
</div></section>'''


def glossary(id_="glossary", heading=True):
    rows = "".join(
        f'<div class="g-row"><dt>{L(t)}</dt><dd>{L(d)}<span class="g-ref">{L(r)}</span></dd></div>'
        for t, d, r in GLOSSARY)
    head = (f'<div class="sec-head"><p class="kicker">{L(("용어", "Glossary"))}</p>'
            f'<h2>{L(("SERA 고유 용어", "Terms used in SERA"))}</h2>{L(GLOSSARY_INTRO, "p", "sec-lede")}</div>') if heading else ""
    return f'<section class="sec" id="{id_}"><div class="wrap">{head}<dl class="gloss">{rows}</dl></div></section>'


def docs():
    return f'''
<section class="sec sec-tint" id="docs"><div class="wrap">
  <div class="sec-head"><p class="kicker">{L(("문서", "Documents"))}</p><h2>{L(("SERA의 기준이 되는 두 문서", "The two documents that define SERA"))}</h2></div>
  <div class="docs">
    <a class="doc" href="#charter"><span class="doc-meta">{L(("v1.0 초안 · 5장 17조 · 부칙", "v1.0 draft · 5 chapters, 17 articles · addenda"))}</span>
      <h3>{L(CHARTER_META["title"])}</h3>{L(("SERA의 철학과 핵심 원칙을 세우고, 모든 교육과정, SERAship, SERA Agent, My SERA Agent가 지켜야 할 최상위 규범입니다.", "Sets out SERA's philosophy and core principles. It is the highest norm for every curriculum, SERAship, SERA Agent and My SERA Agent."), "p")}
      <span class="doc-go">{L(("전문 읽기", "Read in full"))} →</span></a>
    <a class="doc" href="#principles"><span class="doc-meta">{L(("v1.1 · 2026년 10월 9일 · 8장 38조 · 부록", "v1.1 · October 9, 2026 · 8 chapters, 38 articles · appendix"))}</span>
      <h3>{L(P_META["title"])}</h3>{L(("네 가지 원리, 열두 가지 공통 원칙, 실행 구조, SERAship 운영, 기록과 SDX재단의 역할을 담은 실행 원칙입니다.", "The working principles: the four elements, twelve shared principles, how SERA runs, SERAship operations, and records and the role of SDX Foundation."), "p")}
      <span class="doc-go">{L(("전문 읽기", "Read in full"))} →</span></a>
  </div>
</div></section>'''


def charter_view():
    pre = "".join(L(p, "p") for p in CHARTER_PREAMBLE)
    add = "".join(f'<li><span class="art-no-inline">{L((f"제{i + 1}조", f"Article {i + 1}"))}</span> {L(a)}</li>' for i, a in enumerate(CHARTER_ADDENDA))
    return f'''
<div class="view" id="charter"><div class="wrap doc-wrap">
  <aside class="doc-aside"><a class="back" href="#docs">← {L(("SERA 홈", "SERA home"))}</a>
    <nav aria-label="Charter contents">{toc("c", CHARTER, [("c-pre", ("전문", "Preamble")), ("c-add", ("부칙", "Addenda"))])}</nav></aside>
  <div class="doc-main">
    <header class="doc-head"><p class="kicker">{L(CHARTER_META["version"])}</p><h1>{L(CHARTER_META["title"])}</h1>
      {L(CHARTER_META["motto"], "p", "doc-motto")}</header>
    <section class="chapter" id="c-pre"><h2 class="ch-title">{L(("전문", "Preamble"))}</h2><div class="preamble">{pre}</div></section>
    {chapters("c", CHARTER)}
    <section class="chapter" id="c-add"><h2 class="ch-title">{L(("부칙", "Addenda"))}</h2><ol class="addenda">{add}</ol></section>
    <p class="doc-sign">SERA · Story · Empathy · Resilience · Achievement</p>
    {L(("영문은 이해를 돕기 위한 번역이며, 해석의 기준은 한국어 원문입니다.", "The English text is a translation provided for reference. The Korean original is authoritative."), "p", "note")}
  </div>
</div></div>'''


def principles_view():
    decl = "".join(f"<li>{L(d)}</li>" for d in DECLARATION)
    rows = "".join(f'<div class="g-row"><dt>{L(t)}</dt><dd>{L(d)}<span class="g-ref">{L(r)}</span></dd></div>' for t, d, r in GLOSSARY)
    return f'''
<div class="view" id="principles"><div class="wrap doc-wrap">
  <aside class="doc-aside"><a class="back" href="#docs">← {L(("SERA 홈", "SERA home"))}</a>
    <nav aria-label="Principles contents">{toc("p", PRINCIPLES, [("p-decl", ("제8장 · SERA의 핵심 선언", "Chapter 8 · The SERA Declaration")), ("p-app", ("부록 · SERA 고유 용어 정의", "Appendix · SERA Terms"))])}</nav></aside>
  <div class="doc-main">
    <header class="doc-head"><p class="kicker">{L(P_META["date"])}</p><h1>{L(P_META["title"])}</h1>
      <p class="doc-motto">{e(P_META["subtitle"][1])}</p></header>
    {chapters("p", PRINCIPLES)}
    <section class="chapter" id="p-decl"><h2 class="ch-title">{L(("제8장", "Chapter 8"), "span", "ch-label")}{L(("SERA의 핵심 선언", "The SERA Declaration"))}</h2>
      <ol class="decl-doc">{decl}</ol>{L(DECLARATION_CLOSE, "p")}</section>
    <section class="chapter" id="p-app"><h2 class="ch-title">{L(("부록", "Appendix"), "span", "ch-label")}{L(("SERA 고유 용어 정의", "SERA Terms"))}</h2>
      {L(GLOSSARY_INTRO, "p")}<dl class="gloss">{rows}</dl></section>
    {L(("영문은 이해를 돕기 위한 번역이며, 해석의 기준은 한국어 원문입니다.", "The English text is a translation provided for reference. The Korean original is authoritative."), "p", "note")}
  </div>
</div></div>'''


def footer():
    return f'''
<footer class="foot"><div class="wrap foot-in">
  <div class="foot-brand">{mark(34)}<div><p class="foot-word">SERA</p>{L(("SERA는 SDX재단이 연구하고 확산하는 성장 프레임워크입니다.", "SERA is a growth framework researched and shared by SDX Foundation."), "p")}</div></div>
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
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+KR:wght@400;500;700&display=swap">')


def body():
    return (header()
            + '<main id="top">'
            + '<div class="view active" id="home">' + hero() + about() + four() + cycle() + common()
            + seraship() + records() + declaration() + glossary() + docs() + '</div>'
            + charter_view() + principles_view()
            + '</main>' + footer())


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
<meta property="og:description" content="자신을 이해하고, 서로를 공감하며, 함께 영글어 가는 삶">
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
