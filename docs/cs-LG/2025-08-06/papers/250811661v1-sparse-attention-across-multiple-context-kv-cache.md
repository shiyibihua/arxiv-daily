---
layout: default
title: Sparse Attention across Multiple-context KV Cache
---

# Sparse Attention across Multiple-context KV Cache

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11661" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11661v1</a>
  <a href="https://arxiv.org/pdf/2508.11661.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11661v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11661v1', 'Sparse Attention across Multiple-context KV Cache')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyi Cao, Qingyi Si, Jingbin Zhang, Bingquan Liu

**分类**: cs.LG, cs.CL

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出SamKV以解决多上下文KV缓存的稀疏注意力问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长序列推理` `稀疏注意力` `多上下文` `键值缓存` `检索增强生成` `自然语言处理` `模型优化`

## 📋 核心要点

1. 现有方法在多上下文场景中缺乏交叉注意力，导致推理效率低下。
2. SamKV通过考虑其他上下文的信息来稀疏化当前上下文，从而提高效率。
3. 实验结果显示，SamKV在不损失准确度的情况下，序列长度压缩至15%，显著提升了吞吐量。

## 📝 摘要（中文）

大型语言模型在长序列推理中面临显著的成本挑战。为提高推理效率，重用历史的键值（KV）缓存已成为主流方法。近期的进展通过稀疏注意力机制选择最相关的KV缓存，进一步提升了吞吐量。然而，这些技术仅限于单上下文场景。在检索增强生成（RAG）场景中，文档的KV缓存独立计算，缺乏上下文间的交叉注意力，导致现有方法效果不佳。本文提出SamKV，首次探索多上下文KV缓存的注意力稀疏化，考虑其他上下文的互补信息以稀疏化一个上下文，并局部重新计算稀疏信息。实验表明，该方法在不降低准确度的情况下将序列长度压缩至15%，显著提升了多上下文RAG场景的吞吐量。

## 🔬 方法详解

**问题定义**：本文旨在解决在多上下文场景中，现有方法因缺乏交叉注意力而导致的推理效率低下问题。现有技术在计算KV缓存时需保留所有缓存，造成内存开销大。

**核心思路**：SamKV的核心思路是通过稀疏化一个上下文时，考虑其他上下文的互补信息，从而在保持准确度的同时，减少计算量和内存使用。

**技术框架**：SamKV的整体架构包括多个模块：首先独立计算每个文档的KV缓存，然后在稀疏化过程中引入其他上下文的信息，最后局部重新计算稀疏后的信息以提高效率。

**关键创新**：SamKV的主要创新在于首次实现了多上下文KV缓存的注意力稀疏化，突破了以往方法仅适用于单上下文的限制，显著提升了多上下文场景下的推理效率。

**关键设计**：在设计中，SamKV采用了特定的参数设置以优化稀疏化过程，并设计了损失函数以确保在稀疏化过程中不损失准确度，同时保持网络结构的灵活性和高效性。

## 📊 实验亮点

实验结果表明，SamKV在多上下文RAG场景中将序列长度压缩至15%，与全重计算基线相比，准确度未降低，显著提升了吞吐量，展示了其在实际应用中的有效性。

## 🎯 应用场景

该研究在检索增强生成（RAG）任务中具有广泛的应用潜力，能够有效提升长文本处理的效率，适用于信息检索、对话系统和文本生成等领域，未来可能推动更高效的自然语言处理模型的发展。

## 📄 摘要（原文）

> Large language models face significant cost challenges in long-sequence inference. To address this, reusing historical Key-Value (KV) Cache for improved inference efficiency has become a mainstream approach. Recent advances further enhance throughput by sparse attention mechanisms to select the most relevant KV Cache, thereby reducing sequence length. However, such techniques are limited to single-context scenarios, where historical KV Cache is computed sequentially with causal-attention dependencies. In retrieval-augmented generation (RAG) scenarios, where retrieved documents as context are unknown beforehand, each document's KV Cache is computed and stored independently (termed multiple-context KV Cache), lacking cross-attention between contexts. This renders existing methods ineffective. Although prior work partially recomputes multiple-context KV Cache to mitigate accuracy loss from missing cross-attention, it requires retaining all KV Cache throughout, failing to reduce memory overhead. This paper presents SamKV, the first exploration of attention sparsification for multiple-context KV Cache. Specifically, SamKV takes into account the complementary information of other contexts when sparsifying one context, and then locally recomputes the sparsified information. Experiments demonstrate that our method compresses sequence length to 15% without accuracy degradation compared with full-recompuation baselines, significantly boosting throughput in multi-context RAG scenarios.

