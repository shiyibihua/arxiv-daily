---
layout: default
title: Event-guided 3D Gaussian Splatting for Dynamic Human and Scene Reconstruction
---

# Event-guided 3D Gaussian Splatting for Dynamic Human and Scene Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18566" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18566v1</a>
  <a href="https://arxiv.org/pdf/2509.18566.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18566v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18566v1', 'Event-guided 3D Gaussian Splatting for Dynamic Human and Scene Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoting Yin, Hao Shi, Kailun Yang, Jiajun Zhai, Shangwei Guo, Lin Wang, Kaiwei Wang

**分类**: cs.CV, cs.RO, eess.IV

**发布日期**: 2025-09-23

---

## 💡 一句话要点

**提出事件相机引导的3D高斯溅射方法，用于动态人体和场景重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `事件相机` `3D高斯溅射` `动态重建` `人体建模` `场景重建` `单目视觉` `运动模糊`

## 📋 核心要点

1. 单目视频重建动态人体和静态场景面临运动模糊挑战，尤其是在快速运动下，RGB帧质量下降。
2. 利用事件相机高时间分辨率的优势，提出基于3D高斯溅射的事件引导人体-场景联合重建框架。
3. 通过事件引导的损失函数匹配渲染亮度变化与事件流，提升快速运动区域的重建保真度，并在benchmark上取得SOTA结果。

## 📝 摘要（中文）

本文提出了一种新颖的事件引导的人体-场景重建框架，该框架通过3D高斯溅射从单个单目事件相机联合建模人体和场景。具体来说，统一的3D高斯集合携带可学习的语义属性；只有被分类为人体的Gaussians才进行形变以用于动画，而场景Gaussians保持静态。为了对抗模糊，我们提出了一种事件引导的损失，该损失将连续渲染之间的模拟亮度变化与事件流进行匹配，从而提高了快速移动区域的局部保真度。我们的方法无需外部人体掩模，并简化了管理单独高斯集合的过程。在两个基准数据集ZJU-MoCap-Blur和MMHPSD-Blur上，它提供了最先进的人体-场景重建，与强大的基线相比，在PSNR/SSIM方面有显著提高，并降低了LPIPS，尤其是在高速对象上。

## 🔬 方法详解

**问题定义**：论文旨在解决从单目事件相机数据中，同时重建动态人体和静态场景的问题。现有方法在处理快速运动时，由于RGB图像的运动模糊，重建效果不佳。此外，现有方法通常需要外部人体掩模，增加了复杂性。

**核心思路**：论文的核心思路是利用事件相机的高时间分辨率特性，结合3D高斯溅射技术，实现对动态人体和静态场景的联合建模。通过事件引导的损失函数，将渲染图像的亮度变化与事件流进行匹配，从而在快速运动区域提高重建的保真度。

**技术框架**：整体框架包含以下几个主要模块：1) 使用3D高斯溅射表示场景和人体；2) 为每个高斯赋予可学习的语义属性，区分人体和场景；3) 对人体高斯进行形变以实现动画效果，场景高斯保持静态；4) 使用事件引导的损失函数优化高斯参数，提高重建质量。

**关键创新**：论文的关键创新在于：1) 提出了一种事件引导的损失函数，能够有效利用事件相机数据来提高重建质量，尤其是在快速运动区域；2) 提出了一种统一的3D高斯表示方法，能够同时建模动态人体和静态场景，无需外部人体掩模。

**关键设计**：事件引导的损失函数计算连续渲染帧之间的亮度变化，并将其与事件流进行匹配。具体来说，通过渲染得到两帧图像，计算像素级别的亮度差异，然后与事件相机记录的事件信息进行对比，最小化两者之间的差异。此外，论文还设计了可学习的语义属性，用于区分人体和场景高斯，并使用形变场对人体高斯进行动画。

## 📊 实验亮点

在ZJU-MoCap-Blur和MMHPSD-Blur两个基准数据集上，该方法取得了state-of-the-art的结果。与现有方法相比，在PSNR和SSIM指标上均有显著提升，LPIPS指标也得到了有效降低，尤其是在处理高速运动对象时，优势更加明显。实验结果表明，该方法能够有效利用事件相机数据，提高动态人体和场景的重建质量。

## 🎯 应用场景

该研究成果可应用于虚拟现实、增强现实、人机交互等领域。例如，可以用于创建更加逼真的虚拟化身，或者在AR应用中实现对动态人体和周围环境的实时重建和交互。此外，该技术还可以应用于运动分析、动作捕捉等领域，为相关研究提供更准确的数据支持。

## 📄 摘要（原文）

> Reconstructing dynamic humans together with static scenes from monocular videos remains difficult, especially under fast motion, where RGB frames suffer from motion blur. Event cameras exhibit distinct advantages, e.g., microsecond temporal resolution, making them a superior sensing choice for dynamic human reconstruction. Accordingly, we present a novel event-guided human-scene reconstruction framework that jointly models human and scene from a single monocular event camera via 3D Gaussian Splatting. Specifically, a unified set of 3D Gaussians carries a learnable semantic attribute; only Gaussians classified as human undergo deformation for animation, while scene Gaussians stay static. To combat blur, we propose an event-guided loss that matches simulated brightness changes between consecutive renderings with the event stream, improving local fidelity in fast-moving regions. Our approach removes the need for external human masks and simplifies managing separate Gaussian sets. On two benchmark datasets, ZJU-MoCap-Blur and MMHPSD-Blur, it delivers state-of-the-art human-scene reconstruction, with notable gains over strong baselines in PSNR/SSIM and reduced LPIPS, especially for high-speed subjects.

