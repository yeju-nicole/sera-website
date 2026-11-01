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


def sec_head(kicker, title, lede=None):
    l = L(lede, "p", "sec-lede") if lede else ""
    return f'<div class="sec-head"><p class="kicker">{L(kicker)}</p><h2>{L(title)}</h2>{l}</div>'


def hero():
    letters = "".join(
        f'<li class="hl hl-{f["key"].lower()}"><span class="hl-letter">{f["key"]}</span>'
        f'<span class="hl-name">{f["name"]}</span>{L(FOUR_SHORT[f["key"]][0], "span", "hl-line")}</li>'
        for f in FOUR)
    return f'''
<section class="hero"><div class="wrap">
  <p class="eyebrow">{e(POSITION["kicker"][0])}</p>
  <h1 class="hero-title">{L(POSITION["title"])}</h1>
  {L(POSITION["tagline"], "p", "hero-tag")}
  {L(POSITION["lede"], "p", "hero-lede")}
  <div class="cta">
    <a class="btn btn-solid" href="#way">{L(("SERA Way 알아보기", "How SERA works"))}</a>
    <a class="btn btn-line" href="#together">{L(("함께하기", "Get involved"))}</a>
  </div>
  <ol class="hero-letters" aria-label="SERA">{letters}</ol>
  <p class="ripen-note">{L(("영글다", "yeonggeulda (영글다)"), "b")} {L(("곡식이나 열매가 알이 차서 단단하게 익다. SERA의 네 가지 보랏빛은 옅은 꽃빛에서 무르익은 열매빛까지, 각자의 속도로 영글어 가는 과정을 담았습니다.", "to ripen, as grain fills out and fruit matures. SERA's four shades of purple run from pale blossom to ripe fruit, for growth that happens at each person's own pace."))}</p>
</div></section>'''


def about():
    phil = "".join(f'<li><span class="ph-n">{i + 1}</span>{L(p, "p")}</li>' for i, p in enumerate(PHILOSOPHY))
    person = PRINCIPLES[0]["articles"][2][2]
    traits = "".join(f"<li>{L(t)}</li>" for t in person[1][1])
    return f'''
<section class="sec" id="about"><div class="wrap">
  {sec_head(("왜 SERA인가", "Why SERA"), ("경험이 저절로 다음 선택이 되지는 않습니다", "Experience does not turn into the next choice on its own"))}
  <div class="split">
    <div class="prose">{L(WHY[0], "p")}{L(WHY[1], "p")}{L(PRINCIPLES[0]["articles"][0][2][1][1], "p")}</div>
    <div><h3 class="h-sm">{L(("SERA의 핵심 철학", "What SERA believes"))}</h3><ol class="phil">{phil}</ol></div>
  </div>
  <div class="person">
    <h3 class="h-sm">{L(("SERA가 지향하는 사람", "The person SERA hopes to support"))}</h3>
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
        verb, line = FOUR_SHORT[f["key"]]
        panels.append(f'''
  <article class="pp pp-{f["key"].lower()}" id="four-{f["key"].lower()}">
    <div class="pp-side"><span class="pp-letter" aria-hidden="true">{f["key"]}</span>
      <h3 class="pp-name">{f["name"]}</h3>
      {L(verb, "p", "pp-verb")}
      {L(line, "p", "pp-motto")}
    </div>
    <div class="pp-main">
      {L(f["title"], "p", "pp-title")}
      {L(f["concept"], "p", "pp-concept")}
      <div class="pp-q"><h4 class="blk-h">{L(("핵심 질문", "Key questions"))}</h4><ul class="qlist">{qs}</ul></div>
      <div class="pp-change"><h4 class="blk-h">{L(("기대하는 변화", "Expected change"))}</h4>{L(f["change"], "p")}</div>
      <details class="more"><summary>{L(("실천 원칙 보기", "Show practice principles"))}</summary>
        <div class="more-in one"><ul>{pr}</ul></div>
      </details>
    </div>
  </article>''')
    return f'''
