# Korean Sentence Complexity Reduction for Machine Translation
# 기계번역을 위한 한국어 문장 복잡성 감소




## Abstract

Text simplification used as a preprocessing task for the improved functionality of natural language processing systems has a long history of research based on European languages, yet, there is no research that has utilized Korean as the object of study. However, there is great demand for comprehensible Korean to English machine translations, yet due to the disparate nature of these two languages, machine translation often fails to achieve fluent results.
자연어 처리 시스템의 기능 향상을 위한 사전 처리 과제로 사용되는 텍스트 단순화는 유럽어를 기반으로 한 오랜 연구 역사를 가지고 있지만, 한국어를 연구 대상으로 삼은 연구는 아직 없다.
그러나 영어 기계번역에는 이해하기 쉬운 한국어와 영어 기계번역의 수요가 많지만, 이 두 언어의 이질적인 특성 때문에 기계번역이 유창한 결과를 얻지 못하는 경우가 많다.

In order to improve the translation quality of Korean text as the source language, the first-ever rule-based Korean complexity reduction system was designed, constructed, and implemented in this study. This system was achieved by a unique technique termed "phrase-grouping and generalization of nuance structures," in Korean as a disambiguation tool. This technique has potential applications in all languages and additional natural language processing tasks. On top of this, in order to set a foundation for which complexity reduction operations and combinations generate fluent Korean and improved machine translation output, a unique factorial approach to simplification generation was also implemented.
원어로서의 국어 번역의 질을 높이기 위하여,
본 연구에서는 사상 최초의 규칙 기반의 국어 복잡성 감소 시스템을 설계, 구축, 시행하였다.
이 시스템은 한글로 "구조의 집합화 및 일반화"라는 독특한 기법을 통해 달성되었다.
이 기술은 모든 언어 및 추가 자연어 처리 작업에 잠재적으로 적용할 수 있습니다.
여기에 복잡도 감소 연산과 조합이 유창한 한글화와 기계 번역 출력 개선을 위한 기반을 마련하기 위해 단순화를 위한 고유한 요인 접근법도 구현했다.

In order to assess the output of the system proposed in the current research, the parallel evaluation of simplified Korean text by Korean native speakers and the evaluation of translations by English native speakers was conducted. The translation systems used in this study were Google Translate and Moses, both statistical machine translation systems, and Naver Translate, a neural machine translation system. This is the first research to conduct experiments on the interaction of text simplification and neural networks. Additionally, no known research has analyzed output from three machine translation systems simultaneously.
본 연구에서 제시된 시스템의 산출물을 평가하기 위하여,
한국어 원어민에 의한 한국어 간체본의 병행평가와 영어 원어민에 의한 번역평가를 실시하였다.
이 연구에 사용된 번역 시스템은 통계 기계 번역 시스템인 Google Translate와 Moses와 신경 기계 번역 시스템인 Naver Translate이다.
이것은 텍스트 단순화와 신경망의 상호작용에 대한 실험을 수행한 첫 번째 연구이다.
또한, 세 기계 번역 시스템의 출력을 동시에 분석한 알려진 연구는 없습니다.

Generally, the proposed system generated relatively fluent Korean, though due to the factorial nature by which simplifications were generated, sentence quality usually began to deteriorate after more than one simplification operation. On the other hand, the proposed system as a preprocessing task for machine translation consistently improved translation quality for all three systems utilized in this study by up to two performed simplifications.
일반적으로 제안된 시스템은 비교적 유창한 한국어를 생성했지만, 단순화가 생성된 요인 특성 때문에 문장 품질은 보통 두 번 이상의 단순화 작업 후에 악화되기 시작했다.
한편, 기계번역을 위한 전처리 과제로 제안된 시스템은 본 연구에 사용된 3개 시스템 모두에 대한 번역 품질을 최대 2개까지 단순화하여 일관되게 향상시켰다.

In the case of the statistical machine translation systems used in this study, more than two simplifications deteriorated not only Korean sentence quality, but also translation quality. However, in the case of Naver Translate, the neural machine translation system used in this study, even three simplifications resulted in translation improvement according to the evaluators. This study, then, emphasizes the need for more research conducted on text simplification as the field of natural language processing transitions to neural network-based approaches and applications.
본 연구에서 사용된 통계 기계 번역 시스템의 경우, 두 가지 이상의 단순화가 한국어 문장 품질뿐만 아니라 번역 품질도 악화되었다.
하지만, 이 연구에 사용된 신경 기계 번역 시스템인 네이버 번역기의 경우, 평가자들에 따르면, 심지어 세 번의 단순화가 번역 개선을 낳았다.
그런 다음 이 연구는 자연어 처리 분야가 신경망 기반 접근법과 애플리케이션으로 전환됨에 따라 텍스트 단순화에 대해 더 많은 연구가 필요하다는 점을 강조한다.




## 1. Introduction

Text simplification (TS) is a discipline that deals with the conversion of complicated text into a simpler alternative which bears the same meaning as the original text. Traditionally, TS is and was performed by humans, typically educators, who rewrite complicated text using simpler forms for the benefit of the learning impaired, those with literacy issues, or foreign language learners. However, in addition to being performed by humans, TS also has a long history of automation as a Natural Language Processing (NLP) task.
텍스트 단순화(TS)는 복잡한 텍스트를 원래 텍스트와 동일한 의미를 갖는 단순한 대안으로 변환하는 것을 다루는 분야이다.
전통적으로 TS는 학습 장애자, 읽고 쓰는 능력 문제가 있는 사람 또는 외국어 학습자의 이익을 위해 더 간단한 양식을 사용하여 복잡한 텍스트를 다시 쓰는 교육자, 인간(일반 교육자)에 의해 수행되고 수행되었다.
그러나 TS는 사람에 의해 수행되는 것 외에도 자연어 처리(NLP) 작업으로서 자동화 역사가 오래되었다.

Within TS there are two main types of simplification: semantic or lexical simplification and syntactic simplification. Semantic simplification focuses on the conversion from difficult, infrequent words or phrases to a simpler alternative. For example, consider (1) below:
(1) a. President Barack Obama was given the gift of life in Kenya.
    b. President Barack Obama was born in Kenya.
TS 내에는 의미론적 또는 어휘적 단순화와 구문적 단순화의 두 가지 주요 유형의 단순화가 있다.
의미적 단순화는 어렵고 자주 사용하지 않는 단어나 구문을 단순한 대안으로 전환하는 데 초점을 맞춘다.
예를 들어, (1) a를 고려해보자.
(1) a. 버락 오바마 대통령은 케냐에서 삶의 선물을 받았다.
    b. 버락 오바마 대통령은 케냐에서 태어났다.

(1a) and (1b) ultimately convey the same meaning, however, (1b)'s born is a far more frequent, simple, and easily understood alternative to (1a)'s given the gift of life, and is therefore much easier to process for someone who struggles with esoteric vocabulary or phrasing. Syntactic simplification, on the other hand, focuses on the conversion of complex syntactic structures into simpler alternative(s).
(1a)와 (1b)는 궁극적으로 동일한 의미를 전달하지만,
(1b)의 출생은 (1a)가 주어진 삶의 재능에 비해 훨씬 빈번하고 단순하며 쉽게 이해되는 대안이며, 따라서 난해한 어휘나 표현과 씨름하는 사람에게는 훨씬 더 쉽다.
반면에 구문 단순화는 복잡한 구문 구조를 단순한 대안으로 전환하는 데 초점을 맞춘다.

Please consider (2) below:
(2) a. President Obama is from Kenya and Donald Trump is from Mars.
    b. President Obama is from Kenya. Donald Trump is from Mars.
(2) a. 오바마 대통령은 케냐 출신이고 도널드 트럼프는 화성 출신이다.
    b. 오바마 대통령은 케냐 출신이다. 도널드 트럼프는 화성 출신이다.

(2a) is an example of two clauses being coordinated within the same sentence, resulting in a single complicated syntactic structure, while (2b) conveys the same meaning using two simpler structures.
(2a)는 두 절이 동일한 문장 내에서 조정되어 하나의 복잡한 구문 구조를 초래하는 예인 반면, (2b)는 두 개의 단순한 구조를 사용하여 동일한 의미를 전달한다.

TS, whether as a human or an automated NLP task, also has many applications within the NLP field itself. It is perhaps intuitive that TS could be helpful for humans, but it is not immediately intuitive that it would assist in an NLP environment. However, when one considers the sheer number of rules required to appropriately process normal language in a rule-based approach or that statistical machine learning is based primarily on frequency of occurrence, and it is a fact of language that shorter structures are simply more common than longer structures, it becomes a reasonable assumption the TS could help improve the functionality of NLP systems.
TS는 사람이든 자동화 NLP 작업이든 상관없이 NLP 분야 자체 내에 많은 애플리케이션을 가지고 있다.
TS가 사람에게 도움이 될 수 있다는 것은 직관적일 수 있지만, NLP 환경에서 도움이 된다는 것은 즉시 직관적이지는 않다.
그러나 규칙 기반 접근법에서 정상 언어를 적절하게 처리하는 데 필요한 규칙의 수 또는 통계 기계 학습이 주로 발생 빈도에 기초하고 있으며, 짧은 구조가 긴 구조보다 더 일반적이라는 것은 언어의 사실이다.
그는 TS가 NLP 시스템의 기능을 향상시키는데 도움을 줄 수 있었다.

One such NLP task is machine translation (MT). MT, put simply, is the automated translation of one language to another, and MT has a long history of benefitting from TS. Indeed, as A. Siddharthan notes in his survey summarizing the field of TS, the combination of TS and MT is perhaps the most prolific application of automated TS (2014). Traditional MT is and was performed primarily via a rulebased (RMT) approach, before transitioning to the most prolific approach in modern MT: statistical machine translation (SMT). The benefits of TS on both versions of MT have been demonstrated throughout the years and will be discussed in detail later in Chapter 2, but it is noteworthy that regardless of the MT approach, TS can benefit both types of systems.
그러한 NLP 작업 중 하나는 기계 번역(MT)이다.
간단히 말해서 MT는 한 언어를 다른 언어로 자동 번역하는 것이며 MT는 TS의 혜택을 받은 오랜 역사를 가지고 있다. 네, A로요.
Siddharthan은 TS 분야를 요약한 설문조사에서 TS와 MT의 조합이 자동화 TS(2014)의 가장 많은 애플리케이션이라고 언급했습니다.
전통적인 MT는 현대의 MT: 통계 기계 변환(SMT)에서 가장 많이 사용되는 접근방식으로 전환하기 전에 주로 규칙 기반(RMT) 접근방식을 통해 수행되었다.
두 버전의 MT에서 TS의 이점은 수년에 걸쳐 입증되었으며 2장의 후반부에서 자세히 논의될 예정이지만, MT 접근방식과 관계없이 TS가 두 유형의 시스템에 모두 이익이 될 수 있다는 점이 주목할 만하다.

Cutting-edge MT systems, however, are based in the use of the deep learning technique known was neural networks. While the marriage of TS and neural network motivated MT (NMT) is still an extremely new undertaking with little-tono known literature covering the topic, it is a goal of this study to address TS's future in MT as the field transitions to NMT.
그러나 최첨단 MT 시스템은 신경 네트워크라고 알려진 딥 러닝 기술의 사용에 기반을 두고 있다.
TS와 신경 네트워크 동기 MT(NMT)의 결합은 이 주제를 다루는 거의 알려지지 않은 문헌과 함께 여전히 매우 새로운 과제이지만, 이 연구의 목표는 필드가 NMT로 전환됨에 따라 MT에서 TS의 미래를 다루는 것이다.

Regardless of the MT approach, be it out-dated RMT or cutting-edge NMT, highly divergent language pairs pose problems that any MT system must overcome. Language pairs that share a common origin, structure, or evolution, for example, English and German, are capable of being translated relatively well by most MT systems. However, as Koehn points out in his book, even the most advanced statistical applications in SMT fall lamentably short of the goal when the language pairs are divergent in nature, for example, English and Korean (2009). Despite the underwhelming performance by most MT systems on disparate language pairs, it is in fact on these types of language pairs where there is the most demand for reliable MT systems.
MT 접근법에 관계없이, 구식 RMT 또는 최첨단 NMT에 관계없이, 고도로 다른 언어 쌍은 MT 시스템이 극복해야 하는 문제를 제기한다.
예를 들어 영어와 독일어와 같은 공통의 기원, 구조 또는 진화를 공유하는 언어 쌍은 대부분의 MT 시스템에 의해 비교적 잘 번역될 수 있다.
그러나 Koehn이 그의 책에서 지적했듯이, 시만텍에서 가장 발전된 통계 애플리케이션도 영어와 한국어(2009)와 같이 언어 쌍이 본질적으로 서로 다른 경우 목표에 한심할 정도로 미치지 못한다.
서로 다른 언어 쌍에서 대부분의 MT 시스템의 성능이 저조함에도 불구하고, 신뢰할 수 있는 MT 시스템에 대한 수요가 가장 많은 이러한 유형의 언어 쌍에 해당됩니다.

Given that Korean to English MT is an intimidating undertaking for even the most modern and robust MT system, it stands to reason that a TS system could provide a valuable means by which to improve output. One shortcoming of TS, though, is its relative lack of exposure in Asian NLP. Indeed, at the time of writing, there has been very little known research conducted on the automation of TS on an Asian language, that is, one article on Japanese and one on Korean, however, both were created for the assistance of humans. The inclusion of Korean-based automated TS would then be a valuable contribution to nearly any NLP undertaking involving the language, and the techniques used in such a system could be extended to other related languages, such as Japanese or Mongolian.
한국식부터 영국식까지 MT가 가장 현대적이고 강력한 MT 시스템에도 위협적인 사업임을 감안할 때, TS 시스템이 생산량을 향상시킬 수 있는 귀중한 수단을 제공할 수 있다는 것은 당연하다.
그러나 TS의 한 가지 단점은 아시아 NLP에서의 노출이 상대적으로 부족하다는 것이다.
사실, 집필 당시, 아시아 언어에 대한 TS의 자동화에 대한 알려진 연구는 거의 없었다.
즉, 일본어에 대한 한 편과 한국어에 대한 한 편, 둘 다 인간의 도움을 위해 만들어졌다.
한국어 기반 자동 TS의 포함은 언어와 관련된 거의 모든 NLP 사업에 귀중한 공헌이 될 것이며, 이러한 시스템에 사용되는 기술은 일본어 또는 몽골어와 같은 다른 관련 언어로 확장될 수 있다.




### 1-1. Korean Text Simplification

As stated above, there is little known research on the simplification of Korean text as an automated NLP task. As such, there exists no foundation on which to base any research on Korean TS, nor a jumping-off point from which to expand. It would indeed be quite an undertaking to build a simplification system for an entire language from the ground up. That being the case, this research will instead focus its interests on the most basic version of syntactic simplification, which is the creation of independent sentences from clauses embedded, subordinated, or coordinated within a sentence. If we are able to demonstrate a reasonable and effective way of rephrasing these clauses into their own independent sentences, and demonstrate a method which can additionally improve MT output, it can then be left to future research for the expansion and adaption of a Korean TS system.
위에서 말한 것처럼, 자동화된 NLP 과제로서 한글 텍스트의 단순화에 대한 연구는 거의 알려져 있지 않다.
따라서, 한국 TS를 기반으로 연구를 할 토대도, 확장할 출발점도 없다.
처음부터 전체 언어에 대한 단순화 시스템을 구축하는 것은 정말 대단한 일이 될 것이다.
따라서, 이 연구는 대신 구문 단순화의 가장 기본적인 버전에 관심을 집중시킬 것이다.
구문 단순화는 문장 내에 삽입, 종속 또는 조정된 절로부터 독립적 문장을 만드는 것이다.
만약 우리가 이러한 조항들을 독자적인 문장으로 바꾸는 합리적이고 효과적인 방법을 입증하고 MT 출력을 추가적으로 개선할 수 있는 방법을 증명할 수 있다면, 그것은 한국 TS 시스템의 확장과 적응을 위한 향후 연구에 맡겨질 수 있다.




#### 1-1-1. Korean Sentence Complexity Reduction

Sentence complexity, as defined by R Chandrasekar et al. and later redefined by A. Siddharthan, is based on the number of clauses a sentence bears (1996, 2002). The reason for this definition comes from the fact that all elements in a sentence are typically related in some way to the verb. For example, verbs can introduce arguments, bear case, gender, and number features, and supply their own content as well. As number of clauses in a sentence increases, it then becomes exceedingly more difficult of for an NLP system to process the information related to and introduced by these verbs. In terms of a rule-based approach, the longer and more complicated the sentence, the more rules needed to process the sentence. From a statistically motivated approach, as sentence length increases, so too does the number of calculations performed. MT, in particular, is done on a sentence by sentence basis, and as such, sentences with lower complexity are handled much more effectively by MT systems.
R Chandrasekar 등에 의해 정의되고 나중에 A에 의해 재정의된 문장 복잡성. 싯다르탄은 한 문장이 포함하는 절의 수에 기초한다(1996, 2002).
이 정의의 이유는 문장의 모든 요소들이 일반적으로 동사와 어떤 식으로든 관련되어 있다는 사실에서 비롯된다.
예를 들어, 동사는 인수, 대소문자, 성별, 숫자 특징을 소개하고 자체적인 내용도 제공할 수 있습니다.
문장의 절의 수가 증가함에 따라, NLP 시스템이 이러한 동사들에 의해 관련되고 도입되는 정보를 처리하는 것은 훨씬 더 어려워진다.
규칙 기반 접근법의 관점에서, 문장이 길고 복잡할수록, 문장을 처리하는 데 더 많은 규칙이 필요하다.
통계적으로 동기가 부여된 접근법에서 문장 길이가 증가함에 따라 수행된 계산의 수도 증가한다.
특히 MT는 문장별로 이루어지며, 복잡성이 낮은 문장은 MT 시스템에 의해 훨씬 더 효과적으로 처리된다.

