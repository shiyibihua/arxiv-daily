---
layout: default
title: Cross-Temporal 3D Gaussian Splatting for Sparse-View Guided Scene Update
---

# Cross-Temporal 3D Gaussian Splatting for Sparse-View Guided Scene Update

**arXiv**: [2512.00534v1](https://arxiv.org/abs/2512.00534) | [PDF](https://arxiv.org/pdf/2512.00534.pdf)

**作者**: Zeyuan An, Yanghang Xiao, Zhiying Leng, Frederick W. B. Li, Xiaohui Liang

**分类**: cs.CV

**发布日期**: 2025-11-29

**备注**: AAAI2026 accepted

---

## 💡 一句话要点

**提出Cross-Temporal 3DGS，利用稀疏视图实现跨时序场景更新与重建**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `跨时序重建` `稀疏视图` `场景更新` `相机姿态估计`

## 📋 核心要点

1. 现有方法难以利用稀疏视图进行跨时序的3D场景更新，尤其是在缺乏密集扫描数据的情况下。
2. Cross-Temporal 3DGS通过跨时序相机对齐、干涉置信度初始化和渐进式优化，有效融合历史先验信息。
3. 实验表明，该方法在稀疏视图下显著提升了重建质量和数据效率，优于现有基线方法。

## 📝 摘要（中文）

本文提出了一种名为Cross-Temporal 3D Gaussian Splatting (Cross-Temporal 3DGS) 的新框架，用于利用稀疏图像和先前捕获的场景先验，高效地重建和更新不同时间段的3D场景。该方法包含三个阶段：1) 跨时序相机对齐，用于估计和对齐不同时间戳的相机姿态；2) 基于干涉的置信度初始化，用于识别时间戳之间未改变的区域，从而指导更新；3) 渐进式跨时序优化，迭代地将历史先验信息集成到3D场景中，以提高重建质量。该方法支持非连续捕获，不仅可以使用新的稀疏视图来细化现有场景，还可以借助当前捕获的数据，从有限的数据中恢复过去的场景。实验结果表明，该方法在重建质量和数据效率方面均优于基线方法，使其成为场景版本控制、跨时序数字孪生和长期空间文档记录的有前景的解决方案。

## 🔬 方法详解

**问题定义**：在计算机视觉中，随着时间的推移保持一致的3D场景表示是一个重要的挑战。在城市规划、灾害评估和历史遗址保护等实际应用中，通常无法获得或不切实际地进行密集扫描，因此从稀疏视图观测更新3D场景至关重要。现有方法在稀疏视图下进行跨时序场景更新时，重建质量和数据效率较低。

**核心思路**：Cross-Temporal 3DGS的核心思路是利用历史场景的先验知识，结合当前稀疏视图的信息，通过跨时序的优化策略，逐步更新和完善3D场景的表示。通过对齐不同时间戳的相机姿态，并识别场景中未发生变化的区域，可以更有效地利用历史信息，减少对新数据的依赖。

**技术框架**：Cross-Temporal 3DGS框架包含三个主要阶段：
1. **跨时序相机对齐**：估计和对齐不同时间戳的相机姿态，建立不同时间点图像之间的对应关系。
2. **基于干涉的置信度初始化**：识别不同时间戳之间未发生变化的区域，为后续的场景更新提供指导。
3. **渐进式跨时序优化**：迭代地将历史先验信息集成到3D场景中，逐步提高重建质量。

**关键创新**：该方法最重要的创新点在于其跨时序的优化策略，能够有效地融合历史先验信息和当前稀疏视图的信息。与现有方法相比，Cross-Temporal 3DGS能够更好地处理稀疏视图下的场景更新问题，并能够在数据有限的情况下恢复过去的场景。

**关键设计**：该方法使用3D Gaussian Splatting作为场景表示，并设计了基于干涉的置信度初始化方法来识别场景中未发生变化的区域。在优化过程中，采用了渐进式的策略，逐步将历史先验信息集成到3D场景中。具体的损失函数和网络结构等技术细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

实验结果表明，Cross-Temporal 3DGS在重建质量和数据效率方面均优于基线方法。具体性能数据和提升幅度在论文中进行了详细展示（未知），证明了该方法在稀疏视图下进行跨时序场景更新的有效性。

## 🎯 应用场景

Cross-Temporal 3DGS在多个领域具有广泛的应用前景，包括城市规划、灾害评估、历史遗址保护、场景版本控制和跨时序数字孪生。该方法能够利用稀疏视图数据高效地更新和重建3D场景，为长期空间文档记录提供了一种有前景的解决方案，并可用于构建随时间演变的动态3D模型。

## 📄 摘要（原文）

> Maintaining consistent 3D scene representations over time is a significant challenge in computer vision. Updating 3D scenes from sparse-view observations is crucial for various real-world applications, including urban planning, disaster assessment, and historical site preservation, where dense scans are often unavailable or impractical. In this paper, we propose Cross-Temporal 3D Gaussian Splatting (Cross-Temporal 3DGS), a novel framework for efficiently reconstructing and updating 3D scenes across different time periods, using sparse images and previously captured scene priors. Our approach comprises three stages: 1) Cross-temporal camera alignment for estimating and aligning camera poses across different timestamps; 2) Interference-based confidence initialization to identify unchanged regions between timestamps, thereby guiding updates; and 3) Progressive cross-temporal optimization, which iteratively integrates historical prior information into the 3D scene to enhance reconstruction quality. Our method supports non-continuous capture, enabling not only updates using new sparse views to refine existing scenes, but also recovering past scenes from limited data with the help of current captures. Furthermore, we demonstrate the potential of this approach to achieve temporal changes using only sparse images, which can later be reconstructed into detailed 3D representations as needed. Experimental results show significant improvements over baseline methods in reconstruction quality and data efficiency, making this approach a promising solution for scene versioning, cross-temporal digital twins, and long-term spatial documentation.

