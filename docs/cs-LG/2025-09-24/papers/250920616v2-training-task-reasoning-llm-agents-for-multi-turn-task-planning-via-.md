---
layout: default
title: Training Task Reasoning LLM Agents for Multi-turn Task Planning via Single-turn Reinforcement Learning
---

# Training Task Reasoning LLM Agents for Multi-turn Task Planning via Single-turn Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20616" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20616v2</a>
  <a href="https://arxiv.org/pdf/2509.20616.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20616v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20616v2', 'Training Task Reasoning LLM Agents for Multi-turn Task Planning via Single-turn Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanjiang Hu, Changliu Liu, Na Li, Yebin Wang

**分类**: cs.LG, eess.SY

**发布日期**: 2025-09-24 (更新: 2025-12-08)

**备注**: Accepted by IEEE Control Systems Letters (L-CSS)

---

## 💡 一句话要点

**提出单轮强化学习训练任务推理LLM Agent，解决多轮任务规划问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `任务规划` `强化学习` `单轮推理` `Group Relative Policy Optimization`

## 📋 核心要点

1. 多轮任务规划中，LLM Agent面临奖励稀疏、信用分配困难和计算开销大的挑战。
2. 该论文将多轮任务规划转化为单轮任务推理，利用专家轨迹提供密集奖励，并通过GRPO进行策略优化。
3. 实验结果表明，使用单轮GRPO训练的15亿参数模型优于高达140亿参数的基线模型，长时程任务成功率达70%。

## 📝 摘要（中文）

大型语言模型(LLMs)在知识获取、推理和工具使用方面表现出卓越的能力，使其成为自主Agent应用的有希望的候选者。然而，训练LLM Agent进行复杂的多轮任务规划面临重大挑战，包括稀疏的episode奖励、跨长时程的信用分配以及多轮交互环境中强化学习的计算开销。为此，本文提出了一种新方法，将多轮任务规划转化为单轮任务推理问题，从而可以通过Group Relative Policy Optimization (GRPO)以及来自专家轨迹的密集且可验证的奖励来实现有效的策略优化。我们的理论分析表明，单轮任务推理中GRPO的改进会导致最小轮数下多轮成功概率的下界，以及推广到具有较短时程的子任务。在复杂任务规划基准上的实验评估表明，我们使用单轮GRPO训练的15亿参数模型与高达140亿参数的更大基线模型相比，实现了卓越的性能，对于长时程规划任务的成功率达到70%。

## 🔬 方法详解

**问题定义**：论文旨在解决训练LLM Agent进行复杂多轮任务规划时遇到的挑战，包括奖励稀疏性、长时程信用分配困难以及强化学习的计算开销。现有方法难以有效训练LLM Agent完成复杂任务，尤其是在需要多步交互和规划的场景下。

**核心思路**：核心思路是将复杂的多轮任务规划问题分解为更简单的单轮任务推理问题。通过这种转化，可以利用专家轨迹提供密集且可验证的奖励信号，从而避免了稀疏奖励带来的训练难题。同时，采用Group Relative Policy Optimization (GRPO) 算法进行策略优化，提高训练效率和性能。

**技术框架**：整体框架包含以下几个关键步骤：1) 将多轮任务规划问题转化为单轮任务推理问题；2) 利用专家轨迹生成密集奖励信号；3) 使用GRPO算法优化LLM Agent的策略；4) 在复杂任务规划基准上进行实验评估。该框架的核心在于将复杂问题简化，并利用专家知识加速学习过程。

**关键创新**：最重要的技术创新在于将多轮任务规划问题转化为单轮任务推理问题。这种转化使得可以使用更有效的强化学习算法（如GRPO）进行训练，并利用专家轨迹提供的密集奖励信号来克服奖励稀疏性问题。与传统的直接在多轮交互环境中进行强化学习的方法相比，该方法显著提高了训练效率和性能。

**关键设计**：论文的关键设计包括：1) 使用专家轨迹生成密集奖励函数，奖励函数的设计需要能够准确反映Agent的行为与目标之间的关系；2) 采用Group Relative Policy Optimization (GRPO) 算法进行策略优化，GRPO算法能够有效地利用专家数据，并避免策略崩溃；3) 针对具体的任务规划问题，设计合适的单轮任务推理问题，确保转化后的问题能够保留原始问题的关键信息。

## 📊 实验亮点

实验结果表明，使用单轮GRPO训练的15亿参数模型在复杂任务规划基准上取得了显著的性能提升，成功率达到70%，优于高达140亿参数的基线模型。这表明该方法能够有效地训练LLM Agent进行长时程任务规划，并且在参数效率方面具有优势。

## 🎯 应用场景

该研究成果可应用于各种需要复杂任务规划的自主Agent领域，例如机器人导航、智能家居控制、自动化客服、游戏AI等。通过提高LLM Agent的任务规划能力，可以实现更智能、更高效的自动化系统，从而提升生产效率和服务质量，具有广泛的应用前景和实际价值。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities in knowledge acquisition, reasoning, and tool use, making them promising candidates for autonomous agent applications. However, training LLM agents for complex multi-turn task planning faces significant challenges, including sparse episode-wise rewards, credit assignment across long horizons, and the computational overhead of reinforcement learning in multi-turn interaction settings. To this end, this paper introduces a novel approach that transforms multi-turn task planning into single-turn task reasoning problems, enabling efficient policy optimization through Group Relative Policy Optimization (GRPO) with dense and verifiable reward from expert trajectories. Our theoretical analysis shows that GRPO improvement on single-turn task reasoning results in a lower bound of the multi-turn success probability under the minimal turns, as well as the generalization to subtasks with shorter horizons. Experimental evaluation on the complex task planning benchmark demonstrates that our 1.5B parameter model trained with single-turn GRPO achieves superior performance compared to larger baseline models up to 14B parameters, with success rates of 70% for long-horizon planning tasks.

