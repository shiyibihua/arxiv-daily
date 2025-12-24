---
layout: default
title: Evaluating Large Language Models as Expert Annotators
---

# Evaluating Large Language Models as Expert Annotators

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07827" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07827v1</a>
  <a href="https://arxiv.org/pdf/2508.07827.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07827v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07827v1', 'Evaluating Large Language Models as Expert Annotators')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu-Min Tseng, Wei-Lin Chen, Chung-Chi Chen, Hsin-Hsi Chen

**分类**: cs.CL

**发布日期**: 2025-08-11

**备注**: Accepted to COLM 2025

---

## 💡 一句话要点

**评估大型语言模型作为专家标注者的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数据标注` `专家知识` `多代理讨论` `推理模型` `自然语言处理` `金融` `生物医学`

## 📋 核心要点

1. 现有方法在需要专家知识的领域中，LLMs的标注效果尚未得到充分验证，存在性能不足的问题。
2. 论文提出了一种多代理讨论框架，模拟人类标注者的讨论过程，以提高LLMs的标注准确性。
3. 实验结果显示，单个LLMs的推理技术效果有限，且多代理环境中模型行为表现出特定特征，未能显著提升标注性能。

## 📝 摘要（中文）

文本数据标注是一个成本高、耗时长且劳动密集的过程。尽管大型语言模型（LLMs）在一般自然语言处理任务中显示出作为人类标注者的潜力，但在需要专家知识的领域中的标注任务效果仍未得到充分探索。本文研究了顶尖LLMs是否能够作为人类专家标注者的直接替代品，特别是在金融、生物医学和法律等高度专业化领域。我们提出了一种多代理讨论框架，模拟人类标注者的讨论过程，LLMs在此过程中考虑其他代理的标注和理由。实验结果表明，单个LLMs的推理技术在数据标注中的效果有限，且多代理环境中模型行为表现出特定特征。

## 🔬 方法详解

**问题定义**：本文旨在探讨大型语言模型在金融、生物医学和法律等专业领域的标注效果，现有方法未能充分验证其在专家知识领域的有效性。

**核心思路**：通过构建多代理讨论框架，模拟人类标注者的互动，使LLMs在考虑他人标注和理由的基础上进行最终标注，以期提高标注质量。

**技术框架**：整体架构包括多个LLMs作为代理，参与讨论并进行标注。每个代理在标注前需考虑其他代理的意见和理由，形成集体决策。

**关键创新**：提出的多代理讨论框架是与现有单一LLM标注方法的本质区别，强调了模型间的互动和讨论对标注结果的影响。

**关键设计**：在实验中使用了推理模型（如o3-mini）进行比较，设置了不同的推理时间技术（如链式思维和自一致性），以评估其对标注效果的影响。实验结果表明，推理模型在大多数设置下未能显著提升性能。

## 📊 实验亮点

实验结果显示，单个LLMs在推理技术的应用下仅有边际或负向的性能提升，且多代理讨论环境中，某些模型（如Claude 3.7 Sonnet）在面对其他代理的正确标注时，仍然保持初始标注不变，表明模型的固执性。

## 🎯 应用场景

该研究的潜在应用领域包括金融分析、生物医学研究和法律文书处理等专业领域，能够为数据标注提供更高效的解决方案，降低人工成本，提高标注质量。未来，随着LLMs技术的进步，该方法可能会在更多专业领域得到应用。

## 📄 摘要（原文）

> Textual data annotation, the process of labeling or tagging text with relevant information, is typically costly, time-consuming, and labor-intensive. While large language models (LLMs) have demonstrated their potential as direct alternatives to human annotators for general domains natural language processing (NLP) tasks, their effectiveness on annotation tasks in domains requiring expert knowledge remains underexplored. In this paper, we investigate: whether top-performing LLMs, which might be perceived as having expert-level proficiency in academic and professional benchmarks, can serve as direct alternatives to human expert annotators? To this end, we evaluate both individual LLMs and multi-agent approaches across three highly specialized domains: finance, biomedicine, and law. Specifically, we propose a multi-agent discussion framework to simulate a group of human annotators, where LLMs are tasked to engage in discussions by considering others' annotations and justifications before finalizing their labels. Additionally, we incorporate reasoning models (e.g., o3-mini) to enable a more comprehensive comparison. Our empirical results reveal that: (1) Individual LLMs equipped with inference-time techniques (e.g., chain-of-thought (CoT), self-consistency) show only marginal or even negative performance gains, contrary to prior literature suggesting their broad effectiveness. (2) Overall, reasoning models do not demonstrate statistically significant improvements over non-reasoning models in most settings. This suggests that extended long CoT provides relatively limited benefits for data annotation in specialized domains. (3) Certain model behaviors emerge in the multi-agent discussion environment. For instance, Claude 3.7 Sonnet with thinking rarely changes its initial annotations, even when other agents provide correct annotations or valid reasoning.