<section class="sec sec-tint" id="four"><div class="wrap">
  {sec_head(("네 가지 요소", "The four elements"), ("Story, Empathy, Resilience, Achievement", "Story, Empathy, Resilience, Achievement"), PRINCIPLES[0]["articles"][1][2][1][1])}
  <div class="pps">{"".join(panels)}</div>
</div></section>'''


def way():
    ring = "".join(
        f'<li class="ring-i ring-{f["key"].lower()}"><b>{f["name"]}</b>{L(FOUR_SHORT[f["key"]][0], "span")}</li>' for f in FOUR)
    flow = "".join(f'<li class="fl"><span class="fl-n">{i + 1}</span>{L(t, "h4")}{L(d, "p")}</li>' for i, (t, d) in enumerate(FLOW))
    ex = "".join(f'<li>{L(t, "b")}{L(d, "span")}</li>' for t, d in ART_EXAMPLE)
    steps = "".join(f'<li class="ship-s"><span class="ship-n">{i + 1}</span>{L(t, "h4")}{L(d, "p")}</li>' for i, (t, d) in enumerate(SHIP_STEPS))
    aud = "".join(f'<li>{L(t, "b")}{L(d, "span")}</li>' for t, d in AUDIENCES)
    return f'''
<section class="sec" id="way"><div class="wrap">
  {sec_head(("SERA Way · SERAship", "SERA Way · SERAship"), ("성장의 원리와 현장의 실행", "The principle of growth, put into practice"))}
  <div class="split split-even way-top">
    <div class="panel">
      <p class="kicker">SERA Way</p>
      <h3 class="h-md">{L(("네 가지 요소가 순환하며 작동하는 성장 프로세스", "A growth process in which the four elements keep cycling"))}</h3>
      <ol class="ring" aria-label="SERA Way">{ring}</ol>
      {L(("네 요소는 정해진 순서대로 밟아 가는 단계가 아닙니다. 활동에 따라 여러 요소가 함께 다루어지기도 하고, 같은 요소가 여러 번 되풀이되기도 합니다.", "The four elements are not steps to be taken in a fixed order. Depending on the activity, several may come up together, and the same one may come back many times."), "p", "note")}
    </div>
    <div class="panel">
      <p class="kicker">{L(("하나의 경험이 이어지는 방식", "How one experience carries forward"))}</p>
      <ol class="flow">{flow}</ol>
      {L(("다음 활동에서 얻은 경험은 다시 기록과 이해로 이어집니다.", "What you experience next flows back into recording and understanding."), "p", "note")}
    </div>
  </div>
  <div class="example">
    <h3 class="h-sm">{L(("예시: 미술 활동에서", "Example: in an art class"))}</h3>
    <ol class="ex-steps">{ex}</ol>
    {L(ART_NOTE, "p", "note")}
  </div>
  <div class="ship">
    <p class="kicker">SERAship</p>
    <h3 class="h-md">{L(("실제 삶과 교육 현장에서 구현하는 실행 프로그램", "Programs that bring SERA into real life and learning"))}</h3>
    {L(PRINCIPLES[4]["articles"][0][2][0][1], "p", "ship-lede")}
    <ol class="ship-steps">{steps}</ol>
    <p class="aud-h">{L(("대상과 현장에 따라 유연하게 설계합니다", "Designed flexibly for each group and setting"))}</p>
    <ul class="aud">{aud}</ul>
  </div>
</div></section>'''


def common():
    items = "".join(
        f'<li class="cp"><div><span class="cp-n">{i + 1:02d}</span>{L(t, "h3")}{L(first_sentence(b[0][1]), "p")}</div></li>'
        for i, (n, t, b) in enumerate(PRINCIPLES[2]["articles"]))
    return f'''
<section class="sec sec-tint" id="common"><div class="wrap">
  {sec_head(("SERA를 관통하는 원칙", "Principles running through SERA"), ("모든 SERA 프로그램이 함께 지키는 열두 가지 원칙", "Twelve principles every SERA program shares"), PRINCIPLES[2]["intro"])}
  <ol class="cps">{items}</ol>
