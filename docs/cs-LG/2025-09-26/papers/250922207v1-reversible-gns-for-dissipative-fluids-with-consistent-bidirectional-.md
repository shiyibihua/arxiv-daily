---
layout: default
title: Reversible GNS for Dissipative Fluids with Consistent Bidirectional Dynamics
---

# Reversible GNS for Dissipative Fluids with Consistent Bidirectional Dynamics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22207" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22207v1</a>
  <a href="https://arxiv.org/pdf/2509.22207.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22207v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22207v1', 'Reversible GNS for Dissipative Fluids with Consistent Bidirectional Dynamics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mu Huang, Linning Xu, Mingyue Dai, Yidi Shao, Bo Dai

**分类**: cs.LG, cs.AI, physics.flu-dyn

**发布日期**: 2025-09-26

**备注**: 13 pages, 5 figures

---

## 💡 一句话要点

**提出可逆图网络模拟器解决耗散流体的双向动态问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `流体动力学` `可逆模拟` `图网络` `逆推断` `物理一致性` `高效计算` `动态模拟`

## 📋 核心要点

1. 现有的粒子基础模拟器在正向动态上表现良好，但在耗散系统中逆推断困难且优化求解器常常不稳定，难以收敛。
2. 提出的R-GNS框架通过残差可逆消息传递设计，结合正向动态与逆推断，避免了对基础物理的逆转，确保了双向一致性。
3. 实验结果显示，R-GNS在多个基准测试中表现出更高的准确性和一致性，且逆推断速度比传统方法快100倍以上。

## 📝 摘要（中文）

模拟物理上合理的轨迹以达到用户定义的目标是流体动力学中的一项基本而具有挑战性的任务。尽管基于粒子的模拟器能够有效地重现正向动态，但在耗散系统中，逆推断仍然困难。本文提出了可逆图网络模拟器（R-GNS），这是一个在单一图架构中强制双向一致性的统一框架。与以往通过拟合反向数据来近似逆动态的神经模拟器不同，R-GNS并不试图逆转基础物理，而是基于残差可逆消息传递的数学可逆设计，结合正向动态与逆推断，提供准确的预测和高效的合理初始状态恢复。实验表明，R-GNS在三个耗散基准（Water-3D、WaterRamps和WaterDrop）上实现了更高的准确性和一致性，参数量仅为四分之一，并且逆推断速度比基于优化的基线快100倍以上。

## 🔬 方法详解

**问题定义**：本文旨在解决耗散流体系统中的正向与逆向动态模拟问题。现有方法在逆推断时常常面临不稳定和收敛困难，尤其是在处理不可逆的流体动态时。

**核心思路**：R-GNS的核心思路是通过设计一个数学上可逆的框架，结合正向动态与逆推断，而不是简单地逆转物理过程。这种设计使得模型能够在保持物理一致性的同时，进行高效的状态恢复。

**技术框架**：R-GNS采用了残差可逆消息传递机制，整体架构包括正向动态模拟模块和逆推断模块。通过共享参数，这两个模块能够有效地协同工作，确保双向一致性。

**关键创新**：R-GNS的主要创新在于其可逆性设计和双向一致性，首次在耗散流体系统中统一了正向与逆向模拟。这一设计与传统方法的根本区别在于不依赖于对物理过程的逆转，而是通过消息传递实现动态的双向一致性。

**关键设计**：在参数设置上，R-GNS的参数量仅为传统模型的四分之一，损失函数设计上强调了正向与逆向动态的一致性，网络结构采用了共享参数的残差网络，以提高模型的效率和准确性。

## 📊 实验亮点

实验结果表明，R-GNS在三个耗散基准测试中实现了更高的准确性和一致性，参数量仅为传统模型的四分之一，逆推断速度比基于优化的基线快100倍以上。在目标条件任务中，R-GNS还展示了对复杂目标形状的处理能力，显著提升了模拟效率。

## 🎯 应用场景

该研究的潜在应用领域包括计算机动画、虚拟现实和游戏开发等，能够为流体动态模拟提供更高效和准确的解决方案。未来，R-GNS可能在科学计算和工程模拟中发挥重要作用，推动相关领域的技术进步。

## 📄 摘要（原文）

> Simulating physically plausible trajectories toward user-defined goals is a fundamental yet challenging task in fluid dynamics. While particle-based simulators can efficiently reproduce forward dynamics, inverse inference remains difficult, especially in dissipative systems where dynamics are irreversible and optimization-based solvers are slow, unstable, and often fail to converge. In this work, we introduce the Reversible Graph Network Simulator (R-GNS), a unified framework that enforces bidirectional consistency within a single graph architecture. Unlike prior neural simulators that approximate inverse dynamics by fitting backward data, R-GNS does not attempt to reverse the underlying physics. Instead, we propose a mathematically invertible design based on residual reversible message passing with shared parameters, coupling forward dynamics with inverse inference to deliver accurate predictions and efficient recovery of plausible initial states. Experiments on three dissipative benchmarks (Water-3D, WaterRamps, and WaterDrop) show that R-GNS achieves higher accuracy and consistency with only one quarter of the parameters, and performs inverse inference more than 100 times faster than optimization-based baselines. For forward simulation, R-GNS matches the speed of strong GNS baselines, while in goal-conditioned tasks it eliminates iterative optimization and achieves orders-of-magnitude speedups. On goal-conditioned tasks, R-GNS further demonstrates its ability to complex target shapes (e.g., characters "L" and "N") through vivid, physically consistent trajectories. To our knowledge, this is the first reversible framework that unifies forward and inverse simulation for dissipative fluid systems.

