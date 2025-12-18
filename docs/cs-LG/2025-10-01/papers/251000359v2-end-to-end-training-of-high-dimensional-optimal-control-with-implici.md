---
layout: default
title: End-to-End Training of High-Dimensional Optimal Control with Implicit Hamiltonians via Jacobian-Free Backpropagation
---

# End-to-End Training of High-Dimensional Optimal Control with Implicit Hamiltonians via Jacobian-Free Backpropagation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00359" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00359v2</a>
  <a href="https://arxiv.org/pdf/2510.00359.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00359v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00359v2', 'End-to-End Training of High-Dimensional Optimal Control with Implicit Hamiltonians via Jacobian-Free Backpropagation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eric Gelphman, Deepanshu Verma, Nicole Tianjiao Yang, Stanley Osher, Samy Wu Fung

**分类**: math.OC, cs.LG

**发布日期**: 2025-10-01 (更新: 2025-10-07)

---

## 💡 一句话要点

**提出基于隐式哈密顿量的端到端高维最优控制方法，通过无雅可比反向传播实现高效训练。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `最优控制` `隐式哈密顿量` `深度学习` `无雅可比反向传播` `值函数` `反馈控制器`

## 📋 核心要点

1. 现有方法难以处理具有隐式哈密顿量的高维最优控制问题，限制了其在实际问题中的应用。
2. 该方法直接参数化值函数，利用最优控制与值函数梯度的关系，学习最优控制律，无需显式哈密顿量公式。
3. 通过无雅可比反向传播（JFB）实现高效训练，并在多个涉及隐式哈密顿量的场景中验证了方法的有效性。

## 📝 摘要（中文）

本文提出了一种端到端的隐式深度学习方法，直接参数化值函数来学习最优控制律，从而解决具有隐式哈密顿量的高维最优控制问题。现有方法在哈密顿量具有显式公式时，可以通过参数化值函数的神经网络来近似高维最优反馈控制器。然而，许多实际问题，如航天飞机再入问题和自行车动力学等，涉及不具有显式公式的隐式哈密顿量，限制了现有方法的适用性。本文方法通过确保训练后的网络遵守控制规律来强化物理原则，利用最优控制和值函数梯度之间的基本关系。通过使用无雅可比反向传播（JFB），即使在轨迹优化中存在时间耦合，也能实现高效训练。实验表明，该方法有效地学习了涉及隐式哈密顿量的多个场景中的高维反馈控制器，这是现有方法无法解决的。

## 🔬 方法详解

**问题定义**：论文旨在解决高维最优控制问题，特别是在哈密顿量没有显式表达式的情况下。现有方法通常依赖于显式哈密顿量，或者直接参数化控制策略，这在处理复杂系统时效率低下或难以实现。这些方法无法充分利用哈密顿量的内在结构，导致性能受限。

**核心思路**：论文的核心思路是直接参数化值函数，并通过神经网络学习最优控制律。这种方法避免了对显式哈密顿量的依赖，并且能够利用值函数与最优控制之间的关系（通过Pontryagin最大值原理和动态规划）。通过确保训练后的网络满足控制规律，可以强化物理约束，提高控制器的鲁棒性。

**技术框架**：整体框架包括以下几个主要步骤：1) 定义系统的动力学方程和目标函数；2) 使用神经网络参数化值函数；3) 利用Pontryagin最大值原理推导出最优控制与值函数梯度的关系；4) 使用无雅可比反向传播（JFB）训练神经网络，优化值函数，使其满足最优控制条件。JFB用于高效地计算梯度，避免了显式计算雅可比矩阵的复杂性。

**关键创新**：最重要的创新点在于使用隐式哈密顿量进行端到端训练，并结合无雅可比反向传播。与现有方法相比，该方法不需要显式哈密顿量，可以直接学习最优控制律，从而扩展了最优控制的应用范围。JFB的使用显著提高了训练效率，使得处理高维问题成为可能。

**关键设计**：关键设计包括：1) 使用深度神经网络来参数化值函数，网络的结构需要根据具体问题进行调整；2) 定义合适的损失函数，例如，可以包括值函数满足Bellman方程的程度，以及控制策略的稳定性；3) 使用无雅可比反向传播（JFB）来计算梯度，JFB的具体实现依赖于自动微分工具；4) 选择合适的优化算法，例如Adam或L-BFGS，并调整学习率等超参数。

## 📊 实验亮点

实验结果表明，该方法在涉及隐式哈密顿量的多个场景中，能够有效地学习高维反馈控制器。例如，在航天飞机再入问题和自行车动力学问题中，该方法能够找到最优控制策略，并且优于现有的基于显式哈密顿量的方法。此外，JFB的使用显著提高了训练效率，使得该方法能够处理更高维度的问题。

## 🎯 应用场景

该研究成果可应用于各种涉及复杂动力学系统和隐式哈密顿量的控制问题，例如航天器姿态控制、机器人运动规划、能源系统优化等。通过学习最优控制策略，可以提高系统的性能、效率和鲁棒性，降低运营成本，并为复杂系统的自动化控制提供新的解决方案。

## 📄 摘要（原文）

> Neural network approaches that parameterize value functions have succeeded in approximating high-dimensional optimal feedback controllers when the Hamiltonian admits explicit formulas. However, many practical problems, such as the space shuttle reentry problem and bicycle dynamics, among others, may involve implicit Hamiltonians that do not admit explicit formulas, limiting the applicability of existing methods. Rather than directly parameterizing controls, which does not leverage the Hamiltonian's underlying structure, we propose an end-to-end implicit deep learning approach that directly parameterizes the value function to learn optimal control laws. Our method enforces physical principles by ensuring trained networks adhere to the control laws by exploiting the fundamental relationship between the optimal control and the value function's gradient; this is a direct consequence of the connection between Pontryagin's Maximum Principle and dynamic programming. Using Jacobian-Free Backpropagation (JFB), we achieve efficient training despite temporal coupling in trajectory optimization. We show that JFB produces descent directions for the optimal control objective and experimentally demonstrate that our approach effectively learns high-dimensional feedback controllers across multiple scenarios involving implicit Hamiltonians, which existing methods cannot address.

