# Complex Word Identification as a Sequence Labelling Task
# 시퀀스 라벨링 작업으로 복잡한 단어 식별



## Abstract

Complex Word Identification (CWI) is concerned with detection of words in need of simplification and is a crucial first step in a simplification pipeline. It has been shown that reliable CWI systems considerably  mprove text simplification. However, most CWI systems to date address the task on a word-by-word basis, not taking the context into account. In this paper, we present a novel approach to CWI based on sequence modelling. Our system is capable of performing CWI in context, does not require extensive feature engineering and outperforms state-of-the-art systems on this task.
복잡한 단어 식별(CWI)은 단순화가 필요한 단어의 감지와 관련이 있으며 단순화 파이프라인의 중요한 첫 번째 단계입니다. 신뢰할 수 있는 CWI 시스템은 텍스트 단순화를 상당히 향상시키는 것으로 나타났습니다. 그러나 현재까지 대부분의 CWI 시스템은 문맥을 고려하지 않고 단어 단위로 작업을 처리합니다. 이 논문에서는 시퀀스 모델링을 기반으로 하는 CWI에 대한 새로운 접근 방식을 제시합니다. 우리 시스템은 상황에 따라 CWI를 수행할 수 있으며 광범위한 기능 엔지니어링이 필요하지 않으며 이 작업에서 최첨단 시스템보다 성능이 뛰어납니다.



## 1. Introduction

Lexical complexity is one of the main aspects contributing to overall text complexity (Dubay, 2004). It is typically addressed with lexical simplification (LS) systems that aim to paraphrase and substitute complex terms for simpler alternatives. Previous research has shown that Complex Word Identification (CWI) considerably improves lexical simplification (Shardlow, 2014; Paetzold and Specia, 2016a). This is achieved by identifying complex terms in text prior to word substitution. The performance of a CWI component is crucial, as low recall of this component might result in an overly difficult text with many missed complex words, while low precision might result in meaning distortions with an LS system trying to unnecessarily simplify non-complex words (Shardlow, 2013).
어휘 복잡성은 전체 텍스트 복잡성에 기여하는 주요 측면 중 하나입니다(Dubay, 2004). 이것은 일반적으로 더 간단한 대안을 복잡한 용어로 바꾸고 대체하는 것을 목표로 하는 어휘 단순화(LS) 시스템으로 해결됩니다. 이전 연구에서는 복잡한 단어 식별(CWI)이 어휘 단순화를 상당히 향상시키는 것으로 나타났습니다(Shardlow, 2014; Paetzold and Specia, 2016a). 이것은 단어를 대체하기 전에 텍스트에서 복잡한 용어를 식별함으로써 달성됩니다. CWI 구성요소의 성능은 매우 중요합니다. 이 구성요소의 낮은 재현율은 많은 복잡한 단어를 놓친 지나치게 어려운 텍스트를 초래할 수 있는 반면, 낮은 정밀도는 LS 시스템이 복잡하지 않은 단어를 불필요하게 단순화하려는 의미 왜곡을 초래할 수 있기 때문입니다(Shardlow , 2013).



