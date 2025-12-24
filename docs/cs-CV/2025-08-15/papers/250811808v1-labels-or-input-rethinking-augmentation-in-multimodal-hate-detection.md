---
layout: default
title: Labels or Input? Rethinking Augmentation in Multimodal Hate Detection
---

# Labels or Input? Rethinking Augmentation in Multimodal Hate Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11808" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11808v1</a>
  <a href="https://arxiv.org/pdf/2508.11808.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11808v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11808v1', 'Labels or Input? Rethinking Augmentation in Multimodal Hate Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sahajpreet Singh, Rongxin Ouyang, Subhayan Mukerjee, Kokil Jaidka

**分类**: cs.CV, cs.AI, cs.CL, cs.CY, cs.MM

**发布日期**: 2025-08-15

**备注**: 13 pages, 2 figures, 7 tables

---

## 💡 一句话要点

**提出双重方法以提升多模态仇恨检测的准确性**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态仇恨检测` `视觉语言模型` `提示优化` `数据增强` `鲁棒性提升`

## 📋 核心要点

1. 现有的多模态仇恨检测方法在细粒度监督和隐性仇恨言论的识别上存在不足，导致检测效果不佳。
2. 本文提出的提示优化框架和多模态数据增强管道，旨在通过优化提示设计和生成中立数据来提升检测性能。
3. 实验结果表明，结构化提示和数据组成对模型性能至关重要，InternVL2在二元和扩展设置中取得了最佳F1分数。

## 📝 摘要（中文）

现代网络充斥着多模态内容，使得检测仇恨表情包的挑战加剧。这些表情包常通过文本与图像之间的微妙互动传达有害意图。尽管近期视觉语言模型（VLMs）取得了一定进展，但它们在细粒度监督方面仍显不足，并容易受到隐性仇恨言论的影响。本文提出了一种双重方法来改善多模态仇恨检测，首先是一个提示优化框架，通过系统性地变化提示结构、监督粒度和训练模式，发现结构化提示能在小模型中提升鲁棒性；其次，介绍了一种多模态数据增强管道，生成2479个反事实中立的表情包，有效减少虚假相关性并提高分类器的泛化能力。我们的研究为构建合成数据以训练稳健和公平的视觉语言模型开辟了新方向。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态仇恨检测中存在的细粒度监督不足和隐性仇恨言论识别困难的问题。现有方法在处理复杂的文本与图像交互时表现不佳，导致检测效果受限。

**核心思路**：论文提出的核心思路是通过优化提示设计和引入多模态数据增强，来提升模型的鲁棒性和泛化能力。通过系统性地调整提示结构和监督粒度，能够有效改善模型在小样本情况下的表现。

**技术框架**：整体架构包括两个主要模块：提示优化框架和多模态数据增强管道。提示优化框架通过不同的提示结构和训练模式进行实验，而数据增强管道则利用多代理的LLM-VLM设置生成中立表情包。

**关键创新**：最重要的技术创新在于引入了系统化的提示优化和针对性的多模态数据增强，这与现有方法的单一模型训练和数据处理方式有本质区别。

**关键设计**：在提示优化中，设计了多种提示结构和监督粒度，实验表明结构化提示能显著提升小模型的鲁棒性；数据增强管道生成的中立表情包数量达到2479个，有效减少了虚假相关性。实验中使用的损失函数和网络结构经过精心设计，以确保模型的高效训练和准确性。

## 📊 实验亮点

实验结果显示，结构化提示设计和数据增强显著提升了模型性能，InternVL2在二元和扩展设置中分别达到了最佳F1分数。通过引入2479个反事实中立表情包，模型的泛化能力得到了有效增强，减少了虚假相关性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容监测、在线社区管理和自动化内容审核等。通过提升多模态仇恨检测的准确性，可以有效减少网络暴力和仇恨言论的传播，促进更安全的网络环境。未来，该方法可能为其他多模态任务提供借鉴，推动相关领域的研究进展。

## 📄 摘要（原文）

> The modern web is saturated with multimodal content, intensifying the challenge of detecting hateful memes, where harmful intent is often conveyed through subtle interactions between text and image under the guise of humor or satire. While recent advances in Vision-Language Models (VLMs) show promise, these models lack support for fine-grained supervision and remain susceptible to implicit hate speech. In this paper, we present a dual-pronged approach to improve multimodal hate detection. First, we propose a prompt optimization framework that systematically varies prompt structure, supervision granularity, and training modality. We show that prompt design and label scaling both influence performance, with structured prompts improving robustness even in small models, and InternVL2 achieving the best F1-scores across binary and scaled settings. Second, we introduce a multimodal data augmentation pipeline that generates 2,479 counterfactually neutral memes by isolating and rewriting the hateful modality. This pipeline, powered by a multi-agent LLM-VLM setup, successfully reduces spurious correlations and improves classifier generalization. Our approaches inspire new directions for building synthetic data to train robust and fair vision-language models. Our findings demonstrate that prompt structure and data composition are as critical as model size, and that targeted augmentation can support more trustworthy and context-sensitive hate detection.

