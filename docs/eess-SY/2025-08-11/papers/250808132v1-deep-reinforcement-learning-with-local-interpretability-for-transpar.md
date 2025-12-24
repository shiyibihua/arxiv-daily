---
layout: default
title: Deep Reinforcement Learning with Local Interpretability for Transparent Microgrid Resilience Energy Management
---

# Deep Reinforcement Learning with Local Interpretability for Transparent Microgrid Resilience Energy Management

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08132" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08132v1</a>
  <a href="https://arxiv.org/pdf/2508.08132.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08132v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08132v1', 'Deep Reinforcement Learning with Local Interpretability for Transparent Microgrid Resilience Energy Management')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad Hossein Nejati Amiri, Fawaz Annaz, Mario De Oliveira, Florimond Gueniat

**分类**: eess.SY

**发布日期**: 2025-08-11

---

## 💡 一句话要点

**提出可解释深度强化学习以提升微电网韧性管理**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `微电网` `可再生能源` `深度强化学习` `可解释人工智能` `韧性管理` `PPO算法` `LIME方法` `能源管理`

## 📋 核心要点

1. 现有微电网管理方法在应对可再生能源波动和极端天气事件时缺乏透明性和可靠性。
2. 本研究提出了一种结合PPO算法与LIME方法的可解释深度强化学习框架，以提升微电网的韧性管理能力。
3. 实验结果表明，该方法在极端天气条件下实现了韧性指数0.9736，电池寿命预估为15.11年，展示了其有效性。

## 📝 摘要（中文）

可再生能源的整合已成为应对气候变化和资源短缺等全球能源问题的关键方法。然而，可再生能源的波动性和高影响低概率事件的增加要求创新的可靠韧性能源管理策略。本研究提出了一种通过可解释深度强化学习（XDRL）管理微电网韧性的方法。该方法结合了近端策略优化（PPO）算法进行决策，并使用局部可解释模型无关解释（LIME）方法提高决策透明度。通过在印度翁戈尔的案例研究，验证了该方法在极端天气条件下的有效性，结果显示韧性指数为0.9736，电池预期寿命为15.11年。LIME分析揭示了代理在不同模式下的决策依据，表明可再生发电是最具影响力的特征。

## 🔬 方法详解

**问题定义**：本研究旨在解决微电网在可再生能源波动和高影响低概率事件下的韧性管理问题。现有方法往往缺乏透明度，难以解释决策过程，导致用户信任度低。

**核心思路**：本研究通过结合可解释深度强化学习（XDRL）的方法，利用PPO算法进行决策，同时引入LIME方法提升决策的透明性，从而增强微电网的韧性管理能力。

**技术框架**：整体架构包括数据采集、模型训练和决策执行三个主要模块。首先，收集微电网的实时数据，然后使用PPO算法进行训练，最后通过LIME分析决策过程，确保透明性。

**关键创新**：本研究的主要创新在于将可解释性与深度强化学习相结合，利用LIME方法分析决策背后的原因，显著提升了微电网管理的透明度和可靠性。与传统方法相比，XDRL能够提供更清晰的决策依据。

**关键设计**：在模型设计中，采用PPO算法优化决策策略，损失函数设计为结合奖励和可解释性损失，网络结构则包括多层感知机以处理复杂的输入特征。

## 📊 实验亮点

实验结果显示，所提出的方法在极端天气条件下实现了韧性指数0.9736，电池预期寿命为15.11年。LIME分析揭示了可再生发电对决策的关键影响，表明该方法在透明性和可靠性方面的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括智能电网、可再生能源管理和灾害应对等。通过提升微电网的韧性管理能力，能够有效应对极端天气事件，保障能源供应的稳定性和可靠性，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Renewable energy integration into microgrids has become a key approach to addressing global energy issues such as climate change and resource scarcity. However, the variability of renewable sources and the rising occurrence of High Impact Low Probability (HILP) events require innovative strategies for reliable and resilient energy management. This study introduces a practical approach to managing microgrid resilience through Explainable Deep Reinforcement Learning (XDRL). It combines the Proximal Policy Optimization (PPO) algorithm for decision-making with the Local Interpretable Model-agnostic Explanations (LIME) method to improve the transparency of the actor network's decisions. A case study in Ongole, India, examines a microgrid with wind, solar, and battery components to validate the proposed approach. The microgrid is simulated under extreme weather conditions during the Layla cyclone. LIME is used to analyse scenarios, showing the impact of key factors such as renewable generation, state of charge, and load prioritization on decision-making. The results demonstrate a Resilience Index (RI) of 0.9736 and an estimated battery lifespan of 15.11 years. LIME analysis reveals the rationale behind the agent's actions in idle, charging, and discharging modes, with renewable generation identified as the most influential feature. This study shows the effectiveness of integrating advanced DRL algorithms with interpretable AI techniques to achieve reliable and transparent energy management in microgrids.

