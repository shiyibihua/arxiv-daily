---
layout: default
title: AI-Generated Lecture Slides for Improving Slide Element Detection and Retrieval
---

# AI-Generated Lecture Slides for Improving Slide Element Detection and Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23605" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23605v1</a>
  <a href="https://arxiv.org/pdf/2506.23605.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23605v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23605v1', 'AI-Generated Lecture Slides for Improving Slide Element Detection and Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Suyash Maniyar, Vishvesh Trivedi, Ajoy Mondal, Anand Mishra, C. V. Jawahar

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-30

**备注**: 40 pages including supplementary, accepted at ICDAR 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://synslidegen.github.io/)

---

## 💡 一句话要点

**提出SynLecSlideGen以解决讲义幻灯片元素检测与检索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `幻灯片生成` `元素检测` `迁移学习` `合成数据` `教育技术` `人工智能`

## 📋 核心要点

1. 现有的讲义幻灯片元素检测和检索方法依赖大量人工标注，效率低且需要专业知识。
2. 本文提出的SynLecSlideGen通过大型语言模型生成合成幻灯片，减少了对人工标注的依赖。
3. 实验表明，使用合成幻灯片进行少样本迁移学习显著提升了模型在真实数据上的表现。

## 📝 摘要（中文）

讲义幻灯片元素检测与检索是幻灯片理解中的关键问题。训练有效模型通常依赖于大量的人工标注，而标注大量讲义幻灯片既费时又需要领域专业知识。为此，本文提出了一种基于大型语言模型（LLM）的合成讲义幻灯片生成管道SynLecSlideGen，能够生成高质量、连贯且真实的幻灯片。同时，我们手动标注了1050个真实讲义幻灯片，创建了评估基准RealSlide。通过在真实数据上进行少样本迁移学习，使用在合成幻灯片上预训练的模型，实验结果表明，与仅在真实数据上训练相比，基于合成幻灯片的少样本迁移学习显著提高了性能。这表明合成数据能够有效弥补标注讲义幻灯片的不足。我们的代码和资源已在项目网站上公开。

## 🔬 方法详解

**问题定义**：本研究旨在解决讲义幻灯片元素检测与检索中的数据标注不足问题。现有方法依赖大量人工标注，导致训练过程费时且成本高昂。

**核心思路**：提出的SynLecSlideGen利用大型语言模型生成合成讲义幻灯片，以此减少对真实标注数据的依赖，提升模型的训练效率和效果。

**技术框架**：该方法包括合成幻灯片生成模块和评估基准创建模块。合成模块生成高质量幻灯片，评估模块则通过手动标注构建RealSlide基准。

**关键创新**：最重要的创新在于通过合成数据进行少样本迁移学习，显著提高了模型在真实数据上的性能，与传统方法相比，减少了对标注数据的需求。

**关键设计**：在合成幻灯片生成过程中，采用了特定的参数设置和损失函数，以确保生成幻灯片的质量和连贯性。

## 📊 实验亮点

实验结果显示，使用合成幻灯片进行少样本迁移学习后，模型在真实数据集上的性能提升显著，具体提升幅度达到XX%（具体数据未知），表明合成数据在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、在线学习平台和知识管理系统。通过减少对人工标注的依赖，SynLecSlideGen能够加速幻灯片内容的生成与检索，提升学习效率，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Lecture slide element detection and retrieval are key problems in slide understanding. Training effective models for these tasks often depends on extensive manual annotation. However, annotating large volumes of lecture slides for supervised training is labor intensive and requires domain expertise. To address this, we propose a large language model (LLM)-guided synthetic lecture slide generation pipeline, SynLecSlideGen, which produces high-quality, coherent and realistic slides. We also create an evaluation benchmark, namely RealSlide by manually annotating 1,050 real lecture slides. To assess the utility of our synthetic slides, we perform few-shot transfer learning on real data using models pre-trained on them. Experimental results show that few-shot transfer learning with pretraining on synthetic slides significantly improves performance compared to training only on real data. This demonstrates that synthetic data can effectively compensate for limited labeled lecture slides. The code and resources of our work are publicly available on our project website: https://synslidegen.github.io/.

