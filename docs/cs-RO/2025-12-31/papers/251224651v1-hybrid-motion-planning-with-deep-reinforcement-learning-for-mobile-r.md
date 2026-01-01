---
layout: default
title: Hybrid Motion Planning with Deep Reinforcement Learning for Mobile Robot Navigation
---

# Hybrid Motion Planning with Deep Reinforcement Learning for Mobile Robot Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24651" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24651v1</a>
  <a href="https://arxiv.org/pdf/2512.24651.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24651v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24651v1', 'Hybrid Motion Planning with Deep Reinforcement Learning for Mobile Robot Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yury Kolomeytsev, Dmitry Golembiovsky

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-12-31

**备注**: 22 pages, 4 figures

---

## 💡 一句话要点

**提出HMP-DRL混合运动规划，提升移动机器人在复杂动态环境中的导航能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `移动机器人导航` `深度强化学习` `混合运动规划` `全局路径规划` `局部避障` `动态环境` `人机交互` `社交合规性`

## 📋 核心要点

1. 传统图搜索规划器缺乏对动态环境的反应性，而深度强化学习方法缺乏全局路径规划能力，导致导航效率和安全性不足。
2. HMP-DRL框架融合了图搜索全局规划和深度强化学习局部控制，利用全局路径点引导局部策略，实现长期规划和短期反应的结合。
3. 实验结果表明，HMP-DRL在成功率、碰撞率和到达目标时间等指标上优于现有方法，提升了复杂环境下的导航性能。

## 📝 摘要（中文）

本文提出了一种混合运动规划与深度强化学习(HMP-DRL)框架，旨在解决移动机器人在复杂动态环境中导航的问题。传统图搜索规划器擅长长距离路径规划，但缺乏反应性；深度强化学习(DRL)方法在避障方面表现出色，但由于缺乏全局上下文信息，难以到达远距离目标。HMP-DRL框架结合了图搜索全局规划器和局部DRL策略，通过将全局路径上的检查点编码到状态空间和奖励函数中，实现二者的有效集成。为了确保社交合规性，局部规划器采用了一种实体感知的奖励结构，该结构根据周围智能体的语义类型动态调整安全边际和惩罚。在基于真实地图数据的仿真环境中进行的大量实验表明，HMP-DRL在成功率、碰撞率和到达目标时间等关键指标上始终优于其他方法，包括最先进的方法。研究结果表明，将长期路径引导与语义感知的局部控制相结合，可以显著提高自主导航在复杂人机交互环境中的安全性和可靠性。

## 🔬 方法详解

**问题定义**：移动机器人在复杂动态环境中导航，需要兼顾长距离路径规划和局部避障。传统图搜索规划器难以应对动态障碍物，而深度强化学习方法缺乏全局视野，容易陷入局部最优，导致导航效率低下和安全性不足。

**核心思路**：将图搜索全局规划器提供的长距离路径信息融入到深度强化学习的局部控制策略中，利用全局路径点引导局部策略的学习，从而实现长期规划和短期反应的有效结合。通过实体感知的奖励函数，使机器人能够根据周围环境中的智能体类型调整行为，提高社交合规性。

**技术框架**：HMP-DRL框架包含两个主要模块：全局规划器和局部DRL策略。全局规划器使用图搜索算法生成从起点到目标点的全局路径。然后，将全局路径上的关键点（检查点）编码到局部DRL策略的状态空间和奖励函数中。局部DRL策略根据当前状态（包括机器人自身状态、周围环境信息和全局路径点信息）选择动作，并根据奖励函数进行学习。

**关键创新**：HMP-DRL的关键创新在于将全局路径信息有效地融入到局部DRL策略中。通过将全局路径点编码到状态空间和奖励函数中，局部策略能够感知到全局目标，避免陷入局部最优。此外，实体感知的奖励函数能够使机器人根据周围环境中的智能体类型调整行为，提高社交合规性。

**关键设计**：奖励函数的设计是HMP-DRL的关键。奖励函数包含多个部分，包括到达目标点的奖励、避开障碍物的惩罚、与周围智能体保持安全距离的奖励以及偏离全局路径的惩罚。实体感知的奖励函数根据周围智能体的类型动态调整安全距离和惩罚力度。具体的网络结构和参数设置在论文中未明确给出，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24651v1/figures/map1_v2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24651v1/figures/checkpoints.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24651v1/figures/map_example.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，HMP-DRL在成功率、碰撞率和到达目标时间等关键指标上始终优于其他方法，包括最先进的方法。具体性能数据和提升幅度在摘要中提及，但在论文信息中未给出具体数值，属于未知信息。

## 🎯 应用场景

该研究成果可应用于各种需要在复杂动态环境中进行自主导航的移动机器人，例如服务机器人、物流机器人、自动驾驶汽车等。通过提高导航的安全性和效率，可以降低运营成本，提升用户体验，并促进相关产业的发展。

## 📄 摘要（原文）

> Autonomous mobile robots operating in complex, dynamic environments face the dual challenge of navigating large-scale, structurally diverse spaces with static obstacles while safely interacting with various moving agents. Traditional graph-based planners excel at long-range pathfinding but lack reactivity, while Deep Reinforcement Learning (DRL) methods demonstrate strong collision avoidance but often fail to reach distant goals due to a lack of global context. We propose Hybrid Motion Planning with Deep Reinforcement Learning (HMP-DRL), a hybrid framework that bridges this gap. Our approach utilizes a graph-based global planner to generate a path, which is integrated into a local DRL policy via a sequence of checkpoints encoded in both the state space and reward function. To ensure social compliance, the local planner employs an entity-aware reward structure that dynamically adjusts safety margins and penalties based on the semantic type of surrounding agents. We validate the proposed method through extensive testing in a realistic simulation environment derived from real-world map data. Comprehensive experiments demonstrate that HMP-DRL consistently outperforms other methods, including state-of-the-art approaches, in terms of key metrics of robot navigation: success rate, collision rate, and time to reach the goal. Overall, these findings confirm that integrating long-term path guidance with semantically-aware local control significantly enhances both the safety and reliability of autonomous navigation in complex human-centric settings.