The most basic task then for any syntactic simplification system is the reduction of individual sentence complexity in a way that also maintains the original intended meaning of the sentence. As the vast majority of the TS literature is based in the simplification of European languages, we then must explore a wholly unique means by which to reduce Korean sentence complexity. On top of that, our system must not only output simplified Korean text which bears the same meaning as the original text, but must also contribute in a meaningful way to the improvement of MT system output. The specifics of such a system will be discussed in detail in Chapter 4.
구문 단순화 시스템의 가장 기본적인 과제는 문장의 원래 의도한 의미를 유지하는 방식으로 개별 문장의 복잡성을 줄이는 것이다.
TS 문학의 대부분이 유럽어의 단순화에 바탕을 두고 있기 때문에, 우리는 한국어 문장의 복잡성을 줄이기 위한 완전히 독특한 방법을 탐구해야 한다.
여기에 우리 시스템은 원문과 같은 의미를 지닌 단순화된 한글을 출력할 뿐만 아니라 MT 시스템 출력 개선에 의미 있는 기여를 해야 한다.
그러한 시스템의 구체적인 내용은 4장에서 자세히 논의될 것이다.




### 1-2. Research Objectives

The first goal of this research is to expand on the field of text simplification with the inclusion of a syntactically motivated Korean simplification system. This is accomplished via the following steps taken in the implementation of our system:
이 연구의 첫 번째 목표는 구문론적 동기를 가진 한국어 단순화 시스템을 포함하여 텍스트 단순화 분야를 확장하는 것이다.
이 작업은 시스템 구현 시 취한 다음 단계를 통해 수행됩니다.

(1) Complex Korean sentence splitting and simplification
(2) The creation of a factorial system for generating simplified sentences
(3) The grouping and generalization of nuance structures
(1) 복잡한 한글 문장 분할 및 단순화
(2) 단순화된 문장 생성을 위한 요인 시스템의 생성
(3) 뉘앙스 구조의 분류 및 일반화

It is our hope that the creation of such a system will set the foundation for future TS research involving the Korean language.
우리는 이러한 시스템의 설립이 한국어를 포함하는 향후 TS 연구의 토대가 되기를 희망한다.

The second goal is to demonstrate that Korean TS can have a positive influence on modern MT output. This goal will be accomplished by using two SMT systems, namely Moses and Google Translate, and one NMT system, Naver Translate. By demonstrating that Korean TS can assist in NLP tasks we hope to expose the field of TS to Asian NLP, which might then gain traction and lead to the simplification of other Asian languages. Additionally, we hope to demonstrate that, while neural networks are capable of great feats, TS can be a useful stepping stone between the current available results and desired results.
두 번째 목표는 한국 TS가 현대 MT 출력에 긍정적인 영향을 미칠 수 있다는 것을 보여주는 것이다.
이 목표는 시만텍 시스템인 Moses와 Google Translate와 NMT 시스템인 네이버 Translate를 사용하여 달성될 것이다.
한국어 TS가 NLP 작업을 지원할 수 있다는 것을 입증함으로써 TS 분야를 아시아 NLP에 노출시켜 견인력을 얻고 다른 아시아 언어의 단순화로 이어질 수 있기를 바란다.
또한 신경망이 큰 성과를 거둘 수 있지만 TS가 현재 사용 가능한 결과와 원하는 결과 사이에 유용한 디딤돌이 될 수 있음을 입증하고자 한다.

And finally we simply wish to note that while TS as a pre-processing task for NLP systems is very useful, TS also has place in the field of education. Korea has never been of greater interest to the world at large, and as interest in the country continues to grow, so too will the number of those wishing to learn the language. Unfortunately, Korean is not the most accessible language, and many find it difficult to learn, especially as sentences become longer and more complex. It is possible that TS, perhaps even automated TS, could be used a tool for helping learners of Korean transition from one stage in their language learning to another. Additionally native speakers of Korean who suffer from learning disabilities or struggle with literacy issues may also benefit from Korean text simplification.
마지막으로, 우리는 단지 TS가 NLP 시스템의 전처리 작업으로서 매우 유용하지만, TS는 교육 분야에서도 자리를 잡고 있다는 것을 주목하고 싶다.
한국은 세계적으로 가장 큰 관심을 가졌던 적이 없었고, 한국에 대한 관심이 계속 증가함에 따라, 한국어를 배우기를 원하는 사람들의 수도 증가할 것이다.
불행하게도, 한국어는 가장 접근하기 쉬운 언어가 아니며, 많은 사람들은 특히 문장이 길어지고 복잡해지면서 배우는 것을 어려워한다.
어쩌면 자동화된 TS일지라도, TS는 한국어 학습자가 언어 학습에서 한 단계에서 다른 단계로 넘어가는 것을 돕는 도구가 될 수 있다.
또한 학습 장애를 겪고 있거나 읽고 쓰는 능력 문제로 어려움을 겪고 있는 한국어 원어민들도 한국어 텍스트 단순화의 혜택을 받을 수 있다.




### 1-3. Research Outline

The outline of this research is as follows:
Chapter 2 provides a literature review of text simplification, machine translation, and TS and a preprocessing step for MT.
Chapter 3 introduces and discusses the corpus used in this research.
Chapter 4 provides a detailed account of the simplification system we developed.
Chapter 5 discusses the pilot study conducted using Moses and Google Translate.
Chapter 6 contains the full-scale experiment using all three translation systems.
Chapter 7 lays out the limitations of the current research, research we leave for the future, and concludes the paper.
본 연구의 개요는 다음과 같습니다.
2장에서는 텍스트 단순화, 기계 번역 및 TS에 대한 문헌 검토와 MT의 사전 처리 단계를 제공한다.
3장은 이 연구에 사용된 말뭉치를 소개하고 논한다.
4장에서는 우리가 개발한 단순화 시스템에 대한 자세한 설명을 제공합니다.
5장에서는 Moses와 Google Translate를 사용하여 수행한 시범 연구에 대해 설명합니다.
6장에는 세 가지 번역 시스템을 모두 사용한 실제 실험이 수록되어 있다.
7장에서는 현재 연구의 한계와 미래를 위해 남겨둔 연구를 제시하고 논문을 마무리한다.




## 2. Literature Review

In this chapter the relevant literature is reviewed concerning the history and development of text simplification, machine translation, and text simplification as a preprocessing step for machine translation. Additionally, in the machine translation section, the machine translation systems used in the current research will be introduced and briefly discussed.
이 장에서는 기계번역을 위한 사전 처리 단계로서 텍스트 단순화, 기계번역 및 텍스트 단순화의 역사와 개발에 관한 관련 문헌을 검토한다.
또한, 기계번역 부분에서는 현재 연구에 사용되는 기계번역 시스템을 소개하고 간략하게 논의할 것이다.




### 2-1. Text Simplification

Text simplification (TS) can perhaps be best understood as the conversion of complex or normal written text to alternative(s) that use simpler or more common phrasing than the original text. It is of course imperative that during the conversion of the text, the original meaning of the text is preserved. TS has perhaps existed as a concept since the beginning of written language, however, its origin as a practiced and researched discipline can be traced back to work of Clark H. and Clark E. (1968). In their study, the Clarks documented and measured the semantic distinctions between words made by native speakers as the structure and content of sentences increase in complexity. This initial psychology research sparked a whole field of study, giving insight into the perception and understanding of written language of varying difficulty for both those with and without learning impairments.
텍스트 단순화(TS)는 복잡한 또는 일반 필기 텍스트를 원본 텍스트보다 단순하거나 일반적인 표현을 사용하는 대체 텍스트로 변환하는 것으로 가장 잘 이해할 수 있다.
물론 텍스트를 변환하는 동안 텍스트의 원래 의미를 보존해야 한다.
TS는 아마도 문어의 시작 이래로 개념으로서 존재해 왔지만, 연습되고 연구된 학문으로서의 그것의 기원은 Clark H.와 Clark E. (1968)의 연구로 거슬러 올라갈 수 있다.
그들의 연구에서 Clarks 부부는 문장의 구조와 내용이 복잡해짐에 따라 원어민에 의해 만들어진 단어들 사이의 의미적 차이를 문서화하고 측정했다.
이 초기 심리학 연구는 학습 장애가 있는 사람들과 없는 사람들 모두에게 다양한 난이도의 문어에 대한 인식과 이해에 대한 통찰력을 주면서, 전체 분야의 연구를 촉발시켰다.

It has been demonstrated throughout the decades in dozens of articles that the manual application of TS can have a profound benefit for those with literacy issues, such as dyslexia, allowing them to read and understand abstract concepts they would have otherwise been denied access to (Canning et al., 2000). Additionally, while the majority of the manual TS literature has used English as the object of study, the practice has spread to other European languages, such as Portuguese, and shown promising results for the learning impaired who speak other languages (Candido et al., 2009).
TS의 수동 적용이 난독증과 같은 읽고 쓰는 능력 문제를 가진 사람들에게 수십 년 동안 큰 이익을 줄 수 있다는 것이 수십 개의 기사에서 입증되어 그렇지 않았다면 접근이 거부되었을 추상적 개념을 읽고 이해할 수 있다(Canning et al., 2000).
또한 대부분의 수동 TS 문헌이 영어를 연구 대상으로 사용한 반면, 이 관행은 포르투갈어와 같은 다른 유럽 언어로 확산되었으며, 다른 언어를 사용하는 학습 장애인에게 유망한 결과를 보여주었다(Candido et al., 2009).

The automation of TS as a Natural Language Processing (NLP) task was first proposed by Chandrasekar et al., with the suggestion of specific rules to follow the next year (1996, 1997). Interestingly, Chandrasekar et al's initial proposal was not to create a TS system that would benefit the learning impaired, as had been the tradition in the field, but rather a simplifier that would make for speedier parsing of documents by NLP systems. Put simply, their proposal was to create a corpus with original and hand-simplified sentences aligned together, and then use a lightweight dependency analyzer to parse and learn rules from the aligned sentences. This early research did not make much progress as the author's goal was ultimately faster parsing, but the use of a parser to accomplish such a goal negated their efforts.
자연어 처리(NLP)로서의 TS 자동화 작업은 찬드라세카르 등이 다음 해(1996, 1997)에 따를 특정 규칙을 제안하면서 처음 제안했다.
흥미롭게도, Chandrasekar 등의 초기 제안은 현장의 전통처럼 학습 장애인에게 도움이 되는 TS 시스템을 만드는 것이 아니라 NLP 시스템에 의한 문서 구문 분석을 더 빠르게 하는 단순화를 만드는 것이었다.
간단히 말해서, 그들의 제안은 원래 문장과 손으로 단순화한 문장으로 함께 정렬된 말뭉치를 만든 다음 경량 의존성 분석기를 사용하여 정렬된 문장으로부터 규칙을 구문 분석하고 학습하는 것이었다.
이 초기 연구는 저자의 목표가 궁극적으로 더 빠른 구문 분석이었기 때문에 큰 진전을 이루지 못했지만, 그러한 목표를 달성하기 위해 파서를 사용하는 것은 그들의 노력을 무효화시켰다.

The next brick laid in the foundation of automated TS was done primarily in Dras' doctoral work. In his PhD dissertation, Mark Dras attempted to address wider groups of paraphrase options, employing synchronous TAG formalism and integer programming to create text conversions from constraints proposed on the system externally, such as length (1999). His contribution was motivated by English alone, but did indeed provide interesting solutions for pure syntactic rewrites.
자동화 TS의 토대 위에 놓인 다음 벽돌은 주로 Dras의 박사학위 연구에서 이루어졌다.
박사학위 논문에서 마크 드라스는 동기식 TAG 형식주의와 정수 프로그래밍을 사용하여 길이(1999년)와 같이 외부에 제안된 제약조건으로부터 텍스트 변환을 만들어내면서 더 넓은 그룹의 패러프레이즈 옵션을 다루려고 시도했다.
그의 기여는 영어에만 동기가 부여되었지만, 정말로 순수한 구문 재작성을 위한 흥미로운 해결책을 제공했다.

Please see below: 
\1. Light verb constructions:
(a) Steven made an attempt to stop playing Hearts.
(b) Steven attempted to stop playing Hearts.

\2. Clausal Complements
(a) His willingness to leave made Gillian upset.
(b) He was willing to leave. This made Gillian upset.

\3. Genitives
(a) The arrival of the train
(b) The train’s arrival

\4. Cleft constructions
(a) It was his best suit that John wore to the ball.
(b) John wore his best suit to the ball.

\1. 경동사 구성:
(a) 스티븐은 하트 게임을 중단하려고 시도했다.
(b) Steven은 Hearts 게임을 중단하려고 했다.

\2. (문법상)절 보어
(a) 기꺼이 떠나겠다는 그의 의지는 길시언을 화나게 했다.
(b) 그는 기꺼이 떠나려고 했다. 이것은 길시언을 화나게 했다.

\3. 유전자
(a) 열차의 도착
(b) 기차 도착

\4. 구순 구조
(a) 존이 무도회에 입고 나온 것은 그의 가장 좋은 정장이었다.
(b) 존은 무도회에 가장 좋은 정장을 입고 갔다.

While many TS researchers found Dras' approach too reliant on English grammar and too syntactically restrictive to be employed practically at the time, his use of constraint satisfaction through integer programming has enjoyed a bit of a renaissance in recent TS research (Angrosh et al., 2014). It is noteworthy, however, that Dras' approach supported both human and NLP-motivated, automated TS.
많은 TS 연구자들이 Dras의 접근 방식이 영어 문법에 너무 의존적이고 구문론적으로 너무 제한적이어서 그 당시 실질적으로 채용될 수 없다는 것을 발견했지만, 정수 프로그래밍을 통한 제약 만족의 사용은 최근 TS 연구에서 다소 부흥기를 누렸다(Angrosh et al., 2014).
그러나 Dras의 접근 방식이 인간과 NLP 동기 자동 TS를 모두 지원했다는 점은 주목할 만하다.

While the state of automated TS continued to advance for the next several years, it was A. Siddharthan that developed the basic architecture and text cohesion that set the standard and continues to enjoy prominence in modern TS (2002). The main goal behind Siddharthan's approach to TS was to create an implementable TS system that was not reliant on parsers, however, due to the flexibility and intuitive nature of Siddharthan's design, even with the use of a parser, this design was simple enough to implement. Not only that, but TS researchers have noted that when automated TS is brought into a language for the first time, most researchers base the foundation of their work on Siddharthan's structure (Specia et al., 2012). Though the majority of Siddharthan's early work was focused on syntactic simplification, lexical or semantic simplification was included in his architecture as well,
자동화 TS의 상태는 이후 몇 년 동안 계속 발전했지만, A였습니다.
Siddharthan은 표준을 설정하고 현대 TS(2002년)에서 계속 두각을 나타내고 있는 기본 아키텍처와 텍스트 응집력을 개발했습니다.
Siddharthan의 TS 접근 방식 이면의 주요 목표는 파서에 의존하지 않는 구현 가능한 TS 시스템을 만드는 것이었지만, Siddharthan 설계의 유연성과 직관성 때문에 파서를 사용하더라도 이 설계는 구현하기에 충분히 간단했다.
뿐만 아니라 TS 연구원들은 자동화 TS가 처음으로 언어로 도입되었을 때 대부분의 연구자들이 Siddharthan의 구조에 기초하고 있다는 점에 주목했다(Specia et al., 2012).
Siddharthan의 초기 연구의 대부분은 구문적 단순화에 초점을 맞췄지만, 어휘적 또는 의미적 단순화는 그의 아키텍처에도 포함되었다.

shown below in Figure 2.1:
아래 그림 2.1:

![Siddharthan's Text Simplification Architecture.png](img/Siddharthan's Text Simplification Architecture.png)

Figure 2.1: Siddharthan's Text Simplification Architecture
그림 2.1: Siddharthan의 텍스트 단순화 아키텍처

As can be seen in Figure 2.1, Siddharthan's approach was recursive in nature, performing all possible syntactic simplifications one at a time before transitioning to a lexical or semantic simplification stage. The reason for this being that a syntactic simplification may rule out a semantic simplification after being performed.
그림 2.1에서 볼 수 있듯이, 싯다르탄의 접근법은 어휘적 또는 의미적 단순화 단계로 전환하기 전에 한 번에 한 번씩 가능한 모든 구문적 단순화를 수행하는 본질적으로 재귀적이었다.
그 이유는 통사적 단순화가 수행된 후 의미적 단순화를 배제할 수 있기 때문이다.

