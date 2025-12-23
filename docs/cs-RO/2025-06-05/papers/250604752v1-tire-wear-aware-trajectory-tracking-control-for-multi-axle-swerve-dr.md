---
layout: default
title: Tire Wear Aware Trajectory Tracking Control for Multi-axle Swerve-drive Autonomous Mobile Robots
---

# Tire Wear Aware Trajectory Tracking Control for Multi-axle Swerve-drive Autonomous Mobile Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04752" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04752v1</a>
  <a href="https://arxiv.org/pdf/2506.04752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04752v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04752v1', 'Tire Wear Aware Trajectory Tracking Control for Multi-axle Swerve-drive Autonomous Mobile Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianxin Hu, Xinhang Xu, Thien-Minh Nguyen, Fen Liu, Shenghai Yuan, Lihua Xie

**分类**: cs.RO, math.OC

**发布日期**: 2025-06-05

**备注**: Accepted in Journal of Automation and Intelligence

---

## 💡 一句话要点

**提出轮胎磨损感知轨迹跟踪控制以优化多轴转向自主移动机器人**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `轮胎磨损` `自主移动机器人` `轨迹跟踪` `分层控制器` `动态模型` `物流运输`

## 📋 核心要点

1. 现有的轨迹跟踪控制方法未能有效考虑轮胎磨损，导致轮胎寿命缩短和维护成本增加。
2. 本文提出了一种基于模型预测控制的轨迹跟踪方法，目标函数中纳入了轮胎磨损的最小化，提升了控制精度与效率。
3. 实验结果显示，所提方法在曲线跟踪中轮胎磨损减少19.19%，在偏航角60度的情况下减少幅度提升至65.20%。

## 📝 摘要（中文）

多轴转向自主移动机器人（MS-AGVs）因其独立转向轮的设计，广泛应用于高负载运输。本文提出了一种新颖的模型预测控制（MPC）方法，旨在优化MS-AGV的轨迹跟踪，同时考虑轮胎磨损的最小化。为加快问题求解过程，研究者设计了分层控制器，并通过整合魔术公式轮胎模型与简化轮胎磨损模型来简化动态模型。实验结果表明，采用该方法可以在普通个人计算机上实时求解，并在曲线跟踪实验中实现轮胎磨损减少19.19%，同时保持跟踪精度。在更具挑战性的场景中，当期望轨迹偏离车辆航向60度时，轮胎磨损的减少幅度提升至65.20%。

## 🔬 方法详解

**问题定义**：本文旨在解决多轴转向自主移动机器人在轨迹跟踪过程中未考虑轮胎磨损的问题，现有方法往往忽视这一因素，导致轮胎寿命缩短和维护成本增加。

**核心思路**：提出了一种新颖的模型预测控制（MPC）方法，通过在目标函数中引入轮胎磨损的最小化，优化轨迹跟踪性能。分层控制器设计和简化动态模型的结合使得求解过程更加高效。

**技术框架**：整体架构包括模型预测控制模块、分层控制器设计和轮胎磨损模型的整合。首先，构建动态模型并简化，然后通过分层控制器进行实时轨迹跟踪控制。

**关键创新**：最重要的技术创新在于将轮胎磨损纳入控制目标，显著提高了轮胎使用效率，与传统方法相比，能够在保持跟踪精度的同时减少磨损。

**关键设计**：关键设计包括使用魔术公式轮胎模型与简化轮胎磨损模型的结合，损失函数中明确考虑轮胎磨损因素，确保控制策略的有效性与实时性。实验中采用模拟退火算法进行实时求解。

## 📊 实验亮点

实验结果显示，所提控制方法在曲线跟踪实验中实现了轮胎磨损减少19.19%，在期望轨迹偏离60度的情况下，轮胎磨损减少幅度提升至65.20%。与未考虑轮胎磨损优化的运动学模型相比，显著提升了性能。

## 🎯 应用场景

该研究的潜在应用领域包括物流运输、仓储管理及自动驾驶技术等。通过优化轮胎磨损，能够降低运营成本，提高机器人在复杂环境中的适应能力，未来可能推动更广泛的自主移动机器人应用。

## 📄 摘要（原文）

> Multi-axle Swerve-drive Autonomous Mobile Robots (MS-AGVs) equipped with independently steerable wheels are commonly used for high-payload transportation. In this work, we present a novel model predictive control (MPC) method for MS-AGV trajectory tracking that takes tire wear minimization consideration in the objective function. To speed up the problem-solving process, we propose a hierarchical controller design and simplify the dynamic model by integrating the \textit{magic formula tire model} and \textit{simplified tire wear model}. In the experiment, the proposed method can be solved by simulated annealing in real-time on a normal personal computer and by incorporating tire wear into the objective function, tire wear is reduced by 19.19\% while maintaining the tracking accuracy in curve-tracking experiments. In the more challenging scene: the desired trajectory is offset by 60 degrees from the vehicle's heading, the reduction in tire wear increased to 65.20\% compared to the kinematic model without considering the tire wear optimization.

