---
layout: default
title: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy
---

# Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01247" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01247v2</a>
  <a href="https://arxiv.org/pdf/2508.01247.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01247v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01247v2', 'Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Buqing Nie, Yang Zhang, Rongjun Jin, Zhanxiang Cao, Huangxuan Lin, Xiaokang Yang, Yue Gao

**分类**: cs.RO

**发布日期**: 2025-08-02 (更新: 2025-11-16)

**备注**: AAAI 2026 accepted

---

## 💡 一句话要点

**提出对称等变策略以解决类人机器人运动协调问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `类人机器人` `深度强化学习` `对称性` `运动协调` `速度跟踪` `时空协调性` `机器人控制`

## 📋 核心要点

1. 现有的深度强化学习方法未能充分利用类人机器人的形态对称性，导致运动表现不佳和协调性不足。
2. 本文提出的对称等变策略（SE-Policy）通过在演员和评论者中嵌入对称性，增强了机器人的运动协调性。
3. 在Unitree G1类人机器人上进行的实验表明，SE-Policy在速度跟踪任务中提高了跟踪精度达40%，并实现了更好的时空协调性。

## 📝 摘要（中文）

人类神经系统具有双侧对称性，使得运动协调和平衡成为可能。然而，现有的深度强化学习方法忽视了类人机器人的形态对称性，导致运动不协调和表现不佳。受人类运动控制的启发，本文提出了一种新的深度强化学习框架——对称等变策略（SE-Policy），该策略在演员中嵌入严格的对称等变性，在评论者中嵌入对称不变性，无需额外的超参数。SE-Policy在对称观察下强制执行一致行为，产生时空协调的运动，提升任务表现。通过在Unitree G1类人机器人上进行的速度跟踪任务的广泛实验，SE-Policy的跟踪精度比最先进的基线提高了40%，同时实现了更优的时空协调性。这些结果证明了SE-Policy的有效性及其在类人机器人中的广泛适用性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有深度强化学习方法在类人机器人运动控制中忽视形态对称性的问题，导致的运动不协调和表现不佳。

**核心思路**：提出对称等变策略（SE-Policy），通过在演员中嵌入对称等变性和在评论者中嵌入对称不变性，来增强机器人的运动协调性和表现。

**技术框架**：SE-Policy的整体架构包括两个主要模块：演员网络和评论者网络。演员网络负责生成动作，而评论者网络评估这些动作的价值。

**关键创新**：SE-Policy的核心创新在于其对称性设计，使得机器人在对称观察下能够执行一致的行为，这一设计与传统方法的无对称性处理形成鲜明对比。

**关键设计**：在网络结构上，SE-Policy不需要额外的超参数设置，损失函数设计上考虑了对称性约束，确保了模型在训练过程中的稳定性和协调性。

## 📊 实验亮点

实验结果表明，SE-Policy在速度跟踪任务中相比于最先进的基线提升了跟踪精度达40%，同时在时空协调性方面表现优越。这些结果验证了该方法的有效性和广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、医疗辅助机器人和娱乐机器人等。通过提高类人机器人的运动协调性，SE-Policy能够在复杂环境中实现更自然的交互和任务执行，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The human nervous system exhibits bilateral symmetry, enabling coordinated and balanced movements. However, existing Deep Reinforcement Learning (DRL) methods for humanoid robots neglect morphological symmetry of the robot, leading to uncoordinated and suboptimal behaviors. Inspired by human motor control, we propose Symmetry Equivariant Policy (SE-Policy), a new DRL framework that embeds strict symmetry equivariance in the actor and symmetry invariance in the critic without additional hyperparameters. SE-Policy enforces consistent behaviors across symmetric observations, producing temporally and spatially coordinated motions with higher task performance. Extensive experiments on velocity tracking tasks, conducted in both simulation and real-world deployment with the Unitree G1 humanoid robot, demonstrate that SE-Policy improves tracking accuracy by up to 40% compared to state-of-the-art baselines, while achieving superior spatial-temporal coordination. These results demonstrate the effectiveness of SE-Policy and its broad applicability to humanoid robots.

