---
layout: default
title: Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning
---

# Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18395" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18395v2</a>
  <a href="https://arxiv.org/pdf/2508.18395.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18395v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18395v2', 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jungsuk Oh, Jay-Yoon Lee

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-25 (更新: 2025-12-16)

---

## 💡 一句话要点

**提出潜在自一致性方法以解决长短答案推理中的一致性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自一致性` `语言模型` `短答案推理` `长答案推理` `语义一致性` `机器学习` `自然语言处理`

## 📋 核心要点

1. 现有方法在处理复杂或长形式问题时，输出一致性较差，尤其是短形式问答中的准确性受到影响。
2. 论文提出的潜在自一致性（LSC）方法，通过可学习的标记嵌入选择语义一致的响应，提升了输出的一致性。
3. 实验结果表明，LSC在短形式和长形式推理基准上均超越了现有方法，且计算开销极小，表现出色。

## 📝 摘要（中文）

在大型语言模型（LLMs）中，概率解码常常导致不一致的输出，尤其是在复杂或长形式问题上。自一致性（SC）通过对精确字符串进行多数投票来缓解短形式问答中的这一问题，而通用自一致性（USC）和加权单元一致性评分（WUCS）虽然扩展到长形式响应，但在短形式基准上准确性下降。本文提出了潜在自一致性（LSC），通过可学习的标记嵌入选择最语义一致的响应。LSC在标准解码基础上仅引入最多0.9%的运行时开销，且无需改变模型架构。在6个短形式和5个长形式推理基准上，LSC在平均性能上超越了SC、USC和WUCS，同时在原始推理上增加的计算开销微乎其微。这些结果使LSC成为一种可靠的一致性选择方法，能够有效处理各种答案格式。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在复杂问题上的输出不一致性，现有的自一致性方法在短形式和长形式问答中存在准确性不足的问题。

**核心思路**：潜在自一致性（LSC）通过引入可学习的标记嵌入，选择最语义一致的响应，从而提高输出的一致性和准确性。

**技术框架**：LSC的整体架构包括对输入的标记进行嵌入处理，随后通过轻量级的前向处理来选择最优响应，整个过程不需要改变基础模型的架构。

**关键创新**：LSC的主要创新在于其轻量级的处理方式和可学习的嵌入选择机制，使其在保持高性能的同时，计算开销极小，与现有方法相比具有显著优势。

**关键设计**：在设计中，LSC采用了可学习的标记嵌入，并在损失函数中引入了语义一致性度量，确保选择的响应在语义上最为一致。

## 📊 实验亮点

在6个短形式和5个长形式推理基准上，LSC方法在平均性能上超越了自一致性（SC）、通用自一致性（USC）和加权单元一致性评分（WUCS），并且在计算开销上仅增加了最多0.9%。

## 🎯 应用场景

该研究的潜在应用领域包括教育、客服和信息检索等场景，能够有效提升基于语言模型的问答系统的准确性和可靠性。未来，LSC方法可能在多种自然语言处理任务中发挥重要作用，推动智能问答系统的发展。

## 📄 摘要（原文）

> Probabilistic decoding in Large Language Models (LLMs) often yields inconsistent outputs, particularly on complex or long-form questions. Self-Consistency (SC) mitigates this for short-form QA by majority voting over exact strings, whereas Universal Self-Consistency (USC) and Weighted Unigram Consistency Score (WUCS) extend to long-form responses but lose accuracy on short-form benchmarks.
>   We introduce \textbf{Latent Self-Consistency (LSC)}, which selects the most semantically consistent response using learnable token embeddings. LSC's lightweight forward processing of summary tokens only introduces negligible runtime overhead (at most $0.9\%$) on top of standard decoding of the base LLM, and requires no changes to the model architecture.
>   Across 6 short-form and 5 long-form reasoning benchmarks (e.g., MATH, MMLU, TruthfulQA), LSC surpasses SC, USC, and WUCS on both short-form and long-form on average performance, while adding negligible computational overhead on vanilla inference. These results position LSC as a reliable consistency-selection method that works effectively across various answer formats. Additionally, LSC provides well-calibrated confidence estimates, maintaining low expected calibration error across both answer formats.

