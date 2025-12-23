---
layout: default
title: A MISMATCHED Benchmark for Scientific Natural Language Inference
---

# A MISMATCHED Benchmark for Scientific Natural Language Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04603" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04603v1</a>
  <a href="https://arxiv.org/pdf/2506.04603.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04603v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04603v1', 'A MISMATCHED Benchmark for Scientific Natural Language Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Firoz Shaik, Mobashir Sadat, Nikita Gautam, Doina Caragea, Cornelia Caragea

**分类**: cs.CL

**发布日期**: 2025-06-05

**备注**: Accepted to Findings of ACL 2025

---

## 💡 一句话要点

**提出MISMATCHED基准以解决科学自然语言推理的领域偏差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `科学自然语言推理` `数据集构建` `领域偏差` `模型训练` `语言模型`

## 📋 核心要点

1. 现有的科学自然语言推理数据集主要集中在计算机科学领域，忽视了心理学、工程学和公共卫生等非计算机科学领域，导致评估的局限性。
2. 本文提出了MISMATCHED基准，包含来自三个非计算机科学领域的句子对，并通过引入隐含NLI关系的句子对来提升模型性能。
3. 在MISMATCHED基准上，使用预训练的小型和大型语言模型建立的基线表现出宏观F1值为78.17%，显示出显著的改进空间。

## 📝 摘要（中文）

科学自然语言推理（NLI）是预测研究文章中句子对之间语义关系的任务。现有数据集主要来自计算机科学领域，忽略了非计算机科学领域。本文提出了一个新的科学NLI评估基准——MISMATCHED，涵盖心理学、工程学和公共卫生等三个非计算机科学领域，并包含2700对人工标注的句子对。我们在MISMATCHED上建立了强基线，使用预训练的小型语言模型和大型语言模型。最佳基线的宏观F1值为78.17%，显示出未来改进的潜力。此外，研究表明在模型训练中加入具有隐含科学NLI关系的句子对可以提升其性能。我们将数据集和代码公开在GitHub上。

## 🔬 方法详解

**问题定义**：本文旨在解决科学自然语言推理任务中现有数据集的领域偏差问题，尤其是缺乏非计算机科学领域的句子对数据集。

**核心思路**：通过引入MISMATCHED基准，涵盖心理学、工程学和公共卫生等领域的句子对，并在模型训练中加入隐含NLI关系的句子对，以提高模型的推理能力。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要模块。数据集构建阶段涉及人工标注句子对，模型训练阶段使用预训练的小型和大型语言模型，评估阶段则通过宏观F1值来衡量模型性能。

**关键创新**：MISMATCHED基准的提出是本研究的核心创新，填补了科学NLI领域的空白，并通过隐含NLI关系的句子对提升了模型的推理能力。

**关键设计**：在模型训练中，采用了多种预训练语言模型，并通过调整超参数和损失函数来优化模型性能，确保在不同领域的句子对上都能取得良好效果。

## 📊 实验亮点

在MISMATCHED基准上，最佳基线模型的宏观F1值达到了78.17%，显示出在非计算机科学领域的推理能力仍有显著提升空间。这一结果为未来的研究提供了明确的改进方向。

## 🎯 应用场景

该研究的潜在应用领域包括科学文献的自动分析、信息检索和知识图谱构建等。通过提升科学NLI的性能，能够更好地支持科研人员在文献综述、数据挖掘等方面的工作，未来可能对科学研究的效率和准确性产生积极影响。

## 📄 摘要（原文）

> Scientific Natural Language Inference (NLI) is the task of predicting the semantic relation between a pair of sentences extracted from research articles. Existing datasets for this task are derived from various computer science (CS) domains, whereas non-CS domains are completely ignored. In this paper, we introduce a novel evaluation benchmark for scientific NLI, called MISMATCHED. The new MISMATCHED benchmark covers three non-CS domains-PSYCHOLOGY, ENGINEERING, and PUBLIC HEALTH, and contains 2,700 human annotated sentence pairs. We establish strong baselines on MISMATCHED using both Pre-trained Small Language Models (SLMs) and Large Language Models (LLMs). Our best performing baseline shows a Macro F1 of only 78.17% illustrating the substantial headroom for future improvements. In addition to introducing the MISMATCHED benchmark, we show that incorporating sentence pairs having an implicit scientific NLI relation between them in model training improves their performance on scientific NLI. We make our dataset and code publicly available on GitHub.

