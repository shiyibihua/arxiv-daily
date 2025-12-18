---
layout: default
title: Your Dense Retriever is Secretly an Expeditious Reasoner
---

# Your Dense Retriever is Secretly an Expeditious Reasoner

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21727" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21727v2</a>
  <a href="https://arxiv.org/pdf/2510.21727.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21727v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.21727v2', 'Your Dense Retriever is Secretly an Expeditious Reasoner')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yichi Zhang, Jun Bai, Zhixin Cai, Shuhan Qin, Zhuofan Chen, Jinghua Guan, Wenge Rong

**分类**: cs.IR, cs.AI, cs.LG

**发布日期**: 2025-09-27 (更新: 2025-10-28)

**备注**: 16 pages, 11 figures

---

## 💡 一句话要点

**提出AdaQR，自适应混合查询重写框架，提升推理检索效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稠密检索` `查询重写` `大型语言模型` `推理优化` `自适应路由`

## 📋 核心要点

1. 稠密检索器在处理推理密集型查询时面临挑战，计算成本高昂。
2. AdaQR框架通过Reasoner Router动态选择快速稠密推理或深度LLM推理。
3. 实验表明，AdaQR在降低推理成本的同时，保持甚至提高了检索性能。

## 📝 摘要（中文）

稠密检索器通过将查询和文档编码为连续向量来增强检索效果，但它们通常难以处理推理密集型查询。虽然大型语言模型（LLM）可以重构查询以捕捉复杂的推理，但普遍应用它们会产生巨大的计算成本。在这项工作中，我们提出了自适应查询推理（AdaQR），这是一个混合查询重写框架。在该框架内，Reasoner Router动态地将每个查询导向快速稠密推理或深度LLM推理。稠密推理由稠密推理器实现，该推理器直接在嵌入空间中执行LLM风格的推理，从而在效率和准确性之间实现可控的权衡。在大型检索基准BRIGHT上的实验表明，AdaQR将推理成本降低了28%，同时保持甚至提高了7%的检索性能。

## 🔬 方法详解

**问题定义**：稠密检索器在处理需要复杂推理的查询时表现不佳，而使用大型语言模型（LLM）进行查询重写虽然可以提升性能，但计算成本过高，难以在实际应用中普及。因此，如何在保证检索性能的同时，降低推理计算成本，是本文要解决的核心问题。

**核心思路**：本文的核心思路是设计一个自适应的查询推理框架，该框架能够根据查询的复杂程度，动态地选择使用计算成本较低的稠密推理器或计算成本较高的LLM推理器。通过这种方式，可以避免对所有查询都使用LLM进行推理，从而降低整体的计算成本。

**技术框架**：AdaQR框架包含三个主要模块：Reasoner Router、Dense Reasoner和LLM Reasoner。Reasoner Router负责根据查询的特征，决定将查询路由到Dense Reasoner或LLM Reasoner。Dense Reasoner在嵌入空间中执行LLM风格的推理，提供快速但可能不太准确的推理结果。LLM Reasoner使用大型语言模型进行查询重写，提供更准确但计算成本更高的推理结果。最终，检索器使用重写后的查询进行检索。

**关键创新**：该方法最重要的创新点在于提出了Dense Reasoner，它能够在嵌入空间中模拟LLM的推理过程，从而在保证一定推理能力的同时，大大降低了计算成本。与直接使用LLM进行推理相比，Dense Reasoner更加高效。此外，自适应路由机制能够根据查询的复杂程度，动态地选择合适的推理器，进一步优化了计算资源的利用。

**关键设计**：Reasoner Router的设计至关重要，需要准确地判断查询是否需要LLM的深度推理。具体实现可能涉及训练一个分类器，该分类器以查询的特征为输入，输出查询应该路由到Dense Reasoner还是LLM Reasoner。Dense Reasoner的训练可能需要使用知识蒸馏技术，将LLM的推理能力迁移到嵌入空间中。损失函数的设计需要平衡检索的准确性和计算成本。

## 📊 实验亮点

在BRIGHT基准测试中，AdaQR在保持甚至提高7%检索性能的同时，将推理成本降低了28%。这表明AdaQR能够有效地平衡检索性能和计算成本，为实际应用提供了可行的解决方案。实验结果证明了自适应查询推理框架的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要进行信息检索的场景，例如搜索引擎、问答系统、推荐系统等。通过降低推理计算成本，可以使LLM的推理能力更广泛地应用于实际应用中，提升用户体验。未来的研究可以探索更高效的Dense Reasoner设计和更准确的Reasoner Router。

## 📄 摘要（原文）

> Dense retrievers enhance retrieval by encoding queries and documents into continuous vectors, but they often struggle with reasoning-intensive queries. Although Large Language Models (LLMs) can reformulate queries to capture complex reasoning, applying them universally incurs significant computational cost. In this work, we propose Adaptive Query Reasoning (AdaQR), a hybrid query rewriting framework. Within this framework, a Reasoner Router dynamically directs each query to either fast dense reasoning or deep LLM reasoning. The dense reasoning is achieved by the Dense Reasoner, which performs LLM-style reasoning directly in the embedding space, enabling a controllable trade-off between efficiency and accuracy. Experiments on large-scale retrieval benchmarks BRIGHT show that AdaQR reduces reasoning cost by 28% while preserving-or even improving-retrieval performance by 7%.

