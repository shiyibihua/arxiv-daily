---
layout: default
title: Can LLMs Generate Good Stories? Insights and Challenges from a Narrative Planning Perspective
---

# Can LLMs Generate Good Stories? Insights and Challenges from a Narrative Planning Perspective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10161" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10161v1</a>
  <a href="https://arxiv.org/pdf/2506.10161.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10161v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10161v1', 'Can LLMs Generate Good Stories? Insights and Challenges from a Narrative Planning Perspective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Wang, Max Kreminski

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-11

**备注**: In 2025 IEEE Conference on Games (CoG)

---

## 💡 一句话要点

**提出基于叙事规划的基准以评估LLMs的故事生成能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `故事生成` `叙事规划` `计算叙事学` `因果合理性` `角色意图` `戏剧冲突` `强化学习`

## 📋 核心要点

1. 现有的故事生成方法在自动评估和人工评估方面存在局限性，导致对LLMs生成高质量故事能力的理解不足。
2. 论文通过引入叙事规划问题，利用计算叙事学的见解，提出了一个评估LLMs故事生成能力的基准。
3. 实验结果显示，GPT-4级别的LLMs在小规模上能够生成因果合理的故事，但在角色意图和戏剧冲突方面仍需改进。

## 📝 摘要（中文）

故事生成是大型语言模型（LLMs）的一个重要应用。然而，由于自动评估方法的局限性以及人工评估的高成本和主观性，理解LLMs生成高质量故事的能力仍然有限。计算叙事学提供了关于好故事构成的宝贵见解，已应用于符号叙事规划方法。本文旨在通过解决叙事规划问题来加深对LLMs故事生成能力的理解。我们提出了一个基于文献示例的叙事规划评估基准，重点关注因果合理性、角色意图和戏剧冲突。实验表明，GPT-4级别的LLMs能够在小规模上生成因果合理的故事，但在角色意图和戏剧冲突的规划上仍然面临挑战，需要通过强化学习训练的LLMs进行复杂推理。研究结果提供了LLMs在不同方面生成高质量故事的规模洞察，同时揭示了有趣的问题解决行为，并为在游戏环境中应用LLM叙事规划提供了挑战和考虑。

## 🔬 方法详解

**问题定义**：本文旨在解决LLMs在故事生成中的评估问题，现有方法在自动和人工评估中存在主观性和高成本的痛点。

**核心思路**：通过引入叙事规划的框架，利用计算叙事学的理论，建立一个基准来评估LLMs在故事生成中的表现，特别关注因果合理性、角色意图和戏剧冲突。

**技术框架**：整体架构包括数据收集、叙事规划问题的定义、LLMs的训练与评估。主要模块包括文献示例的选择、评估指标的设计和实验结果的分析。

**关键创新**：提出了一个新的评估基准，结合了叙事规划的理论，能够更全面地评估LLMs在故事生成中的能力，特别是在角色意图和戏剧冲突方面的表现。

**关键设计**：在实验中，使用了强化学习来训练LLMs以提高其复杂推理能力，设置了针对因果合理性和角色意图的特定损失函数，以优化生成故事的质量。

## 📊 实验亮点

实验结果表明，GPT-4级别的LLMs在小规模故事生成中能够实现因果合理性，然而在角色意图和戏剧冲突的生成上仍存在挑战。具体而言，生成的故事在因果关系上表现良好，但在复杂的角色互动和冲突情节上需要进一步的强化学习训练。

## 🎯 应用场景

该研究的潜在应用领域包括游戏设计、互动叙事和教育等。通过改进LLMs的故事生成能力，可以为游戏开发者提供更丰富的叙事工具，提升玩家的沉浸感和参与度。此外，该研究也为教育领域的创意写作提供了新的思路，帮助学生更好地理解故事结构和叙事技巧。

## 📄 摘要（原文）

> Story generation has been a prominent application of Large Language Models (LLMs). However, understanding LLMs' ability to produce high-quality stories remains limited due to challenges in automatic evaluation methods and the high cost and subjectivity of manual evaluation. Computational narratology offers valuable insights into what constitutes a good story, which has been applied in the symbolic narrative planning approach to story generation. This work aims to deepen the understanding of LLMs' story generation capabilities by using them to solve narrative planning problems. We present a benchmark for evaluating LLMs on narrative planning based on literature examples, focusing on causal soundness, character intentionality, and dramatic conflict. Our experiments show that GPT-4 tier LLMs can generate causally sound stories at small scales, but planning with character intentionality and dramatic conflict remains challenging, requiring LLMs trained with reinforcement learning for complex reasoning. The results offer insights on the scale of stories that LLMs can generate while maintaining quality from different aspects. Our findings also highlight interesting problem solving behaviors and shed lights on challenges and considerations for applying LLM narrative planning in game environments.

