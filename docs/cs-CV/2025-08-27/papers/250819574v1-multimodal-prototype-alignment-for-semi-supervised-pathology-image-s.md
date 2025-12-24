---
layout: default
title: Multimodal Prototype Alignment for Semi-supervised Pathology Image Segmentation
---

# Multimodal Prototype Alignment for Semi-supervised Pathology Image Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19574" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19574v1</a>
  <a href="https://arxiv.org/pdf/2508.19574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19574v1', 'Multimodal Prototype Alignment for Semi-supervised Pathology Image Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingxi Fu, Fanglei Fu, Xitong Ling, Huaitian Yuan, Tian Guan, Yonghong He, Lianghui Zhu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出MPAMatch以解决病理图像分割中的模糊边界问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `病理图像分割` `半监督学习` `多模态对比学习` `语义建模` `图像处理` `深度学习`

## 📋 核心要点

1. 现有方法主要依赖图像模态内的扰动一致性，难以捕捉复杂病理图像的高层次语义信息。
2. MPAMatch通过双重对比学习方案，结合图像和文本原型，提供结构和语义层面的监督，提升分割效果。
3. 在GLAS、EBHI-SEG-GLAND、EBHI-SEG-CANCER和KPI数据集上的实验结果表明，MPAMatch在结构和语义建模方面优于现有最先进方法。

## 📝 摘要（中文）

病理图像分割面临诸多挑战，尤其是模糊的语义边界和像素级标注的高成本。尽管基于一致性正则化的半监督方法（如UniMatch）取得了一定进展，但主要依赖于图像模态内的扰动一致性，难以捕捉高层次的语义先验。为了解决这些局限性，本文提出了MPAMatch，一个在多模态原型引导监督范式下进行像素级对比学习的新型分割框架。MPAMatch的核心创新在于图像原型与像素标签、文本原型与像素标签之间的双重对比学习方案，提供了结构和语义层面的监督。该方法显著提升了对未标记样本的判别能力，并首次将文本原型监督引入分割，显著改善了语义边界建模。

## 🔬 方法详解

**问题定义**：本文旨在解决病理图像分割中的模糊语义边界和高成本像素级标注的问题。现有的半监督方法在捕捉复杂结构的高层次语义先验方面存在不足。

**核心思路**：MPAMatch的核心思路是通过多模态原型引导的对比学习，结合图像和文本原型的监督，增强模型对未标记样本的判别能力。该方法首次引入文本原型监督，提升了语义边界建模的效果。

**技术框架**：MPAMatch的整体架构包括两个主要模块：图像原型与像素标签之间的对比学习，以及文本原型与像素标签之间的对比学习。通过这两个模块，模型能够在结构和语义层面进行有效的学习。

**关键创新**：MPAMatch的最重要创新在于其双重对比学习方案，区别于以往方法仅依赖图像模态的单一对比学习。这一设计使得模型能够同时利用结构信息和语义信息，从而显著提升分割性能。

**关键设计**：在网络结构上，MPAMatch重构了经典的TransUNet架构，采用病理预训练的基础模型（Uni）替代其ViT主干，以更有效地提取与病理相关的特征。同时，损失函数设计上结合了对比损失和传统的分割损失，以增强模型的学习能力。

## 📊 实验亮点

在GLAS、EBHI-SEG-GLAND、EBHI-SEG-CANCER和KPI数据集上的实验结果显示，MPAMatch在结构和语义建模方面显著优于现有最先进方法，具体性能提升幅度达到XX%（具体数据未知），验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、病理学研究和临床诊断等。通过提高病理图像分割的准确性，MPAMatch有助于医生在疾病诊断和治疗方案制定中的决策支持，未来可能对医疗行业产生深远影响。

## 📄 摘要（原文）

> Pathological image segmentation faces numerous challenges, particularly due to ambiguous semantic boundaries and the high cost of pixel-level annotations. Although recent semi-supervised methods based on consistency regularization (e.g., UniMatch) have made notable progress, they mainly rely on perturbation-based consistency within the image modality, making it difficult to capture high-level semantic priors, especially in structurally complex pathology images. To address these limitations, we propose MPAMatch - a novel segmentation framework that performs pixel-level contrastive learning under a multimodal prototype-guided supervision paradigm. The core innovation of MPAMatch lies in the dual contrastive learning scheme between image prototypes and pixel labels, and between text prototypes and pixel labels, providing supervision at both structural and semantic levels. This coarse-to-fine supervisory strategy not only enhances the discriminative capability on unlabeled samples but also introduces the text prototype supervision into segmentation for the first time, significantly improving semantic boundary modeling. In addition, we reconstruct the classic segmentation architecture (TransUNet) by replacing its ViT backbone with a pathology-pretrained foundation model (Uni), enabling more effective extraction of pathology-relevant features. Extensive experiments on GLAS, EBHI-SEG-GLAND, EBHI-SEG-CANCER, and KPI show MPAMatch's superiority over state-of-the-art methods, validating its dual advantages in structural and semantic modeling.

