---
layout: default
title: Quantum Reinforcement Learning Trading Agent for Sector Rotation in the Taiwan Stock Market
---

# Quantum Reinforcement Learning Trading Agent for Sector Rotation in the Taiwan Stock Market

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20930" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20930v2</a>
  <a href="https://arxiv.org/pdf/2506.20930.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20930v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20930v2', 'Quantum Reinforcement Learning Trading Agent for Sector Rotation in the Taiwan Stock Market')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chi-Sheng Chen, Xinyu Zhang, Ya-Chuan Chen

**分类**: quant-ph, cs.LG, q-fin.CP

**发布日期**: 2025-06-26 (更新: 2025-10-20)

---

## 💡 一句话要点

**提出混合量子-经典强化学习框架以解决台湾股市的行业轮换问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `量子强化学习` `行业轮换` `金融市场` `自动化交易` `PPO算法` `量子计算` `模型正则化` `特征工程`

## 📋 核心要点

1. 现有方法在金融领域应用强化学习时，面临代理奖励信号与真实投资目标不匹配的挑战。
2. 论文提出了一种混合量子-经典强化学习框架，结合PPO算法与量子增强模型以优化行业轮换策略。
3. 实证结果显示量子模型在训练奖励上表现优异，但在实际投资回报和风险调整指标上却不如经典模型。

## 📝 摘要（中文）

本文提出了一种混合量子-经典强化学习框架，用于台湾股市的行业轮换。该系统以近端策略优化（PPO）为核心算法，结合经典架构（LSTM、Transformer）和量子增强模型（QNN、QRWKV、QASA）作为策略和价值网络。通过自动化特征工程管道提取金融指标，确保所有配置下模型输入的一致性。实证回测结果显示，尽管量子增强模型在训练奖励上表现更佳，但在实际投资指标如累计回报和夏普比率上却不及经典模型。这一差异揭示了强化学习在金融领域应用中的核心挑战，即代理奖励信号与真实投资目标之间的不匹配。分析表明，当前的奖励设计可能激励过拟合短期波动，而非优化风险调整后的回报。我们讨论了这一奖励-表现差距的影响，并提出了未来改进的方向，包括奖励塑造、模型正则化和基于验证的早停。我们的研究提供了可重复的基准和对量子强化学习在实际金融中应用的关键见解。

## 🔬 方法详解

**问题定义**：本文旨在解决量子强化学习在金融领域应用时，代理奖励信号与真实投资目标之间的不匹配问题。现有方法往往导致模型在训练中表现良好，但在实际投资中效果不佳。

**核心思路**：本研究提出了一种混合量子-经典的强化学习框架，利用PPO作为核心算法，结合经典和量子模型，以期在行业轮换中实现更优的投资策略。

**技术框架**：该框架包括自动化特征工程管道、策略网络（结合LSTM、Transformer和量子模型）和价值网络（同样结合经典与量子模型）。整个流程确保了模型输入的一致性，并通过量子模型提升策略的表达能力。

**关键创新**：论文的主要创新在于将量子增强模型与经典模型结合，尽管量子模型在训练奖励上表现优异，但在实际投资中却未能超越经典模型，揭示了量子模型在金融应用中的潜在局限性。

**关键设计**：在模型设计中，采用了PPO算法作为优化策略，结合了多种网络结构（如LSTM、Transformer、QNN等），并在奖励设计上进行了深入探讨，以避免过拟合短期波动。

## 📊 实验亮点

实验结果表明，量子增强模型在训练阶段的奖励普遍高于经典模型，但在实际投资回报和夏普比率等关键指标上却表现不佳，显示出量子模型在真实市场环境中的应用挑战。

## 🎯 应用场景

该研究的潜在应用领域包括金融市场的自动化交易系统，特别是在行业轮换策略的优化方面。通过结合量子计算与经典机器学习技术，未来可能提高投资决策的准确性与效率，推动金融科技的发展。

## 📄 摘要（原文）

> We propose a hybrid quantum-classical reinforcement learning framework for sector rotation in the Taiwan stock market. Our system employs Proximal Policy Optimization (PPO) as the backbone algorithm and integrates both classical architectures (LSTM, Transformer) and quantum-enhanced models (QNN, QRWKV, QASA) as policy and value networks. An automated feature engineering pipeline extracts financial indicators from capital share data to ensure consistent model input across all configurations. Empirical backtesting reveals a key finding: although quantum-enhanced models consistently achieve higher training rewards, they underperform classical models in real-world investment metrics such as cumulative return and Sharpe ratio. This discrepancy highlights a core challenge in applying reinforcement learning to financial domains -- namely, the mismatch between proxy reward signals and true investment objectives. Our analysis suggests that current reward designs may incentivize overfitting to short-term volatility rather than optimizing risk-adjusted returns. This issue is compounded by the inherent expressiveness and optimization instability of quantum circuits under Noisy Intermediate-Scale Quantum (NISQ) constraints. We discuss the implications of this reward-performance gap and propose directions for future improvement, including reward shaping, model regularization, and validation-based early stopping. Our work offers a reproducible benchmark and critical insights into the practical challenges of deploying quantum reinforcement learning in real-world finance.

