---
layout: default
title: Vertex Features for Neural Global Illumination
---

# Vertex Features for Neural Global Illumination

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07852" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07852v1</a>
  <a href="https://arxiv.org/pdf/2508.07852.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07852v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07852v1', 'Vertex Features for Neural Global Illumination')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Su, Honghao Dong, Haojie Jin, Yisong Chen, Guoping Wang, Sheng Li

**分类**: cs.GR, cs.AI

**发布日期**: 2025-08-11

**备注**: Accepted by ACM SIGGRAPH Asia'2025

---

## 💡 一句话要点

**提出神经顶点特征以解决传统特征网格的内存瓶颈问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `神经渲染` `3D场景重建` `特征表示` `内存优化` `几何对齐` `深度学习`

## 📋 核心要点

1. 现有的特征网格表示在内存占用上存在显著瓶颈，限制了其在现代并行计算硬件上的应用。
2. 本文提出神经顶点特征，通过在网格顶点直接存储可学习特征，优化内存使用并改善特征表示。
3. 实验结果显示，该方法的内存消耗仅为传统网格表示的五分之一，同时保持了相似的渲染质量。

## 📝 摘要（中文）

近年来，学习型神经表示在3D场景重建和神经渲染应用中得到了广泛应用。然而，传统的特征网格表示通常存在显著的内存占用，成为现代并行计算硬件的瓶颈。本文提出了神经顶点特征，这是一种针对涉及显式网格表面的神经渲染任务的学习表示的广义形式。我们的方法直接在网格顶点处存储可学习特征，利用底层几何结构作为紧凑且结构化的神经处理表示。这不仅优化了内存效率，还通过与表面紧密对齐的任务特定几何先验改善了特征表示。实验结果表明，我们的方法将内存消耗降低至网格表示的五分之一甚至更少，同时保持了可比的渲染质量并降低了推理开销。

## 🔬 方法详解

**问题定义**：本文旨在解决传统特征网格表示在内存占用上的不足，尤其是在3D场景重建和神经渲染任务中，现有方法的内存消耗过大，影响了性能和效率。

**核心思路**：提出神经顶点特征，通过在网格顶点处存储可学习特征，利用几何结构的紧凑性来优化内存使用，并通过任务特定的几何先验来改善特征表示的质量。

**技术框架**：整体架构包括特征提取、几何对齐和神经渲染三个主要模块。特征提取模块负责从输入数据中提取特征，几何对齐模块确保特征与网格表面紧密对齐，最后神经渲染模块进行最终的图像生成。

**关键创新**：最重要的创新在于将可学习特征直接存储在网格顶点，而不是均匀分布在3D空间中，这种方法显著提高了内存效率和特征表示的质量。

**关键设计**：在设计中，采用了特定的损失函数来优化特征与几何的对齐，同时在网络结构上进行了调整，以适应顶点特征的存储和处理。

## 📊 实验亮点

实验结果表明，神经顶点特征方法的内存消耗仅为传统网格表示的五分之一，甚至更低，同时保持了相似的渲染质量，显著降低了推理开销，展示了其在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括3D场景重建、虚拟现实和游戏开发等。通过优化内存使用和提升渲染质量，神经顶点特征可以在资源受限的环境中实现更高效的渲染，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Recent research on learnable neural representations has been widely adopted in the field of 3D scene reconstruction and neural rendering applications. However, traditional feature grid representations often suffer from substantial memory footprint, posing a significant bottleneck for modern parallel computing hardware. In this paper, we present neural vertex features, a generalized formulation of learnable representation for neural rendering tasks involving explicit mesh surfaces. Instead of uniformly distributing neural features throughout 3D space, our method stores learnable features directly at mesh vertices, leveraging the underlying geometry as a compact and structured representation for neural processing. This not only optimizes memory efficiency, but also improves feature representation by aligning compactly with the surface using task-specific geometric priors. We validate our neural representation across diverse neural rendering tasks, with a specific emphasis on neural radiosity. Experimental results demonstrate that our method reduces memory consumption to only one-fifth (or even less) of grid-based representations, while maintaining comparable rendering quality and lowering inference overhead.

