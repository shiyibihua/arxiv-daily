---
layout: default
title: EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes
---

# EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.00771" target="_blank" class="toolbar-btn">arXiv: 2512.00771v1</a>
    <a href="https://arxiv.org/pdf/2512.00771.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00771v1" 
            onclick="toggleFavorite(this, '2512.00771v1', 'EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xiaoshan Wu, Yifei Yu, Xiaoyang Lyu, Yihua Huang, Bo Wang, Baoheng Zhang, Zhongrui Wang, Xiaojuan Qi

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-30

**备注**: Accepted at NeurIPS 2025 (spotlight)

---

## 💡 一句话要点

**EAG3R：事件相机增强的3D几何估计，解决动态和极端光照场景问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D几何估计` `事件相机` `动态场景` `低光照` `多模态融合` `信噪比感知` `光度一致性` `点云重建`

## 📋 核心要点

1. 传统RGB相机在动态物体和极端光照条件下进行3D几何估计时面临挑战，限制了其在自动驾驶和SLAM等领域的应用。
2. EAG3R利用事件相机提供的异步事件流，通过信噪比感知融合机制自适应地结合RGB和事件特征，提升几何估计的鲁棒性。
3. 实验结果表明，EAG3R在动态低光场景中显著优于纯RGB方法，无需额外夜间数据训练即可实现高性能。

## 📝 摘要（中文）

本文提出EAG3R，一种新颖的几何估计框架，利用异步事件流增强基于点云的重建。EAG3R基于MonST3R主干网络，引入了两项关键创新：一是受Retinex启发的图像增强模块和轻量级事件适配器，采用信噪比感知融合机制，自适应地结合RGB和事件特征；二是基于事件的光度一致性损失，增强全局优化过程中的时空一致性。该方法无需在夜间数据上重新训练，即可在具有挑战性的动态低光场景中实现鲁棒的几何估计。大量实验表明，EAG3R在单目深度估计、相机姿态跟踪和动态重建任务中，显著优于最先进的纯RGB方法。

## 🔬 方法详解

**问题定义**：现有基于RGB图像的3D几何估计方法在动态场景和极端光照条件下表现不佳。传统相机曝光时间固定，容易受到运动模糊和光照变化的影响，导致特征提取和匹配困难，进而影响重建精度和鲁棒性。

**核心思路**：利用事件相机对光照变化的快速响应和高动态范围特性，弥补传统RGB相机的不足。通过融合RGB图像和事件流的信息，提高在动态和极端光照条件下几何估计的准确性和鲁棒性。核心在于自适应地融合两种模态的信息，并利用事件信息增强时空一致性。

**技术框架**：EAG3R框架基于MonST3R，主要包含三个模块：1) Retinex启发式图像增强模块，用于提升低光照RGB图像的质量；2) 轻量级事件适配器，用于提取事件特征，并采用信噪比感知融合机制与RGB特征融合；3) 基于事件的光度一致性损失，用于约束全局优化过程，增强时空一致性。整体流程为：输入RGB图像和事件流，分别提取特征并融合，然后进行点云回归，最后通过全局优化得到最终的3D几何估计结果。

**关键创新**：EAG3R的关键创新在于：1) 提出了一种信噪比感知融合机制，能够根据局部可靠性自适应地结合RGB和事件特征，避免了简单融合可能带来的噪声干扰；2) 提出了一种基于事件的光度一致性损失，利用事件流的时空信息，增强全局优化过程中的一致性约束，提高了重建的鲁棒性。

**关键设计**：信噪比感知融合机制通过计算RGB和事件特征的信噪比，作为融合权重的依据。信噪比的计算方式未知，但其目的是为了更可靠地融合两种模态的信息。基于事件的光度一致性损失利用事件流中的时间戳信息，对相邻帧之间的光度变化进行建模，从而约束全局优化过程。具体网络结构和参数设置未知。

## 📊 实验亮点

实验结果表明，EAG3R在单目深度估计、相机姿态跟踪和动态重建任务中均显著优于最先进的纯RGB方法。具体性能提升数据未知，但强调了在具有挑战性的动态低光场景下，EAG3R无需在夜间数据上重新训练即可实现高性能，体现了其良好的泛化能力和实用价值。

## 🎯 应用场景

EAG3R在自动驾驶、机器人导航、SLAM和3D场景重建等领域具有广泛的应用前景。尤其是在光照条件恶劣或存在快速运动物体的场景下，EAG3R能够提供更准确和鲁棒的3D几何信息，从而提高系统的可靠性和安全性。未来，该技术有望应用于夜间或隧道等复杂环境下的自动驾驶，以及动态环境下的机器人操作。

## 📄 摘要（原文）

> Robust 3D geometry estimation from videos is critical for applications such as autonomous navigation, SLAM, and 3D scene reconstruction. Recent methods like DUSt3R demonstrate that regressing dense pointmaps from image pairs enables accurate and efficient pose-free reconstruction. However, existing RGB-only approaches struggle under real-world conditions involving dynamic objects and extreme illumination, due to the inherent limitations of conventional cameras. In this paper, we propose EAG3R, a novel geometry estimation framework that augments pointmap-based reconstruction with asynchronous event streams. Built upon the MonST3R backbone, EAG3R introduces two key innovations: (1) a retinex-inspired image enhancement module and a lightweight event adapter with SNR-aware fusion mechanism that adaptively combines RGB and event features based on local reliability; and (2) a novel event-based photometric consistency loss that reinforces spatiotemporal coherence during global optimization. Our method enables robust geometry estimation in challenging dynamic low-light scenes without requiring retraining on night-time data. Extensive experiments demonstrate that EAG3R significantly outperforms state-of-the-art RGB-only baselines across monocular depth estimation, camera pose tracking, and dynamic reconstruction tasks.

