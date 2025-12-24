---
layout: default
title: Ethics-Aware Safe Reinforcement Learning for Rare-Event Risk Control in Interactive Urban Driving
---

# Ethics-Aware Safe Reinforcement Learning for Rare-Event Risk Control in Interactive Urban Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14926" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14926v3</a>
  <a href="https://arxiv.org/pdf/2508.14926.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14926v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14926v3', 'Ethics-Aware Safe Reinforcement Learning for Rare-Event Risk Control in Interactive Urban Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dianzhao Li, Ostap Okhrin

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-08-19 (更新: 2025-11-07)

---

## 💡 一句话要点

**提出伦理意识安全强化学习框架以解决城市驾驶中的稀有事件风险控制问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `安全强化学习` `伦理决策` `自动驾驶` `城市交通` `脆弱道路使用者` `风险控制` `多项式路径规划` `优先经验回放`

## 📋 核心要点

1. 现有自动驾驶系统在处理稀有高风险事件时缺乏有效的伦理决策机制，导致对脆弱道路使用者的保护不足。
2. 论文提出了一种分层的安全强化学习框架，结合伦理风险成本信号和动态优先经验回放机制，以提高对稀有事件的学习能力。
3. 实验结果显示，该方法在两个交互基准测试中将冲突频率降低了25-45%，同时保持了舒适性指标在5%以内。

## 📝 摘要（中文）

自动驾驶车辆有望减少交通事故和提高运输效率，但其广泛应用依赖于在常规和紧急操作中嵌入可信且透明的伦理推理，特别是保护脆弱道路使用者（如行人和骑自行车者）。本文提出了一种分层的安全强化学习（Safe RL）框架，通过伦理意识成本信号增强标准驾驶目标。在决策层，Safe RL代理使用复合伦理风险成本进行训练，以生成高层运动目标。在执行层，结合PID和Stanley控制器的多项式路径规划将这些目标转化为平滑、可行的轨迹。我们在基于真实交通数据的闭环仿真环境中训练和验证了该方法，结果表明其在降低他人风险的同时保持自我性能和舒适性方面优于基线方法。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶车辆在城市环境中对脆弱道路使用者的伦理决策问题。现有方法在处理稀有高风险事件时缺乏有效的学习机制，导致潜在的安全隐患。

**核心思路**：论文的核心思路是通过引入伦理意识的成本信号来增强安全强化学习的决策能力，特别是在高风险情况下，确保自动驾驶系统能够做出更为人性化的决策。

**技术框架**：整体架构分为决策层和执行层。在决策层，使用复合伦理风险成本训练Safe RL代理以生成运动目标；在执行层，采用多项式路径规划和PID控制器将目标转化为平滑轨迹。

**关键创新**：最重要的创新在于引入了动态、风险敏感的优先经验回放机制，使得模型能够更有效地学习稀有但关键的高风险事件，从而提升决策的伦理性和安全性。

**关键设计**：在训练过程中，使用复合伦理风险成本作为损失函数，结合多项式路径规划和PID控制器的设计，确保生成的轨迹既准确又舒适。

## 📊 实验亮点

实验结果表明，所提出的框架在两个交互基准测试中，相较于基线方法，冲突频率降低了25-45%，同时保持了舒适性指标在5%以内，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用场景包括城市自动驾驶系统、智能交通管理以及人机交互的安全性提升。通过将伦理决策嵌入自动驾驶系统，可以显著提高对脆弱道路使用者的保护，推动智能交通的可持续发展。

## 📄 摘要（原文）

> Autonomous vehicles hold great promise for reducing traffic fatalities and improving transportation efficiency, yet their widespread adoption hinges on embedding credible and transparent ethical reasoning into routine and emergency maneuvers, particularly to protect vulnerable road users (VRUs) such as pedestrians and cyclists. Here, we present a hierarchical Safe Reinforcement Learning (Safe RL) framework that augments standard driving objectives with ethics-aware cost signals. At the decision level, a Safe RL agent is trained using a composite ethical risk cost, combining collision probability and harm severity, to generate high-level motion targets. A dynamic, risk-sensitive Prioritized Experience Replay mechanism amplifies learning from rare but critical, high-risk events. At the execution level, polynomial path planning coupled with Proportional-Integral-Derivative (PID) and Stanley controllers translates these targets into smooth, feasible trajectories, ensuring both accuracy and comfort. We train and validate our approach on closed-loop simulation environments derived from large-scale, real-world traffic datasets encompassing diverse vehicles, cyclists, and pedestrians, and demonstrate that it outperforms baseline methods in reducing risk to others while maintaining ego performance and comfort. This work provides a reproducible benchmark for Safe RL with explicitly ethics-aware objectives in human-mixed traffic scenarios. Our results highlight the potential of combining formal control theory and data-driven learning to advance ethically accountable autonomy that explicitly protects those most at risk in urban traffic environments. Across two interactive benchmarks and five random seeds, our policy decreases conflict frequency by 25-45% compared to matched task successes while maintaining comfort metrics within 5%.

