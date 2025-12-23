---
layout: default
title: Learning General Policies with Policy Gradient Methods
---

# Learning General Policies with Policy Gradient Methods

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19366" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19366v1</a>
  <a href="https://arxiv.org/pdf/2512.19366.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19366v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19366v1', 'Learning General Policies with Policy Gradient Methods')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Simon Ståhlberg, Blai Bonet, Hector Geffner

**分类**: cs.AI, cs.LG

**发布日期**: 2025-12-22

**备注**: In Proceedings of the 20th International Conference on Principles of Knowledge Representation and Reasoning (KR 2023)

---

## 💡 一句话要点

**提出基于图神经网络的策略梯度方法，学习可泛化的通用策略**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `策略梯度` `图神经网络` `泛化` `规划`

## 📋 核心要点

1. 现有强化学习方法在泛化能力上存在挑战，难以生成可靠且系统性的通用策略。
2. 论文提出将策略建模为状态转移分类器，并利用图神经网络处理关系结构，学习通用策略。
3. 实验表明，该方法在泛化能力上接近组合方法，同时避免了可扩展性瓶颈，并通过优化成本结构解决了GNN的局限性。

## 📝 摘要（中文）

强化学习方法在许多领域取得了显著成果，但泛化能力，即以可靠和系统的方式生成可泛化策略的能力，仍然是一个挑战。泛化问题在经典规划中得到了正式解决，其中使用组合方法学习了可在给定领域的所有实例中泛化的可证明正确的策略。本研究旨在将这两个研究方向结合起来，阐明在何种条件下，（深度）强化学习方法，特别是策略优化方法，可以像组合方法一样用于学习可泛化的策略。我们借鉴了先前组合和深度学习方法的经验，并以一种方便的方式对其进行了扩展。与前者类似，我们将策略建模为状态转移分类器，因为（ground）动作不是通用的，并且因实例而异。与后者类似，我们使用适用于处理关系结构的图神经网络（GNN）来表示规划状态上的价值函数，在我们的例子中，是策略。有了这些要素，我们发现actor-critic方法可以用于学习几乎与使用组合方法获得的策略一样好的策略，同时避免了可扩展性瓶颈和特征池的使用。此外，DRL方法在所考虑的基准测试中的局限性与深度学习或强化学习算法无关，而是源于GNN的表达能力限制，以及最优性和泛化之间的权衡（通用策略在某些领域可能不是最优的）。通过添加派生谓词和优化替代成本结构，可以在不改变基本DRL方法的情况下解决这两个限制。

## 🔬 方法详解

**问题定义**：现有强化学习方法在规划问题中难以泛化到不同的实例。传统的强化学习方法通常学习针对特定实例的策略，而无法推广到具有不同初始状态或目标状态的相同领域的新实例。此外，组合规划方法虽然可以生成可证明正确的通用策略，但在可扩展性方面存在瓶颈。

**核心思路**：论文的核心思路是将策略表示为状态转移分类器，而不是直接学习动作。这种表示方式允许策略在不同的实例之间共享知识，因为状态转移规则在同一领域内是通用的。此外，论文利用图神经网络（GNN）来处理规划状态的关系结构，从而更好地捕捉状态之间的依赖关系。

**技术框架**：该方法采用Actor-Critic框架，其中Actor使用GNN来表示策略，Critic使用GNN来评估策略的价值。Actor的目标是学习一个策略，该策略可以预测给定状态下采取哪个动作会导致期望的状态转移。Critic的目标是学习一个价值函数，该函数可以预测给定状态下遵循策略的预期回报。训练过程使用策略梯度方法，通过最大化预期回报来更新Actor和Critic的参数。

**关键创新**：该方法的关键创新在于将策略建模为状态转移分类器，并使用GNN来处理规划状态的关系结构。这种组合使得该方法能够学习可泛化的通用策略，同时避免了传统强化学习方法的可扩展性问题。此外，论文还提出了一种优化成本结构的方法，以解决GNN的表达能力限制。

**关键设计**：论文使用消息传递神经网络（MPNN）作为GNN的骨干网络。状态表示为图中的节点，节点之间的边表示状态之间的关系。消息传递过程用于聚合来自相邻节点的信息，从而更新节点的状态表示。策略网络使用更新后的节点表示来预测状态转移概率。损失函数包括策略梯度损失和价值函数损失。为了解决GNN的表达能力限制，论文添加了派生谓词，这些谓词是基于原始状态变量计算得到的。此外，论文还使用了一种替代成本结构，该结构鼓励策略学习更有效的状态转移。

## 📊 实验亮点

实验结果表明，该方法在多个规划基准测试中取得了与组合方法相当的泛化性能，同时避免了组合方法的可扩展性瓶颈。例如，在某些领域，该方法可以学习在所有实例中都表现良好的策略，而传统强化学习方法只能学习针对特定实例的策略。此外，通过添加派生谓词和优化成本结构，该方法可以解决GNN的表达能力限制，进一步提高泛化性能。

## 🎯 应用场景

该研究成果可应用于各种规划和决策问题，例如机器人导航、游戏AI和资源调度。通过学习可泛化的通用策略，可以使智能体在面对新的环境和任务时更加灵活和高效。此外，该方法还可以用于解决传统强化学习方法难以处理的复杂规划问题。

## 📄 摘要（原文）

> While reinforcement learning methods have delivered remarkable results in a number of settings, generalization, i.e., the ability to produce policies that generalize in a reliable and systematic way, has remained a challenge. The problem of generalization has been addressed formally in classical planning where provable correct policies that generalize over all instances of a given domain have been learned using combinatorial methods. The aim of this work is to bring these two research threads together to illuminate the conditions under which (deep) reinforcement learning approaches, and in particular, policy optimization methods, can be used to learn policies that generalize like combinatorial methods do. We draw on lessons learned from previous combinatorial and deep learning approaches, and extend them in a convenient way. From the former, we model policies as state transition classifiers, as (ground) actions are not general and change from instance to instance. From the latter, we use graph neural networks (GNNs) adapted to deal with relational structures for representing value functions over planning states, and in our case, policies. With these ingredients in place, we find that actor-critic methods can be used to learn policies that generalize almost as well as those obtained using combinatorial approaches while avoiding the scalability bottleneck and the use of feature pools. Moreover, the limitations of the DRL methods on the benchmarks considered have little to do with deep learning or reinforcement learning algorithms, and result from the well-understood expressive limitations of GNNs, and the tradeoff between optimality and generalization (general policies cannot be optimal in some domains). Both of these limitations are addressed without changing the basic DRL methods by adding derived predicates and an alternative cost structure to optimize.

