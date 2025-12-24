---
layout: default
title: Bio-Inspired Topological Autonomous Navigation with Active Inference in Robotics
---

# Bio-Inspired Topological Autonomous Navigation with Active Inference in Robotics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07267" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07267v1</a>
  <a href="https://arxiv.org/pdf/2508.07267.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07267v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07267v1', 'Bio-Inspired Topological Autonomous Navigation with Active Inference in Robotics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daria de Tinguy, Tim Verbelen, Emilio Gamba, Bart Dhoedt

**分类**: cs.RO

**发布日期**: 2025-08-10

**备注**: Conference ICCAS 2025 - accepted (in processing)

---

## 💡 一句话要点

**提出生物启发式拓扑自主导航以解决机器人导航挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自主导航` `生物启发` `主动推理` `拓扑地图` `动态环境` `机器人技术` `ROS2` `概率推理`

## 📋 核心要点

1. 现有的导航方法往往缺乏适应性，依赖于严格的规则或需要大量数据的预训练，限制了在动态环境中的应用。
2. 本文提出了一种基于主动推理框架的生物启发式智能体，能够实时创建拓扑地图并进行自适应决策，无需预训练。
3. 实验结果表明，该方法在大型模拟环境中成功探索，并能有效应对动态障碍，表现与现有策略相当。

## 📝 摘要（中文）

实现完全自主的探索和导航仍然是机器人技术中的一项关键挑战，需要整合定位、地图构建、决策和运动规划等解决方案。现有方法往往依赖于严格的导航规则或预训练，缺乏适应性，且计算成本高，限制了其在动态或未知环境中的适应能力。本文提出了一种基于主动推理框架的生物启发式智能体，统一了自主导航中的地图构建、定位和自适应决策。该模型实时创建和更新环境的拓扑地图，规划目标导向的轨迹以探索或到达目标，无需预训练。关键贡献包括可解释导航的概率推理框架、对动态变化的强大适应性，以及与现有导航系统兼容的模块化ROS2架构。我们的模型在模拟和现实环境中进行了测试，成功适应动态障碍和漂移，证明其与其他探索策略如Gbplanner、FAEL和Frontiers相当。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人自主导航中的定位、地图构建和决策制定的整合问题。现有方法往往依赖于静态假设或高计算成本的预训练，导致在动态环境中的适应性不足。

**核心思路**：论文提出的生物启发式智能体基于主动推理框架，能够实时更新环境的拓扑地图，并规划目标导向的轨迹。这种设计使得智能体能够在未知环境中进行自主探索，而无需依赖大量的预训练数据。

**技术框架**：整体架构包括环境感知、地图构建、决策制定和运动规划四个主要模块。智能体通过传感器获取环境信息，实时更新拓扑地图，并根据目标进行路径规划。

**关键创新**：最重要的技术创新在于将主动推理框架应用于导航任务，使得智能体能够在动态环境中进行概率推理和自适应决策。这与传统方法的静态假设形成了显著对比。

**关键设计**：在设计中，智能体使用了模块化的ROS2架构，确保与现有导航系统的兼容性。同时，采用了概率推理机制，使得导航过程更加可解释和透明。

## 📊 实验亮点

实验结果显示，所提出的智能体在大型模拟环境中成功探索，并能够适应动态障碍和漂移，其性能与Gbplanner、FAEL和Frontiers等现有探索策略相当，证明了该方法的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括无人驾驶汽车、服务机器人和探索机器人等。通过提供一种可扩展且透明的导航方法，该技术能够在复杂和非结构化环境中实现更高效的自主导航，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Achieving fully autonomous exploration and navigation remains a critical challenge in robotics, requiring integrated solutions for localisation, mapping, decision-making and motion planning. Existing approaches either rely on strict navigation rules lacking adaptability or on pre-training, which requires large datasets. These AI methods are often computationally intensive or based on static assumptions, limiting their adaptability in dynamic or unknown environments. This paper introduces a bio-inspired agent based on the Active Inference Framework (AIF), which unifies mapping, localisation, and adaptive decision-making for autonomous navigation, including exploration and goal-reaching. Our model creates and updates a topological map of the environment in real-time, planning goal-directed trajectories to explore or reach objectives without requiring pre-training. Key contributions include a probabilistic reasoning framework for interpretable navigation, robust adaptability to dynamic changes, and a modular ROS2 architecture compatible with existing navigation systems. Our method was tested in simulated and real-world environments. The agent successfully explores large-scale simulated environments and adapts to dynamic obstacles and drift, proving to be comparable to other exploration strategies such as Gbplanner, FAEL and Frontiers. This approach offers a scalable and transparent approach for navigating complex, unstructured environments.

