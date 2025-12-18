---
layout: default
title: On the Alignment of Large Language Models with Global Human Opinion
---

# On the Alignment of Large Language Models with Global Human Opinion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01418" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01418v2</a>
  <a href="https://arxiv.org/pdf/2509.01418.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01418v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01418v2', 'On the Alignment of Large Language Models with Global Human Opinion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Liu, Masahiro Kaneko, Chenhui Chu

**分类**: cs.CL

**发布日期**: 2025-09-01 (更新: 2025-11-19)

**备注**: 28 pages, 26 figures

**🔗 代码/项目**: [GITHUB](https://github.com/ku-nlp/global-opinion-alignment) | [GITHUB](https://github.com/nlply/global-opinion-alignment)

---

## 💡 一句话要点

**提出基于世界价值观调查的框架，评估大语言模型与全球人类意见的对齐程度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `意见对齐` `世界价值观调查` `多语言` `跨文化` `提示工程` `价值观评估`

## 📋 核心要点

1. 现有研究缺乏对大语言模型在全球范围内与不同国家、历史时期人类意见对齐程度的系统评估。
2. 论文提出一个基于世界价值观调查(WVS)的评估框架，用于评估LLMs在不同国家、语言和历史时期与人类意见的对齐情况。
3. 实验表明，LLMs在意见对齐方面存在偏差，且提示语言的选择能够有效引导LLMs与特定国家或时期的意见对齐。

## 📝 摘要（中文）

当前的大语言模型(LLMs)能够支持多语言场景，允许用户以母语与LLMs交互。当LLMs回答用户提出的主观问题时，它们应该与特定人口群体或历史时期的观点保持一致，而这些观点受到用户与模型交互所用语言的影响。现有的研究主要集中于研究LLMs在美国或少数几个国家的人口群体中所代表的观点，缺乏全球范围内的国家样本以及对不同历史时期人类意见的研究，也缺乏关于使用语言来引导LLMs的讨论。此外，他们也忽略了提示语言对LLMs意见对齐的潜在影响。在本研究中，我们的目标是填补这些空白。为此，我们创建了一个基于世界价值观调查(WVS)的评估框架，以系统地评估LLMs与全球不同国家、语言和历史时期的人类意见的对齐程度。我们发现LLMs仅与少数几个国家的意见适当或过度对齐，而与大多数国家的意见对齐不足。此外，将提示的语言更改为与问卷中使用的语言相匹配，可以比现有的引导方法更有效地引导LLMs与相应国家的意见对齐。同时，LLMs更倾向于与当代人口的意见对齐。据我们所知，我们的研究是首次对LLMs中跨全球、语言和时间维度进行意见对齐的全面调查。我们的代码和数据可在https://github.com/ku-nlp/global-opinion-alignment和https://github.com/nlply/global-opinion-alignment公开获取。

## 🔬 方法详解

**问题定义**：现有研究主要关注LLMs在美国等少数国家的人群意见对齐，缺乏全球视角和历史维度的考察。同时，忽略了prompt语言对LLMs意见的影响，导致无法有效评估和控制LLMs的意见倾向。

**核心思路**：论文的核心思路是利用世界价值观调查（WVS）提供的多国、多语言、多时期的社会价值观数据，构建一个评估LLMs意见对齐的框架。通过改变prompt的语言，引导LLMs与特定国家或历史时期的价值观对齐。

**技术框架**：该研究的技术框架主要包含以下几个阶段：1) 数据收集：从世界价值观调查（WVS）中获取不同国家、语言和历史时期的社会价值观数据。2) Prompt构建：设计不同语言的prompt，用于引导LLMs回答与WVS相关的问题。3) LLM推理：使用不同的LLMs对构建的prompt进行推理，获取LLMs的回答。4) 对齐评估：将LLMs的回答与WVS数据进行比较，评估LLMs与不同国家、语言和历史时期人类意见的对齐程度。

**关键创新**：该研究的关键创新在于：1) 首次构建了一个基于WVS的全球范围内的LLMs意见对齐评估框架。2) 揭示了prompt语言对LLMs意见对齐的重要影响，并提出了一种基于语言的引导方法。3) 发现了LLMs在意见对齐方面存在的偏差，例如对某些国家过度对齐，对另一些国家对齐不足。

**关键设计**：研究的关键设计包括：1) WVS数据的选择和处理，确保数据的代表性和可靠性。2) Prompt的设计，需要保证prompt能够有效地引导LLMs回答与WVS相关的问题，并且能够控制prompt的语言。3) 对齐评估指标的选择，需要选择合适的指标来衡量LLMs与人类意见的对齐程度。

## 📊 实验亮点

实验结果表明，LLMs在意见对齐方面存在显著偏差，仅与少数国家适当对齐，而与大多数国家对齐不足。通过改变prompt的语言，可以有效引导LLMs与特定国家的意见对齐，效果优于现有方法。同时，LLMs更倾向于与当代人口的意见对齐，表明其可能受到训练数据的影响。

## 🎯 应用场景

该研究成果可应用于提升大语言模型在多语言、跨文化场景下的应用效果，例如，在国际交流、文化传播、跨国合作等领域，可以利用该研究成果引导LLMs生成更符合当地文化价值观的内容，避免文化冲突和误解。此外，该研究也有助于提高LLMs的公平性和可信度，减少其在不同人群中产生偏见。

## 📄 摘要（原文）

> Today's large language models (LLMs) are capable of supporting multilingual scenarios, allowing users to interact with LLMs in their native languages. When LLMs respond to subjective questions posed by users, they are expected to align with the views of specific demographic groups or historical periods, shaped by the language in which the user interacts with the model. Existing studies mainly focus on researching the opinions represented by LLMs among demographic groups in the United States or a few countries, lacking worldwide country samples and studies on human opinions in different historical periods, as well as lacking discussion on using language to steer LLMs. Moreover, they also overlook the potential influence of prompt language on the alignment of LLMs' opinions. In this study, our goal is to fill these gaps. To this end, we create an evaluation framework based on the World Values Survey (WVS) to systematically assess the alignment of LLMs with human opinions across different countries, languages, and historical periods around the world. We find that LLMs appropriately or over-align the opinions with only a few countries while under-aligning the opinions with most countries. Furthermore, changing the language of the prompt to match the language used in the questionnaire can effectively steer LLMs to align with the opinions of the corresponding country more effectively than existing steering methods. At the same time, LLMs are more aligned with the opinions of the contemporary population. To our knowledge, our study is the first comprehensive investigation of the topic of opinion alignment in LLMs across global, language, and temporal dimensions. Our code and data are publicly available at https://github.com/ku-nlp/global-opinion-alignment and https://github.com/nlply/global-opinion-alignment.

