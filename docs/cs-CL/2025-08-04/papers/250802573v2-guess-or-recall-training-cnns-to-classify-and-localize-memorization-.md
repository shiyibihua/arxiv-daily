---
layout: default
title: Guess or Recall? Training CNNs to Classify and Localize Memorization in LLMs
---

# Guess or Recall? Training CNNs to Classify and Localize Memorization in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02573" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02573v2</a>
  <a href="https://arxiv.org/pdf/2508.02573.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02573v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02573v2', 'Guess or Recall? Training CNNs to Classify and Localize Memorization in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jérémie Dentan, Davide Buscaldi, Sonia Vanier

**分类**: cs.CL

**发布日期**: 2025-08-04 (更新: 2025-11-13)

**备注**: This paper has been accepted for publication at AAAI-26

---

## 💡 一句话要点

**提出新分类法以分析大语言模型中的记忆现象**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `记忆机制` `卷积神经网络` `注意力权重` `自然语言处理` `模型分析`

## 📋 核心要点

1. 现有的记忆分类法未能有效反映大型语言模型中的不同记忆机制，导致分析不准确。
2. 本文通过训练CNN分析LLM的注意力权重，提出了一种新的记忆分类法，旨在提高对记忆现象的理解。
3. 实验结果表明，少量逐字记忆并不对应于特定的注意力机制，且许多样本是模型的猜测，需进行单独研究。

## 📝 摘要（中文）

在大型语言模型（LLMs）中，逐字记忆是一种复杂现象，涉及不同的基本机制。本文提出了一种新方法，通过训练卷积神经网络（CNN）分析LLM的注意力权重，并评估现有记忆分类法与注意力权重的对齐情况。研究发现，现有分类法表现不佳，未能反映注意力块中的不同机制。我们提出的新分类法包括三类：通过语言建模能力猜测的记忆样本、高重复训练集导致的回忆样本以及非记忆样本。结果显示，少量逐字记忆并不对应于独特的注意力机制，且大量可提取样本实际上是模型猜测的，需单独研究。最后，我们开发了一种自定义的可视化解释技术，以定位与每种记忆形式相关的注意力权重区域。

## 🔬 方法详解

**问题定义**：本文旨在解决现有记忆分类法在分析大型语言模型中的不足，特别是未能准确反映注意力机制的多样性。

**核心思路**：通过训练卷积神经网络（CNN）在LLM的注意力权重上进行分析，提出新的分类法以提高对记忆现象的理解。

**技术框架**：整体框架包括数据收集、CNN训练、注意力权重分析和新分类法的提出，主要模块包括数据预处理、模型训练和结果评估。

**关键创新**：提出的新分类法将记忆样本分为三类，强调了模型猜测和高重复样本的区别，显著改善了对记忆机制的理解。

**关键设计**：在模型训练中，使用特定的损失函数和网络结构，以确保CNN能够有效捕捉注意力权重的特征，并进行可视化解释。

## 📊 实验亮点

实验结果显示，现有的记忆分类法在反映注意力机制方面表现不佳，而新提出的分类法能够更好地对齐注意力权重。研究发现，少量逐字记忆并不对应于独特的注意力机制，且约有相当比例的样本是模型的猜测，需单独分析。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等。通过更好地理解大型语言模型的记忆机制，可以优化模型设计，提高其在实际应用中的表现和可靠性。未来，该研究可能推动更高效的模型训练和更准确的记忆分析方法的发展。

## 📄 摘要（原文）

> Verbatim memorization in Large Language Models (LLMs) is a multifaceted phenomenon involving distinct underlying mechanisms. We introduce a novel method to analyze the different forms of memorization described by the existing taxonomy. Specifically, we train Convolutional Neural Networks (CNNs) on the attention weights of the LLM and evaluate the alignment between this taxonomy and the attention weights involved in decoding.
>   We find that the existing taxonomy performs poorly and fails to reflect distinct mechanisms within the attention blocks. We propose a new taxonomy that maximizes alignment with the attention weights, consisting of three categories: memorized samples that are guessed using language modeling abilities, memorized samples that are recalled due to high duplication in the training set, and non-memorized samples. Our results reveal that few-shot verbatim memorization does not correspond to a distinct attention mechanism. We also show that a significant proportion of extractable samples are in fact guessed by the model and should therefore be studied separately. Finally, we develop a custom visual interpretability technique to localize the regions of the attention weights involved in each form of memorization.

