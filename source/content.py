# -*- coding: utf-8 -*-
"""Bilingual content for the SERA site.

Every text value is a (korean, english) tuple. Body blocks are:
  ("p", (ko, en))            paragraph
  ("h", (ko, en))            small label heading inside an article
  ("ul", [(ko, en), ...])    bullet list
  ("ol", [(ko, en), ...])    numbered list
  ("cl", [(ko, en), ...])    charter clauses, numbered ① ② ③
"""

# ---------------------------------------------------------------- charter
CHARTER_META = {
    "title": ("SERA 기본헌장", "SERA Charter"),
    "motto": ("자신을 이해하고, 서로를 공감하며, 함께 영글어 가는 삶",
              "A life of understanding yourself, empathizing with one another, and ripening together"),
    "version": ("문서 버전: v1.0 초안", "Document version: v1.0 draft"),
}

CHARTER_PREAMBLE = [
    ("모든 사람은 저마다 고유한 가치와 가능성을 지닌다.",
     "Every person holds a worth and a potential that are uniquely their own."),
    ("자신을 있는 그대로 이해하고 받아들이는 자신감은 자기 삶을 스스로 정의하는 출발점이다. 자신을 이해하는 사람은 자신과 다른 타인의 크기와 관점을 인정하고 공감할 수 있다. 어떤 상황에서도 새로운 시작을 찾고, 작은 성취를 쌓아 가는 과정에서 사람은 자라고 영글어 간다.",
     "The confidence to understand and accept oneself as one is, is the starting point for defining one's own life. A person who understands themselves can acknowledge and empathize with the stature and perspectives of others who differ from them. People grow and ripen as they find a new beginning in any situation and build up small achievements."),
    ("SERA는 모든 사람이 이러한 삶의 여정을 스스로 만들어 가도록 돕는 파트너이다.",
     "SERA is a partner that helps every person shape this journey of life for themselves."),
    ("SERA는 Story, Empathy, Resilience, Achievement의 네 가지 원칙을 바탕으로 개인의 자기 이해와 자율성, 상호 공감과 지속적인 성숙을 지원한다.",
     "Grounded in four principles, Story, Empathy, Resilience and Achievement, SERA supports each person's self-understanding and autonomy, mutual empathy, and continuing maturity."),
    ("이에 SERA의 모든 교육과정, SERAship, SERA Agent, My SERA Agent 및 관련 서비스는 다음의 기본헌장을 준수한다.",
     "Accordingly, every SERA curriculum, SERAship, SERA Agent, My SERA Agent and related service shall abide by the following Charter."),
]

