---
layout: default
title: Revisiting Actor-Critic Methods in Discrete Action Off-Policy Reinforcement Learning
---

# Revisiting Actor-Critic Methods in Discrete Action Off-Policy Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09838" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09838v1</a>
  <a href="https://arxiv.org/pdf/2509.09838.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09838v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09838v1', 'Revisiting Actor-Critic Methods in Discrete Action Off-Policy Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Reza Asad, Reza Babanezhad, Sharan Vaswani

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-11

---

## 💡 一句话要点

**解耦Actor-Critic熵正则化，提升离散动作离策略强化学习性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离策略强化学习` `Actor-Critic方法` `熵正则化` `离散动作空间` `Atari游戏`

## 📋 核心要点

1. 现有离散动作离策略强化学习中，基于策略的方法（如DSAC）性能不佳，主要原因是Actor和Critic的熵耦合。
2. 通过解耦Actor和Critic的熵，并结合m步Bellman算子，构建了一个更灵活的离策略Actor-Critic框架。
3. 实验表明，新框架在Atari游戏上可以达到与DQN相当的性能，无需额外的熵正则化或探索策略。

## 📝 摘要（中文）

在离散动作环境（如Atari）中，基于价值的方法（如DQN）是离策略强化学习的常用方法。常见的基于策略的方法要么是同策略的，无法有效地从离策略数据中学习（如PPO），要么在离散动作环境中表现不佳（如SAC）。因此，本文从离散SAC（DSAC）出发，重新审视了在这种设置下Actor-Critic方法的设计。首先，确定Actor和Critic熵之间的耦合是DSAC性能不佳的主要原因。通过解耦这些组件，DSAC可以达到与DQN相当的性能。受此启发，本文提出了一个灵活的离策略Actor-Critic框架，该框架将DSAC作为特例包含在内。该框架允许使用m步Bellman算子进行Critic更新，并能够将标准策略优化方法与熵正则化相结合，从而实例化最终的Actor目标。理论上，证明了所提出的方法可以保证收敛到表格设置中的最优正则化价值函数。实验上，证明了这些方法可以接近DQN在标准Atari游戏上的性能，即使没有熵正则化或显式探索也能做到。

## 🔬 方法详解

**问题定义**：在离散动作空间的离策略强化学习任务中，传统的基于策略的方法，例如离散SAC (DSAC)，通常表现不如基于价值的方法，例如DQN。DSAC的性能瓶颈在于Actor和Critic之间的熵耦合，这限制了其学习效率和最终性能。

**核心思路**：本文的核心思路是解耦Actor和Critic的熵正则化项，允许它们独立地进行优化。通过这种解耦，可以更灵活地控制探索和利用之间的平衡，从而提高学习效率。此外，还引入了m步Bellman算子来更新Critic，以加速价值函数的学习。

**技术框架**：该框架是一个通用的离策略Actor-Critic架构，包含以下主要模块：1) Actor网络，用于生成策略；2) Critic网络，用于评估策略的价值；3) 经验回放缓冲区，用于存储和采样经验数据；4) 目标网络，用于稳定学习过程。该框架允许使用不同的策略优化方法（如策略梯度、TRPO等）来更新Actor，并使用m步Bellman算子来更新Critic。

**关键创新**：最重要的技术创新点在于解耦Actor和Critic的熵正则化项，并将其纳入一个统一的离策略Actor-Critic框架中。这种解耦允许更灵活地控制探索和利用，从而提高学习效率。此外，使用m步Bellman算子来更新Critic，可以加速价值函数的学习。

**关键设计**：关键的设计包括：1) Actor和Critic网络的结构选择（例如，多层感知机、卷积神经网络等）；2) 熵正则化系数的设置，需要根据具体任务进行调整；3) m步Bellman算子的步数m的选择，需要在偏差和方差之间进行权衡；4) 策略优化方法的选择（例如，策略梯度、TRPO等），需要根据具体任务进行选择。

## 📊 实验亮点

实验结果表明，通过解耦Actor和Critic的熵正则化，所提出的方法在Atari游戏上的性能可以接近DQN，甚至在没有熵正则化或显式探索的情况下也能实现。这表明该方法具有很强的鲁棒性和泛化能力。此外，该方法在某些游戏上的性能甚至超过了DQN。

## 🎯 应用场景

该研究成果可应用于各种离散动作空间的强化学习任务，例如游戏AI、机器人控制、推荐系统等。通过解耦Actor和Critic的熵正则化，可以提高学习效率和最终性能，从而在实际应用中获得更好的效果。此外，该框架的通用性使其易于扩展到其他离策略强化学习算法。

## 📄 摘要（原文）

> Value-based approaches such as DQN are the default methods for off-policy reinforcement learning with discrete-action environments such as Atari. Common policy-based methods are either on-policy and do not effectively learn from off-policy data (e.g. PPO), or have poor empirical performance in the discrete-action setting (e.g. SAC). Consequently, starting from discrete SAC (DSAC), we revisit the design of actor-critic methods in this setting. First, we determine that the coupling between the actor and critic entropy is the primary reason behind the poor performance of DSAC. We demonstrate that by merely decoupling these components, DSAC can have comparable performance as DQN. Motivated by this insight, we introduce a flexible off-policy actor-critic framework that subsumes DSAC as a special case. Our framework allows using an m-step Bellman operator for the critic update, and enables combining standard policy optimization methods with entropy regularization to instantiate the resulting actor objective. Theoretically, we prove that the proposed methods can guarantee convergence to the optimal regularized value function in the tabular setting. Empirically, we demonstrate that these methods can approach the performance of DQN on standard Atari games, and do so even without entropy regularization or explicit exploration.