CWI has recently attracted attention as a standalone application, with at least two shared tasks focusing on it. Current approaches to CWI, including state-of-the-art systems, have a number of limitations. First of all, CWI systems typically address this task on a word-by-word basis, using a large number of features to capture the complexity of a word. For instance, the CWI system by Paetzold and Specia (2016c) uses a total of 69 features, while the one by Gooding and Kochmar (2018) uses 27 features. Secondly, systems performing CWI in a static manner are unable to take the context into account, thus failing to predict word complexity for polysemous words as well as words in various metaphorical or novel contexts. For instance, consider the following two contexts of the word molar from the CWI 2018 shared task (Yimam et al., 2018). Molar has been annotated as complex in the first context (resulting in the binary annotation of 1) by 17 out of 20 annotators (thus, the “probabilistic” label of 0.85), and as non-complex (label 0) in the second context:
CWI는 최근 두 가지 이상의 공유 작업에 초점을 맞춘 독립 실행형 애플리케이션으로 주목받고 있습니다. 최신 시스템을 포함한 CWI에 대한 현재 접근 방식에는 여러 가지 제한 사항이 있습니다. 우선, CWI 시스템은 일반적으로 단어의 복잡성을 캡처하기 위해 많은 기능을 사용하여 단어별로 이 작업을 처리합니다. 예를 들어 Paetzold and Specia(2016c)의 CWI 시스템은 총 69개의 기능을 사용하는 반면 Gooding과 Kochmar(2018)의 시스템은 27개의 기능을 사용합니다. 둘째, 정적 방식으로 CWI를 수행하는 시스템은 컨텍스트를 고려할 수 없으므로 다의어 단어 및 다양한 은유적이거나 새로운 컨텍스트의 단어에 대한 단어 복잡성을 예측하지 못합니다. 예를 들어, CWI 2018 공유 작업(Yimam et al., 2018)에서 molar라는 단어의 다음 두 컨텍스트를 고려하십시오. Molar는 첫 번째 컨텍스트에서 20개 주석 중 17개(따라서 "probabilistic" 레이블 0.85)에 의해 복잡한 것으로 주석이 달렸고(이진 주석이 1이 됨) 두 번째 컨텍스트:


|Contexts|Bin|Prob|
|:---|:---:|:---:|
|Elephants have four molars...|1|0.85|
|... new molars emerge in the back of the mouth.|0|0.00|


The annotators may have found the second context simpler on the whole, as molars is surrounded by familiar words that imply the meaning (e.g., mouth), whereas elephants is a rarer and less semantically similar co-occurrence. Such contextrelated effects are hard to capture with a CWI system that only takes word-level features into account. Thirdly, CWI systems that only look at individual words cannot grasp complexity above the word level, for example, when a whole phrase is considered complex.
어금니는 의미를 암시하는 친숙한 단어(예: 입)로 둘러싸여 있는 반면, 코끼리는 더 드물고 의미적으로 덜 유사한 동시 발생이기 때문에 주석가는 두 번째 컨텍스트가 전체적으로 더 단순하다는 것을 발견했을 수 있습니다. 이러한 컨텍스트 관련 효과는 단어 수준 기능만 고려하는 CWI 시스템으로 포착하기 어렵습니다. 셋째, 개별 단어만 보는 CWI 시스템은 전체 구문이 복잡한 것으로 간주되는 경우와 같이 단어 수준 이상의 복잡성을 파악할 수 없습니다.



In this paper, we apply a novel approach to the CWI, based on sequence labelling. We show that our system is capable of:
- taking word context into account;
- relying on word embeddings only, thus eliminating the need for extensive feature engineering; detecting both complex words and phrases;
- not requiring genre-specific training and representing a one-model-fits-all approach.
이 백서에서는 시퀀스 라벨링을 기반으로 CWI에 새로운 접근 방식을 적용합니다. 우리 시스템이 다음을 수행할 수 있음을 보여줍니다.
- 단어 문맥을 고려하는 것
- 단어 임베딩에만 의존하므로 광범위한 기능 엔지니어링이 필요하지 않습니다. 복잡한 단어와 구를 모두 감지합니다.
- 장르별 학습이 필요하지 않으며 만능 모델 접근 방식을 나타냅니다.



## 2. Related Work
## 2. 관련 사항


### 2-1. ComplexWord Identification
### 2-1. 복잡한 단어 식별



Early studies on CWI address this task by either attempting to simplify all words (Thomas and Anderson, 2012; Bott et al., 2012) or setting a frequency-based threshold (Zeng et al., 2005; Elhadad, 2006; Biran et al., 2011). Horn et al. (2014) show that the former approach may miss up to one third of complex words due to its inability to find simpler alternatives, and Shardlow (2013) argues that a simplify-all approach might result in meaning distortions, but the more resource-intensive threshold-based approach does not necessarily perform significantly better either. At the same time, Shardlow (2013) shows that a classification-based approach to CWI is the most promising one. Most of the teams participating in the recent CWI shared tasks also use classification approaches with extensive feature engineering.
CWI에 대한 초기 연구에서는 모든 단어를 단순화하려고 시도하거나(Thomas and Anderson, 2012; Bott et al., 2012) 빈도 기반 임계값을 설정하여(Zeng et al., 2005; Elhadad, 2006; Biran et al.) 이 작업을 해결합니다. ., 2011). Horn et al. (2014) 전자의 접근 방식은 더 간단한 대안을 찾을 수 없기 때문에 복잡한 단어의 최대 3분의 1을 놓칠 수 있음을 보여주고 Shardlow(2013)는 모든 단순화 접근 방식이 의미 왜곡을 초래할 수 있지만 리소스 집약적이라고 주장합니다. 임계값 기반 접근 방식이 반드시 훨씬 더 나은 성능을 보이는 것은 아닙니다. 동시에 Shardlow(2013)는 CWI에 대한 분류 기반 접근 방식이 가장 유망한 방법임을 보여줍니다. 최근 CWI 공유 작업에 참여하는 대부분의 팀은 또한 광범위한 기능 엔지니어링과 함께 분류 접근 방식을 사용합니다.