CHARTER = [
    {"label": ("제1장", "Chapter 1"), "title": ("총칙", "General Provisions"), "articles": [
        (1, ("목적", "Purpose"), [("p", (
            "본 헌장은 SERA의 철학과 핵심 원칙을 확립하고, SERA의 모든 활동과 서비스가 일관된 목적과 기준에 따라 설계·운영되도록 하는 최상위 규범이다.",
            "This Charter establishes SERA's philosophy and core principles. It is the highest norm ensuring that every SERA activity and service is designed and operated according to a consistent purpose and standard."))]),
        (2, ("SERA의 정의", "Definition of SERA"), [("p", (
            "SERA는 자신을 있는 그대로 받아들일 수 있는 자신감을 바탕으로 자신을 정의하고 주변과 공감하며, 끊임없이 새로운 작은 성취를 이루면서 자라고 영글어 가도록 돕는 파트너이다.",
            "SERA is a partner that helps people, through the confidence to accept themselves as they are, to define themselves, empathize with those around them, and grow and ripen by continually reaching new small achievements."))]),
        (3, ("적용 범위", "Scope"), [("cl", [
            ("본 헌장은 SERA의 모든 교육과정, SERAship, SERA Agent, My SERA Agent 및 관련 서비스의 기획·설계·개발·운영·평가에 적용한다.",
             "This Charter applies to the planning, design, development, operation and evaluation of every SERA curriculum, SERAship, SERA Agent, My SERA Agent and related service."),
            ("모든 하위 규정과 실행 지침은 본 헌장의 원칙에 부합해야 한다.",
             "All subordinate regulations and implementation guidelines must conform to the principles of this Charter."),
            ("기술적 효율성, 서비스 성과 및 운영상의 편의는 본 헌장의 기본 원칙을 침해하는 근거가 될 수 없다.",
             "Technical efficiency, service performance and operational convenience can never justify infringing the basic principles of this Charter."),
        ])]),
    ]},
    {"label": ("제2장", "Chapter 2"), "title": ("SERA의 네 가지 원칙", "The Four Principles of SERA"), "articles": [
        (4, ("Story — 나를 이해하고 나의 삶을 정의한다", "Story: I understand myself and define my own life"), [("cl", [
            ("SERA는 개인이 자신의 경험과 감정, 능력과 한계, 관심과 가능성을 탐색하도록 돕는다.",
             "SERA helps individuals explore their experiences and emotions, abilities and limits, interests and possibilities."),
            ("개인이 자신의 고유한 가치를 이해하고 받아들이며, 스스로 삶의 의미와 방향을 만들어 가도록 지원한다.",
             "It supports individuals in understanding and accepting their own unique worth and in shaping the meaning and direction of their lives for themselves."),
            ("개인의 이야기는 성급한 평가나 고정된 규정의 근거가 되어서는 안 된다. 이야기는 자기 이해와 새로운 가능성 발견의 출발점으로 활용한다.",
             "A person's story must never become grounds for hasty judgment or a fixed label. A story is used as the starting point for self-understanding and for discovering new possibilities."),
        ])]),
        (5, ("Empathy — 서로의 다름을 인정하고 공감한다", "Empathy: We acknowledge and empathize with one another's differences"), [("cl", [
            ("SERA는 사람마다 서로 다른 능력과 관점, 처지와 속도, 가능성이 있음을 존중한다.",
             "SERA respects that every person has different abilities and perspectives, circumstances and pace, and possibilities."),
            ("자신의 기준만으로 타인을 판단하지 않고, 상대방의 경험과 관점을 이해하도록 돕는다.",
             "It helps people understand the experiences and perspectives of others instead of judging them by their own standards alone."),
            ("비교와 경쟁에 따른 우열의 판단보다 상호 존중과 공감, 함께 살아가는 지혜를 지향한다.",
             "It pursues mutual respect, empathy and the wisdom of living together rather than ranking people through comparison and competition."),
        ])]),
        (6, ("Resilience — 어떤 상황에서도 다시 시작한다", "Resilience: We begin again in any situation"), [("cl", [
            ("SERA는 실패와 실수, 변화와 어려움을 경험의 일부로 받아들이도록 돕는다.",
             "SERA helps people accept failure and mistakes, change and hardship as part of experience."),
            ("개인이 현재의 상황을 새로운 출발점으로 삼고, 그 안에서 자신이 선택할 수 있는 행동을 발견하도록 지원한다.",
             "It supports individuals in treating their present situation as a new starting point and in discovering the actions they can choose within it."),
            ("다시 시작할 용기와 스스로 대응할 수 있다는 믿음을 기르도록 돕는다.",
             "It helps people build the courage to begin again and the belief that they can respond for themselves."),
            ("현실의 어려움과 제약을 가볍게 여기거나 개인에게 모든 책임을 돌려서는 안 된다.",
             "Real difficulties and constraints must never be taken lightly, nor may all responsibility be placed on the individual."),
        ])]),
        (7, ("Achievement — 작은 성취를 통해 자라고 영글어 간다", "Achievement: We grow and ripen through small achievements"), [("cl", [
            ("SERA는 개인이 실천할 수 있는 작은 목표를 세우고, 시도하고, 경험하며, 배우도록 돕는다.",
             "SERA helps individuals set small goals they can act on, then try, experience and learn."),
            ("작은 성취의 축적을 통해 자신에 대한 신뢰와 새로운 가능성을 키우도록 지원한다.",
             "It supports people in building trust in themselves and new possibilities through an accumulation of small achievements."),
            ("성과의 크기와 속도만으로 개인의 가치를 판단하지 않는다.",
             "It never judges a person's worth by the size or speed of their results alone."),
            ("개인이 자신의 변화와 성장을 돌아보고, 각자의 속도로 자라고 영글어 가도록 돕는다.",
             "It helps individuals look back on their change and growth, and grow and ripen at their own pace."),
        ])]),
    ]},
    {"label": ("제3장", "Chapter 3"), "title": ("모든 SERA 과정의 공통 의무", "Common Duties of Every SERA Program"), "articles": [
        (8, ("질문과 발견", "Questions and Discovery"), [("cl", [
            ("SERA의 질문은 실제 경험과 맥락에 기반해야 한다.",
             "SERA's questions must be grounded in real experience and context."),
            ("질문은 개인이 스스로 관찰하고 생각하며 새로운 의미를 발견하도록 돕는 방향으로 설계한다.",
             "Questions are designed to help individuals observe, think and discover new meaning for themselves."),
            ("질문을 통해 특정한 답이나 결론을 강요하거나, 충분한 근거 없이 개인의 성격·능력·적성·미래를 단정해서는 안 된다.",
             "Questions must never force a particular answer or conclusion, nor pronounce on a person's character, ability, aptitude or future without sufficient grounds."),
        ])]),
        (9, ("자기 결정권과 자율성", "Self-Determination and Autonomy"), [("cl", [
            ("SERA는 개인이 자신의 삶에 관한 선택과 판단을 스스로 내릴 수 있도록 지원한다.",
             "SERA supports individuals in making their own choices and judgments about their lives."),
            ("SERA는 개인의 생각과 감정, 선택을 대신 결정하거나 일방적으로 규정하지 않는다.",
             "SERA does not decide a person's thoughts, feelings or choices on their behalf, nor define them unilaterally."),
            ("개인은 질문에 답하지 않거나, 제안된 활동을 거절하거나, 자신의 생각을 수정할 수 있다.",
             "Individuals may decline to answer a question, refuse a suggested activity, or change their minds."),
        ])]),
        (10, ("관찰과 해석의 구분", "Separating Observation from Interpretation"), [("cl", [
            ("SERA는 관찰된 사실과 개인이 직접 표현한 내용, AI가 추론한 내용을 구분해야 한다.",
             "SERA must distinguish observed facts, what the individual has expressed directly, and what AI has inferred."),
            ("제한된 경험이나 단일 장면을 근거로 개인의 내면이나 지속적인 행동 특성을 확정해서는 안 된다.",
             "A person's inner life or lasting behavioral traits must never be settled on the basis of limited experience or a single scene."),
            ("개인에 관한 해석은 필요한 경우 추가 질문과 반복된 경험을 통해 확인하고 수정해야 한다.",
             "Interpretations about an individual must, where needed, be checked and revised through further questions and repeated experience."),
        ])]),
        (11, ("경험과 기록의 활용", "Using Experiences and Records"), [("cl", [
            ("SERA는 개인의 경험과 성찰, 시도와 성취를 연결하여 자기 이해와 지속적인 성장을 지원한다.",
             "SERA connects a person's experiences and reflections, attempts and achievements to support self-understanding and continuing growth."),
            ("기록은 개인이 자신의 변화 과정을 이해하고 미래의 선택에 활용할 수 있도록 관리한다.",
             "Records are managed so that individuals can understand their own process of change and draw on it for future choices."),
            ("개인의 기록을 성급한 평가, 고정된 분류 또는 개인의 가능성을 제한하는 목적으로 사용해서는 안 된다.",
             "A person's records must never be used for hasty evaluation, fixed classification, or to limit their possibilities."),
            ("기록의 수집·보관·활용은 개인정보 보호와 관련 법령을 준수해야 하며, 이용 목적과 범위는 사용자에게 명확히 안내해야 한다.",
             "Collecting, storing and using records must comply with privacy protection and related laws, and the purpose and scope of use must be clearly explained to users."),
        ])]),
        (12, ("지속적인 검증과 개선", "Continuous Review and Improvement"), [("cl", [
            ("SERA의 모든 기능과 프로그램은 자기 이해, 공감, 다시 시작하는 용기, 작은 성취라는 목적에 기여하는지 검토해야 한다.",
             "Every SERA feature and program must be reviewed for whether it contributes to its purposes: self-understanding, empathy, the courage to begin again, and small achievements."),
            ("사용자의 만족도와 참여도뿐 아니라 실제 자기 이해와 행동 변화에 도움이 되는지도 살펴야 한다.",
             "Beyond user satisfaction and engagement, it must also be examined whether it actually helps self-understanding and behavioral change."),
            ("효과가 확인되지 않거나 헌장의 원칙에 어긋나는 기능과 운영 방식은 개선하거나 중단해야 한다.",
             "Features and practices whose effect is unconfirmed, or that conflict with the Charter's principles, must be improved or discontinued."),
        ])]),
    ]},
    {"label": ("제4장", "Chapter 4"), "title": ("서비스별 준수 의무", "Service-Specific Duties"), "articles": [
        (13, ("SERAship의 의무", "Duties of SERAship"), [("cl", [
            ("SERAship은 실제 활동과 경험을 자기 이해의 기회로 연결해야 한다.",
             "SERAship must connect real activities and experiences to opportunities for self-understanding."),
            ("활동의 성과뿐 아니라 과정에서 나타나는 관심, 선택, 시도, 성찰과 작은 성취를 소중히 다룬다.",
             "It values not only the results of an activity but the interests, choices, attempts, reflections and small achievements that appear along the way."),
            ("교육과정은 참여자가 자신의 속도로 배우고, 스스로 선택하며, 작은 성취를 경험할 수 있도록 설계한다.",
             "Curricula are designed so participants can learn at their own pace, make their own choices and experience small achievements."),
        ])]),
        (14, ("SERA Agent의 의무", "Duties of SERA Agent"), [("cl", [
            ("SERA Agent는 본 헌장을 질문 생성과 대화 운영의 기본 원칙으로 준수해야 한다.",
             "SERA Agent must follow this Charter as the basic principle for generating questions and conducting conversations."),
            ("질문은 사용자의 실제 경험과 답변, 해당 활동에 관한 지식을 바탕으로 생성해야 한다.",
             "Questions must be generated from the user's real experiences and answers, and from knowledge of the activity in question."),
            ("질문의 개수보다 적절성과 답변의 부담을 우선하며, 필요한 순간에 이해하기 쉬운 질문을 제공해야 한다.",
             "Relevance and the burden of answering come before the number of questions, and easy-to-understand questions should be offered at the moment they are needed."),
            ("사용자의 답변을 특정한 결론으로 유도하거나, 불확실한 해석을 사실처럼 제시해서는 안 된다.",
             "It must never steer a user's answers toward a particular conclusion, nor present uncertain interpretations as fact."),
            ("모든 대화는 사용자의 자기 이해와 자율적인 발견을 지원하는 방향으로 이어져야 한다.",
             "Every conversation must move in a direction that supports the user's self-understanding and autonomous discovery."),
        ])]),
        (15, ("My SERA Agent의 의무", "Duties of My SERA Agent"), [("cl", [
            ("My SERA Agent는 사용자의 시간에 따른 경험과 변화를 연결하여 자기 이해를 돕는다.",
             "My SERA Agent supports self-understanding by connecting the user's experiences and changes over time."),
            ("과거 기록을 활용할 때는 해당 기록의 맥락과 현재 상황을 함께 고려해야 한다.",
             "When drawing on past records, it must consider both the context of those records and the present situation."),
            ("반복적으로 나타나는 특징과 일시적인 반응을 구분하고, 충분한 근거 없이 개인의 정체성이나 미래를 규정해서는 안 된다.",
             "It must distinguish recurring traits from passing reactions, and must never define a person's identity or future without sufficient grounds."),
            ("개인이 자신의 기록과 해석을 확인하고 필요한 경우 수정할 수 있도록 해야 한다.",
             "It must let individuals review their own records and interpretations and correct them where needed."),
            ("My SERA Agent는 개인의 삶을 대신 설계하는 존재가 아니라, 개인이 자신의 삶을 스스로 만들어 가도록 돕는 파트너로 기능해야 한다.",
             "My SERA Agent must act as a partner that helps individuals build their own lives, never as something that designs their lives for them."),
        ])]),
    ]},
    {"label": ("제5장", "Chapter 5"), "title": ("준수와 개정", "Compliance and Amendment"), "articles": [
        (16, ("헌장 준수와 적합성 검토", "Compliance and Conformity Review"), [("cl", [
            ("SERA의 신규 기능과 프로그램은 설계 단계에서 본 헌장과의 적합성을 검토해야 한다.",
             "New SERA features and programs must be reviewed for conformity with this Charter at the design stage."),
            ("운영 중 헌장에 어긋나는 문제가 발견되면 원인을 확인하고 개선 조치를 마련해야 한다.",
             "If a problem that conflicts with the Charter is found during operation, its cause must be identified and corrective measures prepared."),
            ("구체적인 검토 절차와 책임 주체는 SERA 운영규정에서 정한다.",
             "Specific review procedures and responsible parties are set out in the SERA Operating Regulations."),
        ])]),
        (17, ("개정과 버전 관리", "Amendment and Version Control"), [("cl", [
            ("본 헌장은 SERA의 핵심 철학과 기본 원칙을 유지하면서 필요한 경우 개정할 수 있다.",
             "This Charter may be amended when necessary while preserving SERA's core philosophy and basic principles."),
            ("헌장을 개정할 때는 개정 사유와 변경 내용, 시행일을 기록하고 버전을 관리한다.",
             "When the Charter is amended, the reason, the changes and the effective date are recorded and versions are managed."),
            ("하위 규정과 실행 지침은 헌장 개정 시 적합성을 재검토해야 한다.",
             "Subordinate regulations and implementation guidelines must be re-reviewed for conformity whenever the Charter is amended."),
            ("질문 생성 방식이나 기술적 구현의 변경만으로 헌장의 핵심 원칙이 임의로 변경되어서는 안 된다.",
             "The Charter's core principles must never be changed arbitrarily merely through changes in how questions are generated or how technology is implemented."),
        ])]),
    ]},
]

CHARTER_ADDENDA = [
    ("본 헌장은 승인된 시행일부터 적용한다.",
     "This Charter applies from its approved effective date."),
    ("본 헌장의 구체적인 실행을 위한 SERA 운영규정 및 기술별 실행 지침은 별도로 정한다.",
     "The SERA Operating Regulations and technology-specific implementation guidelines for carrying out this Charter are set out separately."),
    ("본 헌장은 SERA의 철학과 모든 서비스의 설계·운영을 판단하는 최상위 기준으로 활용한다.",
     "This Charter serves as the highest standard for judging SERA's philosophy and the design and operation of all its services."),
]

