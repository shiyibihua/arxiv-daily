---
layout: default
title: Identifying Features Associated with Bias Against 93 Stigmatized Groups in Language Models and Guardrail Model Safety Mitigation
---

# Identifying Features Associated with Bias Against 93 Stigmatized Groups in Language Models and Guardrail Model Safety Mitigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19238" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19238v1</a>
  <a href="https://arxiv.org/pdf/2512.19238.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19238v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19238v1', 'Identifying Features Associated with Bias Against 93 Stigmatized Groups in Language Models and Guardrail Model Safety Mitigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anna-Maria Gueorguieva, Aylin Caliskan

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**研究揭示LLM中针对污名化群体的偏见特征，并评估Guardrail模型缓解效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `社会偏见` `污名化群体` `Guardrail模型` `偏见缓解` `社会特征` `风险评估`

## 📋 核心要点

1. 现有研究对LLM中针对污名化群体的偏见关注不足，且缺乏对污名社会特征与偏见关联的深入理解。
2. 该研究通过分析污名的六个社会特征（美学、可隐藏性等）与LLM偏见输出之间的关系，揭示了危险性特征与偏见程度的正相关性。
3. 实验表明，Guardrail模型能一定程度缓解偏见，但对高危险性污名的偏见缓解效果有限，且难以识别提示中的偏见意图。

## 📝 摘要（中文）

大型语言模型(LLM)已显示出社会偏见，但针对非受保护的污名化身份的偏见仍未得到充分研究。此外，污名的哪些社会特征与LLM输出中的偏见相关仍然未知。心理学文献表明，污名包含六个共同的社会特征：美学、可隐藏性、过程、破坏性、起源和危险性。本研究调查了人类和LLM对污名特征的评分，以及提示风格和污名类型，是否会对LLM输出中针对污名化群体的偏见产生影响。我们使用SocialStigmaQA（一个包含37个关于污名化身份的社会场景的基准，例如决定是否推荐他们参加实习）来衡量三种广泛使用的LLM（Granite 3.0-8B、Llama-3.1-8B、Mistral-7B）中针对93个污名化群体的偏见。我们发现，人类评定为高度危险的污名（例如，成为帮派成员或感染艾滋病毒）在SocialStigmaQA提示中产生最多的偏见输出（来自所有模型的60%），而社会人口污名（例如，亚裔美国人或老年）产生的偏见输出最少（11%）。我们测试了使用guardrail模型（旨在识别有害输入的模型）是否可以减少偏见输出的数量，使用了每个LLM各自的guardrail模型（Granite Guardian 3.0、Llama Guard 3.0、Mistral Moderation API）。我们发现，偏见分别显著降低了10.4%、1.4%和7.8%。然而，我们表明，对偏见有显著影响的特征在缓解后仍然没有改变，并且guardrail模型通常无法识别提示中偏见的意图。这项工作对在涉及污名化群体的场景中使用LLM具有重要意义，我们建议未来的工作应致力于改进用于偏见缓解的guardrail模型。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型(LLM)中存在的、针对污名化群体的社会偏见问题。现有方法主要关注受保护群体的偏见，而对非受保护的污名化群体（如患有特定疾病、从事特定职业等）的偏见研究不足。此外，现有方法缺乏对污名本身特征与LLM偏见输出之间关联性的深入分析，难以有效缓解此类偏见。

**核心思路**：论文的核心思路是，从心理学角度出发，将污名分解为六个关键的社会特征（美学、可隐藏性、过程、破坏性、起源和危险性），并研究这些特征与LLM偏见输出之间的关系。通过量化这些特征，并结合不同的提示风格和污名类型，分析其对LLM偏见程度的影响。同时，评估Guardrail模型在缓解此类偏见方面的效果。

