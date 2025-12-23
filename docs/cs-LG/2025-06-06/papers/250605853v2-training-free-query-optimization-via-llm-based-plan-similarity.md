---
layout: default
title: Training-Free Query Optimization via LLM-Based Plan Similarity
---

# Training-Free Query Optimization via LLM-Based Plan Similarity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05853" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05853v2</a>
  <a href="https://arxiv.org/pdf/2506.05853.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05853v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05853v2', 'Training-Free Query Optimization via LLM-Based Plan Similarity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikita Vasilenko, Alexander Demin, Vladimir Boorlakov

**分类**: cs.DB, cs.LG

**发布日期**: 2025-06-06 (更新: 2025-07-07)

**备注**: 18 pages, 5 figures

---

## 💡 一句话要点

**提出LLM-PM框架以实现无训练的查询优化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据库查询优化` `大型语言模型` `无训练优化` `执行计划嵌入` `性能提升`

## 📋 核心要点

1. 现有的数据库查询优化方法通常依赖于模型训练，导致灵活性和效率不足。
2. 本文提出的LLM-PM框架利用预训练的执行计划嵌入，避免了额外的训练过程，直接进行查询优化。
3. 在JOB-CEB基准测试中，LLM-PM实现了平均21%的查询延迟减少，显示出显著的性能提升。

## 📝 摘要（中文）

大型语言模型（LLM）嵌入为数据库查询优化提供了新的可能性。本文探讨了如何利用预训练的执行计划嵌入来指导SQL查询执行，而无需额外的模型训练。我们提出了LLM-PM（基于LLM的计划映射）框架，该框架嵌入查询的默认执行计划，找到其在先前执行计划中的k个最近邻，并基于邻域投票推荐数据库提示集。一个轻量级的一致性检查验证所选提示，而回退机制在需要时搜索完整的提示空间。在使用OpenGauss的JOB-CEB基准测试中评估，LLM-PM实现了平均21%的查询延迟减少。此项工作突显了LLM驱动的嵌入在查询性能上的实际改进潜力，并为无训练的嵌入式优化器指导系统开辟了新的方向。

## 🔬 方法详解

**问题定义**：本文旨在解决现有数据库查询优化方法依赖模型训练的问题，这限制了其灵活性和效率。

**核心思路**：LLM-PM框架通过使用预训练的执行计划嵌入，找到相似的历史执行计划，从而在无需额外训练的情况下优化查询。

**技术框架**：LLM-PM框架包括三个主要模块：执行计划嵌入、邻近计划查找和提示集推荐。首先，将查询的默认执行计划嵌入；然后，利用k近邻算法找到相似的历史计划；最后，基于邻域投票推荐提示集。

**关键创新**：LLM-PM的创新在于其无训练的优化方式，利用LLM嵌入直接进行查询优化，与传统方法相比，显著提高了效率和灵活性。

**关键设计**：框架中的关键设计包括轻量级的一致性检查机制和回退机制，确保在提示不合适时能够搜索完整的提示空间，以提高查询优化的可靠性。

## 📊 实验亮点

在JOB-CEB基准测试中，LLM-PM框架实现了平均21%的查询延迟减少，相较于传统方法表现出显著的性能提升。这一结果表明，LLM驱动的嵌入在实际应用中具有良好的效果，为数据库查询优化提供了新的思路。

## 🎯 应用场景

该研究的潜在应用领域包括数据库管理系统、数据分析平台和云计算服务等。通过提供无训练的查询优化方案，LLM-PM能够显著提高数据库查询的性能，降低延迟，提升用户体验，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large language model (LLM) embeddings offer a promising new avenue for database query optimization. In this paper, we explore how pre-trained execution plan embeddings can guide SQL query execution without the need for additional model training. We introduce LLM-PM (LLM-based Plan Mapping), a framework that embeds the default execution plan of a query, finds its k nearest neighbors among previously executed plans, and recommends database hintsets based on neighborhood voting. A lightweight consistency check validates the selected hint, while a fallback mechanism searches the full hint space when needed. Evaluated on the JOB-CEB benchmark using OpenGauss, LLM-PM achieves an average speed-up of 21% query latency reduction. This work highlights the potential of LLM-powered embeddings to deliver practical improvements in query performance and opens new directions for training-free, embedding-based optimizer guidance systems.

