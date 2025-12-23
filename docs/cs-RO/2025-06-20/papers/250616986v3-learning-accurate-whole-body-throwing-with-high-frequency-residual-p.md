---
layout: default
title: Learning Accurate Whole-body Throwing with High-frequency Residual Policy and Pullback Tube Acceleration
---

# Learning Accurate Whole-body Throwing with High-frequency Residual Policy and Pullback Tube Acceleration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16986" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16986v3</a>
  <a href="https://arxiv.org/pdf/2506.16986.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16986v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16986v3', 'Learning Accurate Whole-body Throwing with High-frequency Residual Policy and Pullback Tube Acceleration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuntao Ma, Yang Liu, Kaixian Qu, Marco Hutter

**分类**: cs.RO

**发布日期**: 2025-06-20 (更新: 2025-06-24)

**备注**: 8 pages, IROS 2025

---

## 💡 一句话要点

**提出高频残差策略与拉回管加速的整体投掷控制框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人投掷` `动态操控` `高频残差策略` `末端执行器控制` `腿式移动操控器`

## 📋 核心要点

1. 现有方法在机器人投掷任务中面临精度不足和控制不稳定的问题，限制了其在动态环境中的应用。
2. 本文提出的控制框架结合了名义跟踪策略和高频残差策略，旨在提高投掷的精度和稳定性。
3. 实验结果表明，所提系统在投掷精度和成功率上显著优于人类，展示了其在动态操控中的潜力。

## 📝 摘要（中文）

投掷是一项基本技能，使机器人能够以超出其手臂范围的方式操控物体。本文提出了一种控制框架，结合了学习和基于模型的控制，用于腿式移动操控器的整体投掷。该框架由三个部分组成：末端执行器的名义跟踪策略、高频残差策略以增强跟踪精度，以及基于优化的模块以改善末端执行器的加速度控制。实验结果显示，在6米远的目标投掷中，平均落点误差为0.28米。此外，与大学生的比较研究中，该系统在3-5米距离内随机投掷小目标时，速度跟踪误差为0.398米/秒，成功率为56.8%，而人类的成功率仅为15.2%。这项工作为动态整体操控中的可抓取投掷提供了量化精度的早期演示。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在动态环境中进行整体投掷时的精度不足和控制不稳定的问题。现有方法往往依赖于简单的控制策略，难以适应复杂的投掷任务。

**核心思路**：论文提出的控制框架通过结合学习与模型驱动的控制方法，利用高频残差策略来增强末端执行器的跟踪精度，从而实现更为精准的投掷。

**技术框架**：整体框架由三个主要模块组成：1) 名义跟踪策略，负责末端执行器的基本控制；2) 高频残差策略，实时调整控制输出以提高跟踪精度；3) 优化模块，专注于末端执行器的加速度控制，确保投掷过程中的稳定性。

**关键创新**：最重要的创新在于引入高频残差策略，该策略能够在快速变化的动态环境中实时调整控制信号，显著提升了投掷的精度和成功率。

**关键设计**：在设计中，采用了优化算法来调整加速度控制参数，并通过实验验证了不同策略的有效性，确保了系统在多种投掷条件下的稳定性和可靠性。

## 📊 实验亮点

实验结果显示，所提控制系统在6米远的目标投掷中实现了平均0.28米的落点误差，成功率达到56.8%，显著高于人类的15.2%。此外，系统的速度跟踪误差为0.398米/秒，展示了其在动态操控中的优越性能。

## 🎯 应用场景

该研究的潜在应用领域包括机器人运动控制、自动化制造、救援任务等，能够帮助机器人在复杂环境中进行精确的物体投掷和操控。未来，该技术可能推动机器人在动态环境中的自主决策能力，提升其在实际应用中的价值。

## 📄 摘要（原文）

> Throwing is a fundamental skill that enables robots to manipulate objects in ways that extend beyond the reach of their arms. We present a control framework that combines learning and model-based control for prehensile whole-body throwing with legged mobile manipulators. Our framework consists of three components: a nominal tracking policy for the end-effector, a high-frequency residual policy to enhance tracking accuracy, and an optimization-based module to improve end-effector acceleration control. The proposed controller achieved the average of 0.28 m landing error when throwing at targets located 6 m away. Furthermore, in a comparative study with university students, the system achieved a velocity tracking error of 0.398 m/s and a success rate of 56.8%, hitting small targets randomly placed at distances of 3-5 m while throwing at a specified speed of 6 m/s. In contrast, humans have a success rate of only 15.2%. This work provides an early demonstration of prehensile throwing with quantified accuracy on hardware, contributing to progress in dynamic whole-body manipulation.

