---
layout: default
title: Planning-Query-Guided Model Generation for Model-Based Deformable Object Manipulation
---

# Planning-Query-Guided Model Generation for Model-Based Deformable Object Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19199" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19199v1</a>
  <a href="https://arxiv.org/pdf/2508.19199.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19199v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19199v1', 'Planning-Query-Guided Model Generation for Model-Based Deformable Object Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alex LaGrassa, Zixuan Huang, Dmitry Berenson, Oliver Kroemer

**分类**: cs.RO, cs.LG

**发布日期**: 2025-08-26

**备注**: 9 pages, 7 figures

---

## 💡 一句话要点

**提出基于规划查询的模型生成方法以解决可变形物体操控问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `可变形物体` `动态模型` `空间自适应` `机器人操控` `规划查询` `效率提升` `闭环性能` `扩散模型`

## 📋 核心要点

1. 现有方法在处理可变形物体时，动态模型的表达能力与计算效率之间存在矛盾，难以满足高维空间的规划需求。
2. 本文提出了一种基于扩散模型的动态模型生成方法，通过学习物体区域的建模需求，实现任务特定的空间自适应建模。
3. 在树操控任务中，所提方法将规划速度提升至原来的两倍，且任务性能仅有轻微下降，显示出显著的效率提升。

## 📝 摘要（中文）

在高维空间中进行有效规划，尤其是涉及可变形物体时，需要计算上可行且足够表达的动态模型。本文提出了一种方法，通过学习物体的哪些区域需要高分辨率建模，自动生成任务特定的空间自适应动态模型。该方法基于扩散模型生成器，根据定义规划查询的起始和目标点云预测每个区域的模型分辨率。为了高效收集学习该映射的数据，采用两阶段过程，先使用预测动态作为先验优化分辨率，然后再通过闭环性能直接优化。在树操控任务中，该方法将规划速度提高了一倍，同时任务性能仅有小幅下降。此方法为利用先前的规划和控制数据生成计算高效且足够表达的动态模型指明了方向。

## 🔬 方法详解

**问题定义**：本文旨在解决在高维空间中进行可变形物体操控时，动态模型的计算效率与表达能力之间的矛盾。现有方法往往无法在保证模型精度的同时，满足实时规划的需求。

**核心思路**：论文的核心思路是通过学习物体不同区域的建模需求，自动生成适应特定任务的动态模型。该方法利用扩散模型生成器，根据规划查询的起始和目标点云，预测每个区域所需的模型分辨率。

**技术框架**：整体架构包括两个主要阶段：第一阶段使用预测动态作为先验，优化模型分辨率；第二阶段则通过闭环性能直接优化模型，以提高任务执行的效率和效果。

**关键创新**：最重要的技术创新在于提出了一种空间自适应的动态模型生成方法，能够根据任务需求动态调整模型分辨率。这与现有方法的静态建模方式形成了鲜明对比。

**关键设计**：在模型生成过程中，采用了特定的损失函数来平衡模型的分辨率与计算效率，同时设计了适应性强的网络结构，以便于在不同任务中灵活应用。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

在实验中，所提方法在树操控任务中将规划速度提高了100%，而任务性能仅有约5%的小幅下降。这一结果表明，所提出的动态模型生成方法在效率与性能之间实现了良好的平衡，具有显著的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操控、虚拟现实和增强现实等场景，尤其是在需要处理复杂物体交互的任务中。通过提高动态模型的生成效率，可以显著提升机器人在动态环境中的适应能力和操作精度，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Efficient planning in high-dimensional spaces, such as those involving deformable objects, requires computationally tractable yet sufficiently expressive dynamics models. This paper introduces a method that automatically generates task-specific, spatially adaptive dynamics models by learning which regions of the object require high-resolution modeling to achieve good task performance for a given planning query. Task performance depends on the complex interplay between the dynamics model, world dynamics, control, and task requirements. Our proposed diffusion-based model generator predicts per-region model resolutions based on start and goal pointclouds that define the planning query. To efficiently collect the data for learning this mapping, a two-stage process optimizes resolution using predictive dynamics as a prior before directly optimizing using closed-loop performance. On a tree-manipulation task, our method doubles planning speed with only a small decrease in task performance over using a full-resolution model. This approach informs a path towards using previous planning and control data to generate computationally efficient yet sufficiently expressive dynamics models for new tasks.

