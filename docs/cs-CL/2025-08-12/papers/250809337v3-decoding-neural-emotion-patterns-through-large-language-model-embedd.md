---
layout: default
title: Decoding Neural Emotion Patterns through Large Language Model Embeddings
---

# Decoding Neural Emotion Patterns through Large Language Model Embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09337" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09337v3</a>
  <a href="https://arxiv.org/pdf/2508.09337.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09337v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09337v3', 'Decoding Neural Emotion Patterns through Large Language Model Embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gideon Vos, Maryam Ebrahimpour, Liza van Eijk, Zoltan Sarnyai, Mostafa Rahimi Azghadi

**分类**: cs.CL

**发布日期**: 2025-08-12 (更新: 2025-12-21)

**备注**: 26 pages, 9 figures

---

## 💡 一句话要点

**提出一种新框架以无神经影像解码语言情感与大脑功能的关系**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感计算` `自然语言处理` `大脑映射` `文本嵌入` `心理健康` `机器学习`

## 📋 核心要点

1. 现有的情感与大脑功能映射方法多依赖于昂贵的神经影像技术，缺乏对自然语言的有效分析。
2. 本文提出了一种新颖的计算框架，利用文本嵌入模型将情感内容直接映射到大脑区域，避免了神经影像的需求。
3. 实验结果表明，该方法能够有效区分临床人群，并在情感强度分析上表现出高空间特异性。

## 📝 摘要（中文）

理解语言中的情感表达如何与大脑功能相关是计算神经科学和情感计算中的一大挑战。传统的神经影像技术成本高且受限于实验室环境，而丰富的数字文本为情感与大脑的映射提供了新途径。本文提出了一种计算框架，将文本情感内容映射到解剖学定义的大脑区域，无需神经影像。通过OpenAI的文本嵌入模型生成高维语义表示，应用降维和聚类识别情感组，并将其映射到18个与情感处理相关的大脑区域。实验结果显示，抑郁个体在负面情感上表现出更强的边缘系统参与，且成功区分了不同情感。LLM生成的文本在基本情感分布上与人类相似，但在同理心和自我指涉区域的激活上缺乏细腻性。

## 🔬 方法详解

**问题定义**：本文旨在解决如何将语言中的情感表达与大脑功能进行有效映射的问题。现有方法主要依赖于神经影像技术，成本高且受限于实验室环境，限制了大规模分析的可能性。

**核心思路**：论文提出的核心思路是利用大规模文本数据，通过计算框架将文本情感内容映射到解剖学定义的大脑区域，避免了对神经影像的依赖。通过高维语义表示和聚类分析，识别情感组并进行空间映射。

**技术框架**：整体架构包括文本嵌入生成、降维处理、情感聚类和大脑区域映射四个主要模块。首先使用OpenAI的文本嵌入模型生成高维表示，然后通过降维和聚类识别情感组，最后将这些组映射到相关的大脑区域。

**关键创新**：最重要的技术创新在于提出了一种无神经影像的情感与大脑映射方法，能够在大规模文本分析中实现情感识别，并提供了一个基于大脑的AI情感表达评估基准。

**关键设计**：在技术细节上，使用了OpenAI的text-embedding-ada-002模型进行文本嵌入，采用了适当的降维技术（如PCA或t-SNE）进行数据处理，并设计了针对情感强度的词汇分析方法。

## 📊 实验亮点

实验结果显示，抑郁个体在情感映射上表现出更强的边缘系统参与，且成功区分了不同情感。LLM生成的文本在基本情感分布上与人类相似，但在同理心和自我指涉区域的激活上存在显著差异，表明该方法在情感分析中的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括情感计算、心理健康监测和人机交互等。通过大规模分析自然语言中的情感表达，可以为临床心理学提供新的工具，并为AI系统的情感理解能力提供基准，推动情感智能的发展。

## 📄 摘要（原文）

> Understanding how emotional expression in language relates to brain function is a challenge in computational neuroscience and affective computing. Traditional neuroimaging is costly and lab-bound, but abundant digital text offers new avenues for emotion-brain mapping. Prior work has largely examined neuroimaging-based emotion localization or computational text analysis separately, with little integration. We propose a computational framework that maps textual emotional content to anatomically defined brain regions without requiring neuroimaging. Using OpenAI's text-embedding-ada-002, we generate high-dimensional semantic representations, apply dimensionality reduction and clustering to identify emotional groups, and map them to 18 brain regions linked to emotional processing. Three experiments were conducted: i) analyzing conversational data from healthy vs. depressed subjects (DIAC-WOZ dataset) to compare mapping patterns, ii) applying the method to the GoEmotions dataset and iii) comparing human-written text with large language model (LLM) responses to assess differences in inferred brain activation. Emotional intensity was scored via lexical analysis. Results showed neuroanatomically plausible mappings with high spatial specificity. Depressed subjects exhibited greater limbic engagement tied to negative affect. Discrete emotions were successfully differentiated. LLM-generated text matched humans in basic emotion distribution but lacked nuanced activation in empathy and self-referential regions (medial prefrontal and posterior cingulate cortex). This cost-effective, scalable approach enables large-scale analysis of naturalistic language, distinguishes between clinical populations, and offers a brain-based benchmark for evaluating AI emotional expression.

