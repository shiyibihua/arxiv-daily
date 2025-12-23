---
layout: default
title: Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms
---

# Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09457" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09457v2</a>
  <a href="https://arxiv.org/pdf/2506.09457.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09457v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09457v2', 'Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeguan Xiao, Yun Chen, Guanhua Chen, Ke Tang

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-11 (更新: 2025-08-22)

---

## 💡 一句话要点

**提出POET以解决直接对齐算法中的奖励生成差距问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `直接对齐算法` `奖励生成` `前缀导向训练` `自然语言处理` `生成模型`

## 📋 核心要点

1. 现有的直接对齐算法在训练优化目标与推理生成性能之间存在奖励生成差距，影响了模型的实际表现。
2. 论文提出了前缀导向等长训练（POET）方法，通过截断响应长度来解决奖励生成差距问题，增强了对前缀标记的关注。
3. 实验结果显示，POET在DPO和SimPO的标准实现上均有显著提升，特别是在AlpacaEval 2中提高了15.6分。

## 📝 摘要（中文）

直接对齐算法（DAAs），如直接偏好优化（DPO）和简单偏好优化（SimPO），作为对人类反馈强化学习（RLHF）算法的高效替代方案，面临奖励生成差距的根本限制。本文识别了这一差距的原因，主要是前缀标记在生成过程中的重要性与DAAs隐含奖励函数之间的错位。为此，本文提出了一种名为前缀导向等长训练（POET）的方法，通过将偏好和不偏好的响应截断为相同长度，优化DAAs的目标，使其在训练过程中更关注前缀标记。实验结果表明，POET在AlpacaEval 2中提升了多达15.6分，并在下游任务中整体改善了性能。

## 🔬 方法详解

**问题定义**：本文解决的具体问题是直接对齐算法（DAAs）在训练和推理阶段之间的奖励生成差距，导致模型生成的响应与人类偏好不一致。现有方法未能有效考虑前缀标记的重要性，造成优化目标与生成性能的错位。

**核心思路**：论文的核心解决思路是采用前缀导向等长训练（POET），通过将偏好和不偏好的响应截断为相同长度，确保优化过程更关注前缀标记，从而缩小奖励生成差距。

**技术框架**：整体架构包括两个主要阶段：首先，收集包含偏好和不偏好响应的训练样本；其次，在训练过程中将这些响应截断为相同长度，以便在优化过程中保持一致性。

**关键创新**：最重要的技术创新点在于引入了前缀导向的训练策略，使得DAAs在优化过程中能够更有效地对前缀标记进行建模，与传统方法相比，显著提高了生成性能。

**关键设计**：在关键设计上，POET方法通过动态截断响应长度来实现多样化的训练样本长度，确保优化目标在所有时间步上收敛，并在损失函数中强调前缀标记的重要性。

## 📊 实验亮点

实验结果显示，POET在AlpacaEval 2中提升了多达15.6分，相较于DPO和SimPO的标准实现，整体性能在多个下游任务中均有显著改善，验证了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的对话系统、文本生成和人机交互等场景。通过改善模型对人类偏好的对齐能力，POET方法能够提升生成模型在实际应用中的表现，增强用户体验，推动智能助手和自动化系统的发展。

## 📄 摘要（原文）

> Direct Alignment Algorithms (DAAs), such as Direct Preference Optimization (DPO) and Simple Preference Optimization (SimPO), have emerged as efficient alternatives to Reinforcement Learning from Human Feedback (RLHF) algorithms for aligning large language models (LLMs) with human preferences. However, DAAs suffer from a fundamental limitation we identify as the "reward-generation gap" -- a misalignment between optimization objectives during training and actual generation performance during inference. In this paper, we find a contributor to the reward-generation gap is the mismatch between the inherent importance of prefix tokens during the LLM generation process and how this importance is reflected in the implicit reward functions of DAAs. To bridge the gap, we adopt a token-level MDP perspective of DAAs to analyze its limitations and introduce a simple yet effective approach called Prefix-Oriented Equal-length Training (POET), which truncates both preferred and dispreferred responses to match the shorter one's length. Training with \mname, where both responses in each sample are truncated to equal length, resulting in diverse truncated lengths across samples, the optimization of DAAs objective is implicitly constrained to converge across all timesteps of token-level MDP, thus paying more attention to prefix tokens than the standard DAAs. We conduct experiments with DPO and SimPO, two representative DAAs, demonstrating that POET improves over their standard implementations, achieving up to 15.6 points in AlpacaEval 2 and overall improvements across downstream tasks. Our results highlight the importance of addressing the misalignment between reward optimization and generation performance in DAAs.

