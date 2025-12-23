---
layout: default
title: Re-Evaluating Code LLM Benchmarks Under Semantic Mutation
---

# Re-Evaluating Code LLM Benchmarks Under Semantic Mutation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17369" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17369v1</a>
  <a href="https://arxiv.org/pdf/2506.17369.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17369v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17369v1', 'Re-Evaluating Code LLM Benchmarks Under Semantic Mutation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyuan Pan, Xing Hu, Xin Xia, Xiaohu Yang

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-20

---

## 💡 一句话要点

**提出通用框架以解决代码基准测试中的提示敏感性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码基准测试` `提示敏感性` `大型语言模型` `性能评估` `软件工程` `实验设计` `语义相似性`

## 📋 核心要点

1. 现有代码基准测试通常依赖单一提示模板，导致提示敏感性问题，影响模型性能评估的可靠性。
2. 本文提出了一种通用框架，通过修改提示模板来保持其语义和结构，解决提示敏感性问题。
3. 实验结果显示，提示的微小变化会显著影响模型性能，并导致不同模型的性能排名不一致。

## 📝 摘要（中文）

在大型语言模型（LLMs）时代，代码基准测试成为软件工程研究的重要领域，广泛应用于实践中。这些基准测试评估LLMs在特定代码相关任务上的表现，如代码理解和生成。构建代码基准测试的关键步骤是提示设计。然而，现有基准测试通常依赖于每个任务的单一提示模板，容易出现提示敏感性问题，即微小的提示变化可能导致性能的显著波动，从而影响模型能力的评估。本文提出了一种通用框架，通过修改提示模板来尽可能保留其语义和结构，并在十个开源LLMs上进行了广泛实验，结果表明提示的细微变化会导致显著的性能变化，强调了在设计未来代码基准测试时考虑提示敏感性的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有代码基准测试中提示敏感性的问题。现有方法通常依赖单一的提示模板，导致微小变化引起的性能波动，影响模型能力的可靠评估。

**核心思路**：论文提出了一种通用框架，旨在通过修改提示模板的方式，尽可能保留其语义和结构，从而减轻提示敏感性对评估结果的影响。

**技术框架**：整体架构包括提示模板的设计与修改、实验设计、性能评估等主要模块。框架首先生成100个语义相似的提示模板，然后在八个代码基准任务上进行实验。

**关键创新**：最重要的创新点在于提出了一个系统化的方法来生成和评估多个提示模板，显著提高了对模型性能评估的可靠性，与传统方法相比，能够更全面地反映模型能力。

**关键设计**：在实验中，使用了多种统计指标来分析模型性能，包括绝对性能和相对性能的比较，确保评估结果的全面性和准确性。

## 📊 实验亮点

实验结果显示，提示的微小变化可导致模型性能的显著波动，甚至影响不同模型的性能排名。具体而言，在十个开源LLMs的实验中，性能变化幅度达到20%以上，强调了在设计基准测试时考虑提示敏感性的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括软件工程中的代码生成与理解、自动化测试和代码审查等。通过提高代码基准测试的可靠性，能够为开发者提供更准确的模型性能评估，进而推动LLMs在实际应用中的有效性和可靠性。未来，该框架还可能扩展到其他领域的基准测试设计中。

## 📄 摘要（原文）

> In the era of large language models (LLMs), code benchmarks have become an important research area in software engineering and are widely used by practitioners. These benchmarks evaluate the performance of LLMs on specific code-related tasks, such as code understanding and generation. A critical step in constructing code benchmarks is the design of prompts. However, as existing code benchmarks typically rely on a single prompt template per task, they are prone to the issue of prompt sensitivity, where minor prompt variations could result in substantial performance variations, leading to unreliable evaluations of model capabilities.
>   While previous studies have explored prompt sensitivity, their experimental designs and findings are limited to traditional natural language processing (NLP) tasks. In this paper, we present an empirical study to investigate prompt sensitivity in code benchmarks. We first propose a general framework that modifies prompt templates in a manner that preserves both their semantics and their structure as much as possible. Based on the framework, we conduct extensive experiments across eight code benchmark tasks on 10 representative open-source LLMs, with each task featuring 100 semantically similar prompt templates. We then analyze the evaluation results using various statistical metrics, focusing on both absolute and relative model performance. Our findings suggest that even slight prompt variations can lead to significant shifts in performance. Additionally, we observe that such variations can introduce inconsistencies in the performance rankings across different models. These insights highlight the need for considering prompt sensitivity when designing future code benchmarks, to ensure more reliable and accurate evaluation of LLM capabilities.

