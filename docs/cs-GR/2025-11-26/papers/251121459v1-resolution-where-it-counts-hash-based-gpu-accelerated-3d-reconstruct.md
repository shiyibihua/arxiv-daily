---
layout: default
title: Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids
---

# Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.21459" target="_blank" class="toolbar-btn">arXiv: 2511.21459v1</a>
    <a href="https://arxiv.org/pdf/2511.21459.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21459v1" 
            onclick="toggleFavorite(this, '2511.21459v1', 'Resolution Where It Counts: Hash-based GPU-Accelerated 3D Reconstruction via Variance-Adaptive Voxel Grids')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Lorenzo De Rebotti, Emanuele Giacomini, Giorgio Grisetti, Luca Di Giammarino

**分类**: cs.GR

**发布日期**: 2025-11-26

**备注**: Accepted for publication in ACM Transaction on Graphics. Project site: https://rvp-group.github.io/mrhash/

**DOI**: [10.1145/3777909](https://doi.org/10.1145/3777909)

---

## 💡 一句话要点

**提出基于方差自适应体素栅格的GPU加速哈希3D重建方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `三维重建` `体素栅格` `空间哈希` `GPU加速` `方差自适应` `实时渲染` `CUDA`

## 📋 核心要点

1. 传统体素方法在实时和资源受限场景中面临内存效率低、计算开销大和缺乏GPU支持等问题。
2. 论文提出一种基于方差自适应的多分辨率体素栅格，利用哈希表实现高效的GPU并行加速。
3. 实验结果表明，该方法在重建精度相当的情况下，速度提升高达13倍，内存使用降低4倍。

## 📝 摘要（中文）

本文提出了一种新颖的方差自适应多分辨率体素栅格，用于高效且可扩展的3D表面重建。该方法基于局部有向距离场（SDF）观测值的方差动态调整体素大小。与依赖递归八叉树结构的传统多分辨率方法不同，本文利用扁平空间哈希表存储所有体素块，支持常数时间访问和完全GPU并行。这种设计实现了高内存效率和实时可扩展性。此外，本文还展示了该表示如何通过用于高斯溅射的并行四叉树结构支持GPU加速渲染，从而有效控制溅射密度。开放源代码CUDA/C++实现与固定分辨率基线相比，实现了高达13倍的速度提升和4倍的内存使用降低，同时在重建精度方面保持了相当的结果，为高性能3D重建提供了一种实用且可扩展的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决从深度数据中高效、实时地进行3D表面重建的问题。现有基于固定分辨率体素栅格或八叉树等分层结构的体素方法，在内存效率、计算效率以及GPU并行支持方面存在不足，难以满足实时性和资源约束场景的需求。

**核心思路**：论文的核心思路是使用一种方差自适应的多分辨率体素栅格，并结合空间哈希表来实现高效的GPU加速。通过根据局部SDF观测值的方差动态调整体素大小，可以在保证重建精度的前提下，显著降低内存占用。使用哈希表可以实现对体素块的常数时间访问，从而充分利用GPU的并行计算能力。

**技术框架**：该方法主要包含以下几个阶段：1) 深度数据输入；2) 计算局部SDF观测值的方差；3) 根据方差自适应地创建和调整体素大小；4) 使用空间哈希表存储体素块；5) 使用GPU并行地进行SDF融合和表面重建；6) 使用并行四叉树结构进行GPU加速渲染。

**关键创新**：该方法最重要的技术创新点在于将方差自适应的多分辨率体素栅格与空间哈希表相结合。与传统的基于八叉树的多分辨率方法相比，该方法避免了递归结构带来的计算开销，并能够更好地利用GPU的并行计算能力。此外，使用方差作为体素大小调整的依据，可以更有效地利用内存资源，并在保证重建精度的前提下，降低内存占用。

**关键设计**：论文中关键的设计包括：1) 使用SDF观测值的方差作为体素大小调整的依据；2) 使用空间哈希表来存储体素块，实现常数时间访问；3) 设计了并行四叉树结构，用于GPU加速渲染，并有效控制溅射密度；4) 针对CUDA架构进行了优化，充分利用GPU的并行计算能力。

## 📊 实验亮点

实验结果表明，与固定分辨率基线相比，该方法在重建精度相当的情况下，实现了高达13倍的速度提升和4倍的内存使用降低。这表明该方法在保证重建质量的同时，显著提高了计算效率和内存效率，具有很强的实用价值。

## 🎯 应用场景

该研究成果可广泛应用于机器人导航、增强现实、虚拟现实、三维地图构建、逆向工程等领域。通过提供高效、实时的三维重建能力，可以提升机器人的环境感知能力，改善AR/VR的用户体验，加速三维模型的创建过程，并为未来的三维视觉应用奠定基础。

## 📄 摘要（原文）

> Efficient and scalable 3D surface reconstruction from range data remains a core challenge in computer graphics and vision, particularly in real-time and resource-constrained scenarios. Traditional volumetric methods based on fixed-resolution voxel grids or hierarchical structures like octrees often suffer from memory inefficiency, computational overhead, and a lack of GPU support. We propose a novel variance-adaptive, multi-resolution voxel grid that dynamically adjusts voxel size based on the local variance of signed distance field (SDF) observations. Unlike prior multi-resolution approaches that rely on recursive octree structures, our method leverages a flat spatial hash table to store all voxel blocks, supporting constant-time access and full GPU parallelism. This design enables high memory efficiency and real-time scalability. We further demonstrate how our representation supports GPU-accelerated rendering through a parallel quad-tree structure for Gaussian Splatting, enabling effective control over splat density. Our open-source CUDA/C++ implementation achieves up to 13x speedup and 4x lower memory usage compared to fixed-resolution baselines, while maintaining on par results in terms of reconstruction accuracy, offering a practical and extensible solution for high-performance 3D reconstruction.

