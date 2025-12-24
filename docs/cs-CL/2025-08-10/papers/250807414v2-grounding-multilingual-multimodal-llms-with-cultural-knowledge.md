---
layout: default
title: Grounding Multilingual Multimodal LLMs With Cultural Knowledge
---

# Grounding Multilingual Multimodal LLMs With Cultural Knowledge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07414" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07414v2</a>
  <a href="https://arxiv.org/pdf/2508.07414.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07414v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07414v2', 'Grounding Multilingual Multimodal LLMs With Cultural Knowledge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jean de Dieu Nyandwi, Yueqi Song, Simran Khanuja, Graham Neubig

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-10 (更新: 2025-08-12)

---

## 💡 一句话要点

**提出文化知识驱动的多语言多模态LLM以解决文化差距问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `文化知识` `视觉问答` `多语言处理` `知识图谱` `模型训练` `跨文化交流`

## 📋 核心要点

1. 现有的多模态大型语言模型在处理低资源语言和长尾文化实体时表现不佳，导致文化差距问题。
2. 本文提出了一种数据中心的方法，通过构建CulturalGround数据集，将多语言多模态LLM与文化知识直接结合。
3. CulturalPangea模型在文化聚焦的多语言多模态基准测试中表现优异，平均提升5.0，且未影响主流任务的性能。

## 📝 摘要（中文）

多模态大型语言模型在高资源环境中表现优异，但在处理长尾文化实体和低资源语言时常常出现误解。为了解决这一问题，本文提出了一种以数据为中心的方法，直接将多语言多模态LLM（MLLM）与文化知识相结合。通过利用Wikidata的大规模知识图谱，收集代表文化重要实体的图像，并生成合成的多语言视觉问答数据。最终构建的CulturalGround数据集包含2200万对高质量、文化丰富的视觉问答对，覆盖42个国家和39种语言。基于CulturalGround训练的开源MLLM CulturalPangea在多个文化聚焦的多语言多模态基准测试中实现了最先进的性能，平均提升5.0，同时在主流视觉-语言任务上未出现性能下降。研究结果表明，针对性的文化知识驱动方法能够显著缩小MLLM中的文化差距，为全球包容性多模态系统提供了实际路径。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大型语言模型在低资源语言和长尾文化实体处理中的误解问题，现有方法在这些领域表现不足，导致文化差距加大。

**核心思路**：通过构建一个包含丰富文化知识的视觉问答数据集CulturalGround，直接将多语言多模态LLM与文化知识相结合，以提升模型在文化相关任务中的表现。

**技术框架**：整体架构包括数据收集、知识图谱构建、合成数据生成和模型训练四个主要模块。首先，从Wikidata中提取文化实体信息，然后收集相应的图像，生成视觉问答对，最后使用这些数据训练CulturalPangea模型。

**关键创新**：最重要的创新在于通过文化知识图谱直接增强多语言多模态LLM的训练，填补了现有模型在文化理解上的空白，与传统方法相比，提供了更为精准的文化语境理解。

**关键设计**：在数据集构建中，采用了高质量的图像和多样化的语言对，以确保数据的丰富性和代表性；在模型训练中，结合了标准的多语言指令调优数据，以保持模型的通用能力。

## 📊 实验亮点

CulturalPangea模型在文化聚焦的多语言多模态基准测试中实现了最先进的性能，平均提升5.0，超越了之前的模型，同时在主流视觉-语言任务上保持了性能稳定，显示出该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括跨文化交流、教育、旅游和社交媒体等。通过提升多模态LLM在文化理解上的能力，可以更好地服务于全球用户，促进文化间的理解与交流，推动多模态系统的全球包容性发展。

## 📄 摘要（原文）

> Multimodal Large Language Models excel in high-resource settings, but often misinterpret long-tail cultural entities and underperform in low-resource languages. To address this gap, we propose a data-centric approach that directly grounds MLLMs in cultural knowledge. Leveraging a large scale knowledge graph from Wikidata, we collect images that represent culturally significant entities, and generate synthetic multilingual visual question answering data. The resulting dataset, CulturalGround, comprises 22 million high-quality, culturally-rich VQA pairs spanning 42 countries and 39 languages. We train an open-source MLLM CulturalPangea on CulturalGround, interleaving standard multilingual instruction-tuning data to preserve general abilities. CulturalPangea achieves state-of-the-art performance among open models on various culture-focused multilingual multimodal benchmarks, outperforming prior models by an average of 5.0 without degrading results on mainstream vision-language tasks. Our findings show that our targeted, culturally grounded approach could substantially narrow the cultural gap in MLLMs and offer a practical path towards globally inclusive multimodal systems.

