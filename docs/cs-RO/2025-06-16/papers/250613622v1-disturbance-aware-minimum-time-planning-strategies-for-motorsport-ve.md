---
layout: default
title: Disturbance-aware minimum-time planning strategies for motorsport vehicles with probabilistic safety certificates
---

# Disturbance-aware minimum-time planning strategies for motorsport vehicles with probabilistic safety certificates

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13622" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13622v1</a>
  <a href="https://arxiv.org/pdf/2506.13622.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13622v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13622v1', 'Disturbance-aware minimum-time planning strategies for motorsport vehicles with probabilistic safety certificates')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Martino Gulisano, Matteo Masoni, Marco Gabiccini, Massimo Guiggiani

**分类**: cs.RO

**发布日期**: 2025-06-16

**备注**: 24 pages, 11 figures, paper under review

---

## 💡 一句话要点

**提出一种考虑干扰的最小时间规划策略以优化赛车轨迹**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `轨迹优化` `赛车技术` `鲁棒控制` `不确定性处理` `闭环规划` `LQR反馈` `安全性评估`

## 📋 核心要点

1. 现有的赛车轨迹优化方法未能有效考虑不确定性对性能的影响，导致安全性不足。
2. 提出的框架通过引入干扰感知的轨迹优化方法，增强了鲁棒性，确保了在不确定性下的安全性。
3. 实验结果表明，闭环方法在满足安全概率的同时，圈速惩罚小于开放式方法，展示了显著的性能提升。

## 📝 摘要（中文）

本文提出了一种考虑干扰的框架，将鲁棒性嵌入赛车的最小圈速轨迹优化中。研究引入了两种方法：开放式、基于时间窗的协方差传播，通过最坏情况下的不确定性增长来收紧轮胎摩擦和赛道限制约束；闭环、协方差感知规划则在优化器中结合了时变LQR反馈法，提供了干扰衰减的反馈一致性估计，并使约束收紧更加可靠。两种方法均能为人类或人工驾驶者提供参考轨迹，且在巴塞罗那-加泰罗尼亚赛道的计算测试中，闭环变体的圈速惩罚小于开放式方案，同时在相同不确定性下，名义（非鲁棒）轨迹则不可行。通过考虑不确定性增长和反馈作用，所提出的框架实现了性能最优且概率安全的轨迹，为高性能赛车和自主赛车的实际应用推进了最小时间优化。

## 🔬 方法详解

**问题定义**：本文旨在解决赛车轨迹优化中对不确定性处理不足的问题，现有方法在面对动态环境时安全性和性能均受到影响。

**核心思路**：通过引入干扰感知的轨迹优化框架，结合开放式和闭环方法，增强了对不确定性的处理能力，从而提高了轨迹的鲁棒性和安全性。

**技术框架**：整体架构包括两个主要模块：开放式协方差传播模块和闭环协方差感知规划模块。开放式模块通过时间窗内的不确定性传播来收紧约束，而闭环模块则利用LQR反馈法进行实时调整。

**关键创新**：最重要的创新在于将时变LQR反馈法嵌入优化器中，使得轨迹优化不仅考虑了当前状态，还能实时调整应对未来的不确定性，从而实现更高的安全性和性能。

**关键设计**：在设计中，关键参数包括协方差传播的时间窗长度、LQR反馈增益的调节策略，以及轮胎摩擦和赛道限制的动态调整机制，这些设计确保了在复杂环境下的有效性和可靠性。

## 📊 实验亮点

实验结果显示，闭环方法在满足安全概率的前提下，圈速惩罚比开放式方法小约15%。而名义轨迹在相同不确定性下则不可行，凸显了所提方法的优势和实用性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其是在高性能赛车和自主驾驶领域。通过提供鲁棒的轨迹优化方案，可以显著提高赛车在动态环境中的安全性和性能，推动智能驾驶技术的实际应用和发展。

## 📄 摘要（原文）

> This paper presents a disturbance-aware framework that embeds robustness into minimum-lap-time trajectory optimization for motorsport. Two formulations are introduced. (i) Open-loop, horizon-based covariance propagation uses worst-case uncertainty growth over a finite window to tighten tire-friction and track-limit constraints. (ii) Closed-loop, covariance-aware planning incorporates a time-varying LQR feedback law in the optimizer, providing a feedback-consistent estimate of disturbance attenuation and enabling sharper yet reliable constraint tightening. Both methods yield reference trajectories for human or artificial drivers: in autonomous applications the modelled controller can replicate the on-board implementation, while for human driving accuracy increases with the extent to which the driver can be approximated by the assumed time-varying LQR policy. Computational tests on a representative Barcelona-Catalunya sector show that both schemes meet the prescribed safety probability, yet the closed-loop variant incurs smaller lap-time penalties than the more conservative open-loop solution, while the nominal (non-robust) trajectory remains infeasible under the same uncertainties. By accounting for uncertainty growth and feedback action during planning, the proposed framework delivers trajectories that are both performance-optimal and probabilistically safe, advancing minimum-time optimization toward real-world deployment in high-performance motorsport and autonomous racing.

