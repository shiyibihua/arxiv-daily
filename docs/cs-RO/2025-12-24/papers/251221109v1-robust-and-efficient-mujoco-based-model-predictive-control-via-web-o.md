---
layout: default
title: Robust and Efficient MuJoCo-based Model Predictive Control via Web of Affine Spaces Derivatives
---

# Robust and Efficient MuJoCo-based Model Predictive Control via Web of Affine Spaces Derivatives

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21109" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21109v1</a>
  <a href="https://arxiv.org/pdf/2512.21109.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21109v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21109v1', 'Robust and Efficient MuJoCo-based Model Predictive Control via Web of Affine Spaces Derivatives')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Liang, Daniel Rakita

**分类**: cs.RO

**发布日期**: 2025-12-24

**备注**: Submitted to 2026 IEEE International Conference on Robotics & Automation (ICRA 2026)

---

## 💡 一句话要点

**提出基于仿射空间网络导数的MuJoCo模型预测控制，提升效率与鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `MuJoCo` `导数计算` `仿射空间网络` `机器人控制`

## 📋 核心要点

1. MuJoCo MPC依赖有限差分计算导数，在高自由度系统或复杂场景中计算成本高昂，限制了其在时间敏感任务中的应用。
2. 提出使用仿射空间网络(WASP)导数作为有限差分的替代方案，WASP通过重用先前导数信息加速导数计算，适用于MPC的迭代更新。
3. 实验表明，WASP导数能无缝集成到MJPC任务中，提升高达2倍的速度，并且在效率和可靠性上优于基于随机采样的规划器。

## 📝 摘要（中文）

本文提出了一种基于仿射空间网络(Web of Affine Spaces, WASP)导数的MuJoCo模型预测控制(MPC)方法，旨在替代传统的有限差分(FD)方法。MuJoCo是一个强大的物理仿真器，常用于机器人控制。MuJoCo MPC (MJPC)库提供了现成的MPC算法，但其依赖有限差分计算导数，这在高自由度系统或复杂场景中会成为性能瓶颈。WASP是一种高效计算导数近似序列的方法，通过重用先前相关导数计算的信息，加速并稳定新导数的计算，特别适用于MPC的迭代更新。实验结果表明，WASP导数在MJPC中表现出色，能够无缝集成到各种任务中，提供稳定的性能，并且在使用基于导数的规划器(如iLQG)时，速度提升高达2倍。此外，基于WASP的MPC优于MJPC的基于随机采样的规划器，在效率和可靠性方面均有提升。本文开源了完全集成了WASP导数的MJPC实现。

## 🔬 方法详解

**问题定义**：论文旨在解决MuJoCo MPC中，使用有限差分(FD)计算导数时效率低下的问题。有限差分方法需要多次仿真来估计梯度，这在高自由度机器人和复杂环境中计算成本很高，成为实时控制的瓶颈。

**核心思路**：论文的核心思路是使用Web of Affine Spaces (WASP)导数来替代有限差分。WASP通过构建一系列仿射空间来近似目标函数的导数，并利用先前计算的导数信息来加速后续导数的计算。这种方法能够显著减少所需的仿真次数，从而提高MPC的计算效率。

**技术框架**：该方法直接集成到MuJoCo MPC (MJPC)库中，作为一个可替换的导数计算后端。用户可以简单地将有限差分切换为WASP导数，而无需修改其他MPC算法的实现。整体流程包括：1) 初始化WASP导数计算器；2) 在每次MPC迭代中，使用WASP计算目标函数和约束的导数；3) 将计算得到的导数传递给优化器，以更新控制策略。

**关键创新**：WASP导数的核心创新在于其能够高效地重用先前计算的导数信息。与有限差分每次都从头开始计算导数不同，WASP通过维护一个仿射空间网络，可以利用先前迭代中计算的导数来预测当前迭代的导数。这种方法显著减少了所需的仿真次数，从而提高了计算效率。

**关键设计**：WASP的关键设计包括：1) 仿射空间的构建方式，例如如何选择基点和基向量；2) 如何更新和维护仿射空间网络，以保证导数近似的准确性；3) 如何选择合适的步长和正则化参数，以平衡导数计算的效率和精度。论文中可能还涉及一些针对MuJoCo的具体优化，例如如何利用MuJoCo的内部状态信息来加速导数计算（具体细节未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21109v1/figures/quadrotor.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21109v1/figures/swim.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21109v1/figures/climb.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，与传统的有限差分方法相比，WASP导数在使用基于导数的规划器(如iLQG)时，速度提升高达2倍。此外，基于WASP的MPC在多个机器人控制任务中，优于MJPC的基于随机采样的规划器，在效率和可靠性方面均有提升。这些结果表明，WASP导数是一种有效的替代有限差分的方法，可以显著提高MuJoCo MPC的性能。

## 🎯 应用场景

该研究成果可广泛应用于机器人控制领域，尤其是在需要实时响应和高精度控制的场景中，例如：人形机器人、四足机器人、无人驾驶汽车等。通过提高MPC的计算效率，可以实现更复杂的控制策略，并提高机器人的运动性能和鲁棒性。此外，该方法还可以应用于其他需要高效导数计算的领域，例如：优化设计、参数估计等。

## 📄 摘要（原文）

> MuJoCo is a powerful and efficient physics simulator widely used in robotics. One common way it is applied in practice is through Model Predictive Control (MPC), which uses repeated rollouts of the simulator to optimize future actions and generate responsive control policies in real time. To make this process more accessible, the open source library MuJoCo MPC (MJPC) provides ready-to-use MPC algorithms and implementations built directly on top of the MuJoCo simulator. However, MJPC relies on finite differencing (FD) to compute derivatives through the underlying MuJoCo simulator, which is often a key bottleneck that can make it prohibitively costly for time-sensitive tasks, especially in high-DOF systems or complex scenes. In this paper, we introduce the use of Web of Affine Spaces (WASP) derivatives within MJPC as a drop-in replacement for FD. WASP is a recently developed approach for efficiently computing sequences of accurate derivative approximations. By reusing information from prior, related derivative calculations, WASP accelerates and stabilizes the computation of new derivatives, making it especially well suited for MPC's iterative, fine-grained updates over time. We evaluate WASP across a diverse suite of MJPC tasks spanning multiple robot embodiments. Our results suggest that WASP derivatives are particularly effective in MJPC: it integrates seamlessly across tasks, delivers consistently robust performance, and achieves up to a 2$\mathsf{x}$ speedup compared to an FD backend when used with derivative-based planners, such as iLQG. In addition, WASP-based MPC outperforms MJPC's stochastic sampling-based planners on our evaluation tasks, offering both greater efficiency and reliability. To support adoption and future research, we release an open-source implementation of MJPC with WASP derivatives fully integrated.

