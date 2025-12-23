---
layout: default
title: High-speed control and navigation for quadrupedal robots on complex and discrete terrain
---

# High-speed control and navigation for quadrupedal robots on complex and discrete terrain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02835" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02835v1</a>
  <a href="https://arxiv.org/pdf/2506.02835.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02835v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02835v1', 'High-speed control and navigation for quadrupedal robots on complex and discrete terrain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyeongjun Kim, Hyunsik Oh, Jeongsoo Park, Yunho Kim, Donghoon Youm, Moonkyu Jung, Minho Lee, Jemin Hwangbo

**分类**: cs.RO

**发布日期**: 2025-06-03

**期刊**: Science Robotics 10.102 (2025): eads6192

---

## 💡 一句话要点

**提出层次化导航管道以解决四足机器人高速度控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `四足机器人` `高速度导航` `层次化规划` `物理仿真` `动态控制` `复杂地形` `神经网络`

## 📋 核心要点

1. 现有方法在复杂和离散环境中实现高速度四足机器人导航面临高自由度动力学和非凸优化问题的挑战。
2. 本文提出的层次化导航管道通过采样优化和神经网络实现物理可行的足迹计划，并在物理仿真中验证其一致性。
3. 实验结果显示，Raibo机器人能够在30°坡道、楼梯和各种尺寸的箱子上以4米每秒的速度自主导航，表现出优越的动态能力。

## 📝 摘要（中文）

在几何复杂和离散环境中实现高速度的四足机器人导航是一项具有挑战性的任务，主要由于其高自由度的动力学和长时间跨度的非凸优化问题。本文提出了一种层次化导航管道，包含规划器和跟踪器模块，能够高效地找到物理可行的足迹计划，并通过物理仿真确认其一致性。训练阶段中，跟踪器在具有所需难度的环境中进行训练，最终实现了比以往方法更强的地形适应能力。实验结果表明，Raibo机器人能够在复杂地形上进行动态和敏捷的运动。

## 🔬 方法详解

**问题定义**：本文旨在解决四足机器人在几何复杂和离散环境中实现高速度导航的挑战。现有方法在处理高自由度动力学和长时间跨度的非凸优化问题时，效率和准确性不足。

**核心思路**：论文提出的层次化导航管道通过规划器和跟踪器模块的结合，利用采样优化和神经网络来生成物理可行的足迹计划，并通过物理仿真验证其有效性。这样的设计使得机器人能够在复杂环境中高效导航。

**技术框架**：整体架构包括两个主要模块：规划器和跟踪器。规划器负责生成足迹计划，采用基于采样的优化方法，并结合快速序列过滤和启发式算法。跟踪器则确保机器人准确地踩在规划器生成的目标足迹上。

**关键创新**：最重要的创新在于将神经网络与传统的优化方法结合，形成高效的层次化规划模块。这种方法在计算效率和物理准确性上均表现优异，显著提升了机器人的导航能力。

**关键设计**：在训练阶段，跟踪器的目标分布由一个生成模型提供，该模型与跟踪器竞争训练，以确保跟踪器在具有所需难度的环境中进行训练。

## 📊 实验亮点

实验结果显示，Raibo机器人能够在垂直墙面上奔跑、跳跃1.3米的间隙，并以4米每秒的速度在踏石上行走，展示了其在复杂地形中的优越动态能力。这些结果表明，所提出的方法在地形适应性上显著优于以往技术。

## 🎯 应用场景

该研究的潜在应用领域包括救援任务、探索未知环境以及军事行动等，能够显著提升四足机器人在复杂地形中的自主导航能力。未来，该技术可能会推动机器人在更广泛的实际场景中的应用，提升其智能化水平。

## 📄 摘要（原文）

> High-speed legged navigation in discrete and geometrically complex environments is a challenging task because of the high-degree-of-freedom dynamics and long-horizon, nonconvex nature of the optimization problem. In this work, we propose a hierarchical navigation pipeline for legged robots that can traverse such environments at high speed. The proposed pipeline consists of a planner and tracker module. The planner module finds physically feasible foothold plans by sampling-based optimization with fast sequential filtering using heuristics and a neural network. Subsequently, rollouts are performed in a physics simulation to identify the best foothold plan regarding the engineered cost function and to confirm its physical consistency. This hierarchical planning module is computationally efficient and physically accurate at the same time. The tracker aims to accurately step on the target footholds from the planning module. During the training stage, the foothold target distribution is given by a generative model that is trained competitively with the tracker. This process ensures that the tracker is trained in an environment with the desired difficulty. The resulting tracker can overcome terrains that are more difficult than what the previous methods could manage. We demonstrated our approach using Raibo, our in-house dynamic quadruped robot. The results were dynamic and agile motions: Raibo is capable of running on vertical walls, jumping a 1.3-meter gap, running over stepping stones at 4 meters per second, and autonomously navigating on terrains full of 30° ramps, stairs, and boxes of various sizes.

