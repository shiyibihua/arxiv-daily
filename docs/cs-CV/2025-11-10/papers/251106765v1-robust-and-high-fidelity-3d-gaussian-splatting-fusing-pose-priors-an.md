---
layout: default
title: Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes
---

# Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.06765" target="_blank" class="toolbar-btn">arXiv: 2511.06765v1</a>
    <a href="https://arxiv.org/pdf/2511.06765.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06765v1" 
            onclick="toggleFavorite(this, '2511.06765v1', 'Robust and High-Fidelity 3D Gaussian Splatting: Fusing Pose Priors and Geometry Constraints for Texture-Deficient Outdoor Scenes')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Meijun Guo, Yongliang Shi, Caiyun Liu, Yixiao Feng, Ming Ma, Tinghai Yan, Weining Lu, Bin Liang

**分类**: cs.CV, cs.GR

**发布日期**: 2025-11-10

**备注**: 7 pages, 3 figures. Accepted by IROS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/justinyeah/normal_shape.git)

---

## 💡 一句话要点

**针对纹理缺失的室外场景，提出融合位姿先验和几何约束的鲁棒高保真3D高斯溅射方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `位姿估计` `几何约束` `LiDAR-IMU里程计` `场景重建` `纹理缺失` `室外场景`

## 📋 核心要点

1. 现有3DGS方法在纹理弱或重复的室外场景中，由于位姿估计不稳定和场景几何失真，重建效果不佳。
2. 该论文提出融合LiDAR-IMU里程计的位姿先验，并引入法向量约束和秩正则化来优化3D高斯基元，提升场景表示。
3. 实验结果表明，该方法在位姿估计速度和场景重建质量上均优于传统3DGS方法，尤其在自采集的纹理缺失数据集上表现突出。

## 📝 摘要（中文）

3D高斯溅射(3DGS)因其效率和视觉质量之间的平衡，已成为数字资产创建的关键渲染管线。为了解决大型室外场景中由于几何纹理不一致导致的位姿估计不稳定和场景表示失真问题，我们从位姿估计和场景表示两个方面入手。对于位姿估计，我们利用LiDAR-IMU里程计为大规模环境中的相机提供先验位姿。这些先验位姿约束被纳入COLMAP的三角化过程中，并通过Bundle Adjustment进行位姿优化。确保像素数据关联和先验位姿之间的一致性有助于保持鲁棒性和准确性。对于场景表示，我们引入法向量约束和有效的秩正则化，以增强高斯基元的方向和形状一致性。这些约束与现有的光度损失联合优化，以提高地图质量。我们使用公共和自收集的数据集评估了我们的方法。在位姿优化方面，我们的方法仅需三分之一的时间，同时保持了两个数据集上的准确性和鲁棒性。在场景表示方面，结果表明我们的方法明显优于传统的3DGS管线。值得注意的是，在以弱纹理或重复纹理为特征的自收集数据集上，我们的方法展示了增强的可视化能力，并实现了卓越的整体性能。

## 🔬 方法详解

**问题定义**：现有3D高斯溅射方法在处理大型室外场景，特别是那些纹理信息匮乏或纹理重复的场景时，会遇到位姿估计不稳定和场景表示失真的问题。这些问题源于缺乏足够的几何约束和精确的相机位姿信息，导致重建结果不准确，视觉效果差。

**核心思路**：该论文的核心思路是通过融合先验位姿信息和几何约束来增强3D高斯溅射的鲁棒性和保真度。具体来说，利用LiDAR-IMU里程计提供可靠的相机位姿先验，并结合法向量约束和秩正则化来优化高斯基元的形状和方向，从而提高场景表示的质量。这样设计的目的是为了弥补纹理信息不足带来的问题，并确保重建结果在几何上更加准确和一致。

**技术框架**：该方法主要包含两个关键模块：位姿优化和场景表示优化。首先，利用LiDAR-IMU里程计获取的先验位姿信息，将其融入到COLMAP的三角化过程中，并通过Bundle Adjustment进行位姿优化，确保像素数据关联与先验位姿的一致性。其次，在场景表示方面，引入法向量约束和秩正则化，与现有的光度损失联合优化，以增强高斯基元的形状和方向一致性，从而提高地图质量。

**关键创新**：该论文的关键创新在于将先验位姿信息和几何约束有效地融入到3D高斯溅射的优化过程中。与传统方法仅依赖于图像信息进行位姿估计和场景重建不同，该方法利用LiDAR-IMU里程计提供的位姿先验，显著提高了位姿估计的鲁棒性和准确性。同时，通过引入法向量约束和秩正则化，增强了高斯基元的几何一致性，从而提高了场景表示的质量。

**关键设计**：在位姿优化方面，利用LiDAR-IMU里程计提供的位姿作为先验，并将其融入到COLMAP的三角化过程中，通过Bundle Adjustment进行优化。在场景表示方面，法向量约束通过最小化高斯基元法向量与其邻域法向量之间的差异来实现。秩正则化则通过对高斯基元的协方差矩阵进行约束，使其具有较低的秩，从而保证形状的紧凑性。这些约束与光度损失函数联合优化，以获得最佳的场景表示。

## 📊 实验亮点

实验结果表明，该方法在位姿优化方面，仅需传统方法三分之一的时间，同时保持了准确性和鲁棒性。在场景表示方面，该方法显著优于传统3DGS管线，尤其是在自采集的弱纹理或重复纹理数据集上，展示了增强的可视化能力和卓越的整体性能。代码和数据已开源。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、城市建模、虚拟现实等领域。通过提高在纹理缺失环境下的三维重建精度和鲁棒性，可以为自动驾驶车辆提供更可靠的环境感知，为机器人导航提供更精确的地图信息，并为城市建模和虚拟现实应用提供更高质量的三维场景。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a key rendering pipeline for digital asset creation due to its balance between efficiency and visual quality. To address the issues of unstable pose estimation and scene representation distortion caused by geometric texture inconsistency in large outdoor scenes with weak or repetitive textures, we approach the problem from two aspects: pose estimation and scene representation. For pose estimation, we leverage LiDAR-IMU Odometry to provide prior poses for cameras in large-scale environments. These prior pose constraints are incorporated into COLMAP's triangulation process, with pose optimization performed via bundle adjustment. Ensuring consistency between pixel data association and prior poses helps maintain both robustness and accuracy. For scene representation, we introduce normal vector constraints and effective rank regularization to enforce consistency in the direction and shape of Gaussian primitives. These constraints are jointly optimized with the existing photometric loss to enhance the map quality. We evaluate our approach using both public and self-collected datasets. In terms of pose optimization, our method requires only one-third of the time while maintaining accuracy and robustness across both datasets. In terms of scene representation, the results show that our method significantly outperforms conventional 3DGS pipelines. Notably, on self-collected datasets characterized by weak or repetitive textures, our approach demonstrates enhanced visualization capabilities and achieves superior overall performance. Codes and data will be publicly available at https://github.com/justinyeah/normal_shape.git.

