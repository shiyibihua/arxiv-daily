---
layout: default
title: Planning from Point Clouds over Continuous Actions for Multi-object Rearrangement
---

# Planning from Point Clouds over Continuous Actions for Multi-object Rearrangement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04645" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04645v1</a>
  <a href="https://arxiv.org/pdf/2509.04645.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04645v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04645v1', 'Planning from Point Clouds over Continuous Actions for Multi-object Rearrangement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kallol Saha, Amber Li, Angela Rodriguez-Izquierdo, Lifan Yu, Ben Eisner, Maxim Likhachev, David Held

**分类**: cs.RO

**发布日期**: 2025-09-04

**备注**: Conference on Robot Learning (CoRL) 2025 (https://planning-from-point-clouds.github.io/)

---

## 💡 一句话要点

**提出SPOT：一种基于点云变换搜索的多物体重排列规划方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作` `长时程规划` `点云处理` `多物体重排列` `混合学习与规划`

## 📋 核心要点

1. 长时程机器人操作规划面临着对一系列动作在3D场景中效果进行推理的挑战，传统方法需要离散化状态和动作空间。
2. 论文提出SPOT，一种混合学习与规划的方法，利用学习模型作为先验，指导在连续动作空间中搜索点云变换序列。
3. 实验表明，SPOT在多物体重排列任务中表现出色，优于策略学习方法，并验证了搜索规划的重要性。

## 📝 摘要（中文）

针对机器人操作中的长时程规划难题，该论文提出了一种混合学习与规划的方法，利用学习模型作为领域先验，指导高维连续动作空间中的搜索。论文引入了SPOT（Search over Point cloud Object Transformations），通过搜索从初始场景点云到满足目标状态的点云的变换序列来进行规划。SPOT从作用于部分观测点云的学习建议器中采样候选动作，无需离散化动作或对象关系。在多对象重排列任务中，论文评估了SPOT的任务规划成功率和任务执行成功率，包括仿真和真实环境。实验结果表明，SPOT能够生成成功的规划，并且优于策略学习方法。消融实验也突出了基于搜索的规划的重要性。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人操作中长时程、多物体重排列的规划问题。现有方法通常需要将连续的状态和动作空间离散化，转化为符号描述，这限制了其在复杂环境中的应用，并且难以处理高维连续动作空间。

**核心思路**：论文的核心思路是利用学习到的模型作为领域先验知识，指导在连续动作空间中进行搜索。通过学习动作建议器，直接在点云上进行操作，避免了离散化过程，从而能够处理更复杂的场景和动作。

**技术框架**：SPOT的整体框架包括以下几个主要模块：1) 点云观测模块：获取场景的初始点云和目标点云；2) 动作建议器：基于部分观测的点云，生成候选动作；3) 状态预测模块：预测执行动作后的场景点云；4) 搜索算法：在连续动作空间中搜索从初始状态到目标状态的动作序列。该框架通过迭代采样动作、预测状态和评估状态，最终找到满足目标的动作序列。

**关键创新**：最重要的技术创新点在于将学习和规划相结合，利用学习到的动作建议器来指导搜索过程。与传统的基于符号规划的方法不同，SPOT直接在点云上进行操作，避免了离散化过程，能够处理更复杂的场景和动作。此外，SPOT还采用了基于搜索的规划方法，能够有效地探索动作空间，找到满足目标的动作序列。

**关键设计**：动作建议器通常采用神经网络结构，输入为部分观测的点云，输出为候选动作的分布。状态预测模块可以使用物理引擎或学习模型来预测执行动作后的场景点云。搜索算法可以使用A*、RRT等算法，评估函数可以基于点云之间的距离或相似度来设计。

## 📊 实验亮点

实验结果表明，SPOT在多物体重排列任务中取得了显著的成功，在仿真和真实环境中均优于策略学习方法。具体而言，SPOT的任务规划成功率和任务执行成功率均高于对比方法，并且能够处理更复杂的场景。消融实验也验证了基于搜索的规划方法的重要性。

## 🎯 应用场景

该研究成果可应用于自动化仓库、家庭服务机器人、工业装配等领域。通过高效的物体重排列规划，可以提升物流效率、改善用户体验，并降低生产成本。未来，该技术有望扩展到更复杂的机器人操作任务，例如复杂环境下的物体抓取、操作和组装。

## 📄 摘要（原文）

> Long-horizon planning for robot manipulation is a challenging problem that requires reasoning about the effects of a sequence of actions on a physical 3D scene. While traditional task planning methods are shown to be effective for long-horizon manipulation, they require discretizing the continuous state and action space into symbolic descriptions of objects, object relationships, and actions. Instead, we propose a hybrid learning-and-planning approach that leverages learned models as domain-specific priors to guide search in high-dimensional continuous action spaces. We introduce SPOT: Search over Point cloud Object Transformations, which plans by searching for a sequence of transformations from an initial scene point cloud to a goal-satisfying point cloud. SPOT samples candidate actions from learned suggesters that operate on partially observed point clouds, eliminating the need to discretize actions or object relationships. We evaluate SPOT on multi-object rearrangement tasks, reporting task planning success and task execution success in both simulation and real-world environments. Our experiments show that SPOT generates successful plans and outperforms a policy-learning approach. We also perform ablations that highlight the importance of search-based planning.

