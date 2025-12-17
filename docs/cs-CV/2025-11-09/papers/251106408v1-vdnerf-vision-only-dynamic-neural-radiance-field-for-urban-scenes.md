---
layout: default
title: VDNeRF: Vision-only Dynamic Neural Radiance Field for Urban Scenes
---

# VDNeRF: Vision-only Dynamic Neural Radiance Field for Urban Scenes

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.06408" target="_blank" class="toolbar-btn">arXiv: 2511.06408v1</a>
    <a href="https://arxiv.org/pdf/2511.06408.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06408v1" 
            onclick="toggleFavorite(this, '2511.06408v1', 'VDNeRF: Vision-only Dynamic Neural Radiance Field for Urban Scenes')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhengyu Zou, Jingfeng Li, Hao Li, Xiaolei Hou, Jinwen Hu, Jingkun Chen, Lechao Cheng, Dingwen Zhang

**分类**: cs.CV

**发布日期**: 2025-11-09

---

## 💡 一句话要点

**提出VDNeRF以解决动态城市场景中的相机姿态估计问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `动态神经辐射场` `相机姿态估计` `城市场景重建` `自监督学习` `三维场景流`

## 📋 核心要点

1. 现有NeRF方法在动态城市场景中面临相机姿态估计不准确和动态物体重建困难的挑战。
2. VDNeRF通过视觉信息恢复相机轨迹，并使用两个NeRF模型分别处理静态和动态元素，避免了对额外传感器数据的依赖。
3. 实验结果显示，VDNeRF在主流城市驾驶数据集上，超越了最先进的无姿态NeRF方法，提升了相机姿态估计和动态视角合成的性能。

## 📝 摘要（中文）

神经辐射场（NeRF）通过已知相机姿态的图像集隐式建模连续三维场景，从而实现逼真的新视角渲染。然而，现有NeRF方法在自动驾驶和机器人感知等应用中面临挑战，主要是由于准确捕捉相机姿态的困难以及处理大规模动态环境的局限性。为了解决这些问题，本文提出了视觉专用动态NeRF（VDNeRF），该方法无需额外的相机姿态信息或昂贵的传感器数据，能够准确恢复相机轨迹并学习动态城市场景的时空表示。VDNeRF采用两个独立的NeRF模型共同重建场景，其中静态NeRF模型优化相机姿态和静态背景，而动态NeRF模型结合三维场景流以确保动态物体的准确一致重建。通过有效的训练框架，VDNeRF实现了稳健的相机姿态估计和静态与动态元素的自监督分解。大量评估表明，VDNeRF在相机姿态估计和动态新视角合成方面超越了现有的无姿态NeRF方法。

## 🔬 方法详解

**问题定义**：本文旨在解决动态城市场景中相机姿态估计不准确和动态物体重建困难的问题。现有方法在捕捉相机姿态和处理大规模动态环境时存在显著局限性。

**核心思路**：VDNeRF的核心思路是通过视觉信息恢复相机轨迹，并利用两个独立的NeRF模型分别处理静态背景和动态物体，从而实现高质量的场景重建。

**技术框架**：VDNeRF的整体架构包括两个主要模块：静态NeRF模型和动态NeRF模型。静态NeRF模型负责优化相机姿态和静态背景，而动态NeRF模型则结合三维场景流来处理动态物体。

**关键创新**：VDNeRF的关键创新在于设计了一种有效的训练框架，能够实现稳健的相机姿态估计和静态与动态元素的自监督分解。这一方法与现有的依赖额外传感器数据的NeRF方法本质上不同。

**关键设计**：在关键设计方面，VDNeRF采用了特定的损失函数来优化相机姿态和场景重建，同时在网络结构上进行了优化，以确保动态物体的准确重建和一致性。具体的参数设置和网络架构细节在论文中进行了详细描述。

## 📊 实验亮点

在实验中，VDNeRF在主流城市驾驶数据集上表现优异，相比于最先进的无姿态NeRF方法，VDNeRF在相机姿态估计和动态新视角合成方面均有显著提升，具体性能数据未详细列出，但整体效果超越了现有技术。

## 🎯 应用场景

VDNeRF的研究成果在自动驾驶、机器人感知和虚拟现实等领域具有广泛的应用潜力。通过提供高质量的动态场景重建，VDNeRF能够提升自动驾驶系统的环境感知能力，并为机器人在复杂城市环境中的导航提供支持。此外，该方法的自监督特性降低了对昂贵传感器的依赖，具有重要的实际价值。

## 📄 摘要（原文）

> Neural Radiance Fields (NeRFs) implicitly model continuous three-dimensional scenes using a set of images with known camera poses, enabling the rendering of photorealistic novel views. However, existing NeRF-based methods encounter challenges in applications such as autonomous driving and robotic perception, primarily due to the difficulty of capturing accurate camera poses and limitations in handling large-scale dynamic environments. To address these issues, we propose Vision-only Dynamic NeRF (VDNeRF), a method that accurately recovers camera trajectories and learns spatiotemporal representations for dynamic urban scenes without requiring additional camera pose information or expensive sensor data. VDNeRF employs two separate NeRF models to jointly reconstruct the scene. The static NeRF model optimizes camera poses and static background, while the dynamic NeRF model incorporates the 3D scene flow to ensure accurate and consistent reconstruction of dynamic objects. To address the ambiguity between camera motion and independent object motion, we design an effective and powerful training framework to achieve robust camera pose estimation and self-supervised decomposition of static and dynamic elements in a scene. Extensive evaluations on mainstream urban driving datasets demonstrate that VDNeRF surpasses state-of-the-art NeRF-based pose-free methods in both camera pose estimation and dynamic novel view synthesis.

