---
layout: default
title: Pruning Long Chain-of-Thought of Large Reasoning Models via Small-Scale Preference Optimization
---

# Pruning Long Chain-of-Thought of Large Reasoning Models via Small-Scale Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10164" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10164v1</a>
  <a href="https://arxiv.org/pdf/2508.10164.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10164v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10164v1', 'Pruning Long Chain-of-Thought of Large Reasoning Models via Small-Scale Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bin Hong, Jiayu Liu, Zhenya Huang, Kai Zhang, Mengdi Zhang

**分类**: cs.AI

**发布日期**: 2025-08-13

**备注**: 19 pages, 5 figures

---

## 💡 一句话要点

**提出长度控制偏好优化以解决大规模推理模型的效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长链推理` `偏好优化` `计算效率` `大规模推理模型` `自然语言处理`

## 📋 核心要点

1. 现有大规模推理模型在处理复杂任务时，输出长度过长导致计算成本高且可能出现过度思考的问题。
2. 本文提出长度控制偏好优化（LCPO），通过分析生成路径和难度估计，有效减少生成长度并保持推理质量。
3. 实验结果显示，LCPO在多个基准上将平均输出长度减少超过50%，同时推理性能未受影响，展现出良好的效率提升。

## 📝 摘要（中文）

近年来，大规模推理模型（LRMs）在复杂任务中通过长链推理（CoT）展现出强大的性能。然而，冗长的输出增加了计算成本，并可能导致过度思考，平衡推理效果与效率面临挑战。现有的高效推理方法往往牺牲推理质量或需要大量资源。本文探讨了减少LRMs生成长度的有效方法，分析生成路径分布并通过难度估计过滤生成轨迹。基于对各种偏好优化方法在Bradley-Terry损失框架下收敛行为的分析，提出了长度控制偏好优化（LCPO），该方法能够在有限数据和训练下有效学习长度偏好。大量实验表明，该方法在多个基准上显著减少了平均输出长度超过50%，同时保持推理性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模推理模型在长链推理中输出冗长导致的计算成本高和推理效率低的问题。现有方法往往在提高效率时牺牲推理质量，或需要大量计算资源。

**核心思路**：论文提出的长度控制偏好优化（LCPO）通过分析生成路径的分布和难度估计，直接平衡与负对数似然（NLL）损失相关的隐含奖励，从而有效学习长度偏好。

**技术框架**：整体方法包括生成路径分析、难度估计、轨迹过滤和偏好优化四个主要模块。首先分析生成路径的分布，然后通过难度估计过滤不必要的轨迹，最后应用LCPO进行优化。

**关键创新**：LCPO是本研究的核心创新点，它通过在有限数据和训练下有效学习长度偏好，显著提高了推理效率，与现有方法相比，能够在不牺牲推理质量的情况下减少输出长度。

**关键设计**：在设计中，LCPO采用Bradley-Terry损失框架，结合生成路径的难度估计，优化过程中关注长度偏好的学习，确保在多个基准上实现了显著的性能提升。

## 📊 实验亮点

实验结果表明，采用LCPO方法后，平均输出长度在多个基准上减少超过50%，同时推理性能保持稳定，显示出该方法在提升效率方面的显著效果。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动文本生成等。通过提高大规模推理模型的效率，能够在资源受限的环境中实现更高效的推理，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Recent advances in Large Reasoning Models (LRMs) have demonstrated strong performance on complex tasks through long Chain-of-Thought (CoT) reasoning. However, their lengthy outputs increase computational costs and may lead to overthinking, raising challenges in balancing reasoning effectiveness and efficiency. Current methods for efficient reasoning often compromise reasoning quality or require extensive resources. This paper investigates efficient methods to reduce the generation length of LRMs. We analyze generation path distributions and filter generated trajectories through difficulty estimation. Subsequently, we analyze the convergence behaviors of the objectives of various preference optimization methods under a Bradley-Terry loss based framework. Based on the analysis, we propose Length Controlled Preference Optimization (LCPO) that directly balances the implicit reward related to NLL loss. LCPO can effectively learn length preference with limited data and training. Extensive experiments demonstrate that our approach significantly reduces the average output length by over 50\% across multiple benchmarks while maintaining the reasoning performance. Our work highlights the potential for computationally efficient approaches in guiding LRMs toward efficient reasoning.

