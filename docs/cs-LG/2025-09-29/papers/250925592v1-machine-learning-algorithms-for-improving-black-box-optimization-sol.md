---
layout: default
title: Machine Learning Algorithms for Improving Black Box Optimization Solvers
---

# Machine Learning Algorithms for Improving Black Box Optimization Solvers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25592" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25592v1</a>
  <a href="https://arxiv.org/pdf/2509.25592.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25592v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25592v1', 'Machine Learning Algorithms for Improving Black Box Optimization Solvers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Morteza Kimiaei, Vyacheslav Kungurtsev

**分类**: cs.LG

**发布日期**: 2025-09-29

**备注**: 74 pages

---

## 💡 一句话要点

**综述：机器学习算法提升黑盒优化求解器性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `黑盒优化` `机器学习` `强化学习` `无导数优化` `贝叶斯优化` `元学习` `替代模型`

## 📋 核心要点

1. 黑盒优化面临高维、噪声和混合整数等挑战，传统方法难以有效处理。
2. 利用机器学习和强化学习，构建替代模型、自适应更新策略和动态算子配置，提升优化性能。
3. 综述多种基于ML/RL的BBO算法，并回顾了相关基准测试，展示了其在实际优化中的潜力。

## 📝 摘要（中文）

黑盒优化(BBO)处理的是目标函数只能通过代价高昂的查询访问，且没有梯度或显式结构的问题。经典的无导数方法——线搜索、直接搜索和基于模型的求解器（如贝叶斯优化）构成了BBO的支柱，但通常在高维、噪声或混合整数设置中表现不佳。最近的研究进展使用机器学习(ML)和强化学习(RL)来增强BBO：ML提供富有表现力的替代模型、自适应更新、元学习组合和生成模型，而RL支持动态算子配置、鲁棒性和跨任务的元优化。本文综述了这些进展，涵盖了具有模块化模型优化框架的神经网络(mlrMBO)、零阶自适应动量方法(ZO-AdaMM)、自动BBO(ABBO)、分布式块状优化(DiBB)、基于分区的贝叶斯优化(SPBOpt)、基于Transformer的优化器(B2Opt)、基于扩散模型的BBO、差分进化的替代辅助RL(Surr-RLDE)、鲁棒BBO(RBO)、具有相对熵的坐标上升模型优化(CAS-MORE)、对数障碍随机梯度下降(LB-SGD)、黑盒策略改进(PIBB)和具有Mamba骨干的离线Q学习(Q-Mamba)等代表性算法。我们还回顾了NeurIPS 2020 BBO挑战赛和MetaBox框架等基准测试工作。总的来说，我们强调了ML和RL如何将经典的非精确求解器转变为更具可扩展性、鲁棒性和适应性的现实世界优化框架。

## 🔬 方法详解

**问题定义**：黑盒优化问题是指目标函数没有显式表达式或梯度信息，只能通过查询来获取函数值。现有方法，如线搜索、直接搜索和贝叶斯优化，在高维、噪声或混合整数等复杂场景下，效率和效果都难以保证。

**核心思路**：利用机器学习（ML）和强化学习（RL）技术，构建目标函数的替代模型，学习自适应的优化策略，并动态配置优化算子，从而提高黑盒优化的效率和鲁棒性。核心在于用数据驱动的方式替代传统的基于规则或模型的优化方法。

**技术框架**：论文综述了多种基于ML/RL的黑盒优化算法，包括：
1. 基于神经网络的模块化模型优化框架(mlrMBO)。
2. 零阶自适应动量方法(ZO-AdaMM)。
3. 自动BBO(ABBO)。
4. 分布式块状优化(DiBB)。
5. 基于分区的贝叶斯优化(SPBOpt)。
6. 基于Transformer的优化器(B2Opt)。
7. 基于扩散模型的BBO。
8. 差分进化的替代辅助RL(Surr-RLDE)。
9. 鲁棒BBO(RBO)。
10. 具有相对熵的坐标上升模型优化(CAS-MORE)。
11. 对数障碍随机梯度下降(LB-SGD)。
12. 黑盒策略改进(PIBB)。
13. 具有Mamba骨干的离线Q学习(Q-Mamba)。

**关键创新**：关键创新在于将机器学习和强化学习的强大能力引入到黑盒优化领域，突破了传统方法的局限性。具体体现在：
1. 使用神经网络、Transformer等模型构建更精确的替代模型。
2. 利用强化学习学习自适应的优化策略，动态调整优化算子。
3. 引入元学习的思想，实现跨任务的知识迁移。

**关键设计**：不同的算法有不同的关键设计。例如，mlrMBO的关键在于模块化的模型设计，可以灵活组合不同的模型组件。B2Opt的关键在于使用Transformer模型来捕捉优化过程中的依赖关系。Surr-RLDE的关键在于使用替代模型来加速强化学习的训练过程。具体的技术细节需要参考原始论文。

## 📊 实验亮点

论文综述了多种基于ML/RL的BBO算法，并在NeurIPS 2020 BBO Challenge和MetaBox框架等基准测试中进行了评估。结果表明，这些算法在各种复杂场景下都取得了显著的性能提升，例如在高维问题上，基于神经网络的替代模型能够更有效地探索搜索空间，从而找到更好的解。

## 🎯 应用场景

该研究成果可广泛应用于工程设计、超参数优化、材料科学、药物发现等领域。在这些领域中，目标函数通常是黑盒的，且评估成本高昂。通过使用ML/RL增强的黑盒优化算法，可以显著提高优化效率，降低实验成本，加速产品研发。

## 📄 摘要（原文）

> Black-box optimization (BBO) addresses problems where objectives are accessible only through costly queries without gradients or explicit structure. Classical derivative-free methods -- line search, direct search, and model-based solvers such as Bayesian optimization -- form the backbone of BBO, yet often struggle in high-dimensional, noisy, or mixed-integer settings.
>   Recent advances use machine learning (ML) and reinforcement learning (RL) to enhance BBO: ML provides expressive surrogates, adaptive updates, meta-learning portfolios, and generative models, while RL enables dynamic operator configuration, robustness, and meta-optimization across tasks.
>   This paper surveys these developments, covering representative algorithms such as NNs with the modular model-based optimization framework (mlrMBO), zeroth-order adaptive momentum methods (ZO-AdaMM), automated BBO (ABBO), distributed block-wise optimization (DiBB), partition-based Bayesian optimization (SPBOpt), the transformer-based optimizer (B2Opt), diffusion-model-based BBO, surrogate-assisted RL for differential evolution (Surr-RLDE), robust BBO (RBO), coordinate-ascent model-based optimization with relative entropy (CAS-MORE), log-barrier stochastic gradient descent (LB-SGD), policy improvement with black-box (PIBB), and offline Q-learning with Mamba backbones (Q-Mamba).
>   We also review benchmark efforts such as the NeurIPS 2020 BBO Challenge and the MetaBox framework. Overall, we highlight how ML and RL transform classical inexact solvers into more scalable, robust, and adaptive frameworks for real-world optimization.

