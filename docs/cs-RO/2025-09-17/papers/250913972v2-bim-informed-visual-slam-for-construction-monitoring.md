---
layout: default
title: BIM Informed Visual SLAM for Construction Monitoring
---

# BIM Informed Visual SLAM for Construction Monitoring

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13972" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13972v2</a>
  <a href="https://arxiv.org/pdf/2509.13972.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13972v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13972v2', 'BIM Informed Visual SLAM for Construction Monitoring')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Asier Bikandi-Noya, Miguel Fernandez-Cortizas, Muhammad Shaheer, Ali Tourani, Holger Voos, Jose Luis Sanchez-Lopez

**分类**: cs.RO

**发布日期**: 2025-09-17 (更新: 2025-10-08)

**备注**: 8 pages, 5 tables, 4 figures

---

## 💡 一句话要点

**提出BIM信息驱动的视觉SLAM以解决建筑监测中的定位问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉SLAM` `建筑信息模型` `轨迹优化` `实时监测` `深度学习` `施工监控` `RGB-D相机`

## 📋 核心要点

1. 现有的视觉SLAM方法在建筑环境中面临重复布局、遮挡和低纹理结构等挑战，导致轨迹漂移。
2. 本文提出了一种RGB-D SLAM系统，结合建筑信息模型（BIM）作为结构先验，通过建立墙体与BIM的对应关系来增强定位精度。
3. 实验结果表明，所提方法在真实建筑工地上验证，轨迹误差平均减少23.71%，地图均方根误差减少7.14%，显著优于传统视觉SLAM基线。

## 📝 摘要（中文）

同时定位与地图构建（SLAM）是监测建筑工地的重要工具，通过将实际建造状态与设计图纸对齐，可以实现早期错误检测并减少昂贵的返工。尽管基于LiDAR的SLAM具有高几何精度，但其传感器通常体积较大且功耗高，限制了在便携平台上的应用。视觉SLAM提供了一个实用的替代方案，但在建筑环境中进行视觉映射仍然面临挑战。为此，本文提出了一种RGB-D SLAM系统，将建筑信息模型（BIM）作为结构先验知识，持续建立检测到的墙体与其BIM对应物之间的对应关系，并将其作为约束引入后端优化。该方法在真实建筑工地上进行了验证，平均减少了23.71%的轨迹误差和7.14%的地图均方根误差，证明了BIM约束在部分建造条件下可靠对齐数字计划与实际场景的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决在建筑工地中使用视觉SLAM进行定位和地图构建时面临的轨迹漂移问题，现有方法在复杂环境下的稳定性不足。

**核心思路**：通过将建筑信息模型（BIM）作为结构先验知识，持续建立检测到的墙体与其BIM对应物之间的对应关系，从而增强SLAM系统的定位精度。

**技术框架**：该方法的整体架构包括前端的特征提取与匹配模块，以及后端的优化模块，后者将BIM约束引入优化过程以提高地图的准确性。

**关键创新**：最重要的创新点在于将BIM信息作为约束引入SLAM系统，这一设计使得系统能够在部分建造条件下实现更可靠的数字计划与实际场景的对齐。

**关键设计**：在系统设计中，采用了RGB-D相机进行数据采集，利用深度信息提高墙体检测的准确性，并在后端优化中引入了基于BIM的约束条件，以减少轨迹误差和地图误差。

## 📊 实验亮点

实验结果显示，所提RGB-D SLAM系统在真实建筑工地上有效减少了23.71%的轨迹误差和7.14%的地图均方根误差，相较于传统视觉SLAM基线，展现出显著的性能提升，验证了BIM约束的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括建筑工地的实时监测、施工进度跟踪以及质量控制等。通过提高SLAM系统在复杂建筑环境中的准确性，能够有效降低施工过程中的错误和返工成本，提升施工效率。未来，该技术有望在智能建筑、无人机监测等领域得到更广泛的应用。

## 📄 摘要（原文）

> Simultaneous Localization and Mapping (SLAM) is a key tool for monitoring construction sites, where aligning the evolving as-built state with the as-planned design enables early error detection and reduces costly rework. LiDAR-based SLAM achieves high geometric precision, but its sensors are typically large and power-demanding, limiting their use on portable platforms. Visual SLAM offers a practical alternative with lightweight cameras already embedded in most mobile devices. however, visually mapping construction environments remains challenging: repetitive layouts, occlusions, and incomplete or low-texture structures often cause drift in the trajectory map. To mitigate this, we propose an RGB-D SLAM system that incorporates the Building Information Model (BIM) as structural prior knowledge. Instead of relying solely on visual cues, our system continuously establishes correspondences between detected wall and their BIM counterparts, which are then introduced as constraints in the back-end optimization. The proposed method operates in real time and has been validated on real construction sites, reducing trajectory error by an average of 23.71% and map RMSE by 7.14% compared to visual SLAM baselines. These results demonstrate that BIM constraints enable reliable alignment of the digital plan with the as-built scene, even under partially constructed conditions.

