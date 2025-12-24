---
layout: default
title: Large Language Models are Highly Aligned with Human Ratings of Emotional Stimuli
---

# Large Language Models are Highly Aligned with Human Ratings of Emotional Stimuli

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14214" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14214v1</a>
  <a href="https://arxiv.org/pdf/2508.14214.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14214v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14214v1', 'Large Language Models are Highly Aligned with Human Ratings of Emotional Stimuli')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mattson Ogg, Chace Ashcraft, Ritwik Bose, Raphael Norman-Tenazas, Michael Wolmetz

**分类**: cs.AI

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**探讨大型语言模型与人类情感评估的高度一致性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感计算` `大型语言模型` `人机交互` `情感评估` `多模态学习`

## 📋 核心要点

1. 现有方法对大型语言模型在情感评估中的一致性缺乏深入研究，尤其是在高压情境下的表现。
2. 论文通过对多种流行LLMs进行情感评分，探讨其与人类情感评估的一致性，尤其关注快乐、愤怒、悲伤等情感类别。
3. 实验结果表明，GPT-4o在情感评分任务中与人类评分高度一致，尤其在快乐情感的评估中，相关性达到0.9以上。

## 📝 摘要（中文）

情感对人类行为和认知有着深远的影响，尤其在日常和高压任务中。本文研究了大型语言模型（LLMs）如何评估情感刺激，特别是它们与人类在情感内容评估上的一致性。通过对多种流行LLMs进行情感评分，发现GPT-4o在多个模态和刺激上与人类参与者的评分高度一致，尤其在快乐情感的评估中表现最佳。研究结果为理解LLMs在情感交互中的有效性提供了重要依据。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在情感刺激评估中的一致性问题，现有方法未能充分探讨LLMs在情感交互中的有效性与局限性。

**核心思路**：通过对多种流行LLMs进行情感评分，与人类评分进行对比，分析其在不同情感类别中的一致性，特别是快乐、愤怒、悲伤等情感的评估。

**技术框架**：研究采用了多模态数据集，包括词汇和图像，分别由人类和LLMs进行情感评分，构建了一个对比分析框架。

**关键创新**：本研究的创新在于系统性地评估LLMs与人类在情感评分上的一致性，尤其是在五类情感框架下的表现，提供了新的视角。

**关键设计**：实验中使用了多种评分标准，特别关注愤怒、悲伤、恐惧、厌恶和快乐五类情感的评估，设计了相应的评分机制以确保数据的可靠性。

## 📊 实验亮点

实验结果显示，GPT-4o在情感评分任务中与人类评分的相关性高达0.9，尤其在快乐情感的评估中表现最佳。同时，LLMs的评分一致性明显高于人类评分，揭示了其在情感理解中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括情感计算、心理健康监测和人机交互等。通过理解LLMs在情感评估中的表现，可以更好地将其应用于需要情感理解的场景，如客服机器人和社交媒体分析，提升用户体验和交互质量。

## 📄 摘要（原文）

> Emotions exert an immense influence over human behavior and cognition in both commonplace and high-stress tasks. Discussions of whether or how to integrate large language models (LLMs) into everyday life (e.g., acting as proxies for, or interacting with, human agents), should be informed by an understanding of how these tools evaluate emotionally loaded stimuli or situations. A model's alignment with human behavior in these cases can inform the effectiveness of LLMs for certain roles or interactions. To help build this understanding, we elicited ratings from multiple popular LLMs for datasets of words and images that were previously rated for their emotional content by humans. We found that when performing the same rating tasks, GPT-4o responded very similarly to human participants across modalities, stimuli and most rating scales (r = 0.9 or higher in many cases). However, arousal ratings were less well aligned between human and LLM raters, while happiness ratings were most highly aligned. Overall LLMs aligned better within a five-category (happiness, anger, sadness, fear, disgust) emotion framework than within a two-dimensional (arousal and valence) organization. Finally, LLM ratings were substantially more homogenous than human ratings. Together these results begin to describe how LLM agents interpret emotional stimuli and highlight similarities and differences among biological and artificial intelligence in key behavioral domains.

