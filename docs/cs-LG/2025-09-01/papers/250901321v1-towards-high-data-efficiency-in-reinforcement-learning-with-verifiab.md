---
layout: default
title: Towards High Data Efficiency in Reinforcement Learning with Verifiable Reward
---

# Towards High Data Efficiency in Reinforcement Learning with Verifiable Reward

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01321" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01321v1</a>
  <a href="https://arxiv.org/pdf/2509.01321.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01321v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01321v1', 'Towards High Data Efficiency in Reinforcement Learning with Verifiable Reward')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyu Tang, Zhenduo Zhang, Yurou Liu, Wayne Xin Zhao, Zujie Wen, Zhiqiang Zhang, Jun Zhou

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-01

---

## 💡 一句话要点

**DEPO：面向可验证奖励强化学习的高数据效率策略优化**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `数据效率` `策略优化` `可验证奖励` `离线学习`

## 📋 核心要点

1. 现有基于可验证奖励的强化学习方法在扩展时面临数据效率低、训练成本高的挑战。
2. DEPO通过结合优化的离线数据选择（基于多样性、影响力和难度）和在线数据选择（基于可探索性）来提高数据效率。
3. 实验表明，DEPO在多个推理基准上优于现有方法，仅使用20%的数据即可达到甚至超过全数据训练的效果。

## 📝 摘要（中文）

大型推理模型利用可验证奖励强化学习(RLVR)来提升推理能力。然而，扩展这些方法通常需要大量的rollout计算和大型数据集，导致高训练成本和低数据效率。为了解决这个问题，我们提出了DEPO，一种数据高效的策略优化流程，它结合了离线和在线数据选择的优化策略。在离线阶段，我们基于多样性、影响力和适当的难度，筛选出高质量的训练样本子集。在在线RLVR训练期间，我们引入了一个样本级别的可探索性指标，以动态过滤探索潜力低的样本，从而显著降低rollout计算成本。此外，我们还为未充分探索的样本引入了回放机制，以确保充分的训练，从而提高模型的最终收敛性能。在五个推理基准上的实验表明，DEPO在离线和在线数据选择场景中始终优于现有方法。值得注意的是，仅使用20%的训练数据，我们的方法在AIME24上的速度提高了1.85倍，在AIME25上的速度提高了1.66倍，而GRPO则使用完整数据集进行训练。

## 🔬 方法详解

**问题定义**：现有基于可验证奖励的强化学习方法，在提升大型推理模型的推理能力时，需要大量的训练数据和计算资源，导致训练成本高昂，数据利用效率低下。尤其是在线强化学习阶段，大量的rollout计算消耗了大量的资源，而很多rollout样本的探索价值并不高。

**核心思路**：DEPO的核心思路是通过优化数据选择策略，在离线和在线阶段都选择更有价值的样本进行训练，从而提高数据效率，降低训练成本。离线阶段选择具有代表性和难度的样本，在线阶段则关注具有探索潜力的样本。

**技术框架**：DEPO包含离线数据选择和在线数据选择两个主要阶段。离线阶段，首先从原始数据集中筛选出具有多样性、影响力和适当难度的样本子集。在线阶段，引入样本级别的可探索性指标，动态过滤探索潜力低的样本，并对未充分探索的样本进行回放。整个流程旨在减少不必要的rollout计算，并确保模型能够充分学习。

**关键创新**：DEPO的关键创新在于结合了离线和在线的数据选择策略，并提出了样本级别的可探索性指标。离线数据选择侧重于数据的代表性和难度，而在线数据选择则侧重于数据的探索潜力。这种结合使得DEPO能够更有效地利用数据，提高训练效率。

**关键设计**：离线数据选择中，使用了多样性、影响力和难度三个指标来评估样本的价值。在线数据选择中，可探索性指标的具体计算方法未知。此外，DEPO还引入了回放机制，用于存储和重新训练未充分探索的样本，以保证模型的收敛性能。具体的回放策略和参数设置未知。

## 📊 实验亮点

DEPO在五个推理基准上都优于现有方法。特别是在AIME24和AIME25数据集上，仅使用20%的训练数据，DEPO就分别实现了1.85倍和1.66倍的加速，超过了使用完整数据集训练的GRPO模型。这表明DEPO在数据效率方面具有显著优势。

## 🎯 应用场景

DEPO可应用于各种需要高数据效率的强化学习场景，尤其是在计算资源有限或数据获取成本高昂的情况下。例如，可以应用于机器人控制、游戏AI、自然语言处理等领域，帮助模型更快地学习和适应环境，降低开发成本，加速产品迭代。

## 📄 摘要（原文）

> Recent advances in large reasoning models have leveraged reinforcement learning with verifiable rewards (RLVR) to improve reasoning capabilities. However, scaling these methods typically requires extensive rollout computation and large datasets, leading to high training costs and low data efficiency. To mitigate this issue, we propose DEPO, a Data-Efficient Policy Optimization pipeline that combines optimized strategies for both offline and online data selection. In the offline phase, we curate a high-quality subset of training samples based on diversity, influence, and appropriate difficulty. During online RLVR training, we introduce a sample-level explorability metric to dynamically filter samples with low exploration potential, thereby reducing substantial rollout computational costs. Furthermore, we incorporate a replay mechanism for under-explored samples to ensure adequate training, which enhances the model's final convergence performance. Experiments across five reasoning benchmarks show that DEPO consistently outperforms existing methods in both offline and online data selection scenarios. Notably, using only 20% of the training data, our approach achieves a 1.85 times speed-up on AIME24 and a 1.66 times speed-up on AIME25 compared to GRPO trained on the full dataset.

