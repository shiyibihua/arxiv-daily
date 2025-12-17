---
layout: default
title: VGGTFace: Topologically Consistent Facial Geometry Reconstruction in the Wild
---

# VGGTFace: Topologically Consistent Facial Geometry Reconstruction in the Wild

**arXiv**: [2511.20366v2](https://arxiv.org/abs/2511.20366) | [PDF](https://arxiv.org/pdf/2511.20366.pdf)

**作者**: Xin Ming, Yuxuan Han, Tianyu Huang, Feng Xu

**分类**: cs.CV

**发布日期**: 2025-11-25 (更新: 2025-11-26)

**🔗 代码/项目**: [GITHUB](https://github.com/grignarder/vggtface)

---

## 💡 一句话要点

**VGGTFace：利用3D基础模型实现拓扑一致的人脸几何重建**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `人脸重建` `三维重建` `拓扑一致性` `3D基础模型` `Bundle Adjustment`

## 📋 核心要点

1. 现有方法在野外人脸几何重建中，面临人工干预繁琐、泛化性不足或3D形变模型表达能力有限等挑战。
2. VGGTFace利用3D基础模型VGGT的强大泛化能力，并结合Pixel3DMM注入拓扑信息，实现拓扑一致的人脸重建。
3. 实验表明，VGGTFace在基准测试中达到SOTA，并对野外数据表现出良好的泛化能力，重建速度快。

## 📝 摘要（中文）

本文提出VGGTFace，一种自动化的方法，创新性地应用3D基础模型VGGT，从日常用户拍摄的野外多视角图像中重建拓扑一致的人脸几何。核心思想是，通过利用VGGT，该方法自然地继承了其大规模训练和点图表示带来的强大的泛化能力和表达能力。然而，如何从VGGT重建拓扑一致的网格尚不清楚，因为拓扑信息在其预测中缺失。为此，本文使用Pixel3DMM增强VGGT，通过像素对齐的UV值注入拓扑信息。通过这种方式，将VGGT的像素对齐点图转换为具有拓扑的点云。针对这种具有已知拓扑的点云，提出了一种新的拓扑感知Bundle Adjustment策略来融合它们，其中为Bundle Adjustment目标构建了拉普拉斯能量。该方法在单个NVIDIA RTX 4090上，用10秒钟为16个视图实现高质量重建。实验表明，在基准测试上取得了最先进的结果，并对野外数据具有令人印象深刻的泛化能力。代码可在https://github.com/grignarder/vggtface获得。

## 🔬 方法详解

**问题定义**：论文旨在解决从野外多视角图像中自动重建拓扑一致的人脸几何的问题。现有方法的痛点在于，要么需要大量的人工干预，要么缺乏对野外数据的泛化能力，或者受到3D形变模型表达能力的限制，难以捕捉复杂的人脸表情和形状。

**核心思路**：论文的核心思路是利用预训练的3D基础模型VGGT的强大泛化能力和表达能力，并结合Pixel3DMM来注入拓扑信息。通过将VGGT的点图预测与Pixel3DMM的拓扑结构相结合，可以克服VGGT本身缺乏拓扑信息的缺点，从而实现拓扑一致的人脸重建。

**技术框架**：VGGTFace的整体框架主要包含两个阶段：首先，利用VGGT预测人脸的点图，并使用Pixel3DMM提供像素对齐的UV值，从而将点图转换为具有拓扑信息的点云。然后，提出了一种拓扑感知Bundle Adjustment策略，将这些点云进行融合，最终得到拓扑一致的人脸几何模型。

**关键创新**：该方法最重要的技术创新在于将3D基础模型VGGT与Pixel3DMM相结合，从而在利用VGGT的泛化能力的同时，注入了拓扑信息。此外，提出的拓扑感知Bundle Adjustment策略，通过构建拉普拉斯能量，进一步优化了重建结果的拓扑一致性。与现有方法相比，该方法无需人工干预，且具有更强的泛化能力和表达能力。

**关键设计**：在拓扑感知Bundle Adjustment中，关键的设计是拉普拉斯能量的构建，它通过约束相邻顶点的平滑性，来保证重建结果的拓扑一致性。具体的损失函数包括光度损失、几何损失和拉普拉斯损失。此外，论文还针对VGGT的特点，对Bundle Adjustment的优化过程进行了调整，以提高重建的效率和精度。

## 📊 实验亮点

实验结果表明，VGGTFace在公开数据集上取得了state-of-the-art的结果，并且在野外数据上表现出强大的泛化能力。该方法能够在单个NVIDIA RTX 4090上，用10秒钟为16个视图实现高质量重建，显著提高了重建效率。与现有方法相比，VGGTFace在重建精度和拓扑一致性方面均有显著提升。

## 🎯 应用场景

VGGTFace在数字替身创建、虚拟现实/增强现实、人脸识别、动画制作等领域具有广泛的应用前景。该方法能够自动地从用户提供的多视角图像中重建高质量的人脸几何模型，降低了数字内容创作的门槛，并为个性化应用提供了基础。

## 📄 摘要（原文）

> Reconstructing topologically consistent facial geometry is crucial for the digital avatar creation pipelines. Existing methods either require tedious manual efforts, lack generalization to in-the-wild data, or are constrained by the limited expressiveness of 3D Morphable Models. To address these limitations, we propose VGGTFace, an automatic approach that innovatively applies the 3D foundation model, i.e. VGGT, for topologically consistent facial geometry reconstruction from in-the-wild multi-view images captured by everyday users. Our key insight is that, by leveraging VGGT, our method naturally inherits strong generalization ability and expressive power from its large-scale training and point map representation. However, it is unclear how to reconstruct a topologically consistent mesh from VGGT, as the topology information is missing in its prediction. To this end, we augment VGGT with Pixel3DMM for injecting topology information via pixel-aligned UV values. In this manner, we convert the pixel-aligned point map of VGGT to a point cloud with topology. Tailored to this point cloud with known topology, we propose a novel Topology-Aware Bundle Adjustment strategy to fuse them, where we construct a Laplacian energy for the Bundle Adjustment objective. Our method achieves high-quality reconstruction in 10 seconds for 16 views on a single NVIDIA RTX 4090. Experiments demonstrate state-of-the-art results on benchmarks and impressive generalization to in-the-wild data. Code is available at https://github.com/grignarder/vggtface.

