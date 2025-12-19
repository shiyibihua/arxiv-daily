---
layout: default
title: Hypernetworks That Evolve Themselves
---

# Hypernetworks That Evolve Themselves

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16406" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16406v1</a>
  <a href="https://arxiv.org/pdf/2512.16406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16406v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16406v1', 'Hypernetworks That Evolve Themselves')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joachim Winther Pedersen, Erwan Plantec, Eleni Nisioti, Marcello Barylli, Milton Montero, Kathrin Korte, Sebastian Risi

**分类**: cs.NE, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出自引用图超网络，实现无需外部优化器的神经网络自进化。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自进化神经网络` `超网络` `强化学习` `图神经网络` `自我参照` `进化算法` `开放式学习`

## 📋 核心要点

1. 现有神经网络进化依赖外部优化器，限制了其自主性和适应性，难以模拟生物进化。
2. 提出自引用图超网络，将变异和遗传机制嵌入网络内部，实现自我变异和评估，自主调整变异率。
3. 在多个强化学习基准测试中，该方法展现出快速适应环境变化的能力，并进化出连贯的运动步态。

## 📝 摘要（中文）

本文提出自引用图超网络（Self-Referential Graph HyperNetworks, Self-Referential GHNs），该系统将变异和遗传机制嵌入网络内部，无需依赖外部优化器即可实现神经网络的自进化。通过结合超网络、随机参数生成和基于图的表示，Self-Referential GHNs能够自我变异和评估，同时将变异率作为可选择的特征进行调整。在包含环境变化的强化学习基准测试（CartPoleSwitch, LunarLander-Switch）中，Self-Referential GHNs展现出快速、可靠的适应性和涌现的人口动态。在locomotion基准测试Ant-v5中，它们进化出连贯的步态，并通过自主降低种群变异性来集中于有希望的解决方案，显示出良好的微调能力。研究结果表明，可进化性本身可以从神经自我参照中涌现。Self-Referential GHNs代表着朝着更接近生物进化的合成系统迈出的一步，为自主、开放式学习智能体提供了工具。

## 🔬 方法详解

**问题定义**：现有神经网络的进化通常依赖于外部优化器，例如遗传算法或进化策略。这些外部优化器负责选择和变异网络参数，但这种方式限制了网络的自主性和适应性，也难以模拟生物进化中内在的自我进化机制。现有方法的痛点在于缺乏将进化机制内化到网络结构中的能力。

**核心思路**：本文的核心思路是将神经网络的进化机制嵌入到网络自身结构中，使其能够自我变异、自我评估，并自主调整变异率。通过构建一个自引用的系统，网络可以根据自身的性能和环境反馈来调整其进化策略，从而实现更高效和自主的进化。

**技术框架**：Self-Referential GHN 的整体架构包含以下几个主要模块：1) **图超网络 (Graph HyperNetwork)**：使用图结构来表示神经网络的连接和参数。超网络负责生成目标网络的权重。2) **随机参数生成 (Stochastic Parameter Generation)**：引入随机性，允许网络参数在一定范围内变化，从而实现变异。3) **自我参照机制 (Self-Referential Mechanism)**：网络可以访问自身的结构和性能信息，并利用这些信息来调整变异率和其他进化参数。4) **评估与选择 (Evaluation and Selection)**：通过强化学习或其他评估方法来评估网络的性能，并根据性能选择优秀的个体进行繁殖。

**关键创新**：最重要的技术创新点在于将进化机制内化到神经网络的结构中，使其能够自我参照和自我进化。与传统的外部优化器方法相比，Self-Referential GHN 能够更自主地适应环境变化，并进化出更复杂的行为。本质区别在于，传统方法依赖外部力量驱动进化，而 Self-Referential GHN 则通过内部机制实现自我驱动的进化。

**关键设计**：关键设计包括：1) **超网络结构**：超网络的设计需要能够有效地生成目标网络的权重，并允许参数的随机变异。2) **图表示**：图结构需要能够灵活地表示神经网络的连接和参数，并支持高效的变异操作。3) **变异率控制**：变异率的控制是实现稳定进化的关键，需要根据网络的性能和环境反馈进行动态调整。4) **损失函数**：使用强化学习的奖励信号作为损失函数，引导网络朝着更高的性能方向进化。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16406v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16406v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16406v1/figures/environments.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在CartPoleSwitch和LunarLander-Switch等强化学习基准测试中，Self-Referential GHNs展现出快速且可靠的适应性。在Ant-v5 locomotion基准测试中，它们进化出连贯的步态，并通过自主降低种群变异性来集中于有希望的解决方案，显示出良好的微调能力。这些结果表明，该方法在复杂环境中具有强大的适应性和进化能力。

## 🎯 应用场景

该研究成果可应用于自主机器人、游戏AI、以及其他需要持续学习和适应环境的智能体。通过实现自主进化，智能体能够更好地适应复杂和动态的环境，无需人工干预即可完成任务。未来，该技术有望推动开放式学习和通用人工智能的发展。

## 📄 摘要（原文）

> How can neural networks evolve themselves without relying on external optimizers? We propose Self-Referential Graph HyperNetworks, systems where the very machinery of variation and inheritance is embedded within the network. By uniting hypernetworks, stochastic parameter generation, and graph-based representations, Self-Referential GHNs mutate and evaluate themselves while adapting mutation rates as selectable traits. Through new reinforcement learning benchmarks with environmental shifts (CartPoleSwitch, LunarLander-Switch), Self-Referential GHNs show swift, reliable adaptation and emergent population dynamics. In the locomotion benchmark Ant-v5, they evolve coherent gaits, showing promising fine-tuning capabilities by autonomously decreasing variation in the population to concentrate around promising solutions. Our findings support the idea that evolvability itself can emerge from neural self-reference. Self-Referential GHNs reflect a step toward synthetic systems that more closely mirror biological evolution, offering tools for autonomous, open-ended learning agents.

