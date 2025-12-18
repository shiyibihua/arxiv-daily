---
layout: default
title: Bayesian Ego-graph Inference for Networked Multi-Agent Reinforcement Learning
---

# Bayesian Ego-graph Inference for Networked Multi-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16606" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16606v3</a>
  <a href="https://arxiv.org/pdf/2509.16606.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16606v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16606v3', 'Bayesian Ego-graph Inference for Networked Multi-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Duan, Jie Lu, Junyu Xuan

**分类**: cs.MA, cs.LG

**发布日期**: 2025-09-20 (更新: 2025-12-16)

**备注**: Accepted at NeurIPS 2025 https://openreview.net/forum?id=3qeTs05bRL

---

## 💡 一句话要点

**提出BayesG，通过贝叶斯推断学习稀疏交互结构，解决网络化多智能体强化学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `图神经网络` `贝叶斯推断` `变分推断` `动态图` `去中心化` `交通控制`

## 📋 核心要点

1. 现有Networked-MARL方法假设静态邻域，难以适应动态环境，中心化方法依赖全局信息，不适用于去中心化系统。
2. BayesG通过贝叶斯变分推断学习稀疏的、上下文感知的交互结构，每个智能体基于采样子图进行决策。
3. BayesG在交通控制任务中表现出色，智能体数量高达167个，证明了其可扩展性、效率和性能优势。

## 📝 摘要（中文）

在网络化多智能体强化学习（Networked-MARL）中，去中心化的智能体必须在局部可观测性和固定物理图上的受限通信下行动。现有方法通常假设静态邻域，限制了对动态或异构环境的适应性。虽然中心化框架可以学习动态图，但它们依赖于全局状态访问和中心化基础设施，这在实际的去中心化系统中是不切实际的。我们提出了一种基于随机图策略的Networked-MARL方法，其中每个智能体根据其局部物理邻域上的采样子图来决定其决策。在此基础上，我们引入了BayesG，一个去中心化的actor框架，它通过贝叶斯变分推断学习稀疏的、上下文感知的交互结构。每个智能体在其自我图上运行，并采样一个潜在的通信掩码来指导消息传递和策略计算。变分分布使用证据下界（ELBO）目标与策略一起进行端到端训练，使智能体能够联合学习交互拓扑和决策策略。BayesG在具有多达167个智能体的大规模交通控制任务中优于强大的MARL基线，证明了其卓越的可扩展性、效率和性能。

## 🔬 方法详解

**问题定义**：论文旨在解决网络化多智能体强化学习（Networked-MARL）中，智能体如何在局部观测和受限通信条件下，学习动态变化的交互结构的问题。现有方法主要痛点在于依赖静态邻域假设，无法有效适应动态或异构环境，而中心化方法又难以在实际去中心化系统中应用。

**核心思路**：论文的核心思路是让每个智能体学习一个稀疏的、上下文感知的交互结构，而不是依赖预定义的静态邻域。通过贝叶斯变分推断，智能体可以根据当前状态采样一个子图，并基于该子图进行消息传递和策略计算。这种方法允许智能体动态地调整其交互对象，从而更好地适应环境变化。

**技术框架**：BayesG是一个去中心化的actor框架。每个智能体维护一个ego-graph，表示其局部物理邻域。智能体首先根据自身状态和邻居状态，使用变分推断网络采样一个潜在的通信掩码。该掩码用于过滤ego-graph中的边，从而形成一个稀疏的交互子图。然后，智能体在该子图上进行消息传递，聚合邻居信息。最后，智能体基于聚合后的信息计算策略并执行动作。整个过程是端到端可训练的。

**关键创新**：最重要的技术创新点在于使用贝叶斯变分推断来学习动态的交互结构。与现有方法相比，BayesG不需要预定义静态邻域，而是允许智能体根据环境动态地选择交互对象。这种方法能够更好地适应动态和异构环境，并提高智能体的协作效率。

**关键设计**：BayesG的关键设计包括：1) 使用变分自编码器（VAE）来学习潜在的通信掩码，VAE的目标是最大化证据下界（ELBO），从而鼓励学习稀疏的交互结构；2) 使用GNN进行消息传递，聚合邻居信息；3) 使用Actor-Critic框架进行策略学习，Actor网络基于聚合后的信息输出动作，Critic网络评估动作的价值。

## 📊 实验亮点

BayesG在大型交通控制任务中取得了显著的性能提升。在包含167个智能体的场景中，BayesG优于多个强大的MARL基线，证明了其卓越的可扩展性、效率和性能。实验结果表明，BayesG能够有效地学习稀疏的交互结构，并提高智能体的协作效率。

## 🎯 应用场景

BayesG适用于需要去中心化协作且交互结构动态变化的场景，例如交通控制、机器人集群、传感器网络等。该方法能够提高系统的可扩展性、鲁棒性和适应性，在智能交通、智能制造等领域具有广泛的应用前景。

## 📄 摘要（原文）

> In networked multi-agent reinforcement learning (Networked-MARL), decentralized agents must act under local observability and constrained communication over fixed physical graphs. Existing methods often assume static neighborhoods, limiting adaptability to dynamic or heterogeneous environments. While centralized frameworks can learn dynamic graphs, their reliance on global state access and centralized infrastructure is impractical in real-world decentralized systems. We propose a stochastic graph-based policy for Networked-MARL, where each agent conditions its decision on a sampled subgraph over its local physical neighborhood. Building on this formulation, we introduce BayesG, a decentralized actor-framework that learns sparse, context-aware interaction structures via Bayesian variational inference. Each agent operates over an ego-graph and samples a latent communication mask to guide message passing and policy computation. The variational distribution is trained end-to-end alongside the policy using an evidence lower bound (ELBO) objective, enabling agents to jointly learn both interaction topology and decision-making strategies. BayesG outperforms strong MARL baselines on large-scale traffic control tasks with up to 167 agents, demonstrating superior scalability, efficiency, and performance.

