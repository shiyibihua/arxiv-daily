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

**关键词**: `自进化神经网络` `超网络` `强化学习` `神经进化` `图神经网络`

## 📋 核心要点

1. 现有神经网络进化依赖外部优化器，限制了其自主性和适应性。
2. 提出自引用图超网络，将变异和遗传机制嵌入网络内部，实现自我进化。
3. 实验表明，该方法在环境变化和步态进化任务中表现出快速适应性和微调能力。

## 📝 摘要（中文）

本文提出自引用图超网络（Self-Referential Graph HyperNetworks, Self-Referential GHNs），该系统将变异和遗传机制嵌入网络内部，无需依赖外部优化器即可实现神经网络的自进化。通过结合超网络、随机参数生成和基于图的表示，Self-Referential GHNs能够自我变异和评估，同时将变异率作为可选择的特征进行调整。在具有环境变化的强化学习基准测试（CartPoleSwitch, LunarLander-Switch）中，Self-Referential GHNs展现出快速、可靠的适应性和涌现的人口动态。在locomotion基准测试Ant-v5中，它们进化出连贯的步态，并通过自主降低种群变异性以集中于有希望的解决方案，展现出良好的微调能力。研究结果表明，可进化性本身可以从神经自我参照中涌现。Self-Referential GHNs代表了朝着更接近生物进化的合成系统迈出的一步，为自主、开放式学习智能体提供了工具。

## 🔬 方法详解

**问题定义**：现有神经网络的进化通常依赖于外部优化器，例如遗传算法或进化策略。这种依赖限制了神经网络的自主性和适应性，尤其是在环境动态变化的情况下。此外，如何有效地控制和调整变异过程，使其能够适应不同的任务和环境，也是一个挑战。

**核心思路**：本文的核心思路是将神经网络的进化机制嵌入到网络本身，使其能够自我变异、评估和选择。通过使用超网络生成网络的参数，并结合随机参数生成和基于图的表示，实现网络的自我参照和自我进化。这种设计允许网络自主地调整变异率，并根据环境反馈进行优化。

**技术框架**：Self-Referential GHN 的整体架构包含以下几个主要模块：1) 图表示模块：使用图结构表示神经网络的结构和连接。2) 超网络模块：使用超网络生成图结构中各个节点的参数。3) 随机参数生成模块：引入随机性，使得网络可以探索不同的参数空间。4) 评估模块：使用强化学习或其他方法评估网络的性能。5) 变异率控制模块：将变异率作为可选择的特征，通过学习来调整变异的幅度。整个流程是循环的，网络不断地自我变异、评估和选择，从而实现进化。

**关键创新**：最重要的技术创新点在于将进化机制嵌入到神经网络本身，实现了真正的自我进化。与传统的进化算法相比，Self-Referential GHN 不需要外部优化器，而是通过自我参照和自我评估来实现优化。此外，将变异率作为可选择的特征进行学习，使得网络可以自主地调整变异的幅度，从而更好地适应不同的任务和环境。

**关键设计**：在具体实现上，超网络的设计至关重要，需要能够生成具有多样性和适应性的参数。随机参数生成模块需要引入适当的随机性，以保证网络的探索能力。评估模块需要选择合适的评估指标和方法，以准确地评估网络的性能。变异率控制模块需要设计合适的损失函数和优化算法，以有效地调整变异的幅度。具体的网络结构、参数设置和损失函数需要根据具体的任务进行调整。

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

在CartPoleSwitch和LunarLander-Switch等强化学习基准测试中，Self-Referential GHNs展现出快速、可靠的适应性。在Ant-v5 locomotion任务中，它们进化出连贯的步态，并通过自主降低种群变异性以集中于有希望的解决方案，展现出良好的微调能力。这些结果表明，该方法在复杂和动态环境中具有良好的适应性和优化能力。

## 🎯 应用场景

该研究成果可应用于自主机器人、游戏AI、以及其他需要持续学习和适应环境的智能体。通过实现神经网络的自我进化，可以降低对人工干预的依赖，提高智能体的自主性和鲁棒性。未来，该技术有望应用于开发更智能、更灵活的AI系统，例如能够自主适应新环境的机器人或能够不断学习和进化的游戏AI。

## 📄 摘要（原文）

> How can neural networks evolve themselves without relying on external optimizers? We propose Self-Referential Graph HyperNetworks, systems where the very machinery of variation and inheritance is embedded within the network. By uniting hypernetworks, stochastic parameter generation, and graph-based representations, Self-Referential GHNs mutate and evaluate themselves while adapting mutation rates as selectable traits. Through new reinforcement learning benchmarks with environmental shifts (CartPoleSwitch, LunarLander-Switch), Self-Referential GHNs show swift, reliable adaptation and emergent population dynamics. In the locomotion benchmark Ant-v5, they evolve coherent gaits, showing promising fine-tuning capabilities by autonomously decreasing variation in the population to concentrate around promising solutions. Our findings support the idea that evolvability itself can emerge from neural self-reference. Self-Referential GHNs reflect a step toward synthetic systems that more closely mirror biological evolution, offering tools for autonomous, open-ended learning agents.

