---
layout: default
title: Efficient Navigation Among Movable Obstacles using a Mobile Manipulator via Hierarchical Policy Learning
---

# Efficient Navigation Among Movable Obstacles using a Mobile Manipulator via Hierarchical Policy Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15380" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15380v1</a>
  <a href="https://arxiv.org/pdf/2506.15380.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15380v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15380v1', 'Efficient Navigation Among Movable Obstacles using a Mobile Manipulator via Hierarchical Policy Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taegeun Yang, Jiwoo Hwang, Jeil Jeong, Minsung Yoon, Sung-Eui Yoon

**分类**: cs.RO

**发布日期**: 2025-06-18

**备注**: 8 pages, 6 figures, Accepted to IROS 2025. Supplementary Video: https://youtu.be/sZ8_z7sYVP0

---

## 💡 一句话要点

**提出层次化强化学习框架以解决可移动障碍物导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `层次化强化学习` `可移动障碍物` `动态环境` `路径跟踪` `机器人导航` `智能操控` `仿真实验`

## 📋 核心要点

1. 现有方法在处理动态环境中的可移动障碍物时，往往缺乏灵活性和实时性，难以有效执行导航任务。
2. 本研究提出的层次化强化学习框架，通过高低层策略的协同作用，实现了对障碍物的动态推送和路径跟踪。
3. 实验结果显示，该方法在成功率、路径长度和到达时间上均显著优于现有基线，验证了其有效性。

## 📝 摘要（中文）

我们提出了一种层次化强化学习（HRL）框架，用于高效地在可移动障碍物中导航（NAMO），结合了基于交互的障碍物属性估计与结构化推送策略。这种方法能够在遵循预先规划的全局路径的同时，动态处理意外障碍物。高层策略生成考虑环境约束和路径跟踪目标的推送命令，而低层策略则通过协调的全身运动精确稳定地执行这些命令。综合的基于仿真的实验表明，与基线相比，该方法在NAMO任务中表现出更高的成功率、缩短的行进路径长度和减少的到达目标时间。此外，消融研究评估了各个组件的有效性，定性分析进一步验证了实时障碍物属性估计的准确性和可靠性。

## 🔬 方法详解

**问题定义**：本论文旨在解决在动态环境中可移动障碍物导航（NAMO）的问题。现有方法在处理意外障碍物时，往往缺乏灵活性，导致导航效率低下。

**核心思路**：论文提出的层次化强化学习框架，通过高层策略生成推送命令和低层策略执行命令的方式，能够动态适应环境变化，确保路径跟踪的稳定性和准确性。

**技术框架**：整体架构包括高层策略和低层策略两个主要模块。高层策略负责生成考虑环境约束的推送命令，而低层策略则通过协调的全身运动来执行这些命令。

**关键创新**：最重要的技术创新在于将交互式障碍物属性估计与结构化推送策略相结合，使得移动操控器能够在复杂环境中高效导航。这一方法与传统的单一策略方法有本质区别。

**关键设计**：在设计中，采用了特定的损失函数来优化策略的执行效果，并通过仿真环境进行参数调优，以确保高层和低层策略的有效协同。

## 📊 实验亮点

实验结果表明，提出的方法在NAMO任务中实现了更高的成功率（具体数据未知）、缩短了行进路径长度（具体数据未知），并减少了到达目标的时间（具体数据未知），相较于基线方法有显著提升，验证了其有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、仓储物流和服务机器人等场景，能够显著提升机器人在复杂环境中的导航能力和灵活性。未来，该方法有望推动自主移动机器人在动态环境中的广泛应用，提升其智能化水平。

## 📄 摘要（原文）

> We propose a hierarchical reinforcement learning (HRL) framework for efficient Navigation Among Movable Obstacles (NAMO) using a mobile manipulator. Our approach combines interaction-based obstacle property estimation with structured pushing strategies, facilitating the dynamic manipulation of unforeseen obstacles while adhering to a pre-planned global path. The high-level policy generates pushing commands that consider environmental constraints and path-tracking objectives, while the low-level policy precisely and stably executes these commands through coordinated whole-body movements. Comprehensive simulation-based experiments demonstrate improvements in performing NAMO tasks, including higher success rates, shortened traversed path length, and reduced goal-reaching times, compared to baselines. Additionally, ablation studies assess the efficacy of each component, while a qualitative analysis further validates the accuracy and reliability of the real-time obstacle property estimation.

