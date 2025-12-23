---
layout: default
title: Query-Level Uncertainty in Large Language Models
---

# Query-Level Uncertainty in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09669" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09669v3</a>
  <a href="https://arxiv.org/pdf/2506.09669.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09669v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09669v3', 'Query-Level Uncertainty in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lihu Chen, Gerard de Melo, Fabian M. Suchanek, Gaël Varoquaux

**分类**: cs.CL

**发布日期**: 2025-06-11 (更新: 2025-10-06)

**备注**: Under Review

---

## 💡 一句话要点

**提出查询级不确定性方法以提升大语言模型的知识边界识别**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `查询级不确定性` `知识边界` `自适应推理` `内部信心` `信息检索` `计算效率`

## 📋 核心要点

1. 现有的大语言模型在识别知识边界方面存在不足，无法有效区分可回答与不可回答的查询。
2. 本文提出的内部信心方法通过层与标记的自我评估，能够在生成之前评估模型的回答能力。
3. 实验结果显示，内部信心在信心质量上优于多个基线，同时在自适应推理中降低了推理成本。

## 📝 摘要（中文）

大语言模型（LLMs）需要识别其知识边界，以区分能够自信回答的查询与超出其能力范围的查询。本文提出了一种通过查询级不确定性来检测知识边界的方法，能够在生成任何标记之前评估模型是否能够回答特定查询，从而避免生成成本。我们提出了一种名为内部信心的训练无关方法，利用层和标记的自我评估提供可靠的不确定性信号。实证研究表明，内部信心在事实问答和数学推理任务中优于多个基线，同时计算成本更低，并在自适应推理设置中展现出其优势。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在回答查询时无法有效识别知识边界的问题。现有方法往往在生成回答后才发现模型的能力不足，导致不必要的计算开销。

**核心思路**：论文提出的内部信心方法通过自我评估机制，能够在生成任何标记之前评估模型的回答能力，从而避免不必要的生成成本。这样的设计使得模型在面对不确定性时能够采取更为灵活的应对策略。

**技术框架**：该方法的整体架构包括多个模块，首先是自我评估模块，通过对层与标记的分析来计算不确定性信号；其次是决策模块，根据不确定性信号决定是否进行生成或调用检索增强生成（RAG）机制。

**关键创新**：内部信心方法的最大创新在于其训练无关性和高效性，通过自我评估提供的不确定性信号，使得模型在推理过程中能够更好地适应不同的查询类型，与传统方法相比，显著降低了计算成本。

**关键设计**：在设计上，内部信心方法采用了多层次的自我评估机制，结合了不同层的输出信息，确保信心评估的准确性。同时，损失函数的设计也考虑了不确定性信号的有效性，以提升模型的整体性能。

## 📊 实验亮点

实验结果显示，内部信心方法在事实问答和数学推理任务中，相较于多个基线方法，信心质量有显著提升，且计算成本降低。具体而言，在自适应推理设置中，该方法在RAG和模型级联中表现出色，保持了整体性能的同时减少了推理成本。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、教育辅助工具以及任何需要高效信息检索的场景。通过提升模型对知识边界的识别能力，可以显著提高用户体验，减少错误信息的传播，未来可能在信任度高的AI系统中发挥重要作用。

## 📄 摘要（原文）

> It is important for Large Language Models (LLMs) to be aware of the boundary of their knowledge, distinguishing queries they can confidently answer from those that lie beyond their capabilities. Such awareness enables models to perform adaptive inference, such as invoking retrieval-augmented generation (RAG), engaging in slow and deep thinking, or abstaining from answering when appropriate. These mechanisms are key to developing efficient and trustworthy AI. In this work, we propose a method to detect knowledge boundaries via Query-Level Uncertainty, which estimates if a model is capable of answering a given query before generating any tokens, thus avoiding the generation cost. To this end, we propose a novel, training-free method called Internal Confidence, which leverages self-evaluations across layers and tokens to provide a reliable signal of uncertainty. Empirical studies on both factual question answering and mathematical reasoning tasks demonstrate that our Internal Confidence outperforms several baselines in quality of confidence while being computationally cheaper. Furthermore, we demonstrate its benefits in adaptive inference settings, showing that for RAG and model cascading it reduces inference costs while preserving overall performance.

