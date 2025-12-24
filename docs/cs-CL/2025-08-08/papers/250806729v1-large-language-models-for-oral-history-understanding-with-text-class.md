---
layout: default
title: Large Language Models for Oral History Understanding with Text Classification and Sentiment Analysis
---

# Large Language Models for Oral History Understanding with Text Classification and Sentiment Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06729" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06729v1</a>
  <a href="https://arxiv.org/pdf/2508.06729.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06729v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06729v1', 'Large Language Models for Oral History Understanding with Text Classification and Sentiment Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Komala Subramanyam Cherukuri, Pranav Abishai Moses, Aisa Sakata, Jiangping Chen, Haihua Chen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-08

**🔗 代码/项目**: [GITHUB](https://github.com/kc6699c/LLM4OralHistoryAnalysis)

---

## 💡 一句话要点

**提出可扩展框架以自动化日裔美国人监禁口述历史的情感与语义标注**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `口述历史` `情感分析` `语义标注` `大型语言模型` `文化敏感性` `数据集构建` `提示工程`

## 📋 核心要点

1. 现有方法在处理口述历史档案时面临非结构化格式和高标注成本的挑战，限制了大规模分析的可能性。
2. 本文提出了一种多阶段的方法，结合专家标注、提示设计和LLM评估，以实现口述历史的自动化情感与语义标注。
3. 实验结果显示，ChatGPT在语义分类任务中取得了88.71%的F1分数，表明LLMs在大规模口述历史分析中的有效性。

## 📝 摘要（中文）

口述历史是记录生活经历的重要资料，尤其是在经历系统性不公与历史抹除的社区中。有效分析这些口述历史档案有助于促进对其的理解。然而，由于其非结构化格式、情感复杂性和高昂的标注成本，大规模分析仍然有限。本文提出了一种可扩展框架，利用大型语言模型（LLMs）自动化日裔美国人监禁口述历史的语义和情感标注。通过构建高质量数据集、评估多种模型及测试提示工程策略，研究表明LLMs在文化敏感的档案分析中表现出色，并提供了可重用的标注管道和实际指导。

## 🔬 方法详解

**问题定义**：本文旨在解决日裔美国人监禁口述历史档案的情感与语义标注问题。现有方法在处理非结构化数据时面临高昂的标注成本和情感复杂性，限制了其分析能力。

**核心思路**：通过构建高质量的数据集并利用大型语言模型（LLMs），结合专家标注和提示设计，自动化口述历史的情感与语义标注，以提高分析效率和准确性。

**技术框架**：整体框架包括数据集构建、模型评估和提示工程三个主要模块。首先，标注558个句子用于情感和语义分类；其次，评估不同模型的性能；最后，优化提示配置以标注更大规模的句子。

**关键创新**：本研究的创新在于将LLMs应用于文化敏感的档案分析，并通过精心设计的提示提高了模型的标注效果。这一方法在处理复杂情感和语义时展现了显著的优势。

**关键设计**：在实验中，使用了零-shot、few-shot和RAG策略进行模型评估，ChatGPT、Llama和Qwen的性能进行了比较，最终确定了最佳的提示配置以标注92191个句子。

## 📊 实验亮点

实验结果显示，ChatGPT在语义分类任务中取得了88.71%的F1分数，Llama在情感分析中稍微优于其他模型，达到82.66%。所有模型在各自任务中表现出相似的效果，表明LLMs在口述历史分析中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括文化遗产保护、历史研究和社会科学等。通过提供可扩展的标注管道，研究为口述历史的分析提供了新的方法，促进了对历史记忆的理解与保存，具有重要的社会价值和学术意义。

## 📄 摘要（原文）

> Oral histories are vital records of lived experience, particularly within communities affected by systemic injustice and historical erasure. Effective and efficient analysis of their oral history archives can promote access and understanding of the oral histories. However, Large-scale analysis of these archives remains limited due to their unstructured format, emotional complexity, and high annotation costs. This paper presents a scalable framework to automate semantic and sentiment annotation for Japanese American Incarceration Oral History. Using LLMs, we construct a high-quality dataset, evaluate multiple models, and test prompt engineering strategies in historically sensitive contexts. Our multiphase approach combines expert annotation, prompt design, and LLM evaluation with ChatGPT, Llama, and Qwen. We labeled 558 sentences from 15 narrators for sentiment and semantic classification, then evaluated zero-shot, few-shot, and RAG strategies. For semantic classification, ChatGPT achieved the highest F1 score (88.71%), followed by Llama (84.99%) and Qwen (83.72%). For sentiment analysis, Llama slightly outperformed Qwen (82.66%) and ChatGPT (82.29%), with all models showing comparable results. The best prompt configurations were used to annotate 92,191 sentences from 1,002 interviews in the JAIOH collection. Our findings show that LLMs can effectively perform semantic and sentiment annotation across large oral history collections when guided by well-designed prompts. This study provides a reusable annotation pipeline and practical guidance for applying LLMs in culturally sensitive archival analysis. By bridging archival ethics with scalable NLP techniques, this work lays the groundwork for responsible use of artificial intelligence in digital humanities and preservation of collective memory. GitHub: https://github.com/kc6699c/LLM4OralHistoryAnalysis.

