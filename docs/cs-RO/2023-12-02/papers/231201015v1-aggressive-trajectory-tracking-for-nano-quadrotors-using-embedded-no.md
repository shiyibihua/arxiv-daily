---
layout: default
title: Aggressive Trajectory Tracking for Nano Quadrotors Using Embedded Nonlinear Model Predictive Control
---

# Aggressive Trajectory Tracking for Nano Quadrotors Using Embedded Nonlinear Model Predictive Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.01015" class="toolbar-btn" target="_blank">📄 arXiv: 2312.01015v1</a>
  <a href="https://arxiv.org/pdf/2312.01015.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.01015v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.01015v1', 'Aggressive Trajectory Tracking for Nano Quadrotors Using Embedded Nonlinear Model Predictive Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Kazim, Hyunjae Sim, Gihun Shin, Hwancheol Hwang, Kwang-Ki K. Kim

**分类**: cs.RO

**发布日期**: 2023-12-02

---

## 💡 一句话要点

**提出基于嵌入式非线性模型预测控制的Nano四旋翼飞行器高精度轨迹跟踪方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `非线性模型预测控制` `Nano四旋翼飞行器` `轨迹跟踪` `嵌入式系统` `自主导航`

## 📋 核心要点

1. 现有方法难以应对Nano四旋翼飞行器在动态环境中高速轨迹跟踪时复杂的空气动力学扰动，导致跟踪精度下降。
2. 采用基于acados的非线性模型预测控制（NMPC），利用板载传感器实时测量进行反馈控制，补偿空气动力学效应。
3. 在仿真和真实Nano四旋翼飞行器（Crazyflie 2.1）上进行了实验，验证了该方法在动态环境中实现精确轨迹跟踪的有效性。

## 📝 摘要（中文）

本文提出了一种基于acados的非线性模型预测控制（NMPC）方法，用于小型轻量级Nano四旋翼飞行器的高精度轨迹跟踪。由于复杂的空气动力学力引入了显著的扰动和较大的位置跟踪误差，在动态环境中高速控制Nano四旋翼飞行器进行精确的轨迹跟踪极具挑战性。这些空气动力学效应难以识别，需要实时反馈控制进行补偿。NMPC使Nano四旋翼飞行器能够基于板载传感器测量实时控制其运动，非常适合于复杂和动态环境中的激进机动和导航等任务。acados软件包支持在嵌入式系统上实现NMPC算法，这对于计算资源有限的Nano四旋翼飞行器尤为重要。我们的自主导航系统基于AI-deck开发，该AI-deck是一个基于GAP8的并行超低功耗计算平台，带有多范围甲板和光流甲板的板载传感器。基于NMPC的轨迹跟踪控制方法在仿真中进行了测试，结果表明其在考虑动态环境下的轨迹跟踪有效性。它还在真实的Nano四旋翼飞行器硬件（27克Crazyflie 2.1）上进行了测试，该硬件具有定制的MCU，运行嵌入式NMPC，在动态真实世界环境中实现了精确的轨迹跟踪结果。

## 🔬 方法详解

**问题定义**：论文旨在解决Nano四旋翼飞行器在复杂动态环境中进行高精度轨迹跟踪的问题。现有方法难以有效处理高速飞行时复杂的空气动力学效应，导致轨迹跟踪误差增大，尤其是在计算资源受限的嵌入式平台上实现实时控制更具挑战。

**核心思路**：论文的核心思路是利用非线性模型预测控制（NMPC）的预测能力和优化能力，结合板载传感器提供的实时反馈信息，对四旋翼飞行器的未来运动轨迹进行预测和优化，从而实现对复杂空气动力学效应的补偿和高精度轨迹跟踪。NMPC能够显式地考虑系统的非线性特性和约束条件，从而提高控制性能。

**技术框架**：整体框架包括以下几个主要模块：1) 传感器数据采集模块，用于获取四旋翼飞行器的状态信息（位置、速度、姿态等）；2) 状态估计模块，用于对传感器数据进行滤波和融合，得到更准确的状态估计；3) NMPC控制器，基于状态估计和四旋翼飞行器的动力学模型，预测未来一段时间内的状态轨迹，并通过优化算法计算最优控制输入；4) 执行器控制模块，将NMPC计算出的控制输入转化为电机控制信号，驱动四旋翼飞行器运动。

**关键创新**：最重要的技术创新点在于将NMPC算法成功地部署在计算资源有限的嵌入式平台上，并实现了对Nano四旋翼飞行器的高精度轨迹跟踪。与传统的线性控制方法相比，NMPC能够更好地处理系统的非线性特性和约束条件，从而提高控制性能。此外，论文还针对嵌入式平台的特点，对NMPC算法进行了优化，降低了计算复杂度。

**关键设计**：论文使用了acados软件工具包来实现NMPC算法，该工具包提供了高效的数值优化求解器和代码生成功能，方便在嵌入式平台上部署NMPC。在模型预测控制中，需要选择合适的预测时域和控制时域，以及合适的代价函数。代价函数通常包括跟踪误差项和控制输入项，用于平衡跟踪精度和控制能量。此外，还需要考虑四旋翼飞行器的物理约束，如电机转速限制和姿态角限制。

## 📊 实验亮点

实验结果表明，所提出的基于NMPC的轨迹跟踪方法在仿真和真实Nano四旋翼飞行器（Crazyflie 2.1）上均取得了良好的效果。在真实实验中，该方法能够实现对复杂轨迹的精确跟踪，并有效抑制空气动力学扰动。具体性能数据（如跟踪误差、响应时间等）未在摘要中明确给出，但强调了在动态真实世界环境中实现了精确的轨迹跟踪结果。

## 🎯 应用场景

该研究成果可应用于无人机自主导航、快速避障、精准物流配送、复杂环境下的搜救任务等领域。通过提高无人机在动态环境中的轨迹跟踪精度和鲁棒性，可以扩展无人机的使用场景，提升其在实际应用中的价值，并为未来更高级的无人机自主控制技术奠定基础。

## 📄 摘要（原文）

> This paper presents an aggressive trajectory tracking method for a small lightweight nano-quadrotor using nonlinear model predictive control (NMPC) based on acados. Controlling a nano quadrotor for accurate trajectory tracking at high speed in dynamic environments is challenging due to complex aerodynamic forces that introduce significant disturbances and large positional tracking errors. These aerodynamic effects are difficult to be identified and require feedback control that compensates for them in real time. NMPC allows the nano-quadrotor to control its motion in real time based on onboard sensor measurements, making it well-suited for tasks such as aggressive maneuvers and navigation in complex and dynamic environments. The software package acados enables the implementation of the NMPC algorithm on embedded systems, which is particularly important for nano-quadrotor due to its limited computational resources. Our autonomous navigation system is developed based on an AI-deck that is a GAP8-based parallel ultra-low power computing platform with onboard sensors of a multi-ranger deck and a flow deck. The proposed method of NMPC-based trajectory tracking control is tested in simulation and the results demonstrate its effectiveness in trajectory tracking while considering the dynamic environments. It is also tested on a real nano quadrotor hardware, 27-g Crazyflie 2.1, with a customized MCU running embedded NMPC, in which accurate trajectory tracking results are achieved in dynamic real-world environments.

