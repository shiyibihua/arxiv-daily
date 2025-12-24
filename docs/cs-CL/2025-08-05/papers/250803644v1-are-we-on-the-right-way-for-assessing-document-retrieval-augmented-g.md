---
layout: default
title: Are We on the Right Way for Assessing Document Retrieval-Augmented Generation?
---

# Are We on the Right Way for Assessing Document Retrieval-Augmented Generation?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03644" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03644v1</a>
  <a href="https://arxiv.org/pdf/2508.03644.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03644v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03644v1', 'Are We on the Right Way for Assessing Document Retrieval-Augmented Generation?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenxuan Shen, Mingjia Wang, Yaochen Wang, Dongping Chen, Junjie Yang, Yao Wan, Weiwei Lin

**分类**: cs.CL, cs.CV, cs.IR

**发布日期**: 2025-08-05

**备注**: In submission. Project website: https://double-bench.github.io/

---

## 💡 一句话要点

**提出Double-Bench以解决文档检索增强生成评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文档检索` `增强生成` `多模态评估` `大语言模型` `真实数据验证` `评估基准` `信息检索`

## 📋 核心要点

1. 现有文档检索增强生成系统的评估方法存在不足，无法真实反映其在实际应用中的表现。
2. 本文提出Double-Bench评估系统，旨在提供对文档RAG系统各组件的细致评估，克服现有方法的局限。
3. 通过对9种最先进的嵌入模型和4种文档RAG框架的实验，发现文本与视觉嵌入模型的差距正在缩小。

## 📝 摘要（中文）

文档检索增强生成（RAG）系统利用多模态大语言模型（MLLMs）在复杂文档理解中展现出巨大潜力，但其发展受到评估不足的严重制约。现有基准往往聚焦于文档RAG系统的特定部分，使用的合成数据缺乏完整的真实标签，因此未能反映现实世界中的瓶颈与挑战。为克服这些局限性，本文提出了Double-Bench，一个新的大规模、多语言和多模态评估系统，能够对文档RAG系统中的每个组件进行细致评估。该系统包含3,276份文档（72,880页）和5,168个单跳及多跳查询，覆盖6种语言和4种文档类型，并支持动态更新以应对潜在的数据污染问题。我们的实验表明，文本和视觉嵌入模型之间的差距正在缩小，强调了构建更强文档检索模型的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决文档检索增强生成（RAG）系统评估不足的问题。现有方法往往依赖合成数据，缺乏真实的证据支持和完整的标签，导致评估结果不准确。

**核心思路**：提出Double-Bench评估系统，通过大规模、多语言和多模态的数据集，提供对文档RAG系统各个组件的细致评估，确保评估的全面性和准确性。

**技术框架**：Double-Bench系统包含3,276份文档和5,168个查询，支持动态更新以应对数据污染问题。查询基于经过严格审核的证据页面，确保数据的质量和完整性。

**关键创新**：最重要的创新在于构建了一个全面的评估框架，能够细致评估文档RAG系统的各个组成部分，并通过真实数据验证其有效性。与现有方法相比，Double-Bench提供了更高的评估准确性和可靠性。

**关键设计**：在设计中，采用了多模态数据集，确保涵盖多种文档类型和语言。同时，查询的生成经过人类专家验证，以提高数据的质量和完整性。

## 📊 实验亮点

实验结果显示，文本与视觉嵌入模型之间的性能差距正在缩小，强调了构建更强文档检索模型的必要性。此外，研究还揭示了当前文档RAG框架中的过度自信问题，即在缺乏证据支持的情况下仍然提供答案。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索、智能问答系统和文档自动生成等。通过提供更准确的评估基准，Double-Bench将推动文档检索增强生成系统的研究与应用，促进相关技术的进步与发展。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) systems using Multimodal Large Language Models (MLLMs) show great promise for complex document understanding, yet their development is critically hampered by inadequate evaluation. Current benchmarks often focus on specific part of document RAG system and use synthetic data with incomplete ground truth and evidence labels, therefore failing to reflect real-world bottlenecks and challenges. To overcome these limitations, we introduce Double-Bench: a new large-scale, multilingual, and multimodal evaluation system that is able to produce fine-grained assessment to each component within document RAG systems. It comprises 3,276 documents (72,880 pages) and 5,168 single- and multi-hop queries across 6 languages and 4 document types with streamlined dynamic update support for potential data contamination issues. Queries are grounded in exhaustively scanned evidence pages and verified by human experts to ensure maximum quality and completeness. Our comprehensive experiments across 9 state-of-the-art embedding models, 4 MLLMs and 4 end-to-end document RAG frameworks demonstrate the gap between text and visual embedding models is narrowing, highlighting the need in building stronger document retrieval models. Our findings also reveal the over-confidence dilemma within current document RAG frameworks that tend to provide answer even without evidence support. We hope our fully open-source Double-Bench provide a rigorous foundation for future research in advanced document RAG systems. We plan to retrieve timely corpus and release new benchmarks on an annual basis.