</div></section>'''


def promises():
    pr = "".join(f'<li class="prm"><span class="prm-n">{i + 1}</span>{L(t, "h3")}{L(d, "p")}</li>' for i, (t, d) in enumerate(PROMISES))
    notp = "".join(f"<li>{L(x)}</li>" for x in NOT_PROBLEMS)
    who = "".join(f'<li class="who-{i}">{L(t, "b")}{L(d, "span")}</li>' for i, (t, d) in enumerate(WHO_WROTE))
    ai = "".join(f"<li>{L(x)}</li>" for x in PRINCIPLES[5]["articles"][3][2][1][1])
    return f'''
<section class="sec" id="promises"><div class="wrap">
  {sec_head(("참여자와의 약속", "Our promises to participants"), ("SERA의 주인은 언제나 참여자 자신입니다", "Participants are always in charge"), PRINCIPLES[2]["articles"][0][2][0][1])}
  <ol class="prms">{pr}</ol>
  <div class="split split-even">
    <div class="panel"><h3 class="h-sm">{L(("SERA가 고쳐야 할 문제로 보지 않는 것", "What SERA does not treat as a problem"))}</h3>
      <ul class="xs">{notp}</ul>
      {L(("스스로 결정한다는 것이 남이 정한 목표를 모두 거부한다는 뜻은 아닙니다. 참여자가 운영자의 기대와 다른 결론을 내리는 것도 존중합니다.", "Deciding for yourself does not mean rejecting every goal set by others. SERA also respects conclusions that differ from what an operator expected."), "p", "note")}</div>
    <div class="panel"><h3 class="h-sm">{L(("누가 남긴 기록인지 구분합니다", "Every record shows who wrote it"))}</h3>
      <ul class="who">{who}</ul>
      {L(("세 가지를 하나로 합쳐 “파란색을 좋아하고 선택을 자주 바꾸는 성향”처럼 저장하지 않습니다. 해석은 해석이라고 분명히 표시합니다.", "These are never merged into something like “likes blue and often changes their mind.” An interpretation is always marked as an interpretation."), "p", "note")}</div>
  </div>
  <div class="split split-even">
    <div class="panel"><h3 class="h-sm">{L(("디지털 기록과 AI 활용", "Digital records and AI"))}</h3><ul class="ticks">{ai}</ul></div>
    <div class="panel"><h3 class="h-sm">{L(("심리적 안전", "Psychological safety"))}</h3>
      {L(("SERAship은 상담이나 치료가 아닙니다. 운영기관은 위기 상황에 대비한 대응 절차와 상담·의료·복지 전문기관 연계 체계를 미리 갖추고, 퍼실리테이터는 역할 범위를 넘는 개입 대신 전문기관에 연계합니다.", "SERAship is not counseling or therapy. Operating organizations prepare crisis procedures and referral links to counseling, medical and welfare services in advance, and facilitators refer people to specialists rather than intervening beyond their role."), "p")}
      {L(("미성년자 프로그램은 보호자 동의와 참여자 본인의 이해·동의를 함께 확보합니다.", "Programs for minors obtain both guardian consent and the participant's own understanding and consent."), "p")}</div>
  </div>
</div></section>'''


def records():
    cards = "".join(
        f'<li class="rec rec-{i}"><span class="rec-tag">{L(r["tag"])}</span><h3>{r["name"]}</h3>'
        f'<ul>{"".join(f"<li>{L(x)}</li>" for x in r["items"])}</ul></li>'
        for i, r in enumerate(RECORD_FLOW))
    vals = "".join(f'<li>{L(t, "b")}{L(d, "span")}</li>' for t, d in RECORD_VALUES)
    return f'''
