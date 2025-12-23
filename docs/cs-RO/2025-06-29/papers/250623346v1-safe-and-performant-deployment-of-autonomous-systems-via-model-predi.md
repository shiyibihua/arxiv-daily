---
layout: default
title: Safe and Performant Deployment of Autonomous Systems via Model Predictive Control and Hamilton-Jacobi Reachability Analysis
---

# Safe and Performant Deployment of Autonomous Systems via Model Predictive Control and Hamilton-Jacobi Reachability Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23346" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23346v1</a>
  <a href="https://arxiv.org/pdf/2506.23346.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23346v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23346v1', 'Safe and Performant Deployment of Autonomous Systems via Model Predictive Control and Hamilton-Jacobi Reachability Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Wang, Armand Jordana, Ludovic Righetti, Somil Bansal

**分类**: cs.RO, eess.SY

**发布日期**: 2025-06-29

**备注**: RSS 2025 Workshop on Reliable Robotics

---

## 💡 一句话要点

**提出基于模型预测控制和哈密顿-雅可比可达性分析的安全高效自主系统部署框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `哈密顿-雅可比分析` `自主系统` `安全性` `任务性能` `高维系统` `控制策略`

## 📋 核心要点

1. 现有自主系统在执行复杂任务时，往往面临安全性和性能之间的权衡，缺乏有效的解决方案。
2. 本文提出了一种结合模型预测控制和哈密顿-雅可比可达性分析的框架，以优化任务性能并确保安全性。
3. 通过仿真实验，框架在安全约束满足方面显著优于基线方法，展示了其有效性和可扩展性。

## 📝 摘要（中文）

尽管我们在算法上取得了显著进展，使自主系统能够执行复杂任务，但在有效性和安全性之间仍然存在困难。现有方法往往无法提供安全保障，或在安全性上大幅妥协任务性能。本文提出了一种基于模型预测控制（MPC）和哈密顿-雅可比（HJ）可达性分析的框架，旨在优化自主系统的任务性能，同时遵循安全约束。该框架保证了MPC控制器的递归可行性，并且可扩展到高维系统。通过对4D杜宾车和6自由度Kuka iiwa机械臂的两项仿真实验，结果表明该框架显著提高了系统对安全约束的满足程度。

## 🔬 方法详解

**问题定义**：本文旨在解决自主系统在执行任务时的安全性与性能之间的矛盾。现有方法往往无法同时满足安全保障和高效性能的要求，导致自主系统在复杂环境中的应用受限。

**核心思路**：提出的框架结合了模型预测控制（MPC）和哈密顿-雅可比（HJ）可达性分析，通过优化控制策略来确保在遵循安全约束的同时提升任务性能。这样的设计使得系统能够在动态环境中进行有效决策。

**技术框架**：整体架构包括两个主要模块：首先是基于MPC的控制器设计，其次是HJ可达性分析用于评估安全性。框架通过递归可行性保证MPC控制器在高维系统中的有效性。

**关键创新**：该研究的核心创新在于将MPC与HJ可达性分析相结合，形成了一种新的控制策略，能够在保证安全性的同时优化任务性能。这一方法在高维系统中表现出良好的可扩展性。

**关键设计**：在设计中，MPC控制器的参数设置经过精心调整，以确保其在动态环境中的稳定性和响应速度。同时，HJ可达性分析的算法实现也经过优化，以提高计算效率和准确性。

## 📊 实验亮点

实验结果显示，所提出的框架在安全约束满足方面显著优于基线方法，具体表现为在4D杜宾车和6自由度Kuka iiwa机械臂的仿真中，安全约束满足率提高了显著的百分比，验证了框架的有效性和实用性。

## 🎯 应用场景

该研究的框架可广泛应用于自主驾驶、机器人操作和无人机等领域，具有重要的实际价值。通过确保安全性与性能的平衡，该框架能够推动自主系统在复杂环境中的应用，提升其在实际场景中的可靠性和效率。

## 📄 摘要（原文）

> While we have made significant algorithmic developments to enable autonomous systems to perform sophisticated tasks, it remains difficult for them to perform tasks effective and safely. Most existing approaches either fail to provide any safety assurances or substantially compromise task performance for safety. In this work, we develop a framework, based on model predictive control (MPC) and Hamilton-Jacobi (HJ) reachability, to optimize task performance for autonomous systems while respecting the safety constraints. Our framework guarantees recursive feasibility for the MPC controller, and it is scalable to high-dimensional systems. We demonstrate the effectiveness of our framework with two simulation studies using a 4D Dubins Car and a 6 Dof Kuka iiwa manipulator, and the experiments show that our framework significantly improves the safety constraints satisfaction of the systems over the baselines.

