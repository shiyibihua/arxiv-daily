---
layout: default
title: Semi-Infinite Programming for Collision-Avoidance in Optimal and Model Predictive Control
---

# Semi-Infinite Programming for Collision-Avoidance in Optimal and Model Predictive Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12335" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12335v1</a>
  <a href="https://arxiv.org/pdf/2508.12335.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12335v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12335v1', 'Semi-Infinite Programming for Collision-Avoidance in Optimal and Model Predictive Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunfan Gao, Florian Messerer, Niels van Duijkeren, Rashmi Dabir, Moritz Diehl

**分类**: cs.RO, eess.SY

**发布日期**: 2025-08-17

**备注**: 21 pages, 15 figures

---

## 💡 一句话要点

**提出半无限规划方法以解决最优与模型预测控制中的避碰问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `避碰控制` `半无限规划` `模型预测控制` `机器人导航` `不确定性处理`

## 📋 核心要点

1. 现有的避碰方法在处理复杂环境时面临约束数量无限的问题，导致计算效率低下。
2. 本文提出通过局部简化和外部活动集方法结合的方式，有效解决半无限规划中的避碰约束。
3. 实验结果表明，所提出的方法在实际机器人上实现了20Hz的快速无碰撞导航，且在3D仿真中表现良好。

## 📝 摘要（中文）

本文提出了一种新颖的方法用于最优控制和模型预测控制中的避碰问题，其中环境通过大量点表示，机器人则作为一组填充多边形的联合。避免碰撞的条件可以用每个障碍点的无限数量约束来表示。我们展示了如何通过局部简化和外部活动集方法的结合高效地解决由此产生的半无限规划最优控制问题。此外，本文还考虑了在椭球状态不确定性下的稳健避碰，确保在所有可能的不确定性实现下满足约束，从而扩展了约束的无限维度。基于所提出的方法实现的控制器在实际机器人上以20Hz运行，能够在狭小空间中快速且无碰撞地导航，同时在仿真中展示了3D避碰的应用。

## 🔬 方法详解

**问题定义**：本文旨在解决最优控制和模型预测控制中的避碰问题，现有方法在处理复杂环境时面临约束数量无限的问题，导致计算效率低下。

**核心思路**：论文提出通过局部简化和外部活动集方法的结合，有效处理半无限规划中的避碰约束。具体而言，方法通过迭代识别最近的障碍点，确定所有可行机器人形状参数中的下层距离最小化器，并解决上层有限约束子问题。

**技术框架**：整体架构包括两个主要模块：局部简化模块和外部活动集方法模块。局部简化模块负责处理来自平移不确定性的无限约束，而外部活动集方法则用于解决有限约束子问题。

**关键创新**：最重要的技术创新点在于将局部简化与机器人形状参数化结合，处理来自不确定性的无限约束，尤其是通过回退重构来应对旋转不确定性。这与现有方法的本质区别在于更高效地处理了约束的复杂性。

**关键设计**：在设计中，关键参数设置包括障碍点的选择策略和机器人形状的参数化方式，损失函数则侧重于最小化距离，同时确保约束的满足。

## 📊 实验亮点

实验结果显示，基于所提出的方法的控制器在实际机器人上以20Hz的频率运行，成功实现了快速且无碰撞的导航。此外，在3D仿真中也展示了良好的避碰性能，显著提升了机器人在复杂环境中的适应能力。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、工业机器人和服务机器人等，能够在复杂和动态环境中实现安全导航。其实际价值在于提高机器人在狭小空间中的操作能力，未来可能推动智能机器人在更多领域的应用。

## 📄 摘要（原文）

> This paper presents a novel approach for collision avoidance in optimal and model predictive control, in which the environment is represented by a large number of points and the robot as a union of padded polygons. The conditions that none of the points shall collide with the robot can be written in terms of an infinite number of constraints per obstacle point. We show that the resulting semi-infinite programming (SIP) optimal control problem (OCP) can be efficiently tackled through a combination of two methods: local reduction and an external active-set method. Specifically, this involves iteratively identifying the closest point obstacles, determining the lower-level distance minimizer among all feasible robot shape parameters, and solving the upper-level finitely-constrained subproblems.
>   In addition, this paper addresses robust collision avoidance in the presence of ellipsoidal state uncertainties. Enforcing constraint satisfaction over all possible uncertainty realizations extends the dimension of constraint infiniteness. The infinitely many constraints arising from translational uncertainty are handled by local reduction together with the robot shape parameterization, while rotational uncertainty is addressed via a backoff reformulation.
>   A controller implemented based on the proposed method is demonstrated on a real-world robot running at 20Hz, enabling fast and collision-free navigation in tight spaces. An application to 3D collision avoidance is also demonstrated in simulation.

