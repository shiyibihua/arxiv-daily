---
layout: default
title: Vector Contrastive Learning For Pixel-Wise Pretraining In Medical Vision
---

# Vector Contrastive Learning For Pixel-Wise Pretraining In Medical Vision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20850" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20850v1</a>
  <a href="https://arxiv.org/pdf/2506.20850.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20850v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20850v1', 'Vector Contrastive Learning For Pixel-Wise Pretraining In Medical Vision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuting He, Shuo Li

**分类**: cs.CV

**发布日期**: 2025-06-25

**备注**: Accepted by ICCV 2025

---

## 💡 一句话要点

**提出向量对比学习以解决医学视觉中的像素级预训练问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对比学习` `医学视觉` `自监督学习` `像素级表示` `向量回归` `特征建模` `深度学习`

## 📋 核心要点

1. 现有的对比学习方法在医学视觉中的像素级表示扩展上存在挑战，特别是特征分散导致的类内特征相关性破坏。
2. 本文提出的向量对比学习通过将CL重新定义为向量回归问题，解决了像素级预训练中的分散量化问题。
3. 在8个任务的广泛实验中，COVER框架显著提升了像素级SSP的性能，推动了医学视觉基础模型的进步。

## 📝 摘要（中文）

对比学习（CL）已成为基础模型自监督预训练（SSP）的基石，但将CL扩展到医学视觉中的像素级表示仍然是一个未解决的问题。标准的CL将SSP公式化为二元优化问题（binary CL），过度追求特征分散导致过度分散问题，破坏了像素级特征的相关性，从而扰乱了类内分布。本文提出的向量CL将CL重新公式化为向量回归问题，通过建模特征距离来量化像素级预训练中的分散。为实现这一新范式，我们提出了COVER框架，该框架建立了可扩展的基于向量的自学习，强制从向量回归到距离建模的一致优化流程，并利用向量金字塔架构进行粒度适应，从而在SSP中保持像素级特征的相关性。大量实验表明，COVER显著提升了像素级SSP，推动了可泛化的医学视觉基础模型的发展。

## 🔬 方法详解

**问题定义**：本文旨在解决将对比学习扩展到医学视觉中的像素级表示的问题。现有的标准对比学习方法在追求特征分散时，导致了过度分散问题，破坏了像素级特征之间的相关性，影响了类内分布的稳定性。

**核心思路**：论文提出的向量对比学习通过将CL重新公式化为向量回归问题，能够有效量化像素级预训练中的特征分散。这种设计使得特征距离的建模成为可能，从而保持了像素级特征的相关性。

**技术框架**：COVER框架包括多个模块，首先是向量回归模块，通过回归位移向量来建模特征距离；其次是距离建模模块，确保优化流程的一致性；最后是向量金字塔架构，用于适应不同粒度的特征。

**关键创新**：最重要的创新在于将对比学习从二元优化转变为向量回归，允许对像素级特征的分散进行量化，解决了传统方法中的过度分散问题。

**关键设计**：在COVER框架中，采用了特定的损失函数来优化向量回归过程，并设计了向量金字塔架构以适应不同层次的特征表示，确保了像素级特征的相关性得以保持。

## 📊 实验亮点

在8个不同任务的实验中，COVER框架显著提升了像素级自监督预训练的性能，相较于基线方法，性能提升幅度达到XX%（具体数据待补充），展示了其在医学视觉领域的有效性和优越性。

## 🎯 应用场景

该研究在医学图像分析、疾病诊断和治疗规划等领域具有广泛的应用潜力。通过提升像素级特征的表示能力，COVER框架能够为医学视觉基础模型提供更强的支持，从而推动相关领域的技术进步和临床应用。未来，该方法可能会影响医学影像处理的标准化流程，提高诊断的准确性和效率。

## 📄 摘要（原文）

> Contrastive learning (CL) has become a cornerstone of self-supervised pretraining (SSP) in foundation models, however, extending CL to pixel-wise representation, crucial for medical vision, remains an open problem. Standard CL formulates SSP as a binary optimization problem (binary CL) where the excessive pursuit of feature dispersion leads to an over-dispersion problem, breaking pixel-wise feature correlation thus disrupting the intra-class distribution. Our vector CL reformulates CL as a vector regression problem, enabling dispersion quantification in pixel-wise pretraining via modeling feature distances in regressing displacement vectors. To implement this novel paradigm, we propose the COntrast in VEctor Regression (COVER) framework. COVER establishes an extendable vector-based self-learning, enforces a consistent optimization flow from vector regression to distance modeling, and leverages a vector pyramid architecture for granularity adaptation, thus preserving pixel-wise feature correlations in SSP. Extensive experiments across 8 tasks, spanning 2 dimensions and 4 modalities, show that COVER significantly improves pixel-wise SSP, advancing generalizable medical visual foundation models.

