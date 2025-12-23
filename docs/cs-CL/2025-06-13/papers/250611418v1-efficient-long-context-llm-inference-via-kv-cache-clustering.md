---
layout: default
title: Efficient Long-Context LLM Inference via KV Cache Clustering
---

# Efficient Long-Context LLM Inference via KV Cache Clustering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11418" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11418v1</a>
  <a href="https://arxiv.org/pdf/2506.11418.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11418v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11418v1', 'Efficient Long-Context LLM Inference via KV Cache Clustering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jie Hu, Shengnan Wang, Yutong He, Ping Gong, Jiawei Yi, Juncheng Zhang, Youhui Bai, Renhai Chen, Gong Zhang, Cheng Li, Kun Yuan

**分类**: cs.CL

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**提出Chelsea框架以解决长上下文LLM推理中的KV缓存问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文LLM` `KV缓存` `在线聚类` `块状软匹配` `推理加速` `内存优化` `自然语言处理`

## 📋 核心要点

1. 长上下文LLM的KV缓存需求庞大，现有方法要么丢失关键信息，要么效率提升有限。
2. 提出Chelsea框架，通过块状软匹配实现KV缓存的高效聚类，减少内存使用。
3. 实验结果显示，Chelsea在多个模型和基准测试中，KV缓存使用减少80%，推理速度提升显著。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在处理复杂任务中的广泛应用，长上下文LLM所需的庞大KV缓存带来了显著的部署挑战。现有方法往往会丢弃未来生成所需的重要信息，或因计算开销大而效率提升有限。本文提出了Chelsea，一个简单而有效的在线KV缓存聚类框架。我们观察到，关键状态在序列维度上表现出高度相似性。为实现高效聚类，我们将序列划分为块，并提出了块状软匹配方法，通过交替划分策略识别相似性聚类。Chelsea将每个聚类中的KV缓存合并为一个质心。实验表明，Chelsea在保持模型性能的同时，KV缓存内存使用减少高达80%，推理解码阶段加速最高可达3.19倍，端到端延迟减少最高可达2.72倍。

## 🔬 方法详解

**问题定义**：本文旨在解决长上下文LLM推理中KV缓存的高内存需求和计算开销问题。现有方法往往会丢失重要信息或效率提升有限，导致实际应用受限。

**核心思路**：我们提出Chelsea框架，利用关键状态在序列维度上的相似性，通过块状划分和软匹配策略实现KV缓存的高效聚类，从而减少内存使用并加速推理过程。

**技术框架**：Chelsea的整体架构包括序列划分、块状软匹配、聚类识别和KV缓存合并四个主要模块。首先，将输入序列划分为多个块，然后在每个块内进行软匹配以识别相似性，最后将相似的KV缓存合并为质心。

**关键创新**：Chelsea的核心创新在于块状软匹配策略和聚类合并机制，这与现有方法的直接丢弃或简单合并策略有本质区别，能够有效保留关键信息并提高效率。

**关键设计**：在实现过程中，我们采用了交替划分策略来优化块内的相似性识别，并通过理论分析验证了计算复杂度和内部划分策略的最优性。

## 📊 实验亮点

实验结果表明，Chelsea在多个长上下文基准测试中实现了高达80%的KV缓存内存使用减少，同时在推理解码阶段加速最高可达3.19倍，端到端延迟减少最高可达2.72倍，展现了其在效率和性能上的显著优势。

## 🎯 应用场景

Chelsea框架在长上下文LLM的推理中具有广泛的应用潜力，尤其适用于需要处理大量上下文信息的自然语言处理任务，如对话系统、文本生成和信息检索等。其显著的内存和速度优化将推动大型语言模型在实际应用中的部署和普及。

## 📄 摘要（原文）

> Large language models (LLMs) with extended context windows have become increasingly prevalent for tackling complex tasks. However, the substantial Key-Value (KV) cache required for long-context LLMs poses significant deployment challenges. Existing approaches either discard potentially critical information needed for future generations or offer limited efficiency gains due to high computational overhead. In this paper, we introduce Chelsea, a simple yet effective framework for online KV cache clustering. Our approach is based on the observation that key states exhibit high similarity along the sequence dimension. To enable efficient clustering, we divide the sequence into chunks and propose Chunked Soft Matching, which employs an alternating partition strategy within each chunk and identifies clusters based on similarity. Chelsea then merges the KV cache within each cluster into a single centroid. Additionally, we provide a theoretical analysis of the computational complexity and the optimality of the intra-chunk partitioning strategy. Extensive experiments across various models and long-context benchmarks demonstrate that Chelsea achieves up to 80% reduction in KV cache memory usage while maintaining comparable model performance. Moreover, with minimal computational overhead, Chelsea accelerates the decoding stage of inference by up to 3.19$\times$ and reduces end-to-end latency by up to 2.72$\times$.

