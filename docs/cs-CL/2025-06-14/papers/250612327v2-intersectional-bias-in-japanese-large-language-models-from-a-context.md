---
layout: default
title: Intersectional Bias in Japanese Large Language Models from a Contextualized Perspective
---

# Intersectional Bias in Japanese Large Language Models from a Contextualized Perspective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12327" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12327v2</a>
  <a href="https://arxiv.org/pdf/2506.12327.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12327v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12327v2', 'Intersectional Bias in Japanese Large Language Models from a Contextualized Perspective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hitomi Yanaka, Xinqi He, Jie Lu, Namgi Han, Sunjin Oh, Ryoma Kumon, Yuma Matsuoka, Katsuhiko Watabe, Yuko Itatsu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-14 (更新: 2025-07-27)

**备注**: Accepted to the 6th Workshop on Gender Bias in Natural Language Processing (GeBNLP2025) at ACL2025

---

## 💡 一句话要点

**构建日本基准数据集以评估大型语言模型的交叉偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `交叉偏见` `社会属性` `数据集构建` `自然语言处理` `模型评估`

## 📋 核心要点

1. 现有研究多集中于单一社会属性的偏见，忽视了交叉性偏见的复杂性和多样性。
2. 本研究提出了inter-JBBQ基准数据集，专门用于评估大型语言模型的交叉偏见，提供了新的评估框架。
3. 实验结果显示，GPT-4o和Swallow在不同上下文中表现出不同的偏见输出，揭示了交叉偏见的存在和影响。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的快速发展，社会偏见的研究逐渐增多。大多数研究集中于单一社会属性的偏见，而社会科学研究表明，社会偏见往往以交叉性形式出现。本研究构建了日本基准数据集inter-JBBQ，旨在评估LLMs在问答场景中的交叉偏见。通过对GPT-4o和Swallow的分析，我们发现即使在社会属性组合相同的情况下，偏见输出也会因上下文而异。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在问答场景中存在的交叉偏见评估问题。现有方法多关注单一属性，未能全面反映偏见的复杂性。

**核心思路**：通过构建inter-JBBQ数据集，论文提供了一种新的评估框架，能够同时考虑多个社会属性的交叉影响，从而更全面地分析模型的偏见表现。

**技术框架**：研究首先设计了inter-JBBQ数据集，包含多种社会属性的组合。然后，使用该数据集对GPT-4o和Swallow进行评估，分析其在不同上下文下的输出偏见。

**关键创新**：最重要的创新在于提出了交叉偏见的评估框架，强调了上下文对偏见输出的影响，这与传统的单一属性偏见评估方法有本质区别。

**关键设计**：在数据集构建过程中，精心设计了社会属性的组合和上下文场景，以确保评估的全面性和有效性。

## 📊 实验亮点

实验结果表明，GPT-4o和Swallow在不同上下文中表现出显著的偏见差异，揭示了交叉偏见的复杂性。具体而言，模型在相同社会属性组合下的输出偏见变化，显示出上下文对偏见的影响程度。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、社会科学研究及人工智能伦理等。通过更全面地理解和评估模型的偏见，能够为模型的改进和社会责任提供指导，促进更公平的AI系统发展。

## 📄 摘要（原文）

> An increasing number of studies have examined the social bias of rapidly developed large language models (LLMs). Although most of these studies have focused on bias occurring in a single social attribute, research in social science has shown that social bias often occurs in the form of intersectionality -- the constitutive and contextualized perspective on bias aroused by social attributes. In this study, we construct the Japanese benchmark inter-JBBQ, designed to evaluate the intersectional bias in LLMs on the question-answering setting. Using inter-JBBQ to analyze GPT-4o and Swallow, we find that biased output varies according to its contexts even with the equal combination of social attributes.

