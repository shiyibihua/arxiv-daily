---
layout: default
title: Trust Region Reward Optimization and Proximal Inverse Reward Optimization Algorithm
---

# Trust Region Reward Optimization and Proximal Inverse Reward Optimization Algorithm

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23135" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23135v3</a>
  <a href="https://arxiv.org/pdf/2509.23135.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23135v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23135v3', 'Trust Region Reward Optimization and Proximal Inverse Reward Optimization Algorithm')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Chen, Menglin Zou, Jiaqi Zhang, Yitan Zhang, Junyi Yang, Gael Gendron, Libo Zhang, Jiamou Liu, Michael J. Witbrock

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-27 (更新: 2025-10-13)

**备注**: Accepted to NeurIPS 2025. Title used at submission and review: PIRO: Toward Stable Reward Learning for Inverse RL via Monotonic Policy Divergence Reduction

---

## 💡 一句话要点

**提出信赖域奖励优化(TRRO)框架，解决逆强化学习中reward和policy联合学习的不稳定性问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `逆强化学习` `奖励函数学习` `信赖域优化` `策略模仿` `机器人控制`

## 📋 核心要点

1. 现有逆强化学习方法常使用对抗训练，导致奖励和策略优化交替进行，训练过程不稳定。
2. 论文提出信赖域奖励优化(TRRO)框架，通过最大化专家行为的可能性来联合学习奖励和策略，保证单调改进。
3. 实验表明，提出的近端逆奖励优化(PIRO)算法在多个基准测试中达到或超过了现有最佳方法，并具有高样本效率。

## 📝 摘要（中文）

逆强化学习(IRL)旨在学习一个奖励函数来解释专家演示。现有的IRL方法通常采用对抗(minimax)公式，在奖励和策略优化之间交替进行，这往往导致训练不稳定。最近的非对抗IRL方法通过基于能量的公式联合学习奖励和策略，从而提高了稳定性，但缺乏形式化的保证。本文弥补了这一差距。首先，本文提出了一个统一的视角，表明典型的非对抗方法显式或隐式地最大化了专家行为的可能性，这等价于最小化期望回报差距。这一洞察引出了本文的主要贡献：信赖域奖励优化(TRRO)，这是一个通过Minorization-Maximization过程保证这种可能性单调改进的框架。本文将TRRO实例化为近端逆奖励优化(PIRO)，这是一种实用且稳定的IRL算法。在理论上，TRRO为正向强化学习中的信赖域策略优化(TRPO)的稳定性保证提供了IRL对应。在经验上，PIRO在奖励恢复、策略模仿方面与最先进的基线方法相匹配或超过，并在MuJoCo和Gym-Robotics基准测试以及真实的动物行为建模任务中具有很高的样本效率。

## 🔬 方法详解

**问题定义**：逆强化学习旨在从专家演示中学习奖励函数，现有方法如对抗逆强化学习(Adversarial IRL)通过minimax框架交替优化奖励函数和策略，导致训练不稳定，难以收敛。非对抗方法虽然提高了稳定性，但缺乏理论保证，无法确保学习过程的单调改进。

**核心思路**：论文的核心思路是将非对抗IRL方法统一到一个最大化专家行为可能性的框架下，并证明这等价于最小化期望回报差距。基于此，提出信赖域奖励优化(TRRO)框架，通过Minorization-Maximization (MM)过程，保证专家行为可能性的单调改进，从而稳定地学习奖励函数。

**技术框架**：TRRO框架包含以下主要步骤：
1.  **奖励函数更新**：使用MM算法，在信赖域内更新奖励函数，保证专家行为可能性增加。
2.  **策略优化**：根据更新后的奖励函数，优化策略，使其能够更好地模仿专家行为。
3.  **信赖域约束**：通过信赖域约束，限制奖励函数的更新幅度，防止训练过程中的剧烈变化，提高稳定性。

**关键创新**：TRRO的关键创新在于：
1.  **统一视角**：将现有非对抗IRL方法统一到最大化专家行为可能性的框架下。
2.  **单调改进保证**：通过MM过程，保证专家行为可能性的单调改进，提供理论上的稳定性保证。
3.  **信赖域约束**：引入信赖域约束，限制奖励函数的更新幅度，进一步提高训练稳定性。

**关键设计**：TRRO框架的关键设计包括：
1.  **MM算法**：使用MM算法进行奖励函数更新，具体形式需要根据实际问题进行选择。
2.  **信赖域半径**：信赖域半径的设置需要根据具体问题进行调整，过小会导致收敛速度慢，过大会导致训练不稳定。
3.  **近端策略优化(PPO)**：可以使用PPO等算法进行策略优化，以提高样本效率和稳定性。

## 📊 实验亮点

实验结果表明，提出的PIRO算法在MuJoCo和Gym-Robotics基准测试中，在奖励恢复和策略模仿方面与最先进的基线方法相匹配或超过，并且具有更高的样本效率。此外，PIRO还在真实的动物行为建模任务中取得了良好的效果，验证了其在实际应用中的潜力。

## 🎯 应用场景

该研究成果可应用于机器人控制、自动驾驶、游戏AI等领域。通过模仿专家行为，可以训练出高性能的智能体，解决复杂环境下的决策问题。此外，该方法还可以用于动物行为建模，分析动物的学习机制，为生物学研究提供新的工具。

## 📄 摘要（原文）

> Inverse Reinforcement Learning (IRL) learns a reward function to explain expert demonstrations. Modern IRL methods often use the adversarial (minimax) formulation that alternates between reward and policy optimization, which often lead to unstable training. Recent non-adversarial IRL approaches improve stability by jointly learning reward and policy via energy-based formulations but lack formal guarantees. This work bridges this gap. We first present a unified view showing canonical non-adversarial methods explicitly or implicitly maximize the likelihood of expert behavior, which is equivalent to minimizing the expected return gap. This insight leads to our main contribution: Trust Region Reward Optimization (TRRO), a framework that guarantees monotonic improvement in this likelihood via a Minorization-Maximization process. We instantiate TRRO into Proximal Inverse Reward Optimization (PIRO), a practical and stable IRL algorithm. Theoretically, TRRO provides the IRL counterpart to the stability guarantees of Trust Region Policy Optimization (TRPO) in forward RL. Empirically, PIRO matches or surpasses state-of-the-art baselines in reward recovery, policy imitation with high sample efficiency on MuJoCo and Gym-Robotics benchmarks and a real-world animal behavior modeling task.

