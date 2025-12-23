---
layout: default
title: How to craft a deep reinforcement learning policy for wind farm flow control
---

# How to craft a deep reinforcement learning policy for wind farm flow control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06204" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06204v2</a>
  <a href="https://arxiv.org/pdf/2506.06204.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06204v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06204v2', 'How to craft a deep reinforcement learning policy for wind farm flow control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Elie Kadoche, Pascal Bianchi, Florence Carton, Philippe Ciblat, Damien Ernst

**分类**: cs.LG

**发布日期**: 2025-06-06 (更新: 2025-08-23)

**备注**: Eighteenth European Workshop on Reinforcement Learning (EWRL 2025)

---

## 💡 一句话要点

**提出深度强化学习策略以优化风电场流动控制**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `风电场` `流动控制` `涡流引导` `图注意力网络` `多头自注意力` `能量优化`

## 📋 核心要点

1. 现有的涡流引导控制方法在动态风况下的适应性较差，限制了其在实际风电场中的应用。
2. 本文提出了一种结合图注意力网络和多头自注意力模块的深度强化学习方法，以优化涡轮机的偏航角。
3. 实验结果显示，该模型在训练效率和能量产出方面均优于传统方法，具有更强的鲁棒性。

## 📝 摘要（中文）

在风电场中，涡流效应会显著降低整体能量产出。风电场流动控制旨在通过协调涡轮机控制来减轻这些效应。本文提出了一种新的深度强化学习方法，旨在开发一种能够在变化风况下有效工作的涡流引导策略。该方法结合了图注意力网络和多头自注意力模块，设计了新的奖励函数和训练策略。实证研究表明，该模型在低保真度的稳态模拟中，训练步骤比全连接神经网络少约10倍，并且在能量产出上提高了多达14%。

## 🔬 方法详解

**问题定义**：本文旨在解决风电场中涡流效应导致的能量产出下降问题。现有的机器学习方法多局限于准静态风况或小型风电场，难以应对动态变化的环境。

**核心思路**：论文提出了一种新的深度强化学习策略，通过设计新的奖励函数和训练策略，结合图注意力网络和多头自注意力模块，来优化涡轮机的偏航角，从而提高能量产出。

**技术框架**：整体架构包括数据输入模块、图注意力网络模块和多头自注意力模块，最后通过强化学习算法进行训练。模型通过实时反馈调整涡轮机的控制策略，以适应变化的风况。

**关键创新**：最重要的创新在于将图注意力网络与多头自注意力结合，形成了一种新的控制策略，能够在动态风况下有效推广，克服了传统方法的局限性。

**关键设计**：在参数设置上，模型采用了新的奖励函数，强调能量产出的提升；网络结构上，使用了图注意力机制来捕捉涡轮机之间的相互影响，确保了控制策略的有效性。

## 📊 实验亮点

实验结果表明，所提出的模型在稳态低保真度模拟中，训练步骤比全连接神经网络少约10倍，并且在能量产出上提高了多达14%，显示出显著的性能优势和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括大型风电场的智能控制系统，能够在动态风况下优化涡轮机的运行策略，从而提高整体能量产出。未来，该方法有望推广至其他可再生能源领域，提升能源利用效率。

## 📄 摘要（原文）

> Within wind farms, wake effects between turbines can significantly reduce overall energy production. Wind farm flow control encompasses methods designed to mitigate these effects through coordinated turbine control. Wake steering, for example, consists in intentionally misaligning certain turbines with the wind to optimize airflow and increase power output. However, designing a robust wake steering controller remains challenging, and existing machine learning approaches are limited to quasi-static wind conditions or small wind farms. This work presents a new deep reinforcement learning methodology to develop a wake steering policy that overcomes these limitations. Our approach introduces a novel architecture that combines graph attention networks and multi-head self-attention blocks, alongside a novel reward function and training strategy. The resulting model computes the yaw angles of each turbine, optimizing energy production in time-varying wind conditions. An empirical study conducted on steady-state, low-fidelity simulation, shows that our model requires approximately 10 times fewer training steps than a fully connected neural network and achieves more robust performance compared to a strong optimization baseline, increasing energy production by up to 14 %. To the best of our knowledge, this is the first deep reinforcement learning-based wake steering controller to generalize effectively across any time-varying wind conditions in a low-fidelity, steady-state numerical simulation setting.