# ---------------------------------------------------------------- the four
# Used for the home page cards and for Articles 5 to 8 of the Principles.
FOUR = [
    {
        "key": "S", "name": "Story", "art": 5,
        "ko_name": "이야기",
        "charter": CHARTER[1]["articles"][0][1],
        "title": ("경험을 자신의 이야기로 만드는 원리", "Turning experience into one's own story"),
        "purpose": ("자기이해", "Self-understanding"),
        "concept": ("모든 경험이 저절로 자신의 이야기가 되지는 않는다. 경험을 관찰하고 기록하며 의미를 되짚을 때, 사람은 선택·행동·감정·변화 사이의 관계를 이해한다. Story는 외부 기준으로 삶을 설명하는 것이 아니라, 자신의 관점에서 경험의 의미를 만들어 가는 과정이다.",
                    "Not every experience becomes one's story on its own. When we observe and record an experience and revisit its meaning, we come to understand how our choices, actions, feelings and changes relate. Story is not explaining life by outside standards. It is the process of making meaning from experience from one's own point of view."),
        "practice": [
            ("경험을 성공과 실패라는 두 결과만으로 구분하지 않는다.", "Do not sort experiences into just two outcomes, success and failure."),
            ("사실, 감정, 해석, 판단을 구별해 살펴본다.", "Look at facts, feelings, interpretations and judgments separately."),
            ("사소한 일상과 작은 변화도 관찰과 기록의 대상으로 인정한다.", "Treat small everyday moments and small changes as worth observing and recording."),
            ("과거의 경험을 현재의 관점에서 다시 해석할 수 있다.", "Past experiences can be reinterpreted from today's perspective."),
            ("자신의 이야기를 완성된 정체성이 아니라 계속 수정되는 과정으로 이해한다.", "Understand your story as a process that keeps being revised, not a finished identity."),
        ],
        "questions": [
            ("오늘 실제로 무슨 일이 있었는가?", "What actually happened today?"),
            ("그때 무엇을 느끼고 어떻게 행동했는가?", "What did I feel then, and how did I act?"),
            ("왜 그렇게 생각하고 행동했을까?", "Why did I think and act that way?"),
            ("이 경험은 나에 대해 무엇을 알려주는가?", "What does this experience tell me about myself?"),
            ("지금 다시 보면 무엇이 다르게 보이는가?", "Looking again now, what looks different?"),
        ],
        "change": ("경험을 소비하고 지나치는 데서 벗어나 삶을 이해하는 자료로 활용한다. 기록은 과거를 보관하는 수단이자 자신의 변화를 발견하는 수단이 된다.",
                   "Instead of consuming experiences and moving on, people use them as material for understanding their lives. Records become both a way to keep the past and a way to discover one's own change."),
    },
    {
        "key": "E", "name": "Empathy", "art": 6,
        "ko_name": "공감",
        "charter": CHARTER[1]["articles"][1][1],
        "title": ("자신과 타인, 세계를 이해하는 원리", "Understanding oneself, others and the world"),
        "purpose": ("관계이해", "Understanding relationships"),
        "concept": ("공감은 무조건 동의하거나 상대의 감정을 그대로 받아들이는 것이 아니다. 서로 다른 경험과 관점이 있음을 인정하고 그 차이의 이유를 이해하려는 능력이다. 공감은 자신의 감정과 한계를 이해하는 자기공감에서 출발해 타인, 공동체, 자연으로 확장된다.",
                    "Empathy is not agreeing unconditionally or taking on another person's feelings as they are. It is the ability to recognize that people have different experiences and perspectives and to try to understand the reasons for those differences. Empathy begins with self-empathy, understanding one's own feelings and limits, and extends to others, communities and nature."),
        "practice": [
            ("자신의 감정을 옳고 그름으로 즉시 판단하지 않는다.", "Do not immediately judge your own feelings as right or wrong."),
            ("타인의 행동을 평가하기 전에 그의 상황과 관점을 살핀다.", "Before evaluating someone's behavior, consider their situation and perspective."),
            ("서로 다른 의견과 가치관이 존재할 수 있음을 인정한다.", "Accept that different opinions and values can coexist."),
            ("개인의 행동이 다른 사람과 환경에 미치는 영향을 살핀다.", "Notice how individual actions affect other people and the environment."),
            ("공감을 강요하거나 감정 표현 방식을 획일화하지 않는다.", "Do not force empathy or make everyone express feelings the same way."),
        ],
        "questions": [
            ("나는 지금 무엇을 느끼는가?", "What am I feeling right now?"),
            ("상대는 어떤 상황에서 이렇게 행동했을까?", "In what situation did the other person act this way?"),
            ("나와 상대는 무엇을 다르게 보는가?", "What do we see differently?"),
            ("나의 선택은 다른 사람에게 어떤 영향을 미치는가?", "How do my choices affect other people?"),
            ("내가 속한 공동체와 자연은 나의 행동과 어떻게 연결되는가?", "How are my community and nature connected to what I do?"),
        ],
        "change": ("자신의 관점만으로 세상을 해석하는 태도에서 벗어나, 관계를 이해하고 차이를 조정하며 함께 사는 방법을 모색한다.",
                   "People move beyond reading the world through their own perspective alone, and look for ways to understand relationships, work through differences and live together."),
    },
    {
        "key": "R", "name": "Resilience", "art": 7,
        "ko_name": "회복력",
        "charter": CHARTER[1]["articles"][2][1],
        "title": ("경험을 통해 다시 대응하는 원리", "Responding anew through experience"),
        "purpose": ("변화대응", "Responding to change"),
        "concept": ("Resilience는 어려움이 없는 상태나 무조건 견디는 능력이 아니다. 실패·변화·상실·불확실성 앞에서 현재 상황을 있는 그대로 받아들이고, 필요한 도움과 자원을 활용해 새로운 대응을 찾아가는 능력이다. 이는 타고난 성격이 아니라 경험과 관계 속에서 발전하는 역량이다.",
                    "Resilience is neither the absence of hardship nor the ability to endure no matter what. It is the ability, in the face of failure, change, loss and uncertainty, to accept the present situation as it is and find a new response using the help and resources one needs. It is not an inborn trait but a capacity that develops through experience and relationships."),
        "practice": [
            ("실패를 개인의 가치에 대한 최종 평가로 취급하지 않는다.", "Do not treat failure as a final verdict on a person's worth."),
            ("어려움의 원인을 무조건 개인의 노력 부족으로 돌리지 않는다.", "Do not automatically blame difficulty on a lack of personal effort."),
            ("통제할 수 있는 요소와 통제하기 어려운 요소를 구분한다.", "Separate what you can control from what is hard to control."),
            ("도움을 요청하고 외부 자원을 활용하는 것을 역량으로 인정한다.", "Recognize asking for help and using outside resources as a strength."),
            ("휴식, 중단, 방향 수정도 합리적 선택이 될 수 있음을 인정한다.", "Accept that resting, stopping or changing direction can be sound choices."),
        ],
        "questions": [
            ("무엇이 나를 어렵게 만들었는가?", "What made this hard for me?"),
            ("그중 바꿀 수 있는 것과 바꾸기 어려운 것은 무엇인가?", "Which parts can I change, and which are hard to change?"),
            ("이번 경험에서 새로 알게 된 것은?", "What did I learn from this experience?"),
            ("누구에게 어떤 도움을 청할 수 있는가?", "Whom can I ask for help, and what kind?"),
            ("다음에는 무엇을 다르게 시도할까?", "What will I try differently next time?"),
        ],
        "change": ("실패를 회피하거나 자신을 비난하는 데 머무르지 않고, 경험을 분석해 새로운 대응을 찾는다. 다만 SERA는 모든 어려움을 성장 기회로 미화하지 않는다. 부당한 환경이나 구조적 문제는 개선해야 할 대상으로 정당하게 인식한다.",
                   "Instead of avoiding failure or blaming themselves, people analyze their experience and find new responses. SERA does not, however, glorify every hardship as a chance to grow. Unjust environments and structural problems are rightly recognized as things that need to be fixed."),
    },
    {
        "key": "A", "name": "Achievement", "art": 8,
        "ko_name": "성취",
        "charter": CHARTER[1]["articles"][3][1],
        "title": ("달란트를 실천하며 삶의 의미를 이루는 원리", "Realizing life's meaning by practicing one's talent"),
        "purpose": ("삶의 구현", "Living it out"),
        "concept": ("Achievement는 목표에 도달한 순간이 아니라, 자신의 달란트를 발견하고 매일 실천하며 그 의미를 축적해 가는 과정 전체다. 실천이 경험을 쌓고, 경험이 달란트를 키우며, 성장한 달란트가 더 깊은 실천으로 이어진다. 이 순환을 통해 개인은 얕은 노동에서 깊은 노동으로 나아가고, 자기 삶의 장르마스터이자 살림가로 성장할 수 있다.",
                    "Achievement is not the moment a goal is reached. It is the whole process of discovering one's talent (dallant), practicing it every day and accumulating its meaning. Practice builds experience, experience grows talent, and grown talent leads to deeper practice. Through this cycle a person can move from a Shallow Job to a Deep Job and grow into the Genre Master of their own life and a Salimist."),
        "practice": [
            ("타인의 기준보다 자신의 관심, 기쁨, 몰입, 기여 가능성에서 출발한다.", "Start from your own interests, joy, immersion and ability to contribute rather than other people's standards."),
            ("거창한 목표보다 달란트를 매일의 삶에서 실천하는 것을 중시한다.", "Value practicing your talent in daily life over grand goals."),
            ("외부의 보상이나 인정이 없어도 실천 자체에서 의미를 발견한다.", "Find meaning in the practice itself, even without outside reward or recognition."),
            ("처음부터 목표를 확정하기보다 실천을 이어 가며 방향을 구체화한다.", "Rather than fixing a goal from the start, let direction take shape as you keep practicing."),
            ("성취의 형태와 속도를 타인이나 사회적 성공 기준과 비교하지 않는다.", "Do not compare the shape or speed of your achievement with others or with social measures of success."),
        ],
        "questions": [
            ("무엇을 할 때 결과와 관계없이 만족과 의미를 느끼는가?", "When do I feel satisfaction and meaning regardless of the result?"),
            ("오늘 나의 달란트를 어떻게 실천했는가?", "How did I practice my talent today?"),
            ("작은 실천이 쌓이며 내게 어떤 변화가 일어나는가?", "What changes in me as small practices add up?"),
            ("나는 어디로 나아가고 있으며, 그 방향은 나에게 어떤 의미인가?", "Where am I heading, and what does that direction mean to me?"),
        ],
        "change": ("성취를 미래의 보상으로 미루지 않고, 매일의 실천에서 의미와 만족을 발견한다. 외부 평가에 의존하지 않는 힘을 기르고, 그 달란트가 자연스럽게 타인과 세상에 대한 기여로 확장되는 것을 경험한다.",
                   "People stop postponing achievement as a future reward and find meaning and satisfaction in daily practice. They build strength that does not depend on outside evaluation, and experience their talent naturally extending into a contribution to others and the world."),
    },
]

