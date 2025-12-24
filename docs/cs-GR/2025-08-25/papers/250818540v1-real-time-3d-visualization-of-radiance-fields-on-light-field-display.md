---
layout: default
title: Real-time 3D Visualization of Radiance Fields on Light Field Displays
---

# Real-time 3D Visualization of Radiance Fields on Light Field Displays

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18540" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18540v1</a>
  <a href="https://arxiv.org/pdf/2508.18540.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18540v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18540v1', 'Real-time 3D Visualization of Radiance Fields on Light Field Displays')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jonghyun Kim, Cheng Sun, Michael Stengel, Matthew Chan, Andrew Russell, Jaehyun Jung, Wil Braithwaite, Shalini De Mello, David Luebke

**分类**: cs.GR, eess.IV

**发布日期**: 2025-08-25

**备注**: 10 pages, 14 figures. J. Kim, C. Sun, and M. Stengel contributed equally

---

## 💡 一句话要点

**提出实时3D辐射场可视化框架以解决光场显示的渲染挑战**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `辐射场` `光场显示` `实时渲染` `3D可视化` `高效计算` `虚拟现实` `增强现实`

## 📋 核心要点

1. 现有的辐射场与光场显示技术结合面临计算挑战，尤其是高分辨率渲染和视点偏移的需求。
2. 提出的框架通过单次平面扫描和共享组件缓存，支持多种辐射场表示，实现高效实时渲染。
3. 实验结果显示，该方法在45个视角下以200+ FPS的速度运行，相比传统方法加速高达22倍，且保持图像质量。

## 📝 摘要（中文）

辐射场技术通过高保真重建复杂环境，极大地推动了逼真3D场景可视化，适合光场显示。然而，结合这两种技术面临显著的计算挑战，因为光场显示需要从稍微偏移的视点生成多个高分辨率渲染，而辐射场依赖于计算密集的体积渲染。本文提出了一种统一且高效的实时辐射场渲染框架，支持多种辐射场表示，包括NeRF、3D高斯点云和稀疏体素，基于单次平面扫描策略和共享非定向组件的缓存。该框架在不同场景格式间通用，无需重新训练，避免了视图间的冗余计算。我们在Looking Glass显示器上展示了实时交互应用，达到200+ FPS的性能，支持512p分辨率和45个视角，实现无缝沉浸式3D交互。在标准基准测试中，我们的方法相比独立渲染每个视图实现了高达22倍的加速，同时保持图像质量。

## 🔬 方法详解

**问题定义**：本文旨在解决辐射场与光场显示结合时的计算效率问题，现有方法在高分辨率渲染和视点偏移时面临性能瓶颈。

**核心思路**：通过设计一个统一的框架，利用单次平面扫描策略和共享非定向组件的缓存，来提高渲染效率，支持多种辐射场表示。

**技术框架**：整体架构包括输入的辐射场表示模块、平面扫描渲染模块和缓存管理模块，确保在不同视角间高效共享计算结果。

**关键创新**：该框架的核心创新在于其通用性和高效性，能够在不同场景格式下无须重新训练，避免了视图间的冗余计算，显著提升了渲染速度。

**关键设计**：在设计中，采用了单次平面扫描策略，结合共享组件的缓存机制，确保了在多视角渲染时的高效性和图像质量的保持。具体的参数设置和损失函数设计在论文中详细阐述。

## 📊 实验亮点

实验结果表明，提出的方法在45个视角下以超过200 FPS的速度运行，相比于传统的独立渲染方法实现了高达22倍的加速，同时保持了图像的高质量。这一性能提升为实时3D交互应用奠定了基础。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和游戏开发等，能够为用户提供更加沉浸和互动的3D体验。随着光场显示技术的进步，该框架有望在多种场景下实现高效的3D可视化，推动相关领域的发展。

## 📄 摘要（原文）

> Radiance fields have revolutionized photo-realistic 3D scene visualization by enabling high-fidelity reconstruction of complex environments, making them an ideal match for light field displays. However, integrating these technologies presents significant computational challenges, as light field displays require multiple high-resolution renderings from slightly shifted viewpoints, while radiance fields rely on computationally intensive volume rendering. In this paper, we propose a unified and efficient framework for real-time radiance field rendering on light field displays. Our method supports a wide range of radiance field representations, including NeRFs, 3D Gaussian Splatting, and Sparse Voxels, within a shared architecture based on a single-pass plane sweeping strategy and caching of shared, non-directional components. The framework generalizes across different scene formats without retraining, and avoids redundant computation across views. We further demonstrate a real-time interactive application on a Looking Glass display, achieving 200+ FPS at 512p across 45 views, enabling seamless, immersive 3D interaction. On standard benchmarks, our method achieves up to 22x speedup compared to independently rendering each view, while preserving image quality.

