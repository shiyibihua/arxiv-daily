---
layout: default
title: Leveraging Language Models and Machine Learning in Verbal Autopsy Analysis
---

# Leveraging Language Models and Machine Learning in Verbal Autopsy Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19274" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19274v1</a>
  <a href="https://arxiv.org/pdf/2508.19274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19274v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19274v1', 'Leveraging Language Models and Machine Learning in Verbal Autopsy Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Chu

**分类**: cs.CL

**发布日期**: 2025-08-22

**备注**: Ph.D. dissertation submitted to The Ohio State University, August 2025

---

## 💡 一句话要点

**利用语言模型和机器学习提升口述尸检分析的准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `口述尸检` `死亡原因分类` `预训练语言模型` `机器学习` `多模态融合` `公共卫生` `流行病学`

## 📋 核心要点

1. 现有的自动化口述尸检死亡原因分类算法仅依赖于结构化问题，忽略了非结构化叙述中的重要信息，导致分类准确性不足。
2. 本文提出利用预训练语言模型和机器学习技术，充分挖掘口述尸检中的叙述信息，以提升死亡原因分类的准确性。
3. 实验结果表明，基于叙述的变换器模型在个体和群体层面上均优于现有的仅基于问题的算法，特别是在非传染性疾病的识别上表现突出。

## 📝 摘要（中文）

在缺乏民事登记和生命统计数据的国家，口述尸检（VA）是估计死亡原因（COD）和指导政策优先事项的重要工具。现有的自动化VA死亡原因分类算法仅使用问题而忽略叙述中的信息。本文研究了如何利用预训练语言模型（PLMs）和机器学习（ML）技术，通过南非的实证数据，证明仅使用叙述的情况下，基于变换器的PLMs经过任务特定微调后在个体和群体层面上超越了现有的仅基于问题的算法，特别是在识别非传染性疾病方面。我们还探讨了将叙述和问题结合的多模态融合策略，进一步提升了COD分类的性能，确认了每种模态的独特贡献。整体而言，本文推动了自然语言处理、流行病学和全球健康交叉领域的知识发展，强调了叙述在提升COD分类中的价值。

## 🔬 方法详解

**问题定义**：本文旨在解决现有口述尸检死亡原因分类算法未能充分利用叙述信息的问题。现有方法仅依赖于结构化问题，导致分类准确性不足。

**核心思路**：通过使用预训练语言模型（PLMs）和机器学习技术，充分挖掘口述尸检中的叙述信息，以实现更精准的死亡原因分类。

**技术框架**：整体架构包括数据收集、叙述信息提取、模型训练和评估等主要模块。首先收集南非的口述尸检数据，然后利用变换器模型进行任务特定的微调，最后评估模型在分类任务中的表现。

**关键创新**：最重要的技术创新在于将叙述信息与结构化问题结合，采用多模态融合策略，显著提升了分类性能。这一方法与传统的仅依赖问题的算法本质上不同，能够捕捉到更丰富的信息。

**关键设计**：在模型设计中，采用了变换器架构，并进行了任务特定的微调。损失函数的选择和参数设置经过精心调整，以确保模型在分类任务中的最佳表现。

## 📊 实验亮点

实验结果显示，基于叙述的变换器模型在死亡原因分类任务中，准确率超过了现有的仅基于问题的算法，特别是在识别非传染性疾病方面，表现出显著的提升幅度，具体数据未提供。

## 🎯 应用场景

该研究的潜在应用领域包括公共卫生、流行病学研究和政策制定。通过提升口述尸检的死亡原因分类准确性，可以为卫生政策的制定提供更可靠的数据支持，进而改善全球健康状况。未来，该方法有望在其他缺乏民事登记的国家和地区推广应用。

## 📄 摘要（原文）

> In countries without civil registration and vital statistics, verbal autopsy (VA) is a critical tool for estimating cause of death (COD) and inform policy priorities. In VA, interviewers ask proximal informants for details on the circumstances preceding a death, in the form of unstructured narratives and structured questions. Existing automated VA cause classification algorithms only use the questions and ignore the information in the narratives. In this thesis, we investigate how the VA narrative can be used for automated COD classification using pretrained language models (PLMs) and machine learning (ML) techniques. Using empirical data from South Africa, we demonstrate that with the narrative alone, transformer-based PLMs with task-specific fine-tuning outperform leading question-only algorithms at both the individual and population levels, particularly in identifying non-communicable diseases. We explore various multimodal fusion strategies combining narratives and questions in unified frameworks. Multimodal approaches further improve performance in COD classification, confirming that each modality has unique contributions and may capture valuable information that is not present in the other modality. We also characterize physician-perceived information sufficiency in VA. We describe variations in sufficiency levels by age and COD and demonstrate that classification accuracy is affected by sufficiency for both physicians and models. Overall, this thesis advances the growing body of knowledge at the intersection of natural language processing, epidemiology, and global health. It demonstrates the value of narrative in enhancing COD classification. Our findings underscore the need for more high-quality data from more diverse settings to use in training and fine-tuning PLM/ML methods, and offer valuable insights to guide the rethinking and redesign of the VA instrument and interview.

