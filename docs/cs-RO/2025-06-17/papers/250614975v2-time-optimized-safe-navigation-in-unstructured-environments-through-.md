---
layout: default
title: Time-Optimized Safe Navigation in Unstructured Environments through Learning Based Depth Completion
---

# Time-Optimized Safe Navigation in Unstructured Environments through Learning Based Depth Completion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14975" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14975v2</a>
  <a href="https://arxiv.org/pdf/2506.14975.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14975v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14975v2', 'Time-Optimized Safe Navigation in Unstructured Environments through Learning Based Depth Completion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeffrey Mao, Raghuram Cauligi Srinivas, Steven Nogar, Giuseppe Loianno

**分类**: cs.RO

**发布日期**: 2025-06-17 (更新: 2025-10-05)

---

## 💡 一句话要点

**提出基于学习的深度补全方法以解决无人机在复杂环境中的安全导航问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `无人机导航` `深度学习` `环境建模` `路径规划` `实时决策` `安全避障` `三维地图`

## 📋 核心要点

1. 现有方法在复杂环境中导航时面临实时决策和计算复杂度高的问题，尤其是对小型无人机而言。
2. 提出了一种基于轻量级传感器的实时导航系统，结合立体和单目学习的深度估计，构建稠密三维地图。
3. 实验结果表明，系统在计算效率和障碍物避让方面优于现有方法，能够在未知环境中安全导航。

## 📝 摘要（中文）

四旋翼无人机在农业、搜索救援和基础设施检查等多个应用中具有重要潜力。实现自主操作需要系统能够安全地在复杂和未知的环境中导航。由于环境的复杂性以及对实时决策的需求，尤其是在受限于尺寸、重量和功率的情况下，使用传统的激光雷达进行映射变得不切实际。为了解决这些挑战，本文提出了一种完全基于轻量级传感器的实时导航系统，利用新颖的视觉深度估计方法构建环境的稠密三维地图，并引入了一种新的规划和轨迹生成框架，能够快速计算时间最优的全局轨迹。通过在多种室内外环境中的自主飞行实验验证了系统的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决四旋翼无人机在复杂和未知环境中安全导航的问题。现有方法通常依赖于重型传感器（如激光雷达），在尺寸、重量和功率受限的情况下难以实现实时导航。

**核心思路**：论文提出了一种完全基于轻量级传感器的实时导航系统，通过融合立体和单目深度学习方法，构建稠密的三维环境地图，从而实现安全且高效的路径规划。

**技术框架**：系统整体架构包括三个主要模块：环境深度估计模块、地图构建模块和轨迹规划模块。深度估计模块负责生成环境的三维地图，地图构建模块则根据新获取的深度信息不断更新地图，轨迹规划模块则计算时间最优的安全轨迹。

**关键创新**：最重要的技术创新在于提出了一种融合立体和单目深度学习的新方法，生成的深度图比传统立体方法更长距离、更稠密且噪声更少。这一创新使得在复杂环境中进行实时导航成为可能。

**关键设计**：在深度估计中，采用了特定的损失函数以优化深度图的质量，同时在轨迹规划中引入了高效的算法以确保计算速度和路径的安全性。

## 📊 实验亮点

实验结果显示，所提出的导航系统在多种室内外环境中表现出色，计算效率显著提高，能够保证障碍物避让的同时，成功实现时间最优的轨迹规划。与现有方法相比，系统在实时性和安全性方面均有明显提升。

## 🎯 应用场景

该研究的潜在应用领域包括农业监测、灾后搜索与救援、基础设施检查等。通过实现无人机在复杂环境中的安全自主导航，能够大幅提升这些领域的工作效率和安全性，未来可能推动无人机技术的广泛应用。

## 📄 摘要（原文）

> Quadrotors hold significant promise for several applications such as agriculture, search and rescue, and infrastructure inspection. Achieving autonomous operation requires systems to navigate safely through complex and unfamiliar environments. This level of autonomy is particularly challenging due to the complexity of such environments and the need for real-time decision making especially for platforms constrained by size, weight, and power (SWaP), which limits flight time and precludes the use of bulky sensors like Light Detection and Ranging (LiDAR) for mapping. Furthermore, computing globally optimal, collision-free paths and translating them into time-optimized, safe trajectories in real time adds significant computational complexity. To address these challenges, we present a fully onboard, real-time navigation system that relies solely on lightweight onboard sensors. Our system constructs a dense 3D map of the environment using a novel visual depth estimation approach that fuses stereo and monocular learning-based depth, yielding longer-range, denser, and less noisy depth maps than conventional stereo methods. Building on this map, we introduce a novel planning and trajectory generation framework capable of rapidly computing time-optimal global trajectories. As the map is incrementally updated with new depth information, our system continuously refines the trajectory to maintain safety and optimality. Both our planner and trajectory generator outperforms state-of-the-art methods in terms of computational efficiency and guarantee obstacle-free trajectories. We validate our system through robust autonomous flight experiments in diverse indoor and outdoor environments, demonstrating its effectiveness for safe navigation in previously unknown settings.

