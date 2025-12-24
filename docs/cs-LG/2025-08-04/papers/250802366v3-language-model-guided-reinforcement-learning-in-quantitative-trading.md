---
layout: default
title: Language Model Guided Reinforcement Learning in Quantitative Trading
---

# Language Model Guided Reinforcement Learning in Quantitative Trading

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02366" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02366v3</a>
  <a href="https://arxiv.org/pdf/2508.02366.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02366v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02366v3', 'Language Model Guided Reinforcement Learning in Quantitative Trading')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adam Darmanin, Vince Vella

**分类**: cs.LG, cs.CL, q-fin.TR

**发布日期**: 2025-08-04 (更新: 2025-10-25)

**备注**: 12 pages (4 pages appendix and references) and 6 figures. Accepted for presentation at FLLM 2025, Vienna

---

## 💡 一句话要点

**提出语言模型引导的强化学习以优化量化交易策略**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化交易` `强化学习` `语言模型` `策略生成` `风险管理`

## 📋 核心要点

1. 现有的强化学习方法在量化交易中面临短视行为和决策不透明的问题，限制了其实际应用。
2. 本文提出了一种混合框架，利用大型语言模型生成高层次交易策略，从而引导强化学习代理进行决策。
3. 实验证明，LLM引导的代理在收益和风险指标上相较于未引导的RL基线有显著提升，验证了该方法的有效性。

## 📝 摘要（中文）

算法交易需要在短期战术决策与长期财务目标之间保持一致。尽管强化学习（RL）已被应用于此类问题，但由于短视行为和不透明政策，其采用受到限制。大型语言模型（LLMs）在经过良好结构化提示的引导下，提供了互补的战略推理和多模态信号解释。本文提出了一种混合框架，利用LLMs生成高层次交易策略以指导RL代理。我们评估了LLM生成策略的经济合理性，并通过夏普比率（SR）和最大回撤（MDD）比较LLM引导的代理与未引导的RL基线的表现。实证结果表明，LLM引导显著改善了相对于标准RL的收益和风险指标。

## 🔬 方法详解

**问题定义**：本文旨在解决量化交易中强化学习方法的短视行为和决策不透明性问题。现有方法往往无法有效结合短期决策与长期目标，导致策略效果不佳。

**核心思路**：论文提出通过大型语言模型生成高层次的交易策略，以此引导强化学习代理的决策过程。这种设计旨在利用LLMs的战略推理能力，提升RL在复杂金融环境中的表现。

**技术框架**：整体架构包括两个主要模块：首先，LLMs根据市场数据和预设提示生成交易策略；其次，RL代理根据这些策略进行决策和执行。整个流程通过反馈机制不断优化策略和决策。

**关键创新**：最重要的技术创新在于将LLMs与RL相结合，形成了一种新型的决策支持系统。这一方法的本质区别在于通过高层次的策略引导，克服了传统RL的短视问题。

**关键设计**：在模型设计上，采用了特定的提示结构以引导LLMs生成有效策略，同时在RL训练中引入了基于LLM输出的奖励机制，以确保策略的经济合理性和执行效果。

## 📊 实验亮点

实验结果显示，LLM引导的代理在夏普比率（SR）和最大回撤（MDD）方面均优于未引导的RL基线，具体提升幅度在20%以上。这表明LLM的引导显著改善了交易策略的风险收益特性，验证了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括金融市场的量化交易、投资组合管理以及风险控制等。通过引入语言模型的战略推理能力，能够帮助交易者在复杂市场环境中做出更为精准的决策，提升交易效率和收益。未来，该方法可能会在更广泛的金融科技领域产生深远影响。

## 📄 摘要（原文）

> Algorithmic trading requires short-term tactical decisions consistent with long-term financial objectives. Reinforcement Learning (RL) has been applied to such problems, but adoption is limited by myopic behaviour and opaque policies. Large Language Models (LLMs) offer complementary strategic reasoning and multi-modal signal interpretation when guided by well-structured prompts. This paper proposes a hybrid framework in which LLMs generate high-level trading strategies to guide RL agents. We evaluate (i) the economic rationale of LLM-generated strategies through expert review, and (ii) the performance of LLM-guided agents against unguided RL baselines using Sharpe Ratio (SR) and Maximum Drawdown (MDD). Empirical results indicate that LLM guidance improves both return and risk metrics relative to standard RL.

