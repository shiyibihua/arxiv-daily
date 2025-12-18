---
layout: default
title: Adaptive Event-Triggered MPC for Linear Parameter-Varying Systems with State Delays, Actuator Saturation and Disturbances
---

# Adaptive Event-Triggered MPC for Linear Parameter-Varying Systems with State Delays, Actuator Saturation and Disturbances

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07384" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07384v1</a>
  <a href="https://arxiv.org/pdf/2509.07384.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07384v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07384v1', 'Adaptive Event-Triggered MPC for Linear Parameter-Varying Systems with State Delays, Actuator Saturation and Disturbances')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aiping Zhong, Wanlin Lu, Langwen Zhang, Ziyang Bao

**分类**: eess.SY

**发布日期**: 2025-09-09

---

## 💡 一句话要点

**提出自适应事件触发MPC，解决LPV系统状态延迟、饱和与扰动问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `事件触发控制` `模型预测控制` `线性参数变化系统` `状态延迟` `执行器饱和` `自适应控制` `Lyapunov稳定性` `凸优化`

## 📋 核心要点

1. 现有ETMPC方法在处理状态延迟和执行器饱和问题时存在局限性，且缺乏触发机制与控制律的协同优化。
2. 论文提出基于Lyapunov-Krasovskii的自适应ETMPC策略，通过嵌入自适应变量实现触发机制和控制器的协同优化设计。
3. 通过工业电加热系统仿真验证，该方法在降低通信负载方面表现出有效性，证明了其工程应用潜力。

## 📝 摘要（中文）

本文提出了一种统一的自适应事件触发模型预测控制（ETMPC）方案，用于解决线性参数变化（LPV）系统在存在状态延迟、执行器饱和和外部扰动下的控制问题。现有研究中，只有少数ETMPC方法尝试解决状态延迟或执行器饱和问题，并且这些方法通常缺乏自适应事件触发机制与控制律之间的协同优化。为了克服这些限制，本文提出了一种基于Lyapunov-Krasovskii的自适应ETMPC策略，该策略能够协同优化触发机制和控制器。具体而言，事件触发参数矩阵通过在类Lyapunov-Krasovskii函数中嵌入内部自适应变量进行自适应优化。此外，执行器饱和非线性被转换为凸包表示。无限时域鲁棒优化问题被重新表述为具有线性矩阵不等式（LMI）约束的凸优化问题。引入不变集约束以确保递归可行性，并严格建立了多重不确定性下的均方输入-状态稳定性（ISS）。工业电加热系统的仿真验证了所提出方法的有效性，尤其是在降低通信负载方面。

## 🔬 方法详解

**问题定义**：论文旨在解决线性参数变化（LPV）系统在存在状态延迟、执行器饱和和外部扰动下的模型预测控制问题。现有方法的痛点在于，要么只能处理状态延迟或执行器饱和中的一种，要么缺乏事件触发机制与控制律的协同优化，导致控制性能受限，通信资源利用率不高。

**核心思路**：论文的核心思路是设计一种自适应事件触发机制，并将其与模型预测控制器进行协同优化。通过在Lyapunov-Krasovskii函数中引入自适应变量，动态调整事件触发参数，从而在保证系统稳定性的前提下，尽可能减少控制器的触发次数，降低通信负载。同时，采用凸优化方法处理执行器饱和问题，确保控制器的鲁棒性。

**技术框架**：整体框架包括以下几个主要模块：1）LPV系统建模，考虑状态延迟、执行器饱和和外部扰动；2）基于Lyapunov-Krasovskii泛函的稳定性分析，设计包含自适应变量的Lyapunov函数；3）事件触发机制设计，基于Lyapunov稳定性条件，动态调整触发参数；4）模型预测控制器设计，将无限时域优化问题转化为具有LMI约束的凸优化问题；5）递归可行性分析，引入不变集约束，保证控制器的可行性。

**关键创新**：最重要的技术创新点在于自适应事件触发机制的设计，它能够根据系统的状态动态调整触发参数，实现触发机制和控制器的协同优化。与传统的固定阈值事件触发机制相比，该方法能够更有效地降低通信负载，同时保证系统的稳定性。此外，将执行器饱和问题转化为凸优化问题，也提高了控制器的鲁棒性。

**关键设计**：关键设计包括：1）Lyapunov-Krasovskii泛函的选取，需要包含状态延迟的信息，并能够嵌入自适应变量；2）事件触发条件的设定，需要基于Lyapunov稳定性条件，并能够动态调整触发参数；3）凸优化问题的构建，需要将执行器饱和问题转化为线性约束，并保证优化问题的可行性；4）不变集约束的设计，需要保证控制器的递归可行性。

## 📊 实验亮点

论文通过工业电加热系统的仿真实验验证了所提出方法的有效性。实验结果表明，与传统的固定阈值事件触发MPC相比，该方法能够显著降低通信负载，同时保证系统的稳定性和控制性能。具体的性能数据（例如通信负载降低的百分比）在原文中未明确给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于各种需要远程控制和通信受限的工业控制系统，例如电力系统、智能电网、机器人控制、无人机集群控制等。通过降低通信负载，可以有效延长设备寿命、降低能源消耗，并提高系统的整体可靠性和安全性。未来，该方法有望推广到更复杂的非线性系统和多智能体系统。

## 📄 摘要（原文）

> This paper proposes a unified adaptive event-triggered model predictive control (ETMPC) scheme for linear parameter-varying (LPV) systems subject to state delays, actuator saturation, and external disturbances. In existing studies, only a limited number of ETMPC methods have attempted to address either state delays or actuator saturation, and even these few methods typically lack co-design optimization between adaptive event-triggering mechanisms and the control law. To overcome these limitations, this paper presents a Lyapunov-Krasovskii-based adaptive ETMPC strategy that enables the co-design optimization of both the triggering mechanism and the controller. Specifically, the event-triggering parameter matrix is adaptively optimized by embedding an internal adaptive variable within the Lyapunov-Krasovskii-like function. Furthermore, the actuator saturation nonlinearity is transformed into a convex hull representation. The infinite-horizon robust optimization problem is reformulated as a convex optimization problem with linear matrix inequality (LMI) constraints. Invariant set constraints are introduced to ensure recursive feasibility, and mean-square input-to-state stability (ISS) under multiple uncertainties is rigorously established. Simulations on an industrial electric heating system validate the proposed method's effectiveness in reducing communication load.

