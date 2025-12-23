---
layout: default
title: Universal Music Representations? Evaluating Foundation Models on World Music Corpora
---

# Universal Music Representations? Evaluating Foundation Models on World Music Corpora

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17055" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17055v1</a>
  <a href="https://arxiv.org/pdf/2506.17055.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17055v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17055v1', 'Universal Music Representations? Evaluating Foundation Models on World Music Corpora')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Charilaos Papaioannou, Emmanouil Benetos, Alexandros Potamianos

**分类**: cs.SD, cs.IR, cs.LG, eess.AS

**发布日期**: 2025-06-20

**备注**: Accepted at ISMIR 2025

---

## 💡 一句话要点

**评估基础模型在世界音乐语料库上的普适性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `基础模型` `音乐信息检索` `跨文化能力` `少样本学习` `音乐传统` `模型评估` `音乐理解`

## 📋 核心要点

1. 现有基础模型在不同音乐传统中的泛化能力尚不明确，尤其是对非西方音乐的理解存在挑战。
2. 本文提出通过探测、监督微调和少样本学习等方法，系统评估基础模型在多种音乐传统中的表现。
3. 实验结果表明，较大的模型在非西方音乐上表现优异，五个数据集中的五个达到了最先进的性能，显示出基础模型在世界音乐理解中的有效性。

## 📝 摘要（中文）

基础模型在音乐信息检索领域引发了革命，但其在不同音乐传统中的泛化能力仍存在疑问。本文对五种先进的音频基础模型在六个音乐语料库（包括西方流行、希腊、土耳其和印度古典音乐）进行了全面评估。我们采用三种互补的方法来研究这些模型的跨文化能力：探测以评估固有表示、针对1-2层的有针对性监督微调，以及低资源场景下的多标签少样本学习。分析结果显示，模型在非西方音乐上的表现通常优于西方音乐，但对于文化差异较大的传统，结果有所下降。我们的研究框架和基准结果为理解当前模型在实现普适音乐表示方面的进展提供了重要参考。

## 🔬 方法详解

**问题定义**：本文旨在解决基础模型在不同音乐传统中的泛化能力不足的问题，尤其是对非西方音乐的理解能力。现有方法在跨文化音乐信息检索中面临挑战，缺乏系统评估。

**核心思路**：通过探测、针对性微调和少样本学习等方法，全面评估基础模型的跨文化能力，探索其在不同音乐传统中的表现差异。这样的设计旨在揭示模型的固有知识和潜在的改进空间。

**技术框架**：研究采用三种互补的方法：首先，通过探测技术评估模型的固有表示；其次，进行有针对性的监督微调以提升特定层的表现；最后，应用多标签少样本学习应对低资源场景。这些方法结合形成了一个全面的评估框架。

**关键创新**：本文的主要创新在于提出了一个系统的评估框架，结合多种方法来探讨基础模型在不同文化背景下的表现，尤其是对非西方音乐的理解能力。与现有方法相比，本文强调了模型固有知识的有效性。

**关键设计**：在实验中，针对性微调的层数设置为1-2层，采用多标签损失函数以适应多样化的音乐标签。此外，模型的选择涵盖了五种最先进的音频基础模型，确保了评估的全面性和准确性。

## 📊 实验亮点

实验结果显示，较大的基础模型在非西方音乐上的表现优于西方音乐，五个数据集中的五个达到了最先进的性能。尽管针对性微调在某些情况下未必优于探测，但整体结果表明基础模型在音乐知识的编码上已有显著成效。

## 🎯 应用场景

该研究的潜在应用领域包括音乐推荐系统、跨文化音乐分析和音乐教育等。通过提升基础模型在不同音乐传统中的理解能力，能够为用户提供更精准的音乐推荐和更丰富的音乐体验。此外，研究结果为未来音乐信息检索技术的发展奠定了基础，推动了跨文化音乐研究的深入。

## 📄 摘要（原文）

> Foundation models have revolutionized music information retrieval, but questions remain about their ability to generalize across diverse musical traditions. This paper presents a comprehensive evaluation of five state-of-the-art audio foundation models across six musical corpora spanning Western popular, Greek, Turkish, and Indian classical traditions. We employ three complementary methodologies to investigate these models' cross-cultural capabilities: probing to assess inherent representations, targeted supervised fine-tuning of 1-2 layers, and multi-label few-shot learning for low-resource scenarios. Our analysis shows varying cross-cultural generalization, with larger models typically outperforming on non-Western music, though results decline for culturally distant traditions. Notably, our approaches achieve state-of-the-art performance on five out of six evaluated datasets, demonstrating the effectiveness of foundation models for world music understanding. We also find that our targeted fine-tuning approach does not consistently outperform probing across all settings, suggesting foundation models already encode substantial musical knowledge. Our evaluation framework and benchmarking results contribute to understanding how far current models are from achieving universal music representations while establishing metrics for future progress.

