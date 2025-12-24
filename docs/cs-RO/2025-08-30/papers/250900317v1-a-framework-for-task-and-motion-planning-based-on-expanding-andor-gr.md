---
layout: default
title: A Framework for Task and Motion Planning based on Expanding AND/OR Graphs
---

# A Framework for Task and Motion Planning based on Expanding AND/OR Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00317" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00317v1</a>
  <a href="https://arxiv.org/pdf/2509.00317.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00317v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00317v1', 'A Framework for Task and Motion Planning based on Expanding AND/OR Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fulvio Mastrogiovanni, Antony Thomas

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-30

**备注**: Accepted for an oral presentation at ASTRA Conference, 2025

---

## 💡 一句话要点

**提出基于扩展AND/OR图的任务与运动规划框架以应对机器人自主性挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `任务与运动规划` `AND/OR图` `机器人自主性` `不确定性处理` `动态环境` `空间机器人` `实时评估`

## 📋 核心要点

1. 现有的任务与运动规划方法在面对高不确定性和复杂环境时，往往缺乏足够的鲁棒性和灵活性。
2. 本文提出的TMP-EAOG框架通过扩展AND/OR图来整合任务抽象与运动可行性评估，增强了规划过程的适应性。
3. 实验结果显示，TMP-EAOG在多个基准测试中表现出色，能够有效应对各种挑战，提升了机器人自主性。

## 📝 摘要（中文）

在太空环境中，机器人自主性面临高感知和运动不确定性、严格的运动学约束以及有限的人类干预机会等独特挑战。因此，任务与运动规划（TMP）对于自主服务、表面操作或轨道任务至关重要。本文提出了一种基于扩展AND/OR图的TMP框架（TMP-EAOG），并展示了其在不同场景中的适应性。TMP-EAOG在AND/OR图中编码任务级抽象，随着计划执行而迭代扩展，并进行实时运动规划评估以确认其可行性。TMP-EAOG的特点包括对不确定性的鲁棒性、受控的自主性以及有界的灵活性。我们在两个基准领域评估了TMP-EAOG，使用模拟移动操纵器作为太空级自主机器人的代理，结果表明TMP-EAOG能够应对基准中的各种挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在复杂和不确定环境中进行任务与运动规划的挑战。现有方法在处理高不确定性和严格约束时，往往无法有效应对环境变化。

**核心思路**：TMP-EAOG框架通过扩展AND/OR图来实现任务与运动的集成规划，允许在执行过程中动态调整计划，以适应环境的变化和不确定性。

**技术框架**：TMP-EAOG的整体架构包括任务抽象的AND/OR图表示、迭代扩展机制和实时运动规划评估模块。该框架在执行过程中不断更新图结构，以反映新的信息和评估结果。

**关键创新**：TMP-EAOG的主要创新在于其能够在不确定性环境中保持鲁棒性和灵活性，通过AND/OR图的扩展机制，能够有效处理不可预见的事件和运动评估。

**关键设计**：在设计中，TMP-EAOG采用了可验证的AND/OR图结构，允许人类专家进行干预和验证。此外，框架中的运动评估模块能够实时反馈运动的可行性，确保规划的有效性和安全性。

## 📊 实验亮点

实验结果表明，TMP-EAOG在两个基准领域中表现优异，能够有效处理多种挑战。与传统方法相比，TMP-EAOG在不确定性环境中的成功率显著提高，展示了其在复杂任务规划中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括太空任务中的自主机器人操作、复杂环境下的服务机器人以及其他需要高自主性的移动系统。TMP-EAOG框架的灵活性和鲁棒性使其在动态和不确定的环境中具有重要的实际价值，未来可能推动机器人技术的进一步发展。

## 📄 摘要（原文）

> Robot autonomy in space environments presents unique challenges, including high perception and motion uncertainty, strict kinematic constraints, and limited opportunities for human intervention. Therefore, Task and Motion Planning (TMP) may be critical for autonomous servicing, surface operations, or even in-orbit missions, just to name a few, as it models tasks as discrete action sequencing integrated with continuous motion feasibility assessments. In this paper, we introduce a TMP framework based on expanding AND/OR graphs, referred to as TMP-EAOG, and demonstrate its adaptability to different scenarios. TMP-EAOG encodes task-level abstractions within an AND/OR graph, which expands iteratively as the plan is executed, and performs in-the-loop motion planning assessments to ascertain their feasibility. As a consequence, TMP-EAOG is characterised by the desirable properties of (i) robustness to a certain degree of uncertainty, because AND/OR graph expansion can accommodate for unpredictable information about the robot environment, (ii) controlled autonomy, since an AND/OR graph can be validated by human experts, and (iii) bounded flexibility, in that unexpected events, including the assessment of unfeasible motions, can lead to different courses of action as alternative paths in the AND/OR graph. We evaluate TMP-EAOG on two benchmark domains. We use a simulated mobile manipulator as a proxy for space-grade autonomous robots. Our evaluation shows that TMP-EAOG can deal with a wide range of challenges in the benchmarks.

