---
layout: default
title: Fast and Generalizable parameter-embedded Neural Operators for Lithium-Ion Battery Simulation
---

# Fast and Generalizable parameter-embedded Neural Operators for Lithium-Ion Battery Simulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08087" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08087v1</a>
  <a href="https://arxiv.org/pdf/2508.08087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08087v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08087v1', 'Fast and Generalizable parameter-embedded Neural Operators for Lithium-Ion Battery Simulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amir Ali Panahi, Daniel Luder, Billy Wu, Gregory Offer, Dirk Uwe Sauer, Weihan Li

**分类**: cs.LG, physics.chem-ph

**发布日期**: 2025-08-11

**备注**: 31 pages, 6 figures

---

## 💡 一句话要点

**提出参数嵌入的神经算子以加速锂离子电池模拟**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `锂离子电池` `数字双胞胎` `神经算子` `傅里叶神经算子` `参数嵌入` `实时模拟` `电池管理` `机器学习`

## 📋 核心要点

1. 现有的锂离子电池模拟方法在动态负载下表现不佳，难以满足实时应用的需求。
2. 提出的PE-FNO通过在每个谱层中嵌入粒子半径和固相扩散率的参数，实现了更好的泛化能力和速度。
3. 实验结果表明，PE-FNO在多种负载下保持了低于1.7 mV的电压绝对误差，并在参数估计中表现出优越性。

## 📝 摘要（中文）

可靠的锂离子电池数字双胞胎必须在亚毫秒速度下实现高物理保真度。本文基准测试了三种针对单颗粒模型（SPM）的算子学习替代方法：深度算子网络（DeepONets）、傅里叶神经算子（FNOs）以及新提出的参数嵌入傅里叶神经算子（PE-FNO）。PE-FNO在速度上比传统SPM求解器快约200倍，并在参数估计任务中表现出色。该研究为实时电池管理和大规模推断提供了新的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决锂离子电池模拟中现有方法在动态负载下的不足，尤其是速度和准确性之间的权衡问题。现有的深度学习模型在处理复杂负载时表现不佳，无法满足实时应用的需求。

**核心思路**：论文提出的PE-FNO通过在傅里叶神经算子的每个谱层中嵌入与电池特性相关的参数，增强了模型的泛化能力，使其能够适应不同的粒子半径和扩散率。

**技术框架**：PE-FNO的整体架构包括数据预处理、模型训练和推理三个主要阶段。模型通过对四种电流类型（恒定、三角形、脉冲列和高斯随机场）进行训练，确保其在不同状态下的表现。

**关键创新**：PE-FNO的最大创新在于其参数嵌入机制，使得模型在保持高速度的同时，能够处理多样化的电池参数。这一设计显著提高了模型的适应性和准确性。

**关键设计**：在模型设计中，采用了特定的损失函数以优化电压和浓度的预测精度，并通过多线程技术提升计算效率。模型的训练数据涵盖了广泛的充电状态（SOC），确保了其泛化能力。

## 📊 实验亮点

实验结果显示，PE-FNO在执行速度上比传统的16线程SPM求解器快约200倍，同时在多种负载下保持电压绝对误差低于1.7 mV。参数估计任务中，PE-FNO在阳极和阴极扩散率的恢复中分别达到了1.14%和8.4%的平均绝对百分比误差，显示出优越的性能。

## 🎯 应用场景

该研究的潜在应用领域包括实时电池管理系统、实验设计和大规模推断。PE-FNO的高速度和高保真度使其在电池设计和优化中具有重要的实际价值，能够帮助工程师更快地进行电池性能评估和优化。

## 📄 摘要（原文）

> Reliable digital twins of lithium-ion batteries must achieve high physical fidelity with sub-millisecond speed. In this work, we benchmark three operator-learning surrogates for the Single Particle Model (SPM): Deep Operator Networks (DeepONets), Fourier Neural Operators (FNOs) and a newly proposed parameter-embedded Fourier Neural Operator (PE-FNO), which conditions each spectral layer on particle radius and solid-phase diffusivity. Models are trained on simulated trajectories spanning four current families (constant, triangular, pulse-train, and Gaussian-random-field) and a full range of State-of-Charge (SOC) (0 % to 100 %). DeepONet accurately replicates constant-current behaviour but struggles with more dynamic loads. The basic FNO maintains mesh invariance and keeps concentration errors below 1 %, with voltage mean-absolute errors under 1.7 mV across all load types. Introducing parameter embedding marginally increases error, but enables generalisation to varying radii and diffusivities. PE-FNO executes approximately 200 times faster than a 16-thread SPM solver. Consequently, PE-FNO's capabilities in inverse tasks are explored in a parameter estimation task with Bayesian optimisation, recovering anode and cathode diffusivities with 1.14 % and 8.4 % mean absolute percentage error, respectively, and 0.5918 percentage points higher error in comparison with classical methods. These results pave the way for neural operators to meet the accuracy, speed and parametric flexibility demands of real-time battery management, design-of-experiments and large-scale inference. PE-FNO outperforms conventional neural surrogates, offering a practical path towards high-speed and high-fidelity electrochemical digital twins.

