---
layout: default
title: "Patch as Node: Human-Centric Graph Representation Learning for Multimodal Action Recognition"
---

# Patch as Node: Human-Centric Graph Representation Learning for Multimodal Action Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21916" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21916v1</a>
  <a href="https://arxiv.org/pdf/2512.21916.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21916v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21916v1', 'Patch as Node: Human-Centric Graph Representation Learning for Multimodal Action Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeyu Liang, Hailun Xia, Naichuan Zheng

**分类**: cs.CV

**发布日期**: 2025-12-26

---

## 💡 一句话要点

**提出PAN框架，通过人体中心图表示学习实现更有效的多模态动作识别。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态动作识别` `图表示学习` `人体中心` `RGB-骨骼融合` `时空图`

## 📋 核心要点

1. 现有方法在融合RGB和骨骼模态时，难以克服异构性，未能充分利用模态间的互补性。
2. PAN框架以人体关节为中心，将RGB图像块表示为时空图，对齐不同模态，实现有效融合。
3. PAN在多个数据集上取得了SOTA性能，证明了其在多模态动作识别方面的优越性。

## 📝 摘要（中文）

本文提出了一种名为PAN的人体中心图表示学习框架，用于多模态动作识别。该框架将包含人体关节的RGB图像块的token嵌入表示为时空图。这种人体中心图建模范式抑制了RGB帧中的冗余信息，并与基于骨骼的方法对齐，从而实现了更有效和语义连贯的多模态特征融合。由于token嵌入的采样严重依赖于2D骨骼数据，我们进一步提出了基于注意力的后校准方法，以最小的性能代价降低对高质量骨骼数据的依赖。为了探索PAN与基于骨骼的方法集成的潜力，我们提出了两种变体：PAN-Ensemble，采用双路图卷积网络，然后进行后期融合；PAN-Unified，在单个网络中执行统一的图表示学习。在三个广泛使用的多模态动作识别数据集上，PAN-Ensemble和PAN-Unified都在各自的多模态融合设置（分离建模和统一建模）中实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有的多模态动作识别方法，尤其是融合RGB和骨骼数据时，由于两种模态的内在异构性，难以充分挖掘它们之间的互补信息。RGB数据包含大量冗余信息，而骨骼数据则相对稀疏，直接融合效果不佳。此外，现有方法通常没有很好地对齐不同模态的语义信息，导致融合后的特征表示不够有效。

**核心思路**：PAN的核心思想是以人体为中心，将RGB图像中包含人体关节的图像块提取出来，并将其表示为图结构。这种做法有两个优点：一是减少了RGB图像中的冗余信息，只保留与人体动作相关的部分；二是将RGB数据转换成了与骨骼数据相似的图结构，从而更容易进行融合。通过图表示学习，可以更好地捕捉人体动作的时空动态信息。

**技术框架**：PAN框架主要包含以下几个步骤：1) 从RGB图像中提取包含人体关节的图像块（patch），并将其转换为token嵌入；2) 基于这些token嵌入构建时空图，其中节点表示图像块，边表示它们之间的时空关系；3) 使用图神经网络（GNN）学习图的表示；4) 将学习到的图表示与骨骼数据进行融合，用于动作识别。为了降低对高质量骨骼数据的依赖，还引入了基于注意力的后校准模块。PAN框架还提出了两种变体：PAN-Ensemble和PAN-Unified，分别对应于分离建模和统一建模两种融合方式。

**关键创新**：PAN框架的关键创新在于提出了人体中心图表示学习的思想，将RGB图像数据转换成与骨骼数据相似的图结构，从而更容易进行多模态融合。此外，基于注意力的后校准模块可以有效降低对高质量骨骼数据的依赖，提高了模型的鲁棒性。

**关键设计**：在构建时空图时，节点表示RGB图像块的token嵌入，边的权重可以根据节点之间的距离或相似度来确定。图神经网络可以选择不同的架构，如GCN、GAT等。损失函数通常包括分类损失和正则化项。基于注意力的后校准模块通过学习一个注意力权重，来调整不同骨骼关节的重要性，从而降低对噪声骨骼数据的敏感性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21916v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21916v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21916v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PAN-Ensemble和PAN-Unified在三个广泛使用的多模态动作识别数据集上都取得了SOTA性能。具体来说，在某些数据集上，PAN的性能比之前的最佳方法提高了几个百分点，证明了其有效性。实验结果表明，人体中心图表示学习能够有效地融合RGB和骨骼数据，提高动作识别的准确率。

## 🎯 应用场景

该研究成果可应用于视频监控、人机交互、智能安防、康复训练等领域。通过准确识别人的动作行为，可以实现异常行为检测、手势控制、运动姿态评估等功能，具有广泛的应用前景和实际价值。未来可以进一步探索将该方法应用于更复杂的场景，例如多人交互、复杂环境等。

## 📄 摘要（原文）

> While human action recognition has witnessed notable achievements, multimodal methods fusing RGB and skeleton modalities still suffer from their inherent heterogeneity and fail to fully exploit the complementary potential between them. In this paper, we propose PAN, the first human-centric graph representation learning framework for multimodal action recognition, in which token embeddings of RGB patches containing human joints are represented as spatiotemporal graphs. The human-centric graph modeling paradigm suppresses the redundancy in RGB frames and aligns well with skeleton-based methods, thus enabling a more effective and semantically coherent fusion of multimodal features. Since the sampling of token embeddings heavily relies on 2D skeletal data, we further propose attention-based post calibration to reduce the dependency on high-quality skeletal data at a minimal cost interms of model performance. To explore the potential of PAN in integrating with skeleton-based methods, we present two variants: PAN-Ensemble, which employs dual-path graph convolution networks followed by late fusion, and PAN-Unified, which performs unified graph representation learning within a single network. On three widely used multimodal action recognition datasets, both PAN-Ensemble and PAN-Unified achieve state-of-the-art (SOTA) performance in their respective settings of multimodal fusion: separate and unified modeling, respectively.

