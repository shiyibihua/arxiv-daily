---
layout: default
title: Adaptive Model-Predictive Control of a Soft Continuum Robot Using a Physics-Informed Neural Network Based on Cosserat Rod Theory
---

# Adaptive Model-Predictive Control of a Soft Continuum Robot Using a Physics-Informed Neural Network Based on Cosserat Rod Theory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12681" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12681v1</a>
  <a href="https://arxiv.org/pdf/2508.12681.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12681v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12681v1', 'Adaptive Model-Predictive Control of a Soft Continuum Robot Using a Physics-Informed Neural Network Based on Cosserat Rod Theory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Johann Licher, Max Bartholdt, Henrik Krauss, Tim-Lukas Habich, Thomas Seel, Moritz Schappler

**分类**: cs.RO, cs.LG, eess.SY

**发布日期**: 2025-08-18

**备注**: 20 pages, 15 figures

---

## 💡 一句话要点

**提出基于物理信息神经网络的自适应模型预测控制以解决软连续机器人控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `软机器人` `模型预测控制` `物理信息神经网络` `动态控制` `卡尔曼滤波` `Cosserat杆理论` `实时控制`

## 📋 核心要点

1. 现有的软连续机器人控制方法面临高计算需求和适应性不足的问题，限制了其在复杂环境中的应用。
2. 本文提出了一种基于领域解耦物理信息神经网络的非线性模型预测控制框架，能够实时适应机器人动态特性。
3. 实验结果表明，该控制器在仿真和实际应用中均能实现高精度的动态轨迹跟踪，末端执行器位置误差低于3毫米。

## 📝 摘要（中文）

软连续机器人（SCRs）的动态控制具有广泛的应用潜力，但由于准确动态模型的高计算需求，仍然是一个具有挑战性的问题。尽管已有基于数据驱动的方法如Koopman算子方法被提出，但它们通常缺乏适应性，无法捕捉完整的机器人形状，限制了其应用。本文提出了一种基于领域解耦物理信息神经网络（DD-PINN）的实时非线性模型预测控制（MPC）框架，具有可调的弯曲刚度。DD-PINN作为动态Cosserat杆模型的替代，具有44000倍的加速因子，并在无迹卡尔曼滤波器中用于从末端执行器位置测量中估计模型状态和弯曲顺应性。我们在GPU上实现了以70 Hz运行的非线性进化MPC。在仿真中，控制器能够准确跟踪动态轨迹，末端执行器位置误差低于3毫米（占执行器长度的2.3%）。在实际实验中，控制器实现了类似的精度和高达3.55 m/s²的加速度。

## 🔬 方法详解

**问题定义**：本文旨在解决软连续机器人在动态控制中的高计算需求和适应性不足的问题。现有方法如Koopman算子方法无法有效捕捉机器人形状，限制了其应用。

**核心思路**：提出基于领域解耦物理信息神经网络（DD-PINN）的非线性模型预测控制（MPC）框架，利用DD-PINN作为动态Cosserat杆模型的替代，显著提高计算效率和适应性。

**技术框架**：该框架包括DD-PINN作为动态模型的替代，结合无迹卡尔曼滤波器用于状态估计，最终通过非线性进化MPC实现实时控制。整个系统在GPU上以70 Hz的频率运行。

**关键创新**：最重要的创新在于引入DD-PINN作为动态模型的替代，具有44000倍的加速因子，能够实时适应机器人动态特性，显著提升控制精度和响应速度。

**关键设计**：在设计中，DD-PINN的网络结构经过优化，以适应不同的弯曲刚度，同时损失函数设计用于最小化末端执行器位置误差，确保控制精度。

## 📊 实验亮点

实验结果显示，控制器在仿真中能够实现末端执行器位置误差低于3毫米，实际实验中也达到了类似的精度，且加速度高达3.55 m/s²，表明该方法在动态控制中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗机器人、柔性制造和服务机器人等，能够在复杂和动态环境中实现高效的控制，提升机器人在实际应用中的灵活性和适应性。未来，该技术有望推动软机器人在更多领域的应用，如人机协作和自动化生产线。

## 📄 摘要（原文）

> Dynamic control of soft continuum robots (SCRs) holds great potential for expanding their applications, but remains a challenging problem due to the high computational demands of accurate dynamic models. While data-driven approaches like Koopman-operator-based methods have been proposed, they typically lack adaptability and cannot capture the full robot shape, limiting their applicability. This work introduces a real-time-capable nonlinear model-predictive control (MPC) framework for SCRs based on a domain-decoupled physics-informed neural network (DD-PINN) with adaptable bending stiffness. The DD-PINN serves as a surrogate for the dynamic Cosserat rod model with a speed-up factor of 44000. It is also used within an unscented Kalman filter for estimating the model states and bending compliance from end-effector position measurements. We implement a nonlinear evolutionary MPC running at 70 Hz on the GPU. In simulation, it demonstrates accurate tracking of dynamic trajectories and setpoint control with end-effector position errors below 3 mm (2.3% of the actuator's length). In real-world experiments, the controller achieves similar accuracy and accelerations up to 3.55 m/s2.