The first shared task on CWI at SemEval 2016 (Paetzold and Specia, 2016b) used data from several simplification datasets, annotated by non-native speakers. In this data, about 3% of word types and 11% of word tokens, if contexts are taken into account, are annotated as complex (Paetzold and Specia, 2016b). The CWI 2018 shared task (Yimam et al., 2018) used the data from Wikipedia, news sources and unprofessionally written news, derived from the dataset of Yimam et al. (2017). The dataset was annotated by 10 native and 10 non-native speakers, and, depending on the source of the data, contains 40% to 50% words labelled as complex in context. The dataset contains words and phrases with two labels each. The first label represents binary judgement with bin=1 if at least 1 annotator marked the word as complex in context, and bin=0 otherwise. The second label is a “probabilistic” label representing the proportion of the 20 annotators that labelled the item as complex. The importance of context when considering word complexity is exemplified well in this dataset, as 11.34% of items have different binary labels depending on the context they are used in. When considering probabilistic annotations, of the items labelled in different contexts 10.96% have at least a 5-annotator difference in complexity score in differing contexts. The dataset contains 104 instances with a 10-annotator difference between scores based on the context of the word. For instance, suspicion has been annotated 23 times:
SemEval 2016(Paetzold and Specia, 2016b)에서 CWI에 대한 첫 번째 공유 작업은 비원어민이 주석을 추가한 여러 단순화 데이터 세트의 데이터를 사용했습니다. 이 데이터에서 컨텍스트를 고려하면 단어 유형의 약 3%와 단어 토큰의 11%가 복합 주석으로 표시됩니다(Paetzold and Specia, 2016b). CWI 2018 공유 작업(Yimam et al., 2018)은 Yimam et al.의 데이터 세트에서 파생된 Wikipedia, 뉴스 소스 및 비전문적으로 작성된 뉴스의 데이터를 사용했습니다. (2017). 데이터 세트는 10명의 원어민과 10명의 비원어민이 주석을 달았으며, 데이터 출처에 따라 문맥상 복잡한 것으로 표시된 단어가 40~50% 포함되어 있습니다. 데이터 세트에는 각각 두 개의 레이블이 있는 단어와 구문이 포함되어 있습니다. 첫 번째 레이블은 적어도 1명의 주석자가 단어를 문맥에서 복잡한 것으로 표시한 경우 bin=1이고 그렇지 않은 경우 bin=0인 이진 판단을 나타냅니다. 두 번째 레이블은 항목에 복잡한 레이블을 지정한 20명의 주석자의 비율을 나타내는 "확률적" 레이블입니다. 단어 복잡성을 고려할 때 컨텍스트의 중요성은 이 데이터 세트에서 잘 예시됩니다. 항목의 11.34%는 사용되는 컨텍스트에 따라 다른 이진 레이블을 갖습니다. 확률적 주석을 고려할 때 다른 컨텍스트에서 레이블이 지정된 항목 중 10.96%는 다른 컨텍스트에서 복잡성 점수에서 최소 5개의 주석 차이가 있습니다. 데이터 세트에는 단어의 컨텍스트를 기반으로 하는 점수 간에 10개의 주석 차이가 있는 104개의 인스턴스가 포함되어 있습니다. 예를 들어, suspicion은 23번 주석이 달렸습니다.


