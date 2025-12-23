---
layout: default
title: Research on Model Parallelism and Data Parallelism Optimization Methods in Large Language Model-Based Recommendation Systems
---

# Research on Model Parallelism and Data Parallelism Optimization Methods in Large Language Model-Based Recommendation Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17551" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17551v2</a>
  <a href="https://arxiv.org/pdf/2506.17551.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17551v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17551v2', 'Research on Model Parallelism and Data Parallelism Optimization Methods in Large Language Model-Based Recommendation Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haowei Yang, Yu Tian, Zhongheng Yang, Zhao Wang, Chengrui Zhou, Dannier Li

**分类**: cs.DC, cs.AI

**发布日期**: 2025-06-21 (更新: 2025-06-24)

---

## 💡 一句话要点

**提出模型并行与数据并行优化方法以解决推荐系统中的计算瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推荐系统` `模型并行` `数据并行` `优化方法` `分布式训练` `负载均衡` `梯度压缩`

## 📋 核心要点

1. 现有推荐系统在使用大型语言模型时面临计算和通信瓶颈，影响训练效率。
2. 提出模型并行和数据并行的混合优化方案，通过自适应负载均衡和高效通信框架提升性能。
3. 实验结果显示，混合并行方案训练吞吐量提升超过30%，资源利用率提高约20%。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在推荐系统中的快速应用，其庞大的参数规模和数据量导致的计算与通信瓶颈日益突出。本文系统研究了两类优化方法——模型并行和数据并行——在推荐场景下的分布式训练。针对模型并行，我们实现了张量并行和流水线并行，并引入自适应负载均衡机制以减少跨设备通信开销。对于数据并行，我们比较了同步与异步模式，结合梯度压缩和稀疏化技术，构建了高效的聚合通信框架，以显著提高带宽利用率。在真实推荐数据集的实验中，我们提出的混合并行方案相比传统单一模式并行提高了30%以上的训练吞吐量，并改善了约20%的资源利用率，同时保持了良好的可扩展性和鲁棒性。最后，我们讨论了在线部署中不同并行策略的权衡，并概述了未来在异构硬件集成和自动调度技术方面的研究方向。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在推荐系统中训练时的计算与通信瓶颈问题。现有方法在处理庞大参数和数据时，往往导致资源利用率低下，训练效率不高。

**核心思路**：通过结合模型并行和数据并行的优化策略，设计出一种混合并行方案，以提高训练效率和资源利用率。模型并行通过张量和流水线并行化来分散计算负载，而数据并行则通过优化通信方式来提升带宽利用。

**技术框架**：整体架构包括模型并行和数据并行两个主要模块。模型并行实现张量并行和流水线并行，并引入自适应负载均衡机制；数据并行则比较同步与异步模式，结合梯度压缩和稀疏化技术，构建高效的聚合通信框架。

**关键创新**：最重要的技术创新在于提出了自适应负载均衡机制，显著减少了跨设备通信开销，同时结合了梯度压缩与稀疏化技术，提升了数据并行的效率。这些创新使得混合并行方案在性能上优于传统单一模式。

**关键设计**：在模型并行中，采用了张量分割和流水线处理的策略；在数据并行中，设计了高效的聚合通信框架，并使用了梯度压缩和稀疏化技术来优化数据传输，确保了训练过程中的高效性和稳定性。

## 📊 实验亮点

实验结果表明，提出的混合并行方案在真实推荐数据集上训练吞吐量提高超过30%，资源利用率提升约20%。与传统单一模式并行相比，混合方案在可扩展性和鲁棒性方面表现优异，显示出更强的适应性和效率。

## 🎯 应用场景

该研究的潜在应用领域包括电商推荐、社交媒体内容推荐以及个性化广告投放等。通过优化大型语言模型的训练效率，能够显著提升推荐系统的响应速度和用户体验，具有重要的实际价值和广泛的应用前景。未来，随着异构硬件的集成和自动调度技术的发展，该研究成果有望进一步推动推荐系统的智能化进程。

## 📄 摘要（原文）

> With the rapid adoption of large language models (LLMs) in recommendation systems, the computational and communication bottlenecks caused by their massive parameter sizes and large data volumes have become increasingly prominent. This paper systematically investigates two classes of optimization methods-model parallelism and data parallelism-for distributed training of LLMs in recommendation scenarios. For model parallelism, we implement both tensor parallelism and pipeline parallelism, and introduce an adaptive load-balancing mechanism to reduce cross-device communication overhead. For data parallelism, we compare synchronous and asynchronous modes, combining gradient compression and sparsification techniques with an efficient aggregation communication framework to significantly improve bandwidth utilization. Experiments conducted on a real-world recommendation dataset in a simulated service environment demonstrate that our proposed hybrid parallelism scheme increases training throughput by over 30% and improves resource utilization by approximately 20% compared to traditional single-mode parallelism, while maintaining strong scalability and robustness. Finally, we discuss trade-offs among different parallel strategies in online deployment and outline future directions involving heterogeneous hardware integration and automated scheduling technologies.

