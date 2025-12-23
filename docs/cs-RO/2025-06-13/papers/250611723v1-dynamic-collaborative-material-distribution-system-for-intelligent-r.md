---
layout: default
title: Dynamic Collaborative Material Distribution System for Intelligent Robots In Smart Manufacturing
---

# Dynamic Collaborative Material Distribution System for Intelligent Robots In Smart Manufacturing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11723" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11723v1</a>
  <a href="https://arxiv.org/pdf/2506.11723.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11723v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11723v1', 'Dynamic Collaborative Material Distribution System for Intelligent Robots In Smart Manufacturing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziren Xiao, Ruxin Xiao, Chang Liu, Xinheng Wang

**分类**: cs.RO

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**提出轻量级深度强化学习方法以解决智能制造中的动态物料分配问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `多机器人协作` `智能制造` `动态导航` `物料分配` `实时决策` `计算效率`

## 📋 核心要点

1. 现有方法如枚举解法未能从历史经验中学习，导致在大地图上计算时间较长，难以实现实时操作。
2. 本文提出的轻量级深度强化学习方法通过设计目标导向的奖励函数，能够高效训练并快速收敛到最优解。
3. 实验结果表明，训练后的DRL模型在下一步移动的计算时间上可缩短至毫秒级，相较于枚举解法提升了100倍。

## 📝 摘要（中文）

多机器人协作与互动已成为智能制造的重要组成部分。有效的规划与管理在节能和降低整体成本方面至关重要。本文针对动态多源到单目的地导航问题，提出了一种轻量级的深度强化学习方法，能够高效训练并快速收敛到最优解。与现有方法相比，该方法显著减少了计算时间，提升了实时操作的可行性，并可在资源有限的设备上部署。

## 🔬 方法详解

**问题定义**：本文解决的是动态多源到单目的地导航问题，现有方法如枚举解法和有限信息利用的策略在大规模地图上计算效率低下，无法满足实时需求。

**核心思路**：提出了一种轻量级的深度强化学习方法，通过设计目标导向的奖励函数，能够快速学习并优化机器人在物料分配中的导航策略。

**技术框架**：整体架构包括数据收集模块、DRL训练模块和实时决策模块。数据收集模块负责收集历史轨迹信息，DRL训练模块用于训练模型，实时决策模块则根据训练好的模型进行即时导航决策。

**关键创新**：最重要的创新在于引入了目标导向的奖励函数，使得DRL模型能够更有效地学习导航策略，显著提升了计算效率，与传统方法相比，能够在更短的时间内找到最优解。

**关键设计**：在设计中，采用了轻量级网络结构以适应资源有限的设备，同时设置了适当的超参数以确保训练过程的稳定性和收敛速度。

## 📊 实验亮点

实验结果显示，训练后的深度强化学习模型在计算下一步移动时的时间缩短至毫秒级，相较于传统的枚举解法，计算效率提升了100倍，极大地增强了实时操作的可行性。

## 🎯 应用场景

该研究可广泛应用于智能制造领域，尤其是在物料分配、仓储管理和物流调度等场景中。通过提升多机器人协作的效率，能够显著降低运营成本，提高生产灵活性，未来可能推动智能制造的进一步发展。

## 📄 摘要（原文）

> The collaboration and interaction of multiple robots have become integral aspects of smart manufacturing. Effective planning and management play a crucial role in achieving energy savings and minimising overall costs. This paper addresses the real-time Dynamic Multiple Sources to Single Destination (DMS-SD) navigation problem, particularly with a material distribution case for multiple intelligent robots in smart manufacturing. Enumerated solutions, such as in \cite{xiao2022efficient}, tackle the problem by generating as many optimal or near-optimal solutions as possible but do not learn patterns from the previous experience, whereas the method in \cite{xiao2023collaborative} only uses limited information from the earlier trajectories. Consequently, these methods may take a considerable amount of time to compute results on large maps, rendering real-time operations impractical. To overcome this challenge, we propose a lightweight Deep Reinforcement Learning (DRL) method to address the DMS-SD problem. The proposed DRL method can be efficiently trained and rapidly converges to the optimal solution using the designed target-guided reward function. A well-trained DRL model significantly reduces the computation time for the next movement to a millisecond level, which improves the time up to 100 times in our experiments compared to the enumerated solutions. Moreover, the trained DRL model can be easily deployed on lightweight devices in smart manufacturing, such as Internet of Things devices and mobile phones, which only require limited computational resources.

