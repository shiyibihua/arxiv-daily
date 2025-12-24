---
layout: default
title: Vision-driven River Following of UAV via Safe Reinforcement Learning using Semantic Dynamics Model
---

# Vision-driven River Following of UAV via Safe Reinforcement Learning using Semantic Dynamics Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09971" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09971v2</a>
  <a href="https://arxiv.org/pdf/2508.09971.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09971v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09971v2', 'Vision-driven River Following of UAV via Safe Reinforcement Learning using Semantic Dynamics Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Wang, Nina Mahmoudian

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-13 (更新: 2025-09-30)

**备注**: Submitted to Robotics and Autonomous Systems (RAS) journal

---

## 💡 一句话要点

**提出安全强化学习框架以解决无人机河流跟随问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无人机` `安全强化学习` `河流跟随` `语义动态模型` `边际增益优势估计` `环境监测` `自主导航`

## 📋 核心要点

1. 现有方法在复杂河流环境中进行安全导航时，面临GPS信号不可靠和历史依赖奖励的挑战。
2. 论文提出了边际增益优势估计、语义动态模型和约束演员动态估计器，旨在优化安全强化学习的性能。
3. 实验结果表明，MGAE在收敛速度和性能上优于传统的基于评论者的方法，SDM提供更准确的短期状态预测。

## 📝 摘要（中文）

基于视觉的无人机自主河流跟随对于救援、监视和环境监测等应用至关重要，尤其是在GPS信号不可靠的密集河流环境中。这些安全关键的导航任务必须在优化性能的同时满足严格的安全约束。此外，河流跟随的奖励本质上是历史依赖的（非马尔可夫），这使得标准的安全强化学习（SafeRL）面临挑战。为了解决这些问题，本文提出了三个贡献：首先，引入边际增益优势估计（MGAE），通过使用历史回报的滑动窗口基线来优化奖励优势函数。其次，开发了基于水体语义掩码的语义动态模型（SDM），提供更具可解释性和数据效率的短期预测。最后，提出了约束演员动态估计器（CADE）架构，将演员、成本估计器和SDM集成在一起，形成基于模型的SafeRL框架。

## 🔬 方法详解

**问题定义**：本文旨在解决无人机在复杂河流环境中进行安全自主导航的问题。现有的强化学习方法在处理历史依赖奖励和安全约束时存在不足，尤其是在GPS信号不可靠的情况下。

**核心思路**：论文提出的核心思路是通过引入边际增益优势估计（MGAE）和语义动态模型（SDM），来优化奖励估计和状态预测，从而提高安全强化学习的效果。这样的设计能够更好地适应非马尔可夫动态，并增强模型的可解释性。

**技术框架**：整体架构包括三个主要模块：边际增益优势估计（MGAE）、语义动态模型（SDM）和约束演员动态估计器（CADE）。MGAE用于优化奖励优势，SDM用于短期状态预测，而CADE则整合了演员和成本估计器以实现安全强化学习。

**关键创新**：最重要的技术创新点在于引入了MGAE和SDM，使得模型能够更好地处理历史依赖性和安全约束。与传统方法相比，MGAE通过滑动窗口基线优化奖励估计，SDM则提供了更高的数据效率和可解释性。

**关键设计**：在设计中，MGAE使用历史回报的滑动窗口作为基线，SDM基于水体语义掩码进行状态预测，CADE则通过Lagrangian方法在训练中实现奖励与安全的“软”平衡，同时在推理时施加“硬”动作覆盖。

## 📊 实验亮点

实验结果显示，MGAE在收敛速度上比传统的评论者方法（如广义优势估计）更快，且性能优越。SDM提供的短期状态预测准确性显著提高，使得成本估计器能够更好地预测潜在的安全违规情况。

## 🎯 应用场景

该研究的潜在应用领域包括无人机在救援、环境监测和监视等任务中的自主导航。通过提高在复杂河流环境中的安全性和效率，研究成果将为无人机技术的实际应用提供重要支持，推动相关领域的发展。

## 📄 摘要（原文）

> Vision-driven autonomous river following by Unmanned Aerial Vehicles is critical for applications such as rescue, surveillance, and environmental monitoring, particularly in dense riverine environments where GPS signals are unreliable. These safety-critical navigation tasks must satisfy hard safety constraints while optimizing performance. Moreover, the reward in river following is inherently history-dependent (non-Markovian) by which river segment has already been visited, making it challenging for standard safe Reinforcement Learning (SafeRL). To address these gaps, we propose three contributions. First, we introduce Marginal Gain Advantage Estimation, which refines the reward advantage function by using a sliding window baseline computed from historical episodic returns, aligning the advantage estimate with non-Markovian dynamics. Second, we develop a Semantic Dynamics Model based on patchified water semantic masks offering more interpretable and data-efficient short-term prediction of future observations compared to latent vision dynamics models. Third, we present the Constrained Actor Dynamics Estimator architecture, which integrates the actor, cost estimator, and SDM for cost advantage estimation to form a model-based SafeRL framework. Simulation results demonstrate that MGAE achieves faster convergence and superior performance over traditional critic-based methods like Generalized Advantage Estimation. SDM provides more accurate short-term state predictions that enable the cost estimator to better predict potential violations. Overall, CADE effectively integrates safety regulation into model-based RL, with the Lagrangian approach providing a "soft" balance between reward and safety during training, while the safety layer enhances inference by imposing a "hard" action overlay.

