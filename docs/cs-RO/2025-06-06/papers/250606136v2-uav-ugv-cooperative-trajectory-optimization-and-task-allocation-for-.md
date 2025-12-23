---
layout: default
title: UAV-UGV Cooperative Trajectory Optimization and Task Allocation for Medical Rescue Tasks in Post-Disaster Environments
---

# UAV-UGV Cooperative Trajectory Optimization and Task Allocation for Medical Rescue Tasks in Post-Disaster Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06136" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06136v2</a>
  <a href="https://arxiv.org/pdf/2506.06136.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06136v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06136v2', 'UAV-UGV Cooperative Trajectory Optimization and Task Allocation for Medical Rescue Tasks in Post-Disaster Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiyuan Chen, Wanpeng Zhao, Yongxi Liu, Yuanqing Xia, Wannian Liang, Shuo Wang

**分类**: cs.RO, cs.MA

**发布日期**: 2025-06-06 (更新: 2025-08-28)

---

## 💡 一句话要点

**提出无人机与地面无人车协作优化方案以解决灾后医疗救援问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `无人机` `无人地面车辆` `任务分配` `轨迹优化` `遗传算法` `CMA-ES` `灾后救援`

## 📋 核心要点

1. 在灾后环境中，基础设施损坏严重，导致医疗资源的快速交付面临巨大挑战。
2. 本文提出了一种结合遗传算法和信息化快速随机树星算法的协作轨迹优化与任务分配框架。
3. 仿真实验结果显示，所提方法在任务完成时间和行驶距离上均显著优于传统方法，提升效果明显。

## 📝 摘要（中文）

在灾后场景中，快速高效地交付医疗资源至关重要，但基础设施的严重损坏使得这一任务充满挑战。为此，本文提出了一种基于无人机（UAV）和无人地面车辆（UGV）的协作轨迹优化和任务分配框架。该研究结合遗传算法（GA）进行多无人机和无人车之间的高效任务分配，并采用信息化快速随机树星（informed-RRT*）算法生成无碰撞轨迹。通过协方差矩阵自适应进化策略（CMA-ES）进一步优化任务排序和路径效率。仿真实验表明，与传统策略相比，所提方法显著提高了医疗救援操作的整体效率，完成15项任务的总时间缩短至26.7分钟，优于K均值聚类和随机分配超过73%。此外，经过CMA-ES优化后，总行驶距离减少了15.1%。

## 🔬 方法详解

**问题定义**：本文旨在解决灾后环境中医疗资源交付效率低下的问题。现有方法在任务分配和轨迹规划上缺乏有效的协作机制，导致资源利用不充分和时间延误。

**核心思路**：论文的核心思路是通过结合无人机和无人地面车辆的优势，采用遗传算法进行任务分配，并利用信息化快速随机树星算法生成无碰撞轨迹，从而提高整体任务执行效率。

**技术框架**：整体框架包括任务分配模块、轨迹规划模块和优化模块。首先，利用遗传算法进行任务分配，然后通过信息化快速随机树星算法生成轨迹，最后使用CMA-ES进行路径优化。

**关键创新**：最重要的技术创新在于将遗传算法与信息化快速随机树星算法结合，形成了一种新的协作优化框架，显著提升了任务分配和轨迹规划的效率。与现有方法相比，该框架在多无人机和无人车的协作中表现出更好的适应性和效率。

**关键设计**：在参数设置上，遗传算法的种群规模和交叉率经过调优，以确保任务分配的多样性和有效性；信息化快速随机树星算法的采样策略和扩展策略经过优化，以提高轨迹生成的效率和安全性。

## 📊 实验亮点

实验结果表明，所提方法在15项任务场景下，总任务完成时间缩短至26.7分钟，较K均值聚类和随机分配提升超过73%。经过CMA-ES优化后，总行驶距离减少了15.1%，显示出显著的优化效果。

## 🎯 应用场景

该研究的潜在应用领域包括灾后救援、紧急医疗服务和物流配送等。通过优化无人机和无人地面车辆的协作，能够在灾后环境中快速有效地提供医疗资源，提升救援效率，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> In post-disaster scenarios, rapid and efficient delivery of medical resources is critical and challenging due to severe damage to infrastructure. To provide an optimized solution, we propose a cooperative trajectory optimization and task allocation framework leveraging unmanned aerial vehicles (UAVs) and unmanned ground vehicles (UGVs). This study integrates a Genetic Algorithm (GA) for efficient task allocation among multiple UAVs and UGVs, and employs an informed-RRT* (Rapidly-exploring Random Tree Star) algorithm for collision-free trajectory generation. Further optimization of task sequencing and path efficiency is conducted using Covariance Matrix Adaptation Evolution Strategy (CMA-ES). Simulation experiments conducted in a realistic post-disaster environment demonstrate that our proposed approach significantly improves the overall efficiency of medical rescue operations compared to traditional strategies. Specifically, our method reduces the total mission completion time to 26.7 minutes for a 15-task scenario, outperforming K-Means clustering and random allocation by over 73%. Furthermore, the framework achieves a substantial 15.1% reduction in total traveled distance after CMA-ES optimization. The cooperative utilization of UAVs and UGVs effectively balances their complementary advantages, highlighting the system's scalability and practicality for real-world deployment.

