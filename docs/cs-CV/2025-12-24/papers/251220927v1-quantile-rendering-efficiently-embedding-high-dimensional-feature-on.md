---
layout: default
title: "Quantile Rendering: Efficiently Embedding High-dimensional Feature on 3D Gaussian Splatting"
---

# Quantile Rendering: Efficiently Embedding High-dimensional Feature on 3D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20927" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20927v1</a>
  <a href="https://arxiv.org/pdf/2512.20927.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20927v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20927v1', 'Quantile Rendering: Efficiently Embedding High-dimensional Feature on 3D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yoonwoo Jeong, Cheng Sun, Frank Wang, Minsu Cho, Jaesung Choe

**分类**: cs.CV

**发布日期**: 2025-12-24

**备注**: Will be updated

---

## 💡 一句话要点

**提出Quantile Rendering，高效嵌入高维特征于3D高斯溅射，提升开放词汇分割性能。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `开放词汇分割` `体渲染` `高维特征` `Quantile Rendering`

## 📋 核心要点

1. 现有3D开放词汇分割方法在渲染高维特征时效率低下，且特征压缩易造成信息损失，影响分割质量。
2. Q-Render通过稀疏采样光线上具有主导影响的高斯，避免了密集采样，从而高效处理高维特征。
3. 实验表明，该方法在ScanNet和LeRF数据集上优于现有技术，并实现了显著的渲染加速。

## 📝 摘要（中文）

本文提出了一种新的渲染策略Quantile Rendering (Q-Render)，用于高效处理3D高斯溅射中的高维特征，以解决开放词汇分割(OVS)在3D领域中面临的挑战。现有方法通常采用码本或特征压缩，导致信息损失，从而降低分割质量。Q-Render不同于传统的体渲染，它不是密集采样与每条光线相交的所有3D高斯，而是稀疏采样那些沿光线具有主导影响的高斯。此外，本文还将Q-Render集成到一个可泛化的3D神经网络中，提出了高斯溅射网络(GS-Net)，以可泛化的方式预测高斯特征。在ScanNet和LeRF上的大量实验表明，该框架优于最先进的方法，同时实现了近似43.7倍的实时渲染加速（针对512维特征图）。代码将会公开。

## 🔬 方法详解

**问题定义**：论文旨在解决3D开放词汇分割中，高维特征渲染效率低下的问题。现有方法如使用码本或特征压缩，虽然能降低计算量，但会造成信息损失，从而降低分割精度。因此，如何在保证分割质量的前提下，提升高维特征的渲染效率是本文要解决的核心问题。

**核心思路**：论文的核心思路是提出Quantile Rendering (Q-Render)，一种稀疏采样的渲染策略。Q-Render不再像传统体渲染那样密集采样所有与光线相交的3D高斯，而是只采样那些对光线贡献最大的高斯。这样可以显著减少采样数量，从而提高渲染效率。

**技术框架**：整体框架包含两个主要部分：首先，使用Gaussian Splatting Network (GS-Net) 预测可泛化的高斯特征。GS-Net是一个3D神经网络，能够学习场景的几何和语义信息，并预测每个高斯的特征向量。其次，使用Q-Render渲染这些高斯特征，得到最终的分割结果。Q-Render根据每个高斯对光线的贡献度进行排序，并只采样贡献度最高的一部分高斯。

**关键创新**：最重要的技术创新点在于Q-Render的稀疏采样策略。与传统的密集采样方法相比，Q-Render能够显著减少采样数量，从而提高渲染效率，同时避免了特征压缩带来的信息损失。此外，GS-Net的可泛化特征预测能力也是一个重要的创新点，使得该方法能够应用于不同的场景和数据集。

**关键设计**：Q-Render的关键设计在于如何确定哪些高斯对光线具有主导影响。论文采用了一种基于分位数的采样方法，即选择对光线透明度贡献最大的前k%的高斯进行采样。具体来说，对于每条光线，首先计算每个高斯的透明度权重，然后根据权重对高斯进行排序，最后选择权重最高的k%的高斯进行采样。k的具体数值需要根据实际情况进行调整，以在渲染效率和分割精度之间取得平衡。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20927v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20927v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20927v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Q-Render在ScanNet和LeRF数据集上均取得了优于现有方法的性能。尤其是在渲染512维特征图时，实现了约43.7倍的渲染加速，同时保持了较高的分割精度。这表明Q-Render在处理高维特征时具有显著的效率优势。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、虚拟现实/增强现实等领域。通过高效地渲染高维语义特征，可以使机器更好地理解周围环境，从而实现更智能的交互和决策。未来，该方法有望扩展到更复杂的场景和任务中，例如三维场景编辑、三维物体检测等。

## 📄 摘要（原文）

> Recent advancements in computer vision have successfully extended Open-vocabulary segmentation (OVS) to the 3D domain by leveraging 3D Gaussian Splatting (3D-GS). Despite this progress, efficiently rendering the high-dimensional features required for open-vocabulary queries poses a significant challenge. Existing methods employ codebooks or feature compression, causing information loss, thereby degrading segmentation quality. To address this limitation, we introduce Quantile Rendering (Q-Render), a novel rendering strategy for 3D Gaussians that efficiently handles high-dimensional features while maintaining high fidelity. Unlike conventional volume rendering, which densely samples all 3D Gaussians intersecting each ray, Q-Render sparsely samples only those with dominant influence along the ray. By integrating Q-Render into a generalizable 3D neural network, we also propose Gaussian Splatting Network (GS-Net), which predicts Gaussian features in a generalizable manner. Extensive experiments on ScanNet and LeRF demonstrate that our framework outperforms state-of-the-art methods, while enabling real-time rendering with an approximate ~43.7x speedup on 512-D feature maps. Code will be made publicly available.

