# -*- coding: utf-8 -*-
"""Page sections (concise copy). Imported by build.py; helpers come from there."""
from content import DECLARATION, ECOSYSTEM, FLOW, FOUR, FOUR_SHORT, GLOSSARY, MODELS, PHILOSOPHY, POSITION, \
    RECORD_VALUES, SALIMIST, SHIP_STEPS, AUDIENCES

SDX = "https://www.sdxfoundation.org"

FOUR_CONCEPT = {
    "S": ("외부의 기준이 아닌 나의 관점에서 경험의 의미를 찾습니다.", "Find the meaning of your experiences from your own point of view, not outside standards."),
    "E": ("무조건 동의하는 것이 아니라, 서로 다른 관점의 이유를 이해하려는 힘입니다.", "Not agreeing with everything, but trying to understand why others see things differently."),
    "R": ("어려움이 없는 상태가 아니라, 도움과 자원을 활용해 새로운 대응을 찾는 힘입니다.", "Not a life without hardship, but finding a new response with the help and resources around you."),
    "A": ("목표에 도달한 순간이 아니라, 나의 달란트를 매일 실천하며 의미를 쌓아 가는 과정입니다.", "Not the moment you reach a goal, but practicing your talent every day and building meaning along the way."),
}
EXAMPLE = [
    (("기록", "Record"), ("“색을 섞는 게 어려웠다”는 짧은 메모를 남깁니다.", "A short note: “Mixing colors was hard.”")),
    (("질문", "Question"), ("다음 시간, “오늘 다시 해 볼까요?”라는 질문을 받습니다.", "Next time: “Want to try again today?”")),
    (("선택", "Choice"), ("다시 하기, 도움 요청, 다른 활동 중 스스로 고릅니다.", "Try again, ask for help, or do something else. Their call.")),
]
PROMISES = [
    (("답하지 않아도 됩니다", "You can always pass"), ("답하지 않거나, 다르게 표현하거나, 멈출 수 있습니다.", "Skip, answer differently, or stop anytime.")),
    (("해석은 제안일 뿐입니다", "Interpretations are suggestions"), ("교사나 AI의 해석보다 참여자의 설명이 우선합니다.", "Your explanation outranks any teacher's or AI's.")),
    (("공유는 내가 정합니다", "You decide what's shared"), ("무엇을 기록하고 누구와 나눌지 참여자가 정합니다.", "You choose what's recorded and who sees it.")),
    (("단정하지 않습니다", "No fixed labels"), ("몇 번의 경험으로 성격이나 특성을 규정하지 않습니다.", "A few moments never define who you are.")),
    (("침묵도 괜찮습니다", "Silence is fine"), ("응답이 없어도 의욕이 없다고 판단하지 않습니다.", "No answer is never read as no effort.")),
]
AI_RULES = [
    ("어떤 기록을 왜 쓰는지 미리 알리고 동의를 받습니다.", "We explain which records are used and why, and ask first."),
    ("AI 분석은 참고 자료일 뿐, 진단·서열화·선발에 쓰지 않습니다.", "AI analysis is a reference only, never used to diagnose, rank or select."),
    ("동의 없이 AI 학습이나 제3자 제공에 쓰지 않으며, 열람·이의·삭제를 요청할 수 있습니다.", "No model training or third-party sharing without consent; you can view, dispute or delete results."),
]
RECORDS = [
    ("SERA Note", ("기록", "Record"), ("질문과 활동, 생각과 감정을 꾸준히 남깁니다.", "Capture questions, activities, thoughts and feelings as you go.")),
    ("SERA Book", ("이야기", "Story"), ("쌓인 기록을 엮어 나의 변화와 방향을 담습니다.", "Weave your records into the story of your change and direction.")),
    ("SERA Portfolio", ("활용", "Use"), ("원할 때, 경험과 역량을 보여주는 자료로 정리합니다.", "When you want, turn them into a record of your experience and skills.")),
]
GLOSS = ["살림", "살림로직 (Salim Logic)", "머니로직 (Money Logic)", "ESGG", "달란트"]


