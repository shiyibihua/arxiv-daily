---
layout: default
title: On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images
---

# On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05558" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05558v1</a>
  <a href="https://arxiv.org/pdf/2506.05558.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05558v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05558v1', 'On-the-fly Reconstruction for Large-Scale Novel View Synthesis from Unposed Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andreas Meuleman, Ishaan Shah, Alexandre Lanvin, Bernhard Kerbl, George Drettakis

**分类**: cs.CV

**发布日期**: 2025-06-05

**期刊**: ACM Transactions on Graphics 44, 4 (August 2025)

**DOI**: [10.1145/3730913](https://doi.org/10.1145/3730913)

---

## 💡 一句话要点

**提出一种即时重建方法以解决大规模新视角合成问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `新视角合成` `即时重建` `高斯散射` `姿态估计` `大规模场景` `计算机视觉` `虚拟现实`

## 📋 核心要点

1. 现有方法在姿态估计和3DGS优化上耗时较长，难以满足实时需求。
2. 提出了一种即时重建方法，结合快速姿态估计和高效的高斯原语采样，提升了处理速度。
3. 在多种数据集上评估，结果显示该方法在速度和图像质量上与其他方法具有竞争力。

## 📝 摘要（中文）

辐射场方法如3D高斯散射（3DGS）能够轻松从照片中重建，实现自由视点导航。然而，使用运动结构和3DGS优化进行姿态估计仍需数分钟到数小时的计算时间。结合SLAM方法的3DGS虽然速度较快，但在宽基线和大场景中表现不佳。本文提出了一种即时方法，在捕获后立即生成相机姿态和训练好的3DGS，能够处理有序照片序列的密集和宽基线捕获及大规模场景。我们首先引入快速初始姿态估计，利用学习特征和GPU友好的小型束调整。接着，通过直接采样高斯原语的位置和形状，逐步生成所需的原语，显著加速训练。我们的增量方法通过引入可扩展的辐射场构建，逐步聚类3DGS原语，存储在锚点中并从GPU卸载，处理大规模场景。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模新视角合成中的即时重建问题，现有方法在姿态估计和优化上耗时较长，影响实时应用。

**核心思路**：提出一种即时方法，通过快速姿态估计和高效的高斯原语采样，能够在捕获后立即生成相机姿态和3DGS，满足实时需求。

**技术框架**：整体流程包括快速初始姿态估计、直接采样高斯原语、增量生成原语、聚类和存储原语等模块，确保高效处理大规模场景。

**关键创新**：最重要的创新在于结合了快速姿态估计与增量生成高斯原语的策略，使得在处理大规模场景时能够显著加速训练过程。

**关键设计**：采用了GPU友好的小型束调整方法进行姿态估计，并通过逐步聚类和合并高斯原语来优化存储和计算效率。具体参数设置和损失函数设计在文中有详细描述。

## 📊 实验亮点

实验结果表明，该方法在处理速度上显著优于传统方法，能够在多种捕获场景和场景大小下实现即时处理，保持图像质量与速度的竞争力。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和计算机图形学等，能够为实时场景重建和自由视点导航提供技术支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Radiance field methods such as 3D Gaussian Splatting (3DGS) allow easy reconstruction from photos, enabling free-viewpoint navigation. Nonetheless, pose estimation using Structure from Motion and 3DGS optimization can still each take between minutes and hours of computation after capture is complete. SLAM methods combined with 3DGS are fast but struggle with wide camera baselines and large scenes. We present an on-the-fly method to produce camera poses and a trained 3DGS immediately after capture. Our method can handle dense and wide-baseline captures of ordered photo sequences and large-scale scenes. To do this, we first introduce fast initial pose estimation, exploiting learned features and a GPU-friendly mini bundle adjustment. We then introduce direct sampling of Gaussian primitive positions and shapes, incrementally spawning primitives where required, significantly accelerating training. These two efficient steps allow fast and robust joint optimization of poses and Gaussian primitives. Our incremental approach handles large-scale scenes by introducing scalable radiance field construction, progressively clustering 3DGS primitives, storing them in anchors, and offloading them from the GPU. Clustered primitives are progressively merged, keeping the required scale of 3DGS at any viewpoint. We evaluate our solution on a variety of datasets and show that our solution can provide on-the-fly processing of all the capture scenarios and scene sizes we target while remaining competitive with other methods that only handle specific capture styles or scene sizes in speed, image quality, or both.

