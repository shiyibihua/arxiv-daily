---
layout: default
title: Self-supervised Multiplex Consensus Mamba for General Image Fusion
---

# Self-supervised Multiplex Consensus Mamba for General Image Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20921" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20921v1</a>
  <a href="https://arxiv.org/pdf/2512.20921.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20921v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20921v1', 'Self-supervised Multiplex Consensus Mamba for General Image Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingying Wang, Rongjin Zhuang, Hui Zheng, Xuanhua He, Ke Cao, Xiaotong Tu, Xinghao Ding

**分类**: cs.CV

**发布日期**: 2025-12-24

**备注**: Accepted by AAAI 2026, 9 pages, 4 figures

---

## 💡 一句话要点

**提出SMC-Mamba框架，用于通用图像融合，提升多种融合任务性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `图像融合` `Mamba` `自监督学习` `跨模态融合` `对比学习` `通用图像融合` `多模态信息整合`

## 📋 核心要点

1. 现有图像融合方法难以兼顾多种任务，且在提升性能的同时往往会增加模型复杂度。
2. 提出SMC-Mamba框架，通过模态无关特征增强、多路共识跨模态Mamba模块和双层自监督对比学习损失，实现高效的通用图像融合。
3. 实验结果表明，该方法在多种图像融合任务和下游视觉任务中均优于现有最佳算法。

## 📝 摘要（中文）

图像融合旨在整合来自不同模态的互补信息，生成高质量的融合图像，从而增强诸如目标检测和语义分割等下游任务。与主要关注整合模态间信息的特定任务技术不同，通用图像融合需要在不增加复杂性的前提下，处理广泛的任务并提高性能。为了实现这一目标，我们提出了SMC-Mamba，一个用于通用图像融合的自监督多路共识Mamba框架。具体而言，模态无关特征增强（MAFE）模块通过自适应门控保留精细细节，并通过空间-通道和频率-旋转扫描增强全局表示。多路共识跨模态Mamba（MCCM）模块实现了专家之间的动态协作，达成共识以有效地整合来自多个模态的互补信息。MCCM中的跨模态扫描进一步加强了模态间的特征交互，促进了来自两个来源的关键信息的无缝整合。此外，我们引入了一种双层自监督对比学习损失（BSCL），它在不增加计算开销的情况下保留了高频信息，同时提高了下游任务的性能。大量实验表明，我们的方法在红外-可见光、医学、多焦点和多曝光融合等任务以及下游视觉任务中，优于最先进的图像融合算法。

## 🔬 方法详解

**问题定义**：现有图像融合方法通常针对特定任务设计，缺乏通用性，难以同时处理多种融合任务。此外，为了提升融合性能，现有方法往往会增加模型复杂度，导致计算开销增大。因此，如何设计一种既能处理多种融合任务，又能保持较低复杂度的通用图像融合方法是一个挑战。

**核心思路**：论文的核心思路是利用Mamba架构的序列建模能力，结合自监督学习，构建一个能够有效整合多模态信息的通用图像融合框架。通过模态无关的特征增强模块提取各模态的有效信息，并利用多路共识跨模态Mamba模块实现模态间的动态交互和信息融合。同时，引入双层自监督对比学习损失，以保留高频信息并提升下游任务性能。

**技术框架**：SMC-Mamba框架主要包含三个模块：模态无关特征增强（MAFE）模块、多路共识跨模态Mamba（MCCM）模块和双层自监督对比学习损失（BSCL）。首先，MAFE模块用于提取各模态的特征，并增强特征的表达能力。然后，MCCM模块利用Mamba架构进行跨模态特征融合，实现模态间的信息交互。最后，BSCL用于优化模型，提升融合图像的质量和下游任务的性能。

**关键创新**：该论文的关键创新在于以下几点：1) 提出了模态无关的特征增强模块，能够有效提取各模态的特征，并增强特征的表达能力。2) 提出了多路共识跨模态Mamba模块，利用Mamba架构进行跨模态特征融合，实现模态间的动态交互和信息融合。3) 提出了双层自监督对比学习损失，能够保留高频信息，并提升下游任务的性能。与现有方法相比，该方法具有更强的通用性和更高的性能。

**关键设计**：MAFE模块采用自适应门控机制来保留精细细节，并使用空间-通道和频率-旋转扫描来增强全局表示。MCCM模块利用多个专家进行动态协作，并通过跨模态扫描进一步加强模态间的特征交互。BSCL损失函数包含图像层面的对比学习和特征层面的对比学习，以保留高频信息并提升下游任务性能。具体参数设置和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20921v1/figures/framework.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20921v1/figures/Visual_VIF_MSRS.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20921v1/figures/Visual_MFF_MFI-WHU1.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SMC-Mamba在红外-可见光、医学、多焦点和多曝光融合等任务中均取得了优于现有SOTA算法的性能。例如，在红外-可见光图像融合任务中，该方法在多个指标上均取得了显著提升，并且在下游视觉任务中也表现出优越的性能。此外，该方法在保持较低复杂度的同时，能够有效保留高频信息，提升融合图像的质量。

## 🎯 应用场景

该研究成果可广泛应用于红外-可见光图像融合、医学图像融合、多焦点图像融合和多曝光图像融合等领域。高质量的融合图像能够提升目标检测、语义分割等下游任务的性能，从而在安防监控、医疗诊断、遥感图像分析等领域具有重要的应用价值和潜力。未来，该方法有望进一步扩展到更多模态的图像融合任务中。

## 📄 摘要（原文）

> Image fusion integrates complementary information from different modalities to generate high-quality fused images, thereby enhancing downstream tasks such as object detection and semantic segmentation. Unlike task-specific techniques that primarily focus on consolidating inter-modal information, general image fusion needs to address a wide range of tasks while improving performance without increasing complexity. To achieve this, we propose SMC-Mamba, a Self-supervised Multiplex Consensus Mamba framework for general image fusion. Specifically, the Modality-Agnostic Feature Enhancement (MAFE) module preserves fine details through adaptive gating and enhances global representations via spatial-channel and frequency-rotational scanning. The Multiplex Consensus Cross-modal Mamba (MCCM) module enables dynamic collaboration among experts, reaching a consensus to efficiently integrate complementary information from multiple modalities. The cross-modal scanning within MCCM further strengthens feature interactions across modalities, facilitating seamless integration of critical information from both sources. Additionally, we introduce a Bi-level Self-supervised Contrastive Learning Loss (BSCL), which preserves high-frequency information without increasing computational overhead while simultaneously boosting performance in downstream tasks. Extensive experiments demonstrate that our approach outperforms state-of-the-art (SOTA) image fusion algorithms in tasks such as infrared-visible, medical, multi-focus, and multi-exposure fusion, as well as downstream visual tasks.