CYCLE = [
    (("경험하기", "Experience"), ("일상에서 경험을 발견한다.", "Discover experiences in everyday life."), "S"),
    (("관찰하고 기록하기", "Observe and record"), ("사실, 감정, 생각을 구분해 기록한다.", "Record facts, feelings and thoughts separately."), "S"),
    (("이해하고 해석하기", "Understand and interpret"), ("자신과 타인의 관점을 살펴본다.", "Look at your own and others' perspectives."), "E"),
    (("대응 방법 찾기", "Find a response"), ("어려움과 가능성을 검토한다.", "Weigh the difficulties and the possibilities."), "R"),
    (("행동으로 옮기기", "Take action"), ("작은 목표를 정하고 실천한다.", "Set a small goal and act on it."), "A"),
    (("돌아보고 재해석하기", "Reflect and reinterpret"), ("결과를 확인하고 다음 질문을 만든다.", "Check the result and form the next question."), "SERA"),
]

# ---------------------------------------------------------------- principles
P_META = {
    "title": ("SERA 기본원칙", "SERA Principles"),
    "subtitle": ("Principles for Human Growth and Life Contribution", "Principles for Human Growth and Life Contribution"),
    "date": ("2026년 10월 9일 · v1.1", "October 9, 2026 · v1.1"),
}


def four_body(f):
    return [
        ("h", ("기본 개념", "Basic concept")), ("p", f["concept"]),
        ("h", ("실천 원칙", "Practice")), ("ul", f["practice"]),
        ("h", ("핵심 질문", "Key questions")), ("ul", f["questions"]),
        ("h", ("기대하는 변화", "Expected change")), ("p", f["change"]),
    ]


