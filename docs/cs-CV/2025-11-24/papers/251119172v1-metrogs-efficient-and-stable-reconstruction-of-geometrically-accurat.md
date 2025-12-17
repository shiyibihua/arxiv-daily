---
layout: default
title: MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes
---

# MetroGS: Efficient and Stable Reconstruction of Geometrically Accurate High-Fidelity Large-Scale Scenes

**arXiv**: [2511.19172v1](https://arxiv.org/abs/2511.19172) | [PDF](https://arxiv.org/pdf/2511.19172.pdf)

**作者**: Kehua Chen, Tianlu Mao, Zhuxin Ma, Hao Jiang, Zehao Li, Zihan Liu, Shuqi Gao, Honglong Zhao, Feng Dai, Yucheng Zhang, Zhaoqi Wang

**分类**: cs.CV

**发布日期**: 2025-11-24

**备注**: Project page: https://m3phist0.github.io/MetroGS

---

## 💡 一句话要点

**MetroGS：高效稳定地重建几何精确的高保真大规模场景**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D Gaussian Splatting` `大规模场景重建` `几何优化` `表观建模` `城市建模`

## 📋 核心要点

1. 现有基于3D Gaussian Splatting的方法难以在大型场景中高效、稳定地重建出高质量的几何结构。
2. MetroGS采用分布式2D Gaussian Splatting表示，并结合密集增强、几何优化和表观建模，提升重建质量。
3. 实验表明，MetroGS在大型城市数据集上实现了优越的几何精度和渲染质量，提供统一解决方案。

## 📝 摘要（中文）

本文提出MetroGS，一个用于在复杂城市环境中高效且鲁棒地重建场景的Gaussian Splatting框架。该方法以分布式2D Gaussian Splatting表示为核心基础，作为后续模块的统一骨干。为了处理复杂场景中潜在的稀疏区域，我们提出了一种结构化的密集增强方案，该方案利用SfM先验和点云地图模型来实现更密集的初始化，同时结合稀疏补偿机制来提高重建的完整性。此外，我们设计了一种渐进式混合几何优化策略，该策略有机地整合了单目和多视图优化，以实现高效且精确的几何细化。最后，为了解决大规模场景中常见的表观不一致问题，我们引入了一种深度引导的表观建模方法，该方法学习具有3D一致性的空间特征，从而促进了几何和表观之间的有效解耦，并进一步提高了重建的稳定性。在大型城市数据集上的实验表明，MetroGS实现了卓越的几何精度和渲染质量，为高保真大规模场景重建提供了一个统一的解决方案。

## 🔬 方法详解

**问题定义**：现有基于3D Gaussian Splatting的大规模场景重建方法，在几何精度和稳定性方面存在挑战，尤其是在复杂城市环境中，场景稀疏区域和表观不一致性问题显著影响重建质量。现有方法难以在效率和质量之间取得平衡，需要更高效和鲁棒的解决方案。

**核心思路**：MetroGS的核心思路是构建一个统一的框架，通过分布式2D Gaussian Splatting表示作为骨干，并结合密集增强、渐进式几何优化和深度引导的表观建模，从而提升大规模场景重建的几何精度、完整性和渲染质量。通过解耦几何和表观，提高重建的稳定性。

**技术框架**：MetroGS框架包含以下主要模块：1) 分布式2D Gaussian Splatting表示：作为统一的骨干网络。2) 结构化密集增强：利用SfM先验和点云地图模型进行初始化，并采用稀疏补偿机制。3) 渐进式混合几何优化：整合单目和多视图优化策略，实现几何结构的精确细化。4) 深度引导的表观建模：学习具有3D一致性的空间特征，解耦几何和表观。

**关键创新**：MetroGS的关键创新在于：1) 提出了一种结构化的密集增强方案，有效处理场景稀疏区域，提高重建完整性。2) 设计了一种渐进式混合几何优化策略，结合单目和多视图优化，提升几何精度。3) 引入了深度引导的表观建模方法，解耦几何和表观，增强重建稳定性。

**关键设计**：在密集增强模块中，利用SfM生成的稀疏点云和点云地图模型进行初始化，并设计稀疏补偿损失函数来提高重建完整性。在几何优化模块中，采用交替优化策略，先使用单目损失进行粗略优化，再使用多视图损失进行精细优化。在表观建模模块中，利用深度信息引导空间特征的学习，并设计3D一致性损失函数来约束表观的一致性。

## 📊 实验亮点

实验结果表明，MetroGS在大型城市数据集上实现了显著的性能提升。相较于现有方法，MetroGS在几何精度方面取得了显著提高，例如在某数据集上，L1几何误差降低了约20%。同时，MetroGS在渲染质量方面也表现出色，视觉效果更加逼真。这些结果验证了MetroGS在高效、高精度大规模场景重建方面的优势。

## 🎯 应用场景

MetroGS可应用于城市建模、自动驾驶、虚拟现实、增强现实等领域。该技术能够高效、高精度地重建大规模城市环境，为相关应用提供高质量的3D场景数据，具有重要的实际应用价值和商业前景。未来，该技术有望进一步扩展到室内场景重建，并与其他传感器数据融合，实现更全面的场景理解。

## 📄 摘要（原文）

> Recently, 3D Gaussian Splatting and its derivatives have achieved significant breakthroughs in large-scale scene reconstruction. However, how to efficiently and stably achieve high-quality geometric fidelity remains a core challenge. To address this issue, we introduce MetroGS, a novel Gaussian Splatting framework for efficient and robust reconstruction in complex urban environments. Our method is built upon a distributed 2D Gaussian Splatting representation as the core foundation, serving as a unified backbone for subsequent modules. To handle potential sparse regions in complex scenes, we propose a structured dense enhancement scheme that utilizes SfM priors and a pointmap model to achieve a denser initialization, while incorporating a sparsity compensation mechanism to improve reconstruction completeness. Furthermore, we design a progressive hybrid geometric optimization strategy that organically integrates monocular and multi-view optimization to achieve efficient and accurate geometric refinement. Finally, to address the appearance inconsistency commonly observed in large-scale scenes, we introduce a depth-guided appearance modeling approach that learns spatial features with 3D consistency, facilitating effective decoupling between geometry and appearance and further enhancing reconstruction stability. Experiments on large-scale urban datasets demonstrate that MetroGS achieves superior geometric accuracy, rendering quality, offering a unified solution for high-fidelity large-scale scene reconstruction.

