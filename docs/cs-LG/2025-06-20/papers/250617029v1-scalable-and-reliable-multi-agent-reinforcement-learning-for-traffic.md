---
layout: default
title: Scalable and Reliable Multi-agent Reinforcement Learning for Traffic Assignment
---

# Scalable and Reliable Multi-agent Reinforcement Learning for Traffic Assignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17029" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17029v1</a>
  <a href="https://arxiv.org/pdf/2506.17029.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17029v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17029v1', 'Scalable and Reliable Multi-agent Reinforcement Learning for Traffic Assignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leizhen Wang, Peibo Duan, Cheng Lyu, Zewen Wang, Zhiqiang He, Nan Zheng, Zhenliang Ma

**分类**: cs.LG

**发布日期**: 2025-06-20

**DOI**: [10.1016/j.commtr.2025.100225](https://doi.org/10.1016/j.commtr.2025.100225)

---

## 💡 一句话要点

**提出MARL-OD-DA以解决大规模交通分配问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `交通分配` `可扩展性` `可靠性` `城市交通管理`

## 📋 核心要点

1. 现有的多智能体强化学习方法在处理大规模交通分配问题时，面临可扩展性和可靠性不足的挑战。
2. 本文提出的MARL-OD-DA框架通过将智能体定义为OD对路由器，显著提升了系统的可扩展性和效率。
3. 实验结果显示，MARL-OD-DA在SiouxFalls网络中实现了更优的分配解决方案，相对差距显著低于传统方法。

## 📝 摘要（中文）

随着大城市的发展和出行需求的增加，交通分配方法面临严格的要求。多智能体强化学习（MARL）方法在建模自适应路由行为方面优于传统方法，但在处理大规模网络时面临可扩展性和可靠性挑战。为此，本文提出了MARL-OD-DA框架，将智能体重新定义为起点-终点（OD）对路由器，显著提高了可扩展性。同时，设计了基于Dirichlet的动作空间和基于局部相对差距的奖励函数，以增强解决方案的可靠性和收敛效率。实验表明，该框架在处理中等规模网络时表现优异，尤其是在SiouxFalls网络中，相较于传统方法，分配解决方案的相对差距降低了94.99%。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模交通分配中的可扩展性和可靠性问题。现有的MARL方法在处理复杂网络时，往往无法有效应对大量出行需求，限制了其实际应用。

**核心思路**：通过将智能体重新定义为起点-终点（OD）对路由器，而非单个旅行者，来提升系统的可扩展性。同时，设计了基于Dirichlet的动作空间和局部相对差距的奖励函数，以提高解决方案的可靠性和收敛速度。

**技术框架**：MARL-OD-DA框架包括多个模块，首先是OD对的定义与建模，其次是动作空间的构建，最后是基于奖励函数的学习与优化。整体流程通过多智能体协作来实现高效的交通分配。

**关键创新**：最重要的创新在于将智能体的定义从个体旅行者转变为OD对路由器，这一设计显著提高了系统的可扩展性和适应性，与传统方法相比，能够更好地处理大规模交通网络。

**关键设计**：在动作空间设计中，采用了Dirichlet分布进行动作修剪，以减少不必要的计算。同时，奖励函数基于局部相对差距进行设计，旨在引导智能体更快收敛到最优解。

## 📊 实验亮点

在SiouxFalls网络的实验中，MARL-OD-DA框架在10步内实现了更优的交通分配解决方案，其相对差距比传统方法低94.99%。这一结果表明，所提出的方法在处理复杂交通网络时具有显著的优势。

## 🎯 应用场景

该研究的潜在应用领域包括城市交通管理、智能交通系统和自动驾驶车辆的路径规划等。通过提高交通分配的效率和可靠性，MARL-OD-DA框架能够为城市交通流量的优化提供重要支持，具有显著的实际价值和未来影响。

## 📄 摘要（原文）

> The evolution of metropolitan cities and the increase in travel demands impose stringent requirements on traffic assignment methods. Multi-agent reinforcement learning (MARL) approaches outperform traditional methods in modeling adaptive routing behavior without requiring explicit system dynamics, which is beneficial for real-world deployment. However, MARL frameworks face challenges in scalability and reliability when managing extensive networks with substantial travel demand, which limiting their practical applicability in solving large-scale traffic assignment problems. To address these challenges, this study introduces MARL-OD-DA, a new MARL framework for the traffic assignment problem, which redefines agents as origin-destination (OD) pair routers rather than individual travelers, significantly enhancing scalability. Additionally, a Dirichlet-based action space with action pruning and a reward function based on the local relative gap are designed to enhance solution reliability and improve convergence efficiency. Experiments demonstrate that the proposed MARL framework effectively handles medium-sized networks with extensive and varied city-level OD demand, surpassing existing MARL methods. When implemented in the SiouxFalls network, MARL-OD-DA achieves better assignment solutions in 10 steps, with a relative gap that is 94.99% lower than that of conventional methods.

