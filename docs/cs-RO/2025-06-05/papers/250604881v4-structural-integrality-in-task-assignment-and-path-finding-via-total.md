---
layout: default
title: Structural Integrality in Task Assignment and Path Finding via Total Unimodularity of Petri Net Models
---

# Structural Integrality in Task Assignment and Path Finding via Total Unimodularity of Petri Net Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04881" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04881v4</a>
  <a href="https://arxiv.org/pdf/2506.04881.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04881v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04881v4', 'Structural Integrality in Task Assignment and Path Finding via Total Unimodularity of Petri Net Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ioana Hustiu, Roozbeh Abolpour, Marius Kloetzer, Cristian Mahulea

**分类**: cs.RO, eess.SY

**发布日期**: 2025-06-05 (更新: 2025-12-20)

---

## 💡 一句话要点

**提出基于Petri网的优化框架以解决多机器人任务分配与路径规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多机器人系统` `任务分配` `路径规划` `Petri网` `优化算法` `线性规划` `混合整数规划`

## 📋 核心要点

1. 现有的优化方法通常依赖于时间扩展的网络流模型，导致混合整数规划规模庞大，难以扩展。
2. 本文提出了一种基于Petri网的优化框架，利用运动模型的结构特性，避免显式的时间扩展，从而提高计算效率。
3. 在大规模基准测试中，实验结果显示该方法在可扩展性上显著优于传统的时间扩展优化基线。

## 📝 摘要（中文）

任务分配与路径规划（TAPF）涉及为多个机器人计算无碰撞的运动，同时选择目标位置。本文通过要求单位容量的遍历来确保安全性，提出了一种基于Petri网的优化框架，利用运动模型的结构特性提高计算效率，避免了时间扩展带来的大规模混合整数规划问题。我们证明了在固定拥堵水平下，运动规划约束矩阵是完全单调的，从而使得相应的线性规划松弛能够获得整数最优解。通过引入基于中间标记的按需同步机制，保持了运动变量的整数性。最后，扩展了TAPF至布尔规范，并提出了两阶段的线性规划/混合整数线性规划方案，实验结果显示在大规模基准测试中显著提升了可扩展性。

## 🔬 方法详解

**问题定义**：本文旨在解决多机器人任务分配与路径规划中的无碰撞运动计算问题。现有方法依赖于时间扩展的网络流模型，导致计算复杂度高，难以处理大规模场景。

**核心思路**：论文提出了一种基于Petri网的优化框架，利用运动模型的结构特性，避免时间扩展，从而提高计算效率。通过固定拥堵水平，确保运动规划约束矩阵的完全单调性，进而获得整数最优解。

**技术框架**：整体架构包括任务分配、路径规划和同步机制三个主要模块。首先，通过Petri网建模机器人运动，然后在固定拥堵水平下求解运动规划约束，最后引入按需同步机制以处理拥堵情况。

**关键创新**：最重要的技术创新在于证明了在固定拥堵水平下，运动规划约束矩阵是完全单调的，这一性质使得线性规划松弛能够获得整数解，显著提高了计算效率。

**关键设计**：关键设计包括固定拥堵水平的选择、同步阶段的数量设置，以及中间标记的使用，这些设计确保了约束矩阵的完全单调性，从而保持了运动变量的整数性。

## 📊 实验亮点

实验结果表明，所提出的方法在大规模基准测试中，相较于传统的时间扩展优化基线，计算效率提升了显著，具体性能数据展示了在处理复杂场景时的优越性，验证了方法的可扩展性。

## 🎯 应用场景

该研究的潜在应用领域包括多机器人系统的协调控制、自动化仓储、智能制造等场景。通过提高任务分配与路径规划的效率，能够显著提升机器人在复杂环境中的协作能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Task Assignment and Path Finding (TAPF) concerns computing collision-free motions for multiple robots while jointly selecting goal locations. In this paper, safety is enforced by requiring unit-capacity traversal between successive intermediate markings, yielding coordination strategies that are valid independently of any specific time interpretation. Existing optimization-based approaches typically rely on time-expanded network-flow models, which result in large mixed-integer programs and limited scalability. We instead develop a Petri net (PN)-based optimization framework that exploits structural properties of the motion model to improve computational efficiency without explicit time expansion.
>   When robot motion is modeled by strongly connected state-machine PNs, we show that, once the congestion level (equivalently, the synchronization depth) is fixed to an integer value, the resulting motion-planning constraint matrix is totally unimodular. Consequently, the corresponding LP relaxation admits integral optimal solutions for the motion variables. When the estimated congestion exceeds one, we introduce a synchronization-on-demand mechanism based on intermediate markings; for a fixed number of synchronization stages, the associated constraint matrices remain totally unimodular, thereby preserving integrality of the motion variables.
>   Finally, we extend TAPF to Boolean specifications over regions of interest and propose a two-stage LP/mixed-integer linear programming (MILP) scheme in which integrality is confined to task-selection variables. Simulations on large benchmarks demonstrate substantial scalability improvements over time-expanded optimization baselines.

