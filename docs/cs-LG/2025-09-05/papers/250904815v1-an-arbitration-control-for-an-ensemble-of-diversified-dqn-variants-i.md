---
layout: default
title: An Arbitration Control for an Ensemble of Diversified DQN variants in Continual Reinforcement Learning
---

# An Arbitration Control for an Ensemble of Diversified DQN variants in Continual Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04815" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04815v1</a>
  <a href="https://arxiv.org/pdf/2509.04815.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04815v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04815v1', 'An Arbitration Control for an Ensemble of Diversified DQN variants in Continual Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wonseo Jang, Dongjae Kim

**分类**: cs.LG, cs.MA

**发布日期**: 2025-09-05

**备注**: 8 pages, 8 figures

---

## 💡 一句话要点

**提出ACED-DQN，通过仲裁控制多样化DQN集成解决持续强化学习中的灾难性遗忘问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `持续强化学习` `灾难性遗忘` `集成学习` `仲裁控制` `DQN` `深度强化学习` `价值函数`

## 📋 核心要点

1. 深度强化学习在持续学习中面临灾难性遗忘问题，导致性能显著下降。
2. 提出ACED-DQN框架，通过集成多样化的DQN变体，并采用仲裁控制机制来解决该问题。
3. 实验结果表明，ACED-DQN在静态和持续环境中均取得了显著的性能提升。

## 📝 摘要（中文）

深度强化学习（RL）模型在静态环境中学习最优策略时表现高效，但容易丢失先前学习的知识（即灾难性遗忘）。这导致RL模型在持续强化学习（CRL）场景中表现不佳。为了解决这个问题，我们提出了一种基于RL智能体集成的仲裁控制机制。该机制的灵感来源于人类在前额皮层中观察到的，通过并行控制多个RL智能体进行决策的方式。我们的模型集成了两个关键思想：（1）显式训练的、具有多样化价值函数的RL集成（即DQN变体）；（2）一种仲裁控制机制，优先考虑在最近的试验中具有更高可靠性（即更少误差）的智能体。我们提出了一个用于CRL的框架，即用于多样化DQN集成仲裁控制（ACED-DQN）。实验结果表明，在静态和持续环境中，该框架都显著提高了性能，并提供了经验证据，证明了在训练期间对多样化DQN进行仲裁控制的有效性。这项工作提出了一个受人脑启发的、使RL智能体能够持续学习的框架。

## 🔬 方法详解

**问题定义**：论文旨在解决持续强化学习（CRL）中深度强化学习模型面临的灾难性遗忘问题。现有方法在学习新任务时，往往会忘记之前学习的任务知识，导致性能下降。这种现象阻碍了强化学习在动态变化环境中的应用。

**核心思路**：论文的核心思路是模仿人类大脑在前额皮层中进行决策的方式，即通过集成多个具有不同专长的RL智能体，并根据其在近期任务中的表现进行仲裁控制。通过这种方式，模型能够更好地适应新任务，同时保留先前学习的知识。

**技术框架**：ACED-DQN框架包含两个主要组成部分：一是多样化的DQN集成，二是仲裁控制机制。多样化的DQN集成由多个DQN变体组成，每个变体都经过训练以学习不同的价值函数。仲裁控制机制根据每个DQN变体在近期试验中的可靠性（误差）来分配权重，并选择具有最高权重的DQN变体来执行动作。

**关键创新**：该论文的关键创新在于将集成学习和仲裁控制机制相结合，应用于持续强化学习。通过多样化的DQN集成，模型能够学习到更丰富的知识表示。仲裁控制机制则能够根据环境的变化动态地调整每个DQN变体的权重，从而更好地适应新任务，并减轻灾难性遗忘。

**关键设计**：在DQN集成方面，论文采用了不同的DQN变体，例如Double DQN、Dueling DQN等，以增加多样性。在仲裁控制机制方面，论文使用了一种基于误差的权重分配方法，即根据每个DQN变体在近期试验中的误差来计算其权重。误差越小，权重越高。具体的权重计算公式未知，需要在论文中查找。

## 📊 实验亮点

实验结果表明，ACED-DQN在多个持续强化学习环境中均取得了显著的性能提升。与传统的DQN方法相比，ACED-DQN能够更好地保留先前学习的知识，并在学习新任务时表现出更强的适应性。具体的性能提升数据需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于机器人导航、游戏AI、自动驾驶等需要在动态变化环境中持续学习的领域。通过减轻灾难性遗忘，该方法能够使智能体在不断变化的环境中保持高性能，并适应新的任务需求，具有重要的实际应用价值和潜力。

## 📄 摘要（原文）

> Deep reinforcement learning (RL) models, despite their efficiency in learning an optimal policy in static environments, easily loses previously learned knowledge (i.e., catastrophic forgetting). It leads RL models to poor performance in continual reinforcement learning (CRL) scenarios. To address this, we present an arbitration control mechanism over an ensemble of RL agents. It is motivated by and closely aligned with how humans make decisions in a CRL context using an arbitration control of multiple RL agents in parallel as observed in the prefrontal cortex. We integrated two key ideas into our model: (1) an ensemble of RLs (i.e., DQN variants) explicitly trained to have diverse value functions and (2) an arbitration control that prioritizes agents with higher reliability (i.e., less error) in recent trials. We propose a framework for CRL, an Arbitration Control for an Ensemble of Diversified DQN variants (ACED-DQN). We demonstrate significant performance improvements in both static and continual environments, supported by empirical evidence showing the effectiveness of arbitration control over diversified DQNs during training. In this work, we introduced a framework that enables RL agents to continuously learn, with inspiration from the human brain.

