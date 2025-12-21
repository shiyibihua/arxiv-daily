---
layout: default
title: A Task-Driven, Planner-in-the-Loop Computational Design Framework for Modular Manipulators
---

# A Task-Driven, Planner-in-the-Loop Computational Design Framework for Modular Manipulators

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16069" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16069v1</a>
  <a href="https://arxiv.org/pdf/2512.16069.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16069v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16069v1', 'A Task-Driven, Planner-in-the-Loop Computational Design Framework for Modular Manipulators')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maolin Lei, Edoardo Romiti, Arturo Laurenzi, Rui Dai, Matteo Dalle Vedove, Jiatao Ding, Daniele Fontanelli, Nikos Tsagarakis

**分类**: cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出任务驱动的模块化机械臂计算设计框架，实现形态与运动的协同优化**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模块化机械臂` `计算设计` `轨迹规划` `形态优化` `双分支结构` `模型预测控制` `CMA-ES`

## 📋 核心要点

1. 传统单分支机械臂通过增加连杆长度来扩展工作空间，易超出基关节的扭矩限制，存在设计瓶颈。
2. 提出一种统一的计算框架，将轨迹规划与形态、安装姿态的协同优化相结合，实现任务驱动的设计。
3. 通过仿真和硬件实验验证，该框架能生成满足约束的可行设计，并实现灵活的设计目标，如优化可操作性。

## 📝 摘要（中文）

本文提出了一种统一的任务驱动计算框架，用于模块化机械臂的设计，该框架集成了不同形态下的轨迹规划以及形态和安装姿态的协同优化。开发了一种分层模型预测控制（HMPC）策略，用于冗余和非冗余机械臂的运动规划。采用CMA-ES算法高效探索离散形态配置和连续安装姿态的混合搜索空间。引入虚拟模块抽象，实现双分支形态，允许辅助分支卸载主分支的扭矩，扩展可达工作空间，而无需增加单个关节模块的容量。在抛光、钻孔和取放任务中的仿真和硬件实验验证了该框架的有效性。结果表明，该框架可以生成满足运动学和动力学约束的可行设计，同时避免环境碰撞；通过定制成本函数，可以实现灵活的设计目标，例如最大化可操作性、最小化关节力或减少模块数量；无需更强大的基本模块即可实现可在大型工作空间中运行的双分支形态。

## 🔬 方法详解

**问题定义**：模块化机械臂的设计需要同时优化机械臂的形态、安装姿态和运动轨迹，以满足特定的任务需求。传统方法往往采用单分支结构，通过增加连杆长度来扩大工作空间，但容易导致基关节扭矩超出限制。此外，现有方法难以在满足运动学、动力学和物理约束的同时，实现形态和运动的协同优化。

**核心思路**：本文的核心思路是将轨迹规划融入到机械臂的设计过程中，通过任务驱动的方式，同时优化机械臂的形态、安装姿态和运动轨迹。引入双分支结构，利用辅助分支来分担主分支的扭矩，从而在不增加关节模块功率的情况下，扩展机械臂的工作空间。

**技术框架**：该框架包含以下主要模块：1) 运动规划模块，采用分层模型预测控制（HMPC）策略，为冗余和非冗余机械臂生成可行的运动轨迹；2) 设计优化模块，采用CMA-ES算法，在离散的形态配置和连续的安装姿态空间中进行高效搜索；3) 虚拟模块抽象模块，用于实现双分支形态，并评估其对扭矩分担和工作空间扩展的影响。整个流程是迭代的，设计优化模块根据运动规划模块的反馈，不断调整机械臂的形态和安装姿态，直到满足任务需求。

**关键创新**：该论文的关键创新在于：1) 提出了一种任务驱动的设计框架，将运动规划融入到机械臂的设计过程中，实现了形态和运动的协同优化；2) 引入了虚拟模块抽象，实现了双分支形态，可以在不增加关节模块功率的情况下，扩展机械臂的工作空间；3) 采用分层模型预测控制（HMPC）策略，实现了冗余和非冗余机械臂的运动规划。

**关键设计**：在运动规划模块中，HMPC策略被用于生成运动轨迹，其目标是最小化关节力矩和轨迹误差。在设计优化模块中，CMA-ES算法被用于搜索最优的形态和安装姿态，其目标是最大化可操作性、最小化关节力或减少模块数量。虚拟模块抽象通过添加虚拟连杆和关节来模拟双分支结构，并评估其对扭矩分担和工作空间扩展的影响。成本函数可以根据具体任务进行定制，以实现不同的设计目标。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16069v1/figure/dual_arm_robot.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16069v1/figure/framework.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16069v1/figure/balance_updae.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

通过在抛光、钻孔和取放任务中的仿真和硬件实验，验证了该框架的有效性。实验结果表明，该框架能够生成满足运动学和动力学约束的可行设计，并实现灵活的设计目标，例如最大化可操作性、最小化关节力或减少模块数量。此外，双分支形态可以在不增加关节模块功率的情况下，扩展机械臂的工作空间。

## 🎯 应用场景

该研究成果可应用于各种需要灵活适应性的工业自动化场景，例如：复杂曲面的抛光、高精度钻孔、以及在狭小空间内的物料搬运等。通过优化机械臂的形态和运动，可以提高生产效率、降低能源消耗，并扩展机械臂的应用范围。未来，该框架可进一步扩展到多机械臂协同作业、人机协作等领域。

## 📄 摘要（原文）

> Modular manipulators composed of pre-manufactured and interchangeable modules offer high adaptability across diverse tasks. However, their deployment requires generating feasible motions while jointly optimizing morphology and mounted pose under kinematic, dynamic, and physical constraints. Moreover, traditional single-branch designs often extend reach by increasing link length, which can easily violate torque limits at the base joint. To address these challenges, we propose a unified task-driven computational framework that integrates trajectory planning across varying morphologies with the co-optimization of morphology and mounted pose. Within this framework, a hierarchical model predictive control (HMPC) strategy is developed to enable motion planning for both redundant and non-redundant manipulators. For design optimization, the CMA-ES is employed to efficiently explore a hybrid search space consisting of discrete morphology configurations and continuous mounted poses. Meanwhile, a virtual module abstraction is introduced to enable bi-branch morphologies, allowing an auxiliary branch to offload torque from the primary branch and extend the achievable workspace without increasing the capacity of individual joint modules. Extensive simulations and hardware experiments on polishing, drilling, and pick-and-place tasks demonstrate the effectiveness of the proposed framework. The results show that: 1) the framework can generate multiple feasible designs that satisfy kinematic and dynamic constraints while avoiding environmental collisions for given tasks; 2) flexible design objectives, such as maximizing manipulability, minimizing joint effort, or reducing the number of modules, can be achieved by customizing the cost functions; and 3) a bi-branch morphology capable of operating in a large workspace can be realized without requiring more powerful basic modules.

