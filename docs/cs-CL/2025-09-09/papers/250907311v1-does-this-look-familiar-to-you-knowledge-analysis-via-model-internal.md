---
layout: default
title: Does This Look Familiar to You? Knowledge Analysis via Model Internal Representations
---

# Does This Look Familiar to You? Knowledge Analysis via Model Internal Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07311" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07311v1</a>
  <a href="https://arxiv.org/pdf/2509.07311.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07311v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07311v1', 'Does This Look Familiar to You? Knowledge Analysis via Model Internal Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sihyun Park

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-09

---

## 💡 一句话要点

**提出KAMIR方法，通过模型内部表征分析进行高效训练数据选择，提升模型泛化能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据选择` `模型内部表征` `知识分析` `监督微调` `大型语言模型` `机器阅读理解` `文本摘要`

## 📋 核心要点

1. 现有SFT训练数据选择缺乏有效方法，简单增加数据量或依赖提示工程的方法存在局限性。
2. KAMIR通过分析模型内部表征，评估数据与模型知识的关联度，选择对模型而言“不熟悉”但有价值的数据。
3. 实验证明，使用KAMIR选择的数据进行训练，能够提升模型在机器阅读理解和摘要等任务上的泛化性能。

## 📝 摘要（中文）

大型语言模型（LLM）的最新进展得益于预训练、监督微调（SFT）和对齐调整。其中，SFT在将模型的通用知识转化为针对特定任务的结构化响应方面起着关键作用。然而，目前还没有明确有效的数据选择方法。简单地增加数据量并不能保证性能的提升，而预处理、抽样和验证则需要大量的时间和成本。为了解决这个问题，已经提出了各种数据选择方法。其中，基于知识的选择方法通过分析模型的响应来识别合适的训练数据。然而，这些方法通常依赖于提示工程，使其对变化敏感，并产生额外的提示设计成本。本研究提出了知识分析通过模型内部表征（KAMIR），这是一种新颖的方法，通过分析模型内部表征的数据来克服这些限制。KAMIR计算每一层（块）的隐藏状态与给定输入的最终隐藏状态之间的相似性来评估数据。与主要局限于多项选择任务的先前方法不同，KAMIR可以应用于广泛的任务，如机器阅读理解和摘要。此外，即使使用小型数据集和简单的分类器架构，它也能基于模型对输入的熟悉程度选择对训练有用的数据。跨不同任务数据集的实验表明，使用不太熟悉的数据进行训练可以带来更好的泛化性能。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型监督微调（SFT）阶段，如何高效选择训练数据的问题。现有方法，如简单增加数据量或依赖提示工程的方法，要么效率低下，要么对提示变化敏感，且成本较高。这些方法难以准确评估数据对模型学习的价值，导致训练效果不佳。

**核心思路**：论文的核心思路是，通过分析模型内部的隐藏层表征，来评估数据与模型已有知识的关联程度。具体来说，如果一个数据样本在模型的内部表征上与最终表征的相似度较低，则认为该样本对模型而言是“不熟悉”的，可能包含更多有价值的信息，从而更有助于提升模型的泛化能力。

**技术框架**：KAMIR方法主要包含以下几个阶段：1) 对于给定的输入数据，通过模型的前向传播，获取每一层（block）的隐藏状态。2) 计算每一层的隐藏状态与最终隐藏状态之间的相似度。3) 基于计算得到的相似度，对数据进行排序或筛选，选择相似度较低的数据作为训练集。4) 使用选择出的数据对模型进行微调。

**关键创新**：KAMIR的关键创新在于，它利用模型自身的内部表征来评估数据的价值，避免了对外部知识库或提示工程的依赖。与以往主要针对多项选择题的方法不同，KAMIR可以应用于更广泛的任务，如机器阅读理解和摘要。此外，KAMIR方法只需要少量数据和一个简单的分类器架构，就能有效地选择训练数据。

**关键设计**：KAMIR的关键设计包括：1) 隐藏状态相似度的计算方式，例如可以使用余弦相似度或欧氏距离。2) 如何综合不同层的相似度信息，例如可以对不同层的相似度进行加权平均。3) 如何设定相似度阈值，以选择合适的训练数据。论文中可能还涉及了特定任务相关的损失函数或网络结构调整，但摘要中未提及具体细节。

## 📊 实验亮点

实验结果表明，使用KAMIR方法选择的数据进行训练，能够显著提升模型在机器阅读理解和摘要等任务上的泛化性能。即使在小数据集和简单分类器架构下，KAMIR也能有效选择训练数据。具体的性能提升数据和对比基线需要在论文正文中查找。

## 🎯 应用场景

KAMIR方法可应用于各种需要数据选择的自然语言处理任务，例如机器翻译、文本生成、对话系统等。通过选择更有价值的训练数据，可以降低训练成本，提升模型性能，加速模型开发周期。该方法尤其适用于数据资源有限或数据质量参差不齐的场景，具有重要的实际应用价值。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have been driven by pretraining, supervised fine tuning (SFT), and alignment tuning. Among these, SFT plays a crucial role in transforming a model 's general knowledge into structured responses tailored to specific tasks. However, there is no clearly established methodology for effective training data selection. Simply increasing the volume of data does not guarantee performance improvements, while preprocessing, sampling, and validation require substantial time and cost.
>   To address this issue, a variety of data selection methods have been proposed. Among them, knowledge based selection approaches identify suitable training data by analyzing the model 's responses. Nevertheless, these methods typically rely on prompt engineering, making them sensitive to variations and incurring additional costs for prompt design.
>   In this study, we propose Knowledge Analysis via Model Internal Representations (KAMIR), a novel approach that overcomes these limitations by analyzing data based on the model 's internal representations. KAMIR computes similarities between the hidden states of each layer (block) and the final hidden states for a given input to assess the data. Unlike prior methods that were largely limited to multiple choice tasks, KAMIR can be applied to a wide range of tasks such as machine reading comprehension and summarization. Moreover, it selects data useful for training based on the model 's familiarity with the input, even with a small dataset and a simple classifier architecture. Experiments across diverse task datasets demonstrate that training with less familiar data leads to better generalization performance.

