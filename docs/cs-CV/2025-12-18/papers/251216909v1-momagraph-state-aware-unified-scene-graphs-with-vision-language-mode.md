---
layout: default
title: MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Model for Embodied Task Planning
---

# MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Model for Embodied Task Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16909" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16909v1</a>
  <a href="https://arxiv.org/pdf/2512.16909.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16909v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16909v1', 'MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Model for Embodied Task Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanchen Ju, Yongyuan Liang, Yen-Jen Wang, Nandiraju Gireesh, Yuanliang Ju, Seungjae Lee, Qiao Gu, Elvis Hsieh, Furong Huang, Koushil Sreenath

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-18

**备注**: 25 pages, 10 figures. Project page:https://hybridrobotics.github.io/MomaGraph/

---

## 💡 一句话要点

**MomaGraph：面向具身任务规划，融合视觉-语言模型的、状态感知的统一场景图**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `场景图` `具身智能` `任务规划` `视觉-语言模型` `强化学习`

## 📋 核心要点

1. 现有场景图表示方法缺乏对物体状态和时序更新的考虑，且空间和功能关系分离，限制了具身智能体的任务规划能力。
2. MomaGraph通过统一的场景表示，整合空间-功能关系和部件级别的交互元素，从而更全面地描述场景。
3. MomaGraph-R1模型在MomaGraph数据集上训练，并在多个基准测试中取得了显著的性能提升，验证了其有效性。

## 📝 摘要（中文）

本文提出了MomaGraph，一种用于具身智能体的统一场景表示方法，它集成了空间-功能关系和部件级别的交互元素。现有场景图通常分离空间和功能关系，将场景视为静态快照，忽略了与当前任务最相关的信息。为了推进该表示方法，本文贡献了MomaGraph-Scenes，这是首个大规模的、带有丰富标注的、任务驱动的家庭环境场景图数据集，以及MomaGraph-Bench，一个涵盖从高层规划到细粒度场景理解的六种推理能力的系统评估套件。在此基础上，进一步开发了MomaGraph-R1，一个在MomaGraph-Scenes上通过强化学习训练的70亿参数视觉-语言模型。MomaGraph-R1预测面向任务的场景图，并在Graph-then-Plan框架下作为零样本任务规划器。大量实验表明，该模型在开源模型中取得了最先进的结果，在基准测试中达到了71.6%的准确率（比最佳基线高出11.4%），同时推广到公共基准测试，并有效地转移到真实机器人实验。

## 🔬 方法详解

**问题定义**：现有场景图表示方法主要存在三个痛点：一是空间和功能关系分离，无法有效支持复杂任务规划；二是将场景视为静态快照，忽略了物体状态和时序变化；三是缺乏针对具身任务的定制化信息，导致泛化能力不足。这些问题限制了移动操作机器人在家庭环境中的应用。

**核心思路**：MomaGraph的核心思路是构建一个统一的、状态感知的场景图表示，将空间关系、功能关系和物体状态整合在一起。通过引入部件级别的交互元素，MomaGraph能够更精细地描述场景，从而支持更复杂的任务规划。此外，通过视觉-语言模型进行训练，MomaGraph能够更好地理解场景中的语义信息。

**技术框架**：MomaGraph的整体框架包括数据收集与标注、模型训练和任务规划三个主要阶段。首先，构建MomaGraph-Scenes数据集，对家庭环境中的场景进行详细标注，包括物体的位置、功能和状态。然后，使用强化学习训练视觉-语言模型MomaGraph-R1，使其能够预测面向任务的场景图。最后，在Graph-then-Plan框架下，利用预测的场景图进行任务规划。

**关键创新**：MomaGraph的关键创新在于其统一的场景表示方法，它将空间关系、功能关系和物体状态整合在一起，从而更全面地描述场景。此外，MomaGraph-Scenes数据集的构建和MomaGraph-Bench评估套件的提出，为该领域的研究提供了重要的数据和评估标准。

**关键设计**：MomaGraph-R1模型是一个70亿参数的视觉-语言模型，采用Transformer架构。在训练过程中，使用了强化学习方法，以优化模型在任务规划方面的性能。损失函数包括场景图预测损失和任务规划奖励。具体参数设置和网络结构细节未在论文中详细描述，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16909v1/Figures/Teaser.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16909v1/Figures/Failure.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16909v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MomaGraph-R1模型在MomaGraph-Bench基准测试中取得了71.6%的准确率，比最佳基线高出11.4%。此外，该模型还成功地推广到公共基准测试，并有效地转移到真实机器人实验中，验证了其泛化能力和实用性。这些实验结果表明，MomaGraph是一种有效的场景表示方法，可以显著提高具身智能体的任务规划能力。

## 🎯 应用场景

MomaGraph在家庭服务机器人、自动驾驶、虚拟现实等领域具有广泛的应用前景。它可以帮助机器人更好地理解周围环境，从而执行更复杂的任务，例如物品整理、清洁和烹饪。此外，MomaGraph还可以用于构建更逼真的虚拟环境，为用户提供更沉浸式的体验。

## 📄 摘要（原文）

> Mobile manipulators in households must both navigate and manipulate. This requires a compact, semantically rich scene representation that captures where objects are, how they function, and which parts are actionable. Scene graphs are a natural choice, yet prior work often separates spatial and functional relations, treats scenes as static snapshots without object states or temporal updates, and overlooks information most relevant for accomplishing the current task. To address these limitations, we introduce MomaGraph, a unified scene representation for embodied agents that integrates spatial-functional relationships and part-level interactive elements. However, advancing such a representation requires both suitable data and rigorous evaluation, which have been largely missing. We thus contribute MomaGraph-Scenes, the first large-scale dataset of richly annotated, task-driven scene graphs in household environments, along with MomaGraph-Bench, a systematic evaluation suite spanning six reasoning capabilities from high-level planning to fine-grained scene understanding. Built upon this foundation, we further develop MomaGraph-R1, a 7B vision-language model trained with reinforcement learning on MomaGraph-Scenes. MomaGraph-R1 predicts task-oriented scene graphs and serves as a zero-shot task planner under a Graph-then-Plan framework. Extensive experiments demonstrate that our model achieves state-of-the-art results among open-source models, reaching 71.6% accuracy on the benchmark (+11.4% over the best baseline), while generalizing across public benchmarks and transferring effectively to real-robot experiments.

