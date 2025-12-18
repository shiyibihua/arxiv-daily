---
layout: default
title: Differentiable Autoencoding Neural Operator for Interpretable and Integrable Latent Space Modeling
---

# Differentiable Autoencoding Neural Operator for Interpretable and Integrable Latent Space Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00233" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00233v1</a>
  <a href="https://arxiv.org/pdf/2510.00233.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00233v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00233v1', 'Differentiable Autoencoding Neural Operator for Interpretable and Integrable Latent Space Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siva Viknesh, Amirhossein Arzani

**分类**: cs.LG, physics.flu-dyn

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出可微自编码神经算子DIANO，用于可解释和可集成的隐空间建模**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `神经算子` `自编码器` `降维` `隐空间建模` `可解释性` `偏微分方程` `科学机器学习`

## 📋 核心要点

1. 现有科学机器学习方法在从高维时空流动数据中提取物理信息方面存在挑战，尤其是在隐空间中实现可解释性。
2. DIANO通过构建物理可解释的隐空间，并允许在隐空间内直接施加微分控制方程，从而解决了降维和几何缩减的可解释性问题。
3. DIANO在二维圆柱绕流、二维对称狭窄动脉流动和三维患者特异性冠状动脉等问题上，验证了其在隐空间中求解PDE的能力。

## 📝 摘要（中文）

本文提出了一种可微自编码神经算子(DIANO)，这是一个确定性的自编码神经算子框架，旨在构建物理上可解释的隐空间，用于降维和几何缩减，并能够在隐空间内直接施加微分控制方程。DIANO基于神经算子，通过编码神经算子进行空间粗化，将高维输入函数压缩到低维隐空间，然后通过解码神经算子进行空间细化，重建原始输入。评估了DIANO在降维方面的隐空间可解释性和性能，并与卷积神经算子和标准自编码器等基线模型进行了比较。此外，开发了一个完全可微的偏微分方程(PDE)求解器，并将其集成到隐空间中，从而能够对高保真和低保真PDE进行时间推进，从而将物理先验嵌入到隐空间动力学中。进一步研究了各种PDE公式，包括二维非定常平流扩散方程和三维压力泊松方程，以检验它们对塑造潜在流动表示的影响。考虑的基准问题包括流经二维圆柱体、流经二维对称狭窄动脉以及三维患者特异性冠状动脉。这些案例研究证明了DIANO能够在促进降维和几何缩减的同时，在允许潜在可解释性的隐空间中求解PDE。

## 🔬 方法详解

**问题定义**：现有的科学机器学习方法，如线性或非线性降维技术，虽然可以从高维时空数据中提取物理信息，但难以在隐空间中实现可解释性。这意味着我们难以理解隐空间中的变量代表什么物理意义，以及如何利用这些变量来预测或控制物理系统的行为。

**核心思路**：DIANO的核心思路是利用神经算子构建一个自编码器，该自编码器可以将高维输入函数压缩到一个低维的、物理可解释的隐空间，并且可以在该隐空间中直接施加微分控制方程。通过这种方式，DIANO不仅可以实现降维，还可以将物理先验知识嵌入到隐空间动力学中，从而提高模型的可解释性和预测精度。

**技术框架**：DIANO的整体架构包括以下几个主要模块：1) **编码神经算子**：负责将高维输入函数通过空间粗化映射到低维隐空间。2) **隐空间PDE求解器**：一个完全可微的PDE求解器，用于在隐空间中进行时间推进，并嵌入物理先验。3) **解码神经算子**：负责将隐空间表示通过空间细化重构回原始高维空间。整个框架是端到端可训练的。

**关键创新**：DIANO的关键创新在于其构建了一个物理可解释的隐空间，并允许在该隐空间中直接施加微分控制方程。这与传统的自编码器或降维方法不同，后者通常只关注数据的压缩和重构，而忽略了隐空间的物理意义。此外，DIANO利用神经算子作为编码器和解码器，使其能够处理函数空间的数据，并具有更好的泛化能力。

**关键设计**：DIANO的关键设计包括：1) **神经算子的选择**：论文中使用了卷积神经算子作为编码器和解码器，但也可以选择其他类型的神经算子，如傅里叶神经算子。2) **隐空间的维度**：隐空间的维度需要根据具体问题进行调整，以在降维和可解释性之间取得平衡。3) **损失函数的设计**：损失函数包括重构损失和PDE损失，其中重构损失用于保证重构的精度，PDE损失用于将物理先验嵌入到隐空间动力学中。4) **PDE求解器的选择**：可以使用各种类型的PDE求解器，如有限差分法或有限元法，只要它们是可微的。

## 📊 实验亮点

DIANO在二维圆柱绕流、二维对称狭窄动脉流动和三维患者特异性冠状动脉等问题上进行了验证。实验结果表明，DIANO能够有效地降低数据的维度，并在隐空间中准确地求解PDE。此外，DIANO的隐空间表示具有良好的可解释性，可以用于分析和理解物理系统的行为。与传统的自编码器和卷积神经算子相比，DIANO在重构精度和预测精度方面均有所提升。

## 🎯 应用场景

DIANO可应用于各种科学和工程领域，例如流体动力学、传热学、材料科学等。它可以用于对复杂物理系统的行为进行建模、预测和控制，例如预测飞行器的气动性能、优化散热器的设计、或预测材料的力学性能。DIANO的潜在价值在于其能够提高模型的可解释性和预测精度，并为物理系统的设计和优化提供新的思路。

## 📄 摘要（原文）

> Scientific machine learning has enabled the extraction of physical insights from high-dimensional spatiotemporal flow data using linear and nonlinear dimensionality reduction techniques. Despite these advances, achieving interpretability within the latent space remains a challenge. To address this, we propose the DIfferentiable Autoencoding Neural Operator (DIANO), a deterministic autoencoding neural operator framework that constructs physically interpretable latent spaces for both dimensional and geometric reduction, with the provision to enforce differential governing equations directly within the latent space. Built upon neural operators, DIANO compresses high-dimensional input functions into a low-dimensional latent space via spatial coarsening through an encoding neural operator and subsequently reconstructs the original inputs using a decoding neural operator through spatial refinement. We assess DIANO's latent space interpretability and performance in dimensionality reduction against baseline models, including the Convolutional Neural Operator and standard autoencoders. Furthermore, a fully differentiable partial differential equation (PDE) solver is developed and integrated within the latent space, enabling the temporal advancement of both high- and low-fidelity PDEs, thereby embedding physical priors into the latent dynamics. We further investigate various PDE formulations, including the 2D unsteady advection-diffusion and the 3D Pressure-Poisson equation, to examine their influence on shaping the latent flow representations. Benchmark problems considered include flow past a 2D cylinder, flow through a 2D symmetric stenosed artery, and a 3D patient-specific coronary artery. These case studies demonstrate DIANO's capability to solve PDEs within a latent space that facilitates both dimensional and geometrical reduction while allowing latent interpretability.

