---
layout: default
title: Graph-Assisted Stitching for Offline Hierarchical Reinforcement Learning
---

# Graph-Assisted Stitching for Offline Hierarchical Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.07744" class="toolbar-btn" target="_blank">📄 arXiv: 2506.07744v3</a>
  <a href="https://arxiv.org/pdf/2506.07744.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.07744v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.07744v3', 'Graph-Assisted Stitching for Offline Hierarchical Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seungho Baek, Taegeon Park, Jongchan Park, Seungjun Oh, Yusung Kim

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-06-09 (更新: 2025-07-07)

**备注**: ICML 2025

**🔗 代码/项目**: [GITHUB](https://github.com/qortmdgh4141/GAS)

---

## 💡 一句话要点

**提出图辅助拼接方法以解决离线层次强化学习中的子目标选择问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `层次强化学习` `图搜索` `子目标选择` `状态转移拼接` `时间效率` `机器人导航` `智能制造`

## 📋 核心要点

1. 现有的离线层次强化学习方法在任务时间跨度增加时效率显著下降，且缺乏有效的状态转移拼接策略。
2. 本文提出的图辅助拼接（GAS）框架将子目标选择视为图搜索问题，通过聚类语义相似状态来实现高效拼接。
3. 在多个任务中，GAS的表现显著优于之前的离线HRL方法，尤其在拼接关键任务中取得了88.3的高分。

## 📝 摘要（中文）

现有的离线层次强化学习方法依赖于高层策略学习来生成子目标序列，但在任务时间跨度增加时效率下降，并且缺乏有效的策略来拼接不同轨迹中的有用状态转移。为此，本文提出了图辅助拼接（GAS）框架，将子目标选择问题形式化为图搜索问题，而不是学习显式的高层策略。通过将状态嵌入时间距离表示（TDR）空间，GAS将来自不同轨迹的语义相似状态聚类为统一的图节点，从而实现高效的转移拼接。随后，应用最短路径算法在图中选择子目标序列，同时低层策略学习到达这些子目标。引入时间效率（TE）指标以提高图的质量，显著提升任务性能。GAS在运动、导航和操作任务中超越了之前的离线HRL方法。

## 🔬 方法详解

**问题定义**：现有的离线层次强化学习方法依赖于高层策略生成子目标序列，导致在长时间任务中效率低下，且难以有效拼接不同轨迹中的状态转移。

**核心思路**：本文提出的GAS框架通过将子目标选择转化为图搜索问题，避免了显式高层策略的学习。通过将状态嵌入TDR空间，GAS能够将语义相似的状态聚类为统一的图节点，从而实现高效的状态转移拼接。

**技术框架**：GAS的整体架构包括状态嵌入、图节点聚类、最短路径算法选择子目标序列以及低层策略学习四个主要模块。首先，将状态嵌入TDR空间，然后聚类相似状态形成图节点，接着使用最短路径算法选择子目标，最后通过低层策略实现目标的达成。

**关键创新**：GAS的核心创新在于将子目标选择问题形式化为图搜索问题，并引入TE指标以过滤噪声状态，显著提升了图的质量和任务性能。这一方法与传统的高层策略学习方法本质上不同，提供了一种新的思路。

**关键设计**：在GAS中，TE指标用于评估状态转移的有效性，确保只保留高效的状态转移。此外，最短路径算法的选择和低层策略的设计也是关键技术细节，确保了整体框架的高效性和实用性。

## 📊 实验亮点

在实验中，GAS在运动、导航和操作任务上均超越了之前的离线HRL方法，尤其在拼接关键任务中取得了88.3的高分，显著高于之前的1.0的状态-of-the-art分数，展示了其卓越的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、自动驾驶、智能制造等场景，能够有效提升系统在复杂任务中的决策效率和性能。未来，GAS框架有望在更多实际应用中推广，推动离线层次强化学习的发展。

## 📄 摘要（原文）

> Existing offline hierarchical reinforcement learning methods rely on high-level policy learning to generate subgoal sequences. However, their efficiency degrades as task horizons increase, and they lack effective strategies for stitching useful state transitions across different trajectories. We propose Graph-Assisted Stitching (GAS), a novel framework that formulates subgoal selection as a graph search problem rather than learning an explicit high-level policy. By embedding states into a Temporal Distance Representation (TDR) space, GAS clusters semantically similar states from different trajectories into unified graph nodes, enabling efficient transition stitching. A shortest-path algorithm is then applied to select subgoal sequences within the graph, while a low-level policy learns to reach the subgoals. To improve graph quality, we introduce the Temporal Efficiency (TE) metric, which filters out noisy or inefficient transition states, significantly enhancing task performance. GAS outperforms prior offline HRL methods across locomotion, navigation, and manipulation tasks. Notably, in the most stitching-critical task, it achieves a score of 88.3, dramatically surpassing the previous state-of-the-art score of 1.0. Our source code is available at: https://github.com/qortmdgh4141/GAS.

