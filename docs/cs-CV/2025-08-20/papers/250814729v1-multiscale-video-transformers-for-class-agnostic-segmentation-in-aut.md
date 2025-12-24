---
layout: default
title: Multiscale Video Transformers for Class Agnostic Segmentation in Autonomous Driving
---

# Multiscale Video Transformers for Class Agnostic Segmentation in Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14729" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14729v1</a>
  <a href="https://arxiv.org/pdf/2508.14729.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14729v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14729v1', 'Multiscale Video Transformers for Class Agnostic Segmentation in Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leila Cheshmi, Mennatullah Siam

**分类**: cs.CV

**发布日期**: 2025-08-20

**备注**: 6 pages, 2 figures, 1 table

---

## 💡 一句话要点

**提出多尺度视频变换器以解决自动驾驶中的类无关分割问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `类无关分割` `多尺度视频变换器` `自动驾驶` `时空特征` `运动线索`

## 📋 核心要点

1. 现有方法在处理未知物体和新场景时面临挑战，通常依赖于已知类别，导致性能下降。
2. 本文提出了一种高效的视频变换器，采用多阶段多尺度查询-记忆解码，能够实现类无关分割。
3. 实验结果显示，该方法在多个数据集上超越了多尺度基线，同时在GPU内存和运行时间上表现优异。

## 📝 摘要（中文）

确保自动驾驶的安全性是一项复杂的挑战，需要处理未知物体和不可预见的驾驶场景。本文开发了多尺度视频变换器，能够仅通过运动线索检测未知物体。视频语义和全景分割通常依赖于训练期间见过的已知类别，忽视了新类别。我们提出了一种高效的视频变换器，能够端到端训练，实现类无关分割，而无需光流。该方法采用多阶段多尺度查询-记忆解码和特定尺度的随机丢弃标记，以确保效率和准确性，同时保持详细的时空特征，利用共享的可学习记忆模块。与传统解码器不同，我们的记忆中心设计在多个尺度上保留高分辨率信息。我们在DAVIS'16、KITTI和Cityscapes上进行了评估，结果表明该方法在GPU内存和运行时间上均表现出色，展示了在安全关键机器人领域进行实时、稳健密集预测的良好方向。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶中类无关分割的问题，现有方法往往依赖于已知类别，无法有效处理未知物体和新场景。

**核心思路**：提出一种多尺度视频变换器，通过运动线索进行未知物体检测，采用多阶段多尺度查询-记忆解码，避免使用光流，从而提高效率和准确性。

**技术框架**：整体架构包括多阶段解码器和共享的可学习记忆模块，能够在多个尺度上保留高分辨率信息。解码器通过随机丢弃标记来优化计算效率。

**关键创新**：本研究的核心创新在于记忆中心设计，能够在多个尺度上有效保留时空特征，与传统解码器相比，避免了特征压缩带来的信息损失。

**关键设计**：采用特定尺度的随机丢弃标记，优化了模型的计算效率；损失函数设计上，确保了分割精度与效率的平衡。

## 📊 实验亮点

实验结果表明，本文提出的方法在DAVIS'16、KITTI和Cityscapes数据集上均优于多尺度基线，尤其在GPU内存和运行时间上表现出色，展示了在实时密集预测中的应用潜力。

## 🎯 应用场景

该研究在自动驾驶领域具有广泛的应用潜力，能够提高对未知物体的检测能力，增强系统的安全性和鲁棒性。未来，该方法可扩展至其他安全关键的机器人应用，如无人机监控和智能交通系统。

## 📄 摘要（原文）

> Ensuring safety in autonomous driving is a complex challenge requiring handling unknown objects and unforeseen driving scenarios. We develop multiscale video transformers capable of detecting unknown objects using only motion cues. Video semantic and panoptic segmentation often relies on known classes seen during training, overlooking novel categories. Recent visual grounding with large language models is computationally expensive, especially for pixel-level output. We propose an efficient video transformer trained end-to-end for class-agnostic segmentation without optical flow. Our method uses multi-stage multiscale query-memory decoding and a scale-specific random drop-token to ensure efficiency and accuracy, maintaining detailed spatiotemporal features with a shared, learnable memory module. Unlike conventional decoders that compress features, our memory-centric design preserves high-resolution information at multiple scales. We evaluate on DAVIS'16, KITTI, and Cityscapes. Our method consistently outperforms multiscale baselines while being efficient in GPU memory and run-time, demonstrating a promising direction for real-time, robust dense prediction in safety-critical robotics.

