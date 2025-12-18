---
layout: default
title: Diversity-Incentivized Exploration for Versatile Reasoning
---

# Diversity-Incentivized Exploration for Versatile Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26209" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26209v1</a>
  <a href="https://arxiv.org/pdf/2509.26209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26209v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26209v1', 'Diversity-Incentivized Exploration for Versatile Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zican Hu, Shilin Zhang, Yafu Li, Jianhao Yan, Xuyang Hu, Leyang Cui, Xiaoye Qu, Chunlin Chen, Yu Cheng, Zhi Wang

**分类**: cs.AI

**发布日期**: 2025-09-30

**备注**: 26 pages, 10 figures

**🔗 代码/项目**: [GITHUB](https://github.com/NJU-RL/DIVER)

---

## 💡 一句话要点

**DIVER：通过多样性激励探索提升LLM的通用推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `推理能力` `多样性激励` `探索策略`

## 📋 核心要点

1. 现有RLVR方法在LLM推理任务中面临探索不足和样本效率低下的挑战，主要原因是状态-动作空间巨大和奖励稀疏。
2. DIVER框架通过引入全局序列级别多样性作为内在奖励，激励LLM在语义结构化空间中进行深度探索，提升推理能力。
3. 实验结果表明，DIVER在领域内和领域外任务上均优于现有RLVR基线，并在Pass@1和Pass@k评估中取得了显著提升。

## 📝 摘要（中文）

具有可验证奖励的强化学习（RLVR）已成为激励大型语言模型（LLM）推理能力的关键范例。由于推理任务中巨大的状态-动作空间和奖励稀疏性，现有方法通常面临探索不足和样本效率低下的问题。在本文中，我们提出了DIVER（用于通用推理的多样性激励探索），这是一个创新的框架，强调全局序列级别多样性的关键作用，以激励对通用推理的深度探索。我们首先进行了一项初步的实证研究，揭示了全局多样性与推理能力之间存在很强的正相关关系。在此基础上，我们引入全局多样性激励作为内在奖励，以促进在语义结构化空间中的深度探索。结合内在奖励，我们开发了一种基于势的奖励塑造机制，以保持最优策略不变性，并设计了简单的启发式方法来缓解可能的奖励黑客行为。实验结果表明，DIVER在领域内和领域外任务上都优于具有各种探索策略的竞争性RLVR基线，在Pass@1和Pass@k评估中表现出色。我们的代码可在https://github.com/NJU-RL/DIVER上找到。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在复杂推理任务中，由于状态空间巨大和奖励稀疏导致的探索不足问题。现有基于强化学习的方法难以有效探索，导致样本效率低下，最终影响模型的推理能力。

**核心思路**：论文的核心思路是利用全局序列级别的多样性来激励模型进行更深入的探索。作者发现全局多样性与推理能力之间存在正相关关系，因此将多样性作为一种内在奖励，引导模型探索更多不同的推理路径。

**技术框架**：DIVER框架主要包含以下几个模块：1) 奖励函数设计，包含外部奖励（来自环境）和内在奖励（基于全局多样性）；2) 基于势的奖励塑造机制，用于保证策略的最优性；3) 启发式方法，用于缓解奖励黑客问题。整体流程是，模型在环境中进行探索，根据外部奖励和内在奖励更新策略，并通过奖励塑造和启发式方法进行优化。

**关键创新**：该论文的关键创新在于将全局序列级别的多样性引入作为内在奖励，用于激励LLM进行深度探索。与传统的探索方法不同，DIVER关注的是整个推理序列的多样性，而不是单个动作的多样性，从而更好地引导模型探索更有效的推理路径。

**关键设计**：内在奖励的设计是关键，论文中采用某种方式（具体方式未知，需要查看论文细节）来衡量全局序列的多样性，并将其作为内在奖励添加到总奖励中。此外，基于势的奖励塑造机制的具体实现方式（具体公式未知，需要查看论文细节）以及启发式方法的具体设计（具体方法未知，需要查看论文细节）也是重要的技术细节。

## 📊 实验亮点

DIVER在领域内和领域外任务上均取得了显著的性能提升。具体而言，在Pass@1和Pass@k评估中，DIVER优于各种具有不同探索策略的竞争性RLVR基线。这些实验结果表明，DIVER能够有效地提升LLM的推理能力，并且具有良好的泛化能力。

## 🎯 应用场景

该研究成果可应用于各种需要复杂推理能力的场景，例如问答系统、对话生成、代码生成等。通过提升LLM的推理能力，可以提高这些应用在复杂任务上的性能和可靠性，具有重要的实际应用价值和潜在的商业前景。

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a crucial paradigm for incentivizing reasoning capabilities in Large Language Models (LLMs). Due to vast state-action spaces and reward sparsity in reasoning tasks, existing methods often struggle with deficient exploration and poor sample efficiency. In the paper, we propose \textbf{DIVER} (\textbf{D}iversity-\textbf{I}ncentivized Exploration for \textbf{V}ersatil\textbf{E} \textbf{R}easoning), an innovative framework that highlights the pivotal role of global sequence-level diversity to incentivize deep exploration for versatile reasoning. We first conduct a primary empirical study to reveal a strong positive correlation between global diversity and reasoning capacity. Building on this insight, we introduce global diversity incentives as an intrinsic reward to promote deep exploration in a semantically structured space. Incorporating the intrinsic reward, we develop a potential-based reward shaping mechanism to preserve optimal policy invariance and design simple heuristics to mitigate possible reward hacking. Experimental results show that DIVER outperforms competitive RLVR baselines with various exploration strategies on both in-domain and out-of-domain tasks, excelling in both Pass@1 and Pass@k evaluations. Our code is available at https://github.com/NJU-RL/DIVER.

