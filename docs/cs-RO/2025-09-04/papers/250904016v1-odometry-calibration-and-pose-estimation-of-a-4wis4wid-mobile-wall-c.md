---
layout: default
title: Odometry Calibration and Pose Estimation of a 4WIS4WID Mobile Wall Climbing Robot
---

# Odometry Calibration and Pose Estimation of a 4WIS4WID Mobile Wall Climbing Robot

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04016" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04016v1</a>
  <a href="https://arxiv.org/pdf/2509.04016.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04016v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04016v1', 'Odometry Calibration and Pose Estimation of a 4WIS4WID Mobile Wall Climbing Robot')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Branimir Ćaran, Vladimir Milić, Marko Švaco, Bojan Jerbić

**分类**: cs.RO

**发布日期**: 2025-09-04

**备注**: ACCEPTED FOR IEEE EUROPEAN CONFERENCE ON MOBILE ROBOTS 2025. PREPRINT VERSION. ACCEPTED JUNE, 2025 AND PRESENTED SEPTEMBER, 2025

---

## 💡 一句话要点

**针对壁面爬行机器人，提出融合多模态信息的里程计标定与位姿估计方法**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `壁面爬行机器人` `里程计标定` `位姿估计` `多传感器融合` `卡尔曼滤波`

## 📋 核心要点

1. 壁面爬行机器人依赖里程计进行定位，但易受系统和非系统误差影响，导致漂移。
2. 融合轮式里程计、视觉里程计和IMU数据，使用EKF/UKF进行位姿估计，提高定位精度。
3. 采用非线性优化（Levenberg-Marquardt）和随机方法（遗传算法、粒子群）进行系统参数标定，并进行了实验验证。

## 📝 摘要（中文）

本文提出了一种用于四轮独立转向四轮独立驱动（4WIS4WID）壁面爬行移动机器人的位姿估计器设计方案。该方案基于多模态测量信息的融合，包括轮式里程计、视觉里程计和惯性测量单元（IMU）数据，并采用扩展卡尔曼滤波器（EKF）和无迹卡尔曼滤波器（UKF）进行数据融合。位姿估计器是壁面爬行移动机器人的关键组成部分，因为其作业环境涉及在建筑施工中携带精确的测量设备和维护工具，需要了解机器人在建筑物上的位姿信息。由于建筑外墙的复杂几何形状和材料特性，传统的激光、超声或雷达等定位传感器通常不适用于壁面爬行机器人。此外，基于GPS的定位通常在这些环境中不可靠，因为钢筋混凝土和电磁干扰会导致信号衰减。因此，机器人里程计仍然是速度和位置信息的主要来源，尽管它容易受到系统误差和非系统误差引起的漂移的影响。论文使用非线性优化和Levenberg-Marquardt方法（作为牛顿-高斯和基于梯度的模型拟合方法）以及遗传算法和粒子群算法（作为基于随机的方法）对机器人的系统参数进行标定。标定方法和位姿估计器的性能和结果通过在实验性壁面爬行移动机器人上进行的实验进行了详细验证。

## 🔬 方法详解

**问题定义**：壁面爬行机器人在建筑外墙等复杂环境中作业时，依赖里程计进行定位，但由于轮子打滑、表面不平整等因素，里程计会产生累积误差，导致位姿估计漂移。传统的激光、超声、雷达以及GPS等定位方法在这些场景下受到限制，因此需要更精确的里程计标定和位姿估计方法。

**核心思路**：论文的核心思路是通过融合多种传感器信息（轮式里程计、视觉里程计和IMU），利用卡尔曼滤波框架（EKF/UKF）进行数据融合，从而提高位姿估计的精度和鲁棒性。同时，采用不同的优化算法对里程计的系统参数进行标定，减少系统误差的影响。

**技术框架**：整体框架包括以下几个主要模块：1) 数据采集模块：采集轮式里程计、视觉里程计和IMU的数据。2) 里程计标定模块：使用非线性优化方法（Levenberg-Marquardt）和随机优化方法（遗传算法、粒子群）对里程计的系统参数进行标定。3) 位姿估计模块：使用扩展卡尔曼滤波器（EKF）或无迹卡尔曼滤波器（UKF）融合多传感器数据，估计机器人的位姿。4) 实验验证模块：在实际的壁面爬行机器人上进行实验，验证标定方法和位姿估计器的性能。

**关键创新**：论文的关键创新在于：1) 针对壁面爬行机器人的特点，融合了多种传感器信息，提高了位姿估计的鲁棒性。2) 采用了多种优化算法进行里程计标定，并比较了它们的性能。3) 详细的实验验证，证明了所提出方法的有效性。

**关键设计**：在里程计标定中，使用了Levenberg-Marquardt算法进行非线性优化，并与遗传算法和粒子群算法等随机优化方法进行了比较。在位姿估计中，分别使用了EKF和UKF两种卡尔曼滤波方法，并根据实际情况选择合适的滤波器。具体参数设置和损失函数选择在论文中进行了详细描述。

## 📊 实验亮点

论文通过实验验证了所提出的里程计标定和位姿估计方法的有效性。实验结果表明，融合多传感器信息并使用卡尔曼滤波进行位姿估计可以显著提高定位精度和鲁棒性。同时，不同标定方法的性能也进行了比较，为实际应用中选择合适的标定方法提供了参考。

## 🎯 应用场景

该研究成果可应用于建筑外墙检测、维护和清洁等领域。壁面爬行机器人可以携带各种传感器和工具，对建筑物进行精确的检测和维护，例如裂缝检测、涂料喷涂、玻璃清洁等。该研究能够提高机器人的定位精度和自主导航能力，使其能够更安全、高效地完成任务，具有重要的实际应用价值。

## 📄 摘要（原文）

> This paper presents the design of a pose estimator for a four wheel independent steer four wheel independent drive (4WIS4WID) wall climbing mobile robot, based on the fusion of multimodal measurements, including wheel odometry, visual odometry, and an inertial measurement unit (IMU) data using Extended Kalman Filter (EKF) and Unscented Kalman Filter (UKF). The pose estimator is a critical component of wall climbing mobile robots, as their operational environment involves carrying precise measurement equipment and maintenance tools in construction, requiring information about pose on the building at the time of measurement. Due to the complex geometry and material properties of building facades, the use of traditional localization sensors such as laser, ultrasonic, or radar is often infeasible for wall-climbing robots. Moreover, GPS-based localization is generally unreliable in these environments because of signal degradation caused by reinforced concrete and electromagnetic interference. Consequently, robot odometry remains the primary source of velocity and position information, despite being susceptible to drift caused by both systematic and non-systematic errors. The calibrations of the robot's systematic parameters were conducted using nonlinear optimization and Levenberg-Marquardt methods as Newton-Gauss and gradient-based model fitting methods, while Genetic algorithm and Particle swarm were used as stochastic-based methods for kinematic parameter calibration. Performance and results of the calibration methods and pose estimators were validated in detail with experiments on the experimental mobile wall climbing robot.

