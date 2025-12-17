---
layout: default
title: Light-Field Dataset for Disparity Based Depth Estimation
---

# Light-Field Dataset for Disparity Based Depth Estimation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.05866" target="_blank" class="toolbar-btn">arXiv: 2511.05866v1</a>
    <a href="https://arxiv.org/pdf/2511.05866.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.05866v1" 
            onclick="toggleFavorite(this, '2511.05866v1', 'Light-Field Dataset for Disparity Based Depth Estimation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Suresh Nehra, Aupendu Kar, Jayanta Mukhopadhyay, Prabir Kumar Biswas

**分类**: cs.CV

**发布日期**: 2025-11-08

**备注**: This paper has been accepted to ACM ICVGIP 2025

**🔗 代码/项目**: [GITHUB](https://github.com/aupendu/light-field-dataset)

---

## 💡 一句话要点

**提出用于视差深度估计的光场数据集，解决现有数据集的局限性。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `光场图像` `深度估计` `视差` `数据集` `三维重建` `计算机视觉` `Lytro Illum`

## 📋 核心要点

1. 现有的光场数据集在角度信息和空间信息之间存在权衡，且焦点位置对视差影响显著，限制了深度估计算法的开发。
2. 论文提出一个包含真实和合成光场图像的数据集，旨在提供更全面的数据支持，用于设计和测试基于视差的光场深度估计算法。
3. 该数据集包含使用Lytro Illum相机捕获的真实图像，以及使用Blender和机械臂生成的合成图像，涵盖不同视差特性。

## 📝 摘要（中文）

本文介绍了一个公开可用的光场图像数据集，用于支持基于视差的深度估计算法的设计、开发、实现和测试。与传统相机相比，光场相机在主镜头和传感器之间增加了一个二维微透镜阵列。每个微透镜下的传感器像素接收来自主镜头子孔径的光线，从而使图像传感器能够捕获场景点的空间信息和角度分辨率。这种额外的角度信息用于估计三维场景的深度。光场数据中虚拟视点的连续性使得能够使用极线图像（EPI）进行有效的深度估计，并具有强大的遮挡处理能力。然而，角度信息和空间信息之间的权衡非常关键，并且取决于相机的焦点位置。该数据集包含使用Lytro Illum光场相机捕获的285个真实光场图像和13个合成光场图像。此外，还创建了一个具有与真实光场相机相似视差特性的合成数据集，以及一个使用机械龙门系统和Blender创建的真实和合成的立体光场数据集。该数据集可在https://github.com/aupendu/light-field-dataset上公开获取。

## 🔬 方法详解

**问题定义**：现有光场数据集在角度分辨率和空间分辨率之间存在固有的权衡，并且缺乏对焦点位置影响视差的系统性研究。这限制了基于视差的光场深度估计算法的开发和评估，尤其是在处理复杂场景和不同相机参数时。

**核心思路**：论文的核心思路是构建一个包含真实和合成光场图像的综合数据集，该数据集能够覆盖不同的视差范围和相机参数设置。通过提供多样化的数据，研究人员可以更好地理解光场数据的特性，并开发出更鲁棒和准确的深度估计算法。

**技术框架**：该数据集包含三个主要部分：1) 使用Lytro Illum相机捕获的真实光场图像；2) 使用Blender渲染的合成光场图像，旨在模拟真实相机的视差特性；3) 使用机械龙门系统和Blender创建的真实和合成的立体光场数据集。这些数据可以用于训练、验证和测试基于视差的光场深度估计算法。

**关键创新**：该数据集的关键创新在于其多样性和对视差特性的关注。通过包含真实和合成数据，该数据集能够提供更全面的数据支持，并允许研究人员研究不同相机参数和场景条件下的深度估计性能。此外，立体光场数据集的引入为研究立体匹配算法在光场数据上的应用提供了新的机会。

**关键设计**：真实光场图像使用Lytro Illum相机捕获，并进行了校准和预处理。合成光场图像使用Blender渲染，并调整了相机参数以模拟真实相机的视差特性。立体光场数据集使用机械龙门系统精确控制相机的位置，并使用Blender渲染合成场景。数据集的组织结构清晰，并提供了详细的文档说明，方便用户使用。

## 📊 实验亮点

该数据集包含285个真实光场图像和13个合成光场图像，并提供了一个具有与真实光场相机相似视差特性的合成数据集。通过实验验证，该数据集能够有效地支持基于视差的深度估计算法的开发和评估，并为研究光场数据的特性提供了有价值的资源。

## 🎯 应用场景

该数据集可广泛应用于计算机视觉、机器人和三维重建等领域。例如，可用于开发更精确的机器人导航系统，改进三维场景重建算法，以及增强虚拟现实和增强现实体验。此外，该数据集还可以促进光场相机技术的进一步发展。

## 📄 摘要（原文）

> A Light Field (LF) camera consists of an additional two-dimensional array of micro-lenses placed between the main lens and sensor, compared to a conventional camera. The sensor pixels under each micro-lens receive light from a sub-aperture of the main lens. This enables the image sensor to capture both spatial information and the angular resolution of a scene point. This additional angular information is used to estimate the depth of a 3-D scene. The continuum of virtual viewpoints in light field data enables efficient depth estimation using Epipolar Line Images (EPIs) with robust occlusion handling. However, the trade-off between angular information and spatial information is very critical and depends on the focal position of the camera. To design, develop, implement, and test novel disparity-based light field depth estimation algorithms, the availability of suitable light field image datasets is essential. In this paper, a publicly available light field image dataset is introduced and thoroughly described. We have also demonstrated the effect of focal position on the disparity of a 3-D point as well as the shortcomings of the currently available light field dataset. The proposed dataset contains 285 light field images captured using a Lytro Illum LF camera and 13 synthetic LF images. The proposed dataset also comprises a synthetic dataset with similar disparity characteristics to those of a real light field camera. A real and synthetic stereo light field dataset is also created by using a mechanical gantry system and Blender. The dataset is available at https://github.com/aupendu/light-field-dataset.

