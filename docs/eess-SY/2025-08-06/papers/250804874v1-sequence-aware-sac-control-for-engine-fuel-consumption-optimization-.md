---
layout: default
title: Sequence Aware SAC Control for Engine Fuel Consumption Optimization in Electrified Powertrain
---

# Sequence Aware SAC Control for Engine Fuel Consumption Optimization in Electrified Powertrain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04874" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04874v1</a>
  <a href="https://arxiv.org/pdf/2508.04874.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04874v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04874v1', 'Sequence Aware SAC Control for Engine Fuel Consumption Optimization in Electrified Powertrain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wafeeq Jaleel, Md Ragib Rownak, Athar Hanif, Sidra Ghayour Bhatti, Qadeer Ahmed

**分类**: eess.SY, cs.AI, cs.LG

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出基于SAC的序列感知控制以优化电动动力系统的燃油消耗**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `混合电动汽车` `强化学习` `软演员-评论家` `序列决策` `能量管理` `燃油消耗优化` `时间依赖性` `智能交通系统`

## 📋 核心要点

1. 核心问题：现有的能源管理方法在复杂的驾驶条件下难以有效优化燃油消耗，尤其是在电池状态和功率需求变化时。
2. 方法要点：本文提出将控制任务视为序列决策问题，并通过引入GRUs和DTs来增强SAC算法，以捕捉时间依赖性。
3. 实验或效果：实验结果显示，基于DT和GRU的SAC代理在燃油节省方面表现优异，尤其是在未见驾驶周期中显著优于传统的前馈网络（FFN）代理。

## 📝 摘要（中文）

随着混合电动汽车（HEVs）在重型卡车中的普及，适应性和高效的能源管理对于减少燃油消耗和维持电池充电至关重要。本文提出了一种基于软演员-评论家（SAC）算法的新型强化学习框架，以优化系列HEVs中的发动机控制。通过将控制任务重新定义为序列决策问题，并在演员和评论家网络中引入门控循环单元（GRUs）和决策变换器（DTs），以捕捉时间依赖性并改善规划。实验结果表明，基于DT的演员和基于GRU的评论家的SAC代理在高速公路燃油经济性测试（HFET）周期中，燃油节省效果接近动态规划（DP）方法的1.8%。

## 🔬 方法详解

**问题定义**：本文旨在解决混合电动汽车在复杂驾驶条件下的燃油消耗优化问题。现有方法在应对电池状态变化和功率需求波动时，缺乏有效的适应性和规划能力。

**核心思路**：论文通过将控制任务重新定义为序列决策问题，利用强化学习中的SAC算法，结合GRUs和DTs来捕捉时间序列中的依赖关系，从而提升决策的准确性和效率。

**技术框架**：整体框架包括两个主要模块：演员网络和评论家网络。演员网络负责生成控制策略，而评论家网络则评估策略的价值。通过引入GRUs和DTs，增强了模型对时间序列数据的处理能力。

**关键创新**：最重要的创新在于将GRUs和DTs集成到SAC算法中，使得模型能够更好地理解和利用历史信息，从而在动态环境中做出更优决策。这一设计与传统的前馈网络方法形成了鲜明对比。

**关键设计**：在网络结构上，采用GRUs作为评论家网络的核心组件，以处理时间序列数据；同时，DTs被用于演员网络，以优化决策过程。损失函数的设计也考虑了时间依赖性，以确保模型在训练过程中能够有效学习。

## 📊 实验亮点

实验结果显示，基于DT的演员和GRU的评论家的SAC代理在HFET周期中燃油节省效果接近动态规划方法的1.8%。在未见驾驶周期（US06和HHDDT）中，序列感知代理的表现持续优于传统的前馈网络代理，显示出其在现实环境中的适应性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括混合电动汽车的能源管理系统、智能交通系统以及其他需要高效能量优化的自动化系统。通过优化燃油消耗，能够显著降低运营成本，并减少环境影响，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> As hybrid electric vehicles (HEVs) gain traction in heavy-duty trucks, adaptive and efficient energy management is critical for reducing fuel consumption while maintaining battery charge for long operation times. We present a new reinforcement learning (RL) framework based on the Soft Actor-Critic (SAC) algorithm to optimize engine control in series HEVs. We reformulate the control task as a sequential decision-making problem and enhance SAC by incorporating Gated Recurrent Units (GRUs) and Decision Transformers (DTs) into both actor and critic networks to capture temporal dependencies and improve planning over time. To evaluate robustness and generalization, we train the models under diverse initial battery states, drive cycle durations, power demands, and input sequence lengths. Experiments show that the SAC agent with a DT-based actor and GRU-based critic was within 1.8% of Dynamic Programming (DP) in fuel savings on the Highway Fuel Economy Test (HFET) cycle, while the SAC agent with GRUs in both actor and critic networks, and FFN actor-critic agent were within 3.16% and 3.43%, respectively. On unseen drive cycles (US06 and Heavy Heavy-Duty Diesel Truck (HHDDT) cruise segment), generalized sequence-aware agents consistently outperformed feedforward network (FFN)-based agents, highlighting their adaptability and robustness in real-world settings.

