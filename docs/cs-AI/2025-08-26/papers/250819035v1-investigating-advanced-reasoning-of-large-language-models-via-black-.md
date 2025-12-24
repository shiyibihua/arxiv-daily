---
layout: default
title: Investigating Advanced Reasoning of Large Language Models via Black-Box Interaction
---

# Investigating Advanced Reasoning of Large Language Models via Black-Box Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19035" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19035v1</a>
  <a href="https://arxiv.org/pdf/2508.19035.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19035v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19035v1', 'Investigating Advanced Reasoning of Large Language Models via Black-Box Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Congchi Yin, Tianyi Wu, Yankai Shu, Alex Gu, Yunhan Wang, Jun Shao, Xun Jiang, Piji Li

**分类**: cs.AI

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出黑箱交互评估范式以提升大语言模型推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理能力` `黑箱交互` `综合推理` `评估范式` `Oracle基准` `探索策略`

## 📋 核心要点

1. 现有评估方法无法全面评估大语言模型在互动环境中的推理能力，导致推理能力的孤立评估。
2. 本文提出黑箱交互评估范式，要求LLMs通过与黑箱交互推断隐藏函数，整合多种推理方式。
3. 实验结果表明，o3在大多数简单黑箱任务中表现优异，但在困难任务中仍存在显著性能下降。

## 📝 摘要（中文）

现有任务无法有效评估大语言模型（LLMs）在互动未知环境中的推理能力，导致演绎、归纳和溯因推理的孤立评估，忽视了人类在真实世界中发现所需的综合推理过程。为此，本文提出了一种新颖的评估范式——黑箱交互，要求LLMs通过与黑箱的交互，推断隐藏函数。我们构建了包含6种黑箱任务和96个黑箱的Oracle基准，评估了19个现代LLMs的表现。结果显示，o3在6个任务中有5个排名第一，但在一些困难任务中表现不佳，平均准确率低于40%。进一步分析表明，LLMs普遍缺乏高水平的规划能力，无法有效制定假设细化的探索策略。

## 🔬 方法详解

**问题定义**：本文旨在解决现有方法在评估大语言模型推理能力时的不足，特别是在互动未知环境中的综合推理评估痛点。

**核心思路**：通过引入黑箱交互的评估范式，LLMs需要在给定的探索回合中与黑箱交互，推断隐藏的输入-输出映射关系，从而实现综合推理能力的评估。

**技术框架**：整体架构包括黑箱定义、交互过程、推理过程和评估模块。LLMs通过观察输入-输出对进行推理，逐步揭示黑箱的隐藏函数。

**关键创新**：最重要的技术创新在于黑箱交互评估范式的提出，强调了推理过程的综合性，与现有孤立评估方法形成鲜明对比。

**关键设计**：在实验中，设置了多种黑箱任务，采用不同的输入-输出对进行评估，设计了适应性探索策略以提高推理效率。

## 📊 实验亮点

实验结果显示，o3在6个任务中有5个任务排名第一，在大多数简单黑箱任务中准确率超过70%。然而，在一些困难的黑箱任务中，o3的平均表现低于40%，揭示了LLMs在高水平规划能力上的普遍不足。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化决策系统和教育技术等。通过提升大语言模型的推理能力，可以更好地支持复杂任务的处理，推动人机交互的智能化发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Existing tasks fall short in evaluating reasoning ability of Large Language Models (LLMs) in an interactive, unknown environment. This deficiency leads to the isolated assessment of deductive, inductive, and abductive reasoning, neglecting the integrated reasoning process that is indispensable for humans discovery of real world. We introduce a novel evaluation paradigm, \textit{black-box interaction}, to tackle this challenge. A black-box is defined by a hidden function that maps a specific set of inputs to outputs. LLMs are required to unravel the hidden function behind the black-box by interacting with it in given exploration turns, and reasoning over observed input-output pairs. Leveraging this idea, we build the \textsc{Oracle} benchmark which comprises 6 types of black-box task and 96 black-boxes. 19 modern LLMs are benchmarked. o3 ranks first in 5 of the 6 tasks, achieving over 70\% accuracy on most easy black-boxes. But it still struggles with some hard black-box tasks, where its average performance drops below 40\%. Further analysis indicates a universal difficulty among LLMs: They lack the high-level planning capability to develop efficient and adaptive exploration strategies for hypothesis refinement.

