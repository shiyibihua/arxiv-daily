---
layout: default
title: Generative Modeling for Robust Deep Reinforcement Learning on the Traveling Salesman Problem
---

# Generative Modeling for Robust Deep Reinforcement Learning on the Traveling Salesman Problem

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08718" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08718v1</a>
  <a href="https://arxiv.org/pdf/2508.08718.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08718v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08718v1', 'Generative Modeling for Robust Deep Reinforcement Learning on the Traveling Salesman Problem')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Michael Li, Eric Bae, Christopher Haberland, Natasha Jaques

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-12

**备注**: 9 pages, 8 figures

---

## 💡 一句话要点

**提出COGS以解决旅行商问题的分布鲁棒性挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `旅行商问题` `组合优化` `生成模型` `深度强化学习` `数据鲁棒性` `物流优化` `神经网络`

## 📋 核心要点

1. 现有神经网络求解器在真实TSP分布上泛化能力不足，导致最坏情况性能较差。
2. 提出组合优化与生成采样（COGS），通过生成模型采样训练数据，增强数据覆盖和插值能力。
3. 在多个合成数据集和TSPLib50上进行评估，COGS在最坏情况下的性能显著提升，优于现有方法。

## 📝 摘要（中文）

旅行商问题（TSP）是一个经典的NP难题，具有广泛的实际应用。传统启发式求解器在小规模问题上表现良好，但在大规模问题上计算复杂度高。现有神经网络求解器在处理真实分布数据时表现不佳，尤其是在最坏情况下。为了解决这一问题，本文提出了组合优化与生成采样（COGS），通过从生成的TSP模型中采样训练数据，改善了数据覆盖和插值能力。同时，构建了TSPLib50数据集，以测试真实世界的泛化能力。实验结果表明，COGS在各种数据集上优于现有神经基线，尤其在最坏情况下表现显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决旅行商问题（TSP）中的分布鲁棒性挑战。现有神经网络方法在真实数据分布上表现不佳，尤其在最坏情况下性能显著下降。

**核心思路**：提出组合优化与生成采样（COGS），通过从生成的TSP模型中采样训练数据，以改善模型对不同数据分布的适应能力。这样设计的目的是为了增强模型的泛化能力，特别是在处理真实世界的TSP实例时。

**技术框架**：COGS的整体架构包括生成模型的训练和基于生成样本的优化过程。首先，构建一个生成模型来模拟真实的TSP分布，然后从中采样生成训练数据，最后使用这些数据训练神经网络求解器。

**关键创新**：COGS的主要创新在于通过生成模型采样训练数据，从而提高了模型在真实分布上的鲁棒性。这一方法与传统的基于固定数据集的训练方式有本质区别，能够更好地适应多样化的TSP实例。

**关键设计**：在模型训练过程中，采用了特定的损失函数以优化生成样本的质量，并设计了适应性网络结构以提高模型的学习能力。此外，TSPLib50数据集的构建为模型的评估提供了真实的测试场景。

## 📊 实验亮点

实验结果显示，COGS在TSPLib50数据集上的表现优于现有神经基线，尤其在最坏情况下性能提升显著。具体而言，COGS在多个测试场景中实现了性能提升，表明其在处理真实世界TSP实例时的有效性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括物流优化、供应链管理和智能交通系统等。通过提高TSP求解器的鲁棒性，能够更有效地处理动态变化的实际问题，如最后一公里配送的实时调度。这将为相关行业带来显著的效率提升和成本降低，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The Traveling Salesman Problem (TSP) is a classic NP-hard combinatorial optimization task with numerous practical applications. Classic heuristic solvers can attain near-optimal performance for small problem instances, but become computationally intractable for larger problems. Real-world logistics problems such as dynamically re-routing last-mile deliveries demand a solver with fast inference time, which has led researchers to investigate specialized neural network solvers. However, neural networks struggle to generalize beyond the synthetic data they were trained on. In particular, we show that there exist TSP distributions that are realistic in practice, which also consistently lead to poor worst-case performance for existing neural approaches. To address this issue of distribution robustness, we present Combinatorial Optimization with Generative Sampling (COGS), where training data is sampled from a generative TSP model. We show that COGS provides better data coverage and interpolation in the space of TSP training distributions. We also present TSPLib50, a dataset of realistically distributed TSP samples, which tests real-world generalization ability without conflating this issue with instance size. We evaluate our method on various synthetic datasets as well as TSPLib50, and compare to state-of-the-art neural baselines. We demonstrate that COGS improves distribution robustness, with most performance gains coming from worst-case scenarios.

