---
layout: default
title: Stackelberg Learning from Human Feedback: Preference Optimization as a Sequential Game
---

# Stackelberg Learning from Human Feedback: Preference Optimization as a Sequential Game

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16626" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16626v1</a>
  <a href="https://arxiv.org/pdf/2512.16626.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16626v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16626v1', 'Stackelberg Learning from Human Feedback: Preference Optimization as a Sequential Game')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Barna Pásztor, Thomas Kleine Buening, Andreas Krause

**分类**: cs.LG, cs.AI, cs.GT, cs.MA, stat.ML

**发布日期**: 2025-12-18

**备注**: 10 pages, 5 tables, 1 figures

---

## 💡 一句话要点

**提出Stackelberg Learning from Human Feedback (SLHF)框架，用于偏好优化。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机反馈` `偏好优化` `序贯博弈` `Stackelberg学习` `大型语言模型`

## 📋 核心要点

1. 现有RLHF方法为动作分配标量奖励，NLHF寻求同步博弈均衡，无法捕捉复杂偏好结构。
2. SLHF将对齐问题建模为领导者和跟随者之间的序贯博弈，利用序贯博弈的不对称性捕获更丰富的偏好结构。
3. 实验表明，SLHF在不同偏好数据集上实现了强大的对齐，并能进行跨模型迁移的推理时优化。

## 📝 摘要（中文）

本文提出了一种新的偏好优化框架：Stackelberg Learning from Human Feedback (SLHF)。SLHF将对齐问题建模为两个策略之间的序贯博弈：领导者(Leader)先采取行动，然后跟随者(Follower)根据领导者的行动做出响应。这种方法将偏好优化分解为跟随者的优化问题和领导者对抗性优化问题。与为动作分配标量奖励的Reinforcement Learning from Human Feedback (RLHF)或寻求同步博弈均衡的Nash Learning from Human Feedback (NLHF)不同，SLHF利用序贯博弈的不对称性来捕获更丰富的偏好结构。SLHF的序贯设计自然地实现了推理时优化，因为跟随者学习改进领导者的行动，并且这些改进可以通过迭代采样来利用。本文比较了SLHF、RLHF和NLHF的解概念，并阐述了SLHF在一致性、数据敏感性和对非传递偏好的鲁棒性方面的关键优势。在大型语言模型上的实验表明，SLHF在不同的偏好数据集上实现了强大的对齐，可以从0.5B扩展到8B参数，并产生可以在模型系列之间转移而无需进一步微调的推理时优化。

## 🔬 方法详解

**问题定义**：论文旨在解决如何更好地从人类反馈中学习，以对齐大型语言模型（LLM）的输出与人类偏好的问题。现有方法，如RLHF，通常将人类反馈转化为标量奖励，这可能过于简化，无法捕捉人类偏好的复杂性和细微差别。此外，NLHF方法假设策略同时行动，忽略了序贯决策的场景。

**核心思路**：SLHF的核心思路是将对齐问题建模为一个Stackelberg博弈，其中领导者（Leader）策略首先采取行动，然后跟随者（Follower）策略根据领导者的行动做出响应。这种序贯博弈的框架允许模型学习更丰富的偏好结构，因为跟随者可以根据领导者的行为进行优化和改进。

**技术框架**：SLHF的整体框架包含两个主要部分：跟随者策略的训练和领导者策略的优化。首先，通过人类反馈数据训练跟随者策略，使其能够根据领导者的行为给出偏好判断或进行改进。然后，领导者策略通过对抗性训练进行优化，目标是最大化跟随者策略的偏好。在推理阶段，跟随者策略可以进一步优化领导者的输出，从而提高最终结果的质量。

**关键创新**：SLHF的关键创新在于将对齐问题建模为序贯博弈，这与传统的RLHF和NLHF方法不同。这种建模方式允许模型学习更复杂的偏好结构，并实现推理时的优化。此外，SLHF在一致性、数据敏感性和对非传递偏好的鲁棒性方面具有优势。

**关键设计**：SLHF的关键设计包括跟随者策略的训练方式、领导者策略的优化目标以及推理时的优化策略。跟随者策略可以使用各种监督学习或强化学习方法进行训练，目标是准确预测人类偏好或改进领导者的输出。领导者策略的优化目标是最大化跟随者策略的偏好，可以使用对抗性训练或其他优化算法。推理时，跟随者策略可以迭代地优化领导者的输出，直到达到满意的结果。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16626v1/x1.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SLHF在多个偏好数据集上取得了优于RLHF和NLHF的性能。SLHF能够扩展到具有数十亿参数的大型语言模型，并且其推理时优化策略可以跨模型系列迁移，无需额外的微调。这些结果表明SLHF具有很强的泛化能力和实用价值。

## 🎯 应用场景

SLHF可应用于各种需要与人类偏好对齐的场景，例如对话系统、文本生成、图像生成和机器人控制。通过学习更丰富的偏好结构，SLHF可以生成更符合人类期望和价值观的输出，提高用户满意度和信任度。该方法还可用于个性化推荐系统，根据用户的历史行为和偏好，提供更精准的推荐结果。

## 📄 摘要（原文）

> We introduce Stackelberg Learning from Human Feedback (SLHF), a new framework for preference optimization. SLHF frames the alignment problem as a sequential-move game between two policies: a Leader, which commits to an action, and a Follower, which responds conditionally on the Leader's action. This approach decomposes preference optimization into a refinement problem for the Follower and an optimization problem against an adversary for the Leader. Unlike Reinforcement Learning from Human Feedback (RLHF), which assigns scalar rewards to actions, or Nash Learning from Human Feedback (NLHF), which seeks a simultaneous-move equilibrium, SLHF leverages the asymmetry of sequential play to capture richer preference structures. The sequential design of SLHF naturally enables inference-time refinement, as the Follower learns to improve the Leader's actions, and these refinements can be leveraged through iterative sampling. We compare the solution concepts of SLHF, RLHF, and NLHF, and lay out key advantages in consistency, data sensitivity, and robustness to intransitive preferences. Experiments on large language models demonstrate that SLHF achieves strong alignment across diverse preference datasets, scales from 0.5B to 8B parameters, and yields inference-time refinements that transfer across model families without further fine-tuning.