|Word|Unique|Max|Min|σ|
|---|---|---|---|---|
|suspicion|16|0.95|0.15|0.25|


Of the 23 probabilistic annotations for suspicion 70% are unique. Max and min values show the largest difference in annotations for this word in context, with 19 annotators labelling it complex in one scenario and only 3 in another. Finally, σ represents the standard deviation of the probabilistic annotations for this word.
suspicion에 대한 23개의 확률적 주석 중 70%가 고유합니다. 최대값과 최소값은 컨텍스트에서 이 단어에 대한 주석의 가장 큰 차이를 보여줍니다. 한 시나리오에서는 19개의 주석이 복합 레이블을 지정하고 다른 시나리오에서는 3개만 레이블을 지정합니다. 마지막으로 σ는 이 단어에 대한 확률적 주석의 표준 편차를 나타냅니다.



In this paper, we use the data from the CWI 2018 shared task, which contains annotation for both words and word sequences (called phrases in the task), and represents three different genres of text. We focus on the binary setting (complex vs. non-complex) and compare our results to the winning system by Gooding and Kochmar (2018).
이 백서에서는 단어와 단어 시퀀스(작업에서 구문이라고 함) 모두에 대한 주석을 포함하고 세 가지 다른 장르의 텍스트를 나타내는 CWI 2018 공유 작업의 데이터를 사용합니다. 우리는 이진 설정(복잡한 대 비복합)에 초점을 맞추고 결과를 Gooding과 Kochmar(2018)의 우승 시스템과 비교합니다.



## 2-2. Sequence Labelling
## 2-2. 시퀀스 라벨링



Sequence labelling has been applied successfully to a number of NLP tasks that rely on contextual information, such as named entity recognition, part-of-speech tagging and shallow parsing. Within this framework, the model receives as input a sequence of tokens (w1, …, wT ) and predicts a label for each token as output. Typically, the input tokens are first mapped to a distributed vector space, resulting in a sequence of word embeddings (x1, …, xT ). The use of word embeddings allows sequence models to learn similar representations for semantically or functionally similar words. Recent advances to sequential model frameworks have resulted in the models’ ability to infer representations for previously unseen words and to share information abouabout morpheme-level regularities (Rei et al., 2016).
시퀀스 레이블링은 명명된 엔터티 인식, 품사 태깅 및 얕은 구문 분석과 같은 컨텍스트 정보에 의존하는 여러 NLP 작업에 성공적으로 적용되었습니다. 이 프레임워크 내에서 모델은 일련의 토큰(w1, …, wT)을 입력으로 받고 각 토큰에 대한 레이블을 출력으로 예측합니다. 일반적으로 입력 토큰은 먼저 분산 벡터 공간에 매핑되어 일련의 단어 임베딩(x1, …, xT)이 생성됩니다. 단어 임베딩을 사용하면 시퀀스 모델이 의미상 또는 기능적으로 유사한 단어에 대해 유사한 표현을 학습할 수 있습니다. 최근 순차 모델 프레임워크의 발전으로 인해 이전에 볼 수 없었던 단어에 대한 표현을 추론하고 형태소 수준의 규칙성에 대한 정보를 공유할 수 있는 모델의 능력이 생겼습니다(Rei et al., 2016).



Sequence labelling models benefit from the use of long short-term memory (LSTM) units (Gers et al., 2000), as these units can capture the long-term contextual dependencies in natural language. A variation of the traditional architecture, bi-directional LSTMs (BiLSTM) (Hochreiter and Schmidhuber, 1997), has proved highly successful at language tasks, as it is able to consider both the left and right contexts of a word, thus increasing the amount of relevant information available to the network. Similarly, the use of secondary learning objectives can increase the number of salient features and access to relevant information. For example, Rei (2017) shows that training a model to jointly predict surrounding words incentivises the discovery of useful features and associations that are unlikely to be discovered otherwise.
시퀀스 라벨링 모델은 LSTM(장단기 기억) 단위를 사용하는 이점이 있습니다(Gers et al., 2000). 이러한 단위는 자연어에서 장기 컨텍스트 종속성을 캡처할 수 있기 때문입니다. 전통적인 아키텍처의 변형인 양방향 LSTM(BiLSTM)(Hochreiter 및 Schmidhuber, 1997)은 단어의 왼쪽 및 오른쪽 컨텍스트를 모두 고려할 수 있으므로 언어 작업에서 매우 성공적임이 입증되어 양을 증가시킵니다. 네트워크에서 사용할 수 있는 관련 정보. 유사하게, 2차 학습 목표의 사용은 두드러진 특징의 수와 관련 정보에 대한 접근을 증가시킬 수 있습니다. 예를 들어, Rei(2017)는 주변 단어를 공동으로 예측하도록 모델을 훈련하는 것이 다른 방법으로는 발견되지 않을 유용한 기능 및 연관성의 발견을 장려한다는 것을 보여줍니다.



