---
layout: default
title: Unidirectional-Road-Network-Based Global Path Planning for Cleaning Robots in Semi-Structured Environments
---

# Unidirectional-Road-Network-Based Global Path Planning for Cleaning Robots in Semi-Structured Environments

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.13048" target="_blank" class="toolbar-btn">arXiv: 2511.13048v1</a>
    <a href="https://arxiv.org/pdf/2511.13048.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13048v1" 
            onclick="toggleFavorite(this, '2511.13048v1', 'Unidirectional-Road-Network-Based Global Path Planning for Cleaning Robots in Semi-Structured Environments')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yong Li, Hui Cheng

**分类**: cs.RO

**发布日期**: 2025-11-17

**备注**: 2023 IEEE International Conference on Robotics and Automation (ICRA)

**DOI**: [10.1109/ICRA48891.2023.10161557](https://doi.org/10.1109/ICRA48891.2023.10161557)

---

## 💡 一句话要点

**提出基于单向道路网络的全局路径规划方法，提升半结构化环境中清洁机器人的导航效率。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `全局路径规划` `清洁机器人` `半结构化环境` `单向道路网络` `双层势场图`

## 📋 核心要点

1. 现有全局路径规划方法通常忽略环境的交通规则约束，导致频繁的重规划和碰撞风险。
2. 该方法构建单向道路网络表示交通约束，并采用混合策略，允许起始点和目标点横穿道路以缩短路径。
3. 实验结果表明，该方法在路径长度和与道路网络一致性之间实现了更好的平衡，提升了导航效率。

## 📝 摘要（中文）

本文提出了一种通用的系统方法，旨在提升半结构化环境中清洁机器人的全局路径规划性能。该方法构建了一个单向道路网络来表示环境中的交通规则约束，并提出了一种混合策略以保证规划结果。允许起始点和目标点横穿道路，以实现更短的路径。特别地，提出了一种双层势场图，以保证起始点和目标点位于复杂交叉口时的性能。对比实验验证了所提出方法的有效性。定量实验结果表明，与现有技术相比，该方法在路径长度和与道路网络的一致性之间取得了更好的平衡。

## 🔬 方法详解

**问题定义**：现有全局路径规划方法在半结构化环境中面临挑战。针对自由空间的规划方法忽略了交通规则约束，导致清洁机器人频繁重规划和碰撞风险。而严格遵守道路网络的规划方法可能导致路径过长，降低导航效率。因此，需要在路径长度和遵守交通规则之间找到平衡。

**核心思路**：本文的核心思路是构建一个单向道路网络来表示半结构化环境中的交通规则约束。通过允许起始点和目标点横穿道路，可以在保证一定程度的交通规则遵守的前提下，缩短路径长度。此外，针对复杂交叉口，设计了双层势场图来保证规划性能。

**技术框架**：该方法包含以下几个主要阶段：1) 构建单向道路网络，该网络表示了环境中的交通规则约束。2) 采用混合策略进行路径规划，该策略允许起始点和目标点横穿道路，以缩短路径。3) 在复杂交叉口，使用双层势场图来引导路径规划，保证规划性能。

**关键创新**：该方法的主要创新点在于：1) 提出了单向道路网络的概念，用于表示半结构化环境中的交通规则约束。2) 提出了混合策略，允许起始点和目标点横穿道路，在路径长度和交通规则遵守之间取得平衡。3) 提出了双层势场图，用于解决复杂交叉口的路径规划问题。

**关键设计**：双层势场图的设计是关键。第一层势场图用于引导机器人朝向目标点移动，第二层势场图用于避免碰撞。具体参数设置（例如势场强度、衰减系数等）需要根据实际环境进行调整。混合策略中，横穿道路的代价需要仔细权衡，以避免过度横穿导致违反交通规则。

## 📊 实验亮点

实验结果表明，与现有技术相比，该方法在路径长度和与道路网络的一致性之间取得了更好的平衡。定量结果显示，在保证路径与道路网络一致性的前提下，路径长度显著缩短，从而提升了清洁机器人的整体导航效率。具体提升幅度未知，需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于清洁机器人、物流机器人等需要在半结构化环境中进行导航的场景。通过平衡路径长度和交通规则遵守，可以提高机器人的导航效率和安全性，降低人工干预的需求，具有重要的实际应用价值和商业前景。未来可进一步扩展到更复杂的环境和任务中。

## 📄 摘要（原文）

> Practical global path planning is critical for commercializing cleaning robots working in semi-structured environments. In the literature, global path planning methods for free space usually focus on path length and neglect the traffic rule constraints of the environments, which leads to high-frequency re-planning and increases collision risks. In contrast, those for structured environments are developed mainly by strictly complying with the road network representing the traffic rule constraints, which may result in an overlong path that hinders the overall navigation efficiency. This article proposes a general and systematic approach to improve global path planning performance in semi-structured environments. A unidirectional road network is built to represent the traffic constraints in semi-structured environments and a hybrid strategy is proposed to achieve a guaranteed planning result.Cutting across the road at the starting and the goal points are allowed to achieve a shorter path. Especially, a two-layer potential map is proposed to achieve a guaranteed performance when the starting and the goal points are in complex intersections. Comparative experiments are carried out to validate the effectiveness of the proposed method. Quantitative experimental results show that, compared with the state-of-art, the proposed method guarantees a much better balance between path length and the consistency with the road network.

