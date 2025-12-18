---
layout: default
title: Annotating Training Data for Conditional Semantic Textual Similarity Measurement using Large Language Models
---

# Annotating Training Data for Conditional Semantic Textual Similarity Measurement using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14399" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14399v1</a>
  <a href="https://arxiv.org/pdf/2509.14399.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14399v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14399v1', 'Annotating Training Data for Conditional Semantic Textual Similarity Measurement using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gaifan Zhang, Yi Zhou, Danushka Bollegala

**分类**: cs.CL

**发布日期**: 2025-09-17

**备注**: Accepted to EMNLP 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://LivNLP.github.io/CSTS-reannotation)

---

## 💡 一句话要点

**利用大型语言模型重新标注条件语义文本相似度数据集，提升模型性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `条件语义文本相似度` `大型语言模型` `数据标注` `自然语言处理` `语义理解`

## 📋 核心要点

1. 现有的C-STS数据集存在标注问题，限制了C-STS模型性能的提升，高质量数据集的需求迫切。
2. 利用大型语言模型自动修正条件语句和相似度评分，降低人工标注成本，提高数据质量。
3. 在重新标注的数据集上训练C-STS模型，Spearman相关性显著提升5.4%，验证了方法的有效性。

## 📝 摘要（中文）

本文针对条件语义文本相似度(C-STS)任务中缺乏大规模、高质量标注数据集的问题，提出了一种利用大型语言模型(LLM)重新标注现有C-STS数据集的方法。该方法旨在修正原始数据集中条件语句和相似度评分的错误，从而生成更准确的训练数据。通过在重新标注的数据集上训练监督C-STS模型，实验结果表明，该方法在Spearman相关性指标上取得了5.4%的显著提升。重新标注的数据集已公开。

## 🔬 方法详解

**问题定义**：论文旨在解决条件语义文本相似度(C-STS)任务中训练数据不足且质量不高的问题。现有C-STS数据集存在标注错误，导致模型性能受限。人工重新标注成本高昂，难以满足大规模训练的需求。

**核心思路**：论文的核心思路是利用大型语言模型(LLM)的强大能力，自动对现有的C-STS数据集进行清洗和重新标注。LLM能够理解语义并进行推理，从而修正原始数据集中不准确的条件语句和相似度评分。

**技术框架**：该方法主要包含以下几个阶段：1) 使用LLM分析原始C-STS数据集，识别并修正错误的条件语句。2) 使用LLM根据修正后的条件语句，重新评估句子对之间的相似度，并生成新的相似度评分。3) 将修正后的条件语句和相似度评分与原始句子对组合，生成新的C-STS训练数据集。4) 在新的数据集上训练监督C-STS模型。

**关键创新**：该方法最重要的创新点在于利用LLM自动进行数据标注，显著降低了人工成本，并提高了数据质量。与传统的人工标注相比，LLM能够更快速、更一致地处理大规模数据，并减少人为误差。

**关键设计**：论文中使用了特定的LLM模型（具体模型名称未知），并设计了合适的prompt，引导LLM进行条件语句修正和相似度评分。损失函数和网络结构等技术细节在论文中没有明确说明，属于未知信息。

## 📊 实验亮点

实验结果表明，在重新标注的数据集上训练的C-STS模型，在Spearman相关性指标上取得了5.4%的显著提升。这一结果表明，利用LLM进行数据标注能够有效提高C-STS模型的性能，并验证了该方法的有效性。具体的基线模型和绝对性能数据未知。

## 🎯 应用场景

该研究成果可应用于各种需要理解条件语义相似度的场景，例如信息检索、问答系统、文本摘要和对话生成。通过提高C-STS模型的准确性，可以提升这些应用在特定上下文下的性能，从而提供更精准、更智能的服务。未来，该方法可以推广到其他需要大规模标注的自然语言处理任务中。

## 📄 摘要（原文）

> Semantic similarity between two sentences depends on the aspects considered between those sentences. To study this phenomenon, Deshpande et al. (2023) proposed the Conditional Semantic Textual Similarity (C-STS) task and annotated a human-rated similarity dataset containing pairs of sentences compared under two different conditions. However, Tu et al. (2024) found various annotation issues in this dataset and showed that manually re-annotating a small portion of it leads to more accurate C-STS models. Despite these pioneering efforts, the lack of large and accurately annotated C-STS datasets remains a blocker for making progress on this task as evidenced by the subpar performance of the C-STS models. To address this training data need, we resort to Large Language Models (LLMs) to correct the condition statements and similarity ratings in the original dataset proposed by Deshpande et al. (2023). Our proposed method is able to re-annotate a large training dataset for the C-STS task with minimal manual effort. Importantly, by training a supervised C-STS model on our cleaned and re-annotated dataset, we achieve a 5.4% statistically significant improvement in Spearman correlation. The re-annotated dataset is available at https://LivNLP.github.io/CSTS-reannotation.

