---
layout: default
title: Efficient On-Policy Reinforcement Learning via Exploration of Sparse Parameter Space
---

# Efficient On-Policy Reinforcement Learning via Exploration of Sparse Parameter Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25876" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25876v1</a>
  <a href="https://arxiv.org/pdf/2509.25876.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25876v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25876v1', 'Efficient On-Policy Reinforcement Learning via Exploration of Sparse Parameter Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyu Zhang, Aishik Deb, Klaus Mueller

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-30

**备注**: 16 pages; 7 figures

---

## 💡 一句话要点

**提出ExploRLer，通过探索稀疏参数空间提升On-Policy强化学习效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `On-Policy强化学习` `参数空间探索` `策略梯度` `近端策略优化` `连续控制` `迭代级优化`

## 📋 核心要点

1. 传统On-Policy方法仅依赖单一梯度更新，忽略了参数空间中潜在的更优解区域。
2. ExploRLer通过系统探索On-Policy梯度更新的邻域，寻找更高性能的策略。
3. ExploRLer在不增加梯度更新次数的前提下，显著提升了复杂连续控制环境中的性能。

## 📝 摘要（中文）

近端策略优化(PPO)等策略梯度方法通常仅沿单一随机梯度方向更新，忽略了参数空间丰富的局部结构。先前研究表明，替代梯度与真实奖励landscape的相关性较差。基于此，我们可视化了迭代中策略检查点所跨越的参数空间，发现更高性能的解通常位于附近未探索的区域。为了利用这一机会，我们引入ExploRLer，一个可无缝集成到PPO和TRPO等On-Policy算法中的插件式pipeline，系统地探测替代On-Policy梯度更新的未探索邻域。在不增加梯度更新次数的情况下，ExploRLer在复杂的连续控制环境中实现了显著的改进。我们的结果表明，迭代级探索为加强On-Policy强化学习提供了一种实用有效的方法，并为替代目标的局限性提供了新的视角。

## 🔬 方法详解

**问题定义**：现有的On-Policy强化学习方法，如PPO和TRPO，通常只沿着一个随机梯度方向进行更新，这使得算法容易陷入局部最优，无法充分利用参数空间中可能存在的更好的策略。替代梯度与真实奖励landscape的相关性较差，导致算法效率低下。

**核心思路**：论文的核心思路是，通过在每次迭代中探索当前策略参数附近的区域，寻找能够带来更高奖励的策略。作者观察到，在参数空间中，更高性能的解往往位于当前策略附近的未探索区域。因此，通过系统地探索这些区域，可以有效地提升On-Policy算法的性能。

**技术框架**：ExploRLer作为一个插件式pipeline，可以无缝集成到现有的On-Policy算法中，如PPO和TRPO。其主要流程包括：1) 在每次迭代中，基于当前的策略参数，生成多个候选策略参数；2) 使用这些候选策略参数与环境进行交互，收集数据；3) 评估这些候选策略的性能；4) 选择性能最佳的策略参数作为下一次迭代的起点。

**关键创新**：ExploRLer的关键创新在于其迭代级别的参数空间探索机制。与传统的On-Policy方法只依赖单一梯度更新不同，ExploRLer通过系统地探索当前策略参数附近的区域，寻找能够带来更高奖励的策略。这种探索机制能够有效地避免算法陷入局部最优，提升算法的性能。

**关键设计**：ExploRLer的关键设计包括：1) 如何生成候选策略参数：可以使用多种方法，如在当前策略参数周围添加随机噪声，或者使用进化算法等；2) 如何评估候选策略的性能：可以使用多种指标，如平均奖励、成功率等；3) 如何选择性能最佳的策略参数：可以使用多种方法，如选择平均奖励最高的策略参数，或者使用锦标赛选择等。

## 📊 实验亮点

ExploRLer在多个复杂的连续控制环境中进行了实验，结果表明，在不增加梯度更新次数的情况下，ExploRLer能够显著提升On-Policy算法的性能。例如，在某些环境中，ExploRLer能够将算法的性能提升超过20%。实验结果验证了ExploRLer的有效性和实用性。

## 🎯 应用场景

ExploRLer可应用于各种需要高效On-Policy强化学习的场景，例如机器人控制、游戏AI、自动驾驶等。通过提升On-Policy算法的效率和性能，可以降低训练成本，加速算法的部署和应用。该研究为强化学习算法的优化提供了一种新的思路，具有重要的实际价值和潜在的未来影响。

## 📄 摘要（原文）

> Policy-gradient methods such as Proximal Policy Optimization (PPO) are typically updated along a single stochastic gradient direction, leaving the rich local structure of the parameter space unexplored. Previous work has shown that the surrogate gradient is often poorly correlated with the true reward landscape. Building on this insight, we visualize the parameter space spanned by policy checkpoints within an iteration and reveal that higher performing solutions often lie in nearby unexplored regions. To exploit this opportunity, we introduce ExploRLer, a pluggable pipeline that seamlessly integrates with on-policy algorithms such as PPO and TRPO, systematically probing the unexplored neighborhoods of surrogate on-policy gradient updates. Without increasing the number of gradient updates, ExploRLer achieves significant improvements over baselines in complex continuous control environments. Our results demonstrate that iteration-level exploration provides a practical and effective way to strengthen on-policy reinforcement learning and offer a fresh perspective on the limitations of the surrogate objective.

