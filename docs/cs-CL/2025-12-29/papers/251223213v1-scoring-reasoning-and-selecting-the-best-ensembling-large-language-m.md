---
layout: default
title: "Scoring, Reasoning, and Selecting the Best! Ensembling Large Language Models via a Peer-Review Process"
---

# Scoring, Reasoning, and Selecting the Best! Ensembling Large Language Models via a Peer-Review Process

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23213" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23213v1</a>
  <a href="https://arxiv.org/pdf/2512.23213.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23213v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23213v1', 'Scoring, Reasoning, and Selecting the Best! Ensembling Large Language Models via a Peer-Review Process')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhijun Chen, Zeyu Ji, Qianren Mao, Junhang Cheng, Bangjie Qin, Hao Wu, Zhuoran Li, Jingzheng Li, Kai Sun, Zizhe Wang, Yikun Ban, Zhu Sun, Xiangyang Ji, Hailong Sun

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出LLM-PeerReview，通过同行评审集成大语言模型，提升生成质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型集成` `同行评审` `无监督学习` `真值推断` `LLM-as-a-Judge`

## 📋 核心要点

1. 现有LLM集成方法缺乏可解释性，且依赖监督数据，泛化能力受限。
2. LLM-PeerReview模拟同行评审过程，利用多个LLM进行评分、推理和选择，实现无监督集成。
3. 实验表明，LLM-PeerReview在多个数据集上显著优于现有方法，提升效果明显。

## 📝 摘要（中文）

本文提出了一种名为LLM-PeerReview的无监督LLM集成方法，旨在从多个LLM针对同一查询生成的候选答案中选择最佳答案。该方法利用多个模型的集体智慧，充分发挥它们各自的优势。LLM-PeerReview构建于一个新颖的、受同行评审启发的框架之上，该框架提供了一个清晰且可解释的机制，同时保持完全无监督，从而实现灵活的适应性和泛化能力。具体而言，它包含三个阶段：评分阶段，利用新兴的“LLM-as-a-Judge”技术，使用多个LLM对每个答案进行评估；推理阶段，应用基于图模型的真值推断算法或简单的平均策略，聚合多个评分，为每个答案生成最终得分；选择阶段，选择得分最高的答案作为最佳集成输出。LLM-PeerReview概念简单，效果显著。该方法的两个变体在四个数据集上取得了优异的结果，分别超越了最近的先进模型Smoothie-Global 6.9%和7.3%。

## 🔬 方法详解

**问题定义**：现有的大语言模型集成方法通常缺乏可解释性，难以理解每个模型的贡献。此外，许多方法依赖于监督数据进行训练，这限制了它们在不同任务和数据集上的泛化能力。因此，如何设计一种无监督且可解释的LLM集成方法是一个重要的挑战。

**核心思路**：LLM-PeerReview的核心思路是模拟学术界的同行评审过程。每个LLM生成的答案都由其他LLM进行评估（评分），然后通过某种方式（例如，平均或更复杂的真值推断）将这些评分聚合起来，得到一个最终的得分。得分最高的答案被认为是最佳答案。这种设计借鉴了同行评审的智慧，利用多个LLM的判断力来选择最佳答案。

**技术框架**：LLM-PeerReview包含三个主要阶段：
1. **评分阶段**：使用多个LLM作为评审员，对每个候选答案进行评分。每个LLM都根据一定的标准（例如，相关性、准确性、流畅性等）对答案进行评估。
2. **推理阶段**：将多个LLM的评分进行聚合，得到每个答案的最终得分。可以使用简单的平均策略，也可以使用更复杂的基于图模型的真值推断算法，例如，考虑评审员之间的可信度。
3. **选择阶段**：选择得分最高的答案作为最终的集成输出。

**关键创新**：LLM-PeerReview的关键创新在于其基于同行评审的框架。与传统的集成方法相比，LLM-PeerReview具有以下优势：
* **无监督**：不需要监督数据进行训练，可以灵活地应用于不同的任务和数据集。
* **可解释**：每个LLM的评分都可以被追溯，从而可以理解每个模型的贡献。
* **自适应**：可以根据不同的任务和数据集选择不同的LLM作为评审员。

**关键设计**：
* **LLM选择**：选择合适的LLM作为评审员至关重要。可以根据LLM的专业领域、生成能力等因素进行选择。
* **评分标准**：定义清晰的评分标准，例如，相关性、准确性、流畅性等，可以提高评分的准确性。
* **真值推断算法**：选择合适的真值推断算法可以更准确地聚合多个评分。论文中提到了基于图模型的真值推断算法和简单的平均策略。
* **集成策略**：最终选择得分最高的答案作为集成输出，简单有效。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23213v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23213v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23213v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，LLM-PeerReview在四个数据集上取得了显著的性能提升。具体而言，该方法的两个变体分别超越了最近的先进模型Smoothie-Global 6.9%和7.3%。这些结果表明，LLM-PeerReview是一种有效的LLM集成方法，能够显著提升生成文本的质量。

## 🎯 应用场景

LLM-PeerReview可广泛应用于各种需要高质量文本生成的场景，例如问答系统、文本摘要、机器翻译、内容创作等。该方法能够有效提升生成文本的质量和可靠性，具有重要的实际应用价值。未来，可以进一步探索如何将LLM-PeerReview应用于更复杂的任务和领域，例如代码生成、对话系统等。

## 📄 摘要（原文）

> We propose LLM-PeerReview, an unsupervised LLM Ensemble method that selects the most ideal response from multiple LLM-generated candidates for each query, harnessing the collective wisdom of multiple models with diverse strengths. LLM-PeerReview is built on a novel, peer-review-inspired framework that offers a clear and interpretable mechanism, while remaining fully unsupervised for flexible adaptability and generalization. Specifically, it operates in three stages: For scoring, we use the emerging LLM-as-a-Judge technique to evaluate each response by reusing multiple LLMs at hand; For reasoning, we can apply a principled graphical model-based truth inference algorithm or a straightforward averaging strategy to aggregate multiple scores to produce a final score for each response; Finally, the highest-scoring response is selected as the best ensemble output. LLM-PeerReview is conceptually simple and empirically powerful. The two variants of the proposed approach obtain strong results across four datasets, including outperforming the recent advanced model Smoothie-Global by 6.9% and 7.3% points, respectively.

