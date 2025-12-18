---
layout: default
title: Autonomous UAV-Quadruped Docking in Complex Terrains via Active Posture Alignment and Constraint-Aware Control
---

# Autonomous UAV-Quadruped Docking in Complex Terrains via Active Posture Alignment and Constraint-Aware Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21571" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21571v1</a>
  <a href="https://arxiv.org/pdf/2509.21571.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21571v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21571v1', 'Autonomous UAV-Quadruped Docking in Complex Terrains via Active Posture Alignment and Constraint-Aware Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: HaoZhe Xu, Cheng Cheng, HongRui Sang, Zhipeng Wang, Qiyong He, Xiuxian Li, Bin He

**分类**: cs.RO

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**提出一种主动姿态对齐和约束感知控制的无人机-四足机器人复杂地形自主对接框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无人机` `四足机器人` `自主对接` `复杂地形` `深度强化学习` `约束感知控制` `视觉跟踪`

## 📋 核心要点

1. 现有无人机-地面机器人对接方法主要依赖轮式平台，在复杂地形的探索能力受限，而四足机器人姿态变化频繁，难以提供稳定着陆平台。
2. 该论文提出一种无人机-四足机器人自主对接框架，四足机器人通过强化学习稳定躯干，无人机采用三阶段控制策略实现精准对接。
3. 实验结果表明，该框架能够在复杂地形（如楼梯和陡坡）上成功实现无人机与四足机器人的自主对接，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种用于GPS拒止环境下的无人机（UAV）与地面机器人自主对接框架。现有方法主要针对轮式平台，其有限的移动性限制了在复杂地形中的探索。四足机器人具有更强的适应性，但其频繁的姿态变化难以提供稳定的无人机着陆平台。为了解决这些挑战，我们提出了一种自主的无人机-四足机器人对接框架。在四足机器人端，通过深度强化学习训练的混合内部模型与水平对齐（HIM-HA）主动稳定躯干，以提供水平平台。在无人机端，采用三阶段策略，包括使用中值滤波YOLOv8检测器的远程捕获、使用约束感知控制的近距离跟踪（该控制器集成了非奇异快速终端滑模控制器（NFTSMC）和对数障碍函数（BF），以保证在视场（FOV）约束下有限时间误差收敛）以及由安全周期（SP）机制引导的终端下降，该机制共同验证跟踪精度和平台稳定性。所提出的框架在仿真和真实场景中都得到了验证，成功地实现了在高于17厘米的室外楼梯和陡于30度的粗糙斜坡上的对接。

## 🔬 方法详解

**问题定义**：该论文旨在解决在GPS拒止的复杂地形中，无人机与四足机器人自主对接的问题。现有方法主要依赖轮式机器人，其移动性在复杂地形受限。而四足机器人虽然适应性强，但姿态变化频繁，难以提供稳定的着陆平台，导致无人机对接困难。

**核心思路**：论文的核心思路是分别在四足机器人和无人机端进行优化。四足机器人通过深度强化学习训练的混合内部模型（HIM）主动稳定躯干，提供水平的对接平台。无人机则采用三阶段控制策略，实现从远距离目标捕获到近距离精准对接的平稳过渡。

**技术框架**：整体框架分为四足机器人端和无人机端。四足机器人端使用HIM-HA模型稳定躯干。无人机端分为三个阶段：1) 远程捕获：使用YOLOv8检测器识别四足机器人，并进行中值滤波以提高鲁棒性；2) 近距离跟踪：采用约束感知控制器，结合NFTSMC和对数BF，保证在视场约束下快速收敛；3) 终端下降：使用安全周期（SP）机制，同时验证跟踪精度和平台稳定性，引导无人机安全着陆。

**关键创新**：主要创新点在于：1) 提出了一种基于深度强化学习的四足机器人躯干稳定方法（HIM-HA），能够在复杂地形下提供稳定的对接平台；2) 设计了一种约束感知控制器，集成了NFTSMC和对数BF，保证了在视场约束下的快速和稳定的跟踪；3) 提出了安全周期（SP）机制，用于在终端下降阶段验证跟踪精度和平台稳定性，确保安全着陆。

**关键设计**：HIM-HA模型的具体网络结构和强化学习奖励函数未知。约束感知控制器中，NFTSMC的具体参数设置未知，对数BF的具体形式未知。安全周期（SP）机制中，跟踪精度和平台稳定性的具体阈值设置未知。YOLOv8检测器的具体配置未知。

## 📊 实验亮点

该框架在仿真和真实场景中都得到了验证，成功地实现了在高于17厘米的室外楼梯和陡于30度的粗糙斜坡上的对接。这些实验结果表明，该框架具有很强的鲁棒性和适应性，能够在复杂地形下实现无人机与四足机器人的自主对接。

## 🎯 应用场景

该研究成果可应用于复杂地形下的物资运输、环境监测、灾后救援等领域。例如，在灾区，无人机可以携带物资自主降落在四足机器人背上，由四足机器人将物资运送到救援人员手中。此外，该技术还可用于军事侦察、农业巡检等场景，具有广泛的应用前景和实际价值。

## 📄 摘要（原文）

> Autonomous docking between Unmanned Aerial Vehicles (UAVs) and ground robots is essential for heterogeneous systems, yet most existing approaches target wheeled platforms whose limited mobility constrains exploration in complex terrains. Quadruped robots offer superior adaptability but undergo frequent posture variations, making it difficult to provide a stable landing surface for UAVs. To address these challenges, we propose an autonomous UAV-quadruped docking framework for GPS-denied environments. On the quadruped side, a Hybrid Internal Model with Horizontal Alignment (HIM-HA), learned via deep reinforcement learning, actively stabilizes the torso to provide a level platform. On the UAV side, a three-phase strategy is adopted, consisting of long-range acquisition with a median-filtered YOLOv8 detector, close-range tracking with a constraint-aware controller that integrates a Nonsingular Fast Terminal Sliding Mode Controller (NFTSMC) and a logarithmic Barrier Function (BF) to guarantee finite-time error convergence under field-of-view (FOV) constraints, and terminal descent guided by a Safety Period (SP) mechanism that jointly verifies tracking accuracy and platform stability. The proposed framework is validated in both simulation and real-world scenarios, successfully achieving docking on outdoor staircases higher than 17 cm and rough slopes steeper than 30 degrees. Supplementary materials and videos are available at: https://uav-quadruped-docking.github.io.

