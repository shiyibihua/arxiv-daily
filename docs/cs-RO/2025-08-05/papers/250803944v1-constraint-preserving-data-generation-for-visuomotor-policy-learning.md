---
layout: default
title: Constraint-Preserving Data Generation for Visuomotor Policy Learning
---

# Constraint-Preserving Data Generation for Visuomotor Policy Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03944" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03944v1</a>
  <a href="https://arxiv.org/pdf/2508.03944.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03944v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03944v1', 'Constraint-Preserving Data Generation for Visuomotor Policy Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kevin Lin, Varun Ragunath, Andrew McAlinden, Aaditya Prasad, Jimmy Wu, Yuke Zhu, Jeannette Bohg

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-05

**备注**: CoRL 2025. Website: https://cp-gen.github.io

---

## 💡 一句话要点

**提出约束保持数据生成方法以提升机器人策略学习**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `约束保持` `数据生成` `视觉运动策略` `机器人操作` `几何感知` `关键点轨迹` `零样本迁移`

## 📋 核心要点

1. 现有方法在收集大规模演示数据时面临高成本和时间消耗的问题，限制了机器人操作的应用。
2. 本文提出的CP-Gen方法通过单一专家轨迹生成新颖的机器人演示，利用关键点轨迹约束实现几何感知的数据生成。
3. 实验结果显示，CP-Gen训练的策略在多种任务中取得了77%的成功率，显著优于现有最佳方法的50%。

## 📝 摘要（中文）

大规模演示数据推动了机器人操作的关键突破，但数据收集仍然成本高昂且耗时。本文提出了一种约束保持数据生成方法（CP-Gen），利用单一专家轨迹生成包含新颖物体几何形状和姿态的机器人演示。这些生成的演示用于训练闭环视觉运动策略，能够在零样本条件下迁移到现实世界，并在物体几何形状和姿态的变化中实现泛化。CP-Gen通过将机器人技能表述为关键点轨迹约束，实现了几何感知的数据生成。实验表明，使用CP-Gen训练的策略在16个仿真任务和4个现实任务中平均成功率达到77%，显著优于最佳基线的50%。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人操作中大规模演示数据收集成本高、时间长的问题。现有方法在生成多样化的机器人演示时，往往无法有效考虑物体的几何形状和姿态变化。

**核心思路**：CP-Gen通过将专家演示分解为自由空间运动和机器人技能，利用关键点轨迹约束实现几何感知的数据生成。这种设计使得生成的演示能够更好地适应不同的物体几何形状和姿态。

**技术框架**：CP-Gen的整体流程包括从专家轨迹中提取关键点，针对每个任务相关物体进行姿态和几何变换采样，优化机器人关节配置以跟踪变换后的关键点轨迹，并规划无碰撞路径。

**关键创新**：CP-Gen的主要创新在于将机器人技能表述为关键点轨迹约束，这一方法与以往仅依赖姿态变化的生成方法有本质区别，能够更好地捕捉物体几何特征。

**关键设计**：在实现过程中，CP-Gen对关键点的选择、变换的采样策略以及优化算法进行了精心设计，以确保生成的演示在多样性和有效性之间取得平衡。

## 📊 实验亮点

实验结果显示，使用CP-Gen训练的策略在16个仿真任务和4个现实任务中达到了77%的平均成功率，显著高于最佳基线的50%。这一成果表明CP-Gen在提升机器人操作能力方面具有显著效果。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和人机协作等。通过减少对大量演示数据的依赖，CP-Gen能够加速机器人学习过程，提高其在复杂环境中的适应能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large-scale demonstration data has powered key breakthroughs in robot manipulation, but collecting that data remains costly and time-consuming. We present Constraint-Preserving Data Generation (CP-Gen), a method that uses a single expert trajectory to generate robot demonstrations containing novel object geometries and poses. These generated demonstrations are used to train closed-loop visuomotor policies that transfer zero-shot to the real world and generalize across variations in object geometries and poses. Similar to prior work using pose variations for data generation, CP-Gen first decomposes expert demonstrations into free-space motions and robot skills. But unlike those works, we achieve geometry-aware data generation by formulating robot skills as keypoint-trajectory constraints: keypoints on the robot or grasped object must track a reference trajectory defined relative to a task-relevant object. To generate a new demonstration, CP-Gen samples pose and geometry transforms for each task-relevant object, then applies these transforms to the object and its associated keypoints or keypoint trajectories. We optimize robot joint configurations so that the keypoints on the robot or grasped object track the transformed keypoint trajectory, and then motion plan a collision-free path to the first optimized joint configuration. Experiments on 16 simulation tasks and four real-world tasks, featuring multi-stage, non-prehensile and tight-tolerance manipulation, show that policies trained using CP-Gen achieve an average success rate of 77%, outperforming the best baseline that achieves an average of 50%.

