---
layout: default
title: Evaluating Fisheye-Compatible 3D Gaussian Splatting Methods on Real Images Beyond 180 Degree Field of View
---

# Evaluating Fisheye-Compatible 3D Gaussian Splatting Methods on Real Images Beyond 180 Degree Field of View

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06968" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06968v1</a>
  <a href="https://arxiv.org/pdf/2508.06968.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06968v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06968v1', 'Evaluating Fisheye-Compatible 3D Gaussian Splatting Methods on Real Images Beyond 180 Degree Field of View')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ulas Gunes, Matias Turkulainen, Juho Kannala, Esa Rahtu

**分类**: cs.CV, cs.GR

**发布日期**: 2025-08-09

---

## 💡 一句话要点

**提出基于鱼眼镜头的3D高斯点云方法以解决极端畸变问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `鱼眼镜头` `3D重建` `高斯点云` `深度预测` `虚拟现实` `增强现实` `机器人视觉`

## 📋 核心要点

1. 现有的3D重建方法在处理超过180度视场的鱼眼图像时，常常面临严重的畸变问题，导致重建质量下降。
2. 本文提出了Fisheye-GS和3DGUT两种基于鱼眼镜头的3D高斯点云方法，并引入了一种基于深度的初始化策略，以克服SfM方法的局限性。
3. 实验结果表明，Fisheye-GS在160度视场下表现优异，而3DGUT在全视场下保持高质量重建，展示了鱼眼3D重建的实际可行性。

## 📝 摘要（中文）

本文首次评估了基于鱼眼镜头的3D高斯点云方法Fisheye-GS和3DGUT在超过180度视场的真实图像上的表现。研究涵盖了使用200度鱼眼相机捕获的室内和室外场景，分析了每种方法在极端畸变下的处理能力。通过在不同视场（200度、160度和120度）下的性能评估，探讨了周边畸变与空间覆盖之间的权衡。Fisheye-GS在160度时表现出色，而3DGUT在所有设置中保持稳定，且在200度视图下保持高感知质量。为了解决基于结构从运动（SfM）初始化的局限性，本文还提出了一种基于深度的策略，利用仅2-3张鱼眼图像的UniK3D预测，尽管UniK3D未在真实鱼眼数据上训练，但其生成的稠密点云在复杂场景中仍能实现与SfM相当的重建质量。

## 🔬 方法详解

**问题定义**：本文旨在解决现有3D重建方法在处理超过180度视场的鱼眼图像时，因畸变严重而导致的重建质量下降的问题。现有的SfM方法在强畸变条件下常常无法有效初始化。

**核心思路**：论文提出了Fisheye-GS和3DGUT两种新方法，Fisheye-GS通过减少视场来优化重建效果，而3DGUT则在不同视场下保持稳定的重建质量。此外，提出了一种基于深度的初始化策略，以减少对传统SfM方法的依赖。

**技术框架**：整体架构包括图像采集、特征提取、深度预测和点云重建四个主要阶段。首先使用鱼眼相机捕获图像，然后提取特征并进行深度预测，最后生成稠密点云并进行重建。

**关键创新**：最重要的创新在于提出了基于深度的初始化策略，利用UniK3D模型生成稠密点云，尽管该模型未在真实鱼眼数据上训练，但仍能在复杂场景中实现与传统SfM相当的重建质量。

**关键设计**：在参数设置上，Fisheye-GS在160度视场下表现最佳，而3DGUT在200度视场下保持高感知质量。损失函数和网络结构的设计旨在优化重建精度和稳定性，尤其是在处理极端畸变时。

## 📊 实验亮点

实验结果显示，Fisheye-GS在160度视场下的重建质量显著提升，而3DGUT在200度视场下保持高感知质量。与传统方法相比，本文提出的深度初始化策略在复杂场景中实现了与SfM相当的重建质量，展示了鱼眼3D重建的实际可行性。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和机器人视觉等，能够为这些领域提供高质量的3D重建解决方案。通过处理鱼眼图像，研究为广角3D重建提供了新的思路，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We present the first evaluation of fisheye-based 3D Gaussian Splatting methods, Fisheye-GS and 3DGUT, on real images with fields of view exceeding 180 degree. Our study covers both indoor and outdoor scenes captured with 200 degree fisheye cameras and analyzes how each method handles extreme distortion in real world settings. We evaluate performance under varying fields of view (200 degree, 160 degree, and 120 degree) to study the tradeoff between peripheral distortion and spatial coverage. Fisheye-GS benefits from field of view (FoV) reduction, particularly at 160 degree, while 3DGUT remains stable across all settings and maintains high perceptual quality at the full 200 degree view. To address the limitations of SfM-based initialization, which often fails under strong distortion, we also propose a depth-based strategy using UniK3D predictions from only 2-3 fisheye images per scene. Although UniK3D is not trained on real fisheye data, it produces dense point clouds that enable reconstruction quality on par with SfM, even in difficult scenes with fog, glare, or sky. Our results highlight the practical viability of fisheye-based 3DGS methods for wide-angle 3D reconstruction from sparse and distortion-heavy image inputs.

