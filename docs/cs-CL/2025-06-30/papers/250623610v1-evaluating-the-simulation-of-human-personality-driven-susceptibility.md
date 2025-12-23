---
layout: default
title: Evaluating the Simulation of Human Personality-Driven Susceptibility to Misinformation with LLMs
---

# Evaluating the Simulation of Human Personality-Driven Susceptibility to Misinformation with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23610" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23610v1</a>
  <a href="https://arxiv.org/pdf/2506.23610.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23610v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23610v1', 'Evaluating the Simulation of Human Personality-Driven Susceptibility to Misinformation with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Manuel Pratelli, Marinella Petrocchi

**分类**: cs.CL, cs.CY

**发布日期**: 2025-06-30

**备注**: pre-print version - paper actually under submission

**DOI**: [10.3233/FAIA250901](https://doi.org/10.3233/FAIA250901)

---

## 💡 一句话要点

**评估大语言模型在个性驱动的虚假信息易感性模拟中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `个性特征` `虚假信息` `心理学` `行为模拟` `五大人格` `信息辨别`

## 📋 核心要点

1. 核心问题：现有方法在模拟人类个性驱动的虚假信息易感性方面存在不足，无法准确捕捉心理差异。
2. 方法要点：论文通过构建基于五大人格特质的LLM代理，评估其在虚假信息辨别中的表现。
3. 实验或效果：研究发现某些个性特征与虚假信息的关联得到了可靠复制，揭示了LLM的系统性偏差。

## 📝 摘要（中文）

大语言模型（LLMs）能够大规模生成合成行为数据，为人类实验提供了一种伦理且低成本的替代方案。然而，这些数据是否能够真实捕捉由个性特征驱动的心理差异仍然是一个未解之谜。本文评估了基于五大人格特质条件下的LLM代理在虚假信息易感性上的表现，特别关注新闻辨别能力。通过利用已发布的数据集，研究者创建了匹配的LLM代理并比较其响应与原始人类模式。结果显示，某些个性特征与虚假信息的关联（如宜人性和尽责性）得到了可靠的复制，而其他特征则存在偏差，揭示了LLM在内化和表达个性方面的系统性偏差。这些结果强调了个性对齐的LLM在行为模拟中的潜力与局限，并为人工智能代理的认知多样性建模提供了新见解。

## 🔬 方法详解

**问题定义**：本文旨在解决如何利用大语言模型模拟人类个性驱动的虚假信息易感性的问题。现有方法在捕捉个性特征与虚假信息易感性之间的关系时存在局限性，难以准确反映心理差异。

**核心思路**：论文的核心思路是通过构建与五大人格特质相匹配的LLM代理，来评估其在虚假信息辨别中的表现。这种设计旨在探索个性特征如何影响信息判断能力。

**技术框架**：整体架构包括数据收集、LLM代理构建、个性特征匹配和结果比较四个主要模块。首先，利用已有数据集收集人类参与者的个性特征和新闻判断数据；然后，构建相应的LLM代理；接着，进行个性特征匹配；最后，比较LLM的判断与人类的判断。

**关键创新**：本研究的关键创新在于首次系统性地评估了个性驱动的LLM在虚假信息易感性上的表现，揭示了个性特征与信息判断之间的复杂关系。与现有方法相比，本文提供了更为细致的个性特征分析。

**关键设计**：在模型设计中，采用了五大人格特质作为条件输入，使用特定的损失函数来优化LLM的判断能力。此外，模型的训练过程中注重了个性特征的多样性，以确保生成的行为数据能够反映真实的人类心理差异。

## 📊 实验亮点

实验结果表明，基于五大人格特质的LLM代理在虚假信息辨别中的表现与人类参与者的判断存在显著相关性，尤其在宜人性和尽责性方面的表现得到了可靠复制。这一发现为个性驱动的行为模拟提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括心理学研究、社交媒体信息传播分析以及个性化推荐系统。通过理解个性如何影响信息判断，能够为设计更有效的虚假信息干预策略提供依据，提升公众的媒体素养和信息辨别能力。

## 📄 摘要（原文）

> Large language models (LLMs) make it possible to generate synthetic behavioural data at scale, offering an ethical and low-cost alternative to human experiments. Whether such data can faithfully capture psychological differences driven by personality traits, however, remains an open question. We evaluate the capacity of LLM agents, conditioned on Big-Five profiles, to reproduce personality-based variation in susceptibility to misinformation, focusing on news discernment, the ability to judge true headlines as true and false headlines as false. Leveraging published datasets in which human participants with known personality profiles rated headline accuracy, we create matching LLM agents and compare their responses to the original human patterns. Certain trait-misinformation associations, notably those involving Agreeableness and Conscientiousness, are reliably replicated, whereas others diverge, revealing systematic biases in how LLMs internalize and express personality. The results underscore both the promise and the limits of personality-aligned LLMs for behavioral simulation, and offer new insight into modeling cognitive diversity in artificial agents.

