---
layout: default
title: LAHNet: Local Attentive Hashing Network for Point Cloud Registration
---

# LAHNet: Local Attentive Hashing Network for Point Cloud Registration

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.00927" target="_blank" class="toolbar-btn">arXiv: 2512.00927v1</a>
    <a href="https://arxiv.org/pdf/2512.00927.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00927v1" 
            onclick="toggleFavorite(this, '2512.00927v1', 'LAHNet: Local Attentive Hashing Network for Point Cloud Registration')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Wentao Qu, Xiaoshui Huang, Liang Xiao

**分类**: cs.CV

**发布日期**: 2025-11-30

---

## 💡 一句话要点

**LAHNet：面向点云配准的局部注意力哈希网络，提升特征区分性。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `点云配准` `局部注意力` `哈希网络` `Group Transformer` `长程依赖`

## 📋 核心要点

1. 现有基于学习的点云配准描述子侧重于感知局部信息，特征区分性不足，感受野受限。
2. LAHNet通过Group Transformer捕获长程上下文，利用局部敏感哈希进行窗口划分，并采用跨窗口策略扩大感受野。
3. LAHNet在真实数据集上表现出色，学习到鲁棒且具有区分性的特征，显著提升了点云配准的性能。

## 📝 摘要（中文）

本文提出了一种用于点云配准的局部注意力哈希网络（LAHNet），该网络将局部注意力机制与卷积类算子的局部性归纳偏置引入到点云描述子中。具体而言，设计了一个Group Transformer来捕获点云中点之间合理的长程上下文关系。该模块采用线性邻域搜索策略，即局部敏感哈希，从而能够将点云均匀地划分为非重叠窗口。同时，采用高效的跨窗口策略来进一步扩大合理的特征感受野。此外，基于这种有效的窗口化策略，我们提出了一个交互Transformer来增强点云对中重叠区域的特征交互，通过将每个窗口表示为全局信号来计算重叠矩阵，从而匹配点云对之间的重叠区域。大量结果表明，LAHNet可以学习鲁棒且具有区分性的特征，在真实世界的室内和室外基准测试中实现了显著的配准结果。

## 🔬 方法详解

**问题定义**：现有的基于学习的点云配准方法主要关注局部信息的提取，忽略了点云中点与点之间的长程依赖关系，导致特征的区分性不足，难以应对复杂的场景。此外，感受野的限制也阻碍了模型对全局信息的理解，影响了配准的精度和鲁棒性。

**核心思路**：LAHNet的核心思路是引入局部注意力机制，并结合局部敏感哈希（LSH）进行窗口划分，从而在局部范围内捕获长程上下文信息，并扩大特征的感受野。通过Group Transformer和Interaction Transformer，增强点云特征的表达能力和区分性，最终提升点云配准的性能。

**技术框架**：LAHNet的整体框架包括以下几个主要模块：1) Group Transformer：利用LSH将点云划分为非重叠窗口，并在每个窗口内使用Transformer结构捕获长程上下文信息。2) 跨窗口策略：通过高效的跨窗口操作，进一步扩大特征的感受野，增强全局信息的感知能力。3) Interaction Transformer：计算点云对之间的重叠矩阵，并利用Transformer结构增强重叠区域的特征交互，从而实现更精确的配准。

**关键创新**：LAHNet的关键创新在于将局部注意力机制与LSH相结合，提出了一种新的点云特征提取方法。与传统的基于卷积或PointNet的方法相比，LAHNet能够更好地捕获点云中的长程依赖关系，并扩大特征的感受野。此外，Interaction Transformer的设计也有效地增强了点云对之间的特征交互，提升了配准的精度。

**关键设计**：LAHNet的关键设计包括：1) LSH的参数设置：选择合适的哈希函数和哈希表数量，以保证窗口划分的均匀性和效率。2) Group Transformer的结构：采用多头注意力机制和残差连接，以增强模型的表达能力和鲁棒性。3) 跨窗口策略的实现：设计高效的跨窗口操作，以减少计算量和内存消耗。4) Interaction Transformer的损失函数：设计合适的损失函数，以指导模型学习更具有区分性的特征。

## 📊 实验亮点

LAHNet在多个真实世界的室内和室外点云配准基准测试中取得了显著的成果。实验结果表明，LAHNet能够学习到鲁棒且具有区分性的特征，相比于现有的方法，在配准精度和鲁棒性方面都有显著的提升。具体的数据提升幅度未知，但摘要强调了“significant registration results”。

## 🎯 应用场景

LAHNet在机器人导航、三维重建、自动驾驶等领域具有广泛的应用前景。它可以用于精确地配准不同视角的点云数据，从而实现更准确的环境感知和定位。此外，LAHNet还可以应用于文物保护、医疗影像分析等领域，为相关研究提供技术支持。

## 📄 摘要（原文）

> Most existing learning-based point cloud descriptors for point cloud registration focus on perceiving local information of point clouds to generate distinctive features. However, a reasonable and broader receptive field is essential for enhancing feature distinctiveness. In this paper, we propose a Local Attentive Hashing Network for point cloud registration, called LAHNet, which introduces a local attention mechanism with the inductive bias of locality of convolution-like operators into point cloud descriptors. Specifically, a Group Transformer is designed to capture reasonable long-range context between points. This employs a linear neighborhood search strategy, Locality-Sensitive Hashing, enabling uniformly partitioning point clouds into non-overlapping windows. Meanwhile, an efficient cross-window strategy is adopted to further expand the reasonable feature receptive field. Furthermore, building on this effective windowing strategy, we propose an Interaction Transformer to enhance the feature interactions of the overlap regions within point cloud pairs. This computes an overlap matrix to match overlap regions between point cloud pairs by representing each window as a global signal. Extensive results demonstrate that LAHNet can learn robust and distinctive features, achieving significant registration results on real-world indoor and outdoor benchmarks.