def build_sections(L, e, mark):
    def head(kicker, title, lede=None):
        l = L(lede, "p", "sec-lede") if lede else ""
        return f'<div class="sec-head"><p class="kicker">{L(kicker)}</p><h2>{L(title)}</h2>{l}</div>'

    hero = f'''
<section class="hero"><div class="wrap">
  <p class="eyebrow">{e(POSITION["kicker"][0])}</p>
  <h1 class="hero-title">{L(POSITION["title"])}</h1>
  {L(POSITION["tagline"], "p", "hero-tag")}
  {L(("스스로 삶을 설계하고, 함께 성장하며, 세상을 살리는 살림가를 키웁니다.", "Helping people shape their own lives, grow together and give back as Salimists."), "p", "hero-lede")}
  <div class="cta">
    <a class="btn btn-solid" href="#way">{L(("SERA 알아보기", "How SERA works"))}</a>
    <a class="btn btn-line" href="#together">{L(("함께하기", "Get involved"))}</a>
  </div>
  <ol class="hero-letters" aria-label="SERA">{"".join(
        f'<li class="hl hl-{f["key"].lower()}"><span class="hl-letter">{f["key"]}</span>'
        f'<span class="hl-name">{f["name"]}</span>{L(FOUR_SHORT[f["key"]][0], "span", "hl-line")}</li>' for f in FOUR)}</ol>
  <p class="ripen-note">{L(("영글다", "yeonggeulda"), "b")} {L(("열매가 알차게 익다. 네 가지 보랏빛은 각자의 속도로 영그는 성장을 뜻합니다.", "to ripen. The four shades of purple stand for growth at each person's own pace."))}</p>
</div></section>'''

    phil = "".join(f'<li><span class="ph-n">{i + 1}</span>{L(p, "p")}</li>' for i, p in enumerate(PHILOSOPHY))
    about = f'''
<section class="sec" id="about"><div class="wrap">
  {head(("왜 SERA인가", "Why SERA"), ("경험이 다음 선택으로 이어지도록", "Turning experience into your next choice"))}
  <div class="split">
    <div class="prose">{L(("불확실한 시대에 필요한 힘은 나를 이해하고, 방향을 정하고, 관계를 맺고, 작은 성취를 이어 가는 능력입니다.", "In uncertain times, what matters most is understanding yourself, setting your direction, building relationships and keeping small achievements going."), "p")}
      {L(("하지만 경험은 저절로 다음 선택이 되지 않습니다. SERA는 돌아보고, 기록하고, 실천하는 그 연결을 돕습니다.", "But experience doesn't become your next choice on its own. SERA helps you reflect, record and act on it."), "p")}</div>
    <div><h3 class="h-sm">{L(("SERA의 핵심 철학", "What SERA believes"))}</h3><ol class="phil">{phil}</ol></div>
  </div>
</div></section>'''

    panels = "".join(f'''
  <article class="pp pp-{f["key"].lower()}" id="four-{f["key"].lower()}">
    <div class="pp-side"><span class="pp-letter" aria-hidden="true">{f["key"]}</span><h3 class="pp-name">{f["name"]}</h3>{L(FOUR_SHORT[f["key"]][0], "p", "pp-verb")}</div>
    <div class="pp-main">{L(FOUR_CONCEPT[f["key"]], "p", "pp-concept")}
      <ul class="qlist">{"".join(f"<li>{L(q)}</li>" for q in f["questions"][:3])}</ul></div>
  </article>''' for f in FOUR)
    four = f'''
<section class="sec sec-tint" id="four"><div class="wrap">
  {head(("네 가지 요소", "The four elements"), ("Story · Empathy · Resilience · Achievement", "Story · Empathy · Resilience · Achievement"), ("네 요소는 따로 배우는 과목이 아니라, 삶 속에서 함께 자라는 하나의 과정입니다.", "Not four separate subjects, but one process that grows together in everyday life."))}
  <div class="pps">{panels}</div>
</div></section>'''

    ring = "".join(f'<li class="ring-i ring-{f["key"].lower()}"><b>{f["name"]}</b>{L(FOUR_SHORT[f["key"]][0], "span")}</li>' for f in FOUR)
    flow = "".join(f'<li class="fl"><span class="fl-n">{i + 1}</span>{L(t, "h4")}{L(d, "p")}</li>' for i, (t, d) in enumerate(FLOW))
    ex = "".join(f'<li>{L(t, "b")}{L(d, "span")}</li>' for t, d in EXAMPLE)
    steps = "".join(f'<li class="ship-s"><span class="ship-n">{i + 1}</span>{L(t, "h4")}{L(d, "p")}</li>' for i, (t, d) in enumerate(SHIP_STEPS))
    aud = "".join(f'<li>{L(t, "b")}{L(d, "span")}</li>' for t, d in AUDIENCES)
    way = f'''
<section class="sec" id="way"><div class="wrap">
  {head(("SERA Way · SERAship", "SERA Way · SERAship"), ("성장의 원리와 현장의 실천", "The principle, and the practice"))}
  <div class="split split-even way-top">
    <div class="panel"><p class="kicker">SERA Way</p><h3 class="h-md">{L(("네 요소가 순환하는 성장", "Four elements in a continuous cycle"))}</h3>
      <ol class="ring" aria-label="SERA Way">{ring}</ol>
      {L(("정해진 순서가 아니라, 함께 또 반복해서 작동합니다.", "Not fixed steps: they work together and repeat."), "p", "note")}</div>
    <div class="panel"><p class="kicker">{L(("경험이 이어지는 방식", "How experience carries forward"))}</p><ol class="flow">{flow}</ol></div>
  </div>
  <div class="example"><h3 class="h-sm">{L(("예시 · 미술 수업", "Example · an art class"))}</h3><ol class="ex-steps ex-3">{ex}</ol>
    {L(("기록은 그대로 남기되, ‘색에 약한 사람’처럼 단정하지 않습니다.", "The note stays as written, but never becomes a label like “bad with color.”"), "p", "note")}</div>
  <div class="ship"><p class="kicker">SERAship</p>
    <h3 class="h-md">{L(("SERA를 실제 활동과 결합한 프로그램", "SERA, built into real activities"))}</h3>
    {L(("미술, 학습, 진로, 일 등 각 분야의 활동 속에서 SERA를 실천합니다.", "Art, learning, careers, work: SERA happens inside the activity itself."), "p", "ship-lede")}
    <ol class="ship-steps">{steps}</ol>
    <ul class="aud">{aud}</ul>
  </div>
</div></section>'''

    pr = "".join(f'<li class="prm"><span class="prm-n">{i + 1}</span>{L(t, "h3")}{L(d, "p")}</li>' for i, (t, d) in enumerate(PROMISES))
    ai = "".join(f"<li>{L(x)}</li>" for x in AI_RULES)
    promises = f'''
<section class="sec sec-tint" id="promises"><div class="wrap">
  {head(("참여자와의 약속", "Our promises"), ("SERA의 주인은 참여자입니다", "Participants come first"))}
  <ol class="prms">{pr}</ol>
  <div class="split split-even">
    <div class="panel"><h3 class="h-sm">{L(("AI는 참고 자료입니다", "AI is only a reference"))}</h3><ul class="ticks">{ai}</ul></div>
    <div class="panel"><h3 class="h-sm">{L(("안전이 먼저입니다", "Safety first"))}</h3>
      {L(("SERAship은 상담이나 치료가 아닙니다. 위기 상황에는 전문기관과 연계하며, 미성년자 프로그램은 보호자와 본인의 동의를 함께 받습니다.", "SERAship is not counseling or therapy. In a crisis we refer to specialists, and programs for minors need both guardian and participant consent."), "p")}</div>
  </div>
</div></section>'''

    recs = "".join(f'<li class="rec rec-{i}"><span class="rec-tag">{L(t)}</span><h3>{n}</h3>{L(d, "p")}</li>' for i, (n, t, d) in enumerate(RECORDS))
    vals = "".join(f'<li>{L(t, "b")}{L(d, "span")}</li>' for t, d in RECORD_VALUES)
    records = f'''
<section class="sec" id="records"><div class="wrap">
  {head(("기록", "Records"), ("기록이 나의 이야기가 됩니다", "Your records become your story"), ("기록의 주인은 언제나 참여자이며, 공개 범위도 직접 정합니다.", "You always own your records, and you decide who sees them."))}
  <ol class="recs">{recs}</ol>
  <ul class="vals">{vals}</ul>
</div></section>'''

    eco = "".join(
        f'<li class="eco eco-{i}"><div class="eco-h"><h3>{e(x["name"])}</h3>{L(x["who"], "span", "eco-who")}</div>{L(x["what"], "p")}</li>'
        for i, x in enumerate(ECOSYSTEM))
    models = "".join(f'<li class="mdl"><span class="mdl-k">SERA</span><h3>{m}</h3>{L(w, "span", "mdl-w")}{L(d, "p")}</li>' for m, w, d in MODELS)
    together = f'''
<section class="sec sec-tint" id="together"><div class="wrap">
  {head(("SERA 생태계", "The SERA ecosystem"), ("One SERA · Multiple Models · Many Members", "One SERA · Multiple Models · Many Members"), ("하나의 철학 아래 분야별 모델과 현장의 운영기관이 연결됩니다.", "One philosophy, many field models, and local operators, all connected."))}
  <ol class="ecos">{eco}</ol>
  <h3 class="h-md models-h">{L(("분야별 SERA 모델", "SERA models by field"))}</h3>
  <ul class="mdls">{models}</ul>
  <div class="panel join join-wide">
    <div><h3 class="h-md">{L(("SERA와 함께할 기관을 찾습니다", "Join SERA"))}</h3>
      {L(("분야별 모델을 함께 만들 Partner, 현장에서 운영할 Member를 기다립니다.", "We're looking for Partners to build field models and Members to run programs locally."), "p")}</div>
    <div class="join-act"><a class="btn btn-solid" href="{SDX}/33" target="_top" rel="noopener">{L(("문의하기", "Get in touch"))} ↗</a><p class="mail-line">sdx@sdxfoundation.org</p></div>
  </div>
</div></section>'''

    traits = "".join(f'<li><span class="st-n">{i + 1}</span>{L(t, "b")}{L(d, "span")}</li>' for i, (t, d) in enumerate(SALIMIST["traits"]))
    stages = "".join(f'<li class="stg stg-{i}">{L(a, "b")}{L(b, "p")}</li>' for i, (a, b, c) in enumerate(SALIMIST["stages"]))
    salimist = f'''
<section class="sec" id="salimist"><div class="wrap">
  {head(("SERA가 만들어 가는 사람", "Who SERA helps people become"), ("살림가 (Salimist)", "The Salimist"), SALIMIST["def"])}
  <div class="split salim">
    <ol class="strs">{traits}</ol>
    <div class="salim-note">{L(("살림은 ‘살리다’에서 온 말입니다. 나와 이웃, 공동체와 자연을 함께 살리는 일을 뜻합니다.", "Salim comes from the Korean salida, to bring to life: caring for yourself, others, community and nature together."), "p")}</div>
  </div>
  <ol class="stgs">{stages}</ol>
  <p class="motto">Discover Yourself · Grow Together · Become Salim</p>
</div></section>'''

    lines = "".join(f"<li>{L(DECLARATION[i])}</li>" for i in (0, 1, 3, 4))
    declaration = f'''
<section class="decl" id="declaration"><div class="wrap">
  <p class="kicker kicker-light">{L(("SERA 선언", "The SERA declaration"))}</p>
  <ol class="decl-list">{lines}</ol>
</div></section>'''

    rows = "".join(f'<div class="g-row"><dt>{L(t)}</dt><dd>{L(d)}</dd></div>' for t, d, _ in GLOSSARY if t[0] in GLOSS)
    glossary = f'''<section class="sec" id="glossary"><div class="wrap">
  {head(("용어", "Glossary"), ("SERA에서 쓰는 말", "Words used in SERA"))}<dl class="gloss">{rows}</dl></div></section>'''

    return hero + about + four + way + promises + records + together + salimist + declaration + glossary
