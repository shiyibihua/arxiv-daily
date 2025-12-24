---
layout: default
title: A new dataset and comparison for multi-camera frame synthesis
---

# A new dataset and comparison for multi-camera frame synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09068" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09068v2</a>
  <a href="https://arxiv.org/pdf/2508.09068.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09068v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09068v2', 'A new dataset and comparison for multi-camera frame synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Conall Daly, Anil Kokaram

**分类**: eess.IV, cs.CV

**发布日期**: 2025-08-12 (更新: 2025-09-18)

**备注**: SPIE 2025 - Applications of Digital Image Processing XLVIII accepted manuscript, 13 pages

**DOI**: [10.1117/12.3065025](https://doi.org/10.1117/12.3065025)

---

## 💡 一句话要点

**提出多摄像头数据集以解决帧合成方法比较问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `帧合成` `多摄像头` `数据集` `视图合成` `深度学习` `图像处理` `性能评估`

## 📋 核心要点

1. 现有的帧合成方法在比较帧插值和视图合成时面临挑战，尤其是数据集的偏差问题。
2. 本文提出了一种新型的多摄像头数据集，旨在通过公平的实验设计来比较不同的帧合成方法。
3. 实验结果表明，在真实图像数据上，经典方法与深度学习方法的性能相近，而在合成场景中，3D高斯点云方法表现更佳。

## 📝 摘要（中文）

现有的帧合成方法可分为帧插值和视图合成技术，但大多数帧插值数据集侧重于单摄像头的时间序列，而视图合成数据集则偏向于立体深度估计。这使得两者之间的直接比较变得困难。本文开发了一种新型多摄像头数据集，利用定制的密集线性摄像头阵列，旨在实现公平比较。实验结果显示，深度学习方法在真实图像数据上并未显著优于经典方法，而在合成场景中，3D高斯点云方法的表现则优于帧插值算法，提升幅度达到近5 dB PSNR。

## 🔬 方法详解

**问题定义**：本文旨在解决帧插值与视图合成方法之间的比较问题，现有数据集的偏差使得直接比较变得困难。

**核心思路**：通过开发一个新型的多摄像头数据集，利用定制的密集线性摄像头阵列，提供公平的实验基础，以便对比不同的帧合成技术。

**技术框架**：整体架构包括数据集的构建、经典与深度学习帧插值算法的评估，以及与视图合成方法（3D高斯点云）的比较。主要模块包括数据采集、模型训练和性能评估。

**关键创新**：最重要的创新在于构建了一个多摄像头数据集，能够同时支持帧插值和视图合成的比较，填补了现有研究的空白。

**关键设计**：在实验中，采用了多种经典和深度学习的帧插值算法，并使用3D高斯点云作为视图合成基线，评估指标为PSNR，确保了实验的严谨性。

## 📊 实验亮点

实验结果显示，在真实图像数据上，深度学习方法的性能与经典方法相当，3D高斯点云方法在合成场景中表现优异，提升幅度达到近5 dB PSNR，显示出其在特定条件下的优势。

## 🎯 应用场景

该研究的潜在应用领域包括视频处理、虚拟现实和增强现实等场景，能够为多视角图像合成提供更为准确和高效的解决方案。未来，该数据集和比较方法可能推动相关领域的研究进展，促进新算法的开发与应用。

## 📄 摘要（原文）

> Many methods exist for frame synthesis in image sequences but can be broadly categorised into frame interpolation and view synthesis techniques. Fundamentally, both frame interpolation and view synthesis tackle the same task, interpolating a frame given surrounding frames in time or space. However, most frame interpolation datasets focus on temporal aspects with single cameras moving through time and space, while view synthesis datasets are typically biased toward stereoscopic depth estimation use cases. This makes direct comparison between view synthesis and frame interpolation methods challenging. In this paper, we develop a novel multi-camera dataset using a custom-built dense linear camera array to enable fair comparison between these approaches. We evaluate classical and deep learning frame interpolators against a view synthesis method (3D Gaussian Splatting) for the task of view in-betweening. Our results reveal that deep learning methods do not significantly outperform classical methods on real image data, with 3D Gaussian Splatting actually underperforming frame interpolators by as much as 3.5 dB PSNR. However, in synthetic scenes, the situation reverses -- 3D Gaussian Splatting outperforms frame interpolation algorithms by almost 5 dB PSNR at a 95% confidence level.

