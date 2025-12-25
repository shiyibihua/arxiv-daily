---
layout: default
title: "TGC-Net: A Structure-Aware and Semantically-Aligned Framework for Text-Guided Medical Image Segmentation"
---

# TGC-Net: A Structure-Aware and Semantically-Aligned Framework for Text-Guided Medical Image Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21135" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21135v1</a>
  <a href="https://arxiv.org/pdf/2512.21135.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21135v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21135v1', 'TGC-Net: A Structure-Aware and Semantically-Aligned Framework for Text-Guided Medical Image Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gaoren Lin, Huangxuan Zhao, Yuan Xiong, Lefei Zhang, Bo Du, Wentao Zhu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出TGC-Net以解决医学图像分割中的文本引导问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学图像分割` `文本引导` `多模态融合` `CLIP` `深度学习` `结构感知` `语义对齐` `参数高效`

## 📋 核心要点

1. 现有医学图像分割方法在图像和文本编码器未对齐的情况下，导致多模态融合复杂且效果不佳。
2. TGC-Net通过引入语义结构协同编码器和领域增强文本编码器，优化了图像和文本的特征对齐，提升了分割精度。
3. 在多个数据集上，TGC-Net在分割性能上超越了现有方法，且可训练参数显著减少，表现出更高的效率。

## 📝 摘要（中文）

文本引导的医学分割通过利用临床报告作为辅助信息来提高分割精度。然而，现有方法通常依赖于未对齐的图像和文本编码器，这需要复杂的交互模块进行多模态融合。虽然CLIP提供了预对齐的多模态特征空间，但其在医学成像中的直接应用受到三个主要问题的限制：细粒度解剖结构的不足保留、复杂临床描述的建模不足以及领域特定的语义不对齐。为了解决这些挑战，我们提出了TGC-Net，这是一个基于CLIP的框架，专注于参数高效和任务特定的适应。具体而言，它包含一个语义结构协同编码器（SSE），增强CLIP的ViT与CNN分支进行多尺度结构细化，一个领域增强文本编码器（DATE），注入大型语言模型衍生的医学知识，以及一个视觉-语言校准模块（VLCM），在统一特征空间中细化跨模态对应关系。实验结果表明，TGC-Net在胸部X光和胸部CT的五个数据集上实现了最先进的性能，并显著减少了可训练参数。

## 🔬 方法详解

**问题定义**：论文要解决的具体问题是如何有效地将文本信息引导的医学图像分割与现有方法的不足相结合，特别是在图像和文本编码器未对齐的情况下，导致的多模态融合复杂性和效果不佳的问题。

**核心思路**：论文的核心解决思路是通过构建一个基于CLIP的框架，专注于参数高效和任务特定的适应，利用语义结构协同编码器和领域增强文本编码器来优化图像和文本特征的对齐。

**技术框架**：整体架构包括三个主要模块：语义结构协同编码器（SSE），用于多尺度结构细化；领域增强文本编码器（DATE），注入医学知识；视觉-语言校准模块（VLCM），用于在统一特征空间中细化跨模态对应关系。

**关键创新**：最重要的技术创新点在于引入了SSE和DATE模块，使得模型能够更好地保留细粒度解剖结构，并有效建模复杂的临床描述，从而解决了现有方法在医学图像分割中的局限性。

**关键设计**：在设计中，SSE结合了CNN分支以实现多尺度结构细化，DATE则利用大型语言模型的知识进行文本编码，VLCM则确保了图像和文本特征在统一空间中的有效对齐。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21135v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21135v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21135v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在实验中，TGC-Net在胸部X光和胸部CT的五个数据集上实现了最先进的性能，显著提高了Dice系数，并且可训练参数数量大幅减少，展示了其在效率和效果上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、临床辅助诊断和智能医疗系统。通过提高医学图像分割的精度，TGC-Net能够帮助医生更好地进行疾病诊断和治疗规划，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Text-guided medical segmentation enhances segmentation accuracy by utilizing clinical reports as auxiliary information. However, existing methods typically rely on unaligned image and text encoders, which necessitate complex interaction modules for multimodal fusion. While CLIP provides a pre-aligned multimodal feature space, its direct application to medical imaging is limited by three main issues: insufficient preservation of fine-grained anatomical structures, inadequate modeling of complex clinical descriptions, and domain-specific semantic misalignment. To tackle these challenges, we propose TGC-Net, a CLIP-based framework focusing on parameter-efficient, task-specific adaptations. Specifically, it incorporates a Semantic-Structural Synergy Encoder (SSE) that augments CLIP's ViT with a CNN branch for multi-scale structural refinement, a Domain-Augmented Text Encoder (DATE) that injects large-language-model-derived medical knowledge, and a Vision-Language Calibration Module (VLCM) that refines cross-modal correspondence in a unified feature space. Experiments on five datasets across chest X-ray and thoracic CT modalities demonstrate that TGC-Net achieves state-of-the-art performance with substantially fewer trainable parameters, including notable Dice gains on challenging benchmarks.

