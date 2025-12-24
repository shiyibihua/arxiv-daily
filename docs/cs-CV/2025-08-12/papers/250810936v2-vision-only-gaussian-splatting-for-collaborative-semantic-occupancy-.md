---
layout: default
title: Vision-Only Gaussian Splatting for Collaborative Semantic Occupancy Prediction
---

# Vision-Only Gaussian Splatting for Collaborative Semantic Occupancy Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10936" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10936v2</a>
  <a href="https://arxiv.org/pdf/2508.10936.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10936v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10936v2', 'Vision-Only Gaussian Splatting for Collaborative Semantic Occupancy Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheng Chen, Hao Huang, Saurabh Bagchi

**分类**: cs.CV, cs.RO

**发布日期**: 2025-08-12 (更新: 2025-11-22)

**备注**: Accepted by AAAI 2026 (Oral)

---

## 💡 一句话要点

**提出稀疏3D语义高斯点云以解决协作语义占用预测问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `协作感知` `3D语义占用预测` `高斯点云` `信息融合` `自动驾驶`

## 📋 核心要点

1. 现有的视觉方法在3D语义占用预测中依赖密集体素或2D特征，导致高通信成本和对深度估计的依赖。
2. 本文提出利用稀疏3D语义高斯点云进行协作3D语义占用预测，通过共享中间高斯原语来实现信息融合。
3. 实验结果显示，所提方法在mIoU和IoU指标上均显著优于单代理和基线协作方法，且在减少通信量的情况下仍保持性能提升。

## 📝 摘要（中文）

协作感知使得连接车辆能够共享信息，克服单一代理系统的遮挡和有限感知范围。现有的基于视觉的3D语义占用预测方法通常依赖于密集的3D体素，导致高通信成本，或依赖于2D平面特征，需准确的深度估计或额外的监督，限制了其在协作场景中的应用。为了解决这些挑战，本文提出了首个利用稀疏3D语义高斯点云进行协作3D语义占用预测的方法。通过共享和融合中间高斯原语，我们的方法提供了三大优势：基于邻域的跨代理融合，消除重复并抑制噪声或不一致的高斯；在每个原语中联合编码几何和语义，减少对深度监督的依赖并允许简单的刚性对齐；稀疏的以对象为中心的信息，保留结构信息同时减少通信量。大量实验表明，我们的方法在mIoU上比单代理感知和基线协作方法分别提高了+8.42和+3.28点，在IoU上分别提高了+5.11和+22.41点。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉方法在协作3D语义占用预测中的高通信成本和对深度估计的依赖问题。现有方法通常依赖于密集体素或2D特征，限制了其在实际应用中的有效性。

**核心思路**：本文提出的核心思路是利用稀疏的3D语义高斯点云，通过共享和融合中间高斯原语来实现信息的高效传递和处理，从而减少通信量并提高预测精度。

**技术框架**：整体架构包括三个主要模块：高斯原语的生成、跨代理的融合过程以及最终的语义占用预测。每个模块都针对减少冗余和提高信息质量进行了优化。

**关键创新**：最重要的技术创新在于引入了稀疏3D语义高斯点云，结合邻域融合机制，显著降低了通信成本并提高了预测的准确性。这一方法与传统的密集体素方法有本质区别。

**关键设计**：在设计中，采用了稀疏编码策略和对象中心的信息传递方式，减少了对深度监督的依赖，同时通过简单的刚性对齐实现了几何和语义的联合编码。

## 📊 实验亮点

实验结果表明，所提方法在mIoU上比单代理感知提高了+8.42点，比基线协作方法提高了+3.28点；在IoU上分别提高了+5.11和+22.41点。此外，减少传输高斯数量后，仍能实现+1.9的mIoU提升，且通信量仅为34.6%。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、智能交通系统和机器人协作等。通过提高车辆间的信息共享和处理能力，可以显著提升环境感知的准确性和效率，推动智能交通技术的发展。

## 📄 摘要（原文）

> Collaborative perception enables connected vehicles to share information, overcoming occlusions and extending the limited sensing range inherent in single-agent (non-collaborative) systems. Existing vision-only methods for 3D semantic occupancy prediction commonly rely on dense 3D voxels, which incur high communication costs, or 2D planar features, which require accurate depth estimation or additional supervision, limiting their applicability to collaborative scenarios. To address these challenges, we propose the first approach leveraging sparse 3D semantic Gaussian splatting for collaborative 3D semantic occupancy prediction. By sharing and fusing intermediate Gaussian primitives, our method provides three benefits: a neighborhood-based cross-agent fusion that removes duplicates and suppresses noisy or inconsistent Gaussians; a joint encoding of geometry and semantics in each primitive, which reduces reliance on depth supervision and allows simple rigid alignment; and sparse, object-centric messages that preserve structural information while reducing communication volume. Extensive experiments demonstrate that our approach outperforms single-agent perception and baseline collaborative methods by +8.42 and +3.28 points in mIoU, and +5.11 and +22.41 points in IoU, respectively. When further reducing the number of transmitted Gaussians, our method still achieves a +1.9 improvement in mIoU, using only 34.6% communication volume, highlighting robust performance under limited communication budgets.

