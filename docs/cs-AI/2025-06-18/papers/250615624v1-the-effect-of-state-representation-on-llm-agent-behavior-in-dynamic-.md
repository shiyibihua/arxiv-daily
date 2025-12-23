---
layout: default
title: The Effect of State Representation on LLM Agent Behavior in Dynamic Routing Games
---

# The Effect of State Representation on LLM Agent Behavior in Dynamic Routing Games

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15624" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15624v1</a>
  <a href="https://arxiv.org/pdf/2506.15624.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15624v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15624v1', 'The Effect of State Representation on LLM Agent Behavior in Dynamic Routing Games')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lyle Goodyear, Rachel Guo, Ramesh Johari

**分类**: cs.AI

**发布日期**: 2025-06-18

**备注**: 27 pages, 20 figures

---

## 💡 一句话要点

**提出统一框架以优化LLM代理在动态路由游戏中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `动态路由游戏` `状态表示` `多智能体系统` `博弈论` `决策优化` `自然语言处理`

## 📋 核心要点

1. 现有方法在编码游戏历史时采用随意方式，导致状态表示对代理行为的影响不明确，且研究间的可比性受限。
2. 本文提出的框架通过三个维度系统性地描述状态表示方法，旨在优化LLM代理的决策过程。
3. 实验结果表明，特定的自然语言状态表示能够显著提高LLM代理的行为稳定性和与博弈论均衡的吻合度。

## 📝 摘要（中文）

大型语言模型（LLMs）在动态环境中的决策能力已展现出潜力，但其无状态特性要求构建自然语言的历史表示。本文提出一个统一框架，系统性地构建自然语言“状态”表示，以提示LLM代理在重复多智能体游戏中的行为。以动态自私路由游戏为例，研究发现自然语言状态表示对LLM代理行为有显著影响，尤其是总结性表示、关于遗憾的信息以及对他人行为的有限信息能够更好地匹配博弈论均衡预测，并提高游戏的稳定性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM代理在动态游戏中由于状态表示不当而导致的决策不稳定和不一致问题。现有方法缺乏系统性，无法有效比较不同状态表示的影响。

**核心思路**：提出一个统一框架，通过分析状态表示的行动信息量、奖励信息量和提示风格，系统构建自然语言状态表示，以提高LLM代理的决策能力。

**技术框架**：框架包括三个主要模块：1) 行动信息量评估；2) 奖励信息量评估；3) 提示风格优化。每个模块通过不同的自然语言表示方式来影响代理的决策过程。

**关键创新**：最重要的创新在于系统性地将状态表示的影响分解为多个维度，明确了不同表示方式对LLM代理行为的具体影响，填补了以往研究的空白。

**关键设计**：在实验中，采用了总结性而非完整的历史表示，关注遗憾而非原始收益，并限制对他人行为的信息，从而优化了代理的决策过程。

## 📊 实验亮点

实验结果显示，使用总结性自然语言表示的LLM代理在动态自私路由游戏中，其行为更接近博弈论均衡预测，且游戏过程更为稳定。相比于其他表示方式，表现出更小的均衡偏差和更低的动态变化幅度。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、网络流量管理和多智能体协作等。通过优化LLM代理的决策能力，可以提高这些系统的效率和稳定性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown promise as decision-makers in dynamic settings, but their stateless nature necessitates creating a natural language representation of history. We present a unifying framework for systematically constructing natural language "state" representations for prompting LLM agents in repeated multi-agent games. Previous work on games with LLM agents has taken an ad hoc approach to encoding game history, which not only obscures the impact of state representation on agents' behavior, but also limits comparability between studies. Our framework addresses these gaps by characterizing methods of state representation along three axes: action informativeness (i.e., the extent to which the state representation captures actions played); reward informativeness (i.e., the extent to which the state representation describes rewards obtained); and prompting style (or natural language compression, i.e., the extent to which the full text history is summarized).
>   We apply this framework to a dynamic selfish routing game, chosen because it admits a simple equilibrium both in theory and in human subject experiments \cite{rapoport_choice_2009}. Despite the game's relative simplicity, we find that there are key dependencies of LLM agent behavior on the natural language state representation. In particular, we observe that representations which provide agents with (1) summarized, rather than complete, natural language representations of past history; (2) information about regrets, rather than raw payoffs; and (3) limited information about others' actions lead to behavior that more closely matches game theoretic equilibrium predictions, and with more stable game play by the agents. By contrast, other representations can exhibit either large deviations from equilibrium, higher variation in dynamic game play over time, or both.

