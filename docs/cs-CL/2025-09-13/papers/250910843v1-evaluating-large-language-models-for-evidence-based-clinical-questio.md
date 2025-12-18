---
layout: default
title: Evaluating Large Language Models for Evidence-Based Clinical Question Answering
---

# Evaluating Large Language Models for Evidence-Based Clinical Question Answering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10843" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10843v1</a>
  <a href="https://arxiv.org/pdf/2509.10843.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10843v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10843v1', 'Evaluating Large Language Models for Evidence-Based Clinical Question Answering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Can Wang, Yiqun Chen

**分类**: cs.CL

**发布日期**: 2025-09-13

---

## 💡 一句话要点

**评估大型语言模型在循证临床问答中的表现，并提出改进策略。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `临床问答` `循证医学` `检索增强提示` `证据推理`

## 📋 核心要点

1. 现有大型语言模型在临床问答中面临挑战，尤其是在需要证据支持的复杂问题上，准确性有待提高。
2. 论文提出利用检索增强提示，通过提供相关文献摘要来提升模型回答临床问题的准确性和对证据的依赖性。
3. 实验表明，提供黄金摘要能显著提升模型准确率，而语义相关的PubMed摘要也能带来提升，验证了检索增强的有效性。

## 📝 摘要（中文）

大型语言模型(LLMs)在生物医学和临床应用中取得了显著进展，因此需要对其回答细致的、基于证据的问题的能力进行严格评估。本文构建了一个多源基准，数据来自Cochrane系统评价和临床指南，包括美国心脏协会的结构化建议和保险公司使用的叙述性指导。使用GPT-4o-mini和GPT-5，观察到跨来源和临床领域的一致性能模式：在结构化指南建议上的准确率最高(90%)，在叙述性指南和系统评价问题上的准确率较低(60-70%)。还发现准确率与底层系统评价的引用次数之间存在很强的相关性，引用次数每增加一倍，正确答案的几率大约增加30%。模型在提供上下文信息时，显示出适度推理证据质量的能力。当结合检索增强提示时，提供黄金来源摘要可将先前不正确项目的准确率提高到0.79；提供前3个PubMed摘要(按语义相关性排序)可将准确率提高到0.23，而随机摘要会降低准确率(0.10)。这些影响在GPT-4o-mini中得到了体现，强调了来源清晰度和有针对性的检索，而不仅仅是模型大小，驱动了性能。总的来说，结果突出了LLM在循证临床问答中的希望和当前局限性。检索增强提示作为一种有用的策略出现，可以提高事实准确性和与来源证据的一致性，而按专业和问题类型分层评估仍然是理解当前知识获取和将模型性能置于上下文中必不可少的。

## 🔬 方法详解

**问题定义**：论文旨在评估大型语言模型在回答循证临床问题时的能力，并找出提升其准确性的方法。现有方法在处理需要证据支持的复杂临床问题时，准确率较低，且对证据的推理能力不足，容易产生幻觉。

**核心思路**：论文的核心思路是利用检索增强提示，即在向大型语言模型提问时，同时提供相关的证据来源（如文献摘要），以帮助模型更好地理解问题并给出准确的答案。这种方法旨在减少模型对自身知识的依赖，更多地依赖外部证据。

**技术框架**：整体流程包括：1) 构建包含结构化指南、叙述性指南和系统评价的多源基准数据集；2) 使用GPT-4o-mini和GPT-5等大型语言模型回答数据集中的问题；3) 评估模型在不同类型问题上的准确率；4) 引入检索增强提示，分别提供黄金来源摘要、语义相关的PubMed摘要和随机摘要；5) 比较不同提示策略下的模型性能，分析检索增强对准确率的影响。

**关键创新**：论文的关键创新在于系统性地评估了检索增强提示在循证临床问答中的作用，并验证了其有效性。与以往研究相比，该研究更关注如何利用外部证据来提升大型语言模型在特定领域的准确性和可靠性。

**关键设计**：论文的关键设计包括：1) 构建多源基准数据集，确保评估的全面性；2) 使用不同的检索策略（黄金摘要、语义相关摘要、随机摘要）来评估检索质量对模型性能的影响；3) 使用GPT-4o-mini和GPT-5等不同规模的模型，验证结论的泛化性；4) 分析引用次数与准确率之间的关系，探究证据质量对模型性能的影响。

## 📊 实验亮点

实验结果表明，在结构化指南建议上的准确率最高(90%)，在叙述性指南和系统评价问题上的准确率较低(60-70%)。提供黄金来源摘要可将先前不正确项目的准确率提高到0.79；提供前3个PubMed摘要(按语义相关性排序)可将准确率提高到0.23，而随机摘要会降低准确率(0.10)。引用次数每增加一倍，正确答案的几率大约增加30%。

## 🎯 应用场景

该研究成果可应用于智能临床决策支持系统，帮助医生快速获取高质量的循证医学证据，辅助诊断和治疗。通过提升大型语言模型在临床问答中的准确性和可靠性，可以减少医疗错误，提高医疗效率，并为患者提供更优质的医疗服务。未来，该技术有望应用于远程医疗、健康咨询等领域。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated substantial progress in biomedical and clinical applications, motivating rigorous evaluation of their ability to answer nuanced, evidence-based questions. We curate a multi-source benchmark drawing from Cochrane systematic reviews and clinical guidelines, including structured recommendations from the American Heart Association and narrative guidance used by insurers. Using GPT-4o-mini and GPT-5, we observe consistent performance patterns across sources and clinical domains: accuracy is highest on structured guideline recommendations (90%) and lower on narrative guideline and systematic review questions (60--70%). We also find a strong correlation between accuracy and the citation count of the underlying systematic reviews, where each doubling of citations is associated with roughly a 30% increase in the odds of a correct answer. Models show moderate ability to reason about evidence quality when contextual information is supplied. When we incorporate retrieval-augmented prompting, providing the gold-source abstract raises accuracy on previously incorrect items to 0.79; providing top 3 PubMed abstracts (ranked by semantic relevance) improves accuracy to 0.23, while random abstracts reduce accuracy (0.10, within temperature variation). These effects are mirrored in GPT-4o-mini, underscoring that source clarity and targeted retrieval -- not just model size -- drive performance. Overall, our results highlight both the promise and current limitations of LLMs for evidence-based clinical question answering. Retrieval-augmented prompting emerges as a useful strategy to improve factual accuracy and alignment with source evidence, while stratified evaluation by specialty and question type remains essential to understand current knowledge access and to contextualize model performance.

