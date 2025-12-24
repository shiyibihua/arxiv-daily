---
layout: default
title: Propagating Sparse Depth via Depth Foundation Model for Out-of-Distribution Depth Completion
---

# Propagating Sparse Depth via Depth Foundation Model for Out-of-Distribution Depth Completion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04984" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04984v1</a>
  <a href="https://arxiv.org/pdf/2508.04984.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04984v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04984v1', 'Propagating Sparse Depth via Depth Foundation Model for Out-of-Distribution Depth Completion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shenglun Chen, Xinzhu Ma, Hong Zhang, Haojie Li, Zhihui Wang

**分类**: cs.CV

**发布日期**: 2025-08-07

**备注**: Accepted by IEEE TIP

**🔗 代码/项目**: [GITHUB](https://github.com/shenglunch/PSD)

---

## 💡 一句话要点

**提出深度基础模型以解决分布外深度补全问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度补全` `深度基础模型` `分布外学习` `计算机视觉` `环境感知` `鲁棒性` `双空间传播`

## 📋 核心要点

1. 现有深度补全方法在分布外场景中性能下降，缺乏足够的鲁棒性。
2. 提出利用深度基础模型提取环境线索，设计双空间传播方法以增强深度补全的鲁棒性。
3. 在NYUv2和KITTI数据集上训练，框架在16个其他数据集上表现优异，超越现有最先进的方法。

## 📝 摘要（中文）

深度补全是计算机视觉中的一个重要挑战，旨在从稀疏深度图重建密集深度图，通常需要配对的RGB图像。现有的基于学习的方法依赖于精心准备但有限的数据，导致在分布外场景中性能显著下降。本文提出了一种新颖的深度补全框架，利用深度基础模型提取环境线索，以引导稀疏深度信息的传播。我们设计了一种无可学习参数的双空间传播方法，有效地在3D和2D空间中传播稀疏深度，以保持几何结构和局部一致性。此外，我们引入了可学习的修正模块，逐步调整深度预测。实验结果表明，该框架在16个其他数据集上的表现优于现有的深度补全方法。

## 🔬 方法详解

**问题定义**：本文旨在解决深度补全中的分布外问题，现有方法在面对未见过的数据时表现不佳，导致深度重建的准确性下降。

**核心思路**：通过利用深度基础模型提取RGB图像中的结构和语义信息，引导稀疏深度信息的传播，从而增强深度补全模型的鲁棒性，无需大规模训练。

**技术框架**：整体架构包括深度基础模型、双空间传播模块和可学习的修正模块。首先，深度基础模型提取环境线索，然后通过双空间传播在3D和2D空间中传播稀疏深度，最后通过修正模块调整预测结果。

**关键创新**：本研究的创新点在于设计了一种无学习参数的双空间传播方法，能够有效保持几何结构和局部一致性，这是与现有方法的本质区别。

**关键设计**：在模型中，双空间传播方法不依赖于可学习参数，确保了传播过程的稳定性和一致性；修正模块则通过逐步调整深度预测，提升了最终的深度重建质量。

## 📊 实验亮点

实验结果显示，本文框架在16个分布外数据集上的表现显著优于现有最先进的深度补全方法，具体提升幅度达到XX%，验证了其在复杂场景下的有效性和鲁棒性。

## 🎯 应用场景

该研究在自动驾驶、机器人导航和增强现实等领域具有广泛的应用潜力。通过提高深度补全的鲁棒性，可以在复杂环境中实现更准确的深度感知，从而提升系统的整体性能和可靠性。未来，该方法有望推动更多基于深度信息的应用发展。

## 📄 摘要（原文）

> Depth completion is a pivotal challenge in computer vision, aiming at reconstructing the dense depth map from a sparse one, typically with a paired RGB image. Existing learning based models rely on carefully prepared but limited data, leading to significant performance degradation in out-of-distribution (OOD) scenarios. Recent foundation models have demonstrated exceptional robustness in monocular depth estimation through large-scale training, and using such models to enhance the robustness of depth completion models is a promising solution. In this work, we propose a novel depth completion framework that leverages depth foundation models to attain remarkable robustness without large-scale training. Specifically, we leverage a depth foundation model to extract environmental cues, including structural and semantic context, from RGB images to guide the propagation of sparse depth information into missing regions. We further design a dual-space propagation approach, without any learnable parameters, to effectively propagates sparse depth in both 3D and 2D spaces to maintain geometric structure and local consistency. To refine the intricate structure, we introduce a learnable correction module to progressively adjust the depth prediction towards the real depth. We train our model on the NYUv2 and KITTI datasets as in-distribution datasets and extensively evaluate the framework on 16 other datasets. Our framework performs remarkably well in the OOD scenarios and outperforms existing state-of-the-art depth completion methods. Our models are released in https://github.com/shenglunch/PSD.

