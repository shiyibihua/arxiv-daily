---
layout: default
title: Representation Consistency for Accurate and Coherent LLM Answer Aggregation
---

# Representation Consistency for Accurate and Coherent LLM Answer Aggregation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21590" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21590v2</a>
  <a href="https://arxiv.org/pdf/2506.21590.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21590v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21590v2', 'Representation Consistency for Accurate and Coherent LLM Answer Aggregation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junqi Jiang, Tom Bewley, Salim I. Amoukou, Francesco Leofante, Antonio Rago, Saumitra Mishra, Francesca Toni

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-18 (更新: 2025-11-03)

**备注**: Accepted at NeurIPS 2025. Camera-ready version

---

## 💡 一句话要点

**提出表示一致性方法以提升LLM答案聚合的准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `答案聚合` `推理优化` `表示一致性` `内部激活` `稀疏编码` `计算效率`

## 📋 核心要点

1. 现有方法在推理过程中需要复杂的提示和采样策略修改，限制了LLM的灵活性和性能。
2. 本文提出的表示一致性方法通过分析模型内部激活的一致性来优化答案聚合，避免了不一致推理带来的干扰。
3. 通过对四个开源LLM和四个推理数据集的实验，验证了RC方法在准确性上相较于基线的提升，达到了4%。

## 📝 摘要（中文）

测试时扩展通过在推理过程中分配更多计算预算来提高大型语言模型（LLMs）的性能。现有方法通常需要对提示和采样策略进行复杂的修改。本文提出了一种新的测试时扩展方法——表示一致性（RC），用于聚合来自多个候选响应的答案，无论这些答案是如何生成的。RC通过考虑每个答案在候选响应集中的出现次数以及生成每个答案的内部激活一致性来增强答案聚合。实验结果表明，RC在推理过程中显著提高了任务性能，相较于强基线方法，准确性提升可达4%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM在推理时答案聚合的准确性问题，现有方法往往需要复杂的修改，导致灵活性不足。

**核心思路**：提出表示一致性（RC）方法，通过分析模型生成答案时的内部激活一致性，来优化答案聚合，降低不一致推理的影响。

**技术框架**：RC方法的整体流程包括收集候选响应、计算内部激活、评估一致性以及最终的答案聚合，主要模块包括激活缓存和相似度计算。

**关键创新**：RC的核心创新在于引入内部激活一致性作为答案聚合的标准，与传统方法仅依赖答案出现次数的方式本质不同。

**关键设计**：方法中使用了缓存的激活信号和轻量级的相似度计算，无需额外的模型查询，且支持稀疏激活信号的编码，提升了计算效率。

## 📊 实验亮点

实验结果显示，表示一致性方法在四个开源LLM上均实现了显著的性能提升，相较于强基线方法，准确性提升幅度可达4%。这一结果验证了稀疏激活信号的一致性与合理推理之间的良好对应关系。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的问答系统、对话生成和信息检索等。通过提高LLM在推理过程中的答案聚合能力，能够显著提升用户体验和系统的智能化水平，未来可能影响更广泛的AI应用场景。

## 📄 摘要（原文）

> Test-time scaling improves large language models' (LLMs) performance by allocating more compute budget during inference. To achieve this, existing methods often require intricate modifications to prompting and sampling strategies. In this work, we introduce representation consistency (RC), a test-time scaling method for aggregating answers drawn from multiple candidate responses of an LLM regardless of how they were generated, including variations in prompt phrasing and sampling strategy. RC enhances answer aggregation by not only considering the number of occurrences of each answer in the candidate response set, but also the consistency of the model's internal activations while generating the set of responses leading to each answer. These activations can be either dense (raw model activations) or sparse (encoded via pretrained sparse autoencoders). Our rationale is that if the model's representations of multiple responses converging on the same answer are highly variable, this answer is more likely to be the result of incoherent reasoning and should be down-weighted during aggregation. Importantly, our method only uses cached activations and lightweight similarity computations and requires no additional model queries. Through experiments with four open-source LLMs and four reasoning datasets, we validate the effectiveness of RC for improving task performance during inference, with consistent accuracy improvements (up to 4%) over strong test-time scaling baselines. We also show that consistency in the sparse activation signals aligns well with the common notion of coherent reasoning.

