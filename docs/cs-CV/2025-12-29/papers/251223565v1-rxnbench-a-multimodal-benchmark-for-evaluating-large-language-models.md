---
layout: default
title: "RxnBench: A Multimodal Benchmark for Evaluating Large Language Models on Chemical Reaction Understanding from Scientific Literature"
---

# RxnBench: A Multimodal Benchmark for Evaluating Large Language Models on Chemical Reaction Understanding from Scientific Literature

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23565" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23565v1</a>
  <a href="https://arxiv.org/pdf/2512.23565.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23565v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23565v1', 'RxnBench: A Multimodal Benchmark for Evaluating Large Language Models on Chemical Reaction Understanding from Scientific Literature')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanzheng Li, Xi Fang, Yixuan Li, Chaozheng Huang, Junjie Wang, Xi Wang, Hongzhe Bai, Bojun Hao, Shenyu Lin, Huiqi Liang, Linfeng Zhang, Guolin Ke

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**RxnBench：一个多模态基准，用于评估大语言模型对科学文献中化学反应的理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `化学反应理解` `大语言模型` `基准数据集` `科学文献`

## 📋 核心要点

1. 现有MLLM在理解化学文献中复杂的反应图谱和文本信息方面存在不足，限制了其在化学发现中的应用。
2. RxnBench通过构建包含单图问答和全文问答的多层基准，系统性地评估MLLM在化学反应理解方面的能力。
3. 实验结果表明，现有MLLM在化学逻辑和结构识别方面存在明显差距，需要更专业的视觉编码器和推理引擎。

## 📝 摘要（中文）

将多模态大语言模型（MLLM）集成到化学领域有望彻底改变科学发现，但它们理解真实文献中密集、图形化反应语言的能力仍未得到充分探索。本文提出了RxnBench，这是一个多层基准，旨在严格评估MLLM对科学PDF中化学反应的理解能力。RxnBench包含两个任务：单图问答（SF-QA），使用从305个精选反应方案中提取的1525个问题来测试细粒度的视觉感知和机理推理；以及全文问答（FD-QA），要求模型综合来自108篇文章的信息，需要跨模态整合文本、方案和表格。对MLLM的评估揭示了一个关键的能力差距：虽然模型擅长提取显式文本，但它们在深入的化学逻辑和精确的结构识别方面存在困难。值得注意的是，具有推理时推理的模型明显优于标准架构，但没有一个模型在FD-QA上达到50%的准确率。这些发现强调了迫切需要特定领域的视觉编码器和更强大的推理引擎，以推进自主AI化学家的发展。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLM）在理解化学科学文献中化学反应的难题。现有方法在处理包含复杂图表和文本信息的化学文献时，无法有效提取和整合信息，尤其是在理解化学逻辑和精确识别化学结构方面存在明显不足。这阻碍了MLLM在化学研究中的应用，例如自动化文献分析和反应预测。

**核心思路**：论文的核心思路是构建一个专门用于评估MLLM在化学反应理解方面能力的基准数据集RxnBench。通过设计不同难度的问答任务，系统性地测试MLLM对化学反应的视觉感知、机理推理和信息整合能力。该基准旨在揭示现有MLLM的局限性，并推动领域内模型的发展。

**技术框架**：RxnBench包含两个主要任务：单图问答（SF-QA）和全文问答（FD-QA）。SF-QA侧重于细粒度的视觉感知和机理推理，使用从反应方案中提取的问题进行评估。FD-QA则要求模型整合来自整篇文章的信息，包括文本、反应方案和表格，以回答更复杂的问题。整个流程包括数据收集、问题生成、模型评估和结果分析。

**关键创新**：RxnBench的关键创新在于其专注于评估MLLM对化学反应的理解能力，而不仅仅是通用的视觉或文本理解。它通过设计特定领域的问答任务，更准确地反映了MLLM在化学研究中的实际应用需求。此外，RxnBench涵盖了单图和全文两种场景，更全面地评估了模型的跨模态信息整合能力。

**关键设计**：SF-QA任务的问题设计侧重于反应机理和结构识别，例如询问反应物、产物、催化剂等。FD-QA任务的问题则需要模型整合来自不同模态的信息，例如从文本中提取反应条件，从反应方案中识别反应类型。评估指标主要采用准确率，以衡量模型回答问题的正确程度。论文还探索了使用推理时推理（inference-time reasoning）技术来提升模型性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23565v1/media/image1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23565v1/media/image2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23565v1/media/image3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有MLLM在RxnBench上的表现与人类专家存在显著差距，尤其是在FD-QA任务上，没有模型达到50%的准确率。具有推理时推理的模型在一定程度上提升了性能，但仍远低于预期。这些结果表明，需要开发更专业的视觉编码器和推理引擎，以提高MLLM在化学领域的应用能力。

## 🎯 应用场景

RxnBench的潜在应用领域包括：自动化化学文献分析、智能化学反应预测、辅助化学研究和教育等。通过提高MLLM对化学反应的理解能力，可以加速新材料的发现、优化化学反应路径，并为化学研究人员提供更强大的工具。未来，该基准可以扩展到其他化学领域，例如药物发现和材料科学。

## 📄 摘要（原文）

> The integration of Multimodal Large Language Models (MLLMs) into chemistry promises to revolutionize scientific discovery, yet their ability to comprehend the dense, graphical language of reactions within authentic literature remains underexplored. Here, we introduce RxnBench, a multi-tiered benchmark designed to rigorously evaluate MLLMs on chemical reaction understanding from scientific PDFs. RxnBench comprises two tasks: Single-Figure QA (SF-QA), which tests fine-grained visual perception and mechanistic reasoning using 1,525 questions derived from 305 curated reaction schemes, and Full-Document QA (FD-QA), which challenges models to synthesize information from 108 articles, requiring cross-modal integration of text, schemes, and tables. Our evaluation of MLLMs reveals a critical capability gap: while models excel at extracting explicit text, they struggle with deep chemical logic and precise structural recognition. Notably, models with inference-time reasoning significantly outperform standard architectures, yet none achieve 50\% accuracy on FD-QA. These findings underscore the urgent need for domain-specific visual encoders and stronger reasoning engines to advance autonomous AI chemists.

