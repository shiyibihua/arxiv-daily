---
layout: default
title: Utilizing Multilingual Encoders to Improve Large Language Models for Low-Resource Languages
---

# Utilizing Multilingual Encoders to Improve Large Language Models for Low-Resource Languages

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09091" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09091v3</a>
  <a href="https://arxiv.org/pdf/2508.09091.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09091v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09091v3', 'Utilizing Multilingual Encoders to Improve Large Language Models for Low-Resource Languages')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Imalsha Puranegedara, Themira Chathumina, Nisal Ranathunga, Nisansa de Silva, Surangika Ranathunga, Mokanarangan Thayaparan

**分类**: cs.CL

**发布日期**: 2025-08-12 (更新: 2025-11-08)

**DOI**: [10.1109/MERCon67903.2025.11216992](https://doi.org/10.1109/MERCon67903.2025.11216992)

---

## 💡 一句话要点

**提出多层融合策略以提升低资源语言的LLM性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低资源语言` `大型语言模型` `多语言处理` `中间层融合` `Transformer模型` `语言模型优化` `数据效率`

## 📋 核心要点

1. 现有方法在低资源语言上的表现不佳，主要由于训练数据的英语中心化，导致模型无法有效处理多语言输入。
2. 本文提出了一种新颖的架构，通过融合所有中间层的表示，增强了传递给大型语言模型的语言信息。
3. 实验结果显示，所提模型在多个数据集上均显著优于基线，尤其在低资源语言上取得了明显的性能提升。

## 📝 摘要（中文）

大型语言模型（LLMs）在英语上表现优异，但在低资源语言（LRLs）上性能显著下降，主要由于训练数据的英语中心化。现有方法如LangBridge仅使用最终编码层对LLMs进行对齐。本文提出了一种新颖的架构，融合所有中间层，丰富传递给LLM的语言信息。我们的方法包括两种策略：全局Softmax加权和基于Transformer的Softmax模型，后者学习特定于token的权重。通过将融合表示映射到LLM的嵌入空间，使其能够处理多语言输入。实验结果表明，我们的Transformer Softmax模型在XNLI、IndicXNLI、僧伽罗新闻分类和亚马逊评论上显著超越LangBridge基线，尤其在LRLs上表现出色，僧伽罗分类准确率从71.66%提升至75.86%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在低资源语言上的性能下降问题，现有方法如LangBridge仅利用最终编码层，未能充分利用中间层信息。

**核心思路**：通过融合所有中间层的表示，增强传递给LLM的语言信息，从而提升其在低资源语言上的表现。该设计旨在充分利用多层次的语言特征。

**技术框架**：整体架构包括两个主要模块：全局Softmax加权用于评估各层的重要性，以及基于Transformer的Softmax模型用于学习token特定的权重。融合后的表示被映射到LLM的嵌入空间。

**关键创新**：最重要的创新在于融合所有中间层的表示，而非仅依赖最终层。这一方法显著提升了模型对低资源语言的理解能力。

**关键设计**：模型训练仅使用英语数据，未使用任何平行或多语言数据。全局Softmax和Transformer Softmax的设计确保了层间信息的有效整合。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文。

## 📊 实验亮点

实验结果显示，所提Transformer Softmax模型在XNLI、IndicXNLI、僧伽罗新闻分类和亚马逊评论上显著超越LangBridge基线，特别是在低资源语言上，僧伽罗分类准确率从71.66%提升至75.86%，整体XNLI准确率从70.36%提升至71.50%。

## 🎯 应用场景

该研究的潜在应用领域包括多语言翻译、跨语言信息检索和低资源语言的自然语言处理任务。通过提升低资源语言的处理能力，该方法有助于实现更公平的语言技术发展，促进全球语言的平等使用。

## 📄 摘要（原文）

> Large Language Models (LLMs) excel in English, but their performance degrades significantly on low-resource languages (LRLs) due to English-centric training. While methods like LangBridge align LLMs with multilingual encoders such as the Massively Multilingual Text-to-Text Transfer Transformer (mT5), they typically use only the final encoder layer. We propose a novel architecture that fuses all intermediate layers, enriching the linguistic information passed to the LLM. Our approach features two strategies: (1) a Global Softmax weighting for overall layer importance, and (2) a Transformer Softmax model that learns token-specific weights. The fused representations are mapped into the LLM's embedding space, enabling it to process multilingual inputs. The model is trained only on English data, without using any parallel or multilingual data. Evaluated on XNLI, IndicXNLI, Sinhala News Classification, and Amazon Reviews, our Transformer Softmax model significantly outperforms the LangBridge baseline. We observe strong performance gains in LRLs, improving Sinhala classification accuracy from 71.66% to 75.86% and achieving clear improvements across Indic languages such as Tamil, Bengali, and Malayalam. These specific gains contribute to an overall boost in average XNLI accuracy from 70.36% to 71.50%. This approach offers a scalable, data-efficient path toward more capable and equitable multilingual LLMs.

