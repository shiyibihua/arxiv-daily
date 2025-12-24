---
layout: default
title: Large Language Models for Czech Aspect-Based Sentiment Analysis
---

# Large Language Models for Czech Aspect-Based Sentiment Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07860" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07860v1</a>
  <a href="https://arxiv.org/pdf/2508.07860.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07860v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07860v1', 'Large Language Models for Czech Aspect-Based Sentiment Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jakub Šmíd, Pavel Přibáň, Pavel Král

**分类**: cs.CL

**发布日期**: 2025-08-11

**备注**: Accepted for presentation at the 28th International Conference on Text, Speech and Dialogue (TSD 2025)

---

## 💡 一句话要点

**评估大型语言模型在捷克语基于方面的情感分析中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感分析` `大型语言模型` `捷克语` `基于方面的情感分析` `微调` `自然语言处理` `模型评估`

## 📋 核心要点

1. 现有的情感分析方法在捷克语的基于方面的情感分析任务中表现不足，尤其是在零样本和少样本场景下。
2. 本文通过评估19种大型语言模型，提出了在捷克语ABSA中使用领域特定微调模型的方案，以提高分析准确性。
3. 实验结果显示，微调后的领域特定模型在零样本和少样本设置中优于通用模型，且微调LLMs达到了最先进的性能。

## 📝 摘要（中文）

基于方面的情感分析（ABSA）是一项细粒度的情感分析任务，旨在识别对实体特定方面的情感。尽管大型语言模型（LLMs）在各种自然语言处理任务中表现出色，但其在捷克语ABSA中的能力尚未得到充分探索。本文对19种不同规模和架构的LLMs在捷克语ABSA中的表现进行了全面评估，比较了它们在零样本、少样本和微调场景下的性能。结果表明，针对ABSA微调的小型领域特定模型在零样本和少样本设置中优于通用LLMs，而微调后的LLMs则达到了最先进的结果。我们分析了多语言性、模型规模和新颖性等因素对性能的影响，并进行了错误分析，突出了在方面术语预测中的关键挑战。我们的研究为LLMs在捷克语ABSA中的适用性提供了见解，并为未来的研究提供了指导。

## 🔬 方法详解

**问题定义**：本文旨在解决捷克语基于方面的情感分析（ABSA）中的性能不足问题，尤其是在零样本和少样本场景下，现有方法未能有效捕捉特定方面的情感。

**核心思路**：通过对19种不同规模和架构的LLMs进行评估，提出微调领域特定模型的策略，以提高在捷克语ABSA中的表现，尤其是在数据稀缺的情况下。

**技术框架**：研究采用了零样本、少样本和微调三种场景进行评估，比较不同模型的性能，分析多语言性、模型规模和新颖性对结果的影响。

**关键创新**：最重要的创新在于发现小型领域特定模型在零样本和少样本设置中优于通用LLMs，而微调后的LLMs则在性能上达到了新的高度。

**关键设计**：在实验中，模型的选择、微调策略以及评估指标的设置均经过精心设计，以确保结果的可靠性和可比性。

## 📊 实验亮点

实验结果表明，微调的小型领域特定模型在零样本和少样本设置中表现优于通用LLMs，微调后的LLMs在捷克语ABSA中达到了最先进的结果，具体性能提升幅度未明确给出，但整体表现显著优于基线模型。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体分析、产品评论分析和市场调研等，能够帮助企业和研究者更好地理解消费者对特定产品或服务的情感态度。未来，随着模型的进一步优化和数据集的扩展，该方法有望在更多语言和领域中推广应用。

## 📄 摘要（原文）

> Aspect-based sentiment analysis (ABSA) is a fine-grained sentiment analysis task that aims to identify sentiment toward specific aspects of an entity. While large language models (LLMs) have shown strong performance in various natural language processing (NLP) tasks, their capabilities for Czech ABSA remain largely unexplored. In this work, we conduct a comprehensive evaluation of 19 LLMs of varying sizes and architectures on Czech ABSA, comparing their performance in zero-shot, few-shot, and fine-tuning scenarios. Our results show that small domain-specific models fine-tuned for ABSA outperform general-purpose LLMs in zero-shot and few-shot settings, while fine-tuned LLMs achieve state-of-the-art results. We analyze how factors such as multilingualism, model size, and recency influence performance and present an error analysis highlighting key challenges, particularly in aspect term prediction. Our findings provide insights into the suitability of LLMs for Czech ABSA and offer guidance for future research in this area.

