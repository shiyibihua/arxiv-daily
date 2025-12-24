---
layout: default
title: Accelerating Latency-Critical Applications with AI-Powered Semi-Automatic Fine-Grained Parallelization on SMT Processors
---

# Accelerating Latency-Critical Applications with AI-Powered Semi-Automatic Fine-Grained Parallelization on SMT Processors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00883" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00883v1</a>
  <a href="https://arxiv.org/pdf/2509.00883.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00883v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00883v1', 'Accelerating Latency-Critical Applications with AI-Powered Semi-Automatic Fine-Grained Parallelization on SMT Processors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Denis Los, Igor Petushkov

**分类**: cs.DC, cs.AI

**发布日期**: 2025-08-31

**期刊**: International Journal of Open Information Technologies, vol. 13, no. 9, pp. 129-134, 2025

---

## 💡 一句话要点

**提出AI驱动的半自动细粒度并行化方法以提升延迟关键应用性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `延迟关键应用` `并行化` `AI技术` `动态依赖收集` `性能模拟` `SMT技术` `高性能计算`

## 📋 核心要点

1. 现有的延迟关键应用在高性能处理器中面临低功能单元利用率的问题，主要由于缓存未命中和错误预测。
2. 本文提出Aira，一个AI驱动的并行化顾问，结合了动态依赖收集和性能模拟技术，以实现细粒度并行化。
3. 通过与Relic框架结合，Aira在延迟关键基准测试中实现了17%的几何平均性能提升，展示了其有效性。

## 📝 摘要（中文）

延迟关键应用在高性能超标量处理器中由于频繁的缓存未命中和投机执行中的错误预测，往往导致功能单元的低利用率。尽管同时多线程(SMT)技术对单线程性能有显著影响，但在延迟关键应用的重线程中使用较少。本文探讨了利用SMT技术支持延迟关键应用的细粒度并行化。我们引入了Aira，一个AI驱动的并行化顾问，并通过Cursor IDE中的AI编码代理扩展了相关工具，形成了一个端到端的AI代理。通过动态二进制插桩收集动态依赖关系，并进行SMT感知性能模拟，Aira与Relic并行框架结合，实现了对延迟关键基准的并行化，最终展示了17%的几何平均性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决延迟关键应用在高性能超标量处理器中由于缓存未命中和投机执行错误预测导致的功能单元低利用率问题。现有方法在处理重线程时未能有效利用SMT技术。

**核心思路**：论文的核心思路是利用AI技术，特别是大型语言模型，来支持延迟关键应用的细粒度并行化。通过引入Aira，结合动态依赖收集和性能模拟，提升了并行化的效率和效果。

**技术框架**：整体架构包括Aira作为AI并行化顾问，Cursor IDE中的AI编码代理，以及通过模型上下文协议连接的多个工具。主要模块包括热点检测、动态依赖收集和SMT感知性能模拟。

**关键创新**：最重要的技术创新在于将AI与并行化结合，通过动态二进制插桩和性能模拟实现了对延迟关键应用的有效并行化。这与传统方法相比，显著提升了性能和资源利用率。

**关键设计**：关键设计包括动态依赖关系的收集方法、SMT感知性能模拟的实现，以及与Relic框架的集成，确保了细粒度任务并行化的有效性。

## 📊 实验亮点

实验结果显示，使用Aira与Relic框架对延迟关键基准进行并行化，最终实现了17%的几何平均性能提升。这一结果相较于传统方法具有显著的优势，展示了AI驱动的并行化在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括高性能计算、实时数据处理和工业自动化等场景，能够显著提升延迟关键应用的性能，具有广泛的实际价值。未来，随着AI技术的进一步发展，Aira可能会被应用于更多复杂的并行计算任务中，推动相关领域的进步。

## 📄 摘要（原文）

> Latency-critical applications tend to show low utilization of functional units due to frequent cache misses and mispredictions during speculative execution in high-performance superscalar processors. However, due to significant impact on single-thread performance, Simultaneous Multithreading (SMT) technology is rarely used with heavy threads of latency-critical applications. In this paper, we explore utilization of SMT technology to support fine-grained parallelization of latency-critical applications. Following the advancements in the development of Large Language Models (LLMs), we introduce Aira, an AI-powered Parallelization Adviser. To implement Aira, we extend AI Coding Agent in Cursor IDE with additional tools connected through Model Context Protocol, enabling end-to-end AI Agent for parallelization. Additional connected tools enable LLM-guided hotspot detection, collection of dynamic dependencies with Dynamic Binary Instrumentation, SMT-aware performance simulation to estimate performance gains. We apply Aira with Relic parallel framework for fine-grained task parallelism on SMT cores to parallelize latency-critical benchmarks representing real-world applications used in industry. We show 17% geomean performance gain from parallelization of latency-critical benchmarks using Aira with Relic framework.

