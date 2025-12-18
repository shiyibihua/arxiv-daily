---
layout: default
title: Semi-on-Demand Transit Feeders with Shared Autonomous Vehicles and Reinforcement-Learning-Based Zonal Dispatching Control
---

# Semi-on-Demand Transit Feeders with Shared Autonomous Vehicles and Reinforcement-Learning-Based Zonal Dispatching Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01883" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01883v1</a>
  <a href="https://arxiv.org/pdf/2509.01883.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01883v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01883v1', 'Semi-on-Demand Transit Feeders with Shared Autonomous Vehicles and Reinforcement-Learning-Based Zonal Dispatching Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Max T. M. Ng, Roman Engelhardt, Florian Dandl, Hani S. Mahmassani, Klaus Bogenberger

**分类**: cs.LG, eess.SY, math.OC

**发布日期**: 2025-09-02

**备注**: 6 pages, 9 figures, published in 2024 IEEE 27th International Conference on Intelligent Transportation Systems (ITSC), Edmonton, Canada, 24-27 September 2024

**期刊**: 2024 IEEE 27th International Conference on Intelligent Transportation Systems (ITSC)

**DOI**: [10.1109/ITSC58415.2024.10920214](https://doi.org/10.1109/ITSC58415.2024.10920214)

---

## 💡 一句话要点

**提出基于强化学习区域调度的共享自动驾驶车辆半按需公交接驳服务**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `半按需交通` `共享自动驾驶车辆` `强化学习` `区域调度` `公共交通`

## 📋 核心要点

1. 传统固定线路公交在低密度区域效率低，需求响应式交通成本高，难以兼顾成本效益和适应性。
2. 提出半按需公交接驳服务，结合固定线路和按需响应的优点，利用强化学习动态调度车辆。
3. 在慕尼黑真实公交线路仿真表明，该方法在略微增加成本的情况下，显著提升了乘客服务量。

## 📝 摘要（中文）

本文提出了一种基于共享自动驾驶车辆（SAVs）和强化学习（RL）区域调度控制的半按需公交接驳服务。该服务结合了固定线路公交的成本效益和需求响应式交通的适应性，以提高低密度区域的可达性。车辆从终点站出发，首先进行预定的固定站点停靠，然后在预定的灵活线路区域内提供按需接送服务。我们的深度强化学习模型使用策略梯度算法——近端策略优化（Proximal Policy Optimization），根据实时需求波动和运营情况，动态地将车辆分配到细分的灵活线路区域。通过在德国慕尼黑的真实公交线路上的基于Agent的仿真进行了方法验证。结果表明，经过有效的强化学习模型训练后，与传统的固定线路服务相比，具有动态区域控制的半按需服务平均可服务多16%的乘客，但广义成本高13%。强化学习控制带来的效率提升可服务多2.4%的乘客，但成本高1.4%。这项研究不仅展示了将SAV接驳车和机器学习技术集成到公共交通中的潜力，而且为进一步创新以解决多式联运系统中的“最后一公里”问题奠定了基础。

## 🔬 方法详解

**问题定义**：论文旨在解决低密度区域公共交通“最后一公里”问题，现有固定线路公交效率低，无法满足灵活的出行需求；而完全按需响应的交通方式成本又过高。因此，需要一种兼顾成本效益和灵活性的公共交通解决方案。

**核心思路**：论文的核心思路是将固定线路公交与按需响应交通相结合，提出一种半按需公交接驳服务。车辆首先按照固定线路行驶，然后在特定区域内提供按需接送服务。通过强化学习动态调整车辆在不同区域的分配，以适应实时需求变化，从而优化整体服务效率。

**技术框架**：整体框架包括以下几个主要模块：1) 乘客需求生成模块：模拟乘客的出行需求，包括起点、终点和出行时间。2) 车辆调度模块：基于强化学习算法，动态地将车辆分配到不同的区域。3) 路径规划模块：为车辆规划行驶路线，包括固定线路和按需接送路线。4) 仿真环境：模拟真实的交通环境，包括道路网络、交通流量等。强化学习智能体通过与仿真环境交互，学习最优的调度策略。

**关键创新**：论文的关键创新在于将强化学习应用于半按需公交接驳服务的车辆调度。通过强化学习，车辆可以根据实时需求动态调整分配，从而提高服务效率和乘客满意度。与传统的静态调度方法相比，强化学习能够更好地适应需求变化，并做出更优的决策。

**关键设计**：论文采用近端策略优化（Proximal Policy Optimization, PPO）算法作为强化学习的核心算法。状态空间包括各个区域的乘客需求、车辆位置等信息；动作空间包括将车辆分配到不同区域的决策；奖励函数旨在最大化乘客服务量，同时考虑运营成本。具体参数设置未知。

## 📊 实验亮点

实验结果表明，与传统的固定线路服务相比，该半按需服务在经过强化学习训练后，能够服务多16%的乘客，但广义成本高13%。强化学习控制带来的效率提升可服务多2.4%的乘客，但成本高1.4%。这表明该方法在提高服务效率方面具有显著优势，能够在一定程度上平衡服务质量和运营成本。

## 🎯 应用场景

该研究成果可应用于城市低密度区域的公共交通系统，解决“最后一公里”出行难题，提高公共交通的可达性和吸引力。此外，该方法还可扩展到其他类型的交通服务，如共享单车调度、出租车调度等，具有广阔的应用前景。未来，结合更精确的需求预测和更复杂的交通模型，有望进一步提升服务效率和用户体验。

## 📄 摘要（原文）

> This paper develops a semi-on-demand transit feeder service using shared autonomous vehicles (SAVs) and zonal dispatching control based on reinforcement learning (RL). This service combines the cost-effectiveness of fixed-route transit with the adaptability of demand-responsive transport to improve accessibility in lower-density areas. Departing from the terminus, SAVs first make scheduled fixed stops, then offer on-demand pick-ups and drop-offs in a pre-determined flexible-route area. Our deep RL model dynamically assigns vehicles to subdivided flexible-route zones in response to real-time demand fluctuations and operations, using a policy gradient algorithm - Proximal Policy Optimization. The methodology is demonstrated through agent-based simulations on a real-world bus route in Munich, Germany. Results show that after efficient training of the RL model, the semi-on-demand service with dynamic zonal control serves 16% more passengers at 13% higher generalized costs on average compared to traditional fixed-route service. The efficiency gain brought by RL control brings 2.4% more passengers at 1.4% higher costs. This study not only showcases the potential of integrating SAV feeders and machine learning techniques into public transit, but also sets the groundwork for further innovations in addressing first-mile-last-mile problems in multimodal transit systems.

