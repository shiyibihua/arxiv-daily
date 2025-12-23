---
layout: default
title: Dataset of News Articles with Provenance Metadata for Media Relevance Assessment
---

# Dataset of News Articles with Provenance Metadata for Media Relevance Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09847" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09847v1</a>
  <a href="https://arxiv.org/pdf/2506.09847.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09847v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09847v1', 'Dataset of News Articles with Provenance Metadata for Media Relevance Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tomas Peterka, Matyas Bohacek

**分类**: cs.CL, cs.AI, cs.CV, cs.CY

**发布日期**: 2025-06-11

**期刊**: Workshop on NLP for Positive Impact @ ACL 2025

---

## 💡 一句话要点

**提出新闻媒体来源数据集以解决媒体相关性评估问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `媒体操控` `虚假信息` `数据集构建` `大型语言模型` `媒体相关性评估`

## 📋 核心要点

1. 现有方法在检测媒体操控时，往往忽略了图像与文本叙述之间的潜在不一致性。
2. 本文提出了新闻媒体来源数据集，并定义了两个新任务，以更全面地评估媒体相关性。
3. 在六种大型语言模型上进行的实验显示，LOR任务的零样本性能较好，但DTOR任务的表现仍需改进。

## 📝 摘要（中文）

在当今的虚假信息和误导性信息环境中，脱离上下文和错误归属的图像是媒体操控的主要形式。现有方法往往只考虑图像语义与文本叙述的一致性，忽视了图像的操控。为此，本文引入了新闻媒体来源数据集，该数据集包含带有来源标签的新闻文章和图像。我们在此数据集上提出了两个任务：来源位置相关性（LOR）和来源时间相关性（DTOR），并在六种大型语言模型上展示了基线结果。尽管LOR的零样本性能表现良好，但DTOR的性能仍有待提升，未来需要专门的架构进行改进。

## 🔬 方法详解

**问题定义**：本文旨在解决媒体操控检测中的不足，尤其是现有方法未能有效识别图像与文本叙述之间的潜在不一致性。

**核心思路**：通过引入带有来源标签的新闻文章和图像数据集，提出了两个新任务，旨在更全面地评估媒体内容的相关性。

**技术框架**：整体架构包括数据集构建、任务定义和模型评估三个主要模块。数据集包含标注的图像和文本，任务包括LOR和DTOR。

**关键创新**：最重要的创新在于引入了来源标签，允许模型在评估媒体相关性时考虑图像的来源信息，从而克服了传统方法的局限。

**关键设计**：在实验中使用了六种大型语言模型，针对LOR和DTOR任务进行了基线测试，采用了标准的损失函数和评估指标。

## 📊 实验亮点

实验结果显示，在LOR任务上，模型的零样本性能表现良好，具体性能数据未详述；而在DTOR任务上，模型的表现则未达到预期，显示出未来改进的空间。

## 🎯 应用场景

该研究的潜在应用领域包括新闻媒体监测、社交媒体内容审核和虚假信息检测等。通过提高媒体内容的相关性评估能力，可以有效减少误导性信息的传播，增强公众对信息的信任度，具有重要的社会价值和实际影响。

## 📄 摘要（原文）

> Out-of-context and misattributed imagery is the leading form of media manipulation in today's misinformation and disinformation landscape. The existing methods attempting to detect this practice often only consider whether the semantics of the imagery corresponds to the text narrative, missing manipulation so long as the depicted objects or scenes somewhat correspond to the narrative at hand. To tackle this, we introduce News Media Provenance Dataset, a dataset of news articles with provenance-tagged images. We formulate two tasks on this dataset, location of origin relevance (LOR) and date and time of origin relevance (DTOR), and present baseline results on six large language models (LLMs). We identify that, while the zero-shot performance on LOR is promising, the performance on DTOR hinders, leaving room for specialized architectures and future work.

