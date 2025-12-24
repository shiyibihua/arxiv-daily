---
layout: default
title: Locality-aware Concept Bottleneck Model
---

# Locality-aware Concept Bottleneck Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14562" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14562v1</a>
  <a href="https://arxiv.org/pdf/2508.14562.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14562v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14562v1', 'Locality-aware Concept Bottleneck Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sujin Jeon, Hyundo Lee, Eungseo Kim, Sanghack Lee, Byoung-Tak Zhang, Inwoo Hwang

**分类**: cs.CV

**发布日期**: 2025-08-20

**备注**: 34 pages, 25 figures

---

## 💡 一句话要点

**提出局部感知概念瓶颈模型以解决概念定位问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `概念瓶颈模型` `原型学习` `空间定位` `计算机视觉` `图像分类` `目标检测` `可解释性AI`

## 📋 核心要点

1. 现有的无标签概念瓶颈模型在概念定位上存在不足，常常关注与概念无关的视觉区域。
2. 本文提出的局部感知概念瓶颈模型通过原型学习确保概念的空间定位准确性，利用基础模型的信息。
3. 实验结果显示，LCBM在概念识别和定位方面表现优异，分类性能与现有方法相当。

## 📝 摘要（中文）

概念瓶颈模型（CBMs）是一种基于人类可理解视觉线索进行预测的可解释模型。然而，现有的无标签CBMs在概念定位上存在不足，常常关注与概念无关的区域。为此，本文提出了局部感知概念瓶颈模型（LCBM），该模型利用基础模型的丰富信息并采用原型学习，以确保概念的准确空间定位。具体而言，我们为每个概念分配一个原型，促进其代表该概念的典型图像特征。通过鼓励原型编码相似的局部区域，利用基础模型确保每个原型与其相关概念的相关性。实验结果表明，LCBM有效识别图像中的概念，并在保持分类性能的同时改善了定位效果。

## 🔬 方法详解

**问题定义**：本文旨在解决现有无标签概念瓶颈模型在图像中概念定位不准确的问题。现有方法常常无法有效关注与概念相关的区域，导致预测结果不理想。

**核心思路**：提出局部感知概念瓶颈模型（LCBM），通过为每个概念分配一个原型，确保原型能够准确代表该概念的特征，从而改善概念的空间定位。

**技术框架**：LCBM的整体架构包括原型学习模块和概念识别模块。原型学习模块负责学习每个概念的原型，概念识别模块则利用这些原型来确定图像中概念的存在及其位置。

**关键创新**：最重要的创新在于通过原型学习确保概念的空间定位准确性，与现有方法相比，LCBM能够更好地关注与概念相关的局部区域。

**关键设计**：在设计中，原型的学习通过鼓励其编码相似的局部区域来实现，损失函数设计上考虑了原型与概念的相关性，确保每个原型能够有效代表其对应的概念。

## 📊 实验亮点

实验结果表明，LCBM在概念识别和定位方面表现优异，相较于基线模型，定位精度提升显著，同时保持了与现有方法相当的分类性能。这一成果展示了模型在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉中的图像分类、目标检测和场景理解等任务。通过提高概念的空间定位能力，LCBM可以在自动驾驶、医疗影像分析等领域提供更为准确的决策支持，未来可能对智能系统的可解释性和可靠性产生积极影响。

## 📄 摘要（原文）

> Concept bottleneck models (CBMs) are inherently interpretable models that make predictions based on human-understandable visual cues, referred to as concepts. As obtaining dense concept annotations with human labeling is demanding and costly, recent approaches utilize foundation models to determine the concepts existing in the images. However, such label-free CBMs often fail to localize concepts in relevant regions, attending to visually unrelated regions when predicting concept presence. To this end, we propose a framework, coined Locality-aware Concept Bottleneck Model (LCBM), which utilizes rich information from foundation models and adopts prototype learning to ensure accurate spatial localization of the concepts. Specifically, we assign one prototype to each concept, promoted to represent a prototypical image feature of that concept. These prototypes are learned by encouraging them to encode similar local regions, leveraging foundation models to assure the relevance of each prototype to its associated concept. Then we use the prototypes to facilitate the learning process of identifying the proper local region from which each concept should be predicted. Experimental results demonstrate that LCBM effectively identifies present concepts in the images and exhibits improved localization while maintaining comparable classification performance.

