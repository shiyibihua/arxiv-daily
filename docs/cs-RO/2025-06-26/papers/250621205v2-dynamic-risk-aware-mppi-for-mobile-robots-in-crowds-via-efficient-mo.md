---
layout: default
title: Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations
---

# Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21205" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21205v2</a>
  <a href="https://arxiv.org/pdf/2506.21205.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21205v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21205v2', 'Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Elia Trevisan, Khaled A. Mustafa, Godert Notten, Xinwei Wang, Javier Alonso-Mora

**分类**: cs.RO

**发布日期**: 2025-06-26 (更新: 2025-08-20)

**备注**: Accepted for presentation at IROS 2025. Accepted Version

---

## 💡 一句话要点

**提出动态风险感知MPPI以解决移动机器人在人群中的安全导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `动态风险感知` `模型预测控制` `碰撞概率` `蒙特卡洛方法` `移动机器人` `安全导航` `动态障碍物` `路径优化`

## 📋 核心要点

1. 现有方法在处理动态环境中的不确定性时，难以有效预测其他代理的轨迹，导致安全性不足。
2. 本文提出的DRA-MPPI通过结合非高斯随机预测，利用蒙特卡洛方法高效近似碰撞概率，增强了运动规划的安全性。
3. 实验结果显示，DRA-MPPI在多个动态障碍物的环境中，相较于S-MPC、Frenet规划器和传统MPPI，表现出显著的性能提升。

## 📝 摘要（中文）

在人员密集的环境中安全部署移动机器人需要运动规划器考虑其他代理预测轨迹的不确定性。传统方法在处理任意形状的预测和实时约束时面临挑战。为此，本文提出了一种动态风险感知模型预测路径积分控制（DRA-MPPI），该方法结合了可能非高斯的随机预测来建模未来的不确定运动。通过利用MPPI的无梯度特性，本文提出了一种高效的蒙特卡洛方法，实时近似多个动态障碍物之间的联合碰撞概率。这使得可以拒绝超过预定义碰撞概率阈值的样本，或将碰撞概率作为导航成本函数中的加权目标。DRA-MPPI有效缓解了机器人冻结问题，同时增强了安全性。实地和模拟实验表明，DRA-MPPI在多个动态障碍物的情况下表现优于现有的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决移动机器人在人员密集环境中安全导航的问题，现有方法在处理动态障碍物的轨迹预测时存在不确定性和实时性不足的痛点。

**核心思路**：DRA-MPPI通过引入动态风险感知的模型预测路径积分控制，结合非高斯随机预测，能够有效处理未来运动的不确定性，从而提高安全性和导航效率。

**技术框架**：该方法的整体架构包括样本生成、碰撞概率计算和路径优化三个主要模块。首先生成多个轨迹样本，然后通过蒙特卡洛方法计算这些样本的碰撞概率，最后优化路径以降低碰撞风险。

**关键创新**：DRA-MPPI的主要创新在于其高效的碰撞概率近似方法，能够实时处理多个动态障碍物的情况，并将碰撞概率作为加权目标融入导航成本函数中，显著提升了安全性。

**关键设计**：在参数设置上，DRA-MPPI定义了一个预设的碰撞概率阈值，并采用加权目标函数来平衡路径优化与安全性，确保机器人在复杂环境中的有效导航。具体的损失函数设计和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，DRA-MPPI在多个动态障碍物的环境中，成功降低了碰撞概率，提升了导航效率。与S-MPC、Frenet规划器和传统MPPI相比，DRA-MPPI在安全性和实时性方面均表现出显著的提升，具体性能数据在论文中详细列出。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、服务机器人、无人机导航等，能够在复杂和动态的环境中实现安全高效的自主导航。未来，该技术有望推动人机协作的安全性，提升机器人在公共场所的应用价值。

## 📄 摘要（原文）

> Deploying mobile robots safely among humans requires the motion planner to account for the uncertainty in the other agents' predicted trajectories. This remains challenging in traditional approaches, especially with arbitrarily shaped predictions and real-time constraints. To address these challenges, we propose a Dynamic Risk-Aware Model Predictive Path Integral control (DRA-MPPI), a motion planner that incorporates uncertain future motions modelled with potentially non-Gaussian stochastic predictions. By leveraging MPPI's gradient-free nature, we propose a method that efficiently approximates the joint Collision Probability (CP) among multiple dynamic obstacles for several hundred sampled trajectories in real-time via a Monte Carlo (MC) approach. This enables the rejection of samples exceeding a predefined CP threshold or the integration of CP as a weighted objective within the navigation cost function. Consequently, DRA-MPPI mitigates the freezing robot problem while enhancing safety. Real-world and simulated experiments with multiple dynamic obstacles demonstrate DRA-MPPI's superior performance compared to state-of-the-art approaches, including Scenario-based Model Predictive Control (S-MPC), Frenet planner, and vanilla MPPI.

