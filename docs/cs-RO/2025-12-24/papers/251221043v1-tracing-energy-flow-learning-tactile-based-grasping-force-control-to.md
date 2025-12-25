---
layout: default
title: "Tracing Energy Flow: Learning Tactile-based Grasping Force Control to Prevent Slippage in Dynamic Object Interaction"
---

# Tracing Energy Flow: Learning Tactile-based Grasping Force Control to Prevent Slippage in Dynamic Object Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21043" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21043v1</a>
  <a href="https://arxiv.org/pdf/2512.21043.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21043v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21043v1', 'Tracing Energy Flow: Learning Tactile-based Grasping Force Control to Prevent Slippage in Dynamic Object Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheng-Yu Kuo, Hirofumi Shin, Takamitsu Matsubara

**分类**: cs.RO

**发布日期**: 2025-12-24

**备注**: 8 pages. Accepted by IEEE Robotics and Automation Letters (RA-L)

---

## 💡 一句话要点

**提出基于触觉能量流的抓取力控制方法，防止动态物体交互中的滑移**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `触觉感知` `抓取力控制` `能量流` `动态物体交互` `模型预测控制`

## 📋 核心要点

1. 现有方法在动态物体交互中难以有效调节抓取力，尤其是在物体属性未知和外部传感不可靠的情况下。
2. 该论文提出了一种基于物理信息的能量抽象方法，通过建模物体能量变化来推断滑移，并优化抓取力。
3. 实验表明，该方法能够在几分钟内学习抓取力控制，有效减少滑移，并延长抓取时间，无需外部传感或先验知识。

## 📝 摘要（中文）

在动态物体交互中，调节抓取力以减少滑移是一个根本性的挑战，尤其是在物体由多个滚动接触操纵、具有未知属性（如质量或表面条件）以及外部传感不可靠时。受人类即使在没有视觉线索的情况下也能通过触摸快速调节抓取力的能力启发，本文旨在使机器人手能够在运动和有限传感下快速探索物体，并学习触觉驱动的抓取力控制。我们提出了一种基于物理信息的能量抽象，将物体建模为虚拟能量容器。手指施加的功率与物体保持的能量之间的不一致性，为推断滑移感知的稳定性提供了物理基础信号。在此基础上，我们采用基于模型的学习和规划，从触觉传感中有效地建模能量动态，并执行实时抓取力优化。在仿真和硬件中的实验表明，我们的方法可以在几分钟内从头开始学习抓取力控制，有效地减少滑移，并在不同的运动-物体对中延长抓取持续时间，所有这些都不依赖于外部传感或先验物体知识。

## 🔬 方法详解

**问题定义**：论文旨在解决动态物体交互中，机器人如何在物体属性未知、外部传感不可靠的情况下，通过触觉信息控制抓取力，从而防止滑移的问题。现有方法难以适应动态环境和未知物体属性，容易发生滑移，导致操作失败。

**核心思路**：论文的核心思路是将物体视为一个虚拟的能量容器，通过监测手指施加的功率与物体自身能量变化之间的差异来判断是否发生滑移。如果手指施加的能量大于物体保持的能量，则可能发生滑移。基于这种能量不一致性，可以调整抓取力，从而提高抓取的稳定性。

**技术框架**：整体框架包括触觉数据采集、能量动态建模、抓取力优化三个主要阶段。首先，通过触觉传感器获取手指与物体接触的信息。然后，利用这些信息建立物体能量动态模型，该模型描述了手指施加的功率与物体能量变化之间的关系。最后，基于该模型，通过模型预测控制（MPC）等方法，实时优化抓取力，以减少滑移的发生。

**关键创新**：最重要的创新点在于提出了基于物理信息的能量抽象方法，将复杂的抓取问题转化为能量流的分析。这种方法能够有效地利用触觉信息，推断物体的状态和稳定性，而无需依赖外部传感器或先验知识。与传统的基于视觉或力/力矩传感的抓取控制方法相比，该方法更加鲁棒和灵活。

**关键设计**：论文采用基于模型的学习方法来建立能量动态模型。具体来说，可以使用高斯过程回归（GPR）等方法，从触觉数据中学习手指施加的功率与物体能量变化之间的关系。损失函数可以设计为最小化预测的能量变化与实际能量变化之间的差异。在抓取力优化阶段，可以使用模型预测控制（MPC）算法，根据能量动态模型预测未来一段时间内的物体状态，并优化抓取力，以最小化滑移的风险。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21043v1/fig/intro.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21043v1/fig/energy_power_overview.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21043v1/fig/robot_setup.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法能够在几分钟内从零开始学习抓取力控制，有效地减少滑移，并延长抓取持续时间。在仿真和硬件实验中，该方法都表现出良好的性能，能够适应不同的运动-物体对，且无需外部传感或先验知识。与传统的抓取控制方法相比，该方法在防止滑移方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于各种需要精确抓取和操作的场景，例如：工业自动化中对未知物体的抓取和装配、家庭服务机器人中对日常用品的操作、医疗机器人中对脆弱物体的操作等。通过提高抓取的稳定性和可靠性，可以显著提高机器人的工作效率和安全性，扩展其应用范围。

## 📄 摘要（原文）

> Regulating grasping force to reduce slippage during dynamic object interaction remains a fundamental challenge in robotic manipulation, especially when objects are manipulated by multiple rolling contacts, have unknown properties (such as mass or surface conditions), and when external sensing is unreliable. In contrast, humans can quickly regulate grasping force by touch, even without visual cues. Inspired by this ability, we aim to enable robotic hands to rapidly explore objects and learn tactile-driven grasping force control under motion and limited sensing. We propose a physics-informed energy abstraction that models the object as a virtual energy container. The inconsistency between the fingers' applied power and the object's retained energy provides a physically grounded signal for inferring slip-aware stability. Building on this abstraction, we employ model-based learning and planning to efficiently model energy dynamics from tactile sensing and perform real-time grasping force optimization. Experiments in both simulation and hardware demonstrate that our method can learn grasping force control from scratch within minutes, effectively reduce slippage, and extend grasp duration across diverse motion-object pairs, all without relying on external sensing or prior object knowledge.

