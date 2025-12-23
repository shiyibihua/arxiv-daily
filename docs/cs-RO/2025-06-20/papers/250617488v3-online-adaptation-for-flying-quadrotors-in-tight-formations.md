---
layout: default
title: Online Adaptation for Flying Quadrotors in Tight Formations
---

# Online Adaptation for Flying Quadrotors in Tight Formations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17488" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17488v3</a>
  <a href="https://arxiv.org/pdf/2506.17488.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17488v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17488v3', 'Online Adaptation for Flying Quadrotors in Tight Formations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pei-An Hsieh, Kong Yao Chee, M. Ani Hsieh

**分类**: cs.RO, cs.LG, eess.SY

**发布日期**: 2025-06-20 (更新: 2025-10-30)

**备注**: 10 pages, 4 figures

---

## 💡 一句话要点

**提出L1 KNODE-DW MPC以解决四旋翼紧密编队飞行问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `四旋翼` `编队飞行` `气动控制` `自适应控制` `模型预测控制` `无人机技术` `动态系统`

## 📋 核心要点

1. 现有方法在四旋翼紧密编队飞行中面临复杂的气动尾流相互作用，导致个体和团队的不稳定性。
2. 本文提出L1 KNODE-DW MPC框架，通过自适应控制实现四旋翼在飞行中的轨迹跟踪和气动适应。
3. 实验结果显示，该框架在三架四旋翼编队中表现优异，能够保持紧密的垂直对齐，超越多种基线方法。

## 📝 摘要（中文）

在紧密编队飞行中，四旋翼无人机面临复杂的气动尾流相互作用，这可能导致个体及团队的不稳定。针对这一挑战，本文提出了一种自适应的混合专家学习控制框架L1 KNODE-DW MPC，使得四旋翼能够在飞行过程中准确跟踪轨迹，并适应时变的气动相互作用。通过在两种不同的三架四旋翼编队中进行评估，结果表明该框架优于多种模型预测控制基线，能够有效保持编队的垂直对齐。

## 🔬 方法详解

**问题定义**：本文旨在解决四旋翼在紧密编队飞行中因气动尾流相互作用导致的稳定性问题。现有方法难以准确建模和预测这些非线性且快速变化的气动效应，造成飞行控制的挑战。

**核心思路**：提出的L1 KNODE-DW MPC框架结合了自适应控制和混合专家学习，能够实时调整控制策略以应对动态变化的气动环境，从而提高四旋翼的轨迹跟踪精度。

**技术框架**：该框架包括多个模块，首先通过动态模型预测四旋翼的运动，然后利用L1自适应模块对未建模的扰动进行补偿，最后实现精确的轨迹跟踪。

**关键创新**：L1 KNODE-DW MPC的最大创新在于其自适应能力，能够在复杂的气动环境中实时调整控制策略，与传统的模型预测控制方法相比，显著提高了对未建模扰动的补偿能力。

**关键设计**：在设计中，采用了精确的动力学模型，并结合L1损失函数来优化控制策略，确保在快速变化的气动条件下保持稳定性和准确性。

## 📊 实验亮点

实验结果表明，L1 KNODE-DW MPC在两种三架四旋翼编队中表现优异，相较于多种模型预测控制基线，能够有效保持编队的垂直对齐，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括无人机编队飞行、空中交通管理和救援任务等。通过提高四旋翼在复杂环境中的适应能力，该框架能够在实际操作中提升飞行安全性和效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The task of flying in tight formations is challenging for teams of quadrotors because the complex aerodynamic wake interactions can destabilize individual team members as well as the team. Furthermore, these aerodynamic effects are highly nonlinear and fast-paced, making them difficult to model and predict. To overcome these challenges, we present L1 KNODE-DW MPC, an adaptive, mixed expert learning based control framework that allows individual quadrotors to accurately track trajectories while adapting to time-varying aerodynamic interactions during formation flights. We evaluate L1 KNODE-DW MPC in two different three-quadrotor formations and show that it outperforms several MPC baselines. Our results show that the proposed framework is capable of enabling the three-quadrotor team to remain vertically aligned in close proximity throughout the flight. These findings show that the L1 adaptive module compensates for unmodeled disturbances most effectively when paired with an accurate dynamics model. A video showcasing our framework and the physical experiments is available here: https://youtu.be/9QX1Q5Ut9Rs

