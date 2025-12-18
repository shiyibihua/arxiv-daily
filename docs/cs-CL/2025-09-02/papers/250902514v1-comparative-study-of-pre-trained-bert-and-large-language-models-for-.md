---
layout: default
title: Comparative Study of Pre-Trained BERT and Large Language Models for Code-Mixed Named Entity Recognition
---

# Comparative Study of Pre-Trained BERT and Large Language Models for Code-Mixed Named Entity Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02514" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02514v1</a>
  <a href="https://arxiv.org/pdf/2509.02514.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02514v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02514v1', 'Comparative Study of Pre-Trained BERT and Large Language Models for Code-Mixed Named Entity Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mayur Shirke, Amey Shembade, Pavan Thorat, Madhushri Wagh, Raviraj Joshi

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-02

---

## 💡 一句话要点

**对比研究预训练BERT与大语言模型在Code-Mixed命名实体识别中的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Code-Mixed文本` `命名实体识别` `预训练模型` `Hinglish` `大语言模型`

## 📋 核心要点

1. Code-Mixed文本NER面临非正式结构、音译和频繁语言切换的挑战，现有方法难以有效处理。
2. 论文对比了在Code-Mixed数据上微调的模型、非Code-Mixed多语言模型以及零样本LLM，探究其在Code-Mixed NER任务中的性能。
3. 实验结果表明，在Code-Mixed数据上预训练的模型性能更优，甚至超过了闭源LLM，证明了领域特定预训练的有效性。

## 📝 摘要（中文）

本研究对比评估了在Code-Mixed文本（特别是印地语-英语混合文本Hinglish）上进行命名实体识别(NER)的多种模型，包括在Code-Mixed数据上微调的模型、非Code-Mixed多语言模型以及零样本生成式大语言模型(LLM)。具体而言，我们评估了HingBERT、HingMBERT和HingRoBERTa（在Code-Mixed数据上训练），以及BERT Base Cased、IndicBERT、RoBERTa和MuRIL（在非Code-Mixed多语言数据上训练）。我们还使用去除了NER标签的数据集修改版本，评估了Google Gemini在零样本环境下的性能。所有模型均在基准Hinglish NER数据集上使用精确率、召回率和F1分数进行测试。结果表明，由于领域特定的预训练，Code-Mixed模型（特别是基于HingRoBERTa和HingBERT微调的模型）优于其他模型，包括像Google Gemini这样的闭源LLM。非Code-Mixed模型的表现尚可，但适应性有限。值得注意的是，Google Gemini表现出具有竞争力的零样本性能，突显了现代LLM的泛化能力。本研究为Code-Mixed NER任务中专用模型与通用模型的有效性提供了关键见解。

## 🔬 方法详解

**问题定义**：论文旨在解决Code-Mixed文本（特别是Hinglish）中的命名实体识别问题。现有方法，如通用多语言模型，在处理这种混合语言的非正式文本时，由于缺乏对特定语言混合模式的理解，性能会受到限制。此外，标注数据稀缺也是一个挑战。

**核心思路**：论文的核心思路是通过比较不同类型的预训练模型，包括在Code-Mixed数据上训练的模型和通用多语言模型，来评估它们在Code-Mixed NER任务中的性能。同时，还考察了零样本LLM的性能，以了解其泛化能力。通过这种对比，旨在揭示领域特定预训练对于Code-Mixed NER的重要性。

**技术框架**：整体框架包括以下几个步骤：1) 选择合适的预训练模型，包括HingBERT、HingMBERT、HingRoBERTa、BERT Base Cased、IndicBERT、RoBERTa和MuRIL。2) 对部分模型进行微调，使用Hinglish NER数据集。3) 使用修改后的数据集评估Google Gemini的零样本性能。4) 使用精确率、召回率和F1分数等指标评估所有模型的性能。

**关键创新**：论文的关键创新在于对多种模型在Code-Mixed NER任务中的全面对比评估，特别是对在Code-Mixed数据上预训练的模型和零样本LLM的性能进行了深入分析。这为选择合适的模型以及理解领域特定预训练的重要性提供了有价值的见解。

**关键设计**：论文的关键设计包括：1) 选择了一系列具有代表性的预训练模型，涵盖了在Code-Mixed数据上训练的模型和通用多语言模型。2) 使用了标准的Hinglish NER数据集进行评估，保证了结果的可比性。3) 采用了常用的评估指标，如精确率、召回率和F1分数，对模型的性能进行量化。

## 📊 实验亮点

实验结果表明，在Code-Mixed数据上预训练的模型（如HingRoBERTa和HingBERT）在Hinglish NER任务中表现最佳，优于通用多语言模型和Google Gemini等闭源LLM。这突显了领域特定预训练对于处理Code-Mixed文本的重要性。Google Gemini虽然在零样本设置下表现出竞争力，但仍不如经过微调的Code-Mixed模型。

## 🎯 应用场景

该研究成果可应用于社交媒体分析、客户服务、舆情监控等领域，尤其是在印度等混合语言使用广泛的地区。通过提升Code-Mixed文本的NER准确率，可以更有效地提取关键信息，从而支持更智能的决策和自动化流程。未来，该研究可以扩展到其他Code-Mixed语言对，并探索更先进的模型架构。

## 📄 摘要（原文）

> Named Entity Recognition (NER) in code-mixed text, particularly Hindi-English (Hinglish), presents unique challenges due to informal structure, transliteration, and frequent language switching. This study conducts a comparative evaluation of code-mixed fine-tuned models and non-code-mixed multilingual models, along with zero-shot generative large language models (LLMs). Specifically, we evaluate HingBERT, HingMBERT, and HingRoBERTa (trained on code-mixed data), and BERT Base Cased, IndicBERT, RoBERTa and MuRIL (trained on non-code-mixed multilingual data). We also assess the performance of Google Gemini in a zero-shot setting using a modified version of the dataset with NER tags removed. All models are tested on a benchmark Hinglish NER dataset using Precision, Recall, and F1-score. Results show that code-mixed models, particularly HingRoBERTa and HingBERT-based fine-tuned models, outperform others - including closed-source LLMs like Google Gemini - due to domain-specific pretraining. Non-code-mixed models perform reasonably but show limited adaptability. Notably, Google Gemini exhibits competitive zero-shot performance, underlining the generalization strength of modern LLMs. This study provides key insights into the effectiveness of specialized versus generalized models for code-mixed NER tasks.