In the analysis stage of the architecture, the theoretical TS system performs or utilizes word level information, such part of speech tags, grammar structure pattern matching, chunking, and parsing. Additionally, it is in this stage where the system determines which, if any, simplification to perform. Based on the analysis from the first stage, the transformation stage begins simplifying the sentence in question, whether that be splitting the sentence into multiple sentences or converting a passive sentence into an active. It is in the next and final syntactic simplification stage where the simplified sentence(s) are given a cohesive logic, whether through the generation of sentence connecters, referring expressions, the generation or preservation of anaphors, or a sentence reordering. The system then returns the simplified sentence(s) to the initial stage where the process starts over again, should a simplification still be possible. If no simplification is possible, the simplified sentence(s) are sent to the lexical simplification stage.
아키텍처의 분석 단계에서 이론적 TS 시스템은 음성 태그의 일부, 문법 구조 패턴 일치, 청킹 및 구문 분석 등의 워드 레벨 정보를 수행하거나 활용한다.
또한 시스템이 수행할 단순화(있는 경우)를 결정하는 단계입니다.
첫 번째 단계의 분석에 기초하여, 변환 단계는 문제의 문장을 여러 문장으로 나누거나 수동적인 문장을 능동적인 문장으로 변환하는 것이든 간에 단순화하는 것을 시작한다.
문장 연결자의 생성, 참조 표현, 아나포어의 생성 또는 보존, 문장 순서 변경 등 단순화된 문장에 응집 논리가 주어지는 것은 다음 및 마지막 구문 단순화 단계이다.
그런 다음 시스템은 단순화가 여전히 가능한 경우 프로세스가 다시 시작되는 초기 단계로 단순화된 문장을 되돌립니다.
단순화가 불가능한 경우 단순화된 문장은 어휘 단순화 단계로 전송된다.

The current research borrows heavily from the architecture suggested by Siddharthan for our purposed Korean syntactic TS system, however, due to the fact that Korean and English are disparate languages, our architecture is heavily altered and will be introduced in Chapter 4.
현재의 연구는 Siddharthan이 제안한 우리의 한국어 통사적 TS 시스템을 위해 제안한 아키텍처에서 크게 차용되었지만, 한국어와 영어는 서로 다른 언어이기 때문에 우리의 아키텍처가 크게 변형되어 4장에서 소개될 것이다.




### 2-2. Machine Translation

Machine translation (MT) is perhaps the oldest NLP task, and can best be understood as the automatic conversion of text in one language to text in another. However, despite its long history, it is quite often the case that the output from an MT system is less than desirable. This is true for language pairs that are similar in structure, for example English and Spanish, but even more so for disparate language pairs, such as English and Korean. What follows will be a brief description of the most prominent MT system types and their relevance to the current research.
기계 번역(MT)은 아마도 가장 오래된 NLP 작업이며, 한 언어의 텍스트를 다른 언어의 텍스트로 자동 변환하는 것으로 가장 잘 이해할 수 있다.
그러나 오랜 역사에도 불구하고 MT 시스템의 출력이 바람직하지 않은 경우가 많다.
이것은 영어와 스페인어와 같이 구조가 유사한 언어 쌍에 대해 사실이지만, 영어와 한국어와 같은 이질적인 언어 쌍에 대해서는 훨씬 더 그렇다.
다음은 가장 두드러진 MT 시스템 유형 및 현재 연구와의 관련성에 대한 간략한 설명입니다.




#### 2-2-1. Rule-Based Machine Translation

Rule-Based Machine Translation (RMT) is the oldest form of MT, and is perhaps the most intuitive form of MT. Essentially, what a RMT system does is use linguistic information from a source language to convert it into a target language, making use of linguistic information from the target language as well (Hutchins, 1992). Essentially, what this means is the literal automated swapping of words or phrases between languages through the creation of rules. The approach is based in attempting to do computationally what the human mind does when translating a language. The benefits of an RMT system are quite extensive, as it really is the only known MT system that could potentially achieve 100 percent perfect translations. Unfortunately, such a system has never been achieved as the expense, not only in terms of computation but in sheer man-hours, is not only impractical; it is beyond imagination. As such, pure RMT systems have all but been abandoned in modern MT. Their only relevance to the current research is in the use of Hybrid MT systems, which make use of concepts from multiple MT system approaches. This will be discussed in detail later in section 2.2.4 as the current research could be viewed as a hybrid MT system.
RMT(Rule-Based Machine Translation)는 MT의 가장 오래된 형태이며 MT의 가장 직관적인 형태일 수 있다.
본질적으로, RMT 시스템이 하는 것은 소스 언어의 언어 정보를 대상 언어로 변환하기 위해 사용하는 것이며, 대상 언어에서도 언어 정보를 사용하는 것이다(Hutchins, 1992).
본질적으로, 이것이 의미하는 것은 규칙 생성을 통해 언어 간 단어 또는 구문의 문자 그대로 자동 교환이다.
그 접근법은 언어를 번역할 때 인간의 마음이 하는 것을 계산적으로 하려고 시도하는 것에 기초한다.
RMT 시스템의 이점은 상당히 광범위합니다.
이는 100% 완벽한 번역을 달성할 수 있는 유일한 MT 시스템이기 때문입니다.
불행하게도, 계산의 측면뿐만 아니라 순수한 노동 시간의 측면에서도 비용이 비현실적일 뿐만 아니라 상상을 초월하기 때문에 그러한 시스템은 결코 달성되지 못했다.
따라서, 순수 RMT 시스템은 현대 MT에서 거의 폐기되었다.
현재 연구와의 유일한 관련성은 다중 MT 시스템 접근 방식의 개념을 사용하는 하이브리드 MT 시스템의 사용이다.
이는 현재 연구가 하이브리드 MT 시스템으로 간주될 수 있기 때문에 섹션 2.2.4의 후반에 자세히 논의될 것이다.




#### 2-2-2. Statistical Machine Translation

