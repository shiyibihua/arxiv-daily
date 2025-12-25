---
layout: default
title: Wireless Center of Pressure Feedback System for Humanoid Robot Balance Control using ESP32-C3
---

# Wireless Center of Pressure Feedback System for Humanoid Robot Balance Control using ESP32-C3

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21219" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21219v1</a>
  <a href="https://arxiv.org/pdf/2512.21219.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21219v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21219v1', 'Wireless Center of Pressure Feedback System for Humanoid Robot Balance Control using ESP32-C3')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhtadin, Faris Rafi Pramana, Dion Hayu Fandiantoro, Moh Ismarintan Zazuli, Atar Fuady Babgei

**分类**: cs.RO, eess.SY

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**针对人形机器人，提出基于ESP32-C3的无线压力中心反馈平衡控制系统**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `人形机器人` `平衡控制` `压力中心` `无线传感器` `ESP32-C3`

## 📋 核心要点

1. 人形机器人单腿站立平衡控制面临挑战，传统有线传感器限制了关节运动，并引入机械噪声。
2. 设计无线嵌入式系统，利用足部力传感器和ESP32-C3实时估计压力中心，并无线传输数据。
3. 实验表明，该系统具有高精度，且在倾斜地面上单腿站立时，能有效维持机器人平衡。

## 📝 摘要（中文）

本研究针对人形机器人单腿站立时的平衡问题，提出了一种无线嵌入式平衡系统。该系统集成了定制的足部单元，包含四个力传感器和一个ESP32-C3微控制器，用于实时估计压力中心(CoP)。CoP数据通过无线方式传输到主控制器，从而减少了29自由度VI-ROSE人形机器人的布线复杂性。采用PID控制策略，根据CoP反馈调整躯干、髋部和踝关节的横滚关节。实验结果表明，该传感器具有较高的精度，平均测量误差为14.8克。此外，在3度倾斜的单腿抬起任务中，通过优化PID参数(Kp=0.10, Kd=0.005)，该控制系统实现了100%的平衡成功率。验证了无线CoP反馈在增强人形机器人姿态稳定性方面的有效性，且不影响其机械灵活性。

## 🔬 方法详解

**问题定义**：人形机器人在单腿站立阶段保持平衡是一个关键问题，尤其是在需要复杂动作和高机械自由度的舞蹈机器人中。传统的有线传感器配置限制了关节的运动范围，并且容易引入机械噪声，影响控制精度。因此，需要一种无线、高精度的平衡系统来解决这些问题。

**核心思路**：该论文的核心思路是设计一个无线的压力中心（CoP）反馈系统，通过实时测量足底的压力分布，计算出CoP的位置，并将该信息无线传输给主控制器。主控制器根据CoP的位置，调整机器人的姿态，从而实现平衡控制。采用无线方式可以避免有线连接带来的限制和噪声。

**技术框架**：该系统的整体架构包括以下几个主要模块：1) 定制的足部单元，集成了四个力传感器，用于测量足底的压力分布；2) ESP32-C3微控制器，用于采集力传感器的数据，计算CoP的位置，并通过Wi-Fi无线传输数据；3) 主控制器，接收来自ESP32-C3的CoP数据，并根据PID控制策略，调整机器人的躯干、髋部和踝关节的横滚关节；4) VI-ROSE人形机器人，一个29自由度的机器人平台，用于验证该系统的性能。

**关键创新**：该论文的关键创新在于将无线通信技术应用于人形机器人的平衡控制系统，从而避免了有线连接带来的限制和噪声。此外，该系统采用定制的足部单元，集成了多个力传感器，可以更精确地测量足底的压力分布，从而提高CoP的估计精度。

**关键设计**：在关键设计方面，论文采用了ESP32-C3微控制器，因为它具有体积小、功耗低、无线通信能力强的特点。PID控制器的参数（Kp=0.10, Kd=0.005）是通过实验优化得到的，以实现最佳的平衡控制效果。力传感器的选择也至关重要，需要具有高精度和高灵敏度，以确保CoP估计的准确性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21219v1/gambar/Diagram_Sistem_2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21219v1/gambar/Desain_Mekanik_2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21219v1/gambar/Diagram_Elektronik.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该系统具有较高的传感器精度，平均测量误差为14.8克。在3度倾斜的单腿抬起任务中，通过优化PID参数(Kp=0.10, Kd=0.005)，该控制系统实现了100%的平衡成功率。这些结果验证了无线CoP反馈在增强人形机器人姿态稳定性方面的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要高精度平衡控制的人形机器人应用场景，例如舞蹈机器人、康复机器人、服务机器人等。通过无线CoP反馈，可以提高机器人在复杂环境下的稳定性和适应性，使其能够执行更复杂的任务。此外，该系统还可以用于步态分析和运动控制研究，为机器人技术的进一步发展提供支持。

## 📄 摘要（原文）

> Maintaining stability during the single-support phase is a fundamental challenge in humanoid robotics, particularly in dance robots that require complex maneuvers and high mechanical freedom. Traditional tethered sensor configurations often restrict joint movement and introduce mechanical noises. This study proposes a wireless embedded balance system designed to maintain stability on uneven surfaces. The system utilizes a custom-designed foot unit integrated with four load cells and an ESP32-C3 microcontroller to estimate the Center of Pressure (CoP) in real time. The CoP data were transmitted wirelessly to the main controller to minimize the wiring complexity of the 29-DoF VI-ROSE humanoid robot. A PID control strategy is implemented to adjust the torso, hip, and ankle roll joints based on CoP feedback. Experimental characterization demonstrated high sensor precision with an average measurement error of 14.8 g. Furthermore, the proposed control system achieved a 100% success rate in maintaining balance during single-leg lifting tasks at a 3-degree inclination with optimized PID parameters (Kp=0.10, Kd=0.005). These results validate the efficacy of wireless CoP feedback in enhancing the postural stability of humanoid robots, without compromising their mechanical flexibility.

