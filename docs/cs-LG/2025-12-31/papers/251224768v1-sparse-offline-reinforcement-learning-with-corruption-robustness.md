---
layout: default
title: Sparse Offline Reinforcement Learning with Corruption Robustness
---

# Sparse Offline Reinforcement Learning with Corruption Robustness

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24768" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24768v1</a>
  <a href="https://arxiv.org/pdf/2512.24768.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24768v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24768v1', 'Sparse Offline Reinforcement Learning with Corruption Robustness')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nam Phuong Tran, Andi Nika, Goran Radanovic, Long Tran-Thanh, Debmalya Mandal

**分类**: stat.ML, cs.LG

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**提出基于稀疏鲁棒估计的Actor-Critic算法，解决离线稀疏RL中的数据污染问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `稀疏强化学习` `鲁棒性` `数据污染` `Actor-Critic` `高维数据` `马尔可夫决策过程`

## 📋 核心要点

1. 现有离线RL方法在高维稀疏MDP中，面对数据污染时，鲁棒性不足，难以保证策略的有效性。
2. 提出基于稀疏鲁棒估计的Actor-Critic算法，避免使用逐点悲观奖励，从而提升算法的鲁棒性。
3. 理论分析表明，该算法在单策略集中性覆盖和数据污染下，能够学习到接近最优的策略。

## 📝 摘要（中文）

本文研究了离线稀疏强化学习（RL）中对强数据污染的鲁棒性。在我们的设置中，一个攻击者可以任意扰动来自高维但稀疏马尔可夫决策过程的一小部分收集到的轨迹，我们的目标是估计一个接近最优的策略。主要的挑战是，在高维情况下，样本数量N小于特征维度d，利用稀疏性对于获得非平凡的保证至关重要，但在离线RL中尚未得到系统研究。我们分析了均匀覆盖和稀疏单策略集中性假设下的问题。虽然最小二乘值迭代（LSVI）是鲁棒离线RL的标准方法，并且在均匀覆盖下表现良好，但我们表明将稀疏性集成到LSVI中是不自然的，并且由于过于悲观的奖励，其分析可能会崩溃。为了克服这个问题，我们提出了具有稀疏鲁棒估计器oracle的actor-critic方法，该方法避免了逐点悲观奖励的使用，并为单策略集中性覆盖下的稀疏离线RL提供了第一个非平凡的保证。此外，我们将结果扩展到受污染的环境，并表明我们的算法在强污染下仍然是鲁棒的。我们的结果在高维稀疏MDP中提供了第一个具有单策略集中性覆盖和污染的非平凡保证，表明在传统鲁棒离线RL技术可能失败的情况下，学习接近最优的策略仍然是可能的。

## 🔬 方法详解

**问题定义**：论文旨在解决高维稀疏马尔可夫决策过程（MDP）中，离线强化学习算法对数据污染的鲁棒性问题。现有方法，如最小二乘值迭代（LSVI），在处理高维数据时，难以有效利用稀疏性，并且在数据被污染的情况下，性能会显著下降。传统的鲁棒离线RL技术在高维稀疏MDP中可能失效。

**核心思路**：论文的核心思路是设计一种基于稀疏鲁棒估计的Actor-Critic算法，该算法避免使用逐点悲观奖励，从而提高算法对数据污染的鲁棒性。通过利用稀疏性，算法能够在高维环境中更有效地学习策略。

**技术框架**：该算法采用Actor-Critic框架，包含以下主要模块：1) Actor网络，用于生成策略；2) Critic网络，用于评估策略的价值；3) 稀疏鲁棒估计器Oracle，用于估计价值函数，并对数据污染具有鲁棒性。算法通过迭代更新Actor和Critic网络，最终学习到一个接近最优的策略。

**关键创新**：最重要的技术创新点在于提出了稀疏鲁棒估计器Oracle，该Oracle能够有效地利用数据的稀疏性，并且对数据污染具有鲁棒性。与传统的LSVI方法相比，该方法避免了使用逐点悲观奖励，从而避免了过度悲观的估计，提高了算法的性能。

**关键设计**：论文中，稀疏鲁棒估计器Oracle的具体实现方式未知，但其核心在于利用稀疏性约束，例如L1正则化，来提高估计的准确性和鲁棒性。Actor和Critic网络的具体结构也未知，但通常会采用深度神经网络来实现。

## 📊 实验亮点

论文提供了理论分析，证明了所提出的算法在单策略集中性覆盖和数据污染下，能够学习到接近最优的策略。该结果在高维稀疏MDP中提供了第一个具有单策略集中性覆盖和污染的非平凡保证，表明在传统鲁棒离线RL技术可能失败的情况下，学习接近最优的策略仍然是可能的。具体的实验结果未知。

## 🎯 应用场景

该研究成果可应用于高维、数据稀疏且易受污染的强化学习场景，例如推荐系统、金融交易、医疗诊断等。在这些场景中，数据质量难以保证，传统的强化学习算法容易受到数据污染的影响，而该研究提出的算法能够提高策略的鲁棒性和可靠性，具有重要的实际应用价值。

## 📄 摘要（原文）

> We investigate robustness to strong data corruption in offline sparse reinforcement learning (RL). In our setting, an adversary may arbitrarily perturb a fraction of the collected trajectories from a high-dimensional but sparse Markov decision process, and our goal is to estimate a near optimal policy. The main challenge is that, in the high-dimensional regime where the number of samples $N$ is smaller than the feature dimension $d$, exploiting sparsity is essential for obtaining non-vacuous guarantees but has not been systematically studied in offline RL. We analyse the problem under uniform coverage and sparse single-concentrability assumptions. While Least Square Value Iteration (LSVI), a standard approach for robust offline RL, performs well under uniform coverage, we show that integrating sparsity into LSVI is unnatural, and its analysis may break down due to overly pessimistic bonuses. To overcome this, we propose actor-critic methods with sparse robust estimator oracles, which avoid the use of pointwise pessimistic bonuses and provide the first non-vacuous guarantees for sparse offline RL under single-policy concentrability coverage. Moreover, we extend our results to the contaminated setting and show that our algorithm remains robust under strong contamination. Our results provide the first non-vacuous guarantees in high-dimensional sparse MDPs with single-policy concentrability coverage and corruption, showing that learning a near-optimal policy remains possible in regimes where traditional robust offline RL techniques may fail.

