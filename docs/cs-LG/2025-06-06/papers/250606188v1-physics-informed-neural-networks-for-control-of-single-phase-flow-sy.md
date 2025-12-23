---
layout: default
title: Physics-Informed Neural Networks for Control of Single-Phase Flow Systems Governed by Partial Differential Equations
---

# Physics-Informed Neural Networks for Control of Single-Phase Flow Systems Governed by Partial Differential Equations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06188" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06188v1</a>
  <a href="https://arxiv.org/pdf/2506.06188.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06188v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06188v1', 'Physics-Informed Neural Networks for Control of Single-Phase Flow Systems Governed by Partial Differential Equations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luis Kin Miyatake, Eduardo Camponogara, Eric Aislan Antonelo, Alexey Pavlov

**分类**: cs.LG

**发布日期**: 2025-06-06

**备注**: 62 pages, 14 figures

---

## 💡 一句话要点

**提出物理信息神经网络以控制单相流动系统**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `物理信息神经网络` `偏微分方程` `流动控制` `实时监控` `工程优化` `无标注数据` `动态响应`

## 📋 核心要点

1. 现有方法在瞬态条件下对单相流动系统的建模与控制存在困难，尤其是缺乏标注数据的情况下。
2. 本文提出的PINC框架通过结合物理守恒定律，扩展至偏微分方程，分为稳态和瞬态两个网络阶段。
3. 数值实验结果显示，PINC模型在无标注数据的情况下，准确捕捉流动动态，具备实时控制能力。

## 📝 摘要（中文）

单相流动系统的建模与控制，尤其是在瞬态条件下，面临诸多挑战。本文扩展了物理信息神经网络控制框架（PINC），将其应用于偏微分方程（PDE）情形，特别是不可压缩和可压缩流动。PINC模型分为两个阶段：稳态网络学习广泛控制输入的平衡解，瞬态网络捕捉动态响应。通过简化假设降低空间坐标的维度，提升了PINC网络的训练效率。我们通过数值实验验证了该方法，结果表明PINC模型能够准确表示流动动态，并实现实时控制，展示了其在流体流动监测和优化中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决单相流动系统在瞬态条件下建模与控制的挑战，现有方法往往依赖于标注数据，限制了其应用。

**核心思路**：通过扩展物理信息神经网络（PINC）框架，将其应用于偏微分方程（PDE），结合物理守恒定律，避免了对标注数据的依赖。

**技术框架**：PINC模型分为两个主要阶段：稳态网络用于学习不同控制输入下的平衡解，瞬态网络用于捕捉时间变化边界条件下的动态响应。

**关键创新**：提出的简化假设降低了空间坐标的维度，使得PINC网络的训练更加高效，能够推导出最优控制策略。

**关键设计**：在网络结构上，稳态和瞬态网络各自设计了特定的损失函数，确保模型能够有效学习物理规律，并在训练过程中优化控制策略。

## 📊 实验亮点

实验结果表明，PINC模型在无标注数据的情况下，能够准确模拟流动动态，且在实时控制应用中表现出色。与传统方法相比，PINC在流动监测和优化中展现出显著的效率提升，减少了对迭代求解器的依赖。

## 🎯 应用场景

该研究在流体动力学、工程优化和实时监控等领域具有广泛的应用潜力。通过高效的流动动态建模与控制，能够提升工业过程的自动化水平，降低能耗，并提高系统的响应速度。

## 📄 摘要（原文）

> The modeling and control of single-phase flow systems governed by Partial Differential Equations (PDEs) present challenges, especially under transient conditions. In this work, we extend the Physics-Informed Neural Nets for Control (PINC) framework, originally proposed to modeling and control of Ordinary Differential Equations (ODE) without the need of any labeled data, to the PDE case, particularly to single-phase incompressible and compressible flows, integrating neural networks with physical conservation laws. The PINC model for PDEs is structured into two stages: a steady-state network, which learns equilibrium solutions for a wide range of control inputs, and a transient network, which captures dynamic responses under time-varying boundary conditions. We propose a simplifying assumption that reduces the dimensionality of the spatial coordinate regarding the initial condition, allowing the efficient training of the PINC network. This simplification enables the derivation of optimal control policies using Model Predictive Control (MPC). We validate our approach through numerical experiments, demonstrating that the PINC model, which is trained exclusively using physical laws, i.e., without labeled data, accurately represents flow dynamics and enables real-time control applications. The results highlight the PINC's capability to efficiently approximate PDE solutions without requiring iterative solvers, making it a promising alternative for fluid flow monitoring and optimization in engineering applications.

