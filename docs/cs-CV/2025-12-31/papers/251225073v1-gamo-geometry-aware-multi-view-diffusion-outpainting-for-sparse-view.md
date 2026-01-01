---
layout: default
title: "GaMO: Geometry-aware Multi-view Diffusion Outpainting for Sparse-View 3D Reconstruction"
---

# GaMO: Geometry-aware Multi-view Diffusion Outpainting for Sparse-View 3D Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.25073" class="toolbar-btn" target="_blank">📄 arXiv: 2512.25073v1</a>
  <a href="https://arxiv.org/pdf/2512.25073.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.25073v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.25073v1', 'GaMO: Geometry-aware Multi-view Diffusion Outpainting for Sparse-View 3D Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi-Chuan Huang, Hao-Jen Chien, Chin-Yang Lin, Ying-Huan Chen, Yu-Lun Liu

**分类**: cs.CV

**发布日期**: 2025-12-31

**备注**: Project page: https://yichuanh.github.io/GaMO/

**🔗 代码/项目**: [PROJECT_PAGE](https://yichuanh.github.io/GaMO/)

---

## 💡 一句话要点

**GaMO：基于几何感知的多视角扩散外绘用于稀疏视角3D重建**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `3D重建` `稀疏视角` `多视角外绘` `扩散模型` `几何感知` `零样本学习` `图像生成`

## 📋 核心要点

1. 现有3D重建方法在密集多视角图像中表现出色，但在输入视角有限时效果不佳，缺乏对已知视角外围的充分覆盖。
2. GaMO通过多视角外绘扩展现有相机姿态的视野，而非生成新视点，从而在本质上保持了几何一致性，并扩大了场景覆盖范围。
3. GaMO在Replica和ScanNet++数据集上实现了最先进的重建质量，且速度比现有扩散方法快25倍，处理时间缩短至10分钟以内。

## 📝 摘要（中文）

本文提出GaMO（Geometry-aware Multi-view Outpainter），一个通过多视角外绘重新构建稀疏视角3D重建的框架。与生成新视点不同，GaMO从现有相机姿态扩展视野，从而固有地保持了几何一致性，同时提供了更广泛的场景覆盖。该方法采用多视角条件和几何感知去噪策略，以零样本方式运行，无需训练。在Replica和ScanNet++上的大量实验表明，在3、6和9个输入视角下，GaMO实现了最先进的重建质量，在PSNR和LPIPS方面优于现有方法，同时比最先进的基于扩散的方法实现了25倍的加速，处理时间低于10分钟。

## 🔬 方法详解

**问题定义**：论文旨在解决稀疏视角下的3D重建问题。现有方法在视角稀疏时，重建质量显著下降，主要痛点包括：覆盖范围不足，无法有效推断已知视角之外的区域；几何不一致性，生成的视图之间缺乏空间一致性；计算成本高昂，特别是基于扩散模型的方法，推理速度慢。

**核心思路**：GaMO的核心思路是将稀疏视角3D重建问题转化为多视角外绘问题。通过从现有相机姿态向外扩展视野，而不是生成全新的相机姿态，可以自然地保持几何一致性，并提供更广阔的场景覆盖范围。这种方法避免了生成新视点带来的几何校正问题，简化了重建流程。

**技术框架**：GaMO框架主要包含以下几个关键模块：1) 多视角条件输入：利用多个已知视角的图像作为条件信息。2) 几何感知扩散模型：使用扩散模型进行图像外绘，并融入几何信息以保证生成图像的几何一致性。3) 零样本推理：整个过程无需训练，直接利用预训练的扩散模型进行推理。框架通过迭代的去噪过程，逐步生成扩展视野的图像。

**关键创新**：GaMO的关键创新在于将多视角外绘应用于稀疏视角3D重建，并设计了几何感知的扩散模型。与以往生成新视角的扩散方法不同，GaMO通过扩展现有视角的视野，避免了复杂的几何校正，并显著提高了重建速度。此外，零样本推理方式也避免了针对特定场景的训练需求。

**关键设计**：GaMO的关键设计包括：1) 多视角条件融合策略，如何有效地将多个视角的图像信息融入到扩散模型的去噪过程中。2) 几何感知去噪策略，具体如何将几何信息（例如深度信息或相机参数）融入到扩散模型的去噪过程中，以保证生成图像的几何一致性。3) 扩散模型的选择和参数设置，例如使用何种扩散模型架构，以及如何调整扩散模型的参数以获得最佳的重建效果。论文中可能还涉及损失函数的设计，用于指导扩散模型的训练（如果使用了微调）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25073v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25073v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.25073v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

GaMO在Replica和ScanNet++数据集上取得了显著的性能提升。在3、6和9个输入视角下，GaMO在PSNR和LPIPS指标上均优于现有方法，实现了最先进的重建质量。更重要的是，GaMO比最先进的基于扩散的方法实现了25倍的加速，处理时间缩短至10分钟以内，大大提高了重建效率。

## 🎯 应用场景

GaMO在机器人导航、虚拟现实、增强现实、自动驾驶等领域具有广泛的应用前景。该技术可以利用少量图像快速重建场景，降低了对传感器数量和计算资源的需求。在文物保护领域，GaMO可以用于快速重建文物的三维模型，方便研究和展示。未来，该技术有望应用于实时三维重建，为用户提供更加沉浸式的体验。

## 📄 摘要（原文）

> Recent advances in 3D reconstruction have achieved remarkable progress in high-quality scene capture from dense multi-view imagery, yet struggle when input views are limited. Various approaches, including regularization techniques, semantic priors, and geometric constraints, have been implemented to address this challenge. Latest diffusion-based methods have demonstrated substantial improvements by generating novel views from new camera poses to augment training data, surpassing earlier regularization and prior-based techniques. Despite this progress, we identify three critical limitations in these state-of-the-art approaches: inadequate coverage beyond known view peripheries, geometric inconsistencies across generated views, and computationally expensive pipelines. We introduce GaMO (Geometry-aware Multi-view Outpainter), a framework that reformulates sparse-view reconstruction through multi-view outpainting. Instead of generating new viewpoints, GaMO expands the field of view from existing camera poses, which inherently preserves geometric consistency while providing broader scene coverage. Our approach employs multi-view conditioning and geometry-aware denoising strategies in a zero-shot manner without training. Extensive experiments on Replica and ScanNet++ demonstrate state-of-the-art reconstruction quality across 3, 6, and 9 input views, outperforming prior methods in PSNR and LPIPS, while achieving a $25\times$ speedup over SOTA diffusion-based methods with processing time under 10 minutes. Project page: https://yichuanh.github.io/GaMO/