**技术框架**：整体框架包括以下几个主要步骤：1) 收集93个污名化群体的数据，并使用SocialStigmaQA基准测试LLM的偏见程度。2) 人工和LLM对污名的六个社会特征进行评分。3) 分析污名特征、提示风格和污名类型对LLM偏见输出的影响。4) 使用Guardrail模型（Granite Guardian 3.0、Llama Guard 3.0、Mistral Moderation API）对LLM进行偏见缓解。5) 评估Guardrail模型的缓解效果，并分析其局限性。

**关键创新**：论文最重要的技术创新点在于，首次将心理学中污名的社会特征引入到LLM偏见分析中，并揭示了“危险性”这一特征与LLM偏见程度的正相关关系。这为理解和缓解LLM中针对污名化群体的偏见提供了新的视角。与现有方法相比，该研究不仅关注偏见的存在，更深入地探究了偏见的根源。

**关键设计**：关键设计包括：1) 使用SocialStigmaQA基准，该基准包含37个关于污名化身份的社会场景，能够有效衡量LLM的偏见程度。2) 人工和LLM对污名的六个社会特征进行评分，为量化分析提供了数据基础。3) 使用三种不同的Guardrail模型，评估其在缓解偏见方面的效果，并分析其局限性。4) 采用统计分析方法，量化污名特征、提示风格和污名类型对LLM偏见输出的影响。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19238v1/report_images/fig_1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19238v1/report_images/fig_2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19238v1/report_images/fig_3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，LLM对被人类评定为高度危险的污名（如帮派成员、HIV感染者）的偏见输出最多（60%），而对社会人口污名（如亚裔美国人、老年人）的偏见输出最少（11%）。使用Guardrail模型后，偏见分别显著降低了10.4%（Granite Guardian 3.0）、1.4%（Llama Guard 3.0）和7.8%（Mistral Moderation API）。但对偏见有显著影响的特征在缓解后仍然没有改变，且Guardrail模型通常无法识别提示中偏见的意图。

## 🎯 应用场景

该研究成果可应用于开发更公平、更负责任的LLM系统，尤其是在涉及污名化群体的场景中，如医疗诊断、招聘筛选、法律咨询等。通过理解污名特征与偏见的关系，可以设计更有效的偏见缓解策略，并提高Guardrail模型的识别能力，从而减少LLM对弱势群体的歧视。未来的研究可以进一步探索其他社会因素对LLM偏见的影响，并开发更通用的偏见缓解方法。

## 📄 摘要（原文）

> Large language models (LLMs) have been shown to exhibit social bias, however, bias towards non-protected stigmatized identities remain understudied. Furthermore, what social features of stigmas are associated with bias in LLM outputs is unknown. From psychology literature, it has been shown that stigmas contain six shared social features: aesthetics, concealability, course, disruptiveness, origin, and peril. In this study, we investigate if human and LLM ratings of the features of stigmas, along with prompt style and type of stigma, have effect on bias towards stigmatized groups in LLM outputs. We measure bias against 93 stigmatized groups across three widely used LLMs (Granite 3.0-8B, Llama-3.1-8B, Mistral-7B) using SocialStigmaQA, a benchmark that includes 37 social scenarios about stigmatized identities; for example deciding wether to recommend them for an internship. We find that stigmas rated by humans to be highly perilous (e.g., being a gang member or having HIV) have the most biased outputs from SocialStigmaQA prompts (60% of outputs from all models) while sociodemographic stigmas (e.g. Asian-American or old age) have the least amount of biased outputs (11%). We test if the amount of biased outputs could be decreased by using guardrail models, models meant to identify harmful input, using each LLM's respective guardrail model (Granite Guardian 3.0, Llama Guard 3.0, Mistral Moderation API). We find that bias decreases significantly by 10.4%, 1.4%, and 7.8%, respectively. However, we show that features with significant effect on bias remain unchanged post-mitigation and that guardrail models often fail to recognize the intent of bias in prompts. This work has implications for using LLMs in scenarios involving stigmatized groups and we suggest future work towards improving guardrail models for bias mitigation.

