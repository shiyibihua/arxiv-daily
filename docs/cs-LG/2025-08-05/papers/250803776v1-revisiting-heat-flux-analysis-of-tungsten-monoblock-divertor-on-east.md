---
layout: default
title: Revisiting Heat Flux Analysis of Tungsten Monoblock Divertor on EAST using Physics-Informed Neural Network
---

# Revisiting Heat Flux Analysis of Tungsten Monoblock Divertor on EAST using Physics-Informed Neural Network

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03776" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03776v1</a>
  <a href="https://arxiv.org/pdf/2508.03776.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03776v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03776v1', 'Revisiting Heat Flux Analysis of Tungsten Monoblock Divertor on EAST using Physics-Informed Neural Network')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Wang, Zikang Yan, Hao Si, Zhendong Yang, Qingquan Yang, Dengdi Sun, Wanli Lyu, Jin Tang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-05

**🔗 代码/项目**: [GITHUB](https://github.com/Event-AHU/OpenFusion)

---

## 💡 一句话要点

**提出物理信息神经网络以加速EAST热流分析**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `热流估计` `物理信息神经网络` `有限元法` `核聚变` `热传导` `深度学习` `科学计算`

## 📋 核心要点

1. 现有的有限元法在热流估计中计算效率低，难以实现实时模拟，限制了其在实际应用中的有效性。
2. 本文提出的物理信息神经网络（PINN）通过结合物理规律与神经网络，提升了热传导估计的速度和精度。
3. 实验结果显示，所提方法在热传导估计中实现了与有限元法相当的准确性，同时计算效率提高了40倍。

## 📝 摘要（中文）

在核聚变装置EAST中，热流估计是一项至关重要的任务。传统的科学计算方法通常采用有限元法（FEM）进行建模，但FEM依赖于基于网格的采样，计算效率低且难以在实际实验中进行实时模拟。本文提出了一种新颖的物理信息神经网络（PINN），旨在解决这一挑战，显著加速热传导估计过程，同时保持高精度。通过输入不同材料的空间坐标和时间戳，计算边界损失、初始条件损失和物理损失，进一步增强模型的预测能力。实验结果表明，所提方法在均匀和非均匀加热条件下的准确性与有限元法相当，同时计算效率提高了40倍。数据集和源代码将发布在https://github.com/Event-AHU/OpenFusion。

## 🔬 方法详解

**问题定义**：本文旨在解决核聚变装置EAST中热流估计的效率和实时性问题。传统的有限元法在计算上存在低效和实时模拟困难的痛点。

**核心思路**：通过引入物理信息神经网络（PINN），将物理规律与深度学习相结合，利用神经网络的强大拟合能力来加速热传导估计过程。

**技术框架**：整体架构包括输入空间坐标和时间戳，计算边界损失、初始条件损失和物理损失，最后通过小规模数据点的采样来优化模型的拟合能力。

**关键创新**：最重要的技术创新在于将物理信息融入神经网络训练中，使得模型不仅依赖数据驱动，还遵循物理规律，从而在准确性和效率上超越传统方法。

**关键设计**：模型设计中，损失函数包括边界损失、初始条件损失和物理损失，网络结构采用多层感知机（MLP），并通过小规模数据点进行训练以提高模型的适应性。

## 📊 实验亮点

实验结果表明，所提出的物理信息神经网络在均匀和非均匀加热条件下的热传导估计准确性与有限元法相当，同时计算效率提高了40倍，显著提升了实时模拟的可行性。

## 🎯 应用场景

该研究的潜在应用领域包括核聚变装置的热管理和控制系统，能够为实时热流监测和优化提供有效工具。未来，该方法有望推广到其他复杂物理过程的建模与预测中，提升科学计算的效率与准确性。

## 📄 摘要（原文）

> Estimating heat flux in the nuclear fusion device EAST is a critically important task. Traditional scientific computing methods typically model this process using the Finite Element Method (FEM). However, FEM relies on grid-based sampling for computation, which is computationally inefficient and hard to perform real-time simulations during actual experiments. Inspired by artificial intelligence-powered scientific computing, this paper proposes a novel Physics-Informed Neural Network (PINN) to address this challenge, significantly accelerating the heat conduction estimation process while maintaining high accuracy. Specifically, given inputs of different materials, we first feed spatial coordinates and time stamps into the neural network, and compute boundary loss, initial condition loss, and physical loss based on the heat conduction equation. Additionally, we sample a small number of data points in a data-driven manner to better fit the specific heat conduction scenario, further enhancing the model's predictive capability. We conduct experiments under both uniform and non-uniform heating conditions on the top surface. Experimental results show that the proposed thermal conduction physics-informed neural network achieves accuracy comparable to the finite element method, while achieving $\times$40 times acceleration in computational efficiency. The dataset and source code will be released on https://github.com/Event-AHU/OpenFusion.

