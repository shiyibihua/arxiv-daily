---
layout: default
title: Safe and Non-Conservative Contingency Planning for Autonomous Vehicles via Online Learning-Based Reachable Set Barriers
---

# Safe and Non-Conservative Contingency Planning for Autonomous Vehicles via Online Learning-Based Reachable Set Barriers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07464" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07464v1</a>
  <a href="https://arxiv.org/pdf/2509.07464.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07464v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07464v1', 'Safe and Non-Conservative Contingency Planning for Autonomous Vehicles via Online Learning-Based Reachable Set Barriers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Yang, Lei Zheng, Shuzhi Sam Ge, Jun Ma

**分类**: cs.RO, eess.SY

**发布日期**: 2025-09-09

**备注**: 16 pages, 13 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://pathetiue.github.io/frscp.github.io/)

---

## 💡 一句话要点

**提出基于在线学习可达集屏障的自动驾驶车辆安全应急规划方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自动驾驶` `应急规划` `可达集` `在线学习` `轨迹优化` `安全屏障` `不确定性建模`

## 📋 核心要点

1. 现有自动驾驶规划器在应对人类驾驶车辆行为不确定性时，面临安全性和效率难以兼顾的挑战，保守策略牺牲效率，确定性策略则存在安全风险。
2. 该论文提出一种基于在线学习的应急轨迹优化框架，通过动态量化人类驾驶车辆行为的不确定性，并利用可达集屏障确保安全。
3. 通过高保真模拟和真实实验验证，该方法在保持安全性的前提下，显著提高了驾驶效率和乘客舒适度。

## 📝 摘要（中文）

自动驾驶车辆需要在动态不确定的环境中导航，同时平衡安全性和驾驶效率。周围人类驾驶车辆(HVs)的不可预测性和感知不准确性加剧了这一挑战，这要求规划器适应不断变化的不确定性，同时保持安全的轨迹。过度保守的规划器会降低驾驶效率，而确定性方法在面对突发和意外操作时可能会遇到严重问题和失败风险。为了解决这些问题，本文提出了一种实时应急轨迹优化框架。通过采用事件触发的HV控制意图集在线学习，我们的方法动态量化多模态HV不确定性，并逐步细化前向可达集(FRS)。至关重要的是，我们通过基于FRS的屏障约束来强制执行不变安全性，从而确保安全性，而无需依赖HV的准确轨迹预测。这些约束嵌入在应急轨迹优化中，并通过共识交替方向乘子法(ADMM)有效地解决。该系统不断适应HV行为中的不确定性，在不诉诸过度保守主义的情况下保持可行性和安全性。高速公路和城市场景中的高保真模拟以及一系列真实实验表明，在不确定性下保持安全性的同时，驾驶效率和乘客舒适度得到了显着提高。

## 🔬 方法详解

**问题定义**：自动驾驶车辆需要在复杂交通环境中安全高效地行驶，而周围人类驾驶车辆(HVs)的行为具有高度不确定性。传统的确定性规划方法容易因HV的突发动作而失效，而过于保守的规划则会降低驾驶效率。因此，如何在不确定环境下进行安全且高效的轨迹规划是亟待解决的问题。

**核心思路**：该论文的核心思路是通过在线学习动态估计HV的控制意图集，并利用前向可达集(FRS)构建安全屏障，从而在轨迹优化过程中保证安全性。通过事件触发机制，仅在必要时更新HV行为模型，降低计算复杂度。同时，采用共识ADMM算法高效求解优化问题，实现实时规划。

**技术框架**：该方法包含以下主要模块：1) HV控制意图集在线学习模块：通过事件触发机制，根据HV的实际行为在线学习其控制意图集，量化HV行为的不确定性。2) 前向可达集(FRS)计算模块：基于学习到的HV控制意图集，计算HV在未来一段时间内的可达区域，即FRS。3) 应急轨迹优化模块：将基于FRS的安全屏障约束嵌入到轨迹优化问题中，利用共识ADMM算法求解，生成安全且高效的轨迹。

**关键创新**：该方法最重要的创新在于将在线学习与可达集屏障相结合，实现了安全且非保守的应急规划。与传统的基于预测的规划方法不同，该方法不依赖于HV的精确轨迹预测，而是通过FRS保证在HV所有可能的行为下都能保持安全。此外，事件触发的在线学习机制和共识ADMM算法也提高了计算效率。

**关键设计**：HV控制意图集采用多模态高斯混合模型表示，通过贝叶斯滤波在线更新模型参数。事件触发条件基于HV状态与预测轨迹的偏差设定。FRS的计算采用数值方法，通过离散化控制空间和时间，迭代计算可达区域。安全屏障约束采用惩罚函数的形式嵌入到优化目标中。共识ADMM算法用于分布式求解轨迹优化问题，提高计算效率。

## 📊 实验亮点

在高速公路和城市道路场景下的高保真模拟实验表明，该方法能够在保持安全性的前提下，显著提高驾驶效率和乘客舒适度。与传统的保守规划方法相比，该方法能够减少不必要的减速和变道，提高平均速度和行驶里程。真实实验也验证了该方法在实际环境中的可行性和有效性。

## 🎯 应用场景

该研究成果可应用于各种自动驾驶场景，例如高速公路自动巡航、城市道路自动驾驶、以及无人配送等。通过提高自动驾驶车辆在复杂环境下的安全性和效率，可以加速自动驾驶技术的商业化落地，并提升交通运输系统的整体效率和安全性。此外，该方法还可以扩展到其他机器人领域，例如无人机、水下机器人等。

## 📄 摘要（原文）

> Autonomous vehicles must navigate dynamically uncertain environments while balancing the safety and driving efficiency. This challenge is exacerbated by the unpredictable nature of surrounding human-driven vehicles (HVs) and perception inaccuracies, which require planners to adapt to evolving uncertainties while maintaining safe trajectories. Overly conservative planners degrade driving efficiency, while deterministic approaches may encounter serious issues and risks of failure when faced with sudden and unexpected maneuvers. To address these issues, we propose a real-time contingency trajectory optimization framework in this paper. By employing event-triggered online learning of HV control-intent sets, our method dynamically quantifies multi-modal HV uncertainties and refines the forward reachable set (FRS) incrementally. Crucially, we enforce invariant safety through FRS-based barrier constraints that ensure safety without reliance on accurate trajectory prediction of HVs. These constraints are embedded in contingency trajectory optimization and solved efficiently through consensus alternative direction method of multipliers (ADMM). The system continuously adapts to the uncertainties in HV behaviors, preserving feasibility and safety without resorting to excessive conservatism. High-fidelity simulations on highway and urban scenarios, as well as a series of real-world experiments demonstrate significant improvements in driving efficiency and passenger comfort while maintaining safety under uncertainty. The project page is available at https://pathetiue.github.io/frscp.github.io/.

