---
layout: default
title: Do LLMs exhibit the same commonsense capabilities across languages?
---

# Do LLMs exhibit the same commonsense capabilities across languages?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06401" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06401v1</a>
  <a href="https://arxiv.org/pdf/2509.06401.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06401v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06401v1', 'Do LLMs exhibit the same commonsense capabilities across languages?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ivan Martínez-Murillo, Elena Lloret, Paloma Moreda, Albert Gatt

**分类**: cs.CL

**发布日期**: 2025-09-08

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/gplsi)

---

## 💡 一句话要点

**MULTICOM基准测试揭示LLM在多语言常识生成能力上的显著差距**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言常识生成` `大型语言模型` `基准测试` `低资源语言` `自然语言处理`

## 📋 核心要点

1. 现有LLM在多语言常识生成方面存在局限性，尤其是在低资源语言上表现不佳。
2. 论文提出MULTICOM基准，扩展COCOTEROS数据集至四种语言，用于评估LLM的常识生成能力。
3. 实验结果表明，LLM在英语上的表现明显优于其他语言，上下文支持对低资源语言有一定帮助。

## 📝 摘要（中文）

本文探讨了大型语言模型（LLM）的多语言常识生成能力。为了便于研究，我们引入了MULTICOM，这是一个新的基准，它将COCOTEROS数据集扩展到四种语言：英语、西班牙语、荷兰语和瓦伦西亚语。任务包括生成包含给定三个单词的常识性句子。我们评估了一系列开源LLM，包括LLaMA、Qwen、Gemma、EuroLLM和Salamandra。我们的评估结合了自动指标、LLM-as-a-judge方法（使用Prometheus和JudgeLM）以及人工标注。结果始终表明英语的性能优越，而资源较少的语言的性能明显较低。虽然上下文支持产生的结果好坏参半，但它往往有利于代表性不足的语言。这些发现强调了LLM在多语言常识生成方面的当前局限性。该数据集可在https://huggingface.co/datasets/gplsi/MULTICOM公开获取。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM在不同语言环境下常识生成能力不均衡的问题。现有方法主要集中在英语等高资源语言上，忽略了其他语言的常识推理能力，导致LLM在处理多语言任务时表现不佳。

**核心思路**：论文的核心思路是通过构建一个多语言常识生成基准（MULTICOM），来系统地评估LLM在不同语言上的常识推理能力。通过对比LLM在不同语言上的表现，揭示其在多语言常识理解方面的差距。

**技术框架**：整体框架包括数据集构建和模型评估两个主要阶段。数据集构建阶段，作者将COCOTEROS数据集扩展到英语、西班牙语、荷兰语和瓦伦西亚语四种语言。模型评估阶段，作者使用自动指标、LLM-as-a-judge方法（Prometheus和JudgeLM）以及人工标注对LLM进行评估。

**关键创新**：论文的关键创新在于构建了MULTICOM多语言常识生成基准，该基准可以用于评估LLM在不同语言上的常识推理能力。此外，论文还采用了多种评估方法，包括自动指标、LLM-as-a-judge方法和人工标注，从而更全面地评估LLM的性能。

**关键设计**：MULTICOM数据集基于COCOTEROS，包含给定三个单词，要求生成包含这三个单词的常识性句子。评估指标包括自动指标（BLEU, ROUGE等）、LLM-as-a-judge方法（Prometheus, JudgeLM）和人工标注。实验中使用了多种开源LLM，包括LLaMA、Qwen、Gemma、EuroLLM和Salamandra，并分析了上下文信息对生成结果的影响。

## 📊 实验亮点

实验结果表明，LLM在英语上的常识生成能力明显优于其他语言，这表明LLM在多语言常识理解方面存在显著差距。例如，在MULTICOM基准测试中，LLaMA在英语上的表现显著优于西班牙语、荷兰语和瓦伦西亚语。上下文支持对低资源语言的性能提升有一定帮助，但效果并不稳定。

## 🎯 应用场景

该研究成果可应用于提升多语言自然语言处理系统的性能，例如机器翻译、跨语言信息检索和多语言对话系统。通过了解LLM在不同语言上的常识推理能力，可以针对性地改进模型，使其更好地理解和生成不同语言的文本。此外，该研究还可以促进低资源语言的自然语言处理研究。

## 📄 摘要（原文）

> This paper explores the multilingual commonsense generation abilities of Large Language Models (LLMs). To facilitate this investigation, we introduce MULTICOM, a novel benchmark that extends the COCOTEROS dataset to four languages: English, Spanish, Dutch, and Valencian. The task involves generating a commonsensical sentence that includes a given triplet of words. We evaluate a range of open-source LLMs, including LLaMA, Qwen, Gemma, EuroLLM, and Salamandra, on this benchmark. Our evaluation combines automatic metrics, LLM-as-a-judge approaches (using Prometheus and JudgeLM), and human annotations. Results consistently show superior performance in English, with significantly lower performance in less-resourced languages. While contextual support yields mixed results, it tends to benefit underrepresented languages. These findings underscore the current limitations of LLMs in multilingual commonsense generation. The dataset is publicly available at https://huggingface.co/datasets/gplsi/MULTICOM.

