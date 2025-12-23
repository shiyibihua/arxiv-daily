---
layout: default
title: Locomotion on Constrained Footholds via Layered Architectures and Model Predictive Control
---

# Locomotion on Constrained Footholds via Layered Architectures and Model Predictive Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09979" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09979v2</a>
  <a href="https://arxiv.org/pdf/2506.09979.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09979v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09979v2', 'Locomotion on Constrained Footholds via Layered Architectures and Model Predictive Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zachary Olkin, Aaron D. Ames

**分类**: cs.RO

**发布日期**: 2025-06-11 (更新: 2025-08-24)

**备注**: Accepted to Humanoids 2025

---

## 💡 一句话要点

**提出分层架构与模型预测控制以解决腿部机器人运动问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `腿部机器人` `模型预测控制` `分层架构` `实时控制` `运动规划` `优化算法`

## 📋 核心要点

1. 核心问题：现有方法在处理腿部机器人运动时，面临非线性和高维度带来的实时控制难题。
2. 方法要点：提出分层架构，将离散变量选择与平滑的模型预测控制相结合，提升实时性能与灵活性。
3. 实验或效果：在四足机器人和人形机器人上进行实验，结果显示该方法比传统启发式方法更优且计算速度更快。

## 📝 摘要（中文）

实时计算腿部机器人稳定和最优控制动作面临挑战，主要由于其非线性、混合和高维特性。系统的混合特性引入了离散和连续变量的组合，导致数值最优控制出现问题。为了解决这些挑战，本文提出了一种分层架构，将离散变量的选择与平滑的模型预测控制器（MPC）分开。该架构通过结合无梯度和基于梯度的方法，实现了在线灵活性和最优性，而不牺牲实时性能。实验结果表明，该方法在四足机器人跨越间隙和在不同高度地形上行走时表现出更优的性能和可靠性。

## 🔬 方法详解

**问题定义**：本文旨在解决腿部机器人在复杂环境中实时控制的挑战，现有方法在处理混合系统时常常面临离散与连续变量的冲突，导致控制效果不佳。

**核心思路**：提出一种分层架构，通过将离散变量的选择与平滑的模型预测控制器（MPC）分开，允许在保证实时性的同时实现在线优化和灵活性。

**技术框架**：整体架构包括两个主要模块：第一部分是基于采样的方法用于确定离散变量，第二部分是使用固定离散变量的经典平滑MPC公式。该架构允许在控制过程中动态调整离散选择。

**关键创新**：最重要的技术创新在于分层架构的设计，使得控制策略能够在不牺牲实时性的情况下，灵活地处理复杂的运动任务。这一方法比传统的启发式方法更为可靠且计算速度更快。

**关键设计**：在设计中，采用了无梯度和基于梯度的方法相结合的策略，以提高优化效率。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文获取更多细节。

## 📊 实验亮点

实验结果表明，所提出的分层控制方法在四足机器人跨越间隙和不同高度地形的任务中，表现出比传统启发式方法更优的性能，且计算速度显著提升，具体性能数据在实验部分有详细说明。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、自动驾驶和人机协作等场景，能够有效提升机器人在复杂环境中的运动能力和适应性。未来，该方法有望推动腿部机器人在实际应用中的广泛部署，提升其智能化水平。

## 📄 摘要（原文）

> Computing stabilizing and optimal control actions for legged locomotion in real time is difficult due to the nonlinear, hybrid, and high dimensional nature of these robots. The hybrid nature of the system introduces a combination of discrete and continuous variables which causes issues for numerical optimal control. To address these challenges, we propose a layered architecture that separates the choice of discrete variables and a smooth Model Predictive Controller (MPC). The layered formulation allows for online flexibility and optimality without sacrificing real-time performance through a combination of gradient-free and gradient-based methods. The architecture leverages a sampling-based method for determining discrete variables, and a classical smooth MPC formulation using these fixed discrete variables. We demonstrate the results on a quadrupedal robot stepping over gaps and onto terrain with varying heights. In simulation, we demonstrate the controller on a humanoid robot for gap traversal. The layered approach is shown to be more optimal and reliable than common heuristic-based approaches and faster to compute than pure sampling methods.

