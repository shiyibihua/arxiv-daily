---
layout: default
title: Occlusion-robust Stylization for Drawing-based 3D Animation
---

# Occlusion-robust Stylization for Drawing-based 3D Animation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.00398" class="toolbar-btn" target="_blank">📄 arXiv: 2508.00398v1</a>
  <a href="https://arxiv.org/pdf/2508.00398.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.00398v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.00398v1', 'Occlusion-robust Stylization for Drawing-based 3D Animation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sunjae Yoon, Gwanhyeong Koo, Younghwan Lee, Ji Woo Hong, Chang D. Yoo

**分类**: cs.GR, cs.CV

**发布日期**: 2025-08-01

**备注**: 11 pages, 13 figures, ICCV 2025

---

## 💡 一句话要点

**提出抗遮挡风格化框架以解决绘画基础3D动画中的风格损失问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D动画` `风格化` `遮挡处理` `光流技术` `计算机视觉` `艺术风格保持` `动态运动` `深度学习`

## 📋 核心要点

1. 现有绘画基础3D动画方法在遮挡情况下风格属性质量下降，导致轮廓闪烁和笔触模糊。
2. 本文提出的抗遮挡风格化框架（OSF）通过光流提供抗遮挡的边缘引导，确保风格一致性。
3. OSF在单次运行中完成任务，推理速度提高2.4倍，内存使用减少2.1倍，显著提升了效率。

## 📝 摘要（中文）

3D动画旨在从输入图像和目标3D运动序列生成3D动画视频。近年来，图像到3D模型的进展使得用户手绘图像能够直接生成动画。然而，现有方法在遮挡情况下仍然表现出风格属性的质量下降，导致轮廓闪烁和笔触模糊。为了解决这一问题，本文提出了抗遮挡风格化框架（OSF），通过使用光流提供抗遮挡的边缘引导，确保在动态运动下的风格一致性。此外，OSF在单次运行中完成任务，相比于以往的两阶段方法，推理速度提高了2.4倍，内存使用减少了2.1倍。

## 🔬 方法详解

**问题定义**：现有绘画基础3D动画方法在处理遮挡时，因训练和推理阶段的姿态差异，导致风格属性的质量下降，表现为轮廓闪烁和笔触模糊。

**核心思路**：本文提出的抗遮挡风格化框架（OSF）通过引入光流技术，提供抗遮挡的边缘引导，从而在动态运动下保持风格一致性。

**技术框架**：OSF的整体架构包括输入图像处理、光流计算、边缘引导生成和风格化网络四个主要模块，确保在单次运行中完成风格化任务。

**关键创新**：OSF的最大创新在于其抗遮挡的边缘引导机制，利用光流技术克服了传统方法在遮挡情况下的不足，保证了风格化的稳定性。

**关键设计**：在参数设置上，OSF优化了光流计算的精度，并设计了适应性损失函数，以平衡风格保持与运动动态之间的关系。

## 📊 实验亮点

实验结果表明，OSF在推理速度上提高了2.4倍，内存使用减少了2.1倍，相较于传统的两阶段方法，显著提升了效率和风格保持能力，尤其在动态遮挡场景中表现优异。

## 🎯 应用场景

该研究的潜在应用领域包括动画制作、游戏开发和虚拟现实等，能够为艺术家提供更高效的工具，帮助他们在动态场景中保持独特的艺术风格。未来，OSF可能推动更广泛的创意产业发展，提升用户体验和创作自由度。

## 📄 摘要（原文）

> 3D animation aims to generate a 3D animated video from an input image and a target 3D motion sequence. Recent advances in image-to-3D models enable the creation of animations directly from user-hand drawings. Distinguished from conventional 3D animation, drawing-based 3D animation is crucial to preserve artist's unique style properties, such as rough contours and distinct stroke patterns. However, recent methods still exhibit quality deterioration in style properties, especially under occlusions caused by overlapping body parts, leading to contour flickering and stroke blurring. This occurs due to a `stylization pose gap' between training and inference in stylization networks designed to preserve drawing styles in drawing-based 3D animation systems. The stylization pose gap denotes that input target poses used to train the stylization network are always in occlusion-free poses, while target poses encountered in an inference include diverse occlusions under dynamic motions. To this end, we propose Occlusion-robust Stylization Framework (OSF) for drawing-based 3D animation. We found that while employing object's edge can be effective input prior for guiding stylization, it becomes notably inaccurate when occlusions occur at inference. Thus, our proposed OSF provides occlusion-robust edge guidance for stylization network using optical flow, ensuring a consistent stylization even under occlusions. Furthermore, OSF operates in a single run instead of the previous two-stage method, achieving 2.4x faster inference and 2.1x less memory.

