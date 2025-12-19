---
layout: default
title: SegGraph: Leveraging Graphs of SAM Segments for Few-Shot 3D Part Segmentation
---

# SegGraph: Leveraging Graphs of SAM Segments for Few-Shot 3D Part Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16143" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16143v1</a>
  <a href="https://arxiv.org/pdf/2512.16143.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16143v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16143v1', 'SegGraph: Leveraging Graphs of SAM Segments for Few-Shot 3D Part Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yueyang Hu, Haiyong Jiang, Haoxuan Song, Jun Xiao, Hao Pan

**分类**: cs.CV

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/YueyangHu2000/SegGraph)

---

## 💡 一句话要点

**SegGraph：利用SAM分割图进行少样本3D部件分割**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `少样本学习` `3D部件分割` `图神经网络` `SAM分割` `几何特征学习`

## 📋 核心要点

1. 现有少样本3D部件分割方法在几何结构利用和高质量分割线索聚合方面存在不足，导致分割不准确。
2. SegGraph通过构建SAM分割图，显式学习分割掩码中的几何特征，并利用图神经网络进行特征传播。
3. 实验表明，SegGraph在PartNet-E数据集上显著优于现有方法，尤其在小部件和部件边界分割上表现出色。

## 📝 摘要（中文）

本文提出了一种新颖的少样本3D部件分割框架。最近的研究表明，2D基础模型在低样本3D部件分割方面具有巨大的潜力。然而，如何有效地将来自基础模型的2D知识聚合到3D仍然是一个开放的问题。现有方法要么忽略3D特征学习的几何结构，要么忽略来自SAM的高质量分组线索，导致分割不足和部件标签不一致。我们设计了一种新的基于SAM分割图的传播方法，名为SegGraph，以显式地学习编码在SAM分割掩码中的几何特征。我们的方法通过对分割之间的相互重叠和邻接关系进行建模来编码几何特征，同时保持分割内的语义一致性。我们构建了一个分割图，在概念上类似于地图集，其中节点代表分割，边代表它们之间的空间关系（重叠/邻接）。每个节点自适应地调节2D基础模型特征，然后通过图神经网络传播，以学习全局几何结构。为了加强分割内的语义一致性，我们使用一种新的视角方向加权融合将分割特征映射到3D点，从而衰减来自低质量分割的贡献。在PartNet-E上的大量实验表明，我们的方法优于所有竞争基线至少6.9个百分点的mIoU。进一步的分析表明，SegGraph在小部件和部件边界上实现了特别强的性能，证明了其卓越的几何理解能力。

## 🔬 方法详解

**问题定义**：论文旨在解决少样本3D部件分割问题。现有方法主要存在两个痛点：一是忽略了3D几何结构在特征学习中的作用，二是未能充分利用SAM等2D基础模型提供的优质分割信息，导致分割结果出现欠分割和标签不一致等问题。

**核心思路**：论文的核心思路是构建一个基于SAM分割的图结构（SegGraph），将2D分割信息和3D几何关系进行有效融合。通过图神经网络学习分割之间的关系，并利用视角方向加权融合保证分割内部的语义一致性。这样既能利用2D基础模型的语义信息，又能结合3D几何结构进行更精确的分割。

**技术框架**：SegGraph框架主要包含以下几个阶段：1) 利用SAM等2D基础模型对3D点云进行多视角分割，生成一系列2D分割掩码。2) 基于这些分割掩码构建分割图，其中节点代表分割区域，边代表分割区域之间的空间关系（重叠或邻接）。3) 使用图神经网络在分割图上进行特征传播，学习全局几何结构信息。4) 将分割特征映射回3D点云，并使用视角方向加权融合策略，增强分割内部的语义一致性。5) 最后，使用分割后的特征进行3D部件分割。

**关键创新**：论文的关键创新在于提出了SegGraph结构，将2D分割信息和3D几何关系显式地建模到图结构中。与现有方法相比，SegGraph能够更有效地利用SAM等2D基础模型的分割结果，并结合3D几何信息进行特征学习。此外，视角方向加权融合策略也是一个重要的创新点，它能够有效抑制低质量分割区域对最终分割结果的影响。

**关键设计**：分割图的构建方式是关键设计之一，论文中考虑了分割区域之间的重叠和邻接关系，并使用不同的权重来表示这些关系。图神经网络的选择和训练也是关键，论文中使用了特定的GNN结构，并设计了合适的损失函数来优化模型。视角方向加权融合的具体权重计算方式也需要仔细设计，以保证分割内部的语义一致性。

## 📊 实验亮点

SegGraph在PartNet-E数据集上取得了显著的性能提升，mIoU指标超过所有基线方法至少6.9%。尤其在小部件和部件边界的分割上表现出色，证明了其对几何结构的优秀理解能力。代码已开源，方便研究人员复现和进一步研究。

## 🎯 应用场景

该研究成果可应用于机器人场景理解、自动驾驶、3D内容生成等领域。例如，机器人可以利用该技术更准确地识别和分割物体部件，从而实现更精细的操作和交互。在自动驾驶领域，可以用于识别车辆、行人等目标的不同部件，提高环境感知能力。在3D内容生成领域，可以辅助进行3D模型的部件分割和编辑，提高建模效率。

## 📄 摘要（原文）

> This work presents a novel framework for few-shot 3D part segmentation. Recent advances have demonstrated the significant potential of 2D foundation models for low-shot 3D part segmentation. However, it is still an open problem that how to effectively aggregate 2D knowledge from foundation models to 3D. Existing methods either ignore geometric structures for 3D feature learning or neglects the high-quality grouping clues from SAM, leading to under-segmentation and inconsistent part labels. We devise a novel SAM segment graph-based propagation method, named SegGraph, to explicitly learn geometric features encoded within SAM's segmentation masks. Our method encodes geometric features by modeling mutual overlap and adjacency between segments while preserving intra-segment semantic consistency. We construct a segment graph, conceptually similar to an atlas, where nodes represent segments and edges capture their spatial relationships (overlap/adjacency). Each node adaptively modulates 2D foundation model features, which are then propagated via a graph neural network to learn global geometric structures. To enforce intra-segment semantic consistency, we map segment features to 3D points with a novel view-direction-weighted fusion attenuating contributions from low-quality segments. Extensive experiments on PartNet-E demonstrate that our method outperforms all competing baselines by at least 6.9 percent mIoU. Further analysis reveals that SegGraph achieves particularly strong performance on small components and part boundaries, demonstrating its superior geometric understanding. The code is available at: https://github.com/YueyangHu2000/SegGraph.

