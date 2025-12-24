---
layout: default
title: On the dynamic evolution of CLIP texture-shape bias and its relationship to human alignment and model robustness
---

# On the dynamic evolution of CLIP texture-shape bias and its relationship to human alignment and model robustness

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09814" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09814v2</a>
  <a href="https://arxiv.org/pdf/2508.09814.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09814v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09814v2', 'On the dynamic evolution of CLIP texture-shape bias and its relationship to human alignment and model robustness')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pablo Hernández-Cámara, Jose Manuel Jaén-Lorites, Alexandra Gómez-Villa, Jorge Vila-Tomás, Valero Laparra, Jesus Malo

**分类**: cs.CV

**发布日期**: 2025-08-13 (更新: 2025-12-19)

---

## 💡 一句话要点

**分析CLIP模型训练过程中的纹理-形状偏差及其与人类感知的关系**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对比学习` `多模态模型` `视觉表征` `人类感知` `模型鲁棒性` `纹理偏差` `形状表征` `训练动态`

## 📋 核心要点

1. 现有研究主要集中在完全训练后的模型分析，缺乏对训练过程中表征偏差和感知对齐动态的探讨。
2. 本文通过逐轮分析CLIP模型，揭示了纹理-形状偏差的演变及其与人类感知的关系，提供了新的视角。
3. 研究结果表明，早期阶段的低级感知对齐与后期的鲁棒性之间存在系统性的权衡，具有重要的理论与实践意义。

## 📝 摘要（中文）

对比语言-图像模型如CLIP展现了显著的泛化能力，但其内部视觉表征在训练过程中的演变及与人类感知的关系仍不清楚。本文通过逐轮分析CLIP模型，重点研究纹理-形状偏差、与人类感知判断的对齐及对图像噪声的敏感性。研究发现，早期训练阶段表现出强烈的纹理偏差和对低级人类感知的高度对齐，随着训练的进行，纹理偏差逐渐减弱，形状表征增强，同时对噪声的鲁棒性提高。这些动态变化在不同规模的CLIP模型中一致存在，揭示了多模态模型训练中感知对齐、特征偏差与鲁棒性的共同演化。

## 🔬 方法详解

**问题定义**：本文旨在解决对比语言-图像模型在训练过程中内部表征演变的理解不足，尤其是纹理-形状偏差与人类感知对齐的动态关系。现有方法多集中于模型训练完成后的静态分析，缺乏对训练动态的深入探讨。

**核心思路**：通过逐轮分析CLIP模型在训练过程中的表现，研究其纹理偏差如何随训练阶段变化，以及这种变化如何影响模型对人类感知的对齐和对噪声的鲁棒性。

**技术框架**：研究采用多种感知基准进行评估，包括低级图像质量评估、中级感知相似性、显著性对应和噪声鲁棒性。模型在不同训练阶段的表现被系统记录和分析，以识别表征转变的规律。

**关键创新**：本文的主要创新在于提供了对CLIP模型训练过程中表征动态的实证分析，揭示了早期低级感知对齐与后期鲁棒性之间的权衡，这一现象在不同规模的模型中普遍存在。

**关键设计**：研究中使用了多种感知基准和评估指标，确保了对模型表现的全面分析。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文获取更多技术细节。

## 📊 实验亮点

实验结果显示，CLIP模型在早期训练阶段表现出强烈的纹理偏差和对低级感知的高度对齐，随着训练进展，纹理偏差显著减弱，形状表征增强，噪声鲁棒性提高。这一动态变化在不同规模的模型中均有体现，表明该现象具有普遍性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理及多模态学习等。通过深入理解模型的表征动态，可以优化模型设计，提高其在实际应用中的鲁棒性和对人类感知的对齐程度，进而提升多模态系统的性能和用户体验。

## 📄 摘要（原文）

> Contrastive language-image models such as CLIP have demonstrated remarkable generalization capabilities. However, how their internal visual representations evolve during training and how this evolution relates to human perception remains poorly understood. Most existing analysis characterize fully trained models, leaving the dynamics of representational biases and perceptual alignment largely unexplored. In this work, we present an epoch-by-epoch analysis of CLIP models throughout training, focusing on the evolution of texture-shape bias, alignment with human perceptual judgements, and sensitivity to image noise. Using multiple perceptual benchmarks spanning low-level image quality assessment, mid-level perceptual similarity, saliency correspondence, and noisy robustness, we identify a consistent, training-stage-dependent representational transition. Early training stages exhibit strong texture bias, elevated alignment with low-level human perceptual measures, and increased sensitivity to Gaussian noise perturbations. As training progresses, this texture bias gradually diminishes in favor of more shape-based representations, coinciding with improved robustness to noise and a decline in low-level perceptual alignment. Importantly, these dynamics are consistently observed across multiple CLIP model scales, indicating that the phenomenon is not specific to a particular architecture size. Our findings provide an empirical characterization of how perceptual alignment, feature bias, and robustness co-evolve during multimodal model training. This work reveals a systematic trade-off between early low-level perceptual alignment and later robustness, offering new insights into the representational dynamics of vision-language models and their relationship to human visual processing.

