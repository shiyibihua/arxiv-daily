---
layout: default
title: A Hierarchical Signal Coordination and Control System Using a Hybrid Model-based and Reinforcement Learning Approach
---

# A Hierarchical Signal Coordination and Control System Using a Hybrid Model-based and Reinforcement Learning Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20102" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20102v1</a>
  <a href="https://arxiv.org/pdf/2508.20102.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20102v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20102v1', 'A Hierarchical Signal Coordination and Control System Using a Hybrid Model-based and Reinforcement Learning Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianyue Peng, Shenyang Chen, H. Michael Zhang

**分类**: eess.SY, cs.AI

**发布日期**: 2025-08-12

**备注**: 28 pages, 7 figures

---

## 💡 一句话要点

**提出一种混合模型与强化学习的分层信号协调控制系统**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `交通信号控制` `强化学习` `模型优化` `自适应策略` `城市交通管理` `分层设计` `智能交通系统`

## 📋 核心要点

1. 核心问题：现有城市交通信号控制方法难以同时满足主干道流量与局部交叉口需求的动态变化。
2. 方法要点：提出的方案结合了模型优化与强化学习，通过分层结构实现动态协调策略选择。
3. 实验或效果：实验结果显示，混合MFC在高需求下表现最佳，而PAC在中等需求下提升了网络整体出行时间。

## 📝 摘要（中文）

城市走廊的信号控制面临保持主干交通流畅与适应局部交叉口需求变化的双重挑战。本文提出了一种分层交通信号协调与控制方案，结合了基于模型的优化与强化学习。该系统包括高层协调器（HLC）、走廊协调器和混合信号代理（HSA），通过强化学习与动作屏蔽来确定信号相位。实验结果表明，混合最大流协调（MFC）在高需求下最大化通行能力，而混合绿色波浪协调（GWC）在多种交通条件下有效减少主干停靠次数，但可能降低网络整体效率。

## 🔬 方法详解

**问题定义**：本文旨在解决城市走廊信号控制中，如何在保持主干交通流畅的同时，适应局部交叉口需求变化的问题。现有方法往往无法有效平衡这两者，导致交通效率低下。

**核心思路**：提出的分层信号协调与控制方案，结合了基于模型的优化与强化学习，利用高层协调器动态选择协调策略，以适应不同的交通需求。

**技术框架**：系统由三个主要模块组成：高层协调器（HLC）负责选择协调策略，走廊协调器根据所选策略生成相位约束，混合信号代理（HSA）通过强化学习确定信号相位。HLC与HSA的训练采用近端策略优化（PPO）算法。

**关键创新**：最重要的创新在于将强化学习与传统的信号控制方法相结合，通过分层设计实现了自适应策略选择，显著提升了系统在不同需求水平下的鲁棒性。

**关键设计**：在HSA的训练中，设计了三种策略：MFC感知、GWC感知和纯代理控制（PAC），并通过多目标奖励机制平衡走廊级和网络级的性能。

## 📊 实验亮点

实验结果表明，混合MFC在高需求情况下最大化了通行能力，而混合GWC在多种交通条件下有效减少了主干停靠次数。PAC策略在中等需求下显著提升了网络整体出行时间，展示了该方法的灵活性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括城市交通管理、智能交通系统和自动驾驶车辆的信号控制。通过提高交通信号控制的效率和适应性，能够有效缓解城市交通拥堵，提高出行效率，具有重要的社会和经济价值。

## 📄 摘要（原文）

> Signal control in urban corridors faces the dual challenge of maintaining arterial traffic progression while adapting to demand variations at local intersections. We propose a hierarchical traffic signal coordination and control scheme that integrates model-based optimization with reinforcement learning. The system consists of: (i) a High-Level Coordinator (HLC) that selects coordination strategies based on observed and predicted demand; (ii) a Corridor Coordinator that derives phase constraints from the selected strategy-either Max-Flow Coordination (MFC) or Green-Wave Coordination (GWC); and (iii) Hybrid Signal Agents (HSAs) that determine signal phases via reinforcement learning with action masking to enforce feasibility. Hierarchical reinforcement learning with Proximal Policy Optimization (PPO) is used to train HSA and HLC policies. At the lower level, three HSA policies-MFC-aware, GWC-aware, and pure agent control (PAC) are trained in conjunction with their respective coordination strategies. At the higher level, the HLC is trained to dynamically switch strategies using a multi-objective reward balancing corridor-level and network-wide performance. The proposed scheme was developed and evaluated on a SUMO-RLlib platform. Case results show that hybrid MFC maximizes throughput under heavy demand; hybrid GWC consistently minimizes arterial stops and maintains progression across diverse traffic conditions but can reduce network-wide efficiency; and PAC improves network-wide travel time in moderate demand but is less effective under heavy demand. The hierarchical design enables adaptive strategy selection, achieving robust performance across all demand levels.

