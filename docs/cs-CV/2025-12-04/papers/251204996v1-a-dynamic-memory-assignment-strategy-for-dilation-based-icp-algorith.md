---
layout: default
title: A dynamic memory assignment strategy for dilation-based ICP algorithm on embedded GPUs
---

# A dynamic memory assignment strategy for dilation-based ICP algorithm on embedded GPUs

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.04996" target="_blank" class="toolbar-btn">arXiv: 2512.04996v1</a>
    <a href="https://arxiv.org/pdf/2512.04996.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04996v1" 
            onclick="toggleFavorite(this, '2512.04996v1', 'A dynamic memory assignment strategy for dilation-based ICP algorithm on embedded GPUs')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Qiong Chang, Weimin Wang, Junpei Zhong, Jun Miyazaki

**分类**: cs.CV

**发布日期**: 2025-12-04

**🔗 代码/项目**: [GITHUB](https://github.com/changqiong/VANICP4Em.git)

---

## 💡 一句话要点

**针对嵌入式GPU，提出动态内存分配策略优化VANICP点云配准算法。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `点云配准` `ICP算法` `VANICP` `嵌入式GPU` `动态内存分配` `内存优化` `机器人` `计算机视觉`

## 📋 核心要点

1. VANICP算法虽然提升了点云配准效率，但其高内存占用限制了在嵌入式系统上的应用。
2. 论文提出一种GPU导向的动态内存分配策略，专门优化VANICP中膨胀操作的内存使用。
3. 实验结果表明，该策略在保持VANICP原有性能的同时，能够降低超过97%的内存消耗。

## 📝 摘要（中文）

本文提出了一种内存高效的优化策略，用于高性能点云配准算法VANICP，使其能够在硬件资源受限的嵌入式GPU上轻量化执行。VANICP是一种最近发表的加速框架，通过基于膨胀的信息传播机制将全局最近邻搜索转化为局部过程，从而显著提高了基于点云应用的计算效率，极大地降低了NNS的计算复杂度。然而，其原始实现需要大量的内存，这限制了其在嵌入式系统等资源受限环境中的部署。为了解决这个问题，我们提出了一种面向GPU的动态内存分配策略，优化了膨胀操作的内存使用。此外，基于该策略，我们构建了一个增强版本的VANICP框架，在保持原始性能的同时，实现了超过97%的内存消耗降低。源代码已发布在：https://github.com/changqiong/VANICP4Em.git。

## 🔬 方法详解

**问题定义**：VANICP算法虽然在点云配准速度上表现出色，但其内存需求较高，尤其是在进行膨胀操作时。这使得它难以部署在资源受限的嵌入式GPU平台上。现有方法无法在保证性能的同时，有效降低VANICP的内存占用。

**核心思路**：论文的核心思路是通过动态地分配和释放内存来优化膨胀操作的内存使用。膨胀操作需要存储邻域信息，而这些信息并非始终需要同时存在。因此，可以根据实际需要，在GPU上动态地分配和释放内存，从而减少整体的内存占用。

**技术框架**：该方法主要包含以下几个阶段：1. 分析VANICP算法中膨胀操作的内存使用情况；2. 设计动态内存分配策略，确定何时分配和释放内存；3. 在GPU上实现该策略，并与VANICP算法集成；4. 评估优化后的VANICP算法在嵌入式GPU上的性能和内存占用。

**关键创新**：该方法最重要的创新点在于提出了一种针对膨胀操作的GPU动态内存分配策略。与静态内存分配相比，该策略能够根据实际需要分配和释放内存，从而显著降低内存占用，而不会影响算法的性能。

**关键设计**：具体的动态内存分配策略包括：1. 在膨胀操作开始前，仅分配当前需要处理的点云数据的邻域信息所需的内存；2. 在处理完一部分点云数据后，释放相应的内存；3. 根据后续需要，动态地分配新的内存。此外，还需要考虑GPU的内存管理机制，选择合适的内存分配和释放函数，以避免内存碎片和性能瓶颈。

## 📊 实验亮点

实验结果表明，所提出的动态内存分配策略能够显著降低VANICP算法的内存占用，降低幅度超过97%，同时保持了原始算法的配准精度和速度。这使得VANICP算法能够在嵌入式GPU上高效运行，为资源受限的应用场景提供了新的解决方案。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、三维重建等领域，尤其是在资源受限的嵌入式平台上，如无人机、移动机器人等。通过降低点云配准算法的内存需求，可以使这些设备在有限的硬件资源下实现更精确和实时的环境感知和定位，从而提高其智能化水平和应用范围。

## 📄 摘要（原文）

> This paper proposes a memory-efficient optimization strategy for the high-performance point cloud registration algorithm VANICP, enabling lightweight execution on embedded GPUs with constrained hardware resources. VANICP is a recently published acceleration framework that significantly improves the computational efficiency of point-cloud-based applications. By transforming the global nearest neighbor search into a localized process through a dilation-based information propagation mechanism, VANICP greatly reduces the computational complexity of the NNS. However, its original implementation demands a considerable amount of memory, which restricts its deployment in resource-constrained environments such as embedded systems. To address this issue, we propose a GPU-oriented dynamic memory assignment strategy that optimizes the memory usage of the dilation operation. Furthermore, based on this strategy, we construct an enhanced version of the VANICP framework that achieves over 97% reduction in memory consumption while preserving the original performance. Source code is published on: https://github.com/changqiong/VANICP4Em.git.

