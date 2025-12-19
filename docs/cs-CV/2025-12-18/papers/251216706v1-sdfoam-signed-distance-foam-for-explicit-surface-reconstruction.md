---
layout: default
title: SDFoam: Signed-Distance Foam for explicit surface reconstruction
---

# SDFoam: Signed-Distance Foam for explicit surface reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16706" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16706v1</a>
  <a href="https://arxiv.org/pdf/2512.16706.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16706v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16706v1', 'SDFoam: Signed-Distance Foam for explicit surface reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antonella Rech, Nicola Conci, Nicola Garau

**分类**: cs.CV, cs.GR

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**SDFoam：结合显式Voronoi图和隐式SDF，实现精确表面重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `神经辐射场` `三维重建` `有向距离场` `Voronoi图` `光线追踪`

## 📋 核心要点

1. 现有NeRF和3DGS等方法在精确网格重建方面存在不足，难以生成高质量的几何表面。
2. SDFoam结合显式Voronoi图和隐式SDF，利用SDF的度量一致性来约束Voronoi单元，从而优化表面几何。
3. 实验表明，SDFoam在保持光度质量和训练速度的同时，显著提高了网格重建精度，减少了伪影。

## 📝 摘要（中文）

神经辐射场（NeRF）通过光线追踪的体渲染在视角合成方面取得了显著进展。基于Splatting的方法，如3D高斯溅射（3DGS），通过栅格化3D图元提供了更快的渲染速度。RadiantFoam（RF）通过使用显式Voronoi图（VD）组织辐射，重新引入了光线追踪，实现了与高斯溅射相当的吞吐量。然而，上述方法在精确的网格重建方面仍然存在困难。本文通过联合学习显式VD和隐式有向距离场（SDF）来解决这个问题。场景通过光线追踪进行优化，并由Eikonal目标正则化。SDF引入了度量一致的等值面，进而偏置近表面Voronoi单元面与零水平集对齐。由此产生的模型产生更清晰、视角一致的表面，减少了浮动伪影并改善了拓扑结构，同时保持了光度质量，并保持了与RadiantFoam相当的训练速度。在不同的场景中，我们提出的混合隐式-显式公式，命名为SDFoam，在不牺牲效率的情况下，显著提高了网格重建精度（Chamfer距离），并具有可比的外观（PSNR，SSIM）。

## 🔬 方法详解

**问题定义**：现有神经渲染方法，如NeRF和3DGS，虽然在视角合成方面表现出色，但在精确的网格重建方面仍然存在挑战。这些方法生成的网格通常包含浮动伪影，拓扑结构不佳，难以满足对几何精度要求较高的应用。

**核心思路**：SDFoam的核心思路是将显式的Voronoi图表示与隐式的有向距离场（SDF）表示相结合。Voronoi图用于快速渲染和光度优化，而SDF则提供度量一致的几何约束，引导Voronoi单元面与真实的表面对齐。这种混合表示能够兼顾渲染效率和几何精度。

**技术框架**：SDFoam的整体框架包括以下几个主要步骤：1) 初始化：使用一组3D点初始化Voronoi图。2) 光线追踪：通过光线追踪渲染场景，并计算光度损失。3) SDF优化：使用Eikonal损失优化SDF，使其与场景几何一致。4) Voronoi图优化：利用SDF的梯度信息，调整Voronoi单元的位置和形状，使其更贴合表面。5) 重复步骤2-4，直到收敛。

**关键创新**：SDFoam的关键创新在于将显式的Voronoi图表示与隐式的SDF表示相结合，利用SDF的几何约束来优化Voronoi图，从而实现更精确的表面重建。与传统的NeRF方法相比，SDFoam能够生成更清晰、视角一致的表面，减少了浮动伪影。与RadiantFoam相比，SDFoam引入了SDF，从而提高了网格重建精度。

**关键设计**：SDFoam的关键设计包括：1) 使用Eikonal损失来正则化SDF，使其满足有向距离场的性质。2) 使用光线追踪来渲染场景，并计算光度损失。3) 使用SDF的梯度信息来调整Voronoi单元的位置和形状。4) 采用交替优化策略，分别优化SDF和Voronoi图。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16706v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16706v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16706v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SDFoam在网格重建精度方面显著优于现有方法。在多个数据集上，SDFoam的Chamfer距离明显低于NeRF和RadiantFoam，同时保持了与RadiantFoam相当的PSNR和SSIM。这表明SDFoam能够在不牺牲光度质量的情况下，显著提高几何精度。

## 🎯 应用场景

SDFoam在三维重建、虚拟现实、增强现实、机器人导航等领域具有广泛的应用前景。它可以用于生成高质量的三维模型，用于游戏开发、电影制作、工业设计等。此外，SDFoam还可以用于机器人导航，帮助机器人理解周围环境的几何结构。

## 📄 摘要（原文）

> Neural radiance fields (NeRF) have driven impressive progress in view synthesis by using ray-traced volumetric rendering. Splatting-based methods such as 3D Gaussian Splatting (3DGS) provide faster rendering by rasterizing 3D primitives. RadiantFoam (RF) brought ray tracing back, achieving throughput comparable to Gaussian Splatting by organizing radiance with an explicit Voronoi Diagram (VD). Yet, all the mentioned methods still struggle with precise mesh reconstruction. We address this gap by jointly learning an explicit VD with an implicit Signed Distance Field (SDF). The scene is optimized via ray tracing and regularized by an Eikonal objective. The SDF introduces metric-consistent isosurfaces, which, in turn, bias near-surface Voronoi cell faces to align with the zero level set. The resulting model produces crisper, view-consistent surfaces with fewer floaters and improved topology, while preserving photometric quality and maintaining training speed on par with RadiantFoam. Across diverse scenes, our hybrid implicit-explicit formulation, which we name SDFoam, substantially improves mesh reconstruction accuracy (Chamfer distance) with comparable appearance (PSNR, SSIM), without sacrificing efficiency.