PRINCIPLES = [
    {"label": ("제1장", "Chapter 1"), "title": ("SERA의 정의와 목적", "Definition and Purpose of SERA"), "articles": [
        (1, ("SERA의 정의", "Definition of SERA"), [
            ("p", ("SERA는 Story, Empathy, Resilience, Achievement의 네 개념을 바탕으로 한 성장 프레임워크다. 사람이 자신의 삶을 이해하고, 타인과 세계에 공감하며, 변화와 어려움에 대응하고, 자신의 가능성을 구체적인 실천과 성취로 연결하도록 지원한다.",
                   "SERA is a growth framework built on four concepts: Story, Empathy, Resilience and Achievement. It supports people in understanding their own lives, empathizing with others and the world, responding to change and hardship, and turning their potential into concrete practice and achievement.")),
            ("p", ("SERA는 개인이 자신의 삶을 스스로 관찰하고 질문하며 자신만의 의미와 방향을 발견하도록 돕는다. 경쟁과 성장 중심의 머니로직을 넘어, 타인 및 생태계와 공존하며 삶의 풍요를 추구하는 살림로직의 주체가 되는 길을 연다.",
                   "SERA helps individuals observe and question their own lives and discover their own meaning and direction. Moving beyond a Money Logic centered on competition and growth, it opens the way to becoming an agent of Salim Logic, which pursues abundance in life while coexisting with others and with ecosystems.")),
        ]),
        (2, ("SERA의 목적", "Purposes of SERA"), [
            ("ol", [
                ("자기이해(Story): 자신의 경험, 감정, 관심, 가치관과 가능성을 발견한다.", "Self-understanding (Story): discover one's experiences, feelings, interests, values and potential."),
                ("관계이해(Empathy): 타인·사회·자연과의 관계 속에서 자신의 위치와 역할을 이해한다.", "Understanding relationships (Empathy): understand one's place and role in relation to others, society and nature."),
                ("변화대응(Resilience): 실패와 불확실성을 학습의 기회로 삼고 새로운 상황에 대응하는 힘을 기른다.", "Responding to change (Resilience): treat failure and uncertainty as chances to learn and build the strength to respond to new situations."),
                ("삶의 구현(Achievement): 발견한 의미와 가능성을 실제 행동과 성취로 연결한다.", "Living it out (Achievement): connect the meaning and potential one has found to real action and achievement."),
            ]),
            ("p", ("네 목적은 독립된 교육 항목이 아니다. 실제 삶에서 상호작용하며 반복적으로 발전하는 하나의 과정이다.",
                   "The four purposes are not separate subjects. They are a single process that interacts and develops repeatedly in real life.")),
        ]),
        (3, ("SERA가 지향하는 인간상", "The Person SERA Envisions"), [
            ("p", ("SERA가 지향하는 사람은 자신의 삶을 이해하고, 스스로 목표를 세우며, 그 결과에 책임지는 사람이다. 이 사람은 다음 특성을 발전시킨다.",
                   "The person SERA envisions understands their own life, sets their own goals and takes responsibility for the results. This person develops the following traits.")),
            ("ul", [
                ("자신의 경험을 돌아보고 스스로 질문한다.", "Looks back on their experiences and asks their own questions."),
                ("자신의 감정과 타인의 관점을 이해하려 노력한다.", "Tries to understand their own feelings and others' perspectives."),
                ("실패를 자신의 가치에 대한 최종 판정으로 받아들이지 않는다.", "Does not accept failure as a final verdict on their worth."),
                ("평균이 아닌 자기다운 모습, 곧 자신의 고유성을 발견한다.", "Discovers who they truly are, their own uniqueness, rather than an average."),
                ("과거 경험에 의해 설명될 수는 있어도 결정되지 않는다고 믿는다.", "Believes that past experience may explain them but does not determine them."),
                ("자신에게 중요한 것을 행동으로 옮기고, 그 영향이 타인·공동체·자연에 미치는 바를 고려한다.", "Acts on what matters to them and considers the effect on others, communities and nature."),
            ]),
            ("p", ("어떤 사람도 현재 상태로 고정된 존재가 아니다. SERA는 누구나 자신의 출발점에서 이 특성을 발견하고 키워 가도록 돕는다.",
                   "No one is fixed in their present state. SERA helps everyone discover and grow these traits from their own starting point.")),
        ]),
        (4, ("용어의 정의", "Definitions"), [
            ("p", ("이 원칙에서 운영기관은 SERAship을 설계·운영하는 기관을, 퍼실리테이터·멘토는 참여자의 관찰·질문·성찰·실천을 지원하는 사람을 말한다. 살림로직, ESGG, 달란트, 살림가 등 SERA 고유 용어는 부록(Appendix)에서 정의한다.",
                   "In these Principles, an operating organization is an organization that designs and runs a SERAship, and a facilitator or mentor is a person who supports participants' observation, questioning, reflection and practice. Terms specific to SERA, such as Salim Logic, ESGG, talent (dallant) and Salimist, are defined in the Appendix.")),
        ]),
    ]},
    {"label": ("제2장", "Chapter 2"), "title": ("SERA를 구성하는 네 가지 원리", "The Four Elements of SERA"),
     "articles": [(f["art"], (f["name"] + " — " + f["title"][0], f["name"] + ": " + f["title"][1]), four_body(f)) for f in FOUR]},
    {"label": ("제3장", "Chapter 3"), "title": ("SERA를 관통하는 기본원칙", "Principles Running Through SERA"),
     "intro": ("네 원리를 실제 프로그램에 적용할 때 다음 원칙을 공통으로 준수한다.", "When the four elements are applied in real programs, the following principles are observed in common."),
     "articles": [
        (9, ("자기주도성의 원칙", "Self-Direction"), [
            ("p", ("SERA의 주체는 참여자 자신이다. 교육자, 멘토, 부모, 운영기관은 참여자가 스스로 관찰하고 질문하며 의미를 발견하도록 지원한다.",
                   "The participant is the one at the center of SERA. Educators, mentors, parents and operating organizations support participants in observing, questioning and discovering meaning for themselves.")),
            ("ul", [
                ("지시보다 질문을 우선한다.", "Questions come before instructions."),
                ("정답의 전달보다 스스로 발견하는 과정을 중시한다.", "Discovering for oneself matters more than being handed the right answer."),
                ("외부 평가보다 자기이해를 우선한다.", "Self-understanding comes before outside evaluation."),
                ("참여자의 선택과 판단을 존중한다.", "Participants' choices and judgments are respected."),
            ]),
            ("p", ("자기주도성은 방임이 아니다. 도구, 환경, 피드백을 제공하되 최종 판단과 선택의 주체를 참여자로 남겨 두는 것이다.",
                   "Self-direction is not neglect. It means providing tools, environments and feedback while leaving the final judgment and choice with the participant.")),
        ]),
        (10, ("질문 우선의 원칙", "Questions First"), [
            ("p", ("질문은 지식을 확인하는 시험 도구가 아니라 자신과 세계를 새롭게 이해하는 도구다. 질문은 일상의 작은 불편, 예상과 다른 결과, 감정의 변화, 관계의 어긋남에서 출발할 수 있다. SERA는 정해진 질문에 답하는 것뿐 아니라 참여자가 스스로 새 질문을 만드는 능력을 중시한다.",
                   "A question is not a test of knowledge but a tool for understanding oneself and the world anew. Questions can start from small everyday discomforts, unexpected results, shifts in feeling or friction in relationships. SERA values not only answering set questions but participants' ability to form new questions of their own.")),
            ("p", ("운영자는 질문으로 참여자를 특정 결론에 유도하지 않는다. 이 원칙은 SERA가 지향하는 가치(제16조)를 전할 때에도 동일하게 적용된다.",
                   "Operators do not use questions to lead participants to particular conclusions. This applies equally when conveying the values SERA aspires to (Article 16).")),
        ]),
        (11, ("일상 경험 우선의 원칙", "Everyday Experience First"), [
            ("p", ("SERA의 출발점은 특별한 교육 콘텐츠가 아니라 참여자의 실제 삶이다. 그림, 운동, 독서, 일, 대화, 돌봄, 여행, 실패, 갈등 등 다양한 경험을 활용할 수 있다. 중요한 것은 도구가 아니라 그 경험을 통해 관찰하고, 질문하고, 해석하고, 다음 행동을 정하는 과정이다.",
                   "SERA starts from participants' real lives, not from special educational content. Drawing, sport, reading, work, conversation, caregiving, travel, failure and conflict can all be used. What matters is not the tool but the process of observing, questioning, interpreting and deciding the next action through that experience.")),
        ]),
        (12, ("과정 중심의 원칙", "Process over Outcome"), [
            ("p", ("SERA는 특정 시점의 결과만으로 사람을 평가하지 않는다. 새로운 발견, 생각의 변화, 실패와 시행착오, 중단과 재시도, 관심의 변화, 아직 풀지 못한 질문을 모두 기록과 학습의 대상으로 인정한다. 과정 중심은 결과를 무시한다는 뜻이 아니라, 결과만으로 전체 과정을 판단하지 않는다는 뜻이다.",
                   "SERA does not evaluate people by results at a single point in time. New discoveries, changes in thinking, failure and trial and error, stopping and retrying, shifting interests and still-unanswered questions are all recognized as worth recording and learning from. Focusing on process does not mean ignoring results. It means not judging the whole process by results alone.")),
        ]),
        (13, ("개인차와 고유성 존중의 원칙", "Respect for Individual Difference and Uniqueness"), [
            ("p", ("사람마다 경험, 환경, 발달 속도, 관심과 목표가 다르다. SERA는 모든 참여자에게 같은 변화나 성취를 요구하지 않는다. 비교가 필요할 때도 타인과의 순위보다 자신의 이전과 현재의 변화를 우선한다. 성장의 목적은 평균적인 사람이 아니라 자기다운 사람이 되는 것이다.",
                   "Every person differs in experience, environment, pace of development, interests and goals. SERA does not ask the same change or achievement of every participant. When comparison is needed, change between one's own past and present comes before ranking against others. The aim of growth is to become most fully oneself, not an average person.")),
        ]),
        (14, ("자기수용과 변화 가능성의 원칙", "Self-Acceptance and the Possibility of Change"), [
            ("p", ("SERA는 자신을 있는 그대로 이해하는 것과 현재에 머무르는 것을 구분한다. 감정, 한계, 실패를 인정하는 것은 변화의 포기가 아니라 현실적인 변화의 출발점이다. 참여자는 현재의 자신을 이해한 뒤 변화할 부분과 유지할 부분을 스스로 판단한다. SERA는 사람이 언제든 배우고 변화할 수 있다는 믿음 위에 선다.",
                   "SERA distinguishes understanding oneself as one is from staying where one is. Acknowledging feelings, limits and failures is not giving up on change but the realistic starting point for it. After understanding who they are now, participants decide for themselves what to change and what to keep. SERA stands on the belief that people can learn and change at any time.")),
        ]),
        (15, ("관계와 공동창조의 원칙", "Relationship and Co-Creation"), [
            ("p", ("개인의 삶은 가족, 친구, 동료, 지역사회, 자연과의 관계 속에서 형성되며, 성장 역시 혼자 완성되지 않는다. SERA는 참여자들이 서로의 경험과 질문을 존중하며 함께 배우는 문화를 지향한다. 다만 타인을 위한 희생을 성장의 조건으로 강요하지 않는다. 자신의 삶을 돌보는 것과 타인에게 기여하는 것은 함께 추구할 수 있는 가치다.",
                   "A person's life takes shape through relationships with family, friends, colleagues, local communities and nature, and growth is never completed alone. SERA aims for a culture in which participants learn together, respecting one another's experiences and questions. It does not, however, impose sacrifice for others as a condition of growth. Caring for one's own life and contributing to others are values that can be pursued together.")),
        ]),
        (16, ("기여와 살림의 지향", "Toward Contribution and Salim"), [
            ("p", ("SERA는 개인의 성장이 자연스럽게 타인, 공동체, 자연, 미래세대에 대한 기여로 확장되는 것을 지향한다. 이 지향은 ESGG 철학과 살림로직에 뿌리를 둔다.",
                   "SERA hopes that personal growth will naturally extend into contribution to others, communities, nature and future generations. This aspiration is rooted in the ESGG philosophy and Salim Logic.")),
            ("p", ("기여와 살림은 참여자에게 부과되는 의무가 아니라, 참여자가 스스로 탐색하도록 열어 두는 초대다. 운영자는 다음 질문을 제시할 수 있으나 답을 정하지 않는다.",
                   "Contribution and salim are not duties imposed on participants but an open invitation for them to explore. Operators may offer the following questions but do not decide the answers.")),
            ("ul", [
                ("내가 가진 가능성은 누구에게 도움이 될 수 있는가?", "Who could my potential help?"),
                ("나의 선택은 사회와 생태계에 어떤 영향을 미치는가?", "How do my choices affect society and ecosystems?"),
                ("내가 남기고 싶은 긍정적 영향은 무엇인가?", "What positive impact do I want to leave?"),
            ]),
        ]),
        (17, ("자율성과 안전의 원칙", "Autonomy and Safety"), [
            ("p", ("참여자는 자신의 경험을 어디까지 공개할지 선택한다. 개인 기록에는 민감한 감정, 가족관계, 실패와 갈등이 담길 수 있으므로 다음을 지킨다.",
                   "Participants choose how much of their experience to share. Because personal records may hold sensitive feelings, family relationships, failures and conflicts, the following are observed.")),
            ("ul", [
                ("기록의 공개 범위는 참여자가 결정한다.", "Participants decide who can see their records."),
                ("개인적 경험의 공개를 강요하지 않는다.", "No one is pressed to disclose personal experiences."),
                ("기록을 교육 목적 외에 임의로 사용하지 않는다.", "Records are not used at will for purposes other than education."),
                ("미성년자 프로그램은 보호자 동의와 참여자 본인의 이해·동의를 함께 확보한다.", "Programs for minors obtain both guardian consent and the participant's own understanding and consent."),
                ("기록의 보관, 열람, 공유, 삭제 기준을 사전에 명확히 한다.", "Rules for storing, viewing, sharing and deleting records are made clear in advance."),
            ]),
            ("p", ("SERA는 참여자를 이해하기 위한 과정이지, 사생활을 수집하는 제도가 아니다.",
                   "SERA is a process for understanding participants, not a system for collecting their private lives.")),
        ]),
        (18, ("기록과 성찰의 원칙", "Recording and Reflection"), [
            ("p", ("SERA는 일회성 경험을 장기적인 자기이해로 연결한다. 참여자는 경험, 질문, 생각의 변화, 행동과 결과를 지속적으로 기록한다. 기록은 참여 사실의 증명에 그치지 않고, 서로 다른 시점을 연결해 자신의 변화를 살펴보는 자료이자 포트폴리오의 기초가 된다.",
                   "SERA links one-off experiences to long-term self-understanding. Participants keep recording their experiences, questions, changes in thinking, actions and results. Records do more than prove participation. They connect different points in time so people can see their own change, and they form the basis of a portfolio.")),
        ]),
        (19, ("실천과 피드백의 원칙", "Practice and Feedback"), [
            ("p", ("성찰은 작은 실천으로 이어져야 한다. 참여자는 발견한 내용을 바탕으로 다음 행동을 정하고 그 결과를 다시 관찰한다. 타인의 피드백은 참여자를 통제하거나 평가하는 수단이 아니라, 미처 보지 못한 관점과 가능성을 확인하는 자료로 활용한다.",
                   "Reflection should lead to small practice. Participants decide their next action from what they have found and observe the result again. Feedback from others is used not to control or evaluate participants but as material for noticing perspectives and possibilities they had not yet seen.")),
        ]),
        (20, ("지속적 재해석의 원칙", "Continuous Reinterpretation"), [
            ("p", ("SERA는 한 번의 프로그램으로 완성되지 않는다. 새로운 경험은 과거를 다르게 이해하게 하고, 가치와 목표도 달라질 수 있다. 기록은 수정·보완될 수 있으며, 과거와 현재의 판단이 달라지는 것도 성장의 일부로 인정한다. SERA의 목표는 완성된 자아가 아니라 자신의 삶을 계속 새롭게 이해하고 만들어 가는 능력이다.",
                   "SERA is not completed in a single program. New experiences change how we understand the past, and values and goals can change too. Records can be revised and supplemented, and a difference between past and present judgments is recognized as part of growth. SERA's goal is not a finished self but the ability to keep understanding and shaping one's life anew.")),
        ]),
    ]},
    {"label": ("제4장", "Chapter 4"), "title": ("SERA의 실행 구조", "How SERA Works in Practice"), "articles": [
        (21, ("기본 순환 과정", "The Basic Cycle"), [
            ("p", ("SERA의 네 요소는 순서대로 한 번씩 거치는 단계가 아니라, 실제 삶에서 서로 영향을 주고받으며 반복된다. 프로그램 설계 시에는 다음 순환 구조를 활용할 수 있다.",
                   "SERA's four elements are not stages passed through once in order. They influence one another and repeat in real life. When designing a program, the following cycle can be used.")),
            ("ol", [(f"{s[0][0]} — {s[1][0]} ({'네 요소 통합' if s[2] == 'SERA' else ('주된 요소: ' if i == 0 else '') + {'S':'Story','E':'Empathy','R':'Resilience','A':'Achievement'}[s[2]]})" + (" → 새로운 경험으로 이어진다." if i == 5 else ""),
                     f"{s[0][1]}: {s[1][1]} ({'all four elements together' if s[2] == 'SERA' else ('main element: ' if i == 0 else '') + {'S':'Story','E':'Empathy','R':'Resilience','A':'Achievement'}[s[2]]})" + (" This leads into a new experience." if i == 5 else ""))
                    for i, s in enumerate(CYCLE)]),
            ("p", ("괄호 안은 해당 단계에서 두드러지는 요소일 뿐, 모든 단계에서 네 요소가 함께 작동한다. 이 구조는 고정된 절차가 아니며, 활동 특성과 참여자 상황에 따라 단계를 통합하거나 반복할 수 있다.",
                   "The element in parentheses is only the one most prominent at that stage; all four work together at every stage. This structure is not a fixed procedure, and stages can be combined or repeated depending on the activity and the participant's situation.")),
        ]),
        (22, ("경험 도구의 다양성", "A Variety of Experiences"), [
            ("p", ("SERA는 특정 활동을 독점적 방법으로 규정하지 않는다. 예시는 다음과 같다.", "SERA does not prescribe any one activity as the only method. Examples include:")),
            ("ul", [
                ("미술 SERAship: 그림을 그리는 과정에서 자신의 선택과 감정을 관찰한다.", "Art SERAship: observe your choices and feelings while drawing."),
                ("스포츠 SERAship: 연습과 경기에서 반복되는 판단, 감정, 실수와 개선을 탐구한다.", "Sports SERAship: explore the recurring judgments, feelings, mistakes and improvements in practice and games."),
                ("학습 SERAship: 학습 중 나타나는 관심, 집중, 어려움과 대응 방식을 기록한다.", "Learning SERAship: record the interest, focus, difficulty and responses that come up while studying."),
                ("진로 SERAship: 경험과 질문을 통해 자신의 관심과 가능성을 탐색한다.", "Career SERAship: explore your interests and possibilities through experiences and questions."),
                ("일·조직 SERAship: 업무, 협업, 갈등, 성취를 돌아보며 자신의 역할을 이해한다.", "Work and organization SERAship: understand your role by reflecting on tasks, collaboration, conflict and achievement."),
            ]),
            ("p", ("각 프로그램은 활동 자체의 전문성을 유지하면서 SERA의 공통 원칙을 적용한다.", "Each program keeps the expertise of its own activity while applying SERA's common principles.")),
        ]),
        (23, ("사전 질문과 사후 질문", "Questions Before and After"), [
            ("p", ("각 활동은 가능한 한 활동 전후의 질문을 연결한다. 사전 질문은 현재의 생각과 기대를 인식하게 하고, 사후 질문은 실제 경험에서 무엇을 발견했고 무엇이 달라졌는지 살피게 한다. 미술 활동의 예는 다음과 같다.",
                   "Wherever possible, each activity links questions before and after it. Questions before make people aware of their current thoughts and expectations; questions after help them see what they discovered in the real experience and what changed. An example from an art activity:")),
            ("ul", [
                ("사전: 나는 무엇을 표현하고 싶은가?", "Before: What do I want to express?"),
                ("활동 중: 나는 어떤 선택을 했으며, 왜 그렇게 했는가?", "During: What choices did I make, and why?"),
                ("사후: 실제 결과는 내 예상과 어떻게 달랐는가?", "After: How did the result differ from what I expected?"),
                ("후속: 다음에는 무엇을 새롭게 시도하고 싶은가?", "Follow-up: What new thing do I want to try next time?"),
            ]),
            ("p", ("질문의 수와 난도는 연령과 활동에 맞게 조정한다. 질문에 잘 답하는 것이 프로그램의 최종 목표가 되어서는 안 된다.",
                   "The number and difficulty of questions are adjusted to age and activity. Answering questions well must never become the program's final goal.")),
        ]),
    ]},
    {"label": ("제5장", "Chapter 5"), "title": ("SERAship의 운영 원칙", "Operating Principles of SERAship"), "articles": [
        (24, ("SERAship의 정의", "What a SERAship Is"), [
            ("p", ("SERAship은 SERA 원칙을 특정 활동과 결합해, 참여자가 경험을 관찰·질문·기록하고 실천과 성찰을 반복하도록 설계한 프로그램이다. 핵심은 콘텐츠가 아니라 콘텐츠를 활용하는 방식에 있다. 정해진 과제 수행에 그치는 수업은 SERAship이 아니다. 경험이 관찰, 질문, 기록, 성찰을 거쳐 다음 실천으로 연결될 때 SERAship이 된다.",
                   "A SERAship is a program that combines SERA's principles with a specific activity so that participants observe, question and record their experiences and repeat practice and reflection. The key lies not in the content but in how the content is used. A class that stops at completing set tasks is not a SERAship. It becomes a SERAship when experience passes through observation, questioning, recording and reflection and leads into the next practice.")),
        ]),
        (25, ("운영기관의 역할", "Role of Operating Organizations"), [
            ("ol", [
                ("활동 목적과 참여자 특성에 맞는 경험을 설계한다.", "Design experiences suited to the activity's purpose and the participants."),
                ("참여자가 스스로 질문할 수 있는 환경을 제공한다.", "Provide an environment where participants can ask their own questions."),
                ("관찰과 기록을 돕는 도구를 제공한다.", "Provide tools that help with observation and recording."),
                ("정답을 제시하기보다 성찰과 실천을 지원한다.", "Support reflection and practice rather than presenting right answers."),
                ("참여자의 기록과 개인정보를 보호한다.", "Protect participants' records and personal information."),
                ("운영 결과를 검토하고 개선한다.", "Review and improve how the program runs."),
            ]),
            ("p", ("운영기관은 공통 원칙을 준수하면서 자신의 전문 분야와 교육 목적에 맞게 프로그램을 설계할 수 있다.",
                   "Operating organizations may design programs to fit their own field and educational purpose while observing the common principles.")),
        ]),
        (26, ("퍼실리테이터와 멘토의 역할", "Role of Facilitators and Mentors"), [
            ("p", ("퍼실리테이터와 멘토는 참여자의 성장을 대신 결정하지 않는다. 참여자가 경험을 깊이 관찰하고, 다양한 관점을 검토하며, 다음 행동을 스스로 선택하도록 지원한다. 멘토 교육은 다음 역량을 중점으로 한다.",
                   "Facilitators and mentors do not decide a participant's growth for them. They support participants in observing experiences deeply, considering different perspectives and choosing their next action themselves. Mentor training focuses on these skills:")),
            ("ul", [
                ("개방형 질문을 만드는 능력", "Forming open-ended questions"),
                ("판단을 유보하고 경청하는 능력", "Withholding judgment and listening"),
                ("경험과 해석을 구분하도록 돕는 능력", "Helping people tell experience apart from interpretation"),
                ("선택을 존중하며 피드백하는 능력", "Giving feedback that respects people's choices"),
                ("개인정보와 심리적 안전을 보호하는 능력", "Protecting personal information and psychological safety"),
                ("자신의 역할 범위를 알고 전문기관에 연계하는 능력", "Knowing the limits of one's role and referring people to specialist services"),
            ]),
            ("p", ("멘토의 성과는 참여자를 특정 방향으로 얼마나 변화시켰는가가 아니라, 참여자가 스스로 관찰·판단·행동하도록 얼마나 잘 지원했는가로 살펴본다.",
                   "A mentor's success is measured not by how far they changed a participant in a particular direction, but by how well they supported the participant to observe, judge and act on their own.")),
        ]),
        (27, ("심리적 안전과 위기 대응", "Psychological Safety and Crisis Response"), [
            ("p", ("SERAship은 상담이나 치료가 아니다. 그러나 성찰과 기록 과정에서 참여자의 심리적 위기, 학대, 자해 위험 등이 드러날 수 있다. 운영기관은 다음을 갖춘다.",
                   "A SERAship is not counseling or therapy. Even so, a participant's psychological crisis, abuse or risk of self-harm may come to light during reflection and recording. Operating organizations put the following in place.")),
            ("ul", [
                ("위기 신호를 인지했을 때의 대응 절차와 담당자를 사전에 정한다.", "Set in advance the response procedure and the person responsible when warning signs are noticed."),
                ("상담·의료·복지 등 전문기관 연계 체계를 마련한다.", "Establish referral links to counseling, medical, welfare and other specialist services."),
                ("퍼실리테이터는 역할 범위를 넘는 개입을 하지 않고 전문기관에 연계한다.", "Facilitators do not intervene beyond their role and refer to specialist services."),
                ("생명과 안전이 위협받는 경우 기록 비공개 원칙(제17조)보다 보호 조치를 우선하며, 그 범위와 절차를 참여자(미성년자는 보호자 포함)에게 사전에 고지한다.", "When life or safety is threatened, protective measures take priority over the confidentiality of records (Article 17), and the scope and procedure are explained to participants (and guardians, for minors) in advance."),
                ("아동·청소년 프로그램은 관련 법령상 신고 의무를 준수한다.", "Programs for children and youth comply with legal reporting duties."),
            ]),
        ]),
        (28, ("성과 평가의 원칙", "Evaluating Outcomes"), [
            ("p", ("SERAship은 참여자의 성격이나 인간적 가치를 점수화하지 않는다. 성과는 다음과 같은 관찰 가능한 자료로 확인할 수 있다.",
                   "A SERAship never scores a participant's character or human worth. Outcomes can be seen through observable evidence such as:")),
            ("ul", [
                ("자신의 경험을 구체적으로 설명하는 능력", "Ability to describe one's experiences concretely"),
                ("스스로 질문을 생성하는 양상과 변화", "How one forms one's own questions, and how that changes"),
                ("자신과 타인의 관점을 구분하고 검토하는 과정", "The process of distinguishing and examining one's own and others' perspectives"),
                ("어려움에 대한 대응 방식의 변화", "Changes in how one responds to difficulty"),
                ("스스로 정한 행동의 실행과 수정", "Carrying out and adjusting self-chosen actions"),
                ("기록의 지속성과 자기성찰의 변화", "Consistency of recording and changes in self-reflection"),
            ]),
            ("p", ("이 자료는 성장 과정을 이해하는 근거로만 쓴다. 단일 점수로 서열화하거나 서로 다른 사람의 삶을 직접 비교하는 데 사용하지 않는다.",
                   "This evidence is used only to understand the process of growth. It is never used to rank people with a single score or to compare different people's lives directly.")),
        ]),
    ]},
    {"label": ("제6장", "Chapter 6"), "title": ("SERA 기록과 SDX 재단의 역할", "SERA Records and the Role of SDX Foundation"), "articles": [
        (29, ("SERA 기록의 구조", "Structure of SERA Records"), [
            ("p", ("SERA 기록은 서로 연결되는 세 층위로 구성할 수 있다.", "SERA records can be organized in three connected layers.")),
            ("ol", [
                ("활동 기록: 특정 경험에서 무엇을 했고 어떤 결과가 있었는지 기록한다.", "Activity records: what was done in a particular experience and what the result was."),
                ("성찰 기록: 무엇을 느끼고 이해했으며, 어떤 질문과 생각의 변화가 있었는지 기록한다.", "Reflection records: what was felt and understood, and what questions and changes in thinking arose."),
                ("종단 기록: 여러 시점의 활동과 성찰을 시간 순으로 연결해 관심, 판단, 대응 방식, 실천의 변화를 살핀다.", "Longitudinal records: activities and reflections from many points in time, linked in order, to show change in interests, judgments, responses and practice."),
            ]),
            ("p", ("기록이 장기간 축적되었다는 사실만으로 성장이 입증되지는 않는다. 변화에 대한 해석은 기록의 내용과 맥락에 근거해야 한다.",
                   "The fact that records have built up over a long time does not by itself prove growth. Any interpretation of change must rest on the content and context of the records.")),
        ]),
        (30, ("SERA Note, SERA Book, SERA Portfolio", "SERA Note, SERA Book, SERA Portfolio"), [
            ("ul", [
                ("SERA Note: 개별 활동과 성찰을 지속적으로 기록하는 기본 단위(기록)", "SERA Note: the basic unit for continuously recording individual activities and reflections (recording)"),
                ("SERA Book: 일정 기간의 기록을 종합해 경험과 변화를 서사로 구성한 결과물(서사화)", "SERA Book: a work that brings together records over a period and shapes experience and change into a narrative (storytelling)"),
                ("SERA Portfolio: 기록, 결과물, 실천 사례를 축적해 경험과 역량을 보여주는 자료(활용)", "SERA Portfolio: an accumulation of records, works and examples of practice that shows experience and capability (application)"),
            ]),
            ("p", ("참여자는 필요에 따라 책이나 포트폴리오를 만들 수 있다. 모든 참여자에게 같은 형식의 결과물을 의무화하지 않는다.",
                   "Participants may create a book or portfolio as they need. The same format of output is not required of every participant.")),
        ]),
        (31, ("종단 기록의 신뢰성과 무결성", "Reliability and Integrity of Longitudinal Records"), [
            ("p", ("종단 기록이 외부에서 활용되려면 신뢰성이 필요하다. 이를 위해 기록 생성 시점, 수정 이력, 출처, 보관 절차를 명확히 한다. 해시값은 특정 기록이 이후 변경되지 않았음을 확인하는 데 도움을 준다. 그러나 해시값만으로 기록 내용의 사실성이나 성장이 입증되지는 않으므로, 생성 과정, 본인 확인, 수정 이력, 검증 절차를 함께 설계한다.",
                   "For longitudinal records to be used externally, they must be reliable. To that end, the time of creation, revision history, source and storage procedure are made clear. A hash value helps confirm that a record has not been altered since. But a hash alone does not prove the truth of a record's content or a person's growth, so the creation process, identity verification, revision history and verification procedures are designed together.")),
        ]),
        (32, ("디지털 기록과 AI 활용", "Digital Records and the Use of AI"), [
            ("p", ("기록을 디지털 플랫폼에 저장하거나 AI로 분석·요약할 때 다음을 지킨다.", "When records are stored on digital platforms or analyzed and summarized with AI, the following are observed.")),
            ("ul", [
                ("어떤 기록이 어떤 목적으로 처리되는지 참여자에게 사전에 알리고 동의를 받는다.", "Participants are told in advance which records will be processed and for what purpose, and their consent is obtained."),
                ("AI의 분석과 요약은 참여자의 자기해석을 돕는 참고 자료이며, 참여자를 진단하거나 판정하지 않는다.", "AI analysis and summaries are reference material to help participants interpret themselves; they do not diagnose or judge participants."),
                ("AI 분석 결과를 서열화, 선발, 평가의 단독 근거로 쓰지 않는다.", "AI analysis is never the sole basis for ranking, selection or evaluation."),
                ("참여자의 기록을 동의 없이 AI 모델 학습이나 제3자 제공에 사용하지 않는다.", "Participants' records are not used to train AI models or shared with third parties without consent."),
                ("참여자는 AI 분석 결과를 열람하고 이의를 제기하거나 삭제를 요청할 수 있다.", "Participants can view AI analysis results, dispute them or request their deletion."),
            ]),
        ]),
        (33, ("SDX 재단의 역할과 책임 범위", "Role and Responsibilities of SDX Foundation"), [
            ("p", ("SDX 재단은 SERA 원칙의 연구·확산과 개별 운영기관의 프로그램 운영을 구분한다. 재단의 종단 기록 인증 역할은 다음과 같다.",
                   "SDX Foundation keeps research on and dissemination of SERA's principles separate from the program operations of individual operating organizations. The Foundation's role in certifying longitudinal records is as follows.")),
            ("ol", [
                ("인증 대상 기록의 범위와 제출 요건을 정한다.", "Define the scope of records eligible for certification and the submission requirements."),
                ("기록 생성과 관리에 필요한 무결성 요건을 제시한다.", "Set out the integrity requirements for creating and managing records."),
                ("제출된 기록의 출처, 연결성, 변경 이력을 정해진 기준에 따라 검토한다.", "Review the source, continuity and change history of submitted records against set criteria."),
                ("기준을 충족한 종단 기록에 인증 결과를 제공한다.", "Issue a certification result for longitudinal records that meet the criteria."),
                ("인증의 범위와 한계를 명확히 표시한다.", "Clearly state the scope and limits of certification."),
            ]),
            ("p", ("재단의 인증은 기록의 신뢰성과 관리 절차를 확인하는 것이며, 기록에 담긴 진술의 진실성이나 개인의 성장 수준을 보증하지 않는다.",
                   "The Foundation's certification confirms the reliability and management of records. It does not vouch for the truth of the statements in them or for a person's level of growth.")),
        ]),
        (34, ("인증의 독립성과 비서열화", "Independent, Non-Ranking Certification"), [
            ("p", ("재단은 SERA 연구, 프로그램 개발, 퍼실리테이터 육성을 별도 사업으로 추진할 수 있다. 이때 인증의 공정성을 지키기 위해 다음을 따른다.",
                   "The Foundation may carry out SERA research, program development and facilitator training as separate activities. To keep certification fair, it follows these rules.")),
            ("ul", [
                ("인증 기준의 제정과 심사는 사업 부문과 분리된 독립 인증위원회가 맡는다.", "An independent certification committee, separate from the program side, sets certification criteria and conducts reviews."),
                ("재단이 직접 개발하거나 운영에 관여한 프로그램의 기록을 심사할 때는 이해관계가 없는 위원이 맡는다.", "Records from programs the Foundation developed or helped run are reviewed by members with no conflict of interest."),
                ("인증은 충족 여부만 표시하며, 등급이나 점수로 참여자를 서열화하지 않는다.", "Certification shows only whether criteria are met; it never ranks participants with grades or scores."),
                ("인증 결과가 선발이나 채용에서 서열화 도구로 쓰이지 않도록 활용 기관에 그 한계를 고지한다.", "Organizations that use certification results are told their limits, so they are not used to rank people in admissions or hiring."),
            ]),
        ]),
        (35, ("기록의 장기 활용과 개인의 권리", "Long-Term Use of Records and Individual Rights"), [
            ("p", ("SERA 기록은 개인이 자신의 경험과 역량을 설명하는 자료가 될 수 있다. 그러나 기록이 축적되었다는 이유만으로 경제적 가치나 사회적 인정이 자동으로 생기지는 않는다. 교육기관의 평가, 취업, 진로, 협업 등에 활용하려면 목적별 기준과 방식이 따로 필요하다.",
                   "SERA records can help individuals describe their experience and capabilities. But economic value or social recognition does not arise automatically just because records have accumulated. Using them for school evaluation, employment, career paths or collaboration requires separate criteria and methods for each purpose.")),
            ("p", ("기록의 소유·관리 권한, 열람·공유 범위, 활용 동의, 정정·삭제 절차를 명확히 하여 개인이 자신의 기록을 통제할 수 있도록 한다.",
                   "Ownership and management rights, viewing and sharing scope, consent to use, and correction and deletion procedures are made clear so that individuals stay in control of their own records.")),
        ]),
    ]},
    {"label": ("제7장", "Chapter 7"), "title": ("SERA의 확장과 개정", "Growth and Amendment of SERA"), "articles": [
        (36, ("공통 원칙과 개별 프로그램의 자율성", "Common Principles and Program Autonomy"), [
            ("p", ("SERA가 여러 분야로 확산되려면 공통 원칙과 개별 프로그램의 자율성이 함께 보장되어야 한다. 모든 SERAship이 같은 콘텐츠, 질문, 활동, 결과물을 쓸 필요는 없다. 각 운영기관은 자신의 전문성을 살려 설계하되, 자기주도성, 질문 우선, 과정 중심, 개인차 존중, 기록과 성찰 등 핵심 원칙을 준수한다. 이를 통해 SERA는 하나의 교육 상품이 아니라 여러 분야의 공통 프레임워크로 발전한다.",
                   "For SERA to spread across many fields, both common principles and the autonomy of individual programs must be guaranteed. Not every SERAship needs the same content, questions, activities or outputs. Each operating organization designs from its own expertise while keeping the core principles: self-direction, questions first, process over outcome, respect for individual difference, and recording and reflection. In this way SERA grows not into a single education product but into a shared framework across many fields.")),
        ]),
        (37, ("프로그램의 지속적 개선", "Continuous Program Improvement"), [
            ("p", ("운영기관은 참여자의 경험과 피드백을 바탕으로 프로그램을 검토하고 개선한다. 재단은 다양한 운영 사례를 연구해 공통 원칙의 타당성과 적용 가능성을 검토한다. 개선의 기준은 외형적 규모나 단기 성과가 아니라, 참여자가 스스로 관찰·질문하고 실천과 성찰을 지속하도록 돕는지 여부다.",
                   "Operating organizations review and improve their programs based on participants' experiences and feedback. The Foundation studies a range of cases to examine whether the common principles are valid and applicable. The measure of improvement is not outward scale or short-term results but whether a program helps participants keep observing, questioning, practicing and reflecting on their own.")),
        ]),
        (38, ("원칙의 개정", "Amending the Principles"), [
            ("p", ("이 원칙은 고정된 교리가 아니라 실제 운영을 통해 다듬어지는 체계다. 개정은 다음 절차를 따른다.",
                   "These Principles are not fixed doctrine but a system refined through real practice. Amendments follow this procedure.")),
            ("ol", [
                ("재단, 운영기관, 퍼실리테이터, 참여자 누구나 개정을 제안할 수 있다.", "Anyone, whether the Foundation, an operating organization, a facilitator or a participant, may propose an amendment."),
                ("재단은 운영 사례와 연구 결과를 근거로 개정안을 마련하고 운영기관의 의견을 수렴한다.", "The Foundation prepares a draft amendment based on cases and research and gathers the views of operating organizations."),
                ("개정은 재단 이사회 의결로 확정하고, 개정 이유와 시행일을 공개한다.", "Amendments are finalized by resolution of the Foundation's board, and the reason and effective date are published."),
                ("정기 검토는 2년마다 실시한다.", "A regular review takes place every two years."),
            ]),
            ("p", ("개정은 제1장의 정의와 목적, 제9조 자기주도성, 제17조 자율성과 안전의 취지를 훼손하지 않는 범위에서 이루어진다.",
                   "Amendments may not undermine the definition and purposes in Chapter 1, self-direction in Article 9, or autonomy and safety in Article 17.")),
        ]),
    ]},
]

