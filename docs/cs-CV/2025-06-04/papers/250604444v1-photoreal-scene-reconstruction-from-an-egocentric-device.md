---
layout: default
title: Photoreal Scene Reconstruction from an Egocentric Device
---

# Photoreal Scene Reconstruction from an Egocentric Device

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04444" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04444v1</a>
  <a href="https://arxiv.org/pdf/2506.04444.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04444v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04444v1', 'Photoreal Scene Reconstruction from an Egocentric Device')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaoyang Lv, Maurizio Monge, Ka Chen, Yufeng Zhu, Michael Goesele, Jakob Engel, Zhao Dong, Richard Newcombe

**分类**: cs.CV, cs.AI, cs.GR, cs.HC, cs.MM

**发布日期**: 2025-06-04

**备注**: Paper accepted to SIGGRAPH Conference Paper 2025

---

## 💡 一句话要点

**提出视觉惯性束调整以解决滚动快门相机重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉惯性测程` `滚动快门` `高动态范围` `场景重建` `物理图像形成` `高斯点云` `自我中心设备`

## 📋 核心要点

1. 现有方法在使用自我中心设备进行场景重建时，往往忽略了滚动快门相机的时间戳和运动校准，导致重建精度不足。
2. 论文提出使用视觉惯性束调整（VIBA）来精确校准滚动快门相机的时间戳，并结合物理图像形成模型以改善重建效果。
3. 实验结果表明，采用VIBA后PSNR提升了+1 dB，结合图像形成模型后再提升+1 dB，验证了方法的有效性。

## 📝 摘要（中文）

本文研究了使用自我中心设备进行高动态范围场景的真实感重建所面临的挑战。现有方法通常假设使用设备的视觉惯性测程系统估计的帧速率6DoF位姿，这可能忽略了像素级重建所需的关键细节。研究提出了两项重要发现：首先，与主流工作将RGB相机视为全局快门帧速率相机不同，强调了采用视觉惯性束调整（VIBA）来校准滚动快门RGB相机的精确时间戳和运动的重要性；其次，将基于物理图像形成模型与高斯点云结合，有效解决了RGB相机的滚动快门效应及传感器测量的动态范围。通过在不同光照条件下使用开放源代码的Project Aria设备进行全面评估，结果显示引入VIBA后PSNR提升了+1 dB，结合图像形成模型后又增加了+1 dB。

## 🔬 方法详解

**问题定义**：本文旨在解决使用自我中心设备进行高动态范围场景重建时，滚动快门相机的时间戳和运动校准不足的问题。现有方法通常依赖于视觉惯性测程系统的位姿估计，导致重建精度不高。

**核心思路**：论文的核心思路是引入视觉惯性束调整（VIBA）来精确校准滚动快门相机的时间戳，并结合物理图像形成模型，以更好地处理传感器特性，特别是滚动快门效应。这样的设计确保了重建过程中的像素级精度。

**技术框架**：整体架构包括数据采集、VIBA校准、图像形成模型应用和重建输出四个主要模块。首先，通过自我中心设备采集数据，然后应用VIBA进行时间戳校准，接着结合物理图像形成模型进行重建，最后输出高质量的场景重建结果。

**关键创新**：最重要的技术创新在于将视觉惯性束调整与物理图像形成模型结合，解决了滚动快门相机在动态场景下的重建问题。这一方法与传统的全局快门相机处理方式有本质区别，能够更准确地反映传感器特性。

**关键设计**：在设计中，VIBA的参数设置经过精细调整，以确保时间戳的准确性；物理图像形成模型则考虑了RGB相机的动态范围和滚动快门效应，确保重建结果的真实感和精确度。

## 📊 实验亮点

实验结果显示，采用视觉惯性束调整（VIBA）后，PSNR提升了+1 dB，结合物理图像形成模型后再提升+1 dB，验证了方法在不同光照条件下的有效性。这些结果表明，提出的方法在真实感场景重建中具有显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和机器人导航等场景，能够为这些领域提供更高质量的环境重建技术。通过提高重建精度，未来可以在实时应用中实现更自然的交互体验，推动相关技术的发展。

## 📄 摘要（原文）

> In this paper, we investigate the challenges associated with using egocentric devices to photorealistic reconstruct the scene in high dynamic range. Existing methodologies typically assume using frame-rate 6DoF pose estimated from the device's visual-inertial odometry system, which may neglect crucial details necessary for pixel-accurate reconstruction. This study presents two significant findings. Firstly, in contrast to mainstream work treating RGB camera as global shutter frame-rate camera, we emphasize the importance of employing visual-inertial bundle adjustment (VIBA) to calibrate the precise timestamps and movement of the rolling shutter RGB sensing camera in a high frequency trajectory format, which ensures an accurate calibration of the physical properties of the rolling-shutter camera. Secondly, we incorporate a physical image formation model based into Gaussian Splatting, which effectively addresses the sensor characteristics, including the rolling-shutter effect of RGB cameras and the dynamic ranges measured by sensors. Our proposed formulation is applicable to the widely-used variants of Gaussian Splats representation. We conduct a comprehensive evaluation of our pipeline using the open-source Project Aria device under diverse indoor and outdoor lighting conditions, and further validate it on a Meta Quest3 device. Across all experiments, we observe a consistent visual enhancement of +1 dB in PSNR by incorporating VIBA, with an additional +1 dB achieved through our proposed image formation model. Our complete implementation, evaluation datasets, and recording profile are available at http://www.projectaria.com/photoreal-reconstruction/

