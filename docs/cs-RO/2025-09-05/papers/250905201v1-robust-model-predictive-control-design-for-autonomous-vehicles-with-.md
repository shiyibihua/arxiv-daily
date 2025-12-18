---
layout: default
title: Robust Model Predictive Control Design for Autonomous Vehicles with Perception-based Observers
---

# Robust Model Predictive Control Design for Autonomous Vehicles with Perception-based Observers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05201" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05201v1</a>
  <a href="https://arxiv.org/pdf/2509.05201.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05201v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05201v1', 'Robust Model Predictive Control Design for Autonomous Vehicles with Perception-based Observers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nariman Niknejad, Gokul S. Sankar, Bahare Kiumarsi, Hamidreza Modares

**分类**: cs.RO, cs.CV, cs.LG, eess.SY

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**针对深度学习感知误差，提出基于集合论状态估计的鲁棒模型预测控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `鲁棒模型预测控制` `深度学习感知` `非高斯噪声` `集合论状态估计` `约束zonotopes`

## 📋 核心要点

1. 传统MPC方法难以处理深度学习感知模块带来的非高斯噪声，导致控制性能下降甚至不稳定。
2. 采用基于集合的状态估计，使用约束zonotopes来描述感知误差，有效处理有偏差和重尾的不确定性。
3. 通过仿真和硬件实验验证，所提出的感知MPC在重尾噪声下表现优异，显著优于传统方法。

## 📝 摘要（中文）

本文提出了一种鲁棒模型预测控制（MPC）框架，该框架显式地解决了基于深度学习的感知模块中固有的非高斯噪声，这些模块用于状态估计。认识到感知模块的精确不确定性量化对于安全反馈控制至关重要，我们的方法偏离了感知误差的零均值噪声量化的传统假设。相反，它采用基于集合的状态估计与约束zonotopes来捕获有偏差的、重尾的不确定性，同时保持有界的估计误差。为了提高计算效率，鲁棒MPC被重新表述为线性规划（LP），使用基于Minkowski-Lyapunov的成本函数，并添加一个松弛变量以防止退化解。闭环稳定性通过Minkowski-Lyapunov不等式和收缩的zonotopic不变集来保证。然后，通过zonotopes的椭圆近似来推导最大的稳定终端集及其相应的反馈增益。所提出的框架通过全向移动机器人的仿真和硬件实验进行了验证，该机器人配备了摄像头和在ROS2框架内实现的基于卷积神经网络的感知模块。结果表明，感知感知的MPC在重尾噪声条件下提供了稳定和精确的控制性能，在状态估计误差边界和整体控制性能方面显著优于传统的基于高斯噪声的设计。

## 🔬 方法详解

**问题定义**：论文旨在解决自动驾驶车辆中，由于深度学习感知模块引入的非高斯噪声导致传统模型预测控制（MPC）性能下降的问题。现有方法通常假设感知误差服从高斯分布，这在实际应用中并不成立，尤其是在使用深度学习模型进行感知时，误差往往具有偏差和重尾特性，导致状态估计不准确，进而影响控制效果。

**核心思路**：论文的核心思路是采用集合论的方法来描述感知误差的不确定性，使用约束zonotopes来表示状态估计的不确定性集合。这种方法能够有效地处理非高斯噪声，并保证状态估计误差的有界性。同时，为了提高计算效率，将鲁棒MPC问题转化为线性规划问题进行求解。

**技术框架**：整体框架包括以下几个主要模块：1) 基于深度学习的感知模块，用于获取车辆状态的初步估计；2) 基于约束zonotopes的状态估计器，用于描述感知误差的不确定性；3) 鲁棒MPC控制器，基于状态估计器提供的状态集合，计算最优控制输入；4) Minkowski-Lyapunov稳定性分析，用于保证闭环系统的稳定性。

**关键创新**：论文的关键创新在于：1) 显式地考虑了深度学习感知模块带来的非高斯噪声，并采用集合论的方法进行建模；2) 将鲁棒MPC问题转化为线性规划问题，提高了计算效率；3) 基于Minkowski-Lyapunov理论，设计了保证闭环系统稳定性的控制器。

**关键设计**：关键设计包括：1) 使用约束zonotopes来描述状态估计的不确定性集合，zonotopes的大小反映了不确定性的程度；2) 设计基于Minkowski-Lyapunov的成本函数，并添加松弛变量以防止退化解；3) 通过zonotopes的椭圆近似来推导最大的稳定终端集及其相应的反馈增益。

## 📊 实验亮点

通过仿真和硬件实验，验证了所提出的感知MPC在重尾噪声条件下，相比于传统的基于高斯噪声的MPC，在状态估计误差边界和整体控制性能方面均有显著提升。具体而言，在相同的噪声条件下，所提出的方法能够更有效地抑制状态估计误差，并实现更精确的轨迹跟踪。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航等领域，尤其是在感知系统依赖于深度学习模型的场景下。通过更准确地量化感知误差，并将其纳入控制器的设计中，可以提高系统的安全性和可靠性，降低事故发生的风险。未来，该方法可以进一步推广到更复杂的系统和环境，例如无人机集群控制、复杂地形导航等。

## 📄 摘要（原文）

> This paper presents a robust model predictive control (MPC) framework that explicitly addresses the non-Gaussian noise inherent in deep learning-based perception modules used for state estimation. Recognizing that accurate uncertainty quantification of the perception module is essential for safe feedback control, our approach departs from the conventional assumption of zero-mean noise quantification of the perception error. Instead, it employs set-based state estimation with constrained zonotopes to capture biased, heavy-tailed uncertainties while maintaining bounded estimation errors. To improve computational efficiency, the robust MPC is reformulated as a linear program (LP), using a Minkowski-Lyapunov-based cost function with an added slack variable to prevent degenerate solutions. Closed-loop stability is ensured through Minkowski-Lyapunov inequalities and contractive zonotopic invariant sets. The largest stabilizing terminal set and its corresponding feedback gain are then derived via an ellipsoidal approximation of the zonotopes. The proposed framework is validated through both simulations and hardware experiments on an omnidirectional mobile robot along with a camera and a convolutional neural network-based perception module implemented within a ROS2 framework. The results demonstrate that the perception-aware MPC provides stable and accurate control performance under heavy-tailed noise conditions, significantly outperforming traditional Gaussian-noise-based designs in terms of both state estimation error bounding and overall control performance.