DECLARATION = [
    ("SERA는 사람이 자신을 외부의 기준으로만 평가하지 않고, 삶을 관찰하고 질문하며 스스로 의미를 만들어 가도록 돕는다.",
     "SERA helps people stop judging themselves by outside standards alone, and instead observe and question their lives and make meaning for themselves."),
    ("우리는 모든 사람에게 같은 목표나 같은 성장 속도를 요구하지 않는다.",
     "We do not ask everyone for the same goals or the same pace of growth."),
    ("우리는 일상의 경험을 배움의 출발점으로 삼는다. 자신의 감정과 타인의 관점을 이해하고, 어려움 속에서 새로운 대응을 찾으며, 자신의 달란트를 매일의 삶에서 실천하도록 지원한다.",
     "We take everyday experience as the starting point for learning. We support people in understanding their own feelings and others' perspectives, finding new responses in hard times, and practicing their talent in daily life."),
    ("우리는 성취의 결과만이 아니라 그에 이르는 과정과 변화를 소중히 여긴다.",
     "We value not only the results of achievement but the process and change that lead to them."),
    ("우리는 기록으로 경험과 변화를 잇되, 그 기록의 주인은 언제나 참여자 자신임을 존중한다.",
     "We connect experience and change through records, while respecting that the owner of those records is always the participant."),
    ("우리는 개인의 성장이 타인과 공동체, 자연과 미래세대를 함께 살리는 살림으로 자연스럽게 피어나기를 희망한다.",
     "We hope that personal growth will naturally blossom into salim, giving life together to others, communities, nature and future generations."),
]
DECLARATION_CLOSE = (
    "SERA의 목적은 사람을 평가하거나 규격화하는 것이 아니다. 자신의 삶을 이해하고, 스스로 선택하며, 변화에 대응하고, 발견한 가치를 삶에서 구현하는 사람을 지원하는 것이다. 이것이 SERA의 기본 정신이며 모든 SERAship이 공유하는 원칙이다.",
    "SERA's purpose is not to evaluate people or make them uniform. It is to support people who understand their own lives, make their own choices, respond to change, and live out the values they discover. This is SERA's founding spirit and the principle every SERAship shares.",
)

