---
layout: default
title: Reinforcement Learning Increases Wind Farm Power Production by Enabling Closed-Loop Collaborative Control
---

# Reinforcement Learning Increases Wind Farm Power Production by Enabling Closed-Loop Collaborative Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20554" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20554v1</a>
  <a href="https://arxiv.org/pdf/2506.20554.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20554v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20554v1', 'Reinforcement Learning Increases Wind Farm Power Production by Enabling Closed-Loop Collaborative Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrew Mole, Max Weissenbacher, Georgios Rigas, Sylvain Laizet

**分类**: physics.flu-dyn, cs.LG, eess.SY

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出强化学习控制以提升风电场发电效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `风电场控制` `强化学习` `大涡模拟` `动态闭环控制` `可再生能源` `发电效率` `流动控制`

## 📋 核心要点

1. 现有的风电场控制方法主要是独立操作，未能充分利用涡流的协同效应，导致整体发电效率低下。
2. 本研究提出了一种将强化学习与高保真大涡模拟相结合的动态闭环控制策略，以实现实时响应和协同控制。
3. 实验结果表明，所提出的RL控制器使风电场发电量提升4.30%，显著高于传统静态控制方法的增益。

## 📝 摘要（中文）

传统的风电场控制方法通常独立操作每个涡轮，以最大化单个发电量。然而，通过全场的协调性尾流引导，可以显著提高整体风电场的能量产出。尽管动态闭环控制在流动控制应用中已被证明有效，但风电场优化主要依赖于静态、低保真度的模拟器，忽略了关键的湍流动态。在本研究中，我们首次将强化学习（RL）控制器直接与高保真度的大涡模拟（LES）相结合，实现了对大气湍流的实时响应，通过协作的动态控制策略提升了风电场的发电量。我们的RL控制器相比基线操作实现了4.30%的发电量提升，几乎是通过贝叶斯优化获得的静态最佳偏航控制的2.19%增益的两倍。这些结果确立了动态流动响应控制作为风电场优化的变革性方法，对加速可再生能源的部署以实现净零目标具有直接影响。

## 🔬 方法详解

**问题定义**：本研究旨在解决传统风电场控制方法的局限性，即独立操作各涡轮未能有效协调尾流，导致整体发电效率低下。现有方法主要依赖静态模拟，忽视了湍流动态的影响。

**核心思路**：论文提出将强化学习（RL）控制器与高保真大涡模拟（LES）结合，利用动态闭环控制策略实现对大气湍流的实时响应，从而优化风电场的整体发电效率。

**技术框架**：整体架构包括数据采集、RL控制器训练、LES模拟和实时控制四个主要模块。数据采集模块负责获取风场的实时气象数据，RL控制器通过学习优化控制策略，LES模拟用于提供高保真度的流动场信息，实时控制模块则执行优化后的控制指令。

**关键创新**：本研究的主要创新在于将RL控制与LES相结合，形成了一种动态流动响应控制方法。这种方法与传统的静态控制方法相比，能够实时适应环境变化，显著提高了风电场的发电效率。

**关键设计**：在设计中，RL控制器采用深度学习网络结构，损失函数基于发电量的提升进行优化。关键参数设置包括学习率、折扣因子等，确保控制器能够快速收敛并适应复杂的流动环境。实验中还采用了多种场景进行训练，以增强模型的泛化能力。

## 📊 实验亮点

实验结果显示，所提出的RL控制器相比于基线操作实现了4.30%的发电量提升，几乎是传统静态最佳偏航控制增益的两倍（2.19%）。这一显著提升证明了动态流动响应控制在风电场优化中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括风电场的智能控制系统，能够实时优化涡轮的运行状态，提高整体发电效率。随着可再生能源需求的增加，该技术有助于加速风能的利用，推动实现全球净零排放目标，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Traditional wind farm control operates each turbine independently to maximize individual power output. However, coordinated wake steering across the entire farm can substantially increase the combined wind farm energy production. Although dynamic closed-loop control has proven effective in flow control applications, wind farm optimization has relied primarily on static, low-fidelity simulators that ignore critical turbulent flow dynamics. In this work, we present the first reinforcement learning (RL) controller integrated directly with high-fidelity large-eddy simulation (LES), enabling real-time response to atmospheric turbulence through collaborative, dynamic control strategies. Our RL controller achieves a 4.30% increase in wind farm power output compared to baseline operation, nearly doubling the 2.19% gain from static optimal yaw control obtained through Bayesian optimization. These results establish dynamic flow-responsive control as a transformative approach to wind farm optimization, with direct implications for accelerating renewable energy deployment to net-zero targets.

