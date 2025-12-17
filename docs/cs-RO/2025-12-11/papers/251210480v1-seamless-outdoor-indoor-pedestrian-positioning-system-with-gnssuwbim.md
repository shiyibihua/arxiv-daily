---
layout: default
title: Seamless Outdoor-Indoor Pedestrian Positioning System with GNSS/UWB/IMU Fusion: A Comparison of EKF, FGO, and PF
---

# Seamless Outdoor-Indoor Pedestrian Positioning System with GNSS/UWB/IMU Fusion: A Comparison of EKF, FGO, and PF

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.10480" target="_blank" class="toolbar-btn">arXiv: 2512.10480v1</a>
    <a href="https://arxiv.org/pdf/2512.10480.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10480v1" 
            onclick="toggleFavorite(this, '2512.10480v1', 'Seamless Outdoor-Indoor Pedestrian Positioning System with GNSS/UWB/IMU Fusion: A Comparison of EKF, FGO, and PF')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jiaqiang Zhang, Xianjia Yu, Sier Ha, Paola Torrico Moron, Sahar Salimpour, Farhad Kerama, Haizhou Zhang, Tomi Westerlund

**分类**: cs.RO

**发布日期**: 2025-12-11

**备注**: 8 pages, 4 figures, submitted to The 17th International Conference on Ambient Systems, Networks and Technologies

---

## 💡 一句话要点

**提出GNSS/UWB/IMU融合的无缝室内外行人定位系统，对比EKF、FGO和PF算法。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `行人定位` `传感器融合` `GNSS` `UWB` `IMU` `扩展卡尔曼滤波` `因子图优化`

## 📋 核心要点

1. 现有行人定位方案在室内外切换时，易受GNSS信号遮挡、UWB多径效应和IMU漂移影响，难以保证定位精度和连续性。
2. 提出一种GNSS/UWB/IMU融合框架，利用PDR作为运动主干，GNSS和UWB提供绝对位置更新，并引入地图约束提高鲁棒性。
3. 在ROS 2平台上实现并对比了ESKF、FGO和PF三种后端算法，实验结果表明ESKF在所实现的系统中表现出最佳的整体性能。

## 📝 摘要（中文）

本文提出了一种统一的GNSS/UWB/IMU融合框架，用于实现无缝的行人定位。由于GNSS、UWB和基于惯性PDR的定位方法具有互补性，但又容易受到信号阻挡、多径效应和漂移的影响，因此在室内外环境中实现精确和连续的行人定位仍然具有挑战性。本文对三种概率后端进行了受控比较：误差状态扩展卡尔曼滤波器（ESKF）、滑动窗口因子图优化（FGO）和粒子滤波器（PF）。该系统采用胸前佩戴的基于IMU的PDR作为运动主干，并集成了来自室外GNSS和室内UWB的绝对位置更新。为了增强过渡鲁棒性并减轻城市GNSS性能下降的影响，我们引入了一种基于地图的轻量级可行性约束，该约束源自OpenStreetMap建筑物轮廓，将大多数建筑物内部视为不可导航区域，但允许在指定的UWB仪器化建筑物内移动。该框架在ROS 2中实现，并在可穿戴平台上实时运行，并在Foxglove中进行可视化。我们评估了三种场景：室内（UWB+PDR）、室外（GNSS+PDR）和无缝室内外（GNSS+UWB+PDR）。结果表明，在我们的实现中，ESKF提供了最一致的整体性能。

## 🔬 方法详解

**问题定义**：论文旨在解决行人定位在室内外无缝切换时，由于GNSS信号不稳定、UWB信号易受多径干扰以及IMU存在漂移等问题，导致定位精度下降和连续性中断的难题。现有方法通常依赖单一传感器或简单的传感器融合，难以适应复杂的室内外环境。

**核心思路**：论文的核心思路是利用多种传感器的互补特性，构建一个鲁棒的融合定位系统。具体而言，使用IMU进行航位推算（PDR）作为定位的主干，利用GNSS在室外提供绝对位置信息，利用UWB在室内提供绝对位置信息，并通过地图信息约束行人的可行走区域，从而提高定位的精度和鲁棒性。

**技术框架**：该系统的整体架构包括以下几个主要模块：
1. **传感器数据采集**：从GNSS、UWB和IMU传感器获取数据。
2. **预处理**：对传感器数据进行滤波、校准等预处理操作。
3. **PDR模块**：利用IMU数据进行航位推算，估计行人的位置和姿态。
4. **GNSS/UWB融合**：将GNSS和UWB的定位结果与PDR的估计结果进行融合，得到更精确的位置估计。
5. **地图约束**：利用OpenStreetMap数据，对行人的位置进行可行性约束，排除不可能的位置。
6. **后端优化**：使用ESKF、FGO或PF等后端算法对融合后的位置估计进行优化。

**关键创新**：论文的关键创新点在于：
1. **统一的融合框架**：提出了一个能够同时融合GNSS、UWB和IMU数据的统一框架。
2. **地图约束**：引入了基于OpenStreetMap的地图约束，提高了定位的鲁棒性。
3. **多种后端算法对比**：对ESKF、FGO和PF三种后端算法进行了详细的对比分析。

**关键设计**：
1. **地图约束**：将OpenStreetMap的建筑物轮廓信息转换为可行走区域的约束条件，限制行人在建筑物内部的移动。
2. **后端算法选择**：针对不同的应用场景，可以选择不同的后端算法。ESKF计算效率高，适用于实时性要求高的场景；FGO能够进行全局优化，适用于对精度要求高的场景；PF能够处理非线性问题，适用于复杂的环境。

## 📊 实验亮点

实验结果表明，在室内、室外和室内外无缝切换三种场景下，该系统均能实现较为精确的行人定位。对比ESKF、FGO和PF三种后端算法，ESKF在所实现的系统中表现出最稳定的性能。虽然论文中没有给出具体的性能数据，但强调了ESKF在实际应用中的优势。

## 🎯 应用场景

该研究成果可应用于室内外无缝导航、增强现实、物流跟踪、应急救援等领域。通过提供精确和连续的行人定位，可以提升用户体验，提高工作效率，并在紧急情况下提供有效的支持。未来，该技术有望与智能穿戴设备集成，实现更便捷的定位服务。

## 📄 摘要（原文）

> Accurate and continuous pedestrian positioning across outdoor-indoor environments remains challenging because GNSS, UWB, and inertial PDR are complementary yet individually fragile under signal blockage, multipath, and drift. This paper presents a unified GNSS/UWB/IMU fusion framework for seamless pedestrian localization and provides a controlled comparison of three probabilistic back-ends: an error-state extended Kalman filter, sliding-window factor graph optimization, and a particle filter. The system uses chest-mounted IMU-based PDR as the motion backbone and integrates absolute updates from GNSS outdoors and UWB indoors. To enhance transition robustness and mitigate urban GNSS degradation, we introduce a lightweight map-based feasibility constraint derived from OpenStreetMap building footprints, treating most building interiors as non-navigable while allowing motion inside a designated UWB-instrumented building. The framework is implemented in ROS 2 and runs in real time on a wearable platform, with visualization in Foxglove. We evaluate three scenarios: indoor (UWB+PDR), outdoor (GNSS+PDR), and seamless outdoor-indoor (GNSS+UWB+PDR). Results show that the ESKF provides the most consistent overall performance in our implementation.