GLOSSARY_INTRO = ("이 원칙에서 쓰는 SDX 재단 고유 용어를 다음과 같이 정의한다. 본문 해석은 이 정의를 따른다.",
                  "The following defines the terms specific to SDX Foundation used in these Principles. The main text is read according to these definitions.")
GLOSSARY = [
    (("살림", "Salim"), ("’살리다’의 명사형이자 행위의 의미를 담은 말. 특정 대상 하나가 아니라 생명·관계·삶터 등 얽힌 전체를 함께 살리는 일",
                         "The noun form of the Korean verb salida (to bring to life, to sustain), carrying the sense of an action. Not one particular object but the work of bringing the whole interwoven web of life, relationships and living places to life together."), ("제16조", "Art. 16")),
    (("머니로직 (Money Logic)", "Money Logic"), ("화폐적 성장과 경쟁을 우선 가치로 삼는 사고·운영 방식", "A way of thinking and operating that puts monetary growth and competition first."), ("제1조", "Art. 1")),
    (("살림로직 (Salim Logic)", "Salim Logic"), ("자신과 타인, 공동체와 자연이 함께 살아나는 것을 우선 가치로 삼는 사고·운영 방식", "A way of thinking and operating that puts first the flourishing together of oneself, others, communities and nature."), ("제1조, 제16조", "Arts. 1, 16")),
    (("ESGG", "ESGG"), ("Ethical Sustainable Global Good. 윤리적이고 지속가능한 방식으로 지구적 선을 추구하는 철학. 살림로직의 확장 기반", "Ethical Sustainable Global Good. A philosophy of pursuing global good in ethical and sustainable ways; the foundation on which Salim Logic extends."), ("제16조", "Art. 16")),
    (("SERA", "SERA"), ("Story, Empathy, Resilience, Achievement를 바탕으로 한 성장 프레임워크", "A growth framework built on Story, Empathy, Resilience and Achievement."), ("제1조", "Art. 1")),
    (("SERAship", "SERAship"), ("SERA 원칙을 특정 활동과 결합해 관찰·질문·기록·실천·성찰을 반복하도록 설계한 프로그램", "A program that combines SERA's principles with a specific activity so that observation, questioning, recording, practice and reflection repeat."), ("제24조", "Art. 24")),
    (("달란트", "Talent (dallant)"), ("자연스럽게 관심·기쁨·몰입을 느끼며 자신과 타인에게 기여할 가능성을 지닌 고유한 잠재력. 특정 종교적 의미와 무관하다", "A unique potential in which one naturally feels interest, joy and immersion, and which can contribute to oneself and others. It carries no particular religious meaning."), ("제8조", "Art. 8")),
    (("얕은 노동 (Shallow Job)", "Shallow Job"), ("생계유지가 주된 목적이며 자신의 고유한 가치와 연결이 약한 일", "Work whose main purpose is making a living and that is only weakly connected to one's own values."), ("제8조", "Art. 8")),
    (("깊은 노동 (Deep Job)", "Deep Job"), ("자신의 달란트와 고유한 가치를 실현하는 일", "Work that realizes one's talent and one's own values."), ("제8조", "Art. 8")),
    (("장르마스터 (Genre Master)", "Genre Master"), ("자신의 달란트를 깊이 실천해 자기 삶의 고유한 영역을 일군 사람", "A person who has practiced their talent deeply and cultivated a domain of life that is uniquely theirs."), ("제8조", "Art. 8")),
    (("살림가 (Salimist)", "Salimist"), ("자신의 달란트로 자신과 타인, 공동체와 자연을 함께 살리는 실천가", "A practitioner who uses their talent to bring life to themselves, others, communities and nature together."), ("제8조, 제16조", "Arts. 8, 16")),
    (("SERA Note / Book / Portfolio", "SERA Note / Book / Portfolio"), ("기록의 기본 단위 / 기록을 서사로 엮은 결과물 / 기록과 실천을 축적한 활용 자료", "The basic unit of recording / records woven into a narrative / an accumulated body of records and practice for use."), ("제30조", "Art. 30")),
    (("종단 기록", "Longitudinal record"), ("여러 시점의 활동·성찰 기록을 시간 순으로 연결한 자료", "Activity and reflection records from many points in time, linked in chronological order."), ("제29조", "Art. 29")),
]
