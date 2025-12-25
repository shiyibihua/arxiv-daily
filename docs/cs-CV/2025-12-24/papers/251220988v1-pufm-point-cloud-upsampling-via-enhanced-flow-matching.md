---
layout: default
title: "PUFM++: Point Cloud Upsampling via Enhanced Flow Matching"
---

# PUFM++: Point Cloud Upsampling via Enhanced Flow Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20988" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20988v1</a>
  <a href="https://arxiv.org/pdf/2512.20988.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20988v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20988v1', 'PUFM++: Point Cloud Upsampling via Enhanced Flow Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhi-Song Liu, Chenhang He, Roland Maier, Andreas Rupp

**分类**: cs.CV

**发布日期**: 2025-12-24

**备注**: 21 pages, 15 figures

**🔗 代码/项目**: [GITHUB](https://github.com/Holmes-Alan/Enhanced_PUFM)

---

## 💡 一句话要点

**提出PUFM++以解决稀疏点云上采样问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `点云上采样` `流匹配` `生成建模` `计算机视觉` `三维重建`

## 📋 核心要点

1. 现有的点云上采样方法在处理稀疏和噪声输入时常常面临几何保真度不足和鲁棒性差的问题。
2. 论文提出了一种两阶段流匹配策略，通过直接流和噪声扰动样本的结合，提升点云重建的质量和一致性。
3. 实验结果显示，PUFM++在多个基准和真实场景中均超越了现有方法，提供了更高的视觉保真度和定量准确性。

## 📝 摘要（中文）

近年来，生成建模的进展为高质量点云上采样展现了强大的潜力。本文提出了PUFM++，一种增强的流匹配框架，用于从稀疏、噪声和部分观测中重建密集且准确的点云。PUFM++在三个关键方面改进了流匹配：几何保真度、对不完美输入的鲁棒性，以及与下游基于表面的任务的一致性。我们引入了两阶段流匹配策略，首先从稀疏输入学习直接的流，然后利用噪声扰动样本进行精炼。为了加速和稳定推理，我们提出了一种基于插值行为的数据驱动自适应时间调度器。此外，我们在采样过程中施加了流形约束，确保生成的点与基础表面对齐。最后，结合递归接口网络（RIN）增强层次特征交互，提高重建质量。大量实验表明，PUFM++在点云上采样中设定了新的最先进水平。

## 🔬 方法详解

**问题定义**：本文旨在解决从稀疏、噪声和部分观测中重建高质量点云的挑战。现有方法在几何保真度和对不完美输入的鲁棒性方面存在不足，导致重建效果不佳。

**核心思路**：PUFM++的核心思路是通过两阶段流匹配策略，首先学习稀疏输入到密集目标的直接流，然后利用噪声扰动样本进行精炼，以更好地逼近终端边际分布。

**技术框架**：整体架构包括两个主要阶段：第一阶段是直接流学习，第二阶段是基于噪声样本的流精炼。同时引入数据驱动的自适应时间调度器和流形约束，确保生成点与基础表面对齐。

**关键创新**：最重要的创新在于引入了两阶段流匹配策略和自适应时间调度器，这与现有方法的单一流匹配策略形成鲜明对比，显著提升了重建质量和效率。

**关键设计**：在设计中，采用了递归接口网络（RIN）以增强层次特征交互，并在采样过程中施加流形约束，确保生成点的几何一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20988v1/fig/overall_fm.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20988v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20988v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PUFM++在多个合成基准和真实场景中表现出色，相较于现有最先进方法，视觉保真度和定量准确性均有显著提升，具体性能数据表明在多个任务中均达到了新的最佳水平。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、机器人导航、虚拟现实和增强现实等。高质量的点云重建能够提升环境感知和三维重建的准确性，进而推动相关技术的发展和应用。未来，PUFM++有望在自动驾驶、城市建模等领域发挥重要作用。

## 📄 摘要（原文）

> Recent advances in generative modeling have demonstrated strong promise for high-quality point cloud upsampling. In this work, we present PUFM++, an enhanced flow-matching framework for reconstructing dense and accurate point clouds from sparse, noisy, and partial observations. PUFM++ improves flow matching along three key axes: (i) geometric fidelity, (ii) robustness to imperfect input, and (iii) consistency with downstream surface-based tasks. We introduce a two-stage flow-matching strategy that first learns a direct, straight-path flow from sparse inputs to dense targets, and then refines it using noise-perturbed samples to approximate the terminal marginal distribution better. To accelerate and stabilize inference, we propose a data-driven adaptive time scheduler that improves sampling efficiency based on interpolation behavior. We further impose on-manifold constraints during sampling to ensure that generated points remain aligned with the underlying surface. Finally, we incorporate a recurrent interface network~(RIN) to strengthen hierarchical feature interactions and boost reconstruction quality. Extensive experiments on synthetic benchmarks and real-world scans show that PUFM++ sets a new state of the art in point cloud upsampling, delivering superior visual fidelity and quantitative accuracy across a wide range of tasks. Code and pretrained models are publicly available at https://github.com/Holmes-Alan/Enhanced_PUFM.

