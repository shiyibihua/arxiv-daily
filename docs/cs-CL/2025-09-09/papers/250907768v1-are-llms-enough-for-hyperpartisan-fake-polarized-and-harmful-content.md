---
layout: default
title: Are LLMs Enough for Hyperpartisan, Fake, Polarized and Harmful Content Detection? Evaluating In-Context Learning vs. Fine-Tuning
---

# Are LLMs Enough for Hyperpartisan, Fake, Polarized and Harmful Content Detection? Evaluating In-Context Learning vs. Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07768" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07768v1</a>
  <a href="https://arxiv.org/pdf/2509.07768.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07768v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07768v1', 'Are LLMs Enough for Hyperpartisan, Fake, Polarized and Harmful Content Detection? Evaluating In-Context Learning vs. Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Michele Joshua Maggini, Dhia Merzougui, Rabiraj Bandyopadhyay, Gaël Dias, Fabrice Maurel, Pablo Gamallo

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-09

---

## 💡 一句话要点

**对比In-Context Learning与微调，评估大语言模型在检测有害内容方面的能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `有害内容检测` `In-Context Learning` `微调` `多语言处理`

## 📋 核心要点

1. 在线平台上的虚假新闻、极化和有害内容泛滥，现有方法缺乏对不同模型、使用方法和语言的全面基准测试。
2. 本文对比了微调和In-Context Learning两种范式，探索大语言模型在检测有害内容方面的能力，并分析了不同提示策略的影响。
3. 实验结果表明，在检测有害内容方面，微调模型通常优于In-Context Learning，即使是较小的模型，也胜过大型模型。

## 📝 摘要（中文）

本文全面评估了不同大语言模型在检测网络平台上的虚假新闻、极化内容、政治偏见和有害内容方面的性能。研究涵盖了10个数据集和5种语言（英语、西班牙语、葡萄牙语、阿拉伯语和保加利亚语），包括二元和多类分类场景。实验对比了参数高效的微调方法和各种In-Context Learning策略，包括零样本提示、代码本、少样本（使用行列式点过程随机选择和多样性选择）和思维链。研究发现，In-Context Learning通常不如微调模型。这一主要发现强调了即使与LlaMA3.1-8b-Instruct、Mistral-Nemo-Instruct-2407和Qwen2.5-7B-Instruct等大型模型相比，在特定任务上微调较小模型的重要性。

## 🔬 方法详解

**问题定义**：论文旨在解决在线平台上虚假新闻、政治偏见、极化和有害内容的自动检测问题。现有方法，特别是依赖大型语言模型的方法，缺乏跨模型、跨语言和跨使用方法的系统性评估，难以确定最佳实践。

**核心思路**：论文的核心思路是通过对比In-Context Learning和参数高效的微调两种范式，来评估大语言模型在检测有害内容方面的有效性。通过在多种语言和数据集上进行实验，旨在揭示哪种方法更适合于此类任务，并为未来的研究提供指导。

**技术框架**：整体框架包括数据收集、模型选择、方法实现和结果分析四个主要阶段。首先，收集涵盖不同语言和有害内容类型的多个数据集。然后，选择一系列大语言模型，包括LlaMA3.1-8b-Instruct、Mistral-Nemo-Instruct-2407和Qwen2.5-7B-Instruct。接着，实现In-Context Learning和微调两种方法，并采用不同的提示策略（如零样本、少样本、思维链）。最后，对实验结果进行分析和比较，评估不同方法的性能。

**关键创新**：论文的关键创新在于对In-Context Learning和微调进行了全面的对比评估，涵盖了多种语言、数据集和模型。此外，论文还探索了不同的提示策略对In-Context Learning性能的影响，并使用了行列式点过程来选择具有多样性的少样本示例。

**关键设计**：在In-Context Learning中，使用了零样本提示、代码本、少样本（随机选择和行列式点过程选择）和思维链等策略。在微调中，采用了参数高效的微调方法，以减少计算成本。实验中，使用了不同的评估指标，如准确率、精确率、召回率和F1值，以全面评估模型的性能。

## 📊 实验亮点

实验结果表明，在大多数情况下，微调模型优于In-Context Learning。即使是较小的微调模型，也能够胜过大型的In-Context Learning模型，例如LlaMA3.1-8b-Instruct、Mistral-Nemo-Instruct-2407和Qwen2.5-7B-Instruct。这一发现强调了在特定任务上微调模型的重要性。

## 🎯 应用场景

该研究成果可应用于在线内容审核、社交媒体监控、舆情分析等领域。通过自动检测有害内容，可以有效减少虚假信息的传播，维护网络空间的健康生态。未来的研究可以进一步探索如何结合In-Context Learning和微调的优势，开发更高效、更鲁棒的有害内容检测系统。

## 📄 摘要（原文）

> The spread of fake news, polarizing, politically biased, and harmful content on online platforms has been a serious concern. With large language models becoming a promising approach, however, no study has properly benchmarked their performance across different models, usage methods, and languages. This study presents a comprehensive overview of different Large Language Models adaptation paradigms for the detection of hyperpartisan and fake news, harmful tweets, and political bias. Our experiments spanned 10 datasets and 5 different languages (English, Spanish, Portuguese, Arabic and Bulgarian), covering both binary and multiclass classification scenarios. We tested different strategies ranging from parameter efficient Fine-Tuning of language models to a variety of different In-Context Learning strategies and prompts. These included zero-shot prompts, codebooks, few-shot (with both randomly-selected and diversely-selected examples using Determinantal Point Processes), and Chain-of-Thought. We discovered that In-Context Learning often underperforms when compared to Fine-Tuning a model. This main finding highlights the importance of Fine-Tuning even smaller models on task-specific settings even when compared to the largest models evaluated in an In-Context Learning setup - in our case LlaMA3.1-8b-Instruct, Mistral-Nemo-Instruct-2407 and Qwen2.5-7B-Instruct.

