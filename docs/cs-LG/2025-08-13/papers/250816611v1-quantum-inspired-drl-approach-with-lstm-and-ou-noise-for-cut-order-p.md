---
layout: default
title: Quantum-Inspired DRL Approach with LSTM and OU Noise for Cut Order Planning Optimization
---

# Quantum-Inspired DRL Approach with LSTM and OU Noise for Cut Order Planning Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16611" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16611v1</a>
  <a href="https://arxiv.org/pdf/2508.16611.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16611v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16611v1', 'Quantum-Inspired DRL Approach with LSTM and OU Noise for Cut Order Planning Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yulison Herry Chrisnanto, Julian Evan Chrisnanto

**分类**: cs.LG, math.OC

**发布日期**: 2025-08-13

**备注**: 14 pages,3 figures, 4 tables

---

## 💡 一句话要点

**提出量子启发的深度强化学习方法以优化切割顺序规划**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `长短期记忆` `量子启发` `切割顺序规划` `生产优化` `动态环境` `面料利用率`

## 📋 核心要点

1. 现有的切割顺序规划方法基于静态启发式，难以适应动态生产环境，导致资源浪费和成本增加。
2. 本文提出了一种量子启发的深度强化学习框架，结合LSTM网络和OU噪声，以提高切割顺序规划的效率。
3. 实验结果显示，该方法在面料成本节省方面比传统方法提高了13%，并且具有低变异性和稳定收敛性。

## 📝 摘要（中文）

切割顺序规划（COP）是纺织行业中的一个关键挑战，直接影响面料利用率和生产成本。传统基于静态启发式和目录估算的方法在动态生产环境中往往难以适应，导致次优解决方案和浪费增加。为此，本文提出了一种新颖的量子启发深度强化学习（QI-DRL）框架，该框架结合了长短期记忆（LSTM）网络和奥恩斯坦-乌伦贝克（OU）噪声。该混合方法旨在明确解决关于量子启发概率表示的优势、LSTM基于记忆捕捉序列依赖性的作用，以及OU噪声在促进平滑探索和加速收敛方面的有效性。经过1000个回合的广泛训练，表现出强大的性能，平均奖励为0.81（±0.03），预测损失稳定下降至0.15（±0.02）。比较分析显示，该方法在面料成本节省方面比传统方法高达13%。

## 🔬 方法详解

**问题定义**：本文旨在解决纺织行业中的切割顺序规划（COP）问题，现有方法由于依赖静态启发式，难以适应动态变化的生产环境，导致面料利用率低和生产成本高。

**核心思路**：提出的量子启发深度强化学习框架（QI-DRL）结合了LSTM网络的记忆能力和OU噪声的探索特性，旨在捕捉序列依赖性并加速收敛。

**技术框架**：该框架包括数据输入模块、LSTM网络用于序列建模、OU噪声用于探索策略，以及强化学习算法用于优化决策过程。

**关键创新**：最重要的创新在于将量子启发的概率表示与LSTM和OU噪声结合，区别于传统方法的静态决策机制，能够更好地适应动态环境。

**关键设计**：在网络结构上，采用多层LSTM以增强记忆能力，OU噪声的参数设置经过调优，以确保探索过程的平滑性和有效性，损失函数设计为适应强化学习的需求。

## 📊 实验亮点

实验结果表明，提出的QI-DRL方法在1000个训练回合中，平均奖励达到0.81（±0.03），预测损失稳定下降至0.15（±0.02），并在面料成本节省方面比传统方法提高了13%，显示出显著的性能提升和稳定性。

## 🎯 应用场景

该研究的潜在应用领域包括纺织制造、生产调度和资源优化等，能够显著提高面料利用率，降低生产成本，推动智能制造的发展。未来，该框架还可扩展到其他动态优化问题，具有广泛的实际价值和影响力。

## 📄 摘要（原文）

> Cut order planning (COP) is a critical challenge in the textile industry, directly impacting fabric utilization and production costs. Conventional methods based on static heuristics and catalog-based estimations often struggle to adapt to dynamic production environments, resulting in suboptimal solutions and increased waste. In response, we propose a novel Quantum-Inspired Deep Reinforcement Learning (QI-DRL) framework that integrates Long Short-Term Memory (LSTM) networks with Ornstein-Uhlenbeck noise. This hybrid approach is designed to explicitly address key research questions regarding the benefits of quantum-inspired probabilistic representations, the role of LSTM-based memory in capturing sequential dependencies, and the effectiveness of OU noise in facilitating smooth exploration and faster convergence. Extensive training over 1000 episodes demonstrates robust performance, with an average reward of 0.81 (-+0.03) and a steady decrease in prediction loss to 0.15 (-+0.02). A comparative analysis reveals that the proposed approach achieves fabric cost savings of up to 13% compared to conventional methods. Furthermore, statistical evaluations indicate low variability and stable convergence. Despite the fact that the simulation model makes several simplifying assumptions, these promising results underscore the potential of the scalable and adaptive framework to enhance manufacturing efficiency and pave the way for future innovations in COP optimization.

