---
layout: default
title: Accelerating 3D Gaussian Splatting with Neural Sorting and Axis-Oriented Rasterization
---

# Accelerating 3D Gaussian Splatting with Neural Sorting and Axis-Oriented Rasterization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.07069" class="toolbar-btn" target="_blank">📄 arXiv: 2506.07069v1</a>
  <a href="https://arxiv.org/pdf/2506.07069.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.07069v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.07069v1', 'Accelerating 3D Gaussian Splatting with Neural Sorting and Axis-Oriented Rasterization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhican Wang, Guanghui He, Dantong Liu, Lingjun Gao, Shell Xu Hu, Chen Zhang, Zhuoran Song, Nicholas Lane, Wayne Luk, Hongxiang Fan

**分类**: cs.GR, cs.AR, cs.CV, cs.LG

**发布日期**: 2025-06-08

**备注**: Preprint. Under review

---

## 💡 一句话要点

**提出轴向光栅化与神经排序以加速3D高斯点云渲染**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯点云` `实时渲染` `神经网络` `光栅化` `排序算法` `能耗优化` `增强现实` `虚拟现实`

## 📋 核心要点

1. 现有3D高斯点云渲染方法在资源受限设备上实现实时渲染面临显著挑战，尤其是在功耗和面积预算紧张的情况下。
2. 本文提出了轴向光栅化和神经排序相结合的创新方法，通过预计算和重用共享项来减少计算冗余，并提高排序效率。
3. 实验结果显示，所提方法在真实场景中实现了23.4至27.8倍的速度提升和28.8至51.4倍的能耗节省，同时保持了渲染质量。

## 📝 摘要（中文）

3D高斯点云渲染（3DGS）因其高质量和高效的视图合成而受到广泛关注，应用于增强现实、虚拟现实、机器人和自动驾驶等领域。然而，资源受限设备上的实时渲染仍然面临挑战。本文提出了一种架构与算法的协同设计，首先通过轴向光栅化减少重复计算，从而降低乘加操作的数量；其次，采用神经排序方法预测无序混合权重，消除昂贵的硬件排序需求；最后，设计了高效的可重构处理阵列以支持光栅化和神经网络推理。实验表明，该设计在保持渲染质量的同时，速度提升达23.4至27.8倍，能耗降低28.8至51.4倍。

## 🔬 方法详解

**问题定义**：本文旨在解决3D高斯点云渲染在资源受限设备上实时渲染的效率问题，现有方法存在计算冗余和排序效率低下的痛点。

**核心思路**：通过引入轴向光栅化技术，预计算并重用共享项，减少乘加操作，同时采用神经网络进行排序，降低硬件开销。

**技术框架**：整体架构包括轴向光栅化模块、神经排序模块和可重构处理阵列，支持高效的渲染和推理过程。

**关键创新**：引入轴向光栅化和神经排序的结合，显著提高了计算效率和资源利用率，与传统方法相比，减少了重复计算和硬件排序的需求。

**关键设计**：设计了专用硬件以支持轴向光栅化，优化了神经网络的训练框架，确保算法的稳定性，并采用了π轨迹瓦片调度以优化高斯重用和内存访问。

## 📊 实验亮点

实验结果显示，所提方法在真实场景中实现了23.4至27.8倍的速度提升和28.8至51.4倍的能耗节省，相较于边缘GPU，显著提高了渲染效率和降低了能耗，同时保持了高质量的渲染效果。

## 🎯 应用场景

该研究的潜在应用领域包括增强现实、虚拟现实、机器人视觉和自动驾驶等，能够在资源受限的设备上实现高效的3D渲染，提升用户体验和系统性能。未来，该技术可能推动更多实时渲染应用的发展，促进相关领域的创新。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has recently gained significant attention for high-quality and efficient view synthesis, making it widely adopted in fields such as AR/VR, robotics, and autonomous driving. Despite its impressive algorithmic performance, real-time rendering on resource-constrained devices remains a major challenge due to tight power and area budgets. This paper presents an architecture-algorithm co-design to address these inefficiencies. First, we reveal substantial redundancy caused by repeated computation of common terms/expressions during the conventional rasterization. To resolve this, we propose axis-oriented rasterization, which pre-computes and reuses shared terms along both the X and Y axes through a dedicated hardware design, effectively reducing multiply-and-add (MAC) operations by up to 63%. Second, by identifying the resource and performance inefficiency of the sorting process, we introduce a novel neural sorting approach that predicts order-independent blending weights using an efficient neural network, eliminating the need for costly hardware sorters. A dedicated training framework is also proposed to improve its algorithmic stability. Third, to uniformly support rasterization and neural network inference, we design an efficient reconfigurable processing array that maximizes hardware utilization and throughput. Furthermore, we introduce a $π$-trajectory tile schedule, inspired by Morton encoding and Hilbert curve, to optimize Gaussian reuse and reduce memory access overhead. Comprehensive experiments demonstrate that the proposed design preserves rendering quality while achieving a speedup of $23.4\sim27.8\times$ and energy savings of $28.8\sim51.4\times$ compared to edge GPUs for real-world scenes. We plan to open-source our design to foster further development in this field.

