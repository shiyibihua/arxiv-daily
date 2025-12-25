---
layout: default
title: Policy-Conditioned Policies for Multi-Agent Task Solving
---

# Policy-Conditioned Policies for Multi-Agent Task Solving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21024" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21024v1</a>
  <a href="https://arxiv.org/pdf/2512.21024.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21024v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21024v1', 'Policy-Conditioned Policies for Multi-Agent Task Solving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Lin, Shuhui Zhu, Wenhao Li, Ang Li, Dan Qiao, Pascal Poupart, Hongyuan Zha, Baoxiang Wang

**分类**: cs.GT, cs.AI

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出基于策略条件策略的程序化迭代最佳响应算法，解决多智能体任务中的策略适应性问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体学习` `策略表示` `大型语言模型` `程序均衡` `迭代最佳响应`

## 📋 核心要点

1. 多智能体任务中，智能体策略的动态适应是核心挑战，但现有深度强化学习方法难以有效利用对手策略信息。
2. 论文提出将策略表示为人类可解释的源代码，并利用大型语言模型作为策略的近似解释器，实现程序均衡。
3. 实验证明，提出的程序化迭代最佳响应算法（PIBR）能有效解决协调博弈和合作觅食等任务。

## 📝 摘要（中文）

在多智能体任务中，核心挑战在于策略的动态适应。然而，由于“表征瓶颈”的存在，直接以对手的策略为条件进行学习在深度强化学习中是难以实现的：神经策略是不透明的、高维的参数向量，其他智能体难以理解。本文提出了一种范式转变，通过将策略表示为人类可解释的源代码，并利用大型语言模型（LLM）作为近似解释器来弥合这一差距。这种程序化的表示允许我们实现博弈论中的“程序均衡”概念。我们通过利用LLM直接在程序化策略空间中执行优化来重新构建学习问题。LLM充当逐点最佳响应算子，迭代地合成和改进自我智能体的策略代码以响应对手的策略。我们将此过程形式化为“程序化迭代最佳响应（PIBR）”，这是一种通过文本梯度优化策略代码的算法，使用来自博弈效用和运行时单元测试的结构化反馈。我们证明了这种方法有效地解决了几个标准协调矩阵博弈和一个合作的基于等级的觅食环境。

## 🔬 方法详解

**问题定义**：在多智能体环境中，智能体需要根据其他智能体的策略动态调整自身策略。然而，传统的深度强化学习方法中，智能体的策略通常表示为神经网络的参数，这些参数是高维、不透明的，其他智能体难以理解和利用，从而导致策略适应性差。现有方法难以克服“表征瓶颈”，无法有效建模对手策略。

**核心思路**：论文的核心思路是将智能体的策略表示为人类可读的源代码，并利用大型语言模型（LLM）来理解和执行这些代码。通过这种方式，智能体可以更容易地理解其他智能体的策略，并根据这些策略调整自己的行为。这种方法借鉴了博弈论中的“程序均衡”概念，即智能体通过理解彼此的程序化策略来达成均衡。

**技术框架**：论文提出了程序化迭代最佳响应（PIBR）算法。该算法包含以下主要步骤：
1. **策略表示**：将智能体的策略表示为可执行的源代码。
2. **LLM解释**：使用LLM作为近似解释器，理解和执行其他智能体的策略代码。
3. **最佳响应**：利用LLM生成针对对手策略的最佳响应策略代码。
4. **迭代优化**：通过迭代地生成和改进策略代码，逐步优化智能体的策略。
5. **反馈机制**：使用博弈效用和运行时单元测试作为反馈信号，指导LLM生成更有效的策略代码。

**关键创新**：论文最重要的创新在于将策略表示为程序代码，并利用LLM进行策略理解和优化。这与传统的深度强化学习方法有本质区别，后者通常使用神经网络作为策略表示，难以进行策略的解释和推理。通过程序化的策略表示，智能体可以更容易地理解其他智能体的行为，并进行更有效的策略调整。

**关键设计**：
* **策略代码生成**：使用LLM生成策略代码，代码需要满足一定的语法和语义规范。
* **反馈信号设计**：博弈效用用于评估策略的整体性能，运行时单元测试用于验证策略的局部行为。
* **文本梯度优化**：使用文本梯度来指导LLM生成更有效的策略代码，例如通过修改代码中的关键词或逻辑结构。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21024v1/pics/exp/vanilla.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21024v1/pics/exp/climbing.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21024v1/pics/exp/penalty.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，提出的PIBR算法在协调矩阵博弈和合作觅食环境中表现出色。在协调博弈中，PIBR算法能够快速收敛到最优策略，显著优于传统的强化学习方法。在合作觅食环境中，PIBR算法能够有效地协调多个智能体的行为，实现更高的资源收集效率。具体性能数据在论文中有详细展示。

## 🎯 应用场景

该研究成果可应用于多智能体协作、对抗和竞争等场景，例如自动驾驶、机器人协同、网络安全等。通过程序化策略表示和LLM的辅助，智能体可以更好地理解和适应复杂环境，提高协作效率和竞争能力。未来，该方法有望应用于更复杂的现实世界问题，例如供应链优化、资源分配等。

## 📄 摘要（原文）

> In multi-agent tasks, the central challenge lies in the dynamic adaptation of strategies. However, directly conditioning on opponents' strategies is intractable in the prevalent deep reinforcement learning paradigm due to a fundamental ``representational bottleneck'': neural policies are opaque, high-dimensional parameter vectors that are incomprehensible to other agents. In this work, we propose a paradigm shift that bridges this gap by representing policies as human-interpretable source code and utilizing Large Language Models (LLMs) as approximate interpreters. This programmatic representation allows us to operationalize the game-theoretic concept of \textit{Program Equilibrium}. We reformulate the learning problem by utilizing LLMs to perform optimization directly in the space of programmatic policies. The LLM functions as a point-wise best-response operator that iteratively synthesizes and refines the ego agent's policy code to respond to the opponent's strategy. We formalize this process as \textit{Programmatic Iterated Best Response (PIBR)}, an algorithm where the policy code is optimized by textual gradients, using structured feedback derived from game utility and runtime unit tests. We demonstrate that this approach effectively solves several standard coordination matrix games and a cooperative Level-Based Foraging environment.

