---
layout: default
title: Residual Neural Terminal Constraint for MPC-based Collision Avoidance in Dynamic Environments
---

# Residual Neural Terminal Constraint for MPC-based Collision Avoidance in Dynamic Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03428" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03428v2</a>
  <a href="https://arxiv.org/pdf/2508.03428.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03428v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03428v2', 'Residual Neural Terminal Constraint for MPC-based Collision Avoidance in Dynamic Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bojan Derajić, Mohamed-Khalil Bouzidi, Sebastian Bernhard, Wolfgang Hönig

**分类**: cs.RO, cs.LG, eess.SY

**发布日期**: 2025-08-05 (更新: 2025-08-28)

---

## 💡 一句话要点

**提出混合MPC局部规划器以解决动态环境中的碰撞避免问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `碰撞避免` `动态环境` `神经网络` `安全集` `哈密顿-雅可比分析` `实时规划`

## 📋 核心要点

1. 现有方法在动态环境中进行碰撞避免时，实时计算安全集的难度较大，限制了其应用效果。
2. 本文提出了一种基于学习的近似方法，通过神经网络建模残差函数，结合SDF实现实时安全集估计。
3. 实验结果表明，所提方法在成功率上比最佳基线高出30%，且计算开销与现有方法相当。

## 📝 摘要（中文）

本文提出了一种混合模型预测控制（MPC）局部规划器，该规划器利用基于学习的时间变化安全集近似，并将其作为MPC终端约束。该安全集可表示为通过哈密顿-雅可比（HJ）可达性分析计算的值函数的零超水平集，尽管实时计算该值函数是不可行的。我们利用HJ值函数可以表示为相应符号距离函数（SDF）与非负残差函数的差的特性。残差部分被建模为具有非负输出的神经网络，并从计算出的SDF中减去，从而得到实时值函数估计，设计上至少与SDF同样安全。此外，我们通过超网络对神经残差进行参数化，以提高实时性能和泛化能力。与三种最先进的方法进行比较，所提方法在仿真和硬件实验中实现了高达30%的成功率提升，同时计算开销相似，并产生高质量（低旅行时间）解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决动态环境中碰撞避免的实时规划问题。现有方法在计算安全集时面临实时性不足的挑战，导致无法有效应对环境变化。

**核心思路**：论文提出通过神经网络建模残差函数，结合符号距离函数（SDF）来近似安全集，从而实现实时的值函数估计。这种设计确保了安全性，同时提高了计算效率。

**技术框架**：整体架构包括三个主要模块：首先，通过局部观察获取环境信息；其次，利用神经网络对残差函数进行建模；最后，将残差从SDF中减去，得到实时的安全集近似。

**关键创新**：最重要的技术创新在于将神经网络与SDF结合，形成了一种新的安全集近似方法。这一方法在设计上确保了安全性，并且在实时性上优于传统的HJ分析方法。

**关键设计**：在网络结构上，残差函数被设计为非负输出，并通过超网络进行参数化，以提升模型的实时性能和泛化能力。损失函数的设计确保了输出的有效性与安全性。

## 📊 实验亮点

实验结果显示，所提方法在成功率上比最佳基线高出30%，同时在计算开销上与现有方法相当，且能够生成高质量的低旅行时间解决方案。这些结果表明该方法在动态环境中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和无人机飞行等动态环境中的碰撞避免任务。通过提高实时规划的安全性和效率，能够显著提升这些系统在复杂环境中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In this paper, we propose a hybrid MPC local planner that uses a learning-based approximation of a time-varying safe set, derived from local observations and applied as the MPC terminal constraint. This set can be represented as a zero-superlevel set of the value function computed via Hamilton-Jacobi (HJ) reachability analysis, which is infeasible in real-time. We exploit the property that the HJ value function can be expressed as a difference of the corresponding signed distance function (SDF) and a non-negative residual function. The residual component is modeled as a neural network with non-negative output and subtracted from the computed SDF, resulting in a real-time value function estimate that is at least as safe as the SDF by design. Additionally, we parametrize the neural residual by a hypernetwork to improve real-time performance and generalization properties. The proposed method is compared with three state-of-the-art methods in simulations and hardware experiments, achieving up to 30\% higher success rates compared to the best baseline while requiring a similar computational effort and producing high-quality (low travel-time) solutions.

