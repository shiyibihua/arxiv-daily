---
layout: default
title: Improving Drone Racing Performance Through Iterative Learning MPC
---

# Improving Drone Racing Performance Through Iterative Learning MPC

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01103" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01103v3</a>
  <a href="https://arxiv.org/pdf/2508.01103.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01103v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01103v3', 'Improving Drone Racing Performance Through Iterative Learning MPC')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haocheng Zhao, Niklas Schlüter, Lukas Brunke, Angela P. Schoellig

**分类**: cs.RO, eess.SY

**发布日期**: 2025-08-01 (更新: 2025-09-21)

**备注**: Accepted for oral presentation at IROS 2025

---

## 💡 一句话要点

**通过迭代学习MPC提升无人机竞速性能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `无人机竞速` `模型预测控制` `迭代学习` `动态系统` `实时决策` `安全控制` `性能优化`

## 📋 核心要点

1. 现有的迭代学习模型预测控制在无人机竞速中面临实时性和安全性之间的权衡，难以直接应用。
2. 论文提出通过自适应成本函数、偏移局部安全集和笛卡尔坐标表达方式来增强LMPC，解决实时控制问题。
3. 实验结果显示，改进算法在多种控制器上优化初始轨迹，圈速提升最高达60.85%，在实际应用中也有显著改善。

## 📝 摘要（中文）

自主无人机竞速是一个复杂的控制问题，要求实时决策和对非线性系统动态的稳健处理。尽管迭代学习模型预测控制（LMPC）为性能迭代提升提供了有前景的框架，但其在无人机竞速中的直接应用面临实时兼容性和时间最优与安全通行之间的权衡等挑战。本文通过三项关键创新增强了LMPC：1）自适应成本函数动态权衡时间最优跟踪与中心线遵循，2）偏移局部安全集以防止过度捷径并实现更稳健的迭代更新，3）基于笛卡尔坐标的表达方式，避免了Frenet框架变换带来的奇异性或积分误差。大量仿真和实地实验结果表明，改进后的算法能够优化由多种控制器生成的初始轨迹，最大提升圈速达60.85%。即使在最激进调优的最先进模型基础控制器MPCC++上，实际无人机仍实现了6.05%的提升。总体而言，该方法推动无人机更快通行并避免碰撞，成为提升无人机竞速峰值性能的实用解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决无人机竞速中迭代学习模型预测控制（LMPC）在实时性和安全性之间的权衡问题。现有方法在处理非线性动态时存在实时兼容性不足和安全性保障不足的痛点。

**核心思路**：通过引入自适应成本函数、偏移局部安全集和笛卡尔坐标系的表达方式，论文旨在提升LMPC在无人机竞速中的应用效果，确保在追求时间最优的同时保障安全性。

**技术框架**：整体架构包括三个主要模块：自适应成本函数模块、局部安全集模块和笛卡尔坐标转换模块。自适应成本函数根据实时情况动态调整权重，局部安全集确保无人机在迭代更新中不发生过度捷径，而笛卡尔坐标转换则避免了传统方法的奇异性问题。

**关键创新**：论文的关键创新在于自适应成本函数和偏移局部安全集的结合，这一设计使得算法在保证安全的前提下，能够更有效地进行实时决策，显著提升了无人机的竞速性能。

**关键设计**：在参数设置上，成本函数的动态权重根据实时反馈进行调整，局部安全集的构建则基于当前状态和历史轨迹。此外，笛卡尔坐标系的使用避免了Frenet框架中的积分误差，确保了控制的精确性。

## 📊 实验亮点

实验结果表明，改进后的算法在多种控制器上优化初始轨迹，圈速提升最高达60.85%。即使在最先进的MPCC++控制器上，实际无人机也实现了6.05%的性能提升，显示出该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括无人机竞速、自动驾驶和其他需要实时决策的动态系统。通过提升无人机的控制性能，能够在竞速赛事中实现更高的效率和安全性，未来可能推动无人机技术在商业和娱乐领域的广泛应用。

## 📄 摘要（原文）

> Autonomous drone racing presents a challenging control problem, requiring real-time decision-making and robust handling of nonlinear system dynamics. While iterative learning model predictive control (LMPC) offers a promising framework for iterative performance improvement, its direct application to drone racing faces challenges like real-time compatibility or the trade-off between time-optimal and safe traversal. In this paper, we enhance LMPC with three key innovations: (1) an adaptive cost function that dynamically weights time-optimal tracking against centerline adherence, (2) a shifted local safe set to prevent excessive shortcutting and enable more robust iterative updates, and (3) a Cartesian-based formulation that accommodates safety constraints without the singularities or integration errors associated with Frenet-frame transformations. Results from extensive simulation and real-world experiments demonstrate that our improved algorithm can optimize initial trajectories generated by a wide range of controllers with varying levels of tuning for a maximum improvement in lap time by 60.85%. Even applied to the most aggressively tuned state-of-the-art model-based controller, MPCC++, on a real drone, a 6.05% improvement is still achieved. Overall, the proposed method pushes the drone toward faster traversal and avoids collisions in simulation and real-world experiments, making it a practical solution to improve the peak performance of drone racing.

