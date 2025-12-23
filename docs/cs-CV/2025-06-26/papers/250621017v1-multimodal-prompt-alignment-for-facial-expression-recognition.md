---
layout: default
title: Multimodal Prompt Alignment for Facial Expression Recognition
---

# Multimodal Prompt Alignment for Facial Expression Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21017" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21017v1</a>
  <a href="https://arxiv.org/pdf/2506.21017.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21017v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21017v1', 'Multimodal Prompt Alignment for Facial Expression Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fuyan Ma, Yiran He, Bin Sun, Shutao Li

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-26

**备注**: To appear in ICCV2025

---

## 💡 一句话要点

**提出多模态提示对齐框架以提升面部表情识别精度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `面部表情识别` `多模态提示` `视觉-语言模型` `细粒度对齐` `情感计算`

## 📋 核心要点

1. 现有基于视觉-语言模型的面部表情识别方法难以捕捉细粒度的文本-视觉关系，影响识别精度。
2. 本文提出的MPA-FER框架通过多模态提示对齐，利用大型语言模型生成详细描述，增强了视觉特征的学习。
3. 实验结果显示，MPA-FER在三个FER基准数据集上超越了现有方法，提升了识别性能并降低了计算成本。

## 📝 摘要（中文）

提示学习已被广泛应用于高效适应视觉-语言模型（VLMs），如CLIP，处理各种下游任务。然而，现有基于VLM的面部表情识别（FER）方法在捕捉细粒度文本-视觉关系方面存在困难。为了解决这一挑战，本文提出了一种名为MPA-FER的多模态提示对齐框架，为提示的视觉特征学习过程提供细粒度的语义指导，从而实现更精确和可解释的表示。具体而言，我们引入了一种多粒度硬提示生成策略，利用大型语言模型（LLM）生成每种面部表情的详细描述。通过最小化软提示与硬提示之间的特征差异，将LLM的外部知识注入软提示中。此外，本文还提出了跨模态全局-局部对齐模块，进一步改善文本与视觉特征之间的对齐。实验表明，该框架在三个FER基准数据集上超越了现有的最先进方法，同时保留了预训练模型的优势并降低了计算成本。

## 🔬 方法详解

**问题定义**：本文旨在解决现有基于视觉-语言模型的面部表情识别方法在捕捉细粒度文本-视觉关系方面的不足，导致对微妙表情差异的识别能力不足。

**核心思路**：提出多模态提示对齐框架（MPA-FER），通过生成详细的表情描述并将其与视觉特征对齐，增强模型的表达能力和可解释性。

**技术框架**：整体架构包括多粒度硬提示生成策略、软提示与硬提示的特征对齐、原型引导的视觉特征对齐以及跨模态全局-局部对齐模块，确保文本与视觉特征的有效对齐。

**关键创新**：最重要的创新在于结合大型语言模型生成的详细描述与视觉特征的对齐，显著提升了模型对细微表情的识别能力，与现有方法相比，提供了更为精确的语义指导。

**关键设计**：在损失函数设计上，采用最小化软提示与硬提示之间的特征差异，同时在视觉特征对齐中引入类特定原型，确保模型在保持预训练优势的同时，增强了对特定表情的识别能力。

## 📊 实验亮点

实验结果表明，MPA-FER在三个FER基准数据集上均超越了现有最先进的方法，具体提升幅度达到XX%，同时保持了预训练模型的优势，显著降低了计算成本。

## 🎯 应用场景

该研究的潜在应用领域包括情感计算、人机交互和社交机器人等，能够提升机器对人类情感的理解和响应能力。未来，随着多模态技术的进一步发展，该框架有望在更多实际场景中得到应用，推动智能系统的情感识别能力。

## 📄 摘要（原文）

> Prompt learning has been widely adopted to efficiently adapt vision-language models (VLMs) like CLIP for various downstream tasks. Despite their success, current VLM-based facial expression recognition (FER) methods struggle to capture fine-grained textual-visual relationships, which are essential for distinguishing subtle differences between facial expressions. To address this challenge, we propose a multimodal prompt alignment framework for FER, called MPA-FER, that provides fine-grained semantic guidance to the learning process of prompted visual features, resulting in more precise and interpretable representations. Specifically, we introduce a multi-granularity hard prompt generation strategy that utilizes a large language model (LLM) like ChatGPT to generate detailed descriptions for each facial expression. The LLM-based external knowledge is injected into the soft prompts by minimizing the feature discrepancy between the soft prompts and the hard prompts. To preserve the generalization abilities of the pretrained CLIP model, our approach incorporates prototype-guided visual feature alignment, ensuring that the prompted visual features from the frozen image encoder align closely with class-specific prototypes. Additionally, we propose a cross-modal global-local alignment module that focuses on expression-relevant facial features, further improving the alignment between textual and visual features. Extensive experiments demonstrate our framework outperforms state-of-the-art methods on three FER benchmark datasets, while retaining the benefits of the pretrained model and minimizing computational costs.

