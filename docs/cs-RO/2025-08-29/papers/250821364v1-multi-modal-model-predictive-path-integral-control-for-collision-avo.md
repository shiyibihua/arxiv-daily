---
layout: default
title: Multi-Modal Model Predictive Path Integral Control for Collision Avoidance
---

# Multi-Modal Model Predictive Path Integral Control for Collision Avoidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21364" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21364v1</a>
  <a href="https://arxiv.org/pdf/2508.21364.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21364v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21364v1', 'Multi-Modal Model Predictive Path Integral Control for Collision Avoidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alberto Bertipaglia, Dariu M. Gavrila, Barys Shyrokau

**分类**: cs.RO, eess.SY

**发布日期**: 2025-08-29

**备注**: Accepted as an oral presentation at the 29th IAVSD. August 18-22, 2025. Shanghai, China

---

## 💡 一句话要点

**提出多模态模型预测路径积分控制以解决碰撞避免问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `运动规划` `碰撞避免` `模型预测控制` `多模态控制` `自动驾驶` `高保真仿真` `非线性优化`

## 📋 核心要点

1. 现有的运动规划方法在复杂环境中容易产生次优解，导致碰撞风险增加。
2. 本文提出的多模态模型预测路径积分控制算法，通过多样化轨迹探索，提高了碰撞避免的能力。
3. 实验结果表明，该算法在高低摩擦路面和动态障碍物场景中表现优异，显著提升了车辆的稳定性和安全性。

## 📝 摘要（中文）

本文提出了一种新颖的运动规划和决策方法，针对自动驾驶车辆使用多模态模型预测路径积分控制算法。该方法通过在先前输入周围使用Sobol序列进行采样，并结合碰撞避免的解析解。通过利用多种模式，该多模态控制算法探索多样化的轨迹，如绕过障碍物或在障碍物前安全停车，从而降低次优解的风险。采用非线性单轨车辆模型和Fiala轮胎作为预测模型，并在摩擦圆内强制执行轮胎力约束，以确保车辆在规避机动中的稳定性。在高保真仿真环境中，我们展示了所提出的算法能够成功避免障碍物，同时在高低摩擦路面和移动障碍物的遮挡场景中保持车辆稳定，优于标准的模型预测路径积分方法。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶车辆在复杂环境中运动规划时的碰撞避免问题。现有方法常常在多变的环境中产生次优解，导致碰撞风险增加。

**核心思路**：论文提出的多模态模型预测路径积分控制算法，通过使用Sobol序列进行采样，结合解析解来实现碰撞避免。多模态设计使得算法能够探索多样化的轨迹，增强了决策的灵活性和安全性。

**技术框架**：整体架构包括以下几个主要模块：首先，使用非线性单轨车辆模型进行状态预测；其次，利用Sobol序列生成样本轨迹；然后，结合解析解进行碰撞检测与避免；最后，优化转向角和纵向加速度以生成无碰撞轨迹。

**关键创新**：最重要的技术创新在于引入多模态控制策略，允许算法在面对复杂障碍物时灵活选择不同的轨迹，从而有效降低碰撞风险。这与传统的单一模式控制方法形成鲜明对比。

**关键设计**：在设计中，采用Fiala轮胎模型来模拟轮胎力，并在摩擦圆内施加约束，以确保车辆在规避机动中的稳定性。优化过程中，转向角和纵向加速度的计算是通过非线性优化方法实现的。具体参数设置和损失函数设计在实验中经过调优，以达到最佳性能。

## 📊 实验亮点

实验结果显示，所提出的算法在高保真仿真环境中成功避免了障碍物，尤其在双车道变换机动中表现出色。与标准模型预测路径积分方法相比，算法在高摩擦和低摩擦路面上的稳定性显著提升，具体性能提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车、智能交通系统和机器人导航等。通过提高碰撞避免能力，该算法能够在复杂环境中确保车辆安全行驶，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This paper proposes a novel approach to motion planning and decision-making for automated vehicles, using a multi-modal Model Predictive Path Integral control algorithm. The method samples with Sobol sequences around the prior input and incorporates analytical solutions for collision avoidance. By leveraging multiple modes, the multi-modal control algorithm explores diverse trajectories, such as manoeuvring around obstacles or stopping safely before them, mitigating the risk of sub-optimal solutions. A non-linear single-track vehicle model with a Fiala tyre serves as the prediction model, and tyre force constraints within the friction circle are enforced to ensure vehicle stability during evasive manoeuvres. The optimised steering angle and longitudinal acceleration are computed to generate a collision-free trajectory and to control the vehicle. In a high-fidelity simulation environment, we demonstrate that the proposed algorithm can successfully avoid obstacles, keeping the vehicle stable while driving a double lane change manoeuvre on high and low-friction road surfaces and occlusion scenarios with moving obstacles, outperforming a standard Model Predictive Path Integral approach.

