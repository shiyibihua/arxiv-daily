---
layout: default
title: Evaluating Scoring Bias in LLM-as-a-Judge
---

# Evaluating Scoring Bias in LLM-as-a-Judge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22316" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22316v3</a>
  <a href="https://arxiv.org/pdf/2506.22316.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22316v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22316v3', 'Evaluating Scoring Bias in LLM-as-a-Judge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingquan Li, Shaoyu Dou, Kailai Shao, Chao Chen, Haixiang Hu

**分类**: cs.CL

**发布日期**: 2025-06-27 (更新: 2025-08-26)

---

## 💡 一句话要点

**提出评估LLM作为评判者中的评分偏差的方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `评分偏差` `评估框架` `自然语言处理` `公平性` `自动评分` `数据合成`

## 📋 核心要点

1. 现有的LLM作为评判者的研究多集中于比较评估，缺乏对评分评估中偏差的系统性研究。
2. 本文提出了一种新的评分偏差定义，并设计了一个全面的评估框架，以评估LLM作为评判者的评分偏差。
3. 实验结果显示，现有评判模型的评分稳定性受到评分偏差的显著影响，提供了改进评分模板设计的见解。

## 📝 摘要（中文）

大型语言模型（LLMs）的卓越表现促使其被广泛应用于复杂任务的评估中，尤其是在自然语言处理和偏好学习等领域。然而，LLM作为评判者中存在多种偏差，影响了判断的公平性和可靠性。现有研究主要集中在比较评估的偏差上，而对评分评估中的偏差系统性研究较少。本文定义了评分偏差，并提出了一个全面评估评分偏差的框架，通过数据合成增强现有基准，设计多维评估指标。实验结果表明，现有评判模型的评分稳定性受到评分偏差的干扰，进一步的探索性实验为评分提示模板的设计及偏差的缓解提供了有价值的见解。

## 🔬 方法详解

**问题定义**：本文旨在解决LLM作为评判者中评分偏差的问题，现有方法在评分评估中对偏差的关注不足，导致判断的公平性受到影响。

**核心思路**：通过定义评分偏差，并构建一个全面的评估框架，系统地评估LLM的评分偏差，旨在提高评判的公平性和可靠性。

**技术框架**：整体架构包括数据合成、评估数据集构建和多维评估指标设计。首先，通过数据合成增强现有基准，然后设计针对评分偏差的评估指标。

**关键创新**：最重要的创新在于系统性地定义和评估评分偏差，填补了现有研究的空白，提供了新的评估视角。

**关键设计**：在评估过程中，设计了多维度的评分指标，关注评分模板、评分ID和参考答案选择等方面，以全面评估评分偏差的影响。

## 📊 实验亮点

实验结果表明，现有评判模型的评分稳定性受到评分偏差的显著影响，具体表现为在不同偏差条件下评分结果的波动。通过设计的多维评估指标，能够有效识别和量化评分偏差，为后续改进提供了依据。

## 🎯 应用场景

该研究的潜在应用领域包括教育评估、内容审核和自动评分系统等，能够提升这些领域中评估的公平性和可靠性。未来，随着LLM的广泛应用，研究成果将对优化评估系统设计和提高用户信任度产生深远影响。

## 📄 摘要（原文）

> The remarkable performance of Large Language Models (LLMs) gives rise to``LLM-as-a-Judge'', where LLMs are employed as evaluators for complex tasks. Moreover, it has been widely adopted across fields such as Natural Language Processing (NLP), preference learning, and various specific domains. However, there are various biases within LLM-as-a-Judge, which adversely affect the fairness and reliability of judgments. Current research on evaluating or mitigating bias in LLM-as-a-Judge predominantly focuses on comparison-based evaluations, while systematic investigations into bias in scoring-based evaluations remain limited. Therefore, we define scoring bias in LLM-as-a-Judge as the scores differ when scoring judge models are bias-related perturbed, and provide a well-designed framework to comprehensively evaluate scoring bias. We augment existing LLM-as-a-Judge benchmarks through data synthesis to construct our evaluation dataset and design multi-faceted evaluation metrics. Our experimental results demonstrate that the scoring stability of existing judge models is disrupted by scoring biases. Further exploratory experiments and discussions provide valuable insights into the design of scoring prompt templates and the mitigation of scoring biases on aspects such as score rubrics, score IDs, and reference answer selection.

