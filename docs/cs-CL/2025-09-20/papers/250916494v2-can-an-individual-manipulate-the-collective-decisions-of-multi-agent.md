---
layout: default
title: Can an Individual Manipulate the Collective Decisions of Multi-Agents?
---

# Can an Individual Manipulate the Collective Decisions of Multi-Agents?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16494" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16494v2</a>
  <a href="https://arxiv.org/pdf/2509.16494.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16494v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16494v2', 'Can an Individual Manipulate the Collective Decisions of Multi-Agents?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fengyuan Liu, Rui Zhao, Shuo Chen, Guohao Li, Philip Torr, Lei Han, Jindong Gu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-20 (更新: 2025-10-15)

---

## 💡 一句话要点

**M-Spoiler：利用单智能体知识攻击多智能体协同决策系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `对抗攻击` `不完全信息博弈` `大型语言模型` `协同决策`

## 📋 核心要点

1. 现有研究表明，协同的多智能体系统在决策和推理方面表现出更强的能力，但同时也继承了单个LLM的脆弱性。
2. 论文提出M-Spoiler框架，通过模拟智能体交互生成对抗样本，利用单个智能体的知识来操纵多智能体系统的集体决策。
3. 实验证明，即使只了解一个智能体，攻击者也能有效误导整个系统，表明多智能体系统存在潜在的安全风险。

## 📝 摘要（中文）

本文研究了在多智能体系统中，攻击者仅了解单个智能体的情况下，是否能够生成对抗样本来误导整个系统的协同决策。作者将此问题建模为一个不完全信息博弈，并提出了名为M-Spoiler的框架，该框架通过模拟多智能体系统中的智能体交互来生成对抗样本。M-Spoiler引入了一个顽固智能体，通过模拟目标系统中智能体的潜在顽固反应，来辅助优化对抗样本，从而提高误导系统的有效性。实验结果表明，了解单个智能体的信息确实会对多智能体系统构成风险，并且M-Spoiler框架能够有效地误导系统。此外，论文还探讨了几种防御机制，结果表明M-Spoiler的攻击能力仍然优于基线方法，突显了进一步研究防御策略的必要性。

## 🔬 方法详解

**问题定义**：论文旨在解决多智能体系统中，攻击者仅了解其中一个智能体的信息，能否通过构造对抗样本来影响整个系统的决策。现有方法难以应对这种不完全信息下的攻击，因为它们通常需要访问所有智能体的信息或者假设智能体行为是固定的。

**核心思路**：核心思路是将攻击问题建模为不完全信息博弈，攻击者通过模拟目标系统的行为来生成对抗样本。关键在于模拟其他智能体的潜在反应，从而使生成的对抗样本更具鲁棒性，能够成功误导目标智能体，进而影响整个系统的决策。

**技术框架**：M-Spoiler框架包含以下几个主要模块：1) **目标系统模拟**：模拟多智能体系统的交互过程，包括智能体的角色、目标和通信方式。2) **顽固智能体**：引入一个特殊的智能体，模拟目标系统中其他智能体的顽固反应，用于优化对抗样本。3) **对抗样本生成**：利用目标系统模拟和顽固智能体的反馈，生成能够误导目标智能体的对抗样本。4) **攻击执行**：将生成的对抗样本注入到目标智能体中，观察其对系统决策的影响。

**关键创新**：M-Spoiler的关键创新在于引入了“顽固智能体”的概念，通过模拟目标系统中其他智能体的潜在反应，来增强对抗样本的鲁棒性。这使得即使攻击者只了解一个智能体的信息，也能有效地误导整个系统。与现有方法相比，M-Spoiler不需要访问所有智能体的信息，并且能够适应智能体行为的变化。

**关键设计**：顽固智能体的设计是关键。它通过学习目标系统中其他智能体的行为模式，模拟它们在面对对抗样本时的反应。具体实现上，可以使用强化学习或者模仿学习等方法来训练顽固智能体。对抗样本的生成可以使用梯度下降等优化算法，目标是最大化目标智能体被误导的概率，同时最小化对抗样本的扰动幅度。

## 📊 实验亮点

实验结果表明，M-Spoiler框架能够有效地误导多智能体系统，即使攻击者只了解一个智能体的信息。在各种任务中，M-Spoiler的攻击成功率显著高于基线方法，并且在面对防御机制时仍然表现出较强的攻击能力。这表明M-Spoiler框架具有很强的实用性和威胁性，突显了多智能体系统安全研究的重要性。

## 🎯 应用场景

该研究成果可应用于提升多智能体系统的安全性，例如在自动驾驶、金融交易、医疗诊断等领域，多智能体协同决策被广泛应用。通过研究针对多智能体系统的攻击方法，可以帮助开发者更好地理解系统的安全风险，并开发更有效的防御机制，从而保障系统的可靠性和安全性。未来的研究可以探索更复杂的攻击场景和更有效的防御策略。

## 📄 摘要（原文）

> Individual Large Language Models (LLMs) have demonstrated significant capabilities across various domains, such as healthcare and law. Recent studies also show that coordinated multi-agent systems exhibit enhanced decision-making and reasoning abilities through collaboration. However, due to the vulnerabilities of individual LLMs and the difficulty of accessing all agents in a multi-agent system, a key question arises: If attackers only know one agent, could they still generate adversarial samples capable of misleading the collective decision? To explore this question, we formulate it as a game with incomplete information, where attackers know only one target agent and lack knowledge of the other agents in the system. With this formulation, we propose M-Spoiler, a framework that simulates agent interactions within a multi-agent system to generate adversarial samples. These samples are then used to manipulate the target agent in the target system, misleading the system's collaborative decision-making process. More specifically, M-Spoiler introduces a stubborn agent that actively aids in optimizing adversarial samples by simulating potential stubborn responses from agents in the target system. This enhances the effectiveness of the generated adversarial samples in misleading the system. Through extensive experiments across various tasks, our findings confirm the risks posed by the knowledge of an individual agent in multi-agent systems and demonstrate the effectiveness of our framework. We also explore several defense mechanisms, showing that our proposed attack framework remains more potent than baselines, underscoring the need for further research into defensive strategies.

