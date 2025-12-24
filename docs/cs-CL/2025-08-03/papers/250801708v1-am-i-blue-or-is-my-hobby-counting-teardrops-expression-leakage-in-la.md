---
layout: default
title: Am I Blue or Is My Hobby Counting Teardrops? Expression Leakage in Large Language Models as a Symptom of Irrelevancy Disruption
---

# Am I Blue or Is My Hobby Counting Teardrops? Expression Leakage in Large Language Models as a Symptom of Irrelevancy Disruption

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01708" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01708v1</a>
  <a href="https://arxiv.org/pdf/2508.01708.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01708v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01708v1', 'Am I Blue or Is My Hobby Counting Teardrops? Expression Leakage in Large Language Models as a Symptom of Irrelevancy Disruption')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Berkay Köprü, Mehrzad Mashal, Yigit Gurses, Akos Kadar, Maximilian Schmitt, Ditty Mathew, Felix Burkhardt, Florian Eyben, Björn W. Schuller

**分类**: cs.CL

**发布日期**: 2025-08-03

---

## 💡 一句话要点

**提出表达泄漏概念以解决大语言模型的无关信息干扰问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `表达泄漏` `情感分析` `自然语言处理` `模型评估` `无关信息干扰`

## 📋 核心要点

1. 现有研究主要集中在语义泄漏上，未能充分探讨大语言模型生成的情感表达与输入上下文的相关性问题。
2. 本文提出了表达泄漏的概念，并通过构建基准数据集和自动评估管道来分析这一现象，旨在提高模型的生成质量。
3. 实验结果显示，随着模型规模的扩大，表达泄漏现象有所减少，但负面情感的影响更为显著，提示模型构建需特别关注这一问题。

## 📝 摘要（中文）

大语言模型（LLMs）在自然语言处理（NLP）方面取得了显著进展，但其整合广泛上下文的能力使其容易引入无关信息。本文引入了表达泄漏这一新现象，指LLMs系统性生成与输入上下文语义无关的情感表达。为分析表达泄漏，作者收集了基准数据集，并提出了一种自动评估管道，与人类判断高度相关。实验表明，随着模型参数规模的增加，同一LLM家族中的表达泄漏现象有所减少，但在模型构建过程中需要特别关注以减轻表达泄漏，提示无法有效缓解此问题。此外，负面情感的注入对生成过程的干扰程度高于正面情感，导致更高的表达泄漏率。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在生成过程中引入与上下文无关的情感表达的问题。现有方法主要关注语义泄漏，未能深入探讨情感表达的相关性。

**核心思路**：论文提出了表达泄漏这一新概念，强调在生成过程中情感表达的无关性，并通过构建基准数据集和自动评估管道来进行分析和验证。

**技术框架**：整体架构包括数据集的构建、表达泄漏的分析和自动评估管道。数据集通过从公共网络抓取自由文本生成，评估管道则与人类判断高度相关，能够加速基准测试。

**关键创新**：最重要的技术创新在于引入了表达泄漏的概念，并提出了一种新的评估方法，能够有效识别和量化这一现象，与传统的语义泄漏分析方法有本质区别。

**关键设计**：在模型构建过程中，特别关注参数设置和训练过程，以减轻表达泄漏现象。实验表明，负面情感的注入对生成过程的干扰程度高于正面情感，需在模型设计时加以考虑。

## 📊 实验亮点

实验结果显示，随着模型参数的增加，表达泄漏现象在同一LLM家族中有所减少。负面情感的注入导致的表达泄漏率显著高于正面情感，提示在模型构建过程中需特别关注情感的影响。

## 🎯 应用场景

该研究的潜在应用领域包括情感分析、对话系统和内容生成等。通过减轻表达泄漏，能够提高大语言模型在实际应用中的生成质量和用户体验，未来可能对人机交互和自动化写作等领域产生深远影响。

## 📄 摘要（原文）

> Large language models (LLMs) have advanced natural language processing (NLP) skills such as through next-token prediction and self-attention, but their ability to integrate broad context also makes them prone to incorporating irrelevant information. Prior work has focused on semantic leakage, bias introduced by semantically irrelevant context. In this paper, we introduce expression leakage, a novel phenomenon where LLMs systematically generate sentimentally charged expressions that are semantically unrelated to the input context. To analyse the expression leakage, we collect a benchmark dataset along with a scheme to automatically generate a dataset from free-form text from common-crawl. In addition, we propose an automatic evaluation pipeline that correlates well with human judgment, which accelerates the benchmarking by decoupling from the need of annotation for each analysed model. Our experiments show that, as the model scales in the parameter space, the expression leakage reduces within the same LLM family. On the other hand, we demonstrate that expression leakage mitigation requires specific care during the model building process, and cannot be mitigated by prompting. In addition, our experiments indicate that, when negative sentiment is injected in the prompt, it disrupts the generation process more than the positive sentiment, causing a higher expression leakage rate.

