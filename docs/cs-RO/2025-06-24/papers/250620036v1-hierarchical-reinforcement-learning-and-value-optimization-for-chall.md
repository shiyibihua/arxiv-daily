---
layout: default
title: Hierarchical Reinforcement Learning and Value Optimization for Challenging Quadruped Locomotion
---

# Hierarchical Reinforcement Learning and Value Optimization for Challenging Quadruped Locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20036" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20036v1</a>
  <a href="https://arxiv.org/pdf/2506.20036.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20036v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20036v1', 'Hierarchical Reinforcement Learning and Value Optimization for Challenging Quadruped Locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeremiah Coholich, Muhammad Ali Murtaza, Seth Hutchinson, Zsolt Kira

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-24

---

## 💡 一句话要点

**提出分层强化学习框架以解决四足机器人在复杂地形中的行走问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `分层强化学习` `四足机器人` `复杂地形` `路径规划` `在线优化` `演员-评论家算法`

## 📋 核心要点

1. 现有的四足机器人行走方法在复杂地形上表现不佳，难以实现高效的目标选择与路径规划。
2. 本研究提出的分层强化学习框架通过高层策略优化低层策略的目标选择，提升了行走效率与安全性。
3. 实验结果表明，该框架在多种地形上相较于传统端到端强化学习方法，获得了更高的奖励并减少了碰撞次数。

## 📝 摘要（中文）

我们提出了一种新颖的分层强化学习框架，用于四足机器人在复杂地形上的行走。该方法采用两层层次结构，高层策略（HLP）为低层策略（LLP）选择最佳目标。LLP使用基于策略的演员-评论家强化学习算法进行训练，并将足迹放置作为目标。HLP不需要额外的训练或环境样本，而是通过对LLP学习的价值函数进行在线优化来运行。我们通过与端到端强化学习方法的比较，展示了该框架的优势，观察到在不同地形上能够以更少的碰撞获得更高的奖励，尤其是在训练过程中未遇到的更困难地形上。

## 🔬 方法详解

**问题定义**：本论文旨在解决四足机器人在复杂地形上行走时的目标选择与路径规划问题。现有方法往往依赖于单一的强化学习策略，难以适应多变的环境，导致效率低下和碰撞风险增加。

**核心思路**：我们提出的分层强化学习框架通过引入高层策略（HLP）和低层策略（LLP）的两层结构，使得高层策略能够动态选择低层策略的目标，从而优化行走路径和提高适应性。

**技术框架**：该框架包含两个主要模块：高层策略（HLP）和低层策略（LLP）。HLP负责在线优化目标选择，而LLP则通过演员-评论家算法进行训练，执行具体的行走任务。

**关键创新**：本研究的关键创新在于HLP的设计，它无需额外的训练或环境样本，而是通过对LLP学习的价值函数进行在线优化，从而实现了高效的目标选择与路径规划。

**关键设计**：在技术细节上，LLP采用了基于策略的演员-评论家算法，设置了适应复杂地形的损失函数，并设计了适合四足机器人的网络结构，以确保在多样化环境中的稳定性与效率。

## 📊 实验亮点

实验结果显示，所提出的分层强化学习框架在多种复杂地形上，相较于传统的端到端强化学习方法，能够实现更高的奖励，且碰撞次数减少了显著的比例，展示了其在实际应用中的优越性。

## 🎯 应用场景

该研究的潜在应用场景包括自动驾驶、救援机器人、农业机器人等领域，能够显著提升机器人在复杂环境中的自主导航与行走能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We propose a novel hierarchical reinforcement learning framework for quadruped locomotion over challenging terrain. Our approach incorporates a two-layer hierarchy in which a high-level policy (HLP) selects optimal goals for a low-level policy (LLP). The LLP is trained using an on-policy actor-critic RL algorithm and is given footstep placements as goals. We propose an HLP that does not require any additional training or environment samples and instead operates via an online optimization process over the learned value function of the LLP. We demonstrate the benefits of this framework by comparing it with an end-to-end reinforcement learning (RL) approach. We observe improvements in its ability to achieve higher rewards with fewer collisions across an array of different terrains, including terrains more difficult than any encountered during training.

