---
layout: default
title: Meta-RL Induces Exploration in Language Agents
---

# Meta-RL Induces Exploration in Language Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16848" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16848v1</a>
  <a href="https://arxiv.org/pdf/2512.16848.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16848v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16848v1', 'Meta-RL Induces Exploration in Language Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yulun Jiang, Liangze Jiang, Damien Teney, Michael Moor, Maria Brbic

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**LaMer：基于元强化学习提升语言Agent在复杂环境中的探索能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `元强化学习` `语言Agent` `探索策略` `上下文学习` `策略适应`

## 📋 核心要点

1. 现有RL训练的LLM Agent在需要主动探索和长期规划的任务中表现不足，难以有效利用试错经验。
2. LaMer通过元强化学习框架，鼓励Agent在训练时进行跨episode的探索，并在测试时通过反思进行策略调整。
3. 实验结果表明，LaMer在Sokoban、MineSweeper和Webshop等任务中显著优于RL基线，并具有更好的泛化能力。

## 📝 摘要（中文）

强化学习(RL)使得训练大型语言模型(LLM) Agent与环境交互并解决多轮长时程任务成为可能。然而，RL训练的Agent在需要主动探索的任务中表现不佳，并且无法有效地从试错经验中学习。本文提出了LaMer，一个通用的元强化学习框架，使LLM Agent能够在测试时主动探索并从环境反馈中学习。LaMer包含两个关键组件：(i)一个跨episode的训练框架，鼓励探索和长期奖励优化；(ii)通过反思进行上下文策略调整，允许Agent从任务反馈信号中调整其策略，而无需梯度更新。在各种环境中的实验表明，LaMer显著提高了性能，在Sokoban、MineSweeper和Webshop上的性能分别提高了11%、14%和19%。此外，与RL训练的Agent相比，LaMer还展示了更好的泛化能力，可以应对更具挑战性或以前未见过的任务。总的来说，我们的结果表明，元强化学习提供了一种原则性的方法来诱导语言Agent进行探索，从而通过学习到的探索策略实现对新环境的更稳健的适应。

## 🔬 方法详解

**问题定义**：现有的基于强化学习的语言Agent在复杂环境中进行探索时存在效率低下的问题。它们难以有效地从试错经验中学习，尤其是在需要长期规划和主动探索的任务中。传统的强化学习方法往往侧重于利用已知的策略，而忽略了对未知状态和行为的探索，导致Agent容易陷入局部最优解。

**核心思路**：LaMer的核心思路是利用元强化学习的思想，让Agent学习如何进行有效的探索。通过跨episode的训练，Agent可以学习到一种通用的探索策略，使其能够在新的环境中快速适应并找到最优解。此外，LaMer还引入了反思机制，允许Agent根据环境的反馈信号动态调整其策略，从而提高其适应性和鲁棒性。

**技术框架**：LaMer的整体框架包含两个主要阶段：(1) 跨episode训练阶段：在此阶段，Agent在多个不同的episode中与环境交互，并根据获得的奖励更新其策略。该阶段的目标是学习一种通用的探索策略，使其能够在不同的环境中快速适应。(2) 上下文策略调整阶段：在此阶段，Agent根据环境的反馈信号，通过反思机制动态调整其策略。该阶段的目标是提高Agent的适应性和鲁棒性，使其能够更好地应对新的环境。

**关键创新**：LaMer的关键创新在于将元强化学习的思想应用于语言Agent的探索问题。与传统的强化学习方法相比，LaMer能够学习一种通用的探索策略，使其能够在新的环境中快速适应并找到最优解。此外，LaMer的反思机制也能够有效地提高Agent的适应性和鲁棒性。

**关键设计**：LaMer的关键设计包括：(1) 跨episode训练框架：该框架鼓励Agent在不同的episode中进行探索，并根据获得的奖励更新其策略。(2) 反思机制：该机制允许Agent根据环境的反馈信号动态调整其策略。具体来说，Agent会根据过去的经验和当前的反馈，生成一段反思文本，然后将该文本作为上下文信息输入到策略网络中，从而调整其行为。损失函数的设计目标是最大化长期奖励，并鼓励Agent进行有效的探索。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16848v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16848v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16848v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LaMer在Sokoban、MineSweeper和Webshop等任务中取得了显著的性能提升，分别提高了11%、14%和19%。与传统的RL基线相比，LaMer不仅在性能上有所提升，而且还具有更好的泛化能力，能够更好地应对新的环境和任务。这些结果表明，LaMer是一种有效的元强化学习框架，可以显著提高语言Agent的探索能力。

## 🎯 应用场景

LaMer具有广泛的应用前景，例如可以应用于游戏AI、机器人控制、自动驾驶等领域。通过学习有效的探索策略，Agent可以在复杂环境中自主地完成各种任务，例如在游戏中找到最优策略，在机器人控制中实现自主导航，在自动驾驶中安全地行驶。此外，LaMer还可以应用于教育领域，帮助学生更好地学习和掌握知识。

## 📄 摘要（原文）

> Reinforcement learning (RL) has enabled the training of large language model (LLM) agents to interact with the environment and to solve multi-turn long-horizon tasks. However, the RL-trained agents often struggle in tasks that require active exploration and fail to efficiently adapt from trial-and-error experiences. In this paper, we present LaMer, a general Meta-RL framework that enables LLM agents to actively explore and learn from the environment feedback at test time. LaMer consists of two key components: (i) a cross-episode training framework to encourage exploration and long-term rewards optimization; and (ii) in-context policy adaptation via reflection, allowing the agent to adapt their policy from task feedback signal without gradient update. Experiments across diverse environments show that LaMer significantly improves performance over RL baselines, with 11%, 14%, and 19% performance gains on Sokoban, MineSweeper and Webshop, respectively. Moreover, LaMer also demonstrates better generalization to more challenging or previously unseen tasks compared to the RL-trained agents. Overall, our results demonstrate that Meta-RL provides a principled approach to induce exploration in language agents, enabling more robust adaptation to novel environments through learned exploration strategies.

