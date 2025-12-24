---
layout: default
title: Deep Reinforcement Learning for Optimal Asset Allocation Using DDPG with TiDE
---

# Deep Reinforcement Learning for Optimal Asset Allocation Using DDPG with TiDE

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20103" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20103v1</a>
  <a href="https://arxiv.org/pdf/2508.20103.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20103v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20103v1', 'Deep Reinforcement Learning for Optimal Asset Allocation Using DDPG with TiDE')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rongwei Liu, Jin Zheng, John Cartlidge

**分类**: q-fin.PM, cs.AI, cs.LG, q-fin.RM

**发布日期**: 2025-08-12

**备注**: 10 pages, 3 figures, authors accepted manuscript, to appear in 24th International Conference on Modelling and Applied Simulation (MAS), Sep. 2025, Fes, Morocco

---

## 💡 一句话要点

**提出基于DDPG与TiDE的深度强化学习方法以优化资产配置**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `资产配置` `马尔可夫决策过程` `时间序列分析` `风险调整收益` `动态策略` `凯利准则`

## 📋 核心要点

1. 现有资产配置方法依赖于严格的分布假设，缺乏灵活性和稳健性，难以适应金融市场的波动性。
2. 本文提出将资产配置问题转化为马尔可夫决策过程，利用深度强化学习和TiDE实现动态决策。
3. 实验结果显示，DDPG-TiDE在风险调整收益方面优于Q学习和买入持有策略，展示了其有效性。

## 📝 摘要（中文）

在金融市场中，风险资产与无风险资产的最佳配置一直是一个挑战，传统方法依赖于严格的分布假设或非加性奖励比率，限制了其稳健性和适用性。为了解决这些问题，本文将最佳双资产配置问题表述为马尔可夫决策过程中的序列决策任务，利用强化学习机制在模拟金融场景中开发动态策略。我们采用凯利准则平衡即时奖励信号与长期投资目标，并将时间序列密集编码器（TiDE）集成到深度确定性策略梯度（DDPG）框架中。实证结果表明，DDPG-TiDE优于简单的离散动作Q学习框架，并且生成的风险调整收益高于被动的买入持有策略。

## 🔬 方法详解

**问题定义**：本文旨在解决风险资产与无风险资产的最佳配置问题，现有方法的痛点在于其依赖于严格的分布假设，限制了其在动态市场中的应用。

**核心思路**：通过将资产配置问题建模为马尔可夫决策过程，利用深度强化学习方法，特别是DDPG框架，结合TiDE编码器，形成动态决策策略，克服传统方法的局限性。

**技术框架**：整体架构包括状态空间的定义、动作空间的设计、奖励信号的构建以及策略优化过程。TiDE用于处理时间序列数据，DDPG负责策略的学习与优化。

**关键创新**：将TiDE集成到DDPG框架中是本文的主要创新点，这一设计使得模型能够更好地捕捉时间序列数据的特征，从而提升决策质量。

**关键设计**：在模型设计中，采用凯利准则作为奖励信号，设置了适当的超参数以平衡短期与长期收益，网络结构采用了深度神经网络以增强学习能力。

## 📊 实验亮点

实验结果表明，DDPG-TiDE在风险调整收益方面显著优于传统的Q学习框架，且其收益率高于被动的买入持有策略，展示了在动态市场中优化资产配置的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括金融投资、资产管理和风险控制等。通过优化资产配置策略，投资者可以在波动的市场中实现更高的风险调整收益，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The optimal asset allocation between risky and risk-free assets is a persistent challenge due to the inherent volatility in financial markets. Conventional methods rely on strict distributional assumptions or non-additive reward ratios, which limit their robustness and applicability to investment goals. To overcome these constraints, this study formulates the optimal two-asset allocation problem as a sequential decision-making task within a Markov Decision Process (MDP). This framework enables the application of reinforcement learning (RL) mechanisms to develop dynamic policies based on simulated financial scenarios, regardless of prerequisites. We use the Kelly criterion to balance immediate reward signals against long-term investment objectives, and we take the novel step of integrating the Time-series Dense Encoder (TiDE) into the Deep Deterministic Policy Gradient (DDPG) RL framework for continuous decision-making. We compare DDPG-TiDE with a simple discrete-action Q-learning RL framework and a passive buy-and-hold investment strategy. Empirical results show that DDPG-TiDE outperforms Q-learning and generates higher risk adjusted returns than buy-and-hold. These findings suggest that tackling the optimal asset allocation problem by integrating TiDE within a DDPG reinforcement learning framework is a fruitful avenue for further exploration.

