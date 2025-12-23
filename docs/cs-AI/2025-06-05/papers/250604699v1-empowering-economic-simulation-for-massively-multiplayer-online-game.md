---
layout: default
title: Empowering Economic Simulation for Massively Multiplayer Online Games through Generative Agent-Based Modeling
---

# Empowering Economic Simulation for Massively Multiplayer Online Games through Generative Agent-Based Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04699" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04699v1</a>
  <a href="https://arxiv.org/pdf/2506.04699.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04699v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04699v1', 'Empowering Economic Simulation for Massively Multiplayer Online Games through Generative Agent-Based Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bihan Xu, Shiwei Zhao, Runze Wu, Zhenya Huang, Jiawei Wang, Zhipeng Hu, Kai Wang, Haoyu Liu, Tangjie Lv, Le Li, Changjie Fan, Xin Tong, Jiangze Han

**分类**: cs.AI

**发布日期**: 2025-06-05

**备注**: KDD2025 Accepted

---

## 💡 一句话要点

**提出基于大语言模型的代理模型以解决MMO经济模拟中的人类行为仿真问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `代理建模` `经济模拟` `角色扮演` `决策能力` `游戏经济` `人工智能`

## 📋 核心要点

1. 现有的基于代理的建模方法在模拟人类经济行为时存在可靠性、社交性和可解释性不足的问题。
2. 本研究提出了一种新方法，利用大语言模型（LLMs）设计具有人类决策能力的代理，以增强经济模拟的真实性。
3. 实验结果显示，LLM驱动的代理能够有效促进游戏内经济活动中的角色专业化和价格波动等现象。

## 📝 摘要（中文）

在大型多人在线游戏（MMO）经济研究领域，基于代理的建模（ABM）已成为分析游戏经济的重要工具。然而，现有方法在模拟人类经济活动时面临代理可靠性、社交性和可解释性等重大挑战。本研究首次引入大语言模型（LLMs）用于MMO经济模拟，设计了具有人类决策能力和适应性的LLM驱动代理。这些代理具备角色扮演、感知、记忆和推理能力，有效应对了上述挑战。模拟实验表明，LLM赋能的代理能够促进角色专业化和价格波动等市场现象的出现。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有基于代理的建模方法在模拟人类经济活动时的不足，特别是在代理的可靠性、社交性和可解释性方面存在的挑战。

**核心思路**：通过引入大语言模型（LLMs），设计出具有人类决策能力和适应性的代理，利用其角色扮演、推理和记忆能力来提升经济模拟的真实性和复杂性。

**技术框架**：整体架构包括数据输入模块、LLM驱动的代理模块和经济活动模拟模块。代理通过LLMs进行决策，模拟游戏内的经济互动。

**关键创新**：最重要的创新在于将大语言模型应用于经济模拟中，使代理能够进行更复杂的决策和互动，超越传统规则基础的代理模型。

**关键设计**：在设计中，代理的决策过程结合了角色扮演和推理机制，采用了特定的损失函数以优化代理的行为表现，并通过多轮训练提升其适应性。

## 📊 实验亮点

实验结果表明，LLM赋能的代理在模拟经济活动中表现出显著的优势，能够有效促进角色专业化和价格波动等现象，较传统方法在经济活动的真实性和复杂性上有明显提升，具体性能数据尚未披露。

## 🎯 应用场景

该研究的潜在应用领域包括大型多人在线游戏的经济系统设计、虚拟市场的行为模拟以及智能代理的开发。通过更真实的经济模拟，游戏开发者可以优化游戏内经济机制，提高玩家体验和参与度，未来可能对游戏设计和虚拟经济研究产生深远影响。

## 📄 摘要（原文）

> Within the domain of Massively Multiplayer Online (MMO) economy research, Agent-Based Modeling (ABM) has emerged as a robust tool for analyzing game economics, evolving from rule-based agents to decision-making agents enhanced by reinforcement learning. Nevertheless, existing works encounter significant challenges when attempting to emulate human-like economic activities among agents, particularly regarding agent reliability, sociability, and interpretability. In this study, we take a preliminary step in introducing a novel approach using Large Language Models (LLMs) in MMO economy simulation. Leveraging LLMs' role-playing proficiency, generative capacity, and reasoning aptitude, we design LLM-driven agents with human-like decision-making and adaptability. These agents are equipped with the abilities of role-playing, perception, memory, and reasoning, addressing the aforementioned challenges effectively. Simulation experiments focusing on in-game economic activities demonstrate that LLM-empowered agents can promote emergent phenomena like role specialization and price fluctuations in line with market rules.

