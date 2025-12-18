---
layout: default
title: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation
---

# CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06819" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06819v1</a>
  <a href="https://arxiv.org/pdf/2509.06819.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06819v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06819v1', 'CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniel San José Pro, Oliver Hausdörfer, Ralf Römer, Maximilian Dösch, Martin Schuck, Angela P. Schöllig

**分类**: cs.RO

**发布日期**: 2025-09-08

**备注**: 5 pages, 5 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://utiasDSL.github.io/crisp_controllers)

---

## 💡 一句话要点

**CRISP：用于学习操作策略和遥操作的兼容ROS2控制器**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `ROS2控制` `机器人操作` `学习策略` `兼容控制` `笛卡尔空间控制`

## 📋 核心要点

1. 基于学习的控制器通常产生低频或不连续的机器人状态变化，需要低层控制器实现平滑的参考跟踪。
2. CRISP提供兼容的笛卡尔和关节空间控制器，将高层指令转换为关节扭矩，实现接触交互中的兼容行为。
3. CRISP通过统一的pipeline简化了数据记录、策略部署和硬件/模拟验证，加速了学习方法在ROS2机械臂上的应用。

## 📝 摘要（中文）

本文提出CRISP，一个轻量级的C++实现，用于ROS2控制标准的兼容笛卡尔和关节空间控制器。CRISP旨在与高层学习策略和遥操作无缝集成，将高层目标命令转换为关节扭矩，从而在接触交互期间实现兼容行为。该控制器兼容任何暴露关节扭矩接口的机械臂。通过Python和Gymnasium接口，CRISP提供了一个统一的pipeline，用于记录来自硬件和模拟的数据，并无缝部署高层学习策略，从而促进快速实验。该系统已在Franka Robotics FR3硬件以及Kuka IIWA14和Kinova Gen3模拟环境中进行了验证。CRISP的设计目标是快速集成、灵活部署和实时性能，为数据收集和策略执行提供统一的pipeline，降低了在ROS2兼容机械臂上应用基于学习方法的技术门槛。

## 🔬 方法详解

**问题定义**：现有基于学习的控制器，如扩散策略和视觉-语言动作模型，通常输出低频率或不连续的机器人状态变化。这使得机器人难以实现平滑的轨迹跟踪，尤其是在需要与环境进行接触交互时。现有的低层控制器可能无法很好地处理这些不连续的指令，导致机器人运动不稳定或产生较大的力。

**核心思路**：CRISP的核心思路是提供一个兼容的、实时的低层控制器，能够将高层学习策略输出的指令平滑地转换为关节扭矩，从而实现机器人在接触交互中的稳定和兼容行为。通过提供笛卡尔空间和关节空间的控制接口，CRISP可以灵活地适应不同的任务需求。

**技术框架**：CRISP是一个基于C++实现的ROS2软件包，包含笛卡尔空间和关节空间控制器。它提供Python和Gymnasium接口，方便用户进行数据收集、策略训练和部署。该框架支持多种机械臂，包括Franka Robotics FR3、Kuka IIWA14和Kinova Gen3。整体流程包括：高层策略输出目标状态 -> CRISP控制器将目标状态转换为关节扭矩 -> 机器人执行运动。

**关键创新**：CRISP的关键创新在于其兼容性和易用性。它提供了一个统一的pipeline，简化了从数据收集到策略部署的整个流程。此外，CRISP的设计注重实时性能，使其能够应用于实际的机器人控制任务中。与现有的ROS2控制器相比，CRISP更加注重与学习策略的集成。

**关键设计**：CRISP控制器的具体实现细节（如参数设置、损失函数、网络结构等）在论文中没有详细描述。但可以推断，控制器可能采用了PID控制或类似的控制算法，并针对不同的机械臂进行了参数调整。论文强调了控制器的实时性和兼容性，因此在设计上可能采用了轻量级的实现方式，以减少计算负担。

## 📊 实验亮点

论文在Franka Robotics FR3硬件以及Kuka IIWA14和Kinova Gen3模拟环境中验证了CRISP的性能。实验结果表明，CRISP能够有效地将高层学习策略输出的指令转换为关节扭矩，实现机器人在接触交互中的稳定和兼容行为。具体性能数据（如轨迹跟踪误差、力控制精度等）在摘要中未提及，但论文强调了CRISP的实时性和易用性。

## 🎯 应用场景

CRISP可应用于各种机器人操作任务，例如装配、抓取、操作等。它能够帮助研究人员和工程师快速地将学习到的策略部署到实际的机器人系统中，从而提高机器人操作的效率和鲁棒性。此外，CRISP还可以用于遥操作，使操作员能够更加直观地控制机器人，完成复杂的任务。

## 📄 摘要（原文）

> Learning-based controllers, such as diffusion policies and vision-language action models, often generate low-frequency or discontinuous robot state changes. Achieving smooth reference tracking requires a low-level controller that converts high-level targets commands into joint torques, enabling compliant behavior during contact interactions. We present CRISP, a lightweight C++ implementation of compliant Cartesian and joint-space controllers for the ROS2 control standard, designed for seamless integration with high-level learning-based policies as well as teleoperation. The controllers are compatible with any manipulator that exposes a joint-torque interface. Through our Python and Gymnasium interfaces, CRISP provides a unified pipeline for recording data from hardware and simulation and deploying high-level learning-based policies seamlessly, facilitating rapid experimentation. The system has been validated on hardware with the Franka Robotics FR3 and in simulation with the Kuka IIWA14 and Kinova Gen3. Designed for rapid integration, flexible deployment, and real-time performance, our implementation provides a unified pipeline for data collection and policy execution, lowering the barrier to applying learning-based methods on ROS2-compatible manipulators. Detailed documentation is available at the project website - https://utiasDSL.github.io/crisp_controllers.

