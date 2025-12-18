---
layout: default
title: Dynamic Novel View Synthesis in High Dynamic Range
---

# Dynamic Novel View Synthesis in High Dynamic Range

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21853" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21853v2</a>
  <a href="https://arxiv.org/pdf/2509.21853.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21853v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21853v2', 'Dynamic Novel View Synthesis in High Dynamic Range')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu

**分类**: cs.CV

**发布日期**: 2025-09-26 (更新: 2025-09-30)

---

## 💡 一句话要点

**提出HDR-4DGS，解决高动态范围动态场景的新视角合成问题。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `高动态范围` `新视角合成` `动态场景` `高斯溅射` `时间一致性`

## 📋 核心要点

1. 现有HDR NVS方法主要处理静态场景，无法有效处理真实世界中普遍存在的动态元素，如移动物体和光照变化。
2. 论文提出HDR-4DGS，通过动态色调映射模块显式连接HDR和LDR域，并根据时间变化动态调整色调映射函数，保持时间辐射一致性。
3. 实验结果表明，HDR-4DGS在定量指标和视觉效果上均优于现有方法，实现了更逼真的HDR渲染效果。

## 📝 摘要（中文）

高动态范围新视角合成(HDR NVS)旨在从传统成像条件下捕获的低动态范围(LDR)训练图像中学习HDR 3D模型。现有方法主要关注静态场景，隐式地假设所有场景元素保持静止和非生物状态。然而，现实世界的场景经常包含动态元素，如移动的物体、变化的光照条件和其他时间事件，从而提出了一个更具挑战性的场景。为了解决这个差距，我们提出了一个更现实的问题，即HDR动态新视角合成(HDR DNVS)，其中额外的维度“动态”强调了联合建模时间辐射变化以及LDR和HDR之间复杂的3D转换的必要性。为了应对这一复杂的、相互交织的挑战，我们引入了HDR-4DGS，这是一种基于高斯溅射的架构，具有创新的动态色调映射模块，该模块显式地连接了HDR和LDR域，通过根据时间维度上不断变化的辐射分布动态调整色调映射函数来保持时间辐射一致性。因此，HDR-4DGS实现了时间辐射一致性和空间精确的颜色转换，从而能够从任意视点和时间实例进行逼真的HDR渲染。大量的实验表明，HDR-4DGS在定量性能和视觉保真度方面都超过了现有的最先进方法。源代码将会发布。

## 🔬 方法详解

**问题定义**：论文旨在解决高动态范围动态新视角合成(HDR DNVS)问题。现有HDR NVS方法主要针对静态场景，无法处理真实场景中常见的动态元素，导致合成效果不佳。这些方法无法有效建模时间辐射变化以及LDR和HDR之间的复杂转换。

**核心思路**：论文的核心思路是利用基于高斯溅射的HDR-4DGS架构，并引入动态色调映射模块，显式地连接HDR和LDR域。通过动态调整色调映射函数，使模型能够适应时间维度上辐射分布的变化，从而保持时间辐射一致性。

**技术框架**：HDR-4DGS的整体架构基于高斯溅射，主要包含以下模块：LDR图像输入、高斯特征提取、动态色调映射模块、HDR图像生成和渲染模块。动态色调映射模块是核心，负责将LDR特征转换为HDR特征，并保持时间一致性。整个流程通过优化高斯参数和色调映射函数，实现高质量的HDR动态新视角合成。

**关键创新**：论文的关键创新在于动态色调映射模块的设计。该模块能够根据时间维度上辐射分布的变化，动态调整色调映射函数，从而显式地建模LDR和HDR域之间的关系，并保持时间辐射一致性。这与现有方法中隐式地假设静态场景有本质区别。

**关键设计**：动态色调映射模块的具体实现细节未知，但可以推测其可能包含时间相关的参数，并通过损失函数约束时间一致性。损失函数可能包括LDR和HDR图像的重建损失、时间一致性损失以及感知损失等。高斯参数的优化可能采用类似于4D-GS的方法，以保证场景的几何一致性。

## 📊 实验亮点

实验结果表明，HDR-4DGS在合成HDR动态新视角方面取得了显著的性能提升。具体而言，在定量指标上，HDR-4DGS优于现有的state-of-the-art方法。在视觉效果上，HDR-4DGS能够生成更逼真、时间一致的HDR图像，有效解决了动态场景下的伪影问题。具体提升幅度未知，但论文强调了在定量性能和视觉保真度上均超越了现有方法。

## 🎯 应用场景

该研究成果可应用于电影特效制作、游戏开发、虚拟现实/增强现实等领域。通过该技术，可以从普通相机拍摄的LDR视频中生成高质量的HDR动态场景，从而提升视觉体验，并降低HDR内容制作的成本。未来，该技术还可能应用于自动驾驶、机器人导航等领域，提升感知系统的鲁棒性。

## 📄 摘要（原文）

> High Dynamic Range Novel View Synthesis (HDR NVS) seeks to learn an HDR 3D model from Low Dynamic Range (LDR) training images captured under conventional imaging conditions. Current methods primarily focus on static scenes, implicitly assuming all scene elements remain stationary and non-living. However, real-world scenarios frequently feature dynamic elements, such as moving objects, varying lighting conditions, and other temporal events, thereby presenting a significantly more challenging scenario. To address this gap, we propose a more realistic problem named HDR Dynamic Novel View Synthesis (HDR DNVS), where the additional dimension ``Dynamic'' emphasizes the necessity of jointly modeling temporal radiance variations alongside sophisticated 3D translation between LDR and HDR. To tackle this complex, intertwined challenge, we introduce HDR-4DGS, a Gaussian Splatting-based architecture featured with an innovative dynamic tone-mapping module that explicitly connects HDR and LDR domains, maintaining temporal radiance coherence by dynamically adapting tone-mapping functions according to the evolving radiance distributions across the temporal dimension. As a result, HDR-4DGS achieves both temporal radiance consistency and spatially accurate color translation, enabling photorealistic HDR renderings from arbitrary viewpoints and time instances. Extensive experiments demonstrate that HDR-4DGS surpasses existing state-of-the-art methods in both quantitative performance and visual fidelity. Source code will be released.