Statistical Machine Translation (SMT) is the most prolific form of modern MT. Essentially SMT assumes a statistical model for a given sentence in a source language. By thinking of translations as the combination of two models, a conditional translation model (p(S|T)) and a language model (p(T)), we are able assign and calculate probabilities, typically determined by N-grams (Koehn, 2009). The purpose of p(S|T) calculation is to maintain meaning between the source and target language, while p(T) is concerned with fluency of output in the target language (Na, 2015). Basically, these probabilities are calculated, a system is trained on a parallel bilingual corpus, and then a sentence in the source language is run through a decoder. Whatever translation in the target language yields the highest probability is the best translation, and this translation is what the SMT system in question outputs. In this way we can think about SMT as a Hidden Markov Model, where the possible translations are the hidden nodes and the best translation is the nodes whose combination yields the highest probability.
통계 기계 번역(SMT)은 현대 MT의 가장 다작적인 형태이다.
본질적으로 시만텍은 소스 언어의 특정 문장에 대한 통계 모델을 가정한다.
변환을 조건부 변환 모델(p(S|T)과 언어 모델(p(T))의 조합으로 생각함으로써, 일반적으로 N-그램으로 결정되는 확률을 할당하고 계산할 수 있다(Koehn, 2009).
p(S|T) 계산의 목적은 소스 언어와 대상 언어 사이의 의미를 유지하는 것이며, p(T)는 대상 언어의 출력 유창성과 관련이 있다(Na, 2015).
기본적으로, 이러한 확률은 계산되고, 시스템은 병렬 이중 언어 말뭉치에 대해 훈련되며, 소스 언어의 문장은 디코더를 통해 실행된다.
대상 언어의 번역이 가장 높은 확률을 제공하는 것이 어떤 것이든 최상의 번역이며, 이 번역은 해당 시만텍 시스템이 출력하는 것이다.
이러한 방식으로 우리는 시만텍을 은닉 마르코프 모델로 생각할 수 있다.
여기서 가능한 변환은 은닉 노드이고 최상의 변환은 조합이 가장 높은 확률을 산출하는 노드이다.

Figure 2.2 below provides an adequate visualization of this process, taken from Li et al. (2012):
아래 그림 2.2는 Li 등(2012)에서 가져온 이 프로세스의 적절한 시각화를 제공한다.

![SMT visualization taken from Li et al.png](img/SMT visualization taken from Li et al.png)

Figure 2.2: SMT visualization taken from Li et al.
그림 2.2: Li 등으로부터 얻은 시만텍 시각화.

SMT's prevalence in modern MT is in no short part due to the open-source toolkit for SMT, Moses (Koehn et al., 2007). Moses essentially functions as the decoder in Figure 2.2 above, providing a free, easily usable, trainable, and customizable environment where one might conduct SMT experiments. Though there are several other systems of comparable specifications with Moses, none has enjoyed the prominence Moses has, becoming the standard SMT system in the literature and typically acting as the baseline to determine improvement in SMT focused articles and studies.
시만텍이 현대 MT에 널리 보급된 것은 시만텍용 오픈 소스 툴킷 Moses(Koehn 등, 2007) 덕분이다.
Moses는 기본적으로 위의 그림 2.2의 디코더로 기능하여 시만텍 실험을 수행할 수 있는 자유롭고 쉽게 사용할 수 있으며 훈련 가능하며 사용자 지정이 가능한 환경을 제공한다.
Moses와 유사한 사양의 다른 시스템이 몇 개 있지만, Moses가 가진 명성을 누린 시스템은 하나도 없다.
문헌에서 표준 시만텍 시스템이 되고 일반적으로 시만텍 중심 기사와 연구의 개선을 결정하는 기준선으로 작용한다.

Moses may be the most prominent SMT system involved in academic studies, but no SMT system enjoys more prominence and accessibility than Google Translate (2016). At the time of writing, Google Translate is a fully-trained, fullyfunctioning, freely accessible SMT system capable of translating between 103 language pairs, though more are in development (Ahmed, 2016).
Moses는 학술 연구에 관련된 가장 뛰어난 시만텍 시스템일 수 있지만, Google Translate(2016)만큼 뛰어난 시만텍 시스템은 없다.
집필 당시 Google Translate는 103개 언어 쌍을 자유롭게 번역할 수 있는 완전히 훈련되고 완벽하게 기능하며 자유롭게 액세스할 수 있는 시만텍 시스템입니다(Ahmed, 2016).

Moses and Google Translate are based on the same SMT technology, however, Google Translate has no customizability options, nor can it be trained and changed in any way beyond what its developers deem appropriate. In others words, the preprocessing and post-processing techniques used to improve output in Google Translate cannot be altered in any way. What this mean is that Google Translate is inappropriate as an academic baseline as it is hard to determine what processing steps were performed on the output beyond SMT. Moses functions as a pure SMT system and allows for customizability and retraining for the purposes of research, allowing researchers to determine which pre-processing or post-processing techniques improve output relative to the pure SMT baseline. It should be noted, however, that Google Translate typically outperforms Moses. Both Moses and Google Translate are used in the current research and will be discussed in Chapter 5 and 6.
Moses와 Google Translate는 동일한 시만텍 기술에 기반을 두고 있지만, Google Translate는 사용자 정의 옵션이 없으며, 개발자들이 적절하다고 생각하는 것 이상으로 훈련 및 변경할 수 없습니다.
다시 말해, 구글 번역의 출력을 향상시키기 위해 사용되는 전처리 및 후처리 기술은 어떤 식으로도 변경될 수 없다.
이는 구글 번역이 시만텍 이외의 출력물에 대해 어떤 처리 단계를 수행했는지 결정하기 어렵기 때문에 학술적 기준으로 적절하지 않다는 것을 의미한다.
Moses는 순수한 시만텍 시스템으로서 기능하며 연구의 목적을 위해 맞춤화와 재교육을 허용하여 연구자들이 어떤 사전 처리 또는 사후 처리를 결정할 수 있도록 한다.
Occessing 기술은 순수 시만텍 기준선에 비해 출력을 개선한다.
그러나 구글 번역은 일반적으로 모세스를 능가한다는 점에 주목해야 한다.
Moses와 Google Translate는 현재 연구에 사용되고 있으며 5장과 6장에서 논의될 것이다.




#### 2-2-3. Neural Machine Translation

Neural Machine Translation (NMT) is still based in statistical machine learning techniques, however, it is quite a different approach to SMT. In SMT, a translation system typically consists of subcomponents that are seperately optimized, that is, the combination of the highest probability N-grams, while in NMT a large neural network is trained to maximize translation performance (Wolk et al., 2015). NMT models were inspired by representation learning and require only a fraction of the memory used by their SMT counterparts, but each and every component of a NMT system is trained jointly in order to maximize system output (Cho et al., 2014). The complexities of the an NMT system are considerable, and whole papers are written on their explanation, so they will not be discussed indetail here, as that is not in-line with the objectives of the current research. It is noteworthy, however, that NMTs make use of the most current and cutting-edge technology available in modern MT, and they appear to be leading the charge for the direction of future MT research.
신경 기계 번역(NMT)은 여전히 통계 기계 학습 기법에 기반을 두고 있지만, 시만텍에 대한 접근 방식은 상당히 다르다.
시만텍에서 변환 시스템은 일반적으로 개별적으로 최적화되는 하위 구성요소, 즉 가장 높은 확률 N그램의 조합으로 구성되며 NMT에서는 대규모 신경망이 m으로 훈련된다.
acimize 번역 성능(Wolk et al., 2015).
NMT 모델은 표현 학습에서 영감을 얻었으며 시만텍에서 사용하는 메모리의 일부만 요구하지만 NMT 시스템의 각 및 모든 구성 요소는 시스템 출력을 극대화하기 위해 공동으로 훈련된다(Cho et al., 2014).
NMT 시스템의 복잡성은 상당하며, 전체 논문은 설명서에 작성되어 있기 때문에 현재 연구의 목적과 부합하지 않기 때문에 여기서 자세히 논의되지 않을 것이다.
그러나 주목할 점은 NMT가 현대 MT에서 이용 가능한 최신 기술을 활용하고 있으며 향후 MT 연구의 방향을 주도하고 있는 것으로 보인다는 점이다.

Naver Translate is a freely available NMT system and a comparable counterpart to SMT's Google Translate (2016). Naver Translate traditionally functioned as a SMT system, however, it has recently transitioned to a NMT system, and at the time of writing, is the only known, freely-accessbile NMT system capable of translating Korean to English (Lee et al., 2015).
네이버 번역기는 무료로 이용할 수 있는 NMT 시스템이며 시만텍의 구글 번역기 (2016)와 비교해도 손색이 없다.
전통적으로 시만텍 시스템으로서 기능했던 네이버 번역기는 최근 NMT 시스템으로 전환되었으며, 집필 당시 한글을 영어로 번역할 수 있는 유일한 알려진 자유 액세스 가능 NMT 시스템이다. (Lee 등, 2015).

Naver's NMT system makes use of a bi-directional recurrent neural network, the details of which are shown in Figure 2.3:
네이버의 NMT 시스템은 양방향 반복 신경망을 사용하고 있으며, 자세한 내용은 그림 2.3:

![Naver Translate's bi-directional recurrent neural network.png](img/Naver Translate's bi-directional recurrent neural network.png)

Figure 2.3: Naver Translate's bi-directional recurrent neural network
그림 2.3: 네이버 번역의 양방향 반복 신경 네트워크

The details of the system are borrowed from Cho et al., where h~t~ is a hidden state of the encoder, x~t~ is a one-hot encoded vector indicating one of the words in the source vocabulary, W~s_we~ is a weight matrix for the word embedding of the source language, and f~GRU~ is a gated recurrent unit (GRU) (2014).
시스템의 세부 사항은 Cho 등으로부터 차용된 것이다.
여기서 h~t~는 인코더의 숨겨진 상태이고, x~t~는 소스 어휘의 단어 중 하나를 나타내는 원핫 인코딩 벡터이며,
W~s_we~는 소스 언어의 단어 임베딩에 대한 가중치 매트릭스이며, f~GRU~는 게이트 반복 단위(2014)이다.

Naver Translate is capable of translating between English, Korean, Chinese, and Japanese, and in that sense is quite limited, however, at the time of writing, Google Translate has not yet trasitioned to a full NMT system for any language pairs beyond Chinese and English (Coldeway, 2016). Though NMT systems generally produce output that is far more desireable than their SMT counterparts, there is still room left for improvement. Additionally, at the time of writing, there has yet to be any research which comments the role of TS for MT as the field transitions to neural networks, which is one of the goals of the present research and will be discussed more in Chapter 6.
네이버 번역기는 영어, 한국어, 중국어, 일본어를 번역할 수 있고, 그런 점에서 상당히 제한적이지만, 구글 번역기는 아직 중국어와 영어를 넘어서는 언어 쌍들을 위한 완전한 NMT 시스템으로 전환되지 않았다.
NMT 시스템은 일반적으로 시만텍 시스템보다 훨씬 더 원하는 출력을 생산하지만 여전히 개선의 여지가 남아 있습니다.
또한 집필 당시 신경망으로의 현장 전환에 있어 MT에 대한 TS의 역할에 대해 언급하는 연구는 아직 없으며, 이는 본 연구의 목표 중 하나이며 6장에서 더 자세히 논의될 것이다.




#### 2-2-4. Hybrid Machine Translation

Hybrid Machine Translation (HMT) is the combination of two or more MT approaches in one system in order to take advantage of the benefits from both approaches and improve MT system output (Kamran, 2013). This could include any of the MT approaches discussed above or ones not discussed in the present research. For example, the use of a pure SMT Moses system and then the application of a rule-based automatic post-editing system which fixes common errors in SMT output would be considered an HMT system (Rosa, 2013). Such a system would be an example of a statistical-rule-based machine translator. Other combinations are of course possible. The present research, which suggests a rule-based syntactic simplication system through Korean sentence complexity reduction could be viewed as pre-processing step for an MT system. That being the case, we could view such a system as a rule-based simplfier for a statistically or neural network motivated machine translation system.
하이브리드 기계 변환(HMT)은 두 가지 이상의 MT 접근 방식을 하나의 시스템에 조합하여 두 가지 이상의 MT 시스템 접근 방식을 활용하고 MT 시스템 출력을 개선하는 것이다(Kamran, 2013).
여기에는 위에서 논의한 MT 접근방식 또는 본 연구에서 논의되지 않은 접근방식이 포함될 수 있다.
예를 들어, 순수 시만텍 Moses 시스템을 사용한 다음 시만텍 출력의 일반적인 오류를 수정하는 규칙 기반 자동 사후 편집 시스템을 적용하는 것은 HMT 시스템으로 간주할 수 있다(Rosa, 2013).
이러한 시스템은 통계 규칙 기반 기계 번역기의 예가 될 수 있다.
물론 다른 조합도 가능합니다.
한글 문장 복잡도 축소를 통한 규칙 기반의 통사적 단순화 시스템을 제안하는 현재의 연구는 MT 시스템의 전처리 단계로 볼 수 있다.
그러한 경우, 우리는 그러한 시스템을 통계 또는 신경망에 의해 동기화된 기계 번역 시스템에 대한 규칙 기반 단순화로 볼 수 있다.




### 2-3. Text Simplification for Machine Translation

As mentioned above, TS used a preprocessing task for NLP tasks, MT in particular, has quite a long history. After Siddharthan introduced his TS architecture, MT motivated rule-based TS systems, not only for English, but for many other language began appearing quite prominently. The main idea being that TS would be helpful from a rule based perspective, as the number of rules and computational difficulty of a sentence would decrease when utilizing TS. If the apporach was statistical in nature, shorter sentences and less complex structures or phrases result in simpler calculations. As Siddharthan, the most prominent figure in the field of automated TS, reminds us, it is simply a fact of language that short, less complex phrasing is more common and therefore easier for a system to learn (2014). Additionally, the longer a sentence gets, the more constrained the environment becomes, making it less likely to see an uncommon or complicated structure or phrasing. In short, TS has become a method by which to compensate for data scarcity.
위에서 언급한 바와 같이, TS는 NLP 작업에 대해 전처리 작업을 사용했으며, 특히 MT는 꽤 오랜 역사를 가지고 있다.
Siddharthan이 TS 아키텍처를 도입한 후 MT 동기 부여 규칙 기반 TS 시스템이 영어뿐만 아니라 다른 많은 언어에도 상당히 두드러지게 나타나기 시작했습니다.
주요 아이디어는 TS를 활용할 때 문장의 규칙 수와 계산 난이도가 감소하기 때문에 규칙 기반 관점에서 TS가 유용할 것이라는 것이다.
부록이 본질적으로 통계적인 경우, 문장 길이가 짧고 덜 복잡한 구조나 구문은 더 간단한 계산으로 귀결된다.
자동화 TS 분야에서 가장 유명한 인물인 Siddharthan이 상기시켜 주듯이, 짧고 덜 복잡한 표현법이 더 일반적이며 따라서 시스템이 배우기 더 쉽다는 것은 언어의 사실이다(2014). 게다가, 문장이 길어질수록, 환경은 더 제한적이 되어, 흔하지 않거나 복잡한 구조나 문구를 볼 가능성이 더 적어진다.
간단히 말해서, TS는 데이터 부족을 보완하는 방법이 되었다.

One on the first pieces of research that explored non-English TS for MT can be found in Specia et al., where researchers developed a rule-based method for the automatic lexical simplification of difficult words in Brazilian Portuguese (2009). Building on her research in 2009, Specia attempted to create an automatic statisical simplifier by creating a parallel corpus of both original and simplified Portuguese sentences and then training them in Moses (2010). This was the first research that attempted to use SMT to translate between simplified and unsimplified text, however, she noted that since Moses learns at a sentence level, this might only work for lexical simplification and not syntactic simplification where a complex sentence is often split into multiple, simpler sentences.
MT를 위한 비영어 TS를 탐구한 첫 번째 연구 중 하나는 Specia 등에서 찾을 수 있으며, 연구진은 브라질 포르투갈어(2009)에서 어려운 단어의 자동 어휘 단순화를 위한 규칙 기반 방법을 개발했다.
2009년 연구를 바탕으로 Specia는 원본과 단순화된 포르투갈어 문장의 병렬 말뭉치를 만든 다음 Moses (2010)에서 그것들을 훈련시킴으로써 자동 정석적 단순화를 만들려고 시도했다.
이 연구는 시만텍을 사용하여 단순화된 텍스트와 그렇지 않은 텍스트를 번역하려고 시도한 첫 번째 연구였지만, 모세가 문장 수준에서 학습하기 때문에 복잡한 문장이 종종 여러 개의 단순한 문장으로 나뉘는 구문적 단순화가 아닌 어휘적 단순화에만 효과가 있을 수 있다는 점에 주목했다.

Collados, based on Siddharthan's architecture, developed a Spanish syntactic simplification system and used this system in combination with Google Translate to demonstrate a need for further simplification research done on the Spanish language (2013). His research showed that Spanish TS was able to improve translation quality when translating to disparate languages, such as Korean and Chinese. However, as his was the first TS research conducted on Spanish syntactic simplification, he only dealt with a limited number of structures, namely andcoordination, constrastive-coordination, relative clauses, and cause and effect sentences. Additionally, fearing illegible output, Collados limited his system to only simplifiying sentences that bear two clauses, leaving more complicated structures for future research.
Siddharthan의 아키텍처를 기반으로 하는 Colados는 스페인어 구문 단순화 시스템을 개발했고 이 시스템을 Google Translate와 함께 사용하여 스페인어에 대한 추가 단순화 연구의 필요성을 입증했습니다(2013).
그의 연구는 스페인어 TS가 한국어나 중국어 같은 서로 다른 언어로 번역할 때 번역 품질을 향상시킬 수 있었다는 것을 보여주었다.
그러나 스페인어 구문 단순화에 대한 최초의 TS 연구였기 때문에, 그는 제한된 수의 구조, 즉 조정, 대비-조정, 상대조항, 인과관계 문장만을 다루었다.
게다가, 읽기 힘든 결과물을 두려워한 콜라도스는 두 개의 조항을 포함하는 문장을 단순화하는 것으로 그의 시스템을 제한했고, 향후 연구를 위한 더 복잡한 구조를 남겼다.

Siddharthan, Collados, Specia, and nearly all TS researchers have noted that one of the greatest issues in automated TS is the lack of an automatic evaluation metric to determine how well a given system is functioning. As Wubben et al., points out, readability metrics, such as the Flesch-Kincaid grade-level metric, should be avoided in TS because such metrics consider only characteristics of the sentence, such as word length, and completely ignore grammaticality or the content's semantic adequacy (2012).
Siddharthan, Colados, Specia 및 거의 모든 TS 연구자들은 자동화된 TS의 가장 큰 문제 중 하나는 주어진 시스템이 얼마나 잘 작동하는지 결정하는 자동 평가 지표가 없다는 점에 주목했다.
Wubben 등이 지적한 바와 같이, Flesch-Kincaid 등급 수준 메트릭과 같은 가독성 메트릭은 단어 길이와 같은 문장의 특성만을 고려하고 문법성 또는 내용의 의미적 적절성(2012)을 완전히 무시하기 때문에 TS에서는 피해야 한다.

If the goal, then, is MT or some other NLP task, why not use the automatic evaluation metric which is standard to that NLP task? For example, in MT the standard evaluation metric is the BLEU (BiLingual Evaluation Understudy) score (Papineni et al., 2002). The BLEU score essentially compares the GOLD standard translation to the candidate translation by calculating and combining several factors, such as length (modified precision), word choice (recall), word order (distance), while penalizing candidate translations which are significantly longer or shorter than the GOLD standard (brevity penalty(BP)).
그렇다면 목표가 MT 또는 다른 NLP 작업이라면, 해당 NLP 작업에 표준인 자동 평가 지표를 사용하는 것은 어떨까?
예를 들어 MT에서 표준 평가 지표는 BLEU(BiLingual Evaluation Understudy) 점수이다(Papineni 등, 2002).
BLEU 점수는 기본적으로 GOLD 표준(BP)보다 상당히 길거나 짧은 후보 번역에 불이익을 주면서 길이(수정 정밀도), 단어 선택(리콜), 단어 순서(거리)와 같은 몇 가지 요소를 계산하고 결합하여 GOLD 표준 번역을 후보 번역과 비교한다.

Please see Figure 2.4 below:

![BLEU score calculation.png](img/BLEU score calculation.png)

Figure 2.4: BLEU score calculation
그림 2.4: BLEU 점수 계산

Given the nature of its calculation and considering the nature of TS, the BLEU score is bad metric by which to determine if TS has improved translation quality or not. For example, if we perform a sentence splitting simplifiction where one sentence is separated into two, the translation would reflect that and would most certainly be longer than the GOLD standard. The BLEU score would penalize this in its calculation of length, word order, and brevity penalty leading to a low BLEU score, without reflecting whether or not TS has improved translation quality. The BLEU is also criticized because it has no way of accounting for synonyms. If we perform a lexical simplification and choose a simple word in place of complicated word, then use an MT system, the output would likely reflect that simplification. However, even if the meaning is ultimately the same between the candidate and GOLD standard translations, if a synonym is used in the candidate translation, the BLEU score would penalize us for word choice. As Siddharthan, points out, a low BLEU score in a TS + MT system may well be indicative of a well functioning TS system (2014).
계산의 특성과 TS의 특성을 고려할 때, BLEU 점수는 TS가 번역 품질을 개선했는지 여부를 판단하는 잘못된 지표이다.
예를 들어, 한 문장이 두 개로 구분된 문장을 수행할 경우, 번역은 이를 반영할 것이며 GOLD 표준보다 훨씬 길 것이다.
BLEU 점수는 TS의 번역 품질 향상 여부를 반영하지 않고 길이, 어순 및 낮은 BLEU 점수로 이어지는 간결성 패널티 계산에서 이를 처벌할 수 있다.
BLEU는 또한 동의어를 설명할 방법이 없기 때문에 비판을 받는다.
어휘 단순화를 수행하고 복잡한 단어 대신 간단한 단어를 선택한 다음 MT 시스템을 사용하면 출력에 해당 단순화가 반영될 가능성이 높다.
그러나 후보 표준 번역과 GOLD 표준 번역 간에 궁극적으로 의미가 동일하더라도 후보 번역에 동의어가 사용된다면 BLEU 점수는 단어 선택에 대해 우리에게 불이익을 줄 것이다.
Siddharthan이 지적한 바와 같이, TS + MT 시스템에서 낮은 BLEU 점수는 TS 시스템이 잘 작동하고 있음을 나타냅니다(2014).

If readability and NLP automatic evalutation metrics are not a viable option for us, then the only remaining course would be the use of human evaluation. Indeed, unless the explict goal of the work was the exploration of evalutation methods for automated TS, all TS research reviewed for the current research utilized human evaluation to measure the performance of their TS system. However, where previous research focused on evaluting the performace of their TS system in combination with another NLP task, the current research will utilize human evaluation on both the simplified Korean that our system outputs and the translations that our simplifications result in. The reason for this being that the literature addressing the simplification of an Asian language is extremely limited, and therefore provides very little insight on simplification strategies for the task at hand.
가독성과 NLP 자동 평가 지표가 우리에게 실행 가능한 옵션이 아니라면, 남은 유일한 과정은 인간 평가의 사용일 것이다.
실제로 이 연구의 탐구 목표가 자동화된 TS에 대한 평가 방법의 탐구가 아니라면, 현재 연구를 위해 검토한 모든 TS 연구는 TS 시스템의 성능을 측정하기 위해 인간 평가를 활용했다.
그러나 이전 연구가 다른 NLP 과제와 함께 TS 시스템의 성능을 평가하는 데 초점을 맞췄던 경우, 현재 연구는 시스템이 출력하는 단순화된 한글과 단순화가 초래하는 번역 모두에 대한 인간 평가를 활용할 것이다.
그 이유는 아시아 언어의 단순화를 다루는 문헌이 극히 제한적이기 때문에 당면 과제에 대한 단순화 전략에 대한 통찰력을 거의 제공하지 못하기 때문이다.




### 2-4. Automated Asian Text Simplification

As stated above, the research addressing the automated simplification of an Asian language is extremely limited. This is a well documented issue in TS, as the majority of the research has been conducted from a European language perspective (Siddharthan, 2014). One goal of the current research is to increase TS's exposure to Asian NLP.
위에서 언급한 바와 같이, 아시아 언어의 자동 단순화를 다루는 연구는 극히 제한적이다.
대부분의 연구가 유럽어의 관점에서 수행되었기 때문에 이는 TS에서 잘 문서화된 문제이다(Siddharthan, 2014).
현재 연구의 한 가지 목표는 TS의 아시아 NLP 노출을 늘리는 것이다.




### 2-4-1. Automated Japanese Text Simplification

The object of the current research is the Korean language, however, the Japanese language enjoys far more attention than Korean on the international stage, and is therefore the object of NLP research more often than Korean. Additionally, though often an item of strong linguistic dabate, it is undeniable that Japanese and Korean bear many similarities in terms of grammatical structure. Therefore, any strategies used in Japanese TS might then be applicable when developing a Korean TS system. However, to date, there has only been one TS study written with a focus on Japanese.
이번 연구의 목적은 한국어이지만 국제무대에서 일본어는 한국어보다 훨씬 더 많은 관심을 받고 있기 때문에 한국어보다는 NLP 연구의 대상이 되고 있다.
게다가, 비록 종종 강한 언어학상의 한 항목이지만, 일본어와 한국어는 문법적인 구조 면에서 많은 유사점을 가지고 있다는 것은 부인할 수 없다.
따라서, 일본 TS에서 사용되는 모든 전략은 한국 TS 시스템을 개발할 때 적용될 수 있습니다.
그러나 현재까지 일본어에 초점을 맞춘 TS 연구는 단 한 건뿐이었다.

Unfortunately for the present research, Inui et al.'s focus was the use syntactic and lexical paraphrasing for the hearing-impaired whose sign language implements a completely different structure than the Japanese language (2003). As such, the research's focus was not so much fluent output as it was the emphasis of content words and de-emphasis of Japanese grammar not present in Japanese-sign langauge. Given the fact that the researcher's goal was not in line with current research's goal, and the fact that their results were of questionable value, this previous work is of little help to us.
본 연구에서 이누이 등은 수화가 일본어(2003)와 완전히 다른 구조를 구현한 청각 장애인을 위한 구문 및 어휘적 의역 사용에 중점을 두었다.
따라서, 이번 연구의 초점은 일본어 부호 언어에는 없는 내용 단어의 강조와 일본어 문법의 강조가 될 만큼 유창한 결과물은 아니었다.
연구자의 목표가 현재 연구의 목표와 일치하지 않는다는 사실과 그들의 결과가 의심스러운 가치를 가지고 있다는 사실을 고려하면, 이 이전 연구는 우리에게 거의 도움이 되지 않는다.




### 2-4-2. Automated Korean Text Simplification

The Korean language makes use of a phonemic writing system known as Hangeul (한글), which is composed of 14 consonants and 10 vowels. Unlike the English alphabet, Hanguel combines its consonants and vowels together to form a syllabic unit with 11,172 total combinations possible. The combination of these syllabic units form words, though there are indeed many mono-syllabic words in Korean. For example, 번역 is the combination of four consonants (ㅂ, ㄴ, ㅇ, ㄱ) and two vowels (ㅓ, ㅕ), forming the word beonyeok (translation). Until the end of 20th century, Korean was considered to be an Ural-Altaic language as it shares many features with other Ural-Altaic languages, such as the Subject-Object-Verb word order. However, due to the number of borrowings Korean bears from the Chinese language, Korean is currently defined as an isolated language (The National Institute of the Korean Language, 2008).
한국어는 14개의 자음과 10개의 모음으로 이루어진 한글이라고 알려진 음소 문자 체계를 사용한다.
영어 알파벳과 달리 한글은 자음과 모음을 결합하여 음절 단위를 형성하며 총 11,172개의 조합이 가능하다.
이러한 음절단위의 조합은 단어를 형성하지만, 한국어에는 실제로 많은 단음절 단어들이 있다.
예를 들어, '번역'은 네 개의 자음(ㅂ, ㄴ, ㅇ, ㄱ)과 두 개의 모음(ㅓ, ㅕ)가 합쳐져서 번역(번역)이 됩니다.
20세기 말까지, 한국어는 주어-목적어-동사어순과 같은 다른 우랄-알타이어와 많은 특징을 공유하기 때문에 우랄-알타이어로 여겨졌다.
그러나 한국어가 한자어로부터 차용되는 경우가 많아 현재 한국어는 고립어로 정의되고 있다(국립국어원, 2008).

Considering the disparate nature of Korean and English and the bilingual data scarcity between the two languages, a TS system for an NLP task involving both languages could be very useful. However, as was the case with Japanese TS, there is only one known study that automates Korean TS.
한국어와 영어의 이질적인 성격과 두 언어 사이의 이중 언어 데이터 부족을 고려할 때, 두 언어를 포함하는 NLP 작업을 위한 TS 시스템은 매우 유용할 수 있다.
하지만, 일본 TS의 경우와 마찬가지로, 한국어 TS를 자동화하는 연구는 단 한 가지밖에 없다.

In Chung et al., researchers automate a Korean TS system that improves the readability of Korean newspaper articles on the Internet for the hearing impaired (2013). Their approach is quite interesting as they shift meaningful content to prominent locations in the sentence and make use of the webpage format by highlighting objects of importance. The objective being that Korean-sign language and the Korean language have very different structures, making it difficult for the hearing-impaired to read Korean articles. By emphasizing important content via location and graphical representation, the participants in the study showed a greater reading comprehension when using the TS system. However, it was never the researchers' intention to create fluent Korean output, nor were the researchers attempting to use their output for an NLP task. This previous research is therefore of very little use to the present study.
정씨 등 연구원들이 청각장애인을 위해 인터넷에서 한국 신문 기사의 가독성을 향상시키는 한국어 TS 시스템을 자동화한다.
의미 있는 내용을 문장의 눈에 띄는 위치로 옮기고 중요한 대상을 강조하여 웹 페이지 형식을 활용하기 때문에 이들의 접근 방식은 매우 흥미롭다.
그 목적은 한국 수화와 한국어의 구조가 매우 달라 청각 장애인들이 한국 기사를 읽는 것을 어렵게 한다는 것이다.
위치 및 그래픽 표현을 통해 중요한 내용을 강조함으로써, 연구 참가자들은 TS 시스템을 사용할 때 더 높은 읽기 이해도를 보여주었다.
그러나, 유창한 한국어 산출물을 만드는 것은 결코 연구자들의 의도가 아니었고, 연구자들이 그들의 산출물을 NLP 작업에 사용하려고 시도하지도 않았다.
따라서 이 이전의 연구는 현재 연구에 거의 쓸모가 없다.




## 3. Samsung Machine Translation Corpus

The Samsung Machine Translation Corpus (SC) is a corpus created and provided by Samsung Electronics Limited to the Seoul National University Computational Linguistics Laboratoy for a partner machine translation project. It is the combination of two bilingual corpora of Korean and English, and Korean and Chinese. The origin of the corpus is not entirely certain, however, it contains transcriptions of spoken Korean that is believed to have been subsequently translated into English and Chinese. Though the domain of the corpus meanders in places, the majority of the content in the corpus is based around travel and business. As the primary focus of the current research is Korean and English, the Chinese portion of the corpus will not be discussed in any further detail. There were a total of 354,972 Korean and English sentence pairs.
삼성기계번역코퍼스(SC)는 삼성전자유한공사가 협력 기계번역 프로젝트를 위해 서울대 전산언어학과에 제공하고 있는 말뭉치이다.
그것은 한국어와 영어, 그리고 한국어와 중국어의 두 개의 2개 국어의 조합이다.
말뭉치의 기원은 완전히 확실치 않지만, 그것은 후에 영어와 중국어로 번역된 것으로 추정되는 구어체 한국어를 포함하고 있다.
말뭉치의 영역은 군데군데 굽이쳐 있지만, 말뭉치의 콘텐츠의 대부분은 여행과 사업에 기반을 두고 있다.
현재 연구의 주된 초점은 한국어와 영어이기 때문에 말뭉치의 중국어 부분은 더 이상 자세히 논의되지 않을 것이다.
총 354,972개의 한국어와 영어 문장 쌍이 있었다.




### 3-1. Corpus Description

As mentioned above, the SC contains a transcription of spoken Korean, however, unlike many corpora, this corpus is not a collection of conversations, posts, or paragraphs, but rather a collection of isolated sentences that have no bearing on or relation to each other. Additionally, as it is a corpus of spoken Korean, all registers of formality and honorifics are present in the corpus. Korean is an agglutinative language, meaning that morphemes attach to root words to create new word forms and increase word length (Haspelmath et al., 2013). In other words, as the formality and honorific content of the sentence changes, so too does the verb form and verbal ending. Below is an example of the morphological changes the verb 먹다, meokta (to eat), undergoes in the present tense as formality register and honorific level changes.
위에서 언급한 바와 같이, SC는 많은 말뭉치들과 달리, 이 말뭉치는 대화, 게시물 또는 단락의 집합이 아니라, 서로 관련이 없거나 관련이 없는 고립된 문장들의 집합이다.
또한, 그것은 구어체 한국어 말뭉치이기 때문에, 말뭉치에 모든 격식과 존댓말의 등록부가 존재한다.
한국어는 형태소가 어근 단어에 붙어서 새로운 단어 형태를 만들고 단어 길이를 늘린다는 의미의 집적 언어이다(Haspelmath et al., 2013).
즉, 문장의 형식과 존칭의 내용이 바뀌면서 동사의 형태와 구두의 결말도 바뀐다.
아래는 동사 '먹다'가 형식부등본과 존칭어급이 바뀌면서 현재형으로 변하는 형태학적 변화 사례이다.

![Example of Korean formality register and honorifics.png](img/Example of Korean formality register and honorifics.png)

Table 3.1: Example of Korean formality register and honorifics
표 3.1: 한국어 격식부 및 존칭의 예

What this means for the present research is, in order to create a syntactic simplification system that produces fluent Korean output, our system needs to match these verbal endings when reducing sentence complexity by the creation of independent sentences from sentence-internal clauses. This will be discussed in further detail in Chapter 4.
이것이 현재 연구에서 의미하는 것은, 유창한 한국어 출력을 내는 구문 단순화 시스템을 만들기 위해서, 우리의 시스템은 문장 내부 절로부터 독립적 문장을 만들어 문장 복잡성을 줄일 때 이러한 언어적 결말과 일치해야 한다는 것이다.
이에 대해서는 4장에서 자세히 설명하겠습니다.

The Korean portion of the corpus bears part-of-speech (POS) tags from what is believed to be an automatic POS tagger, and the POS tags are consistent with the tagging convention described in Han et al. (2001), with the exception of the ECS tag which is represented as EC in the corpus. The English portion of the corpus also contained POS tags consistent with the Penn Treebank tagging convention (Marcus et al., 1993). However, when the Moses SMT system, used in this study, was being trained, it was discovered that a higher BLEU score was yielded when using only Korean POS tags, and English POS tags were therefore discarded. As a point of reference, the baseline BLEU score yielded by this Moses build was 32.87, a relatively high baseline score for Korean to English SMT. The following table is an example of a bilingual sentence taken from the corpus. Please note that Korean Tagged refers to the original sentence in the corpus and is in the same format as the sentences used to train Moses, Korean Untagged is the same sentence with tags removed for ease of reading and is in the format used when utilizing other MT systems, like Google and Naver, and English refers to the English translation of the original Korean sentence.
말뭉치의 한국어 부분에는 자동 POS 태그로 추정되는 것의 음성 부분 태그(POS)가 있으며, POS 태그는 Han 등에 설명된 태그 지정 관례와 일치한다. (2001)
말뭉치에 EC로 표시되는 ECS 태그를 제외하고.
말뭉치의 영어 부분에는 Penn Treebank 태깅 관례와 일치하는 POS 태그도 포함되어 있었다(Marcus et al., 1993).
그러나 본 연구에서 사용된 Moses 시만텍 시스템을 교육하고 있을 때, 한글 POS 태그만 사용했을 때 더 높은 BLEU 점수가 산출되어 영문 POS 태그는 폐기된 것으로 밝혀졌다.
참고로, 이 모제스 빌드에 의해 산출된 기준 BLEU 점수는 32.87로, 한국어와 영국 시만텍의 기준 점수가 상대적으로 높았다.
다음 표는 말뭉치에서 가져온 이중 언어 문장의 예이다.
한국어 태그는 말뭉치의 원문을 지칭하며 모세를 훈련시키기 위해 사용되는 문장과 같은 형식이며, 한국어 태그는 읽기 쉽도록 제거된 동일한 문장이며 구글이나 네이버와 같은 다른 MT 시스템을 활용할 때 사용되는 형식이며, 영어는 한글 원문의 영어 번역본을 말합니다.

![Corpus sentence example.png](img/Corpus sentence example.png)

Corpus sentence example
말뭉치 문장 예제




### 3-2. Corpus Issues

A number of problems associated with the corpus plagued us during the course of this research. These issues are only addressed here as the thrust of this research is based in human evaluation. Similar problems may have little-to-no bearing on automatic evaluation metrics, but when humans are evaluating output from a system, the input must then also be of high quality.
이 연구의 과정에서 말뭉치와 관련된 많은 문제들이 우리를 괴롭혔다.
이 연구의 추진력이 인간 평가에 기초하고 있기 때문에 이러한 문제들은 여기서만 다루어진다.
유사한 문제는 자동 평가 지표와 거의 관련이 없을 수 있지만, 인간이 시스템 출력을 평가할 때 입력도 고품질이어야 한다.




#### 3-2-1. Korean Issues

During the implementation and development of the simplification system discussed in Chapter 4, a number of mis-tagging issues became apparent during testing of the system. For example, the Korean structure 어/아(서), which is a subordinating structure indicating cause and effect or a logical order between clauses, was consistently mis-tagged as follows: 아서/EC, 어서/EC, 아/EC, 어/EC, 아/EC|서/EC, 어/EC|서/EC, 아/EC 아/EC, 어/EC 어/EC, etc. Such inconsistencies had to be accounted for during the implementation our simplification system.
제4장에서 논의한 단순화 시스템의 구현 및 개발 중에 시스템 시험 중 많은 오타 문제가 명백해졌다.
예를 들어, 원인과 결과를 나타내는 종속구조인 한글구조 어/아(서)는 아서/EC, 어서/EC, 아/EC, 어/EC, 아/EC|서/EC, 어/EC|서/EC, 아/EC 아/EC, 어/EC 어/EC, 등으로 일관되게 잘못 표기되었다.
그러한 불일치는 구현 과정에서 고려되어야 했다.

Inconsistencies in tags are not terribly uncommon and part of the struggle in the NLP field, however, one at least expects the language itself to be natural. This was not the case at all as many of the Korean evaluators who participated in this study stated that the original Korean sentences themselves were unnatural or ungrammatical, even before simplification! Such problems may not pose an issue for automatic evaluation metrics, but for human evaluation the quality of the input is critical.
그러나 태그의 불일치는 매우 드문 일이 아니며 NLP 분야의 투쟁의 일부이지만 최소한 언어 자체가 자연스러울 것으로 예상한다.
이 연구에 참여한 많은 한국인 평가자들이 심지어 단순화 이전에도 원래 한국어 문장 자체가 부자연스럽거나 문법적이지 않다고 말했기 때문에 전혀 그렇지 않았다.
이러한 문제는 자동 평가 지표에는 문제가 되지 않을 수 있지만, 인간 평가의 경우 입력의 품질이 매우 중요하다.




#### 3-2-2. English Issues

The issues plaguing the English side of the corpus were perhaps even worse than the Korean, as the goal of this research is improved translation through simplification. English sentences often bore grammatical errors, for example, if the Korean sentence were "독립문 공원에 갑시다!" the English equivalent was often "Let's go to the Independence Park!" with an out-of-place determiner, the. Worse than ungrammaticality, the English sentence often did not bear the same meaning as the Korean. Consider the Korean and English in Table 3.2. The Korean implies that there are many professionally and financially successful women today, however, the English means that many successful women working in the field of finance. On top of this, it was often the case that content from Korean or English would be missing in the equivalent translations.
이 연구의 목적이 단순화를 통한 번역 개선이기 때문에 말뭉치의 영어측을 괴롭히는 문제는 아마도 한국어보다 훨씬 더 나빴을 것이다.
예를 들어, 만약 한국어 문장이 "독립문 공원에 가자!"였다면, 영어 문장은 종종 "독립공원으로 가자!"라는 문법적인 오류를 가지고 있었다.
문법적으로 맞지 않는 것보다 더 나쁜 것은, 영어 문장이 종종 한국어와 같은 의미를 지니지 않는다는 것이다.
표 3.2의 한국어와 영어를 고려하라.
한국인은 오늘날 직업적으로나 경제적으로 성공한 여성들이 많다는 것을 암시하지만, 영어는 많은 성공한 여성들이 금융 분야에서 일하고 있다는 것을 의미한다.
게다가, 한국어나 영어의 내용이 같은 번역에서 누락되는 경우가 종종 있었다.

For instance, consider the following sentence pair extracted from the corpus:
예를 들어, 말뭉치에서 추출한 다음 문장 쌍을 생각해 보자.

(1) a. 석-박사 학위를 취득할 때까지 4년은 걸릴거라 생각해요.
    b. I expect to take 4 years to earn a M.D and a Ph.D.. I hope it doesn't take any longer.
b. 나는 4년 후에 박사학위를 받을 수 있을 것으로 예상한다. 저는 그보다 더 걸리지 않기를 바래요.

While (1a) and the first sentence in (1b) express roughly the same idea, ignoring the fact that M.D. refers to medical doctor while 석사 means Master's degree, the second sentence in (1b) has no Korean equivalent and seemingly appears at random. This is an issue that impacts not only human evaluation, but also automatic evaluation, as there would be no Korean equivalent for the English sentence when Moses attempts word-alignment or when the BLEU score is calculated.
(1a)와 (1b)의 첫 번째 문장은 M.D.가 의사를, (1b)의 두 번째 문장은 석사 학위를 의미한다는 사실을 무시하고 거의 같은 생각을 표현하고 있으며, (1b)의 두 번째 문장은 한글에 상응하는 것이 없고 무작위로 나오는 것처럼 보입니다.
이것은 모세가 단어 정렬을 시도하거나 BLEU 점수를 계산할 때 영어 문장에 해당하는 한국어가 없기 때문에 인간 평가뿐만 아니라 자동 평가에도 영향을 미치는 문제입니다.




## 4. Korean Sentence Complexity Reduction System

The development of an all-encompassing Korean syntactic simplification system is a daunting task indeed, especially considering the fact that there exists no previous research on which to base such a system. The present research, then, attempts to introduce TS into Korean by performing the most basic syntactic simplification possible: the rephrasing of complex Korean sentences into less complex alternative(s) which bear the same meaning as the original sentence. Recall that sentence complexity refers to the number of clauses in a given sentence.
모든 것을 포괄하는 한국어 구문 단순화 시스템의 개발은 특히 그러한 시스템의 기반이 되는 선행 연구가 없다는 사실을 고려할 때 실제로 어려운 작업입니다.
그런 다음 본 연구는 가능한 가장 기본적인 구문 단순화를 수행하여 TS를 한국어에 도입하려고 시도합니다.
즉, 복잡한 한국어 문장을 원래 문장과 동일한 의미를 지닌 덜 복잡한 대안으로 바꾸는 것입니다.
문장 복잡성은 주어진 문장의 절 수를 나타냅니다.

For example, consider (1) below.

(1) a.
    오바마가 케냐에서 왔으면 트럼프는 화성에서 왔습니다.
    * Translation: If Obama's from Kenya, then Trump's from Mars.

    b.
    오바마가 케냐에서 왔습니다. 그러면 트럼프는 화성에서 왔습니다.
    * Translation: Obama's from Kenya. Then, Trump is from Mars.

(1a) is an example of Korean sentence internal clause-subordination via a if/then conjunction. As it bears two complete verb phrases, the sentence complexity can then be understood as two. (1b) conveys roughly the same meaning as (1a) and is given logical cohesion via a sentence connector. However this meaning is conveyed in two simpler sentences, each with a sentence complexity of one.
(1a)는 if/then 접속사를 통한 한국어 문장 내부절 종속의 예입니다.
두 개의 완전한 동사구를 포함하므로 문장 복잡성은 두 개로 이해될 수 있습니다.
(1b)는 (1a)와 거의 동일한 의미를 전달하며 문장 연결자를 통해 논리적 응집력이 부여됩니다.
그러나 이 의미는 각각 하나의 문장 복잡성을 갖는 두 개의 더 간단한 문장으로 전달됩니다.

This system is accomplished by the creation of rules which convert Korean clause connecting structures into independent sentences. After successfully creating independent sentences from sentence-internal clauses, addition steps were implemented, such as the insertion of appropriate sentence connectors, in order establish a logic between the sentences and generate a cohesive unit. The ultimate goal for the output of this system is the improvement of MT system output, however, we also hope to generate relatively natural Korean sentences. Additionally, through this system, we suggest a method by which to overcome the initial hurdle of simplifying sentences containing more than two clauses.
이 시스템은 구조를 연결하는 한국어 절을 독립적인 문장으로 변환하는 규칙을 생성하여 수행됩니다.
문장 내부 절에서 독립적인 문장을 성공적으로 생성한 후 문장 간의 논리를 설정하고 응집력 있는 단위를 생성하기 위해 적절한 문장 연결자를 삽입하는 등의 추가 단계를 구현했습니다.
이 시스템의 출력에 대한 궁극적인 목표는 MT 시스템 출력의 개선이지만, 우리는 또한 상대적으로 자연스러운 한국어 문장을 생성하기를 희망합니다.
또한 이 시스템을 통해 두 개 이상의 절을 포함하는 문장을 단순화하는 초기 장애물을 극복할 수 있는 방법을 제안합니다.




### 4-1. Rule Creation and Description

The Samsung Corpus (SC), which is discussed in Chapter 3, was reviewed and examined for appropriate clause connecting conjunctions. After extracting dozens of sentences from the corpus, several multiple sentence-splitting rewrites were attempted by hand and then translated via Google Translate. If the rewrite was thought to be relatively natural Korean, which also generated a better translation than the original sentence, the manual rewrite was automated via the programming language Java. It should be noted that this is a supervised task, making use of POS tags in order to distinguish between cases of ambiguity caused by Korean homophony. What follows is a detailed description of the rule-based Korean sentence complexity reduction system proposed by the present study.
3장에서 논의하는 Samsung Corpus(SC)를 검토하고 접속사를 연결하는 적절한 항목에 대해 검토했습니다.
말뭉치에서 수십 개의 문장을 추출한 후 손으로 여러 번 문장을 분할하여 다시 쓰기를 시도한 다음 Google 번역을 통해 번역했습니다.
재작성이 비교적 자연스러운 한국어로 원문보다 더 나은 번역이 나왔다고 생각되면 수동 재작성은 프로그래밍 언어인 Java를 통해 자동화되었습니다.
이것은 한국어 동음이의어에 의해 야기되는 모호함의 경우를 구별하기 위해 POS 태그를 사용하는 감독된 작업이라는 점에 유의해야 합니다.
다음은 본 연구에서 제안한 규칙 기반 한국어 문장 복잡도 감소 시스템에 대한 자세한 설명이다.




#### 4-1-1. Korean Coordination Simplification
한국어 조정 단순화(한국어 접속문 - 접속문을 이루는 연결어미)

The most common form of Korean coordination between two clauses would be conjunctive 고 go (and), though there are of course other examples. The current research simplified 고-coordinated sentences by inserting a period in place of go 고, or 고/EC as it appears in the corpus, and inserting 그리고 at the beginning of the newly formed next sentence. This operation is applicable to noun, adjective, or verb-ending clauses, though the form changes slightly depending on the word-type in question.
물론 다른 예가 있지만, 두 절 사이의 한국어 조정의 가장 일반적인 형태는 접속사 고 go (and)입니다.
현재 연구에서는 코퍼스에 나타난 go 고 또는 고/EC 자리에 마침표를 삽입하고 새로 형성되는 다음 문장의 시작 부분에 그리고를 삽입하여 고 등이 연결된 문장을 단순화했습니다.
이 작업은 명사, 형용사 또는 동사 어미 절에 적용할 수 있지만 문제의 단어 유형에 따라 형식이 약간 바뀝니다.

For example, please consider the summary below:

(1) a. Clause1 N/A/V-고 Clause2.
        * Original: 개스킷을 교체하고 팬벨트가 낡아서 새로운 것으로 교체했습니다.
        * Translation: (I) replaced the gasket, and since the fan belt was old, (I) replaced it with a new one.
        * Google Translate: Replace the gasket and replaced by a new fan belt narkahseo.

    b. Sentence1 N/A/V-다. 그리고 Sentence2.
        * Simplified: 개스킷을 교체합니다. 그리고 팬벨트가 낡아서 새로운 것으로 교체했습니다.
        * Translation: (I) replace the gasket. And then, since the fan belt was old, (I) replaced it with a new one.
        * Google Translate: Replace the gasket. And the fan belt narkahseo replaced it with a new one.

Despite the simplicity of the operation performed in (1b), the insertion of a sentence ending morpheme, a period, and a sentence connector, we see a vast improvement in Google Translate's handling of the two newly generated less complex sentences compared to the syntactically complex, original sentence. This is consistent with what we would expect from research conducted in the literature; less complex and shorter sentences are handled more effectively by SMT systems than complex, longer sentences.
(1b)에서 수행된 작업의 단순성, 문장 종결 형태소, 마침표 및 문장 연결기의 삽입에도 불구하고 구문적으로 복잡한 두 문장에 비해 새로 생성된 덜 복잡한 두 문장을 처리하는 Google 번역이 크게 향상되었습니다.
이것은 문헌에서 수행된 연구에서 기대하는 것과 일치합니다.
덜 복잡하고 짧은 문장은 복잡하고 긴 문장보다 SMT 시스템에서 더 효과적으로 처리됩니다.

There are a few decisions made during the implementation of our complexity reduction system that should be addressed, first among them being tense matching between the reduced sentences. Initially, it was our plan to match tenses between the sentences generated from clauses,
복잡성 감소 시스템을 구현하는 동안 해결해야 할 몇 가지 결정 사항이 있습니다.
그 중 첫 번째는 축소된 문장 간의 시제 일치입니다.
처음에는 절에서 생성된 문장 사이에 시제를 맞추는 것이 우리의 계획이었습니다.

for example, instead of generating the simplified sentences in (1b), we would generate the following:
예를 들어 (1b)에서 단순화된 문장을 생성하는 대신 다음을 생성합니다.

개스킷을 교체했습니다. 그리고 팬벨트가 낡아서 새로운 것으로 교체했습니다, based on the fact that the sentence as a whole is in the past tense.
개스킷을 교체했습니다. 그리고 팬벨트가 낡아서 새로운 것으로 교체했습니다는 그 문장 전체가 과거형이라는 사실에 근거하였다.

However, after attempting translation on several such sentences it was found that maintaining the tense the clauses themselves bore generated translations of greater quality. Additionally, not doing so often resulted in over-fitting and forced a meaning on the Korean sentence that was not intended by the original sentence.
그러나 이러한 여러 문장에 대해 번역을 시도한 후에 절 자체가 시제를 유지하는 것이 더 높은 품질의 번역을 생성한다는 것을 발견했습니다.
또한 그렇게 하지 않으면 과적합이 발생하여 원문에서 의도하지 않은 한국어 문장의 의미를 강제하는 경우가 많았습니다.

Next, one could argue that the insertion of 그리고, kurigo (and then), increases the complexity of the second clause sentence, therefore, negating our efforts and producing one sentence with a complexity of one followed by a second with a complexity of two. This is due to the fact that, syntactically, one could consider 그리고 as a sentence internal clause connector of the form 그리, kuri (that way), + 고, go (and).
다음으로, 그리고 kurigo (그리고 then)를 삽입하면 두 번째 절 문장의 복잡성이 증가하므로 우리의 노력을 무효화하고 복잡성이 1인 문장과 복잡성이 2인 두 번째 문장을 생성한다고 주장할 수 있습니다.
이는 문법적으로 그리고를 문장 내부절 연결자로 간주할 수 있다는 사실 때문입니다.

However, consider the way an MT system sees 그리고 compared to 고. The context of 고 is a fluid environment, ever shifting between verbs, adjectives, and nouns, and such a system can only determine the meaning of the morpheme 고 based on frequency of occurrence. Yet, the form and environment it appears in is inconsistent, as it is a productive morpheme. Additionally, the system must then attempt to determine which word 고 best corresponds to in English, even though 고 is not limited to only the translation of and in English. 고 is a part of many grammatical structures in Korean, not only conjunctive 고. For example, The morpheme also expresses desire, ~고 싶다, or appears in continuous tense, ~고 있다, etc.
그러나 고와 비교하여 MT 시스템이 보는 방식을 고려하십시오.
고의 문맥은 동사, 형용사, 명사 사이를 끊임없이 이동하는 유동적인 환경이며 이러한 시스템은 발생 빈도에 따라 형태소 고의 의미를 결정할 수 있습니다.
그러나 그것이 나타나는 형태와 환경은 생산적인 형태소이기 때문에 일관성이 없다.
또한 시스템은 고가 및 영어로의 번역에만 국한되지 않더라도 영어에서 고가 가장 잘 대응하는 단어를 결정하려고 시도해야 합니다.
고는 접속사 고뿐만 아니라 한국어의 많은 문법 구조의 일부입니다.
예를 들어, 형태소는 욕망, ~고 싶다를 표현하기도 하고, 진행형으로 나타나거나 ~고 있다 등이다.

Given these complications, it is little wonder that even a structure as simple and common as 고 poses problems for NLP tasks. On the other hand, consider 그리고, a nonproductive grouping of morphemes with only one form that is nearly always translated as and then or a close equivalent. Therefore, from a syntactic perspective, the insertion of 그리고 may be suspect, but from a computational perspective, it clearly improves translation quality by acting as a disambiguation tool. On top of that, in the Samsung Corpus (SC), 그리고 is represented as 그리고/MAG (bearing the MAG POS tag, being a magnifying phrase) and 고 is represented as 고/EC. That being the case, a supervised NLP system, such as the Moses SMT system used in the present research, would not even consider the two words/morphemes to be related because they bear completely different POS tags.
이러한 복잡성을 감안할 때 고처럼 단순하고 일반적인 구조라도 NLP 작업에 문제를 제기하는 것은 놀라운 일이 아닙니다.
다른 한편으로, 거의 항상 and then 또는 거의 동등한 것으로 번역되는 하나의 형태만을 갖는 비생산적인 형태소의 그룹인 그리고를 고려하십시오.
따라서 통사론적 관점에서 and의 삽입이 의심될 수 있지만, 계산적 관점에서 명확화 도구 역할을 하여 번역 품질을 향상시킵니다.
여기에 삼성코퍼스(SC)에서 그리고는 그리고/MAG(MAG POS 태그 부착, 돋보기)로, 고는 고/EC로 표기한다.
이 경우 현재 연구에 사용된 Moses SMT 시스템과 같은 지도 NLP 시스템은 완전히 다른 POS 태그를 포함하기 때문에 두 단어/형태소가 관련이 있는 것으로 간주조차 하지 않습니다.

Finally, just as important as a simplification system knowing which structures to simplify, so too must it know when to avoid simplification. As was mentioned above, 고 is an extremely productive morpheme in Korean, appearing in many Korean grammatical structures that express conjunction, desire, continuous tense, etc. However, the simplification system proposed by the present research views it as inappropriate and detrimental to simplify anything beyond conjunctive 고. Therefore, not only for 고, but for every structure handled by this system, exception lists were constructed to determine in which contexts clause reduction should be performed and which contexts it should not. This was achieved by viewing the sentence in question a linear string, finding the morpheme(s) in question, in this case conjunctive 고, and examining the contexts to the left and right of the morpheme as it appears in the string for exceptions. This process is summarized in the pseudocode in Algorithm 1 below.
마지막으로, 어떤 구조를 단순화해야 하는지 아는 단순화 시스템만큼 중요하므로 단순화를 피해야 할 때를 알아야 합니다.
고는 위에서 언급한 바와 같이 접속사, 욕망, 진행형 등을 표현하는 많은 한국어 문법 구조에 나타나며, 한국어에서 매우 생산적인 형태소이다.
그러나 본 연구에서 제안하는 단순화 체계는 모든 것을 단순화하는 데 부적절하고 해롭다고 본다.
접속사 고를 넘어서. 따라서 고뿐만 아니라 이 시스템에서 처리하는 모든 구조에 대해 예외 목록을 구성하여 어떤 컨텍스트에서 절 축소를 수행하고 어떤 컨텍스트에서 수행하지 않아야 하는지를 결정했습니다.
이것은 문제의 문장을 선형 문자열로 보고, 문제의 형태소(이 경우 접속 고)를 찾고, 예외에 대해 문자열에 나타나는 형태소의 왼쪽과 오른쪽 컨텍스트를 조사함으로써 달성되었습니다.
이 과정은 아래 알고리즘 1의 의사코드에 요약되어 있습니다.

![Simplification Exception Check.png](img/Simplification Exception Check.png)

for all 단어 in 단순화할 문장 do
    if 단어 contains 복잡성 감소의 사이트 역할을 하는 결합 then
        if 복잡성 감소의 사이트 역할을 하는 결합 starts with 예외를 형성하는 형태소 앞의 구조 목록 or
        if 복잡성 감소의 사이트 역할을 하는 결합 ends with 예외를 형성하는 형태소 뒤의 구조 나열
            break
        else
            continue
    end if
end for

Though the complexity reduction operation description above is not an exhaustive list of all conjoining structures handled by this system, the vast majority of them operate in a similar manner, following a similar logic by which we avoid the simplification of exceptions. Therefore, for space considerations, examples of simplification via positive coordinating structures will not follow this section, however, a list of structures considered to be coordination will be discussed in section 4.4.
위의 복잡성 감소 작업 설명이 이 시스템에서 처리하는 모든 결합 구조의 완전한 목록은 아니지만 대부분은 예외의 단순화를 피하는 유사한 논리에 따라 유사한 방식으로 작동합니다.
따라서 공간 고려를 위해 긍정적인 조정 구조를 통한 단순화의 예는 이 섹션을 따르지 않지만 조정으로 간주되는 구조 목록은 섹션 4.4에서 논의됩니다.




#### 4-1-2. Contrastive Coordination Simplification
대조적 조정 단순화

Contrastive coordination occurs when two or more clauses are somehow in conflict with each other, and this is realized in English typically in the form of but. The proposed complexity reduction system handles contrastive coordination in essentially the same way as the positive coordination example was reduced; the only change being the insertion of a different sentence connecting unit.
대조적 조정은 둘 이상의 절이 어떻게든 서로 충돌할 때 발생하며, 이는 일반적으로 but의 형태로 영어에서 실현됩니다.
제안된 복잡도 감소 시스템은 긍정적 조정 예가 감소된 것과 본질적으로 동일한 방식으로 대조 조정을 처리합니다.
유일한 변경 사항은 다른 문장 연결 단위의 삽입입니다.

Please see the example in (2) below:

(2) a. Clause1 N/A/V-은데 Clause2.
       * Original: 2개월 머물 것인데 짐 가방이 왜 그렇게 작습니까?
       * Translation: (We're) staying for two month, but why is (your) bag so small?
       * Google Translate: 2 months geotinde luggage Why did I stay so small?

    b. Sentence1 N/A/V-다. 그런데 Sentence2.
       * Simplified: 2개월 머물것입니다. 그런데 가방이 왜 그렇게 작습니까?
       * Translation: (We're) staying for 2 months. But why is (your) bag so small?
       * Google Translate: It will stay for 2 months. But luggage is so small, why?

The only difference between how the proposed system reduces sentence complexity for positive and contrastive coordination is the sentence connector inserted, which is determined based on the clause conjoining structure in question. As we can see in the above example, just as we saw with positive coordination in 4.1.1, even the simple operation performed here greatly increases Google translation quality between (2a) and (2b).
제안된 시스템이 긍정과 대조 조정을 위해 문장 복잡성을 줄이는 방법의 유일한 차이점은 해당 절 연결 구조를 기반으로 결정되는 삽입된 문장 연결자입니다.
위의 예에서 볼 수 있듯이 4.1.1에서 긍정적인 조정으로 보았듯이 여기에서 수행하는 간단한 작업만으로도 (2a)와 (2b) 사이의 Google 번역 품질이 크게 향상됩니다.

Additionally, as was the case with conjunctive 고, Korean homophony did not pose an issue here, because the majority of conjunctive structures targeted by our simplification system bear the ~/EC POS tag, while homophonous structures bear completely different tags. For example, consider 는데/EC vs. 는데/NNB. The former can be translated as but in English, and is therefore a target for conjunctive complexity reduction operations, while the latter is often understood as English while, and while it is a potential site for clause reduction, the means by which it would be reduced are completely different. However, as our system disambiguates based on POS tags, it does not pose an issue for us.
또한 접속사 고의 경우와 마찬가지로 한국어 동음이의어는 여기서 문제가 되지 않았습니다.
우리의 단순화 시스템이 대상으로 하는 대부분의 접속 구조가 ~/EC POS 태그를 포함하는 반면 동음이의 구조는 완전히 다른 태그를 포함하기 때문입니다.
예를 들어, 는데/EC vs 는데/NNB를 고려하십시오.
전자는 as로 번역될 수 있지만 영어로 되어 있으므로 결합 복잡도 감소 연산의 대상이 되는 반면 후자는 종종 영어로 이해되는 반면 절 축소의 잠재적인 사이트인 반면, 완전히 다릅니다.
그러나 우리 시스템은 POS 태그를 기반으로 명확화하므로 문제가 되지 않습니다.

A list of all contrastive conjunctive structures processed by the proposed system will be introduced in section 4.4.
제안된 시스템에 의해 처리되는 모든 대조적 결합 구조의 목록은 섹션 4.4에서 소개될 것입니다.




### 4-1-3. Indirect Sentence Reduction
간접 문장 줄이기

Another sentence type the proposed system attempts to reduce are sentences that contain indirect speech or thoughts conveyed via the 다고/EC structure in Korean.
제안하는 시스템이 한국어에서 다고/EC 구조를 통해 전달되는 간접 발화나 생각을 포함하는 문장을 줄이기 위해 시도한 또 다른 문장 유형입니다.

Please consider (3) below.

(3) a. TOPIC는 Clause1 N/A/V-다고 Clause2.
        * Original: 과학자들은 그 열대 우림에 아직 발전되지 않은 많은 종들이 있다고 믿고 있다.
        * Translation: Scientists believe there many species that have not yet developed in that tropical rainforest.
        * Naver Translate: Scientists have not yet developed in the rainforest believe that there are many species.

    b. Sentence1 N/A/V-다. TOPIC는 그렇게 Sentence2.
        * Simplified: 그 열대 우림에 아직 발전되지 않은 많은 종들이 있다. 과학자들은 그렇게 믿고 있다.
        * Translation: There are many species that have not yet developed in that tropical rainforest. That's what scientists believe.
        * Naver Translate: There are a lot of species not yet developed in the rainforest. Scientists believe so.

While similar to the previous reduction strategies introduced so far, indirect sentence simplification varies slightly as we assume the leftmost topic bearing the 은/는/JX morpheme acts the subject of the matrix clause, while subjects or topics, right of the leftmost topic, act as the subject of the embedded clause. Please consider the visualization below:
지금까지 소개된 이전 축소 전략과 유사하지만 은/는/JX 형태소를 포함하는 가장 왼쪽의 주제가 행렬 절의 주어 역할을 하고 가장 왼쪽 주제의 오른쪽인 주제 또는 주제가 역할을 한다고 가정하기 때문에 간접 문장 단순화는 약간 다릅니다.
포함된 조항의 주제로.

Please consider the visualization below:

![Indirect Sentence Reduction.png](img/Indirect Sentence Reduction.png)

By assuming this pairing, we therefore copy and track the leftmost topic before splitting the sentence and inserting a period and 그렇 게, kurutke (in that way), to establish cohesive logic between the generated sentences. Due to the linear nature of this Korean grammar pattern, where the matrix clause is the rightmost clause, we then are able to simply insert the leftmost topic into the rightmost newly generated sentence, and then delete it from its original position.
따라서 이 쌍을 가정하여 문장을 분할하고 마침표를 삽입하기 전에 가장 왼쪽의 주제를 복사하고 추적하여 생성된 문장 사이에 응집력 있는 논리를 설정합니다.
행렬 절이 맨 오른쪽 절인 이 한국어 문법 패턴의 선형 특성으로 인해 새로 생성된 가장 오른쪽 문장에 맨 왼쪽 주제를 간단히 삽입한 다음 원래 위치에서 삭제할 수 있습니다.

While slightly more complicated and syntactically motivated than the previous complexity reductions, this relatively simple operation generates a much better translation using Naver Translate, a cutting-edge NMT system, as can be seen in (3b). A full list of the indirect structures covered by this reduction system will be introduced section 4.4.
이전의 복잡성 감소보다 약간 더 복잡하고 구문론적 동기가 부여되었지만, 이 비교적 간단한 작업은 (3b)에서 볼 수 있듯이 최첨단 NMT 시스템인 네이버 번역을 사용하여 훨씬 더 나은 번역을 생성합니다.
이 감소 시스템이 적용되는 간접 구조의 전체 목록은 섹션 4.4에서 소개됩니다.




#### 4-1-4. Gerund Reduction
동명사 감소

Another syntactically complex structure reduced in similar way to the indirect speech structure would be that of Korean gerunds; specifically gerunds of the form verb/adjective~기 acting as the topic, subject, or object of the sentence.
간접적인 화법 구조와 유사한 방식으로 축소된 또 다른 구문적으로 복잡한 구조는 한국어 동명사의 구조일 것입니다.
구체적으로 동사/형용사~기 형태의 동명사는 문장의 주제, 주제 또는 목적어 역할을 합니다.

Please consider the example in (4) below.

(4) a. TOPIC는 Clause1 A/V-기를 Clause2.
        * Original: 부모님은 내가 늦게 까지 자지 않고 있기를 원하지 않으셨다.
        * Translation: My parents did not want me staying up late.
        * Google Translate: My parents did not want to be without me stay up late.

    b. Sentence1 N/A/V-다. TOPIC는 그것을 Sentence2.
        * Simplified: 내가 늦게까지 자지 않고 있었다. 부모님은 그것을 원하지 않으셨다.
        * Translation: I did not sleep until late. My parents did not want it.
        * Google Translate: I do not sleep late. My parents did not want it.

The example in (4) proceeds with a logic very similar to the example in (3), where the leftmost topic is assumed to be the subject of the matrix clause and is therefore copied, inserted into the rightmost sentence after its generation, and then deleted from its original position. When the gerund phrase is the topic or subject of the sentence, such topic reorientation would be unnecessary. Additionally, as this is an example of the gerund functioning as the object of the sentence, the pronoun 그것, kugeut (that), is inserted to function as the object of the rightmost sentence after the deletion of the gerund phrase. Though the logic is similar, different pronouns are inserted when processing a gerund phrase functioning as the subject or topic of the sentence.
(4)의 예는 (3)의 예와 매우 유사한 논리로 진행됩니다.
여기서 가장 왼쪽의 주제는 행렬 절의 주제로 가정되고 따라서 생성된 후 가장 오른쪽 문장에 복사되고 삽입된 다음 원래 위치에서 삭제되었습니다.
동명사가 문장의 주제나 주제인 경우에는 이러한 주제의 방향 전환이 필요하지 않습니다.
또한 동명사가 문장의 목적어 역할을 하는 예이므로 동명사구 삭제 후 맨 오른쪽 문장의 목적어로 쓰이도록 대명사 '그'를 삽입한다.
논리는 비슷하지만 문장의 주어나 주제 역할을 하는 동명사구를 처리할 때 다른 대명사가 삽입됩니다.

As a comparison between (4a) and (4b) shows, sentence complexity reduction through the creation of independent sentences greatly increases Google translation quality. This is due to the reduced sentence complexity each sentence individually bears, making for much easier processing by the SMT Google Translation system. Additionally, we have substituted a productive grammar structure, with many different possible forms (V/A~기), for a common non-productive pronoun with only one form (그것). In this way we have maintained the meaning of the original sentence through logical cohesion, reduced sentence complexity, and generated better SMT output.
(4a)와 (4b)를 비교하면 알 수 있듯이 독립적인 문장 생성을 통한 문장 복잡도 감소는 Google 번역 품질을 크게 향상시킵니다.
이는 각 문장이 개별적으로 부담하는 문장 복잡성이 감소하여 SMT Google 번역 시스템에서 훨씬 쉽게 처리할 수 있기 때문입니다.
또한, 우리는 생산적인 문법 구조를 다양한 가능한 형태(V/A~기)로 대체했으며, 일반적인 비생산적인 대명사를 단 하나의 형태(I)로 대체했습니다.
이러한 방식으로 우리는 논리적 응집력을 통해 원래 문장의 의미를 유지하고 문장 복잡성을 줄였으며 더 나은 SMT 출력을 생성했습니다.




### 4-1-5. Cause and Effect Reduction
원인 및 결과 감소

Korean is well known for possessing an uncommonly large number of subordinated structures that express a cause and effect relationship between clauses. All structures bear their own nuanced meaning, however, in English, they are often translated as because. Due to this potential many-to-one mapping when translating between languages, the current research proposes a generalized approach for the handling of this sentence type. Given that the nuanced meaning these structures bear will likely be lost in translation anyway, we propose processing these nuance structures in exactly the same way, regardless of their form.
한국어는 절 사이의 인과 관계를 표현하는 종속 구조가 비정상적으로 많은 것으로 잘 알려져 있습니다.
모든 구조는 고유한 뉘앙스의 의미를 가지고 있지만, 영어에서는 종종 원인으로 번역됩니다.
언어 간 번역 시 잠재적인 다대일 매핑으로 인해 현재 연구에서는 이 문장 유형을 처리하기 위한 일반화된 접근 방식을 제안합니다.
이러한 구조가 갖는 미묘한 의미가 어쨌든 번역에서 손실될 가능성이 있다는 점을 감안할 때 형식에 관계없이 이러한 뉘앙스 구조를 정확히 동일한 방식으로 처리할 것을 제안합니다.

Please see the example in (5) below.

(5) a. Clause1 N/V/A-니(까), 해서, 때문/덕분, 인하여(etc) Clause2.
        * Original: 영어가 서툴러 영어로 설명할 수 없습니다.
        * Translation: Because (my) English is clumsy, (I) can't explain in English.
        * Google Translate: English can not be described as clumsy English.

    b. Clause2 → Sentence1. 왜냐하면 Clause1 → Sentence2때문이다.
        * Simplified: 영어로 설명할 수 없습니다. 왜냐하면 영어가 서투르기 때문입니다.
        * Translation: (I) cannot explain in English. This is because (my) English is clumsy.
        * Google Translate: I can not explain in English. This is because English is awkward.

The method by which the current research simplifies cause and effect sentence constructions in Korean is slightly more complicated than our previous simplification proposals. After identifying the structure in question, we split the sentence at the structure boundary with a period, delete the structure (in this case 어/아(서)), and insert 기 때문이다, gi ddaemunida (because of), in the original structure's position. We then perform a sentence reordering, where the clause to the left of the simplification site (now a sentence) and the clause to right of the site (also now a sentence) change places. The final step is the insertion of 왜냐하면, waenyahamyun (because of), which happens at the beginning of the newly formed sentence containing 기 때문이다. This serves as a means of generating more natural Korean output and as a disambiguating sentence connector to establish a logical flow between the sentences.
현재 연구가 한국어의 인과관계 문장 구성을 단순화하는 방법은 이전의 단순화 제안보다 약간 더 복잡합니다.
해당 구조를 파악한 후, 구조 경계에서 문장을 마침표로 구분하여 구조를 삭제하고(여기서는 어/아(서)), 원문에 기생이다, gi ddaemunida(~때문에)를 삽입한다. 구조의 위치.
그런 다음 단순화 사이트(지금은 문장)의 왼쪽에 있는 절과 사이트(지금도 문장)의 오른쪽에 있는 절이 위치를 바꾸는 문장 재정렬을 수행합니다.
마지막 단계는 '때문에'를 삽입하는 것으로, 새로 형성된 기이를 포함하는 문장의 시작 부분에 발생한다.
이는 보다 자연스러운 한국어 출력을 생성하는 수단이자 문장 간의 논리적 흐름을 설정하기 위한 명확한 문장 연결기 역할을 합니다.

This process is summarized in the pseudocode in Algorithm 2 below.

![Cause and Effect Reduction.png](Cause and Effect Reduction.png)

sent : 단순화되는 문장(들)
morph : 단순화의 자리 역할을 하는 형태소
morph left : 단순화 사이트의 왼쪽에 있는 절/문장
morph right: 단순화 사이트의 왼쪽에 있는 절/문장
temp : 자리 표시자 문자열

for all words in sent do
    if word contains morph
        morph → "기 때문이다."
        morph left → temp
        morph right → morph left
        temp → morph right
        insert "왜냐하면" at temp-1
        return morph left + temp
        temp → null
    end if
end for

Though slightly more complicated than our initial simplification proposals, the method by which the proposed clause reduction system simplifies sentences is still relatively straight forward. Additionally, it suggests a generalized approach for processing structures that bear nuanced meaning in the source language, but lose this nuance when translated into the target language. Generalizing structures to a more common form or simplification has been a common thread throughout this research and will be discussed in greater detail in section 4.3. On top of this, as can be clearly seen in (5a) and (5b), translation quality is greatly improved when utilizing the proposed sentence complexity reduction approach. A full list of structures processed in this way will be introduced in section 4.4.
초기 단순화 제안보다 약간 더 복잡하지만 제안된 절 축소 시스템이 문장을 단순화하는 방법은 여전히 비교적 간단합니다.
또한, 소스 언어에서 미묘한 의미를 지니지만 대상 언어로 번역될 때 이러한 뉘앙스를 잃는 구조를 처리하기 위한 일반화된 접근 방식을 제안합니다.
구조를 보다 일반적인 형태 또는 단순화로 일반화하는 것은 이 연구 전반에 걸쳐 공통된 스레드였으며 섹션 4.3에서 더 자세히 논의될 것입니다.
또한, (5a)와 (5b)에서 명확하게 볼 수 있듯이 제안된 문장 복잡도 감소 접근 방식을 활용하면 번역 품질이 크게 향상됩니다.
이러한 방식으로 처리된 구조의 전체 목록은 섹션 4.4에서 소개됩니다.

Due to space constraints, additional sentence complexity reduction rules utilized in this research will not be discussed any further, however, the most complicated examples have already been introduced and the remaining simplification types follow a similar logic.
본 연구에서 활용하는 추가적인 문장 복잡도 감소 규칙은 지면의 제약으로 더 이상 다루지 않겠지만, 가장 복잡한 예는 이미 소개되었으며 나머지 단순화 유형은 유사한 논리를 따릅니다.




### 4-2. Factorial Complexity Reduction
요인 복잡도 감소

As was noted in Chapter 2, sentence complexity can pose a substantial issue for syntactic simplification systems when they are first introduced into a language. For example, when Collados introduced his Spanish syntactic simplification system, he was limited to only the simplification of Spanish sentences bearing two clauses, that is, a sentences with a complexity of two (2013). In other words, Collados only performed one simplification per sentence. Considering the pro-drop nature of Korean, where entire clauses or even sentences may be nothing but bare verb phrases with no subjects, objects, or topics, the current research views this hurdle extremely limiting.
2장에서 언급했듯이 문장 복잡성은 언어에 처음 도입될 때 구문 단순화 시스템에 상당한 문제를 제기할 수 있습니다.
예를 들어, Collados가 스페인어 구문 단순화 시스템을 도입했을 때 두 개의 절, 즉 복잡도가 2인 문장을 포함하는 스페인어 문장의 단순화에만 국한되었습니다(2013).
즉, Collados는 문장당 하나의 단순화만 수행했습니다.
전체 절이나 문장이 주어도, 목적어도, 주제도 없는 단순한 동사구에 불과한 한국어의 친드랍적 특성을 고려할 때, 현재의 연구는 이 장애물을 극히 제한적으로 보고 있다.

Additionally, when attempting to simplify Korean sentences with a complexity greater than two, there is no basis on which to determine which simplification combination or order would generate the most natural Korean or the best translation. It is possible to force such a decision, however, it is our belief that such a determination should be left up to Korean native speakers evaluating simplified Korean output, and English native speakers evaluating MT output. Therefore, in the present research we propose a method to overcome this initial hurdle and provide foundational insight into what simplifications and simplification combinations generate the most natural Korean and/or the best translations, which we term factorial complexity reduction.
또한 복잡도가 2보다 큰 한국어 문장을 단순화하려고 할 때 가장 자연스러운 한국어 또는 최상의 번역을 생성하는 단순화 조합 또는 순서를 결정할 근거가 없습니다.
이러한 결정을 강제할 수도 있지만, 그러한 결정은 한국어 간체 출력을 평가하는 한국어 원어민과 MT 출력을 평가하는 영어 원어민에게 맡겨야 한다고 생각합니다.
따라서 본 연구에서 우리는 이 초기 장애물을 극복하고 어떤 단순화 및 단순화 조합이 가장 자연스러운 한국어 및/또는 최고의 번역을 생성하는지에 대한 기초적인 통찰력을 제공하는 방법을 제안합니다.

By viewing complex sentences as a string of clause boundaries and making note of these clause boundaries, we are able to view the sentence as a series of clause reduction operations that, when combined together one-by-one, become a cohesive unit of simplified sentences. In other words, we view each simplification possible in a sentence as a factor that, when combined together with other possible simplifications, generate the final, completely simplified unit, hence the factorial nature. We then are able to generate all possible simplifications and all possible simplification permutations in a given syntactically complex sentence.
복잡한 문장을 일련의 절 경계로 보고 이러한 절 경계를 기록함으로써 문장을 하나씩 결합할 때 단순화된 문장의 응집력 있는 단위가 되는 일련의 절 축소 작업으로 볼 수 있습니다.
다시 말해서, 우리는 문장에서 가능한 각 단순화를 다른 가능한 단순화와 결합할 때 최종적이고 완전히 단순화된 단위를 생성하는 요인으로 간주하므로 계승적 특성이 나타납니다.
그런 다음 주어진 구문으로 복잡한 문장에서 가능한 모든 단순화와 가능한 모든 단순화 순열을 생성할 수 있습니다.

Please see the example in (6) below.

(6) a. 아 죄송하지만 예약을 재확인하지 않으셨기 때문에 성함이 탑승자 명단에서 빠져 있습니다.
        * Translation: Ah, I'm sorry, but because you did not reconfirm your reservation, your name is not on the passenger list.

    b. 아 죄송합니다. 하지만 예약을 재확인하지 않으셨기 때문에 성함이 탑승자 명단에서 빠져 있습니다.
        * Translation: Ah, I'm sorry. But because you did not reconfirm your reservation, your name is not on the passenger list.

    c. 아 죄송하지만 성함이 탑승자 명단에서 빠져 있습니다. 왜냐하면 예약을 재확인하지 않으셨기 때문입니다.
        * Translation: Ah, I'm sorry, but your name is not on the passenger list. This is because you did not reconfirm your reservation.

    d. 아 죄송합니다. 하지만 성함이 탑승자 명단에서 빠져 있습니다. 왜냐하면 예약을 재확인하지 않으셨기 때문입니다.
        * Translation: Ah, I'm sorry. But your name is not on the passenger list. This is because you did not reconfirm your reservation.

(6a) above is the original sentence before simplification. By scanning the sentence from left to right, we are able to note clause boundaries, determine which simplifications are possible, and then begin clause reduction operations from left to right as they appear in the sentence. (6b) shows the first simplification our system would perform, which is a contrastive clause coordination similar to the example described in section 4.1.2. Our system outputs the simplified sentences, updates the list of factorial simplifications, and continues. The next simplification possible can be seen in (6c) and is of the cause and effect variety, which is described in section 4.1.5. By noting the clause boundaries and only reordering the relevant clauses, the system successfully performs sentence complexity reduction, updates the list of factorial simplifications, outputs the reduced sentences, and continues on. We have now exhausted the number of possible simplifications available in our original sentence, so the only option left is to output the combination of both complexity reduction operations, which can be seen in (6d). For the sake of space and simplicity, we have described an example with a sentence complexity of three, therefore, outputting the two possible syntactic simplifications and one simplification combination. However, there is no limit to the number of complexity reduction operations and permutations our system could perform, so long as the sentence in question were sufficiently complex.
위의 (6a)는 간략화 전의 원문이다.
문장을 왼쪽에서 오른쪽으로 스캔하여 절 경계를 확인하고 어떤 단순화가 가능한지 결정한 다음 문장에 나타날 때 왼쪽에서 오른쪽으로 절 축소 작업을 시작할 수 있습니다.
(6b)는 우리 시스템이 수행할 첫 번째 단순화를 보여줍니다.
이는 섹션 4.1.2에 설명된 예와 유사한 대조절 조정입니다.
우리 시스템은 단순화된 문장을 출력하고 계승 단순화 목록을 업데이트한 다음 계속합니다.
가능한 다음 단순화는 (6c)에서 볼 수 있으며 4.1.5절에 설명된 다양한 원인과 결과입니다.
절 경계를 확인하고 관련 절만 재정렬함으로써 시스템은 문장 복잡성 감소를 성공적으로 수행하고 계승 단순화 목록을 업데이트하고 축소된 문장을 출력하고 계속합니다.
우리는 이제 원래 문장에서 사용할 수 있는 가능한 단순화의 수를 소진했으므로 남은 유일한 옵션은 (6d)에서 볼 수 있는 두 복잡성 감소 작업의 조합을 출력하는 것입니다.
공간과 단순함을 위해 문장 복잡도가 3인 예를 설명했으므로 두 가지 가능한 구문 단순화와 하나의 단순화 조합을 출력합니다.
그러나 문제의 문장이 충분히 복잡하다면 우리 시스템이 수행할 수 있는 복잡성 감소 연산 및 순열의 수에는 제한이 없습니다.




### 4-3. Phrase Grouping and Generalization
구문 그룹화 및 일반화

Throughout section 4.1 above, during the descriptions of various rules, we made mention of grouping certain nuance structures together and simplifying them in a manner to motivate disambiguation. For example, in 4.1.5 we discuss the insertion of 왜냐하면 and 때문이다, which, when translated into English, both roughly equate to because of, into the clause bearing the cause of the preceding clause which bears the effect. Following this logic, this research suggests the grouping of infrequent nuance structures together with more frequent structures that carry essentially the same meaning, especially when losing their nuanced meaning during translation into English.
위의 섹션 4.1 전체에서 다양한 규칙을 설명하는 동안 특정 뉘앙스 구조를 그룹화하고 명확성을 유도하는 방식으로 단순화하는 것에 대해 언급했습니다.
예를 들어, 4.1.5절에서 우리는 영어로 번역할 때 왜냐하면과 때문이다를 삽입하는 것을 논의하는데, 이는 영어로 번역될 때 둘 다 대략 to 때문에와 동일하다.
이러한 논리에 따라, 이 연구는 특히 영어로 번역하는 동안 뉘앙스 의미를 잃을 때 본질적으로 동일한 의미를 전달하는 보다 빈번한 구조와 함께 드물게 뉘앙스 구조를 그룹화할 것을 제안합니다.

For example, consider the case of 더라도/EC, duhrado, and 도/EC, do. The former occurs 78 times in the SC while the latter occurs 4,538 times, yet when translated into English, both structures are typically understood as even though or even if. When we perform sentence splitting complexity reduction operations on these structures, instead of viewing them as unique, this research suggests grouping such clause conjunctions together, generalizing, and performing the same generalized simplification on both. Generalizing to a more frequent form, which the MT system in question has seen more often, increases translation quality as a greater frequency of occurrence is beneficial to all statistical machine learning techniques.
예를 들어, '완전/EC', '두라도', '도/EC'의 경우를 생각해보자.
전자는 SC에서 78번 발생하고 후자는 4,538번 발생하지만 영어로 번역할 때 두 구조는 일반적으로 even though 또는 even if로 이해됩니다.
이러한 구조에 대해 문장 분할 복잡성 감소 작업을 수행할 때 고유한 것으로 보는 대신 이러한 절 접속사를 함께 그룹화하고 일반화하고 둘 모두에 대해 동일한 일반화 단순화를 수행하는 것이 좋습니다.
문제의 MT 시스템이 더 자주 보았던 더 빈번한 형식으로 일반화하면 발생 빈도가 높을수록 모든 통계적 기계 학습 기술에 유리하므로 번역 품질이 향상됩니다.

For example please consider (7) below.

(7) a. Original: 3 개월 이상에 해당하는 양의 약은 아무리 복용용이라 하더라도 반입하실 수 없습니다.
        * Translation: Even if you say will take it, you cannot bring more than 3 months worth of medicine.
        * Naver Translate: Embargo of corresponding amount of medicine is however one for take inmore than three months can not.

    b. Simplified: 3 개월 이상에 해당하는 양의 약은 아무리 복용용이라 합니다. 그래도 반입하실 수 없습니다.
        * Naver translate: Corresponding amount of medicine is no matter how one for taking on more than three months. Can not still carrying them into.

Additionally, when possible, we attempt to substitute frequent, non-productive pronouns or magnifying phrases in place of productive grammar structures that can appear in many different shapes and forms. The reason for this being nonproductive words typically only have one form, and are therefore much easier to find a one-to-one translation in the target language than productive conjunctive structures with forms as various as the number of verbs, nouns, and adjectives in a source language. We believe this phrase grouping and generalization logic is not limited to only Korean, and could have an application in all languages as a tool for compensating for data scarcity during NLP tasks.
또한 가능하면 다양한 모양과 형태로 나타날 수 있는 생산적인 문법 구조 대신 빈번하고 비생산적인 대명사 또는 확대구로 대체하려고 합니다.
이것이 비생산적인 단어인 이유는 일반적으로 하나의 형태만을 가지므로 목표 언어에서 동사, 명사 및 형용사의 수만큼 다양한 형태의 생산적 접속 구조보다 일대일 번역을 찾는 것이 훨씬 쉽습니다. 소스 언어.
우리는 이 구문 그룹화 및 일반화 논리가 한국어에만 국한되지 않고 NLP 작업 중 데이터 부족을 보완하기 위한 도구로 모든 언어로 응용할 수 있다고 믿습니다.

A list of the phrase groupings made during implementation of this sentence complexity reduction system will be introduced in the next section, 4.4.
이 문장 복잡도 감소 시스템을 구현하는 동안 만들어진 구문 그룹 목록은 다음 섹션인 4.4에서 소개됩니다.




### 4-4. System Coverage
시스템 적용 범위

This section details the coverage of the proposed Korean sentence complexity reduction system as it applies to the Samsung Corpus (SC). In other words, how many sentences within the corpus could our system apply to and simplify? Technically, as the system was constructed with a filter to sort out sentences with insufficient complexity, that is, sentences bearing only one verb phrase, our system has 100% coverage as it would ignore sentences with insufficient complexity or sentences that are only comprised of expectations. As was mentioned in section 4.1.1, not simplifying inappropriately is just as important as successful simplification. However, disregarding this logic, the following table summarizes the grouping of conjunctive structures our system applies to and the percentage of sentences in the corpus they appear in. As a point of reference, there are a total of 354,972 sentences in the corpus. Structures are divided by parenthesis and commas for ease of viewing.②
이 섹션에서는 Samsung Corpus(SC)에 적용되는 제안된 한국어 문장 복잡성 감소 시스템의 적용 범위를 자세히 설명합니다.
즉, 코퍼스 내에서 우리 시스템이 적용하고 단순화할 수 있는 문장은 몇 개입니까?
기술적으로, 시스템은 복잡성이 충분하지 않은 문장, 즉 하나의 동사구로 구성된 문장을 분류하는 필터로 구성되었으므로 복잡성이 불충분한 문장이나 기대만으로 구성된 문장을 무시하므로 100% 적용 범위를 갖습니다.
섹션 4.1.1에서 언급했듯이 부적절하게 단순화하지 않는 것이 성공적인 단순화만큼 중요합니다.
그러나 이러한 논리를 무시하고 다음 표에는 우리 시스템이 적용되는 연결 구조의 그룹화와 그것이 나타나는 문장의 비율이 요약되어 있습니다.
참고로 말뭉치에는 총 354,972개의 문장이 있습니다.
구조는 보기 쉽도록 괄호와 쉼표로 구분합니다.②

② As was mentioned in section 4.1.1, when the proposed system checks for simplification exceptions, it looks to the right and left of the simplification site. This is reflected in grouping marked with exception, as the conjunctive structure may have a null to its immediate right or left. This simply means the system need not check to the right or left of the simplification site.
② 4.1.1절에서 언급한 바와 같이 제안하는 시스템은 단순화 예외사항을 확인할 때 단순화 사이트의 좌우를 본다.
이것은 결합 구조가 바로 오른쪽이나 왼쪽에 null을 가질 수 있기 때문에 예외로 표시된 그룹화에 반영됩니다.
이것은 단순히 시스템이 단순화 사이트의 오른쪽이나 왼쪽을 확인할 필요가 없다는 것을 의미합니다.

!(System Coverage-1.png)[img/System Coverage-1.png]
!(System Coverage-2.png)[img/System Coverage-2.png]

Whether it be the application of a simplification or knowing when a simplification would be inappropriate, the proposed complexity reduction system can successfully review approximately 77% the sentences in the SC. This is achieved by grouping 137 structures into 17 different sets, generalizing, and simplifying based on the rules described in section 4.1. This is in no way an exhaustive list, as there are likely grammar structures not considered by the current study. However, we are confident that the system could be simply updated to incorporate new conjunctions should they become known. For example, a conjunction not considered by his research would be that of N/A/V든지, which roughly expresses an equality between clauses, which in English is often realized as or. Though untested by the current research, we believe such a structure would easily fall within the Or grouping provided above. We leave the discovery of additionally conjunctions to future research.
단순화의 적용이든 단순화가 부적절할 때를 아는 것이든 제안된 복잡도 감소 시스템은 SC의 약 77% 문장을 성공적으로 검토할 수 있습니다.
이것은 137개의 구조를 17개의 다른 세트로 그룹화하고 섹션 4.1에 설명된 규칙을 기반으로 일반화 및 단순화함으로써 달성됩니다.
현재 연구에서 고려하지 않은 문법 구조가 있을 수 있으므로 이것은 완전한 목록이 아닙니다.
그러나 우리는 새로운 접속사가 알려지면 시스템을 간단히 업데이트하여 새로운 접속사를 통합할 수 있다고 확신합니다.
예를 들어 그의 연구에서 고려하지 않는 접속사는 N/A/V던 인데, 이는 영어에서 or로 구현되는 경우가 많은데, 이는 절 사이의 동등성을 대략적으로 표현합니다.
현재 연구에서는 테스트되지 않았지만 이러한 구조는 위에서 제공된 Or 그룹에 쉽게 속할 것이라고 생각합니다.
추가 접속사에 대한 발견은 향후 연구에 맡깁니다.




### 4-5. System Architecture
시스템 구조

The proposed Korean sentence complexity reduction system is heavily based on the simplification architecture introduced by Siddharthan (2002). However, a shortcoming of Siddharthan's research is its exclusive focus on European languages, therefore, some of the steps he suggests are inappropriate for Korean simplification, and the Samsung Corpus (SC) in particular.
제안된 한국어 문장 복잡도 감소 시스템은 Siddharthan(2002)이 도입한 단순화 아키텍처를 기반으로 합니다.
그러나 Siddharthan의 연구의 단점은 유럽 언어에 대한 독점적인 초점이므로 그가 제안한 단계 중 일부는 한국어 간체, 특히 Samsung Corpus(SC)에 적합하지 않습니다.

Therefore we introduce the following architecture for the proposed system in Figure 4.1:
따라서 그림 4.1에서 제안하는 시스템에 대해 다음 아키텍처를 소개합니다.

![Korean Sentence Complexity Reduction Architecture(korean).png](img/Korean Sentence Complexity Reduction Architecture(korean).png)

Using this architecture, we take a Korean input sentence and insert it into our system. In the first stage we perform the necessary analysis such as using POS tags to parse the sentence, identify the sentence type (question, statement, etc) determine what simplifications, if any, to perform, and finally make note of which factorial permutations are possible in the sentence, as described in section 4.2. Based on our findings during analysis, the system determines which rules to apply and does so based on the rules described in section 4.1. The newly generated sentences are then brought to the final stage where we establish a cohesive logic by the insertion of sentence connectors, move anaphors, such as topics if necessary, into their appropriate positions.
이 아키텍처를 사용하여 한국어 입력 문장을 가져와 시스템에 삽입합니다.
첫 번째 단계에서 우리는 POS 태그를 사용하여 문장을 구문 분석하고, 문장 유형(질문, 진술 등)을 식별하는 것과 같은 필요한 분석을 수행합니다.
어떤 단순화를 수행할지 결정하고, 마지막으로 어떤 계승 순열이 가능한지 기록합니다. 섹션 4.2에 설명된 대로 문장에서.
분석 중 발견한 사항을 기반으로 시스템은 적용할 규칙을 결정하고 섹션 4.1에 설명된 규칙에 따라 적용합니다.
새로 생성된 문장은 문장 연결자를 삽입하여 응집력 있는 논리를 설정하고 필요한 경우 주제와 같은 아나포어를 적절한 위치로 이동하는 최종 단계로 이동합니다.

In the final stage we also match the formality between sentences generated by the proposed system. As was mentioned in Chapter 3, the SC is a corpus of spoken Korean, therefore, all registers of Korean formality and honorifics are present in the corpus. In order to generate Korean sentences that sound as natural as possible, we thought it necessary to maintain the formality of the original Korean sentence in our reduced sentences. This was accomplished by making lists of all possible formality endings in the corpus, noting the original sentence's formality and type, then simply inserting the appropriate ending before the sentence ending punctuation at the simplification site. Though not a necessary step for Korean to English MT, as English has no equivalent formality registers, this, we believe, is an imperative step for any Korean syntactic TS system attempting to produce natural output.
마지막 단계에서는 제안된 시스템에서 생성된 문장 간의 형식도 일치시킵니다.
3장에서 언급했듯이 SC는 구어체의 말뭉치이므로 한국어의 격식과 존칭의 모든 레지스터가 말뭉치에 존재한다.
최대한 자연스럽게 들리는 한국어 문장을 생성하기 위해서는 축약된 문장에서 원래 한국어 문장의 형식을 유지할 필요가 있다고 생각했습니다.
이것은 말뭉치에서 가능한 모든 형식 어미의 목록을 만들고 원래 문장의 형식과 유형을 확인한 다음 단순화 사이트에서 문장 끝 구두점 앞에 적절한 어미를 삽입하기만 하면 됩니다.
한국어에서 영어로 MT에 필요한 단계는 아니지만 영어에는 이에 상응하는 형식 레지스터가 없기 때문에 자연스러운 출력을 생성하려는 한국어 구문 TS 시스템의 필수 단계라고 생각합니다.

After the final regeneration stage, the reduced Korean sentences are returned to the initial stage and the process begins anew, in this way simplifying and generating factorial permutations recursively. Should no simplification be possible, the reduced Korean sentences are inserted into an MT system, and then converted into the target language. Though the focus of the current research is Korean to English translation, we believe this system should be able to improve translation output for any MT project where the source language is Korean.
최종 재생성 단계 이후에는 축약된 한국어 문장을 초기 단계로 되돌리고 프로세스를 새로 시작하여 재귀적으로 계승 순열을 단순화하고 생성합니다.
단순화가 불가능한 경우 축소된 한국어 문장을 MT 시스템에 삽입한 후 대상 언어로 변환합니다.
현재 연구의 초점은 한국어에서 영어로의 번역이지만, 우리는 이 시스템이 소스 언어가 한국어인 모든 MT 프로젝트의 번역 출력을 향상시킬 수 있을 것이라고 믿습니다.

