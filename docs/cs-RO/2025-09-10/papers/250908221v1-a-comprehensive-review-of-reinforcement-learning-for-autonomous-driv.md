---
layout: default
title: A Comprehensive Review of Reinforcement Learning for Autonomous Driving in the CARLA Simulator
---

# A Comprehensive Review of Reinforcement Learning for Autonomous Driving in the CARLA Simulator

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08221" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08221v1</a>
  <a href="https://arxiv.org/pdf/2509.08221.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08221v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08221v1', 'A Comprehensive Review of Reinforcement Learning for Autonomous Driving in the CARLA Simulator')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Elahe Delavari, Feeza Khan Khanzada, Jaerock Kwon

**分类**: cs.RO

**发布日期**: 2025-09-10

---

## 💡 一句话要点

**综述：CARLA模拟器中基于强化学习的自动驾驶研究**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `自动驾驶` `强化学习` `CARLA模拟器` `深度学习` `综述` `无模型强化学习` `模型基强化学习`

## 📋 核心要点

1. 现有基于深度强化学习的自动驾驶研究缺乏系统性的分析和评估，阻碍了该领域的发展。
2. 本综述通过分析大量基于CARLA模拟器的论文，对强化学习算法在自动驾驶中的应用进行了全面的分类和总结。
3. 该研究总结了现有方法的局限性，并提出了未来研究方向，为该领域的研究人员提供了有价值的参考。

## 📝 摘要（中文）

深度强化学习(RL)作为一种数据驱动的决策框架，近年来在自动驾驶研究中备受青睐。然而，目前对于这些算法如何被应用、基准测试和评估，仍然缺乏清晰的认识。本综述旨在填补这一空白，系统地分析了约100篇在开源CARLA模拟器中训练、测试或验证RL策略的同行评审论文。我们首先按照算法家族（无模型、基于模型、分层和混合）对文献进行分类，并量化它们的流行程度，强调超过80%的现有研究仍然依赖于DQN、PPO和SAC等无模型方法。接下来，我们解释了不同研究中采用的多样化的状态、动作和奖励设计，阐述了传感器模态（RGB、LiDAR、BEV、语义地图和CARLA运动学状态）、控制抽象（离散与连续）和奖励塑造如何在各种文献中使用。我们还通过列出CARLA基准测试中最常用的指标（成功率、碰撞率、车道偏离、驾驶分数）以及城镇、场景和交通配置，整合了评估体系。我们将稀疏奖励、sim-to-real迁移、安全保证和有限的行为多样性等持续存在的挑战提炼为一系列开放的研究问题，并概述了基于模型的RL、元学习和更丰富的多智能体模拟等有希望的方向。通过提供统一的分类、量化统计和对局限性的批判性讨论，本综述旨在为新手提供参考，并为推进基于RL的自动驾驶走向实际部署提供路线图。

## 🔬 方法详解

**问题定义**：现有基于强化学习的自动驾驶研究，在算法选择、状态动作空间设计、奖励函数设计以及评估指标等方面存在多样性，缺乏统一的标准和深入的分析。此外，稀疏奖励、sim-to-real迁移、安全保证和行为多样性等问题仍然是该领域面临的挑战。

**核心思路**：本综述的核心思路是对现有文献进行系统性的分类、总结和分析，从而揭示当前研究的现状、挑战和未来方向。通过量化统计不同算法的使用频率、状态动作空间的设计方法、奖励函数的构建方式以及评估指标的选择，为研究人员提供全面的参考。

**技术框架**：该综述的技术框架主要包括以下几个步骤：1) 文献收集：收集了大量基于CARLA模拟器的自动驾驶强化学习论文。2) 分类：按照算法家族（无模型、基于模型、分层和混合）对文献进行分类。3) 分析：对不同算法的状态、动作和奖励设计进行分析。4) 评估：总结常用的评估指标和基准测试场景。5) 总结：提炼出当前研究的挑战和未来方向。

**关键创新**：本综述的关键创新在于其系统性和全面性。它不仅对现有文献进行了分类和总结，还深入分析了不同算法的设计细节和评估方法，并提出了未来研究的挑战和方向。这种全面的分析为研究人员提供了有价值的参考，有助于推动该领域的发展。

**关键设计**：该综述的关键设计包括：1) 算法分类：将强化学习算法分为无模型、基于模型、分层和混合等类别，有助于研究人员了解不同算法的特点和适用场景。2) 状态动作空间分析：对不同研究中采用的状态和动作空间设计进行分析，有助于研究人员选择合适的状态和动作空间。3) 奖励函数分析：对不同研究中采用的奖励函数设计进行分析，有助于研究人员设计有效的奖励函数。4) 评估指标总结：总结常用的评估指标，有助于研究人员评估算法的性能。

## 📊 实验亮点

该综述统计了超过80%的现有研究仍然依赖于DQN、PPO和SAC等无模型方法，揭示了当前研究的现状。同时，该综述还总结了常用的评估指标（成功率、碰撞率、车道偏离、驾驶分数）和基准测试场景，为研究人员提供了评估算法性能的参考。

## 🎯 应用场景

该综述的研究成果可以应用于自动驾驶算法的开发和评估，为研究人员提供参考和指导。通过了解现有方法的优缺点和未来发展方向，可以加速自动驾驶技术的研发进程，并最终实现安全可靠的自动驾驶系统。

## 📄 摘要（原文）

> Autonomous-driving research has recently embraced deep Reinforcement Learning (RL) as a promising framework for data-driven decision making, yet a clear picture of how these algorithms are currently employed, benchmarked and evaluated is still missing. This survey fills that gap by systematically analysing around 100 peer-reviewed papers that train, test or validate RL policies inside the open-source CARLA simulator. We first categorize the literature by algorithmic family model-free, model-based, hierarchical, and hybrid and quantify their prevalence, highlighting that more than 80% of existing studies still rely on model-free methods such as DQN, PPO and SAC. Next, we explain the diverse state, action and reward formulations adopted across works, illustrating how choices of sensor modality (RGB, LiDAR, BEV, semantic maps, and carla kinematics states), control abstraction (discrete vs. continuous) and reward shaping are used across various literature. We also consolidate the evaluation landscape by listing the most common metrics (success rate, collision rate, lane deviation, driving score) and the towns, scenarios and traffic configurations used in CARLA benchmarks. Persistent challenges including sparse rewards, sim-to-real transfer, safety guarantees and limited behaviour diversity are distilled into a set of open research questions, and promising directions such as model-based RL, meta-learning and richer multi-agent simulations are outlined. By providing a unified taxonomy, quantitative statistics and a critical discussion of limitations, this review aims to serve both as a reference for newcomers and as a roadmap for advancing RL-based autonomous driving toward real-world deployment.

