---
layout: default
title: The Decrypto Benchmark for Multi-Agent Reasoning and Theory of Mind
---

# The Decrypto Benchmark for Multi-Agent Reasoning and Theory of Mind

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20664" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20664v1</a>
  <a href="https://arxiv.org/pdf/2506.20664.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20664v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20664v1', 'The Decrypto Benchmark for Multi-Agent Reasoning and Theory of Mind')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrei Lupu, Timon Willi, Jakob Foerster

**分类**: cs.AI, cs.CL, cs.HC, cs.MA

**发布日期**: 2025-06-25

**备注**: 41 pages, 19 figures

---

## 💡 一句话要点

**提出Decrypto基准以解决多智能体推理与心智理论问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体推理` `心智理论` `大型语言模型` `游戏基准` `认知科学` `强化学习` `人工智能代理`

## 📋 核心要点

1. 现有的多智能体推理和心智理论评估基准存在范围狭窄、数据泄露和缺乏互动等问题。
2. Decrypto基准通过游戏化设计，旨在提供一个清晰、无混淆因素的多智能体推理与ToM评估平台。
3. 实验结果表明，当前最先进的推理模型在ToM任务上的表现不如早期模型，显示出Decrypto的重要性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）具备代理能力，它们需要在复杂的多智能体场景中与人类用户及其他智能体进行互动。这要求新的推理技能，尤其是心智理论（ToM），即推理其他智能体“心理”状态的能力。然而，现有基准在ToM及其他多智能体能力的评估上存在不足。为此，本文提出了Decrypto，一个基于游戏的多智能体推理与ToM基准，旨在消除现有基准中的混淆因素。通过对前沿LLMs的全面评估，我们发现其游戏能力落后于人类和简单的词嵌入基线。Decrypto填补了当前推理与ToM评估中的重要空白，为更好的人工智能代理铺平了道路。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多智能体场景中推理能力不足的问题。现有基准存在范围狭窄、数据泄露和缺乏互动等痛点，导致对ToM能力的评估不够全面。

**核心思路**：Decrypto基准通过游戏化的方式设计，灵感来源于认知科学和多智能体强化学习，旨在提供一个易于评估的环境，消除其他基准中的混淆因素。

**技术框架**：Decrypto的整体架构包括多个模块，首先是游戏环境的设计，其次是智能体与环境的互动，最后是评估智能体在推理和ToM任务中的表现。

**关键创新**：Decrypto是首个专门为设计互动性ToM实验而构建的平台，填补了现有评估中的重要空白。与传统方法相比，它提供了更为清晰和可控的评估环境。

**关键设计**：在设计中，Decrypto采用了特定的游戏规则和任务设置，以确保评估的有效性和可靠性，同时避免了常见的评估混淆因素。

## 📊 实验亮点

实验结果显示，当前最先进的LLMs在Decrypto基准上的表现显著低于人类和简单的词嵌入基线，表明其在多智能体推理和心智理论任务中的能力仍有待提升。这一发现强调了Decrypto在推动人工智能研究中的重要性。

## 🎯 应用场景

Decrypto基准的潜在应用领域包括人工智能代理的开发、智能体间的协作与竞争研究，以及心智理论相关的认知科学实验。其设计理念和评估方法可以为未来的多智能体系统提供重要的参考，推动智能体在复杂环境中的表现提升。

## 📄 摘要（原文）

> As Large Language Models (LLMs) gain agentic abilities, they will have to navigate complex multi-agent scenarios, interacting with human users and other agents in cooperative and competitive settings. This will require new reasoning skills, chief amongst them being theory of mind (ToM), or the ability to reason about the "mental" states of other agents. However, ToM and other multi-agent abilities in LLMs are poorly understood, since existing benchmarks suffer from narrow scope, data leakage, saturation, and lack of interactivity. We thus propose Decrypto, a game-based benchmark for multi-agent reasoning and ToM drawing inspiration from cognitive science, computational pragmatics and multi-agent reinforcement learning. It is designed to be as easy as possible in all other dimensions, eliminating confounding factors commonly found in other benchmarks. To our knowledge, it is also the first platform for designing interactive ToM experiments.
>   We validate the benchmark design through comprehensive empirical evaluations of frontier LLMs, robustness studies, and human-AI cross-play experiments. We find that LLM game-playing abilities lag behind humans and simple word-embedding baselines. We then create variants of two classic cognitive science experiments within Decrypto to evaluate three key ToM abilities. Surprisingly, we find that state-of-the-art reasoning models are significantly worse at those tasks than their older counterparts. This demonstrates that Decrypto addresses a crucial gap in current reasoning and ToM evaluations, and paves the path towards better artificial agents.

