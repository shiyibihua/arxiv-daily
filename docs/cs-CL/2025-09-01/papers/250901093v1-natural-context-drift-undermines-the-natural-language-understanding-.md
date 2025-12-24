---
layout: default
title: Natural Context Drift Undermines the Natural Language Understanding of Large Language Models
---

# Natural Context Drift Undermines the Natural Language Understanding of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01093" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01093v1</a>
  <a href="https://arxiv.org/pdf/2509.01093.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01093v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01093v1', 'Natural Context Drift Undermines the Natural Language Understanding of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yulong Wu, Viktor Schlegel, Riza Batista-Navarro

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-01

**备注**: EMNLP 2025 Findings

---

## 💡 一句话要点

**提出框架分析自然文本演变对LLM问答能力的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言处理` `大语言模型` `问答系统` `文本演变` `语义相似性`

## 📋 核心要点

1. 现有的生成型大语言模型在处理自然演变的文本时表现不佳，尤其是在问答任务中。
2. 论文提出了一种新框架，能够策划和分析自然演变的文本版本，从而评估LLM的表现。
3. 实验显示，LLM的准确率随着文本的自然偏离而显著下降，最高下降幅度超过30%。

## 📝 摘要（中文）

本文探讨了自然演变的上下文段落如何影响生成型大语言模型（LLMs）的问答能力。为此，提出了一种框架，用于策划自然演变的人为编辑版本的阅读段落，并分析LLM在多个语义相似性评分下的表现。实验结果表明，随着阅读段落与预训练版本的自然偏离，LLM的表现显著下降，尽管问题和必要信息在推理时仍然存在。例如，BoolQ的平均模型准确率在最高和最低相似性区间之间下降超过30%。这些发现表明，自然文本演变对LLM的语言理解能力构成了重大挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决生成型大语言模型在面对自然演变文本时的问答能力下降问题。现有方法未能有效应对文本内容的自然变化，导致模型性能受损。

**核心思路**：论文提出的核心思路是构建一个框架，策划自然演变的文本版本，并通过语义相似性评分来评估LLM的表现。这种设计旨在揭示文本演变对模型理解的影响。

**技术框架**：整体架构包括文本版本的策划、语义相似性评分的计算以及LLM性能的评估。主要模块包括数据准备、模型评估和结果分析。

**关键创新**：最重要的技术创新在于提出了一个系统化的框架，能够量化文本演变对LLM性能的影响，与现有方法相比，提供了更细致的分析视角。

**关键设计**：在实验中，使用了六个问答数据集和八个公开可用的LLM，设计了不同的相似性评分区间，以便全面评估模型的表现。

## 📊 实验亮点

实验结果显示，LLM在处理自然演变文本时的准确率显著下降，BoolQ数据集的平均准确率在最高和最低相似性区间之间下降超过30%。多个LLM的表现斜率超过70，表明文本演变对模型理解能力的重大影响。

## 🎯 应用场景

该研究的潜在应用领域包括教育、信息检索和智能问答系统。通过理解自然文本演变对LLM的影响，可以为模型的改进和优化提供指导，提升其在实际应用中的表现和可靠性。

## 📄 摘要（原文）

> How does the natural evolution of context paragraphs affect question answering in generative Large Language Models (LLMs)? To investigate this, we propose a framework for curating naturally evolved, human-edited variants of reading passages from contemporary QA benchmarks and for analyzing LLM performance across a range of semantic similarity scores, which quantify how closely each variant aligns with content seen during pretraining. Using this framework, we evaluate six QA datasets and eight LLMs with publicly available training data. Our experiments reveal that LLM performance declines as reading passages naturally diverge from the versions encountered during pretraining-even when the question and all necessary information remains present at inference time. For instance, average model accuracy on BoolQ drops by over 30% from the highest to lowest similarity bins, with slopes exceeding 70 across several LLMs. These findings suggest that natural text evolution poses a significant challenge to the language understanding capabilities of LLMs.

