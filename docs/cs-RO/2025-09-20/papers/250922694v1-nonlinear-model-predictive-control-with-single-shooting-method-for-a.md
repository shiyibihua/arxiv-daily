---
layout: default
title: Nonlinear Model Predictive Control with Single-Shooting Method for Autonomous Personal Mobility Vehicle
---

# Nonlinear Model Predictive Control with Single-Shooting Method for Autonomous Personal Mobility Vehicle

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22694" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22694v1</a>
  <a href="https://arxiv.org/pdf/2509.22694.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22694v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22694v1', 'Nonlinear Model Predictive Control with Single-Shooting Method for Autonomous Personal Mobility Vehicle')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rakha Rahmadani Pratama, Catur Hilman A. H. B. Baskoro, Joga Dharma Setiawan, Dyah Kusuma Dewi, P Paryanto, Mochammad Ariyanto, Roni Permana Saputra

**分类**: cs.RO

**发布日期**: 2025-09-20

**备注**: 15 pages, 3 figures, 4 tables

**期刊**: Journal of Mechatronics, Electrical Power, and Vehicular Technology 15.2 (2024): 186-196

**DOI**: [10.55981/j.mev.2024.1105](https://doi.org/10.55981/j.mev.2024.1105)

---

## 💡 一句话要点

**提出基于单次射击法的非线性模型预测控制，用于自主个人交通工具。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `非线性模型预测控制` `单次射击法` `自主车辆` `机器人操作系统` `轨迹跟踪`

## 📋 核心要点

1. 现有自主车辆控制方法在复杂环境下的鲁棒性和实时性方面存在挑战，难以同时满足多种约束条件。
2. 采用单次射击法的非线性模型预测控制，通过非线性规划求解最优控制问题，实现精确的轨迹跟踪和避障。
3. 在Gazebo和ROS环境下进行了仿真实验，验证了该方法在无障碍和静态障碍环境中的有效性和实时性。

## 📝 摘要（中文）

本文提出了一种用于自主个人交通工具（特别是单人电动自主运输车SEATER）的控制方法，该方法采用非线性模型预测控制（NMPC）。该方法利用单次射击法，通过非线性规划（NLP）求解最优控制问题（OCP）。所提出的NMPC应用于具有差动驱动系统的非完整车辆，使用里程计数据作为定位反馈，引导车辆到达目标姿态，同时实现目标并遵守约束，例如避障。为了评估所提出方法的性能，在无障碍和静态障碍环境中进行了一系列仿真。SEATER模型和测试环境已在Gazebo仿真中开发，NMPC在机器人操作系统（ROS）框架内实现。仿真结果表明，基于NMPC的方法成功地控制车辆到达期望的目标位置，同时满足施加的约束。此外，本研究强调了NMPC与单次射击法在评估场景中对自主车辆控制的鲁棒性和实时有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决自主个人交通工具在复杂环境中安全、高效导航的问题。现有方法在处理非线性动力学、约束条件和实时性要求方面存在不足，尤其是在需要同时考虑多个目标和约束的情况下，难以保证车辆的稳定性和安全性。

**核心思路**：论文的核心思路是利用非线性模型预测控制（NMPC）的预测能力和优化能力，通过预测车辆未来一段时间内的状态，并优化控制输入，从而实现精确的轨迹跟踪和避障。单次射击法用于简化优化问题，提高计算效率，使其能够满足实时性要求。

**技术框架**：整体框架包括以下几个主要模块：1) 车辆动力学模型：描述车辆的运动规律；2) 状态估计器：利用里程计数据估计车辆的当前状态；3) NMPC控制器：基于车辆动力学模型和状态估计，预测未来状态并优化控制输入；4) 优化求解器：使用非线性规划（NLP）求解最优控制问题。整个系统在ROS框架下实现，便于与其他模块集成。

**关键创新**：该方法的主要创新在于将单次射击法与NMPC相结合，在保证控制性能的同时，显著降低了计算复杂度，提高了实时性。此外，该方法能够有效地处理非线性动力学和约束条件，使其能够适应复杂环境。

**关键设计**：关键设计包括：1) 车辆动力学模型的选择，需要准确描述车辆的运动特性；2) 预测时域的长度，需要在控制性能和计算复杂度之间进行权衡；3) 优化问题的目标函数，需要综合考虑轨迹跟踪精度、控制输入能量和安全性；4) 约束条件的设计，需要保证车辆在运动过程中不违反物理限制和安全规则。

## 📊 实验亮点

仿真结果表明，所提出的NMPC方法能够成功控制SEATER到达目标位置，同时满足避障等约束条件。在无障碍和静态障碍环境中，车辆均能准确跟踪预定轨迹，并保持良好的稳定性。该方法在ROS框架下的实时性也得到了验证，为实际应用奠定了基础。

## 🎯 应用场景

该研究成果可应用于各种自主移动机器人，包括自主车辆、服务机器人和工业机器人等。通过优化控制策略，可以提高机器人在复杂环境中的导航能力，降低能源消耗，并提高安全性。未来，该技术有望在智能交通、智慧物流和智能制造等领域发挥重要作用。

## 📄 摘要（原文）

> This paper introduces a proposed control method for autonomous personal mobility vehicles, specifically the Single-passenger Electric Autonomous Transporter (SEATER), using Nonlinear Model Predictive Control (NMPC). The proposed method leverages a single-shooting approach to solve the optimal control problem (OCP) via non-linear programming (NLP). The proposed NMPC is implemented to a non-holonomic vehicle with a differential drive system, using odometry data as localization feedback to guide the vehicle towards its target pose while achieving objectives and adhering to constraints, such as obstacle avoidance. To evaluate the performance of the proposed method, a number of simulations have been conducted in both obstacle-free and static obstacle environments. The SEATER model and testing environment have been developed in the Gazebo Simulation and the NMPC are implemented within the Robot Operating System (ROS) framework. The simulation results demonstrate that the NMPC-based approach successfully controls the vehicle to reach the desired target location while satisfying the imposed constraints. Furthermore, this study highlights the robustness and real-time effectiveness of NMPC with a single-shooting approach for autonomous vehicle control in the evaluated scenarios.

