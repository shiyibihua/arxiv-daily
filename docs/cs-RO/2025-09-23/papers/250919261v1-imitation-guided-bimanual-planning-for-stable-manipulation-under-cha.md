---
layout: default
title: Imitation-Guided Bimanual Planning for Stable Manipulation under Changing External Forces
---

# Imitation-Guided Bimanual Planning for Stable Manipulation under Changing External Forces

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19261" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19261v1</a>
  <a href="https://arxiv.org/pdf/2509.19261.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19261v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19261v1', 'Imitation-Guided Bimanual Planning for Stable Manipulation under Changing External Forces')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kuanqi Cai, Chunfeng Wang, Zeqi Li, Haowen Yao, Weinan Chen, Luis Figueredo, Aude Billard, Arash Ajoudani

**分类**: cs.RO

**发布日期**: 2025-09-23

**期刊**: IROS 2025

---

## 💡 一句话要点

**提出模仿引导的双臂规划框架，解决动态环境下稳定操作的抓取过渡问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `双臂机器人` `抓取规划` `模仿学习` `运动规划` `动态环境`

## 📋 核心要点

1. 现有抓取过渡策略难以应对变化的外力和复杂运动约束，无法有效优化运动性能。
2. 该框架通过模仿学习引导，结合抓取流形采样和分层运动规划，实现稳定高效的抓取过渡。
3. 实验结果表明，该方法在抓取过渡效率和运动性能方面均有显著提升，适用于力密集型任务。

## 📝 摘要（中文）

本文提出了一种模仿引导的双臂规划框架，旨在提升机器人在动态环境中操作的稳定性和灵活性。该框架集成了高效的抓取过渡策略和运动性能优化，以实现不同抓取类型之间的无缝切换。我们引入了在抓取流形中采样稳定交点的策略，从而简化单手和双手抓取之间的过渡，降低计算成本和重新抓取的低效性。此外，分层双阶段运动架构结合了基于模仿学习的全局路径生成器和基于二次规划的局部规划器，确保实时运动可行性、避障和卓越的可操作性。通过一系列力密集型任务的评估，证明了该方法在抓取过渡效率和运动性能方面的显著改进。

## 🔬 方法详解

**问题定义**：论文旨在解决动态环境中机器人操作时，由于外部力变化导致的抓取不稳定和抓取过渡效率低下的问题。现有方法通常难以兼顾抓取过渡的平滑性、稳定性和运动性能，尤其是在需要频繁切换单手和双手抓取时，计算成本高，重新抓取效率低。

**核心思路**：论文的核心思路是利用模仿学习先验知识引导双臂运动规划，同时优化抓取过渡策略，从而实现稳定、高效且实时的机器人操作。通过模仿学习，机器人可以学习到人类操作的经验，从而更好地适应动态环境中的外部干扰。

**技术框架**：该框架主要包含两个核心模块：一是抓取流形中的稳定交点采样策略，用于高效地进行单手和双手抓取之间的过渡；二是分层双阶段运动架构，包括基于模仿学习的全局路径生成器和基于二次规划的局部规划器。全局路径生成器负责生成粗略的运动轨迹，局部规划器则在此基础上进行优化，确保运动可行性、避障和可操作性。

**关键创新**：该方法的主要创新点在于：1) 提出了在抓取流形中采样稳定交点的策略，显著降低了抓取过渡的计算复杂度；2) 结合模仿学习和二次规划，构建了分层双阶段运动架构，实现了实时性、稳定性和运动性能的有效平衡。与传统方法相比，该方法能够更好地适应动态环境中的外部干扰，并实现更平滑、更高效的抓取过渡。

**关键设计**：在抓取流形采样方面，论文设计了一种特定的采样策略，以确保采样的抓取姿态具有较高的稳定性。在分层运动规划方面，模仿学习模块使用专家示教数据进行训练，学习人类操作的运动模式。二次规划模块则根据当前环境状态和任务目标，对运动轨迹进行优化，例如最小化关节力矩、避免碰撞等。具体的参数设置和损失函数选择需要根据具体的任务和机器人平台进行调整。

## 📊 实验亮点

实验结果表明，该方法在抓取过渡效率和运动性能方面均有显著提升。与传统方法相比，该方法能够更快速地完成抓取过渡，并保持更高的操作稳定性。具体的性能数据（例如抓取过渡时间、操作稳定性指标等）需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于各种需要在动态环境中进行稳定操作的机器人任务，例如：工业装配、医疗手术、家庭服务等。在工业装配中，机器人可以利用该方法灵活地抓取和操作零件，提高生产效率。在医疗手术中，机器人可以更加稳定地进行微创手术，降低手术风险。在家庭服务中，机器人可以安全地处理各种日常物品，提升生活质量。

## 📄 摘要（原文）

> Robotic manipulation in dynamic environments often requires seamless transitions between different grasp types to maintain stability and efficiency. However, achieving smooth and adaptive grasp transitions remains a challenge, particularly when dealing with external forces and complex motion constraints. Existing grasp transition strategies often fail to account for varying external forces and do not optimize motion performance effectively. In this work, we propose an Imitation-Guided Bimanual Planning Framework that integrates efficient grasp transition strategies and motion performance optimization to enhance stability and dexterity in robotic manipulation. Our approach introduces Strategies for Sampling Stable Intersections in Grasp Manifolds for seamless transitions between uni-manual and bi-manual grasps, reducing computational costs and regrasping inefficiencies. Additionally, a Hierarchical Dual-Stage Motion Architecture combines an Imitation Learning-based Global Path Generator with a Quadratic Programming-driven Local Planner to ensure real-time motion feasibility, obstacle avoidance, and superior manipulability. The proposed method is evaluated through a series of force-intensive tasks, demonstrating significant improvements in grasp transition efficiency and motion performance. A video demonstrating our simulation results can be viewed at \href{https://youtu.be/3DhbUsv4eDo}{\textcolor{blue}{https://youtu.be/3DhbUsv4eDo} }.

