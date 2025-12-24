---
layout: default
title: Jacobian Exploratory Dual-Phase Reinforcement Learning for Dynamic Endoluminal Navigation of Deformable Continuum Robots
---

# Jacobian Exploratory Dual-Phase Reinforcement Learning for Dynamic Endoluminal Navigation of Deformable Continuum Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00329" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00329v1</a>
  <a href="https://arxiv.org/pdf/2509.00329.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00329v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00329v1', 'Jacobian Exploratory Dual-Phase Reinforcement Learning for Dynamic Endoluminal Navigation of Deformable Continuum Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Tian, Chi Kit Ng, Hongliang Ren

**分类**: cs.RO, cs.AI, eess.SY

**发布日期**: 2025-08-30

---

## 💡 一句话要点

**提出Jacobian探索双相强化学习以解决可变形连续机器人导航问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `可变形机器人` `强化学习` `雅可比估计` `动态导航` `医疗机器人` `策略优化` `仿真测试`

## 📋 核心要点

1. 现有方法在可变形连续机器人导航中面临非线性变形和部分可观测性的问题，导致强化学习效果不佳。
2. 论文提出的JEDP-RL框架通过分阶段的雅可比估计和策略执行，增强了状态表示的马尔可夫性。
3. 实验结果显示，JEDP-RL在收敛速度上比PPO快3.2倍，导航效率提高25%，在未见组织环境中成功率提高33%。

## 📝 摘要（中文）

可变形连续机器人（DCRs）由于非线性变形力学和部分状态可观测性，给规划带来了独特的挑战，违反了传统强化学习（RL）方法的马尔可夫假设。尽管基于雅可比的方法为刚性操纵器提供了理论基础，但由于时变运动学和欠驱动变形动力学，其在DCRs中的直接应用仍然有限。本文提出了Jacobian探索双相强化学习（JEDP-RL）框架，将规划分解为相位雅可比估计和策略执行。在每个训练步骤中，首先执行小规模局部探索动作以估计变形雅可比矩阵，然后通过雅可比特征增强状态表示，以恢复近似马尔可夫性。大量SOFA外科动态仿真实验表明，JEDP-RL在收敛速度、导航效率和泛化能力上均优于近端策略优化（PPO）基线。

## 🔬 方法详解

**问题定义**：本文旨在解决可变形连续机器人在动态导航中的规划问题，现有方法因非线性变形和部分可观测性而难以有效应用。

**核心思路**：JEDP-RL框架通过分解规划过程为雅可比估计和策略执行，利用局部探索动作来估计雅可比矩阵，从而增强状态表示的马尔可夫性。

**技术框架**：该框架包括两个主要阶段：第一阶段是小规模局部探索以估计变形雅可比矩阵，第二阶段是基于增强状态表示的策略执行。

**关键创新**：JEDP-RL的核心创新在于通过雅可比特征的引入，克服了传统RL方法在DCRs中的局限性，显著提高了学习效率和导航性能。

**关键设计**：在参数设置上，采用了适应性学习率和特定的损失函数来优化雅可比矩阵的估计，网络结构则结合了卷积神经网络和强化学习策略网络，以实现高效的状态表示和决策。

## 📊 实验亮点

实验结果表明，JEDP-RL在收敛速度上比PPO快3.2倍，导航效率提高25%，在材料属性变化下成功率达到92%，在未见组织环境中的成功率为83%，比PPO高出33%。

## 🎯 应用场景

该研究具有广泛的应用潜力，特别是在医疗机器人、微创手术和复杂环境下的自动导航等领域。通过提高可变形机器人在动态环境中的导航能力，能够显著提升手术的安全性和效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Deformable continuum robots (DCRs) present unique planning challenges due to nonlinear deformation mechanics and partial state observability, violating the Markov assumptions of conventional reinforcement learning (RL) methods. While Jacobian-based approaches offer theoretical foundations for rigid manipulators, their direct application to DCRs remains limited by time-varying kinematics and underactuated deformation dynamics. This paper proposes Jacobian Exploratory Dual-Phase RL (JEDP-RL), a framework that decomposes planning into phased Jacobian estimation and policy execution. During each training step, we first perform small-scale local exploratory actions to estimate the deformation Jacobian matrix, then augment the state representation with Jacobian features to restore approximate Markovianity. Extensive SOFA surgical dynamic simulations demonstrate JEDP-RL's three key advantages over proximal policy optimization (PPO) baselines: 1) Convergence speed: 3.2x faster policy convergence, 2) Navigation efficiency: requires 25% fewer steps to reach the target, and 3) Generalization ability: achieve 92% success rate under material property variations and achieve 83% (33% higher than PPO) success rate in the unseen tissue environment.

