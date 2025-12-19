---
layout: default
title: Staggered Batch Scheduling: Co-optimizing Time-to-First-Token and Throughput for High-Efficiency LLM Inference
---

# Staggered Batch Scheduling: Co-optimizing Time-to-First-Token and Throughput for High-Efficiency LLM Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16134" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16134v1</a>
  <a href="https://arxiv.org/pdf/2512.16134.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16134v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16134v1', 'Staggered Batch Scheduling: Co-optimizing Time-to-First-Token and Throughput for High-Efficiency LLM Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jian Tian, Shuailong Li, Yang Cao, Wenbo Cui, Minghan Zhu, Wenkang Wu, Jianming Zhang, Yanpeng Wang, Zhiwen Xiao, Zhenyu Hou, Dou Shen

**分类**: cs.DC, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出交错批调度(SBS)，优化DP+EP架构下LLM推理的首Token延迟和吞吐量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `分布式推理` `调度算法` `首Token延迟` `吞吐量优化`

## 📋 核心要点

1. DP+EP架构的LLM服务中，立即调度请求导致引擎内排队和并行化气泡，严重影响首Token延迟。
2. 提出交错批调度（SBS），通过缓冲请求形成最佳批次，消除内部排队，并利用调度窗口进行负载均衡。
3. 在生产H800集群上，SBS将Deepseek-V3的TTFT降低30%-40%，吞吐量提升15%-20%。

## 📝 摘要（中文）

大型语言模型（LLM）服务正朝着复杂的分布式架构发展，特别是P/D分离的大规模DP+EP范式，这带来了独特的调度挑战。与传统部署中调度器将实例视为黑盒不同，DP+EP架构表现出较高的内部同步成本。我们发现，在此类系统中立即分发请求会导致严重的引擎内排队和并行化气泡，从而降低首Token延迟（TTFT）。为了解决这个问题，我们提出了交错批调度（SBS），这是一种有意缓冲请求以形成最佳执行批次的机制。这种时间解耦消除了内部排队气泡，而不会影响吞吐量。此外，利用缓冲创建的调度窗口，我们引入了一种负载感知全局分配策略，用于平衡Prefill和Decode阶段跨DP单元的计算负载。在服务Deepseek-V3的生产H800集群上部署后，与最先进的即时调度基线相比，我们的系统将TTFT降低了30%-40%，并将吞吐量提高了15%-20%。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模分布式LLM服务中，特别是采用DP+EP架构时，由于内部同步成本高昂，导致的首Token延迟（TTFT）过高以及吞吐量受限的问题。现有方法通常采用立即调度策略，忽略了DP+EP架构的特殊性，导致引擎内部出现排队和并行化气泡，降低了效率。

**核心思路**：论文的核心思路是引入时间上的解耦，通过交错批调度（SBS）机制，有意缓冲请求，形成更优的执行批次。这样可以避免立即调度带来的内部排队问题，同时利用缓冲窗口，进行全局的负载感知分配，平衡不同DP单元的计算负载。

**技术框架**：SBS包含两个主要部分：请求缓冲和负载感知全局分配。首先，请求会被缓冲一段时间，形成批次。然后，利用缓冲窗口，采用负载感知的全局分配策略，将批次分配到不同的DP单元上，以平衡计算负载。整个流程旨在最小化TTFT，同时最大化吞吐量。

**关键创新**：论文的关键创新在于将调度策略从“立即调度”转变为“交错批调度”，并结合负载感知的全局分配。这种方法充分考虑了DP+EP架构的内部同步成本，通过时间上的解耦，避免了内部排队和并行化气泡。与现有方法相比，SBS能够更有效地利用计算资源，提高LLM服务的效率。

**关键设计**：SBS的关键设计包括缓冲窗口的大小、批次形成策略以及负载感知的全局分配算法。缓冲窗口的大小需要根据实际的系统负载和请求到达率进行调整，以平衡TTFT和吞吐量。负载感知的全局分配算法需要考虑不同DP单元的计算能力和当前负载，以实现最佳的负载均衡。具体的损失函数和网络结构（如果涉及）在论文中未明确说明，属于未知细节。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16134v1/figures/schedule_unit_1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16134v1/figures/schedule_unit_2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16134v1/figures/queue_1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在生产H800集群上，与最先进的即时调度基线相比，SBS将Deepseek-V3的TTFT降低了30%-40%，并将吞吐量提高了15%-20%。这些数据表明SBS在实际应用中具有显著的性能优势，能够有效提升LLM服务的效率。

## 🎯 应用场景

该研究成果可应用于大规模分布式LLM服务，特别是在需要高并发和低延迟的场景下，如在线客服、智能助手、实时翻译等。通过优化调度策略，可以显著提升LLM服务的用户体验和资源利用率，降低运营成本，并为更复杂的LLM应用提供支持。

## 📄 摘要（原文）

> The evolution of Large Language Model (LLM) serving towards complex, distributed architectures--specifically the P/D-separated, large-scale DP+EP paradigm--introduces distinct scheduling challenges. Unlike traditional deployments where schedulers can treat instances as black boxes, DP+EP architectures exhibit high internal synchronization costs. We identify that immediate request dispatching in such systems leads to severe in-engine queuing and parallelization bubbles, degrading Time-to-First-Token (TTFT). To address this, we propose Staggered Batch Scheduling (SBS), a mechanism that deliberately buffers requests to form optimal execution batches. This temporal decoupling eliminates internal queuing bubbles without compromising throughput. Furthermore, leveraging the scheduling window created by buffering, we introduce a Load-Aware Global Allocation strategy that balances computational load across DP units for both Prefill and Decode phases. Deployed on a production H800 cluster serving Deepseek-V3, our system reduces TTFT by 30%-40% and improves throughput by 15%-20% compared to state-of-the-art immediate scheduling baselines.

