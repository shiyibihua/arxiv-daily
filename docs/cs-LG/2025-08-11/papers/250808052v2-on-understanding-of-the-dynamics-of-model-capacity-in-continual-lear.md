---
layout: default
title: On Understanding of the Dynamics of Model Capacity in Continual Learning
---

# On Understanding of the Dynamics of Model Capacity in Continual Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08052" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08052v2</a>
  <a href="https://arxiv.org/pdf/2508.08052.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08052v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08052v2', 'On Understanding of the Dynamics of Model Capacity in Continual Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Supriyo Chakraborty, Krishnan Raghavan

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-11 (更新: 2025-08-14)

---

## 💡 一句话要点

**提出有效模型容量以解决持续学习中的稳定性与可塑性困境**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `持续学习` `模型容量` `稳定性-可塑性` `神经网络` `任务表示` `动态学习` `优化过程`

## 📋 核心要点

1. 核心问题：持续学习中的稳定性与可塑性平衡是一个重要挑战，现有方法在处理新任务时表现出能力下降。
2. 方法要点：引入有效模型容量（CLEMC），通过差分方程描述神经网络与任务数据之间的动态关系。
3. 实验或效果：通过多种网络架构的实验，验证了有效模型容量的非平稳性及其对任务表示能力的影响。

## 📝 摘要（中文）

稳定性-可塑性困境是持续学习中的一个基本挑战，涉及神经网络的模型容量及其任务表示能力。本文引入了有效模型容量（CLEMC），用于表征稳定性-可塑性平衡点的动态行为。通过建立差分方程，模型化神经网络、任务数据和优化过程之间的相互作用。研究表明，无论神经网络的架构或优化方法如何，当新任务分布与先前任务不同时，神经网络表示新任务的能力会减弱。通过广泛的实验验证了理论发现，涵盖了从小型前馈网络到大型语言模型的多种架构。

## 🔬 方法详解

**问题定义**：本文旨在解决持续学习中的稳定性-可塑性困境，现有方法在面对新任务时，神经网络的表示能力往往会下降，尤其是在新任务分布与旧任务分布不一致时。

**核心思路**：提出有效模型容量（CLEMC），用于动态表征稳定性-可塑性平衡点的变化。通过建立差分方程，分析神经网络、任务数据和优化过程之间的相互作用，从而揭示模型容量的动态特性。

**技术框架**：整体架构包括三个主要模块：神经网络模型、任务数据输入和优化过程。通过差分方程描述这三者之间的动态关系，进而分析模型容量的变化。

**关键创新**：最重要的创新在于提出了CLEMC这一概念，强调了模型容量的非平稳性，揭示了不同任务分布对神经网络表示能力的影响，这与现有静态模型容量的理解有本质区别。

**关键设计**：在实验中，使用了多种神经网络架构，包括小型前馈网络、卷积网络、中型图神经网络和基于变换器的大型语言模型，确保了研究结果的广泛适用性。

## 📊 实验亮点

实验结果表明，提出的有效模型容量（CLEMC）能够有效捕捉神经网络在面对不同任务分布时的能力变化。无论是小型网络还是大型语言模型，均显示出在新任务分布下，表示能力显著下降，验证了理论模型的有效性。

## 🎯 应用场景

该研究对持续学习领域具有重要的应用价值，尤其是在需要处理不断变化任务分布的场景中，如机器人学习、自动驾驶和个性化推荐系统等。有效模型容量的概念可以帮助设计更具适应性的学习算法，提高模型在动态环境中的表现。

## 📄 摘要（原文）

> The stability-plasticity dilemma, closely related to a neural network's (NN) capacity-its ability to represent tasks-is a fundamental challenge in continual learning (CL). Within this context, we introduce CL's effective model capacity (CLEMC) that characterizes the dynamic behavior of the stability-plasticity balance point. We develop a difference equation to model the evolution of the interplay between the NN, task data, and optimization procedure. We then leverage CLEMC to demonstrate that the effective capacity-and, by extension, the stability-plasticity balance point is inherently non-stationary. We show that regardless of the NN architecture or optimization method, a NN's ability to represent new tasks diminishes when incoming task distributions differ from previous ones. We conduct extensive experiments to support our theoretical findings, spanning a range of architectures-from small feedforward network and convolutional networks to medium-sized graph neural networks and transformer-based large language models with millions of parameters.

