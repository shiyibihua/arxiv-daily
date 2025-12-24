---
layout: default
title: Combined Stochastic and Robust Optimization for Electric Autonomous Mobility-on-Demand with Nested Benders Decomposition
---

# Combined Stochastic and Robust Optimization for Electric Autonomous Mobility-on-Demand with Nested Benders Decomposition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19933" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19933v2</a>
  <a href="https://arxiv.org/pdf/2508.19933.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19933v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19933v2', 'Combined Stochastic and Robust Optimization for Electric Autonomous Mobility-on-Demand with Nested Benders Decomposition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sten Elling Tingstad Jacobsen, Balázs Kulcsár, Anders Lindman

**分类**: eess.SY

**发布日期**: 2025-08-27 (更新: 2025-09-01)

**备注**: 29 pages, 12 figures

---

## 💡 一句话要点

**提出结合随机与鲁棒优化的方法以解决电动自主按需出行问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `电动汽车` `自主出行` `随机优化` `鲁棒控制` `模型预测控制` `交通管理` `贝叶斯神经网络`

## 📋 核心要点

1. 现有的电动自主按需出行管理方法在面对需求和基础设施的不确定性时，往往无法有效协调调度和充电决策。
2. 本文提出的框架结合了随机优化与鲁棒控制，利用贝叶斯神经网络进行需求预测，并通过嵌套本德分解实现高效求解。
3. 实验结果表明，该方法在减少乘客等待时间、再平衡距离和电力成本方面均有显著提升，展示了其实际应用潜力。

## 📝 摘要（中文）

电动自主按需出行（EAMoD）车队的有效管理需要在多种不确定性下协调调度、再平衡和充电决策。本文提出了一种结合随机和鲁棒模型预测控制（MPC）框架，整合了时空贝叶斯神经网络预测与多阶段随机优化模型，形成大规模混合整数线性规划。为确保实时应用，开发了定制的嵌套本德分解，利用场景树结构实现高效并行求解。通过高保真模拟评估框架，结果显示该方法在减少乘客等待时间和电力成本方面显著优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决电动自主按需出行（EAMoD）车队管理中的调度、再平衡和充电决策问题，现有方法在面对多种不确定性时表现不足，难以保证实时性和有效性。

**核心思路**：提出结合随机和鲁棒模型预测控制的框架，利用贝叶斯神经网络进行需求预测，并通过多阶段随机优化模型来应对不确定性，确保在最坏情况下的可行性。

**技术框架**：整体架构包括需求预测模块、随机优化模块和嵌套本德分解求解模块。需求预测模块使用贝叶斯神经网络，随机优化模块通过混合整数线性规划进行建模，求解模块则实现高效并行计算。

**关键创新**：最重要的创新在于将随机优化与鲁棒控制相结合，并通过嵌套本德分解技术提高求解效率，这在现有方法中尚未见到。

**关键设计**：在模型中设置了鲁棒约束以确保能量消耗和旅行时间的可行性，采用了多阶段随机优化策略，并进行了电池尺寸和车辆效率的敏感性分析，以评估不同条件下的性能表现。

## 📊 实验亮点

实验结果显示，结合随机与鲁棒优化的方法相比于确定性和反应性基线，乘客中位等待时间减少了最高36%，95百分位延迟减少近20%，再平衡距离降低27%，电力成本降低超过35%。

## 🎯 应用场景

该研究的潜在应用领域包括城市交通管理、共享出行服务和电动汽车充电基础设施规划。通过优化电动自主按需出行的调度和资源配置，可以显著提高城市交通系统的效率和可持续性，降低运营成本，促进绿色出行的发展。

## 📄 摘要（原文）

> The electrification and automation of mobility are reshaping how cities operate on-demand transport systems. Managing Electric Autonomous Mobility-on-Demand (EAMoD) fleets effectively requires coordinating dispatch, rebalancing, and charging decisions under multiple uncertainties, including travel demand, travel time, energy consumption, and charger availability. We address this challenge with a combined stochastic and robust model predictive control (MPC) framework. The framework integrates spatio-temporal Bayesian neural network forecasts with a multi-stage stochastic optimization model, formulated as a large-scale mixed-integer linear program. To ensure real-time applicability, we develop a tailored Nested Benders Decomposition that exploits the scenario tree structure and enables efficient parallelized solution. Stochastic optimization is employed to anticipate demand and infrastructure variability, while robust constraints on energy consumption and travel times safeguard feasibility under worst-case realizations. We evaluate the framework using high-fidelity simulations of San Francisco and Chicago. Compared with deterministic, reactive, and robust baselines, the combined stochastic and robust approach reduces median passenger waiting times by up to 36% and 95th-percentile delays by nearly 20%, while also lowering rebalancing distance by 27% and electricity costs by more than 35%. We also conduct a sensitivity analysis of battery size and vehicle efficiency, finding that energy-efficient vehicles maintain stable performance even with small batteries, whereas less efficient vehicles require larger batteries and greater infrastructure support. Our results emphasize the importance of jointly optimizing predictive control, vehicle capabilities, and infrastructure planning to enable scalable, cost-efficient EAMoD operations.

