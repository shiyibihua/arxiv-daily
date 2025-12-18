---
layout: default
title: Kinodynamic Motion Planning for Mobile Robot Navigation across Inconsistent World Models
---

# Kinodynamic Motion Planning for Mobile Robot Navigation across Inconsistent World Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26339" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26339v1</a>
  <a href="https://arxiv.org/pdf/2509.26339.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26339v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26339v1', 'Kinodynamic Motion Planning for Mobile Robot Navigation across Inconsistent World Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eric R. Damm, Thomas M. Howard

**分类**: cs.RO

**发布日期**: 2025-09-30

**备注**: Presented at the Robotics: Science and Systems (RSS) 2025 Workshop on Resilient Off-road Autonomous Robotics (ROAR)

---

## 💡 一句话要点

**针对不一致环境模型的移动机器人运动规划方法GEGRH**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `运动规划` `移动机器人` `环境不确定性` `自主导航` `代价地图` `路径规划` `机器人控制`

## 📋 核心要点

1. 现有移动机器人运动规划方法在环境感知不确定性下难以保证安全性，尤其是在代价地图频繁切换障碍物状态时。
2. 论文提出GEGRH方法，通过延迟子搜索和图修正，在多个历史世界模型中寻找安全且低成本的轨迹。
3. 实验表明，GEGRH在非结构化环境中比VEH方法规划时间更快，成本更低，且比单假设搜索更安全。

## 📝 摘要（中文）

移动地面机器人在缺乏环境先验知识的情况下，必须依赖传感器数据来构建周围环境模型。由于噪声和算法缺陷，障碍物和地形特征的稳定识别变得困难，这给运动规划系统生成安全运动轨迹带来了挑战。一个特别的难题是，代价地图中的区域在连续的规划周期中会在障碍物和自由空间之间切换。一种潜在的解决方案是“在每个假设中有效(VEH)”，即规划系统规划的运动必须保证在历史世界模型中都是安全的。另一种方法是跟踪世界模型的历史，并根据绕过先前危险区域的潜在代价来调整节点代价。本文讨论了该思路的三个主要迭代版本。第一个版本称为PEH，对每个穿过世界模型中发散点的节点扩展调用子搜索。第二和第三个版本分别称为GEH和GEGRH，将子搜索推迟到边缘扩展到目标区域之后。GEGRH使用额外的步骤来基于每个世界中的发散节点来修改图。初步结果表明，虽然PEH和GEH比VEH找到更乐观的解决方案，但它们无法在一秒钟内生成解决方案，这超出了我们对现场部署的要求。在Clearpath Robotics Warthog UGV上进行的非结构化越野环境的现场实验结果分析表明，GEGRH比VEH找到的轨迹成本更低，平均规划时间更快。与仅考虑最新世界模型的单假设(SH)搜索相比，GEGRH生成了更保守的计划，但平均规划时间略有增加。

## 🔬 方法详解

**问题定义**：移动机器人在未知或动态变化的环境中进行运动规划时，传感器噪声和算法局限性会导致环境模型的频繁变化，即代价地图中某些区域在不同时间步被标记为障碍物或自由空间。这使得传统的运动规划方法难以生成安全可靠的轨迹，因为它们可能基于过时的或不准确的环境信息进行规划。现有方法，如VEH，虽然保证了在所有历史模型中的安全性，但过于保守，可能导致规划失败或次优轨迹。

**核心思路**：GEGRH的核心思路是在保证安全性的前提下，尽可能地利用最新的环境信息，避免过于保守的规划。它通过延迟子搜索，即只有当边缘扩展到目标区域时才进行子搜索，来减少计算量。同时，通过图修正，根据每个世界模型中的发散节点来调整图结构，从而更好地适应环境的变化。

**技术框架**：GEGRH方法主要包含以下几个阶段：1) 使用最新的环境模型进行初始路径规划；2) 当边缘扩展到目标区域时，检查该边缘是否穿过不同世界模型中的发散点（即在不同模型中状态不同的区域）；3) 如果存在发散点，则进行子搜索，寻找在所有历史模型中都安全的替代路径；4) 根据每个世界模型中的发散节点，对图结构进行修正，调整节点之间的连接关系和代价。

**关键创新**：GEGRH的关键创新在于其延迟子搜索和图修正的策略。与PEH和GEH方法相比，GEGRH通过延迟子搜索减少了计算量，使其能够在更短的时间内生成解决方案。与VEH方法相比，GEGRH通过图修正更好地适应环境的变化，从而找到更低成本的轨迹。

**关键设计**：GEGRH的关键设计包括：1) 如何有效地检测发散点；2) 如何设计子搜索算法，以在所有历史模型中找到安全路径；3) 如何根据发散节点对图结构进行修正，例如，可以增加节点之间的连接代价，或者删除不安全的连接。论文中可能涉及具体的代价函数设计，用于评估轨迹的安全性、成本和时间。

## 📊 实验亮点

在Clearpath Robotics Warthog UGV上的非结构化越野环境实验表明，GEGRH方法比VEH方法能够找到成本更低的轨迹，并且平均规划时间更快。与单假设(SH)搜索相比，GEGRH方法虽然平均规划时间略有增加，但生成了更保守、更安全的计划，有效应对了环境感知的不确定性。

## 🎯 应用场景

该研究成果可应用于各种需要在复杂、动态或未知环境中进行自主导航的移动机器人，例如：无人驾驶车辆、仓储机器人、搜救机器人、农业机器人等。通过提高机器人在不确定环境下的导航安全性与效率，可以降低事故风险，提升作业效率，并扩展机器人的应用范围。

## 📄 摘要（原文）

> Mobile ground robots lacking prior knowledge of an environment must rely on sensor data to develop a model of their surroundings. In these scenarios, consistent identification of obstacles and terrain features can be difficult due to noise and algorithmic shortcomings, which can make it difficult for motion planning systems to generate safe motions. One particular difficulty to overcome is when regions of the cost map switch between being marked as obstacles and free space through successive planning cycles. One potential solution to this, which we refer to as Valid in Every Hypothesis (VEH), is for the planning system to plan motions that are guaranteed to be safe through a history of world models. Another approach is to track a history of world models, and adjust node costs according to the potential penalty of needing to reroute around previously hazardous areas. This work discusses three major iterations on this idea. The first iteration, called PEH, invokes a sub-search for every node expansion that crosses through a divergence point in the world models. The second and third iterations, called GEH and GEGRH respectively, defer the sub-search until after an edge expands into the goal region. GEGRH uses an additional step to revise the graph based on divergent nodes in each world. Initial results showed that, although PEH and GEH find more optimistic solutions than VEH, they are unable to generate solutions in less than one-second, which exceeds our requirements for field deployment. Analysis of results from a field experiment in an unstructured, off-road environment on a Clearpath Robotics Warthog UGV indicate that GEGRH finds lower cost trajectories and has faster average planning times than VEH. Compared to single-hypothesis (SH) search, where only the latest world model is considered, GEGRH generates more conservative plans with a small increase in average planning time.