From the perspective of CWI, it is clear that context greatly impacts the perceived difficulty of text. In this paper we investigate whether CWI can be framed as a sequence labelling task.
CWI의 관점에서 볼 때 문맥이 텍스트의 인지된 난이도에 큰 영향을 미친다는 것은 분명합니다. 이 논문에서 우리는 CWI가 시퀀스 라벨링 작업으로 프레임될 수 있는지 조사합니다.



## 3. Implementation
## 3. 구현



For our experiments, we use the English part of the CWI datasets from Yimam et al. (2017), which contains texts on professionally written NEWS, amateurishly written WIKINEWS, and WIKIPEDIA articles. The original data includes the annotation for a selected set of content words, which is provided alongside the full sentence and the word span. The annotation contains both binary (bin) and “probabilistic” (prob) labels as detailed in Section 2:
실험을 위해 Yimam et al.의 CWI 데이터 세트의 영어 부분을 사용합니다. (2017), 전문적으로 작성된 NEWS, 아마추어적으로 작성된 WIKINEWS 및 WIKIPEDIA 기사에 대한 텍스트가 포함되어 있습니다. 원본 데이터에는 전체 문장 및 단어 범위와 함께 제공되는 선택된 콘텐츠 단어 세트에 대한 주석이 포함됩니다. 주석에는 섹션 2에 설명된 대로 이진(bin) 및 "확률"(prob) 레이블이 모두 포함됩니다.


|Sentence|Word|Bin|Prob|
|---|---|---|---|
|They drastically...|drastically|1|0.5|



As the sequential model expects the complete word context as an input, we adapt the original format by tokenizing the sentences and including the annotation for each word token, using C for the annotated complex words and phrases, and N for those that are either annotated as non-complex in the original data or not included in it (e.g., function words), which results in the following format:
순차 모델은 완전한 단어 컨텍스트를 입력으로 예상하므로 문장을 토큰화하고 각 단어 토큰에 대한 주석을 포함하여 원래 형식을 적용합니다. 주석이 달린 복잡한 단어와 구에는 C를 사용하고 원본 데이터에 복잡하지 않거나 포함되지 않은(예: 기능어), 결과적으로 다음 형식:


They N
drastically C
...


We opted to use a sequential architecture by Rei (2017), as it has achieved state-of-the-art results on a number of NLP tasks, including error detection, which is similar to CWI in that it identifies relatively rare sequences of words in context. The design of this architecture is highly suited to the task of CWI as: (1) the use of a BiLSTM provides contextual information from both the left and right context of a target word; (2) the context is combined with both word and characterlevel representations (Rei et al., 2016); (3) this architecture uses a language modelling objective, which enables the model to learn better composition functions and to predict the probability of individual words in context. As previous work on CWI has consistently found word frequency and length to be highly informative features, we choose an architecture which utilises sub-word information and a language modelling objective.
우리는 Rei(2017)의 순차 아키텍처를 사용하기로 선택했는데, 이는 비교적 드문 단어 시퀀스를 식별한다는 점에서 CWI와 유사한 오류 감지를 포함하여 여러 NLP 작업에서 최신 결과를 얻었기 때문입니다. 문맥. 이 아키텍처의 디자인은 다음과 같이 CWI의 작업에 매우 적합합니다. (1) BiLSTM의 사용은 대상 단어의 왼쪽 및 오른쪽 컨텍스트 모두에서 컨텍스트 정보를 제공합니다. (2) 문맥이 단어 및 문자 수준 표현과 결합됩니다(Rei et al., 2016). (3) 이 아키텍처는 모델이 더 나은 구성 기능을 학습하고 컨텍스트에서 개별 단어의 확률을 예측할 수 있도록 하는 언어 모델링 목표를 사용합니다. CWI에 대한 이전 작업은 단어 빈도와 길이가 매우 유익한 기능이라는 것을 일관되게 발견했기 때문에 하위 단어 정보와 언어 모델링 목표를 활용하는 아키텍처를 선택합니다.



