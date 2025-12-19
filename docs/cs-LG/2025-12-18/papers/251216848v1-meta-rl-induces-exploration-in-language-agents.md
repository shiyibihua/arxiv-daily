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

**LaMer：通过元强化学习提升语言Agent在复杂环境中的探索能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `元强化学习` `语言Agent` `主动探索` `上下文学习` `策略适应`

## 📋 核心要点

1. 现有RL训练的语言Agent在需要主动探索和从经验中学习的任务中表现不佳。
2. LaMer通过跨episode训练鼓励探索，并利用反思机制实现上下文策略适应，无需梯度更新。
3. 实验表明，LaMer在多个环境中显著优于RL基线，并具有更好的泛化能力。

## 📝 摘要（中文）

强化学习(RL)已使大型语言模型(LLM)Agent能够与环境交互并解决多轮长时程任务。然而，RL训练的Agent在需要主动探索的任务中常常表现不佳，并且无法有效地从试错经验中学习。本文提出了LaMer，一个通用的元强化学习框架，使LLM Agent能够在测试时主动探索并从环境反馈中学习。LaMer包含两个关键组件：(i)一个跨episode训练框架，以鼓励探索和长期奖励优化；(ii)通过反思进行上下文策略适应，允许Agent从任务反馈信号中调整其策略，而无需梯度更新。在各种环境中的实验表明，LaMer显著提高了相对于RL基线的性能，在Sokoban、MineSweeper和Webshop上分别提高了11%、14%和19%的性能。此外，与RL训练的Agent相比，LaMer还展示了对更具挑战性或先前未见过的任务更好的泛化能力。总的来说，我们的结果表明，元强化学习提供了一种原则性的方法来诱导语言Agent中的探索，从而通过学习到的探索策略实现对新环境的更鲁棒的适应。

## 🔬 方法详解

**问题定义**：现有基于强化学习训练的语言Agent在复杂环境中进行探索时效率低下，难以适应新任务。它们通常难以平衡探索和利用，导致次优策略和泛化能力不足。尤其是在长时程任务中，奖励稀疏问题更加突出，Agent难以有效地从试错中学习。

**核心思路**：LaMer的核心思路是利用元强化学习(Meta-RL)的思想，让Agent学习如何学习。通过跨episode的训练，Agent能够学会主动探索环境，并根据环境反馈快速调整策略。这种“学会探索”的能力使得Agent能够更有效地适应新的、未知的任务。

**技术框架**：LaMer框架包含两个主要组成部分：(1) **跨episode训练框架**：该框架通过构建多个episode的任务，鼓励Agent在不同episode之间进行知识迁移，从而学习到更通用的探索策略。训练目标是最大化长期奖励，促使Agent关注长远利益。(2) **上下文策略适应**：该模块利用Agent的反思能力，根据任务的反馈信号（例如奖励、状态变化等）调整策略。这种调整是在上下文环境中进行的，无需进行梯度更新，从而实现了快速适应。

**关键创新**：LaMer的关键创新在于将元强化学习的思想引入到语言Agent的训练中，并设计了跨episode训练和上下文策略适应机制。与传统的RL方法相比，LaMer能够让Agent学会主动探索，并快速适应新任务，从而提高了Agent的泛化能力和鲁棒性。此外，无需梯度更新的上下文策略适应机制也提高了训练效率。

**关键设计**：在跨episode训练中，采用了精心设计的奖励函数，以鼓励Agent进行多样化的探索。上下文策略适应模块利用Transformer架构，将任务反馈信号作为上下文信息输入到Agent中，从而影响Agent的决策。具体而言，Agent会根据历史经验和当前反馈，生成新的行动策略。此外，还采用了经验回放机制，用于存储和重用过去的经验，从而提高学习效率。

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

实验结果表明，LaMer在Sokoban、MineSweeper和Webshop等多个环境中显著优于RL基线，性能分别提升了11%、14%和19%。此外，LaMer还展示了更好的泛化能力，能够适应更具挑战性或先前未见过的任务。这些结果验证了元强化学习在诱导语言Agent探索方面的有效性。

## 🎯 应用场景

LaMer框架可应用于各种需要语言Agent进行主动探索和适应的场景，例如机器人导航、游戏AI、智能助手等。通过学习到的探索策略，Agent能够更有效地完成复杂任务，并适应不断变化的环境。该研究有助于推动通用人工智能的发展，使Agent能够更好地理解和交互真实世界。

## 📄 摘要（原文）

> Reinforcement learning (RL) has enabled the training of large language model (LLM) agents to interact with the environment and to solve multi-turn long-horizon tasks. However, the RL-trained agents often struggle in tasks that require active exploration and fail to efficiently adapt from trial-and-error experiences. In this paper, we present LaMer, a general Meta-RL framework that enables LLM agents to actively explore and learn from the environment feedback at test time. LaMer consists of two key components: (i) a cross-episode training framework to encourage exploration and long-term rewards optimization; and (ii) in-context policy adaptation via reflection, allowing the agent to adapt their policy from task feedback signal without gradient update. Experiments across diverse environments show that LaMer significantly improves performance over RL baselines, with 11%, 14%, and 19% performance gains on Sokoban, MineSweeper and Webshop, respectively. Moreover, LaMer also demonstrates better generalization to more challenging or previously unseen tasks compared to the RL-trained agents. Overall, our results demonstrate that Meta-RL provides a principled approach to induce exploration in language agents, enabling more robust adaptation to novel environments through learned exploration strategies.

