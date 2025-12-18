---
layout: default
title: EKF-Based Fusion of Wi-Fi/LiDAR/IMU for Indoor Localization and Navigation
---

# EKF-Based Fusion of Wi-Fi/LiDAR/IMU for Indoor Localization and Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23118" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23118v1</a>
  <a href="https://arxiv.org/pdf/2509.23118.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23118v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23118v1', 'EKF-Based Fusion of Wi-Fi/LiDAR/IMU for Indoor Localization and Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeyi Li, Zhe Tang, Kyeong Soo Kim, Sihao Li, Jeremy S. Smith

**分类**: cs.RO, cs.LG, cs.NI

**发布日期**: 2025-09-27

**备注**: 8 pages, 7 figures, 3 tables, and submitted for presentation at a conference

---

## 💡 一句话要点

**提出基于EKF的Wi-Fi/LiDAR/IMU融合室内定位导航框架，提升定位精度和鲁棒性。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `室内定位` `多传感器融合` `扩展卡尔曼滤波` `Wi-Fi指纹` `LiDAR SLAM` `IMU导航` `深度学习`

## 📋 核心要点

1. 传统Wi-Fi RSSI指纹定位精度较低，难以满足日益增长的室内定位需求，而LiDAR方案成本高昂且复杂。
2. 论文提出基于EKF的多传感器融合框架，结合Wi-Fi、LiDAR和IMU的优势，实现更精确和鲁棒的室内定位。
3. 实验结果表明，该框架在各种路径配置下均能提供稳定的高精度定位，显著优于单一传感器方案。

## 📝 摘要（中文）

本文提出了一种新颖的室内定位导航框架，该框架集成了Wi-Fi RSSI指纹识别、基于LiDAR的同步定位与地图构建(SLAM)以及基于惯性测量单元(IMU)的导航，并采用扩展卡尔曼滤波器(EKF)进行融合。具体而言，首先利用基于深度神经网络(DNN)的Wi-Fi RSSI指纹识别进行粗略定位，然后通过基于IMU的动态定位进行优化，并使用Gmapping-based SLAM生成占据栅格地图并输出高频姿态估计。最后，EKF预测更新融合传感器信息，有效抑制Wi-Fi噪声和IMU漂移误差。在西安交通大学的IR大楼进行的多组真实实验表明，所提出的多传感器融合框架抑制了单一方法的不稳定性，从而在所有路径配置中提供稳定的精度，平均二维(2D)误差范围为0.2449米至0.3781米。相比之下，Wi-Fi RSSI指纹识别在信号干扰严重的区域的平均2D误差高达1.3404米，而LiDAR/IMU定位由于累积漂移，误差在0.6233米至2.8803米之间。

## 🔬 方法详解

**问题定义**：室内定位面临精度和成本的挑战。Wi-Fi RSSI指纹定位易受环境干扰，精度有限；LiDAR定位精度高，但部署成本和复杂度较高；IMU存在累积漂移误差。现有方法难以兼顾精度、成本和鲁棒性。

**核心思路**：利用多传感器信息互补的特性，通过融合Wi-Fi、LiDAR和IMU数据，克服各自的局限性。Wi-Fi提供初始位置估计，LiDAR构建地图并提供精确的姿态估计，IMU提供高频动态信息，EKF融合这些信息，抑制噪声和漂移。

**技术框架**：该框架包含三个主要阶段：1) 基于DNN的Wi-Fi RSSI指纹定位，提供粗略的位置估计；2) 基于IMU的动态定位和Gmapping SLAM，生成占据栅格地图并输出高频姿态估计；3) 基于EKF的传感器融合，融合Wi-Fi、LiDAR和IMU数据，进行状态预测和更新。

**关键创新**：该方法的关键创新在于使用EKF有效地融合了来自不同传感器的信息，从而在抑制Wi-Fi噪声和IMU漂移误差的同时，利用了LiDAR的高精度姿态估计。这种融合策略提高了定位的整体精度和鲁棒性。

**关键设计**：EKF的状态向量包括位置、姿态和速度。Wi-Fi RSSI指纹定位的结果作为EKF的观测值，用于更新状态。LiDAR SLAM提供的地图用于约束定位结果，IMU数据用于预测状态。EKF的噪声协方差矩阵根据传感器特性进行调整，以优化融合效果。具体参数设置和损失函数细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，所提出的多传感器融合框架在西安交通大学IR大楼的真实环境中，实现了平均2D误差在0.2449米至0.3781米之间的稳定精度。相比之下，Wi-Fi RSSI指纹识别的平均2D误差高达1.3404米，LiDAR/IMU定位的误差在0.6233米至2.8803米之间。该框架显著提高了室内定位的精度和鲁棒性。

## 🎯 应用场景

该研究成果可应用于室内导航、机器人定位、智能仓储、人员跟踪等领域。通过融合多种传感器信息，可以实现更精确、更可靠的室内定位服务，提升用户体验和工作效率。未来可进一步探索在更复杂环境下的应用，例如存在动态障碍物的场景。

## 📄 摘要（原文）

> Conventional Wi-Fi received signal strength indicator (RSSI) fingerprinting cannot meet the growing demand for accurate indoor localization and navigation due to its lower accuracy, while solutions based on light detection and ranging (LiDAR) can provide better localization performance but is limited by their higher deployment cost and complexity. To address these issues, we propose a novel indoor localization and navigation framework integrating Wi-Fi RSSI fingerprinting, LiDAR-based simultaneous localization and mapping (SLAM), and inertial measurement unit (IMU) navigation based on an extended Kalman filter (EKF). Specifically, coarse localization by deep neural network (DNN)-based Wi-Fi RSSI fingerprinting is refined by IMU-based dynamic positioning using a Gmapping-based SLAM to generate an occupancy grid map and output high-frequency attitude estimates, which is followed by EKF prediction-update integrating sensor information while effectively suppressing Wi-Fi-induced noise and IMU drift errors. Multi-group real-world experiments conducted on the IR building at Xi'an Jiaotong-Liverpool University demonstrates that the proposed multi-sensor fusion framework suppresses the instability caused by individual approaches and thereby provides stable accuracy across all path configurations with mean two-dimensional (2D) errors ranging from 0.2449 m to 0.3781 m. In contrast, the mean 2D errors of Wi-Fi RSSI fingerprinting reach up to 1.3404 m in areas with severe signal interference, and those of LiDAR/IMU localization are between 0.6233 m and 2.8803 m due to cumulative drift.