<section class="sec sec-tint" id="records"><div class="wrap">
  {sec_head(("기록이 만드는 성장", "Growth through records"), ("SERA Note에서 SERA Book으로, 일상의 경험을 나의 자산으로", "From SERA Note to SERA Book: everyday experience becomes your own asset"), PRINCIPLES[2]["articles"][9][2][0][1])}
  <ol class="recs">{cards}</ol>
  <p class="rec-flow">{L(("축적 → 정리 → 스토리화", "Collect → organize → tell the story"))}</p>
  <h3 class="h-sm center">{L(("SERA 기록의 가치", "What a SERA record is worth"))}</h3>
  <ul class="vals">{vals}</ul>
  {L(("기록의 공개 범위는 참여자가 정하며, 모든 참여자에게 같은 형식의 결과물을 요구하지 않습니다. 기록이 쌓였다는 사실만으로 성장이 증명되지는 않으며, 변화에 대한 해석은 기록의 내용과 맥락에 근거합니다.", "Participants decide who can see their records, and no one is required to produce the same kind of output. Records piling up does not by itself prove growth; any reading of change rests on what the records say and their context."), "p", "note center")}
</div></section>'''


def together():
    eco = "".join(
        f'<li class="eco eco-{i}"><div class="eco-h"><h3>{e(x["name"])}</h3>{L(x["who"], "span", "eco-who")}</div>'
        f'{L(x["what"], "p")}<ul>{"".join(f"<li>{L(r)}</li>" for r in x["roles"])}</ul></li>'
        for i, x in enumerate(ECOSYSTEM))
    models = "".join(
        f'<li class="mdl"><span class="mdl-k">SERA</span><h3>{m}</h3>{L(w, "span", "mdl-w")}{L(d, "p")}</li>'
        for m, w, d in MODELS)
    case = "".join(f"<li>{L(x)}</li>" for x in ART_CASE)
    return f'''
<section class="sec" id="together"><div class="wrap">
  {sec_head(("SERA 생태계", "The SERA ecosystem"), ("One SERA · Multiple Models · Many Members · Many Salimist", "One SERA · Multiple Models · Many Members · Many Salimist"), ("하나의 SERA 철학을 바탕으로 분야별 모델과 현장 운영 주체가 연결되는, 다양한 기관과 사람이 함께 만들어 가는 개방형 성장 플랫폼입니다.", "An open growth platform built together by many organizations and people, where field-specific models and local operators connect around one shared SERA philosophy."))}
  <ol class="ecos">{eco}</ol>
  <div class="models-h">
    <h3 class="h-md">{L(("분야별 SERA 모델", "SERA models by field"))}</h3>
    {L(("각 분야의 전문성과 결합한 다양한 SERAship 모델", "SERAship models that combine SERA with each field's expertise"), "p", "note")}
  </div>
  <ul class="mdls">{models}</ul>
  <div class="split split-even case-row">
    <div class="panel"><p class="kicker">{L(("운영 예시 · SERA Art", "Example · SERA Art"))}</p>
      <h3 class="h-md">{L(("그림과 예술활동을 통해 자기표현과 자기발견을 돕는 모델", "A model for self-expression and self-discovery through art"))}</h3>
      <ul class="ticks">{case}</ul><p class="case-sig">CREATE · REFLECT · GROW</p></div>
    <div class="panel join">
      <h3 class="h-md">{L(("SERA와 함께할 기관을 찾습니다", "Join SERA"))}</h3>
      {L(("자신의 분야에서 SERA 모델을 개발하고 보급할 SERAship Partner, 현장에서 프로그램을 운영할 SERAship Member를 기다립니다. 학교, 교육기관, 기업, 지자체, 문화·환경 기관 누구나 문의할 수 있습니다.", "We welcome SERAship Partners who will develop and share SERA models in their fields, and SERAship Members who will run programs on the ground. Schools, education providers, companies, local governments and cultural or environmental organizations are all welcome to get in touch."), "p")}
      <a class="btn btn-solid" href="{SDX}/33" target="_top" rel="noopener">{L(("SDX재단에 문의하기", "Contact SDX Foundation"))} ↗</a>
      <p class="mail-line">sdx@sdxfoundation.org</p>
    </div>
  </div>
