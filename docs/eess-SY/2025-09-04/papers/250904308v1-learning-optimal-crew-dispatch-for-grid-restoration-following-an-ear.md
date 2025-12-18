---
layout: default
title: Learning Optimal Crew Dispatch for Grid Restoration Following an Earthquake
---

# Learning Optimal Crew Dispatch for Grid Restoration Following an Earthquake

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04308" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04308v1</a>
  <a href="https://arxiv.org/pdf/2509.04308.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04308v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04308v1', 'Learning Optimal Crew Dispatch for Grid Restoration Following an Earthquake')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Farshad Amani, Faezeh Ardali, Amin Kargarian

**分类**: eess.SY

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**提出基于Transformer和DRL的框架，加速地震后电网恢复中的最优抢修队伍调度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `电网恢复` `抢修队伍调度` `深度强化学习` `Transformer` `灾后重建` `序贯决策` `地震灾害`

## 📋 核心要点

1. 传统混合整数线性规划方法在灾后抢修队伍调度中耗时过长，难以满足实时性要求。
2. 利用Transformer捕获系统状态和时间依赖性，结合DRL实现自适应和可扩展的决策，加速调度过程。
3. 在2869节点欧洲天然气和电力网络上的实验表明，该方法显著加速了恢复，同时保持了高质量的解决方案。

## 📝 摘要（中文）

灾后抢修队伍调度是一项关键但计算密集型任务。传统的混合整数线性规划方法通常需要数分钟甚至数小时才能计算出解决方案，导致在高度动态的恢复环境中决策延误。为了解决这一挑战，我们提出了一种新颖的基于学习的框架，该框架集成了Transformer架构和深度强化学习（DRL），以提供近乎实时的决策支持，同时不影响解决方案的质量。抢修队伍调度被建模为不确定性下的序贯决策问题，其中Transformer捕获高维系统状态和时间依赖性，而DRL实现自适应和可扩展的决策。首先使用已建立的地震标准来表征地震引起的配电网络损坏，然后通过情景生成和缩减流程将可能的结果聚合到单个地理空间影响图中。在此图的基础上，所提出的框架生成二级调度策略，该策略在模拟和历史事件上进行离线训练，并在线部署以实现快速响应。除了显着缩短运行时间外，该方法还通过实现更快，更有效的恢复来增强系统弹性。案例研究，特别是在2869节点欧洲天然气和电力网络上的案例研究表明，该方法在保持高质量解决方案的同时，显着加速了恢复，突显了其在大型灾难响应中实际部署的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决地震等灾害发生后，如何快速有效地调度抢修队伍，以最短的时间恢复电网运行的问题。传统方法，如混合整数线性规划，计算复杂度高，耗时较长，无法满足灾后快速响应的需求。现有方法的痛点在于计算效率低，难以在大规模电网中应用。

**核心思路**：论文的核心思路是将抢修队伍调度问题建模为一个序贯决策问题，并利用深度强化学习（DRL）来学习最优调度策略。为了更好地表征电网状态和时间依赖性，引入了Transformer架构。通过离线训练，在线部署的方式，实现快速的决策。

**技术框架**：该框架主要包含以下几个阶段：1) 地震影响评估：使用地震标准评估地震对配电网络的损害。2) 场景生成与缩减：将可能的地震影响结果聚合为单个地理空间影响图。3) 调度策略生成：基于地理空间影响图，利用Transformer和DRL生成二级调度策略。4) 离线训练与在线部署：在模拟和历史事件上进行离线训练，然后在线部署以实现快速响应。

**关键创新**：该论文的关键创新在于将Transformer架构与深度强化学习相结合，用于解决灾后抢修队伍调度问题。Transformer能够有效地捕获高维系统状态和时间依赖性，而DRL能够实现自适应和可扩展的决策。与传统方法相比，该方法能够显著提高计算效率，实现近乎实时的决策支持。

**关键设计**：论文中Transformer的具体结构和参数设置未知。DRL部分，具体的奖励函数设计和网络结构未知。损失函数的设计也未详细说明。这些细节对于复现论文结果至关重要，但文中并未给出。

## 📊 实验亮点

论文在2869节点欧洲天然气和电力网络上进行了案例研究，结果表明该方法在保持高质量解决方案的同时，显著加速了恢复过程。具体的性能提升数据未知，但摘要强调了运行时间的显著缩短，表明该方法在实际应用中具有很大的潜力。

## 🎯 应用场景

该研究成果可应用于各种灾害后的电力、燃气等基础设施的快速恢复。通过快速优化抢修队伍的调度，可以最大限度地减少停电时间，降低经济损失，并提高社会稳定性。未来，该方法可以扩展到其他类型的灾害和基础设施，例如洪水、飓风和通信网络。

## 📄 摘要（原文）

> Post-disaster crew dispatch is a critical but computationally intensive task. Traditional mixed-integer linear programming methods often require minutes to several hours to compute solutions, leading to delays that hinder timely decision-making in highly dynamic restoration environments. To address this challenge, we propose a novel learning-based framework that integrates transformer architectures with deep reinforcement learning (DRL) to deliver near real-time decision support without compromising solution quality. Crew dispatch is formulated as a sequential decision-making problem under uncertainty, where transformers capture high-dimensional system states and temporal dependencies, while DRL enables adaptive and scalable decision-making. Earthquake-induced distribution network damage is first characterized using established seismic standards, followed by a scenario generation and reduction pipeline that aggregates probable outcomes into a single geospatial impact map. Conditioned on this map, the proposed framework generates second-level dispatch strategies, trained offline on simulated and historical events and deployed online for rapid response. In addition to substantial runtime improvements, the proposed method enhances system resilience by enabling faster and more effective recovery and restoration. Case studies, particularly on the 2869-bus European gas and power network, demonstrate that the method substantially accelerates restoration while maintaining high-quality solutions, underscoring its potential for practical deployment in large-scale disaster response.

