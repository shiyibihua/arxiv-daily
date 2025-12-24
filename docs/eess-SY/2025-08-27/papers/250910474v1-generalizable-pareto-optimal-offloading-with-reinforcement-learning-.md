---
layout: default
title: Generalizable Pareto-Optimal Offloading with Reinforcement Learning in Mobile Edge Computing
---

# Generalizable Pareto-Optimal Offloading with Reinforcement Learning in Mobile Edge Computing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10474" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10474v1</a>
  <a href="https://arxiv.org/pdf/2509.10474.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10474v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10474v1', 'Generalizable Pareto-Optimal Offloading with Reinforcement Learning in Mobile Edge Computing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ning Yang, Junrui Wen, Meng Zhang, Ming Tang

**分类**: eess.SY

**发布日期**: 2025-08-27

**备注**: 28 pages including appendix, 7 figures, 2 tables, accepted to IEEE Transactions on Services Computing

**🔗 代码/项目**: [GITHUB](https://github.com/gracefulning/Generalizable-Pareto-Optimal-Offloading-with-Reinforcement-Learning-in-Mobile-Edge-Computing)

---

## 💡 一句话要点

**提出基于强化学习的通用帕累托最优卸载框架以解决移动边缘计算问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `移动边缘计算` `多目标优化` `强化学习` `任务卸载` `深度学习` `能效` `延迟`

## 📋 核心要点

1. 现有的单目标调度方法无法有效处理移动边缘计算中多目标优化的问题，尤其是在偏好未知的情况下。
2. 本研究提出了一种基于通用多目标深度强化学习的卸载框架，能够适应不同的MEC系统并高效调度任务。
3. 实验结果表明，所提GMORL方案在超体积上较基线提升了121.0%，显示出显著的性能改进。

## 📝 摘要（中文）

移动边缘计算（MEC）是下一代移动网络应用的重要组成部分，需平衡延迟和能效等多种性能指标。然而，传统的单目标调度方案无法直接应用于实际系统，因为不同目标的权重往往未知或难以提前指定。本研究提出了一种多目标卸载问题的框架，旨在最小化预期的长期能耗和延迟，同时考虑未知的偏好。为此，我们提出了一种基于通用多目标深度强化学习（GMORL）的任务卸载框架，采用离散软演员-评论家（Discrete-SAC）方法。该方法利用单一策略模型高效调度任务，适应不同的MEC系统。通过引入直方图状态编码、复杂的奖励函数和新颖的神经网络架构，我们的GMORL方案在超体积上提升了高达121.0%。

## 🔬 方法详解

**问题定义**：本研究旨在解决移动边缘计算中的多目标卸载问题，尤其是在不同目标权重未知的情况下，传统方法难以适用。

**核心思路**：提出基于通用多目标深度强化学习的框架，通过单一策略模型适应不同的偏好和MEC系统，实现高效的任务调度。

**技术框架**：整体架构包括状态编码模块、奖励计算模块和策略学习模块。状态编码使用直方图方法，奖励函数精确计算延迟和能耗的效用。

**关键创新**：引入了直方图状态编码和复杂的奖励函数，提升了模型的泛化能力，与传统方法相比，能够更好地处理多目标优化问题。

**关键设计**：采用离散软演员-评论家（Discrete-SAC）方法，设计了适应性强的神经网络架构，优化了任务调度的效率和准确性。具体参数设置和损失函数设计在实验中进行了详细验证。

## 📊 实验亮点

实验结果显示，所提GMORL方案在超体积上较基线提升了121.0%，显著提高了多目标优化的效果，证明了该方法在实际应用中的有效性和优越性。

## 🎯 应用场景

该研究的成果可广泛应用于移动边缘计算领域，尤其是在智能手机、物联网设备和边缘服务器等场景中。通过优化任务卸载策略，可以有效提升系统的能效和响应速度，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Mobile edge computing (MEC) is essential for next-generation mobile network applications that prioritize various performance metrics, including delays and energy efficiency. However, conventional single-objective scheduling solutions cannot be directly applied to practical systems in which the preferences (i.e., the weights of different objectives) are often unknown or challenging to specify in advance. In this study, we formulate a multi-objective offloading problem for MEC with multiple edges to minimize the sum of expected long-term energy consumption and delay while considering unknown preferences. To address the challenge of unknown preferences and the potentially diverse MEC systems, we propose a generalizable multi-objective (deep) reinforcement learning (GMORL)-based tasks offloading framework, which employs the Discrete Soft Actor-Critic (Discrete-SAC) method. Our method uses a single policy model to efficiently schedule tasks based on varying preferences and adapt to heterogeneous MEC systems with different CPU frequencies and server quantities. Under the proposed framework, we introduce a histogram-based state encoding method for constructing features for multiple edges in MEC systems, a sophisticated reward function for accurately computing the utilities of delay and energy consumption, and a novel neural network architecture for improving generalization. Simulation results demonstrate that our proposed GMORL scheme enhances the hypervolume of the Pareto front by up to $121.0\%$ compared to benchmarks. Our code are avavilable at https://github.com/gracefulning/Generalizable-Pareto-Optimal-Offloading-with-Reinforcement-Learning-in-Mobile-Edge-Computing

