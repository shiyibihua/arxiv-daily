---
layout: default
title: Semantic Outlier Removal with Embedding Models and LLMs
---

# Semantic Outlier Removal with Embedding Models and LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16644" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16644v1</a>
  <a href="https://arxiv.org/pdf/2506.16644.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16644v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16644v1', 'Semantic Outlier Removal with Embedding Models and LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eren Akbiyik, João Almeida, Rik Melis, Ritu Sriram, Viviana Petrescu, Vilhjálmur Vilhjálmsson

**分类**: cs.LG, cs.IR

**发布日期**: 2025-06-19

**备注**: Accepted to the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) Industry Track, 10 pages

---

## 💡 一句话要点

**提出SORE方法以解决多语言文本中冗余内容去除问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语义异常去除` `多语言处理` `文本挖掘` `嵌入模型` `近似最近邻搜索` `信息提取` `机器学习`

## 📋 核心要点

1. 现有的文本处理方法在多语言环境中效果不佳，难以处理上下文敏感的内容，导致冗余信息难以去除。
2. SORE方法通过利用多语言句子嵌入和近似最近邻搜索，识别并剔除不必要的文本段落，提供了一种高效的解决方案。
3. 实验结果显示，SORE在多种场景中表现优异，超越了传统结构化方法，精度接近大型语言模型，且成本显著降低。

## 📝 摘要（中文）

现代文本处理流程需要有效的方法来去除多余内容，同时保留文档的核心信息。传统方法如HTML模板提取或关键词过滤在多语言环境中常常失效，并且难以处理上下文敏感的细微差别。本文提出了SORE（语义异常去除），一种成本效益高、透明的方法，利用多语言句子嵌入和近似最近邻搜索来识别和剔除不必要的文本段落。通过首先利用元数据嵌入识别核心内容，然后标记与预定义异常组相似或显著偏离核心的段落，SORE以极低的成本实现了接近大型语言模型的提取精度。实验结果表明，SORE在HTML数据集上优于结构化方法，并在多种场景中表现出高精度。该系统目前已在生产中部署，每天处理数百万份文档，保持高效和准确。为了促进可重复性和进一步研究，我们发布了实现和评估数据集。

## 🔬 方法详解

**问题定义**：本文旨在解决多语言文本处理中冗余内容的去除问题。现有方法如HTML模板提取和关键词过滤在处理多语言文本时常常失效，无法有效捕捉上下文的细微差别。

**核心思路**：SORE方法的核心思路是利用多语言句子嵌入和近似最近邻搜索，首先识别核心内容，然后标记与预定义异常组相似或显著偏离核心的文本段落，从而实现高效的冗余内容去除。

**技术框架**：SORE的整体架构包括两个主要模块：首先是元数据嵌入模块，用于识别文档的核心内容；其次是异常检测模块，通过近似最近邻搜索来标记不必要的文本段落。

**关键创新**：SORE的主要创新在于其结合了多语言句子嵌入与近似最近邻搜索的技术，显著提高了文本处理的效率和准确性，尤其是在多语言环境中。与传统方法相比，SORE在成本和性能上都有显著优势。

**关键设计**：在设计上，SORE采用了高效的嵌入模型和优化的搜索算法，确保在处理大规模文档时仍能保持高精度。此外，系统的参数设置经过精心调整，以适应不同语言和文本类型的需求。

## 📊 实验亮点

实验结果表明，SORE在处理HTML数据集时的精度显著高于传统结构化方法，接近大型语言模型的提取精度。具体而言，SORE在多种场景下的表现均优于基线方法，展示了其在多语言文本处理中的有效性和高效性。

## 🎯 应用场景

SORE方法具有广泛的应用潜力，尤其适用于需要处理大量多语言文档的场景，如新闻聚合、社交媒体监控和在线内容管理等。其高效的冗余内容去除能力将大大提升信息提取的质量和效率，未来可能在更多领域得到推广和应用。

## 📄 摘要（原文）

> Modern text processing pipelines demand robust methods to remove extraneous content while preserving a document's core message. Traditional approaches such as HTML boilerplate extraction or keyword filters often fail in multilingual settings and struggle with context-sensitive nuances, whereas Large Language Models (LLMs) offer improved quality at high computational cost. We introduce SORE (Semantic Outlier Removal), a cost-effective, transparent method that leverages multilingual sentence embeddings and approximate nearest-neighbor search to identify and excise unwanted text segments. By first identifying core content via metadata embedding and then flagging segments that either closely match predefined outlier groups or deviate significantly from the core, SORE achieves near-LLM extraction precision at a fraction of the cost. Experiments on HTML datasets demonstrate that SORE outperforms structural methods and yield high precision in diverse scenarios. Our system is currently deployed in production, processing millions of documents daily across multiple languages while maintaining both efficiency and accuracy. To facilitate reproducibility and further research, we release our implementation and evaluation datasets.