</div></section>'''


def salimist():
    traits = "".join(f'<li><span class="st-n">{i + 1}</span>{L(t, "b")}{L(d, "span")}</li>' for i, (t, d) in enumerate(SALIMIST["traits"]))
    stages = "".join(f'<li class="stg stg-{i}">{L(a, "b")}{L(c, "span", "stg-c")}{L(b, "p")}</li>' for i, (a, b, c) in enumerate(SALIMIST["stages"]))
    return f'''
<section class="sec sec-tint" id="salimist"><div class="wrap">
  {sec_head(("SERA가 만들어 가는 사람", "Who SERA helps people become"), ("살림가 (Salimist)", "The Salimist"), SALIMIST["def"])}
  <div class="split salim">
    <div><h3 class="h-sm">{L(("살림가의 다섯 가지 모습", "Five traits of a Salimist"))}</h3><ol class="strs">{traits}</ol></div>
    <div class="salim-note">
      {L(("살림은 ‘살리다’에서 온 말로, 생명·관계·삶터처럼 얽힌 전체를 함께 살리는 일을 뜻합니다. 경쟁과 화폐적 성장을 앞세우는 머니로직을 넘어, 나와 타인, 공동체와 자연이 함께 살아나는 살림로직을 지향합니다.", "Salim comes from the Korean salida, to bring to life. It means bringing a whole web of life, relationships and living places to life together. SERA looks beyond a Money Logic of competition and monetary growth toward a Salim Logic in which oneself, others, communities and nature flourish together."), "p")}
      {L(("기여와 살림은 참여자에게 부과되는 의무가 아니라, 스스로 탐색하도록 열어 두는 초대입니다.", "Contribution and salim are never imposed on participants. They are an open invitation to explore."), "p", "note")}
    </div>
  </div>
  <h3 class="h-sm stg-h">{L(("SERA in(人) 생애 단계별 모델", "SERA in (人) across life stages"))}</h3>
  <ol class="stgs">{stages}</ol>
  <p class="motto">Discover Yourself · Grow Together · Become Salim</p>
</div></section>'''


def declaration():
    lines = "".join(f"<li>{L(d)}</li>" for d in DECLARATION)
    return f'''
<section class="decl" id="declaration"><div class="wrap">
  <p class="kicker kicker-light">{L(("SERA의 핵심 선언", "The SERA declaration"))}</p>
  <ol class="decl-list">{lines}</ol>
  {L(DECLARATION_CLOSE, "p", "decl-close")}
</div></section>'''


GLOSS_KEEP = ["살림", "머니로직 (Money Logic)", "살림로직 (Salim Logic)", "ESGG", "SERAship", "달란트",
              "얕은 노동 (Shallow Job)", "깊은 노동 (Deep Job)", "장르마스터 (Genre Master)", "살림가 (Salimist)",
              "SERA Note / Book / Portfolio"]


def glossary():
    rows = "".join(f'<div class="g-row"><dt>{L(t)}</dt><dd>{L(d)}</dd></div>'
                   for t, d, _ in GLOSSARY if t[0] in GLOSS_KEEP)
    return f'''<section class="sec" id="glossary"><div class="wrap">
  {sec_head(("용어", "Glossary"), ("SERA에서 쓰는 말", "Words used in SERA"))}<dl class="gloss">{rows}</dl></div></section>'''


def footer():
    return f'''
<footer class="foot"><div class="wrap foot-in">
  <div class="foot-brand">{mark(34)}<div><p class="foot-word">SERA</p>{L(("SERA는 SDX재단(Sustainable Development eXperience Foundation)이 만들어 가는 자기주도적 삶의 성장 동반자입니다.", "SERA is a companion for self-directed growth from SDX Foundation (Sustainable Development eXperience Foundation)."), "p")}</div></div>
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
            + '<main id="top"><div class="view active" id="home">'
            + hero() + about() + four() + way() + common() + promises() + records()
            + together() + salimist() + declaration() + glossary()
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
