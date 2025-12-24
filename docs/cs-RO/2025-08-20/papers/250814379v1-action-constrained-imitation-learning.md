---
layout: default
title: Action-Constrained Imitation Learning
---

# Action-Constrained Imitation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14379" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14379v1</a>
  <a href="https://arxiv.org/pdf/2508.14379.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14379v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14379v1', 'Action-Constrained Imitation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chia-Han Yeh, Tse-Sheng Nan, Risto Vuorio, Wei Hung, Hung-Yen Wu, Shao-Hua Sun, Ping-Chun Hsieh

**分类**: cs.RO, cs.LG

**发布日期**: 2025-08-20

**备注**: Published in ICML 2025

**🔗 代码/项目**: [GITHUB](https://github.com/NYCU-RL-Bandits-Lab/ACRL-Baselines)

---

## 💡 一句话要点

**提出动作约束模仿学习以解决安全行为问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `动作约束` `模仿学习` `轨迹对齐` `动态时间规整` `模型预测控制` `机器人控制` `样本效率`

## 📋 核心要点

1. 核心问题：现有模仿学习方法在动作约束下，专家与模仿者之间的占用度量存在不匹配，导致学习效果不佳。
2. 方法要点：提出DTWIL，通过轨迹对齐和模型预测控制解决动作约束下的学习问题，生成符合约束的替代数据集。
3. 实验或效果：实验表明，DTWIL生成的数据集显著提高了多个机器人控制任务的性能，样本效率优于多种基准算法。

## 📝 摘要（中文）

在各种机器人控制和资源分配应用中，政策学习在确保安全行为方面起着核心作用。本文研究了一种新的问题设置，称为动作约束模仿学习（ACIL），其中一个受动作约束的模仿者旨在从具有更大动作空间的示范专家那里学习。ACIL的基本挑战在于，由于动作约束，专家与模仿者之间的占用度量不可避免地存在不匹配。我们通过轨迹对齐来解决这一不匹配，并提出了DTWIL，该方法用遵循相似状态轨迹的替代数据集替换原始专家演示，同时遵循动作约束。通过广泛的实验，我们证明了从DTWIL生成的数据集中学习显著提升了多个机器人控制任务的性能，并在样本效率方面超越了多种基准模仿学习算法。

## 🔬 方法详解

**问题定义**：本文要解决的问题是动作约束模仿学习（ACIL），即在动作空间受限的情况下，如何有效地从具有更大动作空间的专家学习。现有方法在处理这种不匹配时，往往无法有效利用专家的知识，导致学习效率低下。

**核心思路**：论文的核心思路是通过轨迹对齐来解决专家与模仿者之间的占用度量不匹配问题。具体而言，采用动态时间规整（DTW）方法，将专家的轨迹与符合动作约束的替代轨迹进行对齐，从而实现有效学习。

**技术框架**：整体架构包括两个主要模块：轨迹生成和轨迹对齐。首先，通过模型预测控制（MPC）生成符合动作约束的替代轨迹；然后，利用DTW算法对替代轨迹与专家轨迹进行对齐，确保学习过程中的信息传递。

**关键创新**：最重要的技术创新在于将轨迹对齐视为一个规划问题，通过MPC与DTW结合，解决了动作约束下的模仿学习难题。这一方法与传统的模仿学习方法相比，能够更好地处理动作空间的限制。

**关键设计**：在设计中，关键参数包括轨迹生成的时间步长、MPC的预测时域和DTW的距离度量方式。此外，损失函数的设计也考虑了轨迹对齐的精度，以确保生成的替代轨迹能够有效反映专家的行为。

## 📊 实验亮点

实验结果表明，使用DTWIL生成的数据集在多个机器人控制任务中显著提高了性能，样本效率提升幅度超过了传统模仿学习算法，具体性能数据未详细披露，但相较于基准算法表现出明显优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、资源分配等场景，能够有效提升系统在复杂环境中的安全性与效率。未来，随着技术的不断发展，ACIL方法有望在更多实际应用中发挥重要作用，推动智能系统的安全性与可靠性。

## 📄 摘要（原文）

> Policy learning under action constraints plays a central role in ensuring safe behaviors in various robot control and resource allocation applications. In this paper, we study a new problem setting termed Action-Constrained Imitation Learning (ACIL), where an action-constrained imitator aims to learn from a demonstrative expert with larger action space. The fundamental challenge of ACIL lies in the unavoidable mismatch of occupancy measure between the expert and the imitator caused by the action constraints. We tackle this mismatch through \textit{trajectory alignment} and propose DTWIL, which replaces the original expert demonstrations with a surrogate dataset that follows similar state trajectories while adhering to the action constraints. Specifically, we recast trajectory alignment as a planning problem and solve it via Model Predictive Control, which aligns the surrogate trajectories with the expert trajectories based on the Dynamic Time Warping (DTW) distance. Through extensive experiments, we demonstrate that learning from the dataset generated by DTWIL significantly enhances performance across multiple robot control tasks and outperforms various benchmark imitation learning algorithms in terms of sample efficiency. Our code is publicly available at https://github.com/NYCU-RL-Bandits-Lab/ACRL-Baselines.

