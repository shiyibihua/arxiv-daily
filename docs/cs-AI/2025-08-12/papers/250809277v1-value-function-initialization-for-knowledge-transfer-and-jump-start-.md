---
layout: default
title: Value Function Initialization for Knowledge Transfer and Jump-start in Deep Reinforcement Learning
---

# Value Function Initialization for Knowledge Transfer and Jump-start in Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09277" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09277v1</a>
  <a href="https://arxiv.org/pdf/2508.09277.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09277v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09277v1', 'Value Function Initialization for Knowledge Transfer and Jump-start in Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Soumia Mehimeh

**分类**: cs.AI, cs.LG, cs.LO

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出DQInit以解决深度强化学习中的价值函数初始化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

## 📋 核心要点

1. 现有的价值函数初始化方法在深度强化学习中面临挑战，包括状态-动作空间的连续性和神经网络的噪声近似。
2. 本文提出DQInit，通过重用紧凑的表格Q值，结合已知度机制，将转移值柔和整合到学习过程中。
3. 实验结果显示，DQInit在多个任务中提升了学习效率和稳定性，相较于标准初始化和现有转移技术表现更佳。

## 📝 摘要（中文）

价值函数初始化（VFI）是一种有效的强化学习（RL）跳启动方法，通过利用先前任务的价值估计来加速学习。尽管在表格设置中该方法已得到广泛应用，但在深度强化学习（DRL）中，由于状态-动作空间的连续性、神经网络的噪声近似以及存储所有过去模型的实际困难，扩展此方法面临挑战。本文提出DQInit，适应性地将价值函数初始化应用于DRL，重用从已解决任务中提取的紧凑表格Q值作为可转移知识库。该方法采用基于已知度的机制，将这些转移值柔和地整合到未充分探索的区域，并逐渐向智能体的学习估计转移，避免了固定时间衰减的局限性。实验结果表明，DQInit在多个连续控制任务中显著提高了早期学习效率、稳定性和整体性能。

## 🔬 方法详解

**问题定义**：本文旨在解决深度强化学习中价值函数初始化的挑战，现有方法在处理连续状态-动作空间时效果不佳，且无法有效利用过去的知识。

**核心思路**：DQInit通过重用已解决任务的紧凑表格Q值，构建可转移的知识库，并采用基于已知度的机制将这些值整合到智能体的学习过程中，逐步向智能体的学习估计过渡。

**技术框架**：DQInit的整体架构包括知识库的构建、已知度机制的应用以及价值函数的动态调整。首先提取已解决任务的Q值，然后根据智能体的探索情况动态调整这些值。

**关键创新**：DQInit的主要创新在于仅依赖价值估计而非策略或示范进行知识转移，这种方法有效结合了跳启动强化学习和策略蒸馏的优点，同时克服了它们的缺陷。

**关键设计**：在DQInit中，关键设计包括如何提取和存储Q值、已知度机制的具体实现，以及如何动态调整转移值以适应智能体的学习进程。

## 📄 摘要（原文）

> Value function initialization (VFI) is an effective way to achieve a jumpstart in reinforcement learning (RL) by leveraging value estimates from prior tasks. While this approach is well established in tabular settings, extending it to deep reinforcement learning (DRL) poses challenges due to the continuous nature of the state-action space, the noisy approximations of neural networks, and the impracticality of storing all past models for reuse. In this work, we address these challenges and introduce DQInit, a method that adapts value function initialization to DRL. DQInit reuses compact tabular Q-values extracted from previously solved tasks as a transferable knowledge base. It employs a knownness-based mechanism to softly integrate these transferred values into underexplored regions and gradually shift toward the agent's learned estimates, avoiding the limitations of fixed time decay. Our approach offers a novel perspective on knowledge transfer in DRL by relying solely on value estimates rather than policies or demonstrations, effectively combining the strengths of jumpstart RL and policy distillation while mitigating their drawbacks. Experiments across multiple continuous control tasks demonstrate that DQInit consistently improves early learning efficiency, stability, and overall performance compared to standard initialization and existing transfer techniques.

