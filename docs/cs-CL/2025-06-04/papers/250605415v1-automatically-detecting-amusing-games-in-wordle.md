---
layout: default
title: Automatically Detecting Amusing Games in Wordle
---

# Automatically Detecting Amusing Games in Wordle

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05415" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05415v1</a>
  <a href="https://arxiv.org/pdf/2506.05415.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05415v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05415v1', 'Automatically Detecting Amusing Games in Wordle')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ronaldo Luo, Gary Liang, Cindy Liu, Adam Kabbara, Minahil Bakhtawar, Kina Kim, Michael Guerzhoy

**分类**: cs.CL

**发布日期**: 2025-06-04

**备注**: Accepted to the Intenational Conference on Computational Creeativity (ICCC) 2025

---

## 💡 一句话要点

**提出自动化预测Wordle游戏趣味性的模型**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `Wordle游戏` `趣味性预测` `用户反应分析` `GPT-3.5` `特征提取` `社交媒体` `自动化模型`

## 📋 核心要点

1. 核心问题：现有方法在预测用户对Wordle游戏趣味性方面存在不足，缺乏有效的特征提取与分析手段。
2. 方法要点：论文通过GPT-3.5对用户反应进行分类，并提取相关特征来预测趣味性，提供了一种新的视角。
3. 实验或效果：研究表明，提取的特征能够在一定程度上预测用户的趣味性，验证了趣味性与创造力的可测量性。

## 📝 摘要（中文）

本研究探讨了如何自动预测Reddit用户对Wordle游戏的趣味性。我们从Reddit抓取了约8万条用户对Wordle游戏的反应，并利用OpenAI的GPT-3.5进行少量示例提示，将反应分类为表达趣味性或非趣味性。验证结果显示，GPT-3.5的标签与人类标签大致相符。我们提取了能够预测用户趣味性的Wordle游戏特征，结果表明这些特征确实提供了一个（微弱的）信号来预测用户的趣味性。这表明用户对Wordle游戏的趣味性在一定程度上是可以通过计算方式预测的，并探讨了哪些游戏特征对用户趣味性有贡献。

## 🔬 方法详解

**问题定义**：本研究旨在解决如何自动预测用户对Wordle游戏的趣味性的问题。现有方法缺乏有效的特征提取和分析，导致趣味性预测的准确性不足。

**核心思路**：论文的核心思路是利用GPT-3.5进行用户反应的分类，并基于此提取特征，构建预测模型。通过这种方式，能够更好地捕捉用户对游戏的趣味性反应。

**技术框架**：整体架构包括数据抓取、反应分类、特征提取和模型训练四个主要模块。首先从Reddit抓取用户反应，然后使用GPT-3.5进行分类，接着提取特征，最后训练预测模型。

**关键创新**：本研究的关键创新在于使用GPT-3.5进行用户反应的分类，并结合特征提取来预测趣味性，这与传统方法的人工标注和特征选择有本质区别。

**关键设计**：在技术细节上，使用了少量示例提示的方式来优化GPT-3.5的分类效果，特征提取过程中关注了游戏的多种维度，如难度、字母组合等，确保模型的有效性。

## 📊 实验亮点

实验结果显示，提取的特征能够在一定程度上预测用户的趣味性，GPT-3.5的分类准确率与人类标注相近，验证了模型的有效性。尽管预测信号较弱，但仍为趣味性分析提供了新的思路。

## 🎯 应用场景

该研究的潜在应用领域包括游戏设计、用户体验优化和社交媒体分析。通过自动化预测用户的趣味性，游戏开发者可以更好地调整游戏内容，以提高用户的参与度和满意度。此外，该方法也可用于分析其他类型的用户生成内容，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> We explore automatically predicting which Wordle games Reddit users find amusing.
>   We scrape approximately 80k reactions by Reddit users to Wordle games from Reddit, classify the reactions as expressing amusement or not using OpenAI's GPT-3.5 using few-shot prompting, and verify that GPT-3.5's labels roughly correspond to human labels.
>   We then extract features from Wordle games that can predict user amusement. We demonstrate that the features indeed provide a (weak) signal that predicts user amusement as predicted by GPT-3.5.
>   Our results indicate that user amusement at Wordle games can be predicted computationally to some extent. We explore which features of the game contribute to user amusement.
>   We find that user amusement is predictable, indicating a measurable aspect of creativity infused into Wordle games through humor.

