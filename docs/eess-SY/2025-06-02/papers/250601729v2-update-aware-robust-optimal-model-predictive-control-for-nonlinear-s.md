---
layout: default
title: Update-Aware Robust Optimal Model Predictive Control for Nonlinear Systems
---

# Update-Aware Robust Optimal Model Predictive Control for Nonlinear Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.01729" class="toolbar-btn" target="_blank">📄 arXiv: 2506.01729v2</a>
  <a href="https://arxiv.org/pdf/2506.01729.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.01729v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.01729v2', 'Update-Aware Robust Optimal Model Predictive Control for Nonlinear Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: J. Wehbeh, E. C. Kerrigan

**分类**: eess.SY, math.OC

**发布日期**: 2025-06-02 (更新: 2025-09-03)

**备注**: 6 pages, 2 figures, published in the IEEE Control System Letters (2025)

**DOI**: [10.1109/LCSYS.2025.3576534](https://doi.org/10.1109/LCSYS.2025.3576534)

---

## 💡 一句话要点

**提出更新感知的鲁棒最优模型预测控制以解决非线性系统问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `鲁棒控制` `非线性系统` `轨迹优化` `更新感知` `最坏情况性能` `半无限程序`

## 📋 核心要点

1. 现有的鲁棒最优MPC方法未能考虑未来控制轨迹的更新，导致设计过于保守。
2. 本文提出了一种更新感知的鲁棒最优MPC算法，能够显式考虑未来的控制轨迹更新，从而优化性能。
3. 在平面四旋翼问题的实验中，所提方法明显优于不考虑未来更新的等效方法，尽管计算时间有所增加。

## 📝 摘要（中文）

鲁棒最优或最小-最大模型预测控制（MPC）方法旨在保证在已知的、有界的不确定性集合中满足约束，同时最小化最坏情况下的性能界限。传统方法计算固定预测视野下的轨迹，应用部分输入后在下一个时间步重新求解MPC问题。然而，这种方法未考虑未来控制轨迹的更新，可能导致保守设计。本文提出了一种新颖的更新感知鲁棒最优MPC算法，专门针对非线性系统的减少视野问题，显式考虑未来控制轨迹的更新。这一新思路使得我们的方法能够证明性地扩展可行解集，并保证相比现有技术的更优最坏情况性能界限。

## 🔬 方法详解

**问题定义**：本文解决的是在非线性系统中，如何在考虑未来控制轨迹更新的情况下进行鲁棒最优模型预测控制的问题。现有方法在固定预测视野下进行计算，未能有效利用未来信息，导致保守设计。

**核心思路**：论文的核心思路是通过更新感知的方式，显式考虑未来控制轨迹的变化，从而在设计时扩展可行解集，优化最坏情况性能界限。这样的设计使得控制策略更加灵活，能够适应未来的变化。

**技术框架**：整体架构包括将轨迹生成问题形式化为一系列嵌套的存在约束半无限程序（SIPs），这些程序可以通过局部简化技术高效求解。主要模块包括轨迹生成、约束处理和性能评估。

**关键创新**：最重要的技术创新点在于引入了更新感知的概念，使得控制策略能够动态适应未来的变化，显著改善了最坏情况性能界限。这与传统方法的静态设计形成鲜明对比。

**关键设计**：在参数设置上，采用了适应性调整的策略，以平衡计算复杂性和性能提升。损失函数设计上，考虑了未来轨迹的影响，确保在优化过程中能够有效利用未来信息。

## 📊 实验亮点

在平面四旋翼问题的实验中，所提更新感知鲁棒最优MPC方法相比于不考虑未来更新的基线方法，表现出显著的性能提升，具体数据表明最坏情况性能界限得到了有效改善，尽管计算时间有所增加。

## 🎯 应用场景

该研究的潜在应用领域包括无人机控制、自动驾驶车辆、工业机器人等需要实时决策和适应性控制的系统。通过引入更新感知的鲁棒控制策略，可以显著提高系统在不确定环境下的性能和安全性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Robust optimal or min-max model predictive control (MPC) approaches aim to guarantee constraint satisfaction over a known, bounded uncertainty set while minimizing a worst-case performance bound. Traditionally, these methods compute a trajectory that meets the desired properties over a fixed prediction horizon, apply a portion of the resulting input, and then re-solve the MPC problem using newly obtained measurements at the next time step. However, this approach fails to account for the fact that the control trajectory will be updated in the future, potentially leading to conservative designs. In this paper, we present a novel update-aware robust optimal MPC algorithm for decreasing horizon problems on nonlinear systems that explicitly accounts for future control trajectory updates. This additional insight allows our method to provably expand the feasible solution set and guarantee improved worst-case performance bounds compared to existing techniques. Our approach formulates the trajectory generation problem as a sequence of nested existence-constrained semi-infinite programs (SIPs), which can be efficiently solved using local reduction techniques. To demonstrate its effectiveness, we evaluate our approach on a planar quadrotor problem, where it clearly outperforms an equivalent method that does not account for future updates at the cost of increased computation time.