We use 300-dimensional GloVe embeddings as word representations (Pennington et al., 2014) and train the model on randomly shuffled texts from all three genres for 20 iterations. We train the model using word annotations and predict binary word scores using the output label probabilities. If the probability of a word belonging to the complex class is above 0.50, it is considered a complex word. For phrase-level binary prediction, we consider the phrases contained within the dataset. The complex class probability for each word, aside from stop words, is predicted and combined into a final average score. If this average is above a predefined threshold of 0.50 then the phrase is considered complex.
우리는 300차원 GloVe 임베딩을 단어 표현으로 사용하고(Pennington et al., 2014) 20회 반복 동안 세 장르 모두에서 무작위로 섞인 텍스트에 대해 모델을 훈련합니다. 단어 주석을 사용하여 모델을 훈련하고 출력 레이블 확률을 사용하여 이진 단어 점수를 예측합니다. 복합 클래스에 속하는 단어의 확률이 0.50 이상인 경우 복합 단어로 간주됩니다. 구문 수준 이진 예측의 경우 데이터 세트에 포함된 구문을 고려합니다. 불용어를 제외하고 각 단어에 대한 복합 클래스 확률이 예측되고 최종 평균 점수로 결합됩니다. 이 평균이 미리 정의된 임계값인 0.50을 초과하면 구문이 복잡한 것으로 간주됩니다.



## 4. Results & Discussion
## 4. 결과 & 토의


Results: We report the results obtained with the sequence labelling (SEQ) model for the binary task and compare them to the current state-of-the-art in complex word identification, CAMB system by Gooding and Kochmar (2018), which achieved the best results across all binary and two probabilistic tracks in the CWI 2018 shared task (Yimam et al., 2018). The evaluation metric reported is the macro-averaged F1, as was used in the 2018 CWI shared task (Yimam et al., 2018). For the binary task, both words and phrases are considered correct if the system outputs the correct binary label.
결과: 우리는 바이너리 작업에 대한 시퀀스 라벨링(SEQ) 모델로 얻은 결과를 보고하고 이를 Gooding and Kochmar(2018)의 복잡한 단어 식별, CAMB 시스템의 최신 기술과 비교합니다. CWI 2018 공유 작업(Yimam et al., 2018)의 모든 바이너리 및 2개의 확률 트랙에서 최상의 결과를 얻었습니다. 보고된 평가 지표는 2018 CWI 공유 작업(Yimam et al., 2018)에서 사용된 매크로 평균 F1입니다. 이진 작업의 경우 시스템이 올바른 이진 레이블을 출력하면 단어와 구 모두 올바른 것으로 간주됩니다.



The CAMB system considers words irrespective of their context and relies on 27 features of various types, encoding lexical, syntactic, frequencybased and other types of information about individual words. The system uses Random Forests and AdaBoost for classification, but as Gooding and Kochmar (2018) report, the choice of the features, algorithm and training data depends on the genre. In addition, phrase classification is performed using a ‘greedy’ approach and simply labelling all phrases as complex.
CAMB 시스템은 문맥에 관계없이 단어를 고려하고 개별 단어에 대한 어휘, 구문, 빈도 기반 및 기타 유형의 정보를 인코딩하는 다양한 유형의 27가지 기능에 의존합니다. 시스템은 분류를 위해 Random Forests와 AdaBoost를 사용하지만 Gooding and Kochmar(2018) 보고서에 따르면 기능, 알고리즘 및 교육 데이터의 선택은 장르에 따라 다릅니다. 또한 구문 분류는 '탐욕스러운' 접근 방식을 사용하여 모든 구문을 복잡한 것으로 표시하기만 하면 수행됩니다.