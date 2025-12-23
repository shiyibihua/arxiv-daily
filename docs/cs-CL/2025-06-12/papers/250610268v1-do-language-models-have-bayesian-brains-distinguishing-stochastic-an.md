---
layout: default
title: Do Language Models Have Bayesian Brains? Distinguishing Stochastic and Deterministic Decision Patterns within Large Language Models
---

# Do Language Models Have Bayesian Brains? Distinguishing Stochastic and Deterministic Decision Patterns within Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10268" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10268v1</a>
  <a href="https://arxiv.org/pdf/2506.10268.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10268v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10268v1', 'Do Language Models Have Bayesian Brains? Distinguishing Stochastic and Deterministic Decision Patterns within Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrea Yaoyun Cui, Pengfei Yu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出区分语言模型决策模式的方法以解决贝叶斯推断问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `贝叶斯推断` `决策模式` `吉布斯采样` `概率分布` `自然语言处理` `机器学习`

## 📋 核心要点

1. 现有研究假设语言模型进行随机决策，但实际表现可能近乎确定性，挑战了这一假设。
2. 论文提出了一种新方法，通过区分随机与确定性决策模式，解决了误导性先验推断的问题。
3. 实验表明，语言模型在不同条件下的决策模式具有显著差异，为理解其决策机制提供了新视角。

## 📝 摘要（中文）

语言模型本质上是对标记序列的概率分布。自回归模型通过迭代计算和从下一个标记的分布中采样生成句子。这种迭代采样引入了随机性，使得语言模型被认为是进行概率决策。本文探讨了一个关键问题：语言模型是否具备贝叶斯思维？研究发现，在特定条件下，语言模型可以表现出近乎确定性的决策行为，挑战了随机采样的假设。我们提出了一种简单的方法来区分吉布斯采样中的随机和确定性决策模式，以防止误导性的语言模型先验推断。实验结果为理解大型语言模型的决策提供了重要见解。

## 🔬 方法详解

**问题定义**：本文旨在解决语言模型在决策过程中是否具备贝叶斯思维的问题。现有方法假设语言模型进行随机决策，但实际可能存在确定性决策，导致先验推断的误导。

**核心思路**：论文的核心思路是通过区分吉布斯采样中的随机与确定性决策模式，重新审视语言模型的决策行为，从而避免误导性先验的推断。

**技术框架**：整体架构包括对语言模型的决策模式进行分类，采用实验方法验证不同条件下的决策行为，主要模块包括数据采集、模型训练和决策模式分析。

**关键创新**：最重要的技术创新点在于提出了一种新的方法来区分随机和确定性决策模式，这与现有方法的随机假设本质上不同。

**关键设计**：在实验中，设置了不同的采样温度和决策条件，使用了最大似然估计等技术细节，以确保对决策模式的准确分析。

## 📊 实验亮点

实验结果显示，在特定条件下，语言模型能够表现出近乎确定性的决策行为，挑战了传统的随机决策假设。通过新方法，成功区分了不同决策模式，为理解语言模型提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和机器翻译等。通过更好地理解语言模型的决策机制，可以提升模型的可靠性和准确性，进而推动智能系统的实际应用和发展。

## 📄 摘要（原文）

> Language models are essentially probability distributions over token sequences. Auto-regressive models generate sentences by iteratively computing and sampling from the distribution of the next token. This iterative sampling introduces stochasticity, leading to the assumption that language models make probabilistic decisions, similar to sampling from unknown distributions. Building on this assumption, prior research has used simulated Gibbs sampling, inspired by experiments designed to elicit human priors, to infer the priors of language models. In this paper, we revisit a critical question: Do language models possess Bayesian brains? Our findings show that under certain conditions, language models can exhibit near-deterministic decision-making, such as producing maximum likelihood estimations, even with a non-zero sampling temperature. This challenges the sampling assumption and undermines previous methods for eliciting human-like priors. Furthermore, we demonstrate that without proper scrutiny, a system with deterministic behavior undergoing simulated Gibbs sampling can converge to a "false prior." To address this, we propose a straightforward approach to distinguish between stochastic and deterministic decision patterns in Gibbs sampling, helping to prevent the inference of misleading language model priors. We experiment on a variety of large language models to identify their decision patterns under various circumstances. Our results provide key insights in understanding decision making of large language models.

