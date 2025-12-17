---
layout: default
title: LiteVGGT: Boosting Vanilla VGGT via Geometry-aware Cached Token Merging
---

# LiteVGGT: Boosting Vanilla VGGT via Geometry-aware Cached Token Merging

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.04939" target="_blank" class="toolbar-btn">arXiv: 2512.04939v1</a>
    <a href="https://arxiv.org/pdf/2512.04939.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04939v1" 
            onclick="toggleFavorite(this, '2512.04939v1', 'LiteVGGT: Boosting Vanilla VGGT via Geometry-aware Cached Token Merging')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhijian Shu, Cheng Lin, Tao Xie, Wei Yin, Ben Li, Zhiyuan Pu, Weize Li, Yao Yao, Xun Cao, Xiaoyang Guo, Xiao-Xiao Long

**分类**: cs.CV

**发布日期**: 2025-12-04

**🔗 代码/项目**: [PROJECT_PAGE](https://garlicba.github.io/LiteVGGT/)

---

## 💡 一句话要点

**LiteVGGT：通过几何感知缓存Token合并加速VGGT，实现大规模场景高效3D重建。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D重建` `视觉几何Transformer` `模型加速` `Token合并` `几何感知` `缓存机制` `大规模场景`

## 📋 核心要点

1. VGGT等3D视觉模型在处理长序列时计算和内存开销大，限制了其在大规模场景中的应用。
2. LiteVGGT通过几何感知缓存token合并，利用局部token的几何相关性和层间token相似性，减少计算冗余。
3. 实验表明，LiteVGGT实现了高达10倍的加速和显著的内存减少，同时保持了VGGT的核心性能。

## 📝 摘要（中文）

视觉几何基础Transformer (VGGT) 等3D视觉基础模型在几何感知方面取得了显著进展。然而，对于长序列而言，其计算耗时和内存占用较高，限制了其在数百张图像以上的大规模场景中的应用。为了解决这个问题，我们提出了LiteVGGT，实现了高达10倍的加速和显著的内存减少，从而能够高效地处理包含1000张图像的场景。我们为3D重建推导出了两个关键见解：(1) 来自局部图像区域的tokens具有固有的几何相关性，导致高度相似性和计算冗余；(2) 相邻网络层之间的token相似性保持稳定，允许重复使用合并决策。在这些见解的指导下，我们设计了一种简单而有效的策略，称为几何感知缓存token合并。我们分析每个token的几何重要性，优化anchor token的选择，以更好地保留用于重建的关键信息。我们还在各层之间缓存和重用合并索引，从而在最小化精度影响的同时显著降低延迟。该策略保留了VGGT的核心性能，从而可以进行高效的微调和FP8量化以获得进一步的收益。大量的实验验证了LiteVGGT的有效性、可扩展性和鲁棒性。

## 🔬 方法详解

**问题定义**：VGGT等模型在处理大规模场景（例如包含大量图像的3D重建任务）时，计算量和内存占用过高，难以应用。现有方法的痛点在于对所有tokens进行同等处理，忽略了局部区域tokens的几何相关性和层间token相似性，导致计算冗余。

**核心思路**：论文的核心思路是利用图像局部区域tokens的几何相关性和相邻网络层之间token相似性的稳定性，通过几何感知的缓存token合并策略，减少计算冗余。具体来说，选择具有代表性的anchor tokens，并缓存合并索引，从而加速计算过程。

**技术框架**：LiteVGGT的整体框架基于VGGT，主要改进在于token合并策略。首先，分析每个token的几何重要性，选择合适的anchor tokens。然后，在网络层之间缓存和重用合并索引，避免重复计算。该框架包含几何重要性分析模块、anchor token选择模块和缓存合并索引模块。

**关键创新**：最重要的技术创新点是几何感知缓存token合并策略。与现有方法不同，LiteVGGT不是对所有tokens进行同等处理，而是根据几何重要性选择anchor tokens，并利用层间token相似性的稳定性，缓存和重用合并索引。这种策略在保证精度的前提下，显著降低了计算量和内存占用。

**关键设计**：几何重要性分析可能涉及计算每个token的梯度或注意力权重，选择梯度或权重较高的token作为anchor tokens。缓存合并索引的设计需要考虑缓存大小和查找效率，可以使用哈希表等数据结构。损失函数与VGGT保持一致，网络结构也基于VGGT进行微调。

## 📊 实验亮点

实验结果表明，LiteVGGT在保持VGGT核心性能的同时，实现了高达10倍的加速和显著的内存减少，能够高效处理包含1000张图像的场景。通过高效微调和FP8量化，LiteVGGT可以进一步提升性能。这些结果验证了LiteVGGT的有效性、可扩展性和鲁棒性。

## 🎯 应用场景

LiteVGGT具有广泛的应用前景，包括大规模场景的3D重建、自动驾驶、机器人导航、虚拟现实和增强现实等领域。通过降低计算成本和内存占用，LiteVGGT使得在资源受限的设备上进行大规模3D场景理解成为可能，加速了相关技术的落地和普及，并为未来的三维视觉应用提供了更高效的解决方案。

## 📄 摘要（原文）

> 3D vision foundation models like Visual Geometry Grounded Transformer (VGGT) have advanced greatly in geometric perception. However, it is time-consuming and memory-intensive for long sequences, limiting application to large-scale scenes beyond hundreds of images. To address this, we propose LiteVGGT, achieving up to 10x speedup and substantial memory reduction, enabling efficient processing of 1000-image scenes. We derive two key insights for 3D reconstruction: (1) tokens from local image regions have inherent geometric correlations, leading to high similarity and computational redundancy; (2) token similarity across adjacent network layers remains stable, allowing for reusable merge decisions. Guided by these, we design a simple yet efficient strategy, dubbed geometry-aware cached token merging. We analyze each token's geometric importance, optimizing anchor token selection to better preserve key information for reconstruction. We also cache and reuse merge indices across layers, substantially reducing latency with minimal accuracy impact. This strategy retains VGGT's core performance, enabling efficient fine-tuning and FP8 quantization for further gains. Extensive experiments validate LiteVGGT's effectiveness, scalability, and robustness. Project page: https://garlicba.github.io/LiteVGGT/

