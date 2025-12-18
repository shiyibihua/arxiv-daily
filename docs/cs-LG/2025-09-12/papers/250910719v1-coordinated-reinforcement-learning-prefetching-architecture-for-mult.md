---
layout: default
title: Coordinated Reinforcement Learning Prefetching Architecture for Multicore Systems
---

# Coordinated Reinforcement Learning Prefetching Architecture for Multicore Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10719" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10719v1</a>
  <a href="https://arxiv.org/pdf/2509.10719.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10719v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10719v1', 'Coordinated Reinforcement Learning Prefetching Architecture for Multicore Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammed Humaid Siddiqui, Fernando Guzman, Yufei Wu, Ruishu Ann

**分类**: cs.DC, cs.AR, cs.LG, cs.PF

**发布日期**: 2025-09-12

**备注**: 47 pages, 12 figures, technical report prepared at Fairleigh Dickinson University

---

## 💡 一句话要点

**提出一种协同强化学习预取架构CRL-Pythia，解决多核系统中的冗余预取问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多核系统` `硬件预取` `强化学习` `协同学习` `性能优化`

## 📋 核心要点

1. 传统预取器在多核系统中面临冗余预取和性能下降的挑战，独立核心操作导致大量重复请求，浪费带宽。
2. CRL-Pythia通过跨核心信息共享和协同决策，减少冗余预取，加速学习收敛，提升多核系统预取效率。
3. 实验表明，CRL-Pythia优于单核Pythia配置，在带宽受限场景下IPC提升约12%，并具有良好的鲁棒性和可扩展性。

## 📝 摘要（中文）

硬件预取对于弥补CPU速度和较慢内存访问之间的性能差距至关重要。随着多核架构的普及，传统的预取器面临严峻挑战。独立的核心操作会产生显著的冗余（高达20%的预取请求是重复的），导致不必要的内存总线流量和带宽浪费。此外，诸如Pythia等先进的预取器在从单核扩展到四核系统时，性能会下降约10%。为了解决这些问题，我们提出了一种基于协同强化学习的预取器CRL-Pythia，专门为多核系统设计。CRL-Pythia通过启用跨核心的信息共享和协同预取决策来解决这些问题，从而大大减少了冗余预取请求，并提高了跨核心的学习收敛性。实验表明，CRL-Pythia在所有情况下都优于单Pythia配置，对于带宽受限的工作负载，IPC（每周期指令数）提高了约12%，同时硬件开销适中。敏感性分析也验证了其鲁棒性和可扩展性，从而使CRL-Pythia成为当代多核系统的一种实用且高效的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决多核系统中传统预取器由于核心独立运行而导致的冗余预取问题。现有预取器，如Pythia，在多核环境下性能下降，且产生大量重复的预取请求，造成内存带宽浪费。这些问题限制了多核系统的整体性能。

**核心思路**：论文的核心思路是利用协同强化学习，让多个核心的预取器共享信息并协同决策，从而减少冗余预取请求，提高预取精度。通过让各个核心的预取器相互学习，可以避免重复的预取操作，并更好地适应多核系统的复杂访问模式。

**技术框架**：CRL-Pythia的整体架构包括多个核心的预取器，每个预取器基于强化学习算法（Pythia）。关键在于引入了跨核心的信息共享机制，允许各个核心的预取器交换状态信息和预取决策。此外，还设计了协同决策机制，使得各个核心的预取器可以共同决定是否进行预取操作。

**关键创新**：CRL-Pythia的关键创新在于将协同强化学习应用于多核系统的预取问题。与传统的独立预取器相比，CRL-Pythia能够利用跨核心的信息，避免冗余预取，提高预取效率。此外，协同决策机制使得各个核心的预取器能够更好地协调工作，从而提高整体性能。

**关键设计**：具体的技术细节包括：(1) 状态表示：每个核心的预取器维护一个状态向量，用于描述当前核心的访问模式。(2) 奖励函数：奖励函数的设计旨在鼓励预取器进行准确的预取，并惩罚冗余的预取。(3) 协同机制：各个核心的预取器通过共享状态信息和预取决策来协同工作。具体的协同策略可以根据实际情况进行调整。

## 📊 实验亮点

实验结果表明，CRL-Pythia在所有测试场景下均优于单核Pythia配置。对于带宽受限的工作负载，CRL-Pythia的IPC（每周期指令数）提升了约12%。此外，敏感性分析验证了CRL-Pythia的鲁棒性和可扩展性，表明其能够适应不同的系统配置和工作负载，具有良好的实用价值。

## 🎯 应用场景

CRL-Pythia适用于各种多核处理器系统，尤其是在内存带宽受限的应用场景下，如高性能计算、服务器和嵌入式系统。通过减少冗余预取，可以有效提升系统性能和能效，降低内存访问延迟，从而改善用户体验。该研究成果对于提升多核系统的整体性能具有重要的实际价值和潜在影响。

## 📄 摘要（原文）

> Hardware prefetching is critical to fill the performance gap between CPU speeds and slower memory accesses. With multicore architectures becoming commonplace, traditional prefetchers are severely challenged. Independent core operation creates significant redundancy (up to 20% of prefetch requests are duplicates), causing unnecessary memory bus traffic and wasted bandwidth. Furthermore, cutting-edge prefetchers such as Pythia suffer from about a 10% performance loss when scaling from a single-core to a four-core system. To solve these problems, we propose CRL-Pythia, a coordinated reinforcement learning based prefetcher specifically designed for multicore systems. In this work, CRL-Pythia addresses these issues by enabling cross-core sharing of information and cooperative prefetching decisions, which greatly reduces redundant prefetch requests and improves learning convergence across cores. Our experiments demonstrate that CRL-Pythia outperforms single Pythia configurations in all cases, with approximately 12% IPC (instructions per cycle) improvement for bandwidth-constrained workloads, while imposing moderate hardware overhead. Our sensitivity analyses also verify its robustness and scalability, thereby making CRL-Pythia a practical and efficient solution to contemporary multicore systems.

