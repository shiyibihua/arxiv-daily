---
layout: default
title: "Context as a Tool: Context Management for Long-Horizon SWE-Agents"
---

# Context as a Tool: Context Management for Long-Horizon SWE-Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.22087" class="toolbar-btn" target="_blank">📄 arXiv: 2512.22087v1</a>
  <a href="https://arxiv.org/pdf/2512.22087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.22087v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.22087v1', 'Context as a Tool: Context Management for Long-Horizon SWE-Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shukai Liu, Jian Yang, Bo Jiang, Yizhi Li, Jinyang Guo, Xianglong Liu, Bryan Dai

**分类**: cs.CL

**发布日期**: 2025-12-26

---

## 💡 一句话要点

**提出CAT框架，通过可调用工具管理上下文，提升长程软件工程Agent性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文管理` `软件工程Agent` `长程推理` `大型语言模型` `主动压缩`

## 📋 核心要点

1. 现有Agent在长程软件工程任务中，依赖追加式上下文维护或被动触发的压缩启发式方法，导致上下文爆炸和推理能力下降。
2. CAT框架将上下文维护作为Agent的可调用工具，主动压缩历史轨迹，形成可操作的摘要，优化上下文管理。
3. 通过CAT-GENERATOR框架训练的SWE-Compressor在SWE-Bench-Verified上表现出色，解决率达57.6%，显著优于现有方法。

## 📝 摘要（中文）

本文提出了一种新的上下文管理范式CAT，旨在解决基于大型语言模型的Agent在处理需要与代码库进行长程交互的实际软件工程（SWE）任务时，面临的上下文爆炸、语义漂移和推理能力下降等问题。CAT将上下文维护提升为Agent决策过程中的可调用工具，构建了一个结构化的上下文工作空间，包括稳定的任务语义、精简的长期记忆和高保真的短期交互。此外，提出了一个基于离线数据构建流程的轨迹级监督框架CAT-GENERATOR，用于将上下文管理动作注入到完整的交互轨迹中，并训练了一个上下文感知的模型SWE-Compressor。在SWE-Bench-Verified上的实验表明，SWE-Compressor达到了57.6%的解决率，显著优于基于ReAct的Agent和静态压缩基线，同时在有限的上下文预算下保持了稳定和可扩展的长程推理能力。

## 🔬 方法详解

**问题定义**：现有基于LLM的Agent在处理长程软件工程任务时，由于需要维护与代码库的大量交互历史，容易出现上下文爆炸、语义漂移等问题，导致推理性能下降。现有的上下文管理方法要么是简单地追加信息，要么是被动地进行压缩，缺乏主动性和结构性，无法有效管理上下文信息。

**核心思路**：CAT的核心思路是将上下文管理提升为Agent的一个可调用工具，使其能够主动地、有选择性地压缩和维护上下文信息。通过构建一个结构化的上下文工作空间，Agent可以更好地组织和利用上下文信息，从而提高长程推理能力。这种主动式的上下文管理方式能够避免上下文爆炸和语义漂移，保持上下文的相关性和有效性。

**技术框架**：CAT框架包含三个主要组成部分：结构化的上下文工作空间、可调用的上下文管理工具以及轨迹级监督框架CAT-GENERATOR。上下文工作空间由稳定的任务语义、精简的长期记忆和高保真的短期交互组成。上下文管理工具允许Agent主动压缩历史轨迹，形成可操作的摘要。CAT-GENERATOR则通过离线数据构建流程，将上下文管理动作注入到完整的交互轨迹中，用于训练上下文感知的模型。

**关键创新**：CAT最重要的创新在于将上下文管理从被动式策略提升为Agent的主动式工具。与传统的追加式或被动压缩方法不同，CAT允许Agent根据当前的任务状态和历史交互信息，主动地选择何时以及如何压缩上下文。这种主动式的上下文管理方式能够更好地适应长程任务的需求，提高Agent的推理能力和效率。

**关键设计**：CAT-GENERATOR框架通过离线数据构建流程，生成带有上下文管理动作的交互轨迹。这些轨迹用于训练SWE-Compressor模型，该模型能够预测何时以及如何压缩上下文。具体来说，SWE-Compressor可能使用Transformer架构，并采用监督学习的方式进行训练，损失函数旨在最小化预测的上下文管理动作与真实动作之间的差异。具体的参数设置和网络结构可能需要根据实际情况进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22087v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22087v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22087v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于CAT框架训练的SWE-Compressor在SWE-Bench-Verified数据集上达到了57.6%的解决率，显著优于基于ReAct的Agent和静态压缩基线。这表明CAT框架能够有效地提升Agent在长程软件工程任务中的性能。此外，实验还验证了SWE-Compressor在有限的上下文预算下，能够保持稳定和可扩展的长程推理能力。

## 🎯 应用场景

该研究成果可应用于各种需要长程交互和复杂推理的软件工程任务，例如代码修复、代码重构、缺陷定位等。通过有效管理上下文信息，可以显著提升软件工程Agent的性能和效率，降低开发成本，提高软件质量。此外，该方法还可以推广到其他需要上下文管理的AI应用领域，例如对话系统、机器人导航等。

## 📄 摘要（原文）

> Agents based on large language models have recently shown strong potential on real-world software engineering (SWE) tasks that require long-horizon interaction with repository-scale codebases. However, most existing agents rely on append-only context maintenance or passively triggered compression heuristics, which often lead to context explosion, semantic drift, and degraded reasoning in long-running interactions. We propose CAT, a new context management paradigm that elevates context maintenance to a callable tool integrated into the decision-making process of agents. CAT formalizes a structured context workspace consisting of stable task semantics, condensed long-term memory, and high-fidelity short-term interactions, and enables agents to proactively compress historical trajectories into actionable summaries at appropriate milestones. To support context management for SWE-agents, we propose a trajectory-level supervision framework, CAT-GENERATOR, based on an offline data construction pipeline that injects context-management actions into complete interaction trajectories. Using this framework, we train a context-aware model, SWE-Compressor. Experiments on SWE-Bench-Verified demonstrate that SWE-Compressor reaches a 57.6% solved rate and significantly outperforms ReAct-based agents and static compression baselines, while maintaining stable and scalable long-horizon reasoning under a bounded context budget.

