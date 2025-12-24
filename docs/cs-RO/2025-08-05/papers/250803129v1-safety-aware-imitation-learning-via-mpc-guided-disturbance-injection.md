---
layout: default
title: Safety-Aware Imitation Learning via MPC-Guided Disturbance Injection
---

# Safety-Aware Imitation Learning via MPC-Guided Disturbance Injection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03129" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03129v1</a>
  <a href="https://arxiv.org/pdf/2508.03129.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03129v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03129v1', 'Safety-Aware Imitation Learning via MPC-Guided Disturbance Injection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Le Qiu, Yusuf Umut Ciftci, Somil Bansal

**分类**: cs.RO

**发布日期**: 2025-08-05

**🔗 代码/项目**: [PROJECT_PAGE](https://leqiu2003.github.io/MPCSafeGIL/)

---

## 💡 一句话要点

**提出MPC-SafeGIL以解决模仿学习中的安全性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模仿学习` `安全性` `模型预测控制` `对抗性干扰` `机器人行为` `动态系统` `四足动物运动` `视觉运动导航`

## 📋 核心要点

1. 现有的模仿学习方法在安全关键应用中存在安全性不足的问题，容易导致策略错误和安全违规。
2. MPC-SafeGIL通过在专家示范中注入对抗性干扰，增强模仿学习的安全性，使得学习策略能够应对更广泛的安全场景。
3. 实验结果表明，MPC-SafeGIL在四足动物运动和视觉运动导航任务中均显著提高了安全性和任务性能。

## 📝 摘要（中文）

模仿学习为从专家示范中学习复杂机器人行为提供了有前景的方法。然而，学习到的策略可能会出现错误，导致安全违规，这限制了其在安全关键应用中的部署。我们提出了MPC-SafeGIL，这是一种设计时的方法，通过在专家示范中注入对抗性干扰来增强模仿学习的安全性。这使得专家暴露于更广泛的安全关键场景中，并允许模仿策略学习稳健的恢复行为。我们的方法使用基于采样的模型预测控制（MPC）来近似最坏情况干扰，使其可扩展到高维和黑箱动态系统。与依赖于分析模型或互动专家的先前工作相比，MPC-SafeGIL将安全考虑直接集成到数据收集过程中。我们通过包括四足动物运动和视觉运动导航的广泛仿真实验以及在四旋翼上的真实世界实验验证了我们的方法，展示了安全性和任务性能的提升。

## 🔬 方法详解

**问题定义**：论文要解决的问题是模仿学习中策略的安全性不足，现有方法在面对复杂和动态环境时容易导致安全违规，限制了其在实际应用中的有效性。

**核心思路**：论文提出MPC-SafeGIL，通过在专家示范中注入对抗性干扰，使模仿学习策略能够学习到更稳健的恢复行为，从而提高安全性。此设计使得策略在面对未知干扰时能够更有效地应对。

**技术框架**：MPC-SafeGIL的整体架构包括数据收集、对抗性干扰注入、模仿学习和策略优化四个主要模块。首先，通过MPC生成对抗性干扰，然后将其注入专家示范中，最后利用这些数据训练模仿策略。

**关键创新**：最重要的技术创新在于将安全性考虑直接集成到数据收集过程中，而不是依赖于传统的分析模型或专家互动。这种方法使得模仿学习能够在更复杂的环境中进行有效训练。

**关键设计**：在设计中，使用了基于采样的模型预测控制（MPC）来近似最坏情况干扰，确保方法的可扩展性。此外，损失函数的设计考虑了安全性和任务性能的平衡，以实现更优的学习效果。

## 📊 实验亮点

实验结果显示，MPC-SafeGIL在四足动物运动和视觉运动导航任务中，相较于基线方法，安全性提升了显著的比例，同时任务性能也得到了明显改善，验证了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人、无人机导航和其他安全关键的自动化系统。通过提高模仿学习的安全性，MPC-SafeGIL能够在复杂和动态环境中实现更可靠的机器人行为，推动智能机器人在实际应用中的广泛部署。

## 📄 摘要（原文）

> Imitation Learning has provided a promising approach to learning complex robot behaviors from expert demonstrations. However, learned policies can make errors that lead to safety violations, which limits their deployment in safety-critical applications. We propose MPC-SafeGIL, a design-time approach that enhances the safety of imitation learning by injecting adversarial disturbances during expert demonstrations. This exposes the expert to a broader range of safety-critical scenarios and allows the imitation policy to learn robust recovery behaviors. Our method uses sampling-based Model Predictive Control (MPC) to approximate worst-case disturbances, making it scalable to high-dimensional and black-box dynamical systems. In contrast to prior work that relies on analytical models or interactive experts, MPC-SafeGIL integrates safety considerations directly into data collection. We validate our approach through extensive simulations including quadruped locomotion and visuomotor navigation and real-world experiments on a quadrotor, demonstrating improvements in both safety and task performance. See our website here: https://leqiu2003.github.io/MPCSafeGIL/

