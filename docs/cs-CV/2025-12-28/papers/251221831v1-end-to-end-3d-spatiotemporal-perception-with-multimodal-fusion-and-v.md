---
layout: default
title: End-to-End 3D Spatiotemporal Perception with Multimodal Fusion and V2X Collaboration
---

# End-to-End 3D Spatiotemporal Perception with Multimodal Fusion and V2X Collaboration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21831" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21831v1</a>
  <a href="https://arxiv.org/pdf/2512.21831.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21831v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21831v1', 'End-to-End 3D Spatiotemporal Perception with Multimodal Fusion and V2X Collaboration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenwei Yang, Yibo Ai, Weidong Zhang

**分类**: cs.CV

**发布日期**: 2025-12-26

**备注**: 19 pages, 19 figures

---

## 💡 一句话要点

**提出XET-V2X，用于V2X协同中多模态融合的端到端3D时空感知。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `V2X协同感知` `多模态融合` `3D目标检测` `目标跟踪` `时空感知`

## 📋 核心要点

1. 现有自动驾驶3D感知方法在遮挡、视角有限和V2X通信延迟等情况下表现不佳，难以保证可靠性。
2. XET-V2X通过多模态融合和V2X协同，在共享时空表示中统一多视角多模态感知，提升感知鲁棒性。
3. 在真实和模拟数据集上的实验表明，XET-V2X在不同通信延迟下，显著提升了检测和跟踪性能。

## 📝 摘要（中文）

本文提出了一种名为XET-V2X的多模态融合端到端跟踪框架，用于V2X协同，旨在统一共享时空表示中的多视角多模态感知。该框架通过双层空间交叉注意力模块（基于多尺度可变形注意力）高效对齐异构视角和模态。首先，聚合多视角图像特征以增强语义一致性，然后，通过更新后的空间查询引导点云融合，从而实现有效的跨模态交互，同时降低计算开销。在真实世界的V2X-Seq-SPD数据集以及模拟的V2X-Sim-V2V和V2X-Sim-V2I基准测试上的实验表明，在不同的通信延迟下，检测和跟踪性能均得到持续提升。定量结果和定性可视化均表明，XET-V2X在复杂的交通场景中实现了鲁棒且时间上稳定的感知。

## 🔬 方法详解

**问题定义**：论文旨在解决V2X协同感知中，由于多视角、多模态数据异构性以及通信延迟带来的3D时空感知难题。现有方法难以有效融合不同视角和模态的信息，并且对通信延迟的鲁棒性较差，导致在复杂交通场景下的感知性能下降。

**核心思路**：论文的核心思路是构建一个端到端的框架，通过共享的时空表示来统一多视角、多模态的数据。利用双层空间交叉注意力机制，先对齐图像特征，再引导点云融合，从而实现高效的跨模态交互，并降低计算复杂度。

**技术框架**：XET-V2X框架包含以下主要模块：1) 多视角图像特征提取；2) 基于多尺度可变形注意力的双层空间交叉注意力模块，用于图像特征聚合和点云融合；3) 3D目标检测与跟踪模块。整体流程是先提取各视角图像特征，然后通过交叉注意力模块进行特征对齐和融合，再利用融合后的特征进行3D目标检测和跟踪。

**关键创新**：论文的关键创新在于提出的双层空间交叉注意力模块。该模块首先利用多尺度可变形注意力聚合多视角图像特征，增强语义一致性，然后利用更新后的空间查询引导点云融合，从而实现高效的跨模态交互，并降低计算开销。这种双层结构能够更好地处理异构数据，并提升计算效率。

**关键设计**：双层空间交叉注意力模块是关键设计。第一层使用多尺度可变形注意力，允许网络关注图像中的关键区域，从而更好地聚合多视角信息。第二层使用更新后的空间查询引导点云融合，确保点云特征能够与图像特征有效对齐。损失函数包括检测损失和跟踪损失，用于优化网络的检测和跟踪性能。具体的网络结构细节和参数设置在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21831v1/images/xet_v2x_diagram.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21831v1/images/xet_v2x_architecture.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21831v1/images/xet_v2x_pc_backbone.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，XET-V2X在V2X-Seq-SPD、V2X-Sim-V2V和V2X-Sim-V2I等数据集上均取得了显著的性能提升。在不同通信延迟下，XET-V2X的检测和跟踪性能均优于现有方法，证明了其在复杂交通场景下的鲁棒性和时间稳定性。具体的性能提升幅度在论文中有详细的定量数据。

## 🎯 应用场景

该研究成果可应用于自动驾驶、智能交通等领域，尤其是在需要V2X协同感知的场景中，例如城市道路、高速公路等。通过提升车辆对周围环境的感知能力，可以提高驾驶安全性、优化交通效率，并为未来的智能交通系统提供技术支撑。

## 📄 摘要（原文）

> Multi-view cooperative perception and multimodal fusion are essential for reliable 3D spatiotemporal understanding in autonomous driving, especially under occlusions, limited viewpoints, and communication delays in V2X scenarios. This paper proposes XET-V2X, a multi-modal fused end-to-end tracking framework for v2x collaboration that unifies multi-view multimodal sensing within a shared spatiotemporal representation. To efficiently align heterogeneous viewpoints and modalities, XET-V2X introduces a dual-layer spatial cross-attention module based on multi-scale deformable attention. Multi-view image features are first aggregated to enhance semantic consistency, followed by point cloud fusion guided by the updated spatial queries, enabling effective cross-modal interaction while reducing computational overhead. Experiments on the real-world V2X-Seq-SPD dataset and the simulated V2X-Sim-V2V and V2X-Sim-V2I benchmarks demonstrate consistent improvements in detection and tracking performance under varying communication delays. Both quantitative results and qualitative visualizations indicate that XET-V2X achieves robust and temporally stable perception in complex traffic scenarios.

