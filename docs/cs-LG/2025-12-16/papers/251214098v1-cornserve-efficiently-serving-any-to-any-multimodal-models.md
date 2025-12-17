---
layout: default
title: Cornserve: Efficiently Serving Any-to-Any Multimodal Models
---

# Cornserve: Efficiently Serving Any-to-Any Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14098" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14098v1</a>
  <a href="https://arxiv.org/pdf/2512.14098.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14098v1" onclick="toggleFavorite(this, '2512.14098v1', 'Cornserve: Efficiently Serving Any-to-Any Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeff J. Ma, Jae-Won Chung, Jisang Ahn, Yizhuo Liang, Akshay Jajoo, Myungjin Lee, Mosharaf Chowdhury

**分类**: cs.LG, cs.DC

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**Cornserve：高效服务任意到任意多模态模型的在线服务系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型服务` `Any-to-Any模型` `模型部署优化` `分布式系统` `计算图`

## 📋 核心要点

1. 现有模型服务系统难以有效处理Any-to-Any多模态模型的异构性，包括请求类型、计算路径和计算规模的差异。
2. Cornserve的核心思想是允许开发者描述模型的计算图，并自动规划和执行优化的模型部署方案，以适应异构性。
3. 实验结果表明，Cornserve在吞吐量和尾部延迟方面显著优于现有解决方案，验证了其高效服务Any-to-Any模型的能力。

## 📝 摘要（中文）

本文提出了Cornserve，一个高效的在线服务系统，专门针对新兴的任意到任意（Any-to-Any）多模态模型。这类模型接受文本和多模态数据（例如，图像、视频、音频）的组合作为输入，并生成文本和多模态数据的组合作为输出，这导致了模型服务中请求类型、计算路径和计算规模的异构性。Cornserve允许模型开发者描述通用Any-to-Any模型的计算图，该计算图由异构组件组成，例如多模态编码器、大型语言模型（LLM）等自回归模型以及扩散Transformer（DiT）等多模态生成器。在此基础上，Cornserve的规划器自动为模型找到优化的部署方案，包括是否以及如何基于模型和工作负载特征将模型分解为更小的组件。然后，Cornserve的分布式运行时按照该方案执行模型，从而在在线服务期间有效地处理Any-to-Any模型的异构性。评估表明，Cornserve可以高效地服务各种Any-to-Any模型和工作负载，与现有解决方案相比，吞吐量提高了3.81倍，尾部延迟降低了5.79倍。

## 🔬 方法详解

**问题定义**：现有模型服务系统在处理Any-to-Any多模态模型时面临挑战，这些模型具有复杂的输入输出组合，导致计算路径和资源需求高度异构。传统的模型服务方法难以有效地处理这种异构性，导致资源利用率低、延迟高。

**核心思路**：Cornserve的核心思路是解耦模型定义和部署执行。它允许模型开发者以计算图的形式描述模型的结构，然后由系统自动规划和优化模型的部署方案。这种解耦使得系统能够根据模型和工作负载的特性，灵活地调整模型的部署方式，从而更好地适应异构性。

**技术框架**：Cornserve包含两个主要组件：规划器（Planner）和分布式运行时（Distributed Runtime）。规划器负责分析模型的计算图和工作负载特征，生成优化的部署方案，包括模型分解、组件放置和资源分配等。分布式运行时则按照规划器生成的方案执行模型，负责请求调度、数据传输和计算执行等。

**关键创新**：Cornserve的关键创新在于其自动化的模型部署规划能力。它能够根据模型和工作负载的特性，动态地调整模型的部署方式，从而更好地适应Any-to-Any模型的异构性。此外，Cornserve还支持将模型分解为更小的组件，并根据需要将这些组件部署到不同的计算资源上，从而实现更细粒度的资源管理。

**关键设计**：Cornserve的规划器使用基于成本模型的优化算法来生成部署方案。该成本模型考虑了模型的计算复杂度、数据传输开销和资源可用性等因素。分布式运行时使用基于消息传递的通信机制来实现组件之间的协同工作。此外，Cornserve还支持动态调整资源分配，以适应工作负载的变化。

## 📊 实验亮点

实验结果表明，Cornserve在服务各种Any-to-Any模型和工作负载时表现出色。与现有解决方案相比，Cornserve实现了高达3.81倍的吞吐量提升和高达5.79倍的尾部延迟降低。这些结果验证了Cornserve在处理多模态模型异构性方面的有效性，并展示了其在实际应用中的潜力。

## 🎯 应用场景

Cornserve适用于需要处理复杂多模态输入输出的各种应用场景，例如智能客服、多模态内容生成、跨模态检索等。它可以帮助开发者更高效地部署和运行Any-to-Any模型，从而加速这些应用的开发和落地。未来，Cornserve可以进一步扩展到支持更多的模型类型和计算平台，并提供更强大的自动化优化能力。

## 📄 摘要（原文）

> We present Cornserve, an efficient online serving system for an emerging class of multimodal models called Any-to-Any models. Any-to-Any models accept combinations of text and multimodal data (e.g., image, video, audio) as input and also generate combinations of text and multimodal data as output, introducing request type, computation path, and computation scaling heterogeneity in model serving.
>   Cornserve allows model developers to describe the computation graph of generic Any-to-Any models, which consists of heterogeneous components such as multimodal encoders, autoregressive models like Large Language Models (LLMs), and multimodal generators like Diffusion Transformers (DiTs). Given this, Cornserve's planner automatically finds an optimized deployment plan for the model, including whether and how to disaggregate the model into smaller components based on model and workload characteristics. Cornserve's distributed runtime then executes the model per the plan, efficiently handling Any-to-Any model heterogeneity during online serving. Evaluations show that Cornserve can efficiently serve diverse Any-to-Any models and workloads, delivering up to 3.81$\times$ throughput improvement and up to 5.79$\times$ tail latency reduction over existing solutions.

