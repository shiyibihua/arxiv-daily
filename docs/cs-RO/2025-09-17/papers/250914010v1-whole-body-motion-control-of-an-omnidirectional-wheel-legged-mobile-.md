---
layout: default
title: Whole-body Motion Control of an Omnidirectional Wheel-Legged Mobile Manipulator via Contact-Aware Dynamic Optimization
---

# Whole-body Motion Control of an Omnidirectional Wheel-Legged Mobile Manipulator via Contact-Aware Dynamic Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14010" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14010v1</a>
  <a href="https://arxiv.org/pdf/2509.14010.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14010v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14010v1', 'Whole-body Motion Control of an Omnidirectional Wheel-Legged Mobile Manipulator via Contact-Aware Dynamic Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zong Chen, Shaoyang Li, Ben Liu, Min Li, Zhouping Yin, Yiqun Li

**分类**: cs.RO

**发布日期**: 2025-09-17

---

## 💡 一句话要点

**提出一种接触感知的全身动态优化方法，用于全向轮腿式移动机械臂的运动控制。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `轮腿式机器人` `全身运动控制` `动态优化` `接触感知` `移动操作`

## 📋 核心要点

1. 轮腿式机器人具有冗余自由度、复杂的轮地接触动力学以及运动和操作之间无缝协调的需求，因此统一控制仍然具有挑战性。
2. 论文提出了一种接触感知的全身动态优化框架，集成了点接触和线接触建模，并采用热启动策略加速在线优化。
3. 仿真和实验结果验证了该框架的有效性，展示了机器人在敏捷地形穿越、高速全向移动和精确操作方面的能力。

## 📝 摘要（中文）

本文提出了一种全向轮腿式四足机器人平台的全身运动控制方法，该机器人配备了一个灵巧的机械臂。该平台采用独立驱动的转向模块和轮毂驱动轮，实现了在结构化环境中灵活的全向运动和高机动性。为了应对富接触交互的挑战，开发了一种接触感知的全身动态优化框架，该框架集成了用于操作的点接触建模和用于轮地交互的线接触建模。引入了一种热启动策略来加速在线优化，确保高维控制的实时可行性。此外，针对机器人4WIS-4WID驱动方案的统一运动学模型消除了不同运动策略之间模式切换的需要，提高了控制的一致性和鲁棒性。仿真和实验结果验证了所提出框架的有效性，展示了在各种场景下的敏捷地形穿越、高速全向移动和精确操作，突出了该系统在工厂自动化、城市物流和服务机器人等半结构化环境中的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决全向轮腿式移动机械臂的全身运动控制问题，尤其是在存在复杂轮地接触和需要操作的情况下。现有方法通常难以处理高维度的优化问题，并且在不同运动模式之间切换时存在不连续性。

**核心思路**：论文的核心思路是利用接触感知的全身动态优化，将操作任务和运动任务统一到一个框架中。通过精确建模轮地接触和机械臂与环境的接触，并结合热启动策略，实现实时可行的全身运动控制。

**技术框架**：该框架包含以下主要模块：1) 机器人运动学和动力学建模，包括轮腿和机械臂；2) 接触建模，使用点接触模型描述机械臂与环境的交互，使用线接触模型描述轮地交互；3) 全身动态优化，将运动和操作任务转化为一个优化问题，目标是最小化能量消耗、跟踪期望轨迹等；4) 热启动策略，利用上一时刻的优化结果作为当前时刻的初始猜测，加速优化过程。

**关键创新**：论文的关键创新在于：1) 提出了一个统一的接触感知的全身动态优化框架，能够同时处理运动和操作任务；2) 针对轮腿式机器人的特殊结构，设计了专门的接触模型，提高了控制精度；3) 引入了热启动策略，显著提高了在线优化的速度，使其能够满足实时控制的需求。

**关键设计**：论文中，接触模型的设计至关重要，需要准确描述轮地之间的力和力矩传递。此外，优化问题的目标函数需要仔细设计，以平衡运动的平滑性、操作的精度和能量的消耗。热启动策略的有效性取决于初始猜测的质量，因此需要选择合适的初始化方法。

## 📊 实验亮点

实验结果表明，该方法能够实现机器人在复杂地形上的敏捷移动和精确操作。例如，机器人能够以较高的速度（具体数值未知）进行全向移动，并能够精确地完成操作任务（具体精度数据未知）。与传统的基于模式切换的控制方法相比，该方法具有更好的鲁棒性和一致性（具体提升幅度未知）。

## 🎯 应用场景

该研究成果可应用于工厂自动化、城市物流、服务机器人等领域。例如，在工厂中，轮腿式机器人可以灵活地在狭窄空间内移动，并利用机械臂进行物料搬运和组装。在城市物流中，机器人可以自主地完成包裹的配送任务。在服务机器人领域，该技术可以帮助机器人更好地与人类进行交互，完成各种服务任务。

## 📄 摘要（原文）

> Wheel-legged robots with integrated manipulators hold great promise for mobile manipulation in logistics, industrial automation, and human-robot collaboration. However, unified control of such systems remains challenging due to the redundancy in degrees of freedom, complex wheel-ground contact dynamics, and the need for seamless coordination between locomotion and manipulation. In this work, we present the design and whole-body motion control of an omnidirectional wheel-legged quadrupedal robot equipped with a dexterous manipulator. The proposed platform incorporates independently actuated steering modules and hub-driven wheels, enabling agile omnidirectional locomotion with high maneuverability in structured environments. To address the challenges of contact-rich interaction, we develop a contact-aware whole-body dynamic optimization framework that integrates point-contact modeling for manipulation with line-contact modeling for wheel-ground interactions. A warm-start strategy is introduced to accelerate online optimization, ensuring real-time feasibility for high-dimensional control. Furthermore, a unified kinematic model tailored for the robot's 4WIS-4WID actuation scheme eliminates the need for mode switching across different locomotion strategies, improving control consistency and robustness. Simulation and experimental results validate the effectiveness of the proposed framework, demonstrating agile terrain traversal, high-speed omnidirectional mobility, and precise manipulation under diverse scenarios, underscoring the system's potential for factory automation, urban logistics, and service robotics in semi-structured environments.

