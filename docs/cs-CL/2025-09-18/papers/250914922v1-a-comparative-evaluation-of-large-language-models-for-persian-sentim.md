---
layout: default
title: A Comparative Evaluation of Large Language Models for Persian Sentiment Analysis and Emotion Detection in Social Media Texts
---

# A Comparative Evaluation of Large Language Models for Persian Sentiment Analysis and Emotion Detection in Social Media Texts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14922" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14922v1</a>
  <a href="https://arxiv.org/pdf/2509.14922.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14922v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14922v1', 'A Comparative Evaluation of Large Language Models for Persian Sentiment Analysis and Emotion Detection in Social Media Texts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kian Tohidi, Kia Dashtipour, Simone Rebora, Sevda Pourfaramarz

**分类**: cs.CL

**发布日期**: 2025-09-18

**备注**: 19 pages, 8 Figures, 9 Tables

---

## 💡 一句话要点

**对比评估大型语言模型在波斯语社交媒体文本情感分析与情绪检测中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `情感分析` `情绪检测` `波斯语` `社交媒体文本`

## 📋 核心要点

1. 现有大型语言模型在跨语言情感分析和情绪检测方面的性能评估不足，尤其缺乏对波斯语的研究。
2. 该研究通过在平衡的波斯语数据集上，使用统一的提示和参数，对四种先进LLM进行直接和公平的比较。
3. 实验结果表明，所有模型均达到可接受的性能水平，GPT-4o准确率略高，Gemini 2.0 Flash成本效益最佳。

## 📝 摘要（中文）

本研究对四种先进的大型语言模型（LLMs）——Claude 3.7 Sonnet、DeepSeek-V3、Gemini 2.0 Flash 和 GPT-4o——在波斯语社交媒体文本情感分析和情绪检测方面的性能进行了全面的对比评估。近年来，LLMs之间的对比分析显著增加，但大多数分析都是在英语语言任务上进行的，导致对跨语言性能模式的理解存在差距。本研究通过严格的实验设计来解决这些差距，使用了包含900个文本的情感分析（积极、消极、中性）和1800个文本的情绪检测（愤怒、恐惧、快乐、仇恨、悲伤、惊讶）的平衡波斯语数据集。主要重点是通过使用一致的提示、统一的处理参数以及分析精度、召回率、F1分数等性能指标以及错误分类模式，从而实现不同模型之间的直接和公平的比较。结果表明，所有模型都达到了可接受的性能水平，并且对最佳三个模型的统计比较表明它们之间没有显着差异。然而，GPT-4o在两项任务中都表现出略高的原始准确度值，而Gemini 2.0 Flash被证明是最具成本效益的。研究结果表明，与情感分析任务相比，情绪检测任务对所有模型都更具挑战性，并且错误分类模式可能代表波斯语文本中的一些挑战。这些发现为波斯语NLP应用建立了性能基准，并为基于准确性、效率和成本考虑因素的模型选择提供了实用指导，同时揭示了在多语言AI系统部署中需要考虑的文化和语言挑战。

## 🔬 方法详解

**问题定义**：论文旨在评估大型语言模型在波斯语社交媒体文本情感分析和情绪检测任务中的性能。现有方法主要集中在英语等高资源语言上，缺乏对波斯语等低资源语言的深入研究，导致跨语言性能模式理解不足。此外，不同模型之间的公平比较也面临挑战，需要统一的评估标准和数据集。

**核心思路**：论文的核心思路是通过构建平衡的波斯语数据集，并采用统一的提示和处理参数，对四种先进的大型语言模型进行直接和公平的比较。通过分析模型的性能指标和错误分类模式，揭示模型在波斯语情感分析和情绪检测任务中的优势和不足，为实际应用提供指导。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 构建平衡的波斯语数据集，包含情感分析和情绪检测任务的数据；2) 选择四种先进的大型语言模型：Claude 3.7 Sonnet、DeepSeek-V3、Gemini 2.0 Flash 和 GPT-4o；3) 使用统一的提示和处理参数，对模型进行微调或零样本推理；4) 评估模型的性能指标，包括精度、召回率、F1分数和准确率；5) 分析模型的错误分类模式，揭示模型在波斯语处理中的挑战。

**关键创新**：该研究的关键创新在于：1) 针对波斯语情感分析和情绪检测任务，构建了平衡且高质量的数据集；2) 对比评估了多种先进的大型语言模型，并提供了详细的性能分析；3) 揭示了模型在波斯语处理中的挑战，为未来的研究提供了方向。与现有方法相比，该研究更加注重跨语言性能的评估和模型之间的公平比较。

**关键设计**：该研究的关键设计包括：1) 数据集的平衡性，确保不同类别的数据量相近，避免模型偏向；2) 提示的设计，采用清晰简洁的提示，引导模型进行情感分析和情绪检测；3) 评估指标的选择，综合考虑精度、召回率和F1分数，全面评估模型的性能；4) 错误分类模式的分析，深入了解模型在波斯语处理中的挑战。

## 📊 实验亮点

实验结果表明，所有模型均达到可接受的性能水平。GPT-4o在情感分析和情绪检测任务中均表现出略高的原始准确度值，但与DeepSeek-V3和Claude 3.7 Sonnet的统计比较没有显著差异。Gemini 2.0 Flash在成本效益方面表现最佳。情绪检测任务对所有模型来说都比情感分析任务更具挑战性。

## 🎯 应用场景

该研究成果可应用于波斯语社交媒体舆情监控、用户情感分析、智能客服等领域。通过选择合适的模型，可以提高波斯语文本情感分析和情绪检测的准确性和效率，从而更好地理解用户需求，提升服务质量。此外，该研究也为多语言AI系统的开发和部署提供了参考。

## 📄 摘要（原文）

> This study presents a comprehensive comparative evaluation of four state-of-the-art Large Language Models (LLMs)--Claude 3.7 Sonnet, DeepSeek-V3, Gemini 2.0 Flash, and GPT-4o--for sentiment analysis and emotion detection in Persian social media texts. Comparative analysis among LLMs has witnessed a significant rise in recent years, however, most of these analyses have been conducted on English language tasks, creating gaps in understanding cross-linguistic performance patterns. This research addresses these gaps through rigorous experimental design using balanced Persian datasets containing 900 texts for sentiment analysis (positive, negative, neutral) and 1,800 texts for emotion detection (anger, fear, happiness, hate, sadness, surprise). The main focus was to allow for a direct and fair comparison among different models, by using consistent prompts, uniform processing parameters, and by analyzing the performance metrics such as precision, recall, F1-scores, along with misclassification patterns. The results show that all models reach an acceptable level of performance, and a statistical comparison of the best three models indicates no significant differences among them. However, GPT-4o demonstrated a marginally higher raw accuracy value for both tasks, while Gemini 2.0 Flash proved to be the most cost-efficient. The findings indicate that the emotion detection task is more challenging for all models compared to the sentiment analysis task, and the misclassification patterns can represent some challenges in Persian language texts. These findings establish performance benchmarks for Persian NLP applications and offer practical guidance for model selection based on accuracy, efficiency, and cost considerations, while revealing cultural and linguistic challenges that require consideration in multilingual AI system deployment.

