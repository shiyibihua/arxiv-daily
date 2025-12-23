---
layout: default
title: Double Q-learning for Value-based Deep Reinforcement Learning, Revisited
---

# Double Q-learning for Value-based Deep Reinforcement Learning, Revisited

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00275" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00275v1</a>
  <a href="https://arxiv.org/pdf/2507.00275.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00275v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00275v1', 'Double Q-learning for Value-based Deep Reinforcement Learning, Revisited')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prabhat Nagarajan, Martha White, Marlos C. Machado

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-30

**备注**: 44 pages

---

## 💡 一句话要点

**提出深度双Q学习以解决Q学习过度估计问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `双Q学习` `过度估计` `深度Q网络` `Atari游戏` `智能体学习` `经验回放` `小批量采样`

## 📋 核心要点

1. 现有的双深度Q网络在训练过程中未能充分利用两个Q函数，导致过度估计问题依然存在。
2. 本文提出深度双Q学习（DDQL），通过训练两个相互引导的Q函数来减少过度估计。
3. 实验结果显示，DDQL在57个Atari 2600游戏中表现优于双深度Q网络，且无需额外的超参数设置。

## 📝 摘要（中文）

过度估计在强化学习中普遍存在，尤其是在Q学习中。双Q学习算法旨在通过训练两个Q函数来解决这一问题，从而去相关化动作选择和动作评估。尽管双Q学习已被适配到深度强化学习中，但现有的双深度Q网络（Double DQN）并未充分利用两个Q函数的训练。本文提出深度双Q学习（DDQL），旨在探讨其是否能减少过度估计并在性能上优于双深度Q网络。研究表明，DDQL在57个Atari 2600游戏中表现优于双深度Q网络，且无需额外的超参数设置。

## 🔬 方法详解

**问题定义**：本文旨在解决强化学习中Q学习算法的过度估计问题。现有的双深度Q网络未能有效利用两个Q函数的训练，导致性能不足。

**核心思路**：深度双Q学习（DDQL）通过同时训练两个Q函数，使得动作选择与动作评估相互去相关，从而减少过度估计现象。这样的设计能够更准确地评估动作的价值。

**技术框架**：DDQL的整体架构包括两个Q网络，这两个网络相互引导进行训练。训练过程中，使用经验回放机制来提高样本效率，并采用小批量采样策略来优化训练过程。

**关键创新**：DDQL的主要创新在于其对双Q学习核心思想的全面适配，充分利用两个Q函数的训练，而不仅仅是松散的适配。这一设计显著改善了Q值的估计精度。

**关键设计**：DDQL在网络结构上采用了标准的深度Q网络架构，并在损失函数中引入了两个Q函数的交互影响。关键参数设置上，DDQL不需要额外的超参数，简化了模型的调优过程。

## 📊 实验亮点

实验结果表明，深度双Q学习在57个Atari 2600游戏中的表现优于双深度Q网络，整体性能提升显著，且不需要额外的超参数设置。这一发现验证了DDQL在减少过度估计方面的有效性，具有重要的实用价值。

## 🎯 应用场景

深度双Q学习（DDQL）在游戏AI、机器人控制和自动驾驶等领域具有广泛的应用潜力。通过减少过度估计，DDQL能够提高智能体在复杂环境中的决策能力，从而实现更高效的学习和更优的性能表现。未来，DDQL的思想也可能被扩展到其他强化学习任务中，推动相关领域的发展。

## 📄 摘要（原文）

> Overestimation is pervasive in reinforcement learning (RL), including in Q-learning, which forms the algorithmic basis for many value-based deep RL algorithms. Double Q-learning is an algorithm introduced to address Q-learning's overestimation by training two Q-functions and using both to de-correlate action-selection and action-evaluation in bootstrap targets. Shortly after Q-learning was adapted to deep RL in the form of deep Q-networks (DQN), Double Q-learning was adapted to deep RL in the form of Double DQN. However, Double DQN only loosely adapts Double Q-learning, forgoing the training of two different Q-functions that bootstrap off one another. In this paper, we study algorithms that adapt this core idea of Double Q-learning for value-based deep RL. We term such algorithms Deep Double Q-learning (DDQL). Our aim is to understand whether DDQL exhibits less overestimation than Double DQN and whether performant instantiations of DDQL exist. We answer both questions affirmatively, demonstrating that DDQL reduces overestimation and outperforms Double DQN in aggregate across 57 Atari 2600 games, without requiring additional hyperparameters. We also study several aspects of DDQL, including its network architecture, replay ratio, and minibatch sampling strategy.

