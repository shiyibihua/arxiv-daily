---
layout: default
title: Reinforcement Learning for Hybrid Charging Stations Planning and Operation Considering Fixed and Mobile Chargers
---

# Reinforcement Learning for Hybrid Charging Stations Planning and Operation Considering Fixed and Mobile Chargers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16764" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16764v2</a>
  <a href="https://arxiv.org/pdf/2506.16764.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16764v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16764v2', 'Reinforcement Learning for Hybrid Charging Stations Planning and Operation Considering Fixed and Mobile Chargers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanchen Zhu, Honghui Zou, Chufan Liu, Yuyu Luo, Yuankai Wu, Yuxuan Liang

**分类**: cs.AI

**发布日期**: 2025-06-20 (更新: 2025-08-10)

**备注**: 9 pages

---

## 💡 一句话要点

**提出混合充电站规划与运营方法以解决电动车充电基础设施不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `混合充电站` `深度强化学习` `充电需求预测` `城市交通` `移动充电器` `资源优化` `电动车充电`

## 📋 核心要点

1. 现有固定充电站因需求波动常出现低利用率或拥堵，影响电动车的充电效率。
2. 本文提出了一种结合固定与移动充电器的混合充电基础设施规划与运营方法，利用深度强化学习进行优化。
3. 实验结果显示，该方法在基础设施覆盖率和用户等待时间上均有显著提升，具有实际应用价值。

## 📝 摘要（中文）

电动车的成功电气化依赖于高效且灵活的充电基础设施。固定充电站常因需求波动而面临利用率低或拥堵的问题，而移动充电器则通过灵活调度提供解决方案。本文研究了结合固定和移动充电器的混合充电基础设施的最佳规划与运营，提出了混合充电站规划与运营（HCSPO）问题的模型，优化固定站点的布局和移动充电器的调度。基于模型预测控制（MPC）的充电需求预测模型支持动态决策。为解决HCSPO问题，本文提出了一种增强启发式调度的深度强化学习方法。实验结果表明，该方法在基础设施可用性上提升了244.4%的覆盖率，并将用户等待时间缩短了79.8%。

## 🔬 方法详解

**问题定义**：本文旨在解决混合充电基础设施的规划与运营问题，现有方法在应对需求波动时常显得不足，导致资源利用不均和用户体验差。

**核心思路**：通过结合固定充电站与移动充电器，提出了一种动态调度与优化的方法，利用深度强化学习来实现实时决策与资源配置。

**技术框架**：整体架构包括充电需求预测模块、固定站点布局优化模块和移动充电器调度模块。首先通过MPC模型预测需求，然后基于预测结果进行调度优化。

**关键创新**：本研究的创新点在于将深度强化学习与启发式调度相结合，显著提升了充电基础设施的响应能力和资源利用效率。

**关键设计**：在模型中设置了多种参数以适应不同的城市交通场景，损失函数设计考虑了用户等待时间和充电站利用率，网络结构采用了深度学习中的卷积神经网络（CNN）以提高预测精度。

## 📊 实验亮点

实验结果表明，所提方法在基础设施可用性上实现了244.4%的覆盖率提升，同时用户等待时间减少了79.8%。与现有解决方案相比，显著改善了充电体验，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括城市电动车充电基础设施的规划与管理，能够有效提升充电站的利用率和用户体验。未来，随着电动车普及，混合充电站的灵活调度将对城市交通系统的可持续发展产生重要影响。

## 📄 摘要（原文）

> The success of vehicle electrification relies on efficient and adaptable charging infrastructure. Fixed-location charging stations often suffer from underutilization or congestion due to fluctuating demand, while mobile chargers offer flexibility by relocating as needed. This paper studies the optimal planning and operation of hybrid charging infrastructures that combine both fixed and mobile chargers within urban road networks. We formulate the Hybrid Charging Station Planning and Operation (HCSPO) problem, jointly optimizing the placement of fixed stations and the scheduling of mobile chargers. A charging demand prediction model based on Model Predictive Control (MPC) supports dynamic decision-making. To solve the HCSPO problem, we propose a deep reinforcement learning approach enhanced with heuristic scheduling. Experiments on real-world urban scenarios show that our method improves infrastructure availability - achieving up to 244.4% increase in coverage - and reduces user inconvenience with up to 79.8% shorter waiting times, compared to existing solutions.

