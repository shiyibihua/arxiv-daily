---
layout: default
title: Interpretable Hybrid Deep Q-Learning Framework for IoT-Based Food Spoilage Prediction with Synthetic Data Generation and Hardware Validation
---

# Interpretable Hybrid Deep Q-Learning Framework for IoT-Based Food Spoilage Prediction with Synthetic Data Generation and Hardware Validation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19361" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19361v1</a>
  <a href="https://arxiv.org/pdf/2512.19361.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19361v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19361v1', 'Interpretable Hybrid Deep Q-Learning Framework for IoT-Based Food Spoilage Prediction with Synthetic Data Generation and Hardware Validation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Isshaan Singh, Divyansh Chawla, Anshu Garg, Shivin Mangal, Pallavi Gupta, Khushi Agarwal, Nimrat Singh Khalsa, Nandan Patel

**分类**: cs.LG

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出一种可解释的混合深度Q学习框架，用于物联网食品腐败预测，并进行硬件验证。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `物联网` `食品腐败预测` `LSTM` `RNN` `可解释人工智能` `混合模型`

## 📋 核心要点

1. 现有食品腐败预测方法缺乏对动态环境的适应性，难以实时优化决策，无法满足现代物联网食品供应链的需求。
2. 提出一种混合强化学习框架，结合LSTM和RNN，利用传感器数据中的时间依赖性，实现更鲁棒和自适应的决策。
3. 在模拟和实时硬件数据上的实验表明，该方法在预测准确性和决策效率方面优于其他强化学习方法，并保持了可解释性。

## 📝 摘要（中文）

本文提出了一种混合强化学习框架，集成长短期记忆网络（LSTM）和循环神经网络（RNN），用于增强食品腐败预测，以应对物联网驱动的食品供应链中易腐货物对环境条件高度敏感的问题。该混合架构捕获传感器数据中的时间依赖性，从而实现鲁棒和自适应的决策。采用基于规则的分类器环境，根据领域特定的阈值，为腐败程度提供透明的ground truth标签，符合可解释人工智能原则。通过腐败准确率、奖励步长比、损失减少率和探索衰减等可解释性驱动的指标来监控模型行为。使用类别腐败分布可视化来分析智能体的决策概况和策略行为。在模拟和实时硬件数据上的大量评估表明，基于LSTM和RNN的智能体在预测准确性和决策效率方面优于其他强化学习方法，同时保持了可解释性。结果突出了具有集成可解释性的混合深度强化学习在可扩展的基于物联网的食品监控系统中的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决物联网驱动的食品供应链中，易腐食品的实时腐败预测问题。现有方法难以适应动态环境，无法有效利用传感器数据中的时间依赖性，导致预测精度不足，且缺乏可解释性。

**核心思路**：论文的核心思路是结合LSTM和RNN的混合深度强化学习框架，利用LSTM和RNN捕获传感器数据中的时间依赖性，从而提高预测精度。同时，通过规则分类器环境和可解释性指标，保证模型决策的透明性和可追溯性。

**技术框架**：整体框架包含以下几个主要模块：1) 数据采集：通过物联网传感器收集环境数据（如温度、湿度等）；2) 状态表示：将传感器数据转化为强化学习智能体的状态；3) 动作空间：定义智能体可以采取的动作，例如调整环境控制参数；4) 奖励函数：根据预测的腐败程度和采取的动作，给予智能体奖励或惩罚；5) 混合深度Q学习智能体：使用LSTM和RNN构建深度Q网络，学习最优策略；6) 可解释性分析：使用腐败准确率、奖励步长比等指标监控模型行为，并进行类别腐败分布可视化。

**关键创新**：该方法的主要创新点在于：1) 提出了一种混合LSTM和RNN的深度Q学习框架，能够有效捕获时间依赖性；2) 引入了基于规则的分类器环境，为腐败程度提供透明的ground truth标签，增强了模型的可解释性；3) 使用可解释性驱动的指标监控模型行为，并进行可视化分析。

**关键设计**：规则分类器环境基于领域专家知识设定腐败阈值，为强化学习提供明确的语义边界。LSTM和RNN的具体网络结构（层数、神经元数量等）未知，奖励函数的设计需要平衡预测精度和控制成本。探索衰减策略用于平衡探索和利用，以提高学习效率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19361v1/fig1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19361v1/fig2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19361v1/fig3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于LSTM和RNN的混合深度Q学习智能体在预测准确性和决策效率方面优于其他强化学习方法。具体性能数据未知，但论文强调了该方法在保持可解释性的同时，实现了性能提升。在模拟和实时硬件数据上的验证进一步证实了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于智能食品供应链管理、冷链物流优化、食品安全监控等领域。通过实时预测食品腐败情况，可以减少食物浪费，降低经济损失，并提高食品安全水平。未来，该技术有望扩展到其他易腐商品的监控和管理。

## 📄 摘要（原文）

> The need for an intelligent, real-time spoilage prediction system has become critical in modern IoT-driven food supply chains, where perishable goods are highly susceptible to environmental conditions. Existing methods often lack adaptability to dynamic conditions and fail to optimize decision making in real time. To address these challenges, we propose a hybrid reinforcement learning framework integrating Long Short-Term Memory (LSTM) and Recurrent Neural Networks (RNN) for enhanced spoilage prediction. This hybrid architecture captures temporal dependencies within sensor data, enabling robust and adaptive decision making. In alignment with interpretable artificial intelligence principles, a rule-based classifier environment is employed to provide transparent ground truth labeling of spoilage levels based on domain-specific thresholds. This structured design allows the agent to operate within clearly defined semantic boundaries, supporting traceable and interpretable decisions. Model behavior is monitored using interpretability-driven metrics, including spoilage accuracy, reward-to-step ratio, loss reduction rate, and exploration decay. These metrics provide both quantitative performance evaluation and insights into learning dynamics. A class-wise spoilage distribution visualization is used to analyze the agents decision profile and policy behavior. Extensive evaluations on simulated and real-time hardware data demonstrate that the LSTM and RNN based agent outperforms alternative reinforcement learning approaches in prediction accuracy and decision efficiency while maintaining interpretability. The results highlight the potential of hybrid deep reinforcement learning with integrated interpretability for scalable IoT-based food monitoring systems.

