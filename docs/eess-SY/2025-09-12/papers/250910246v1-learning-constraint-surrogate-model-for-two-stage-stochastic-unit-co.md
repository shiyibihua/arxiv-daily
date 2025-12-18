---
layout: default
title: Learning Constraint Surrogate Model for Two-stage Stochastic Unit Commitment
---

# Learning Constraint Surrogate Model for Two-stage Stochastic Unit Commitment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10246" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10246v1</a>
  <a href="https://arxiv.org/pdf/2509.10246.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10246v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10246v1', 'Learning Constraint Surrogate Model for Two-stage Stochastic Unit Commitment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amir Bahador Javadi, Amin Kargarian, Mort Naraghi-Pour

**分类**: eess.SY

**发布日期**: 2025-09-12

---

## 💡 一句话要点

**提出基于SVM代理模型的两阶段随机单元组合优化方法，降低计算复杂度。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `随机单元组合` `支持向量机` `代理模型` `电力系统优化` `可再生能源` `直流潮流` `计算复杂度`

## 📋 核心要点

1. 传统确定性单元组合方法在可再生能源高渗透率下计算成本高昂，难以应对电力系统运行中的显著不确定性。
2. 利用支持向量机(SVM)构建代理模型，替代原始TSUC问题中大量的输电线路潮流约束，从而简化可行域。
3. 在IEEE 57和118节点系统上的实验表明，该方法显著降低了计算时间，同时保持了较高的准确率和较低的发电成本增加。

## 📝 摘要（中文）

本文提出了一种机器学习代理建模方法，旨在重构两阶段随机单元组合(TSUC)问题的可行设计空间，从而降低其计算复杂度。该方法使用支持向量机(SVM)构建基于学习器控制方程的代理模型。该模型将原始的2\|L\| * \|S\|条输电线路潮流约束（其中\|S\|是不确定性场景的数量，\|L\|是输电线路的数量，且\|S\|远小于\|L\|）替换为显著减少的1 * \|S\|条线性不等式约束。该方法在直流潮流近似下可行域的多面体结构中具有理论基础，能够将2\|L\|条线路潮流限制约束转换为单个线性约束。代理模型使用来自计算高效的直流最优潮流模拟生成的数据进行训练。在IEEE 57节点和118节点系统上的仿真结果表明，SVM半空间约束的准确率分别为99.72%和99.88%，TSUC计算时间分别减少了46%和31%，发电成本的增加可忽略不计（IEEE 57节点和118节点系统平均分别为0.63%和0.88%）。这表明了该方法在可再生能源不确定性下实际电力系统运行中的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决可再生能源高渗透率下，传统确定性单元组合方法在处理两阶段随机单元组合(TSUC)问题时计算复杂度过高的问题。现有方法需要考虑大量的不确定性场景和输电线路潮流约束，导致计算量巨大，难以满足实际电力系统运行的需求。

**核心思路**：论文的核心思路是利用机器学习中的支持向量机(SVM)构建一个代理模型，该模型能够近似原始TSUC问题的可行域，从而减少需要考虑的约束数量。通过将大量的输电线路潮流约束替换为少量的线性不等式约束，可以显著降低问题的计算复杂度。之所以选择SVM，是因为其在处理高维数据和非线性问题方面具有良好的性能。

**技术框架**：整体框架包括以下几个主要阶段：1) 使用直流最优潮流(DC OPF)模拟生成训练数据；2) 使用生成的数据训练SVM代理模型，该模型用于近似原始TSUC问题的可行域；3) 将原始TSUC问题中的输电线路潮流约束替换为SVM代理模型生成的线性不等式约束；4) 求解简化后的TSUC问题，得到单元组合方案。

**关键创新**：该论文的关键创新在于利用SVM代理模型来简化TSUC问题的可行域。与传统的确定性方法相比，该方法能够显著降低计算复杂度，同时保持较高的准确率。此外，该方法还具有一定的理论基础，能够保证代理模型的有效性。

**关键设计**：论文中，SVM代理模型的目标是学习一个半空间，该半空间能够近似原始TSUC问题的可行域。SVM的训练数据由DC OPF模拟生成，包括不同的场景和对应的潮流数据。损失函数的设计旨在最大化代理模型的准确率，即尽可能地将可行解划分到可行域内，将不可行解划分到可行域外。具体的SVM参数设置（如核函数类型、惩罚系数等）需要根据实际问题进行调整。

## 📊 实验亮点

实验结果表明，在IEEE 57节点和118节点系统上，SVM半空间约束的准确率分别达到了99.72%和99.88%。与原始TSUC问题相比，该方法能够将计算时间分别减少46%和31%，而发电成本的增加可忽略不计（平均分别为0.63%和0.88%）。这些结果表明，该方法在保证较高准确率的同时，能够显著降低计算复杂度，具有良好的实用价值。

## 🎯 应用场景

该研究成果可应用于实际电力系统运行中，特别是在可再生能源高渗透率的场景下。通过降低TSUC问题的计算复杂度，可以更快地得到最优的单元组合方案，从而提高电力系统的运行效率和可靠性。此外，该方法还可以推广到其他类似的优化问题中，例如电力系统规划、需求响应等。

## 📄 摘要（原文）

> The increasing penetration of renewable energy sources introduces significant uncertainty in power system operations, making traditional deterministic unit commitment approaches computationally expensive. This paper presents a machine learning surrogate modeling approach designed to reformulate the feasible design space of the two-stage stochastic unit commitment (TSUC) problem, reducing its computational complexity. The proposed method uses a support vector machine (SVM) to construct a surrogate model based on the governing equations of the learner. This model replaces the original 2\|L\| * \|S\| transmission line flow constraints, where \|S\| is the number of uncertainty scenarios and \|L\| is the number of transmission lines with \|S\| much less than \|L\|, with a significantly reduced set of 1 * \|S\| linear inequality constraints. The approach is theoretically grounded in the polyhedral structure of the feasible region under the DC power flow approximation, enabling the transformation of 2\|L\| line flow limit constraints into a single linear constraint. The surrogate model is trained using data generated from computationally efficient DC optimal power flow simulations. Simulation results on the IEEE 57-bus and 118-bus systems demonstrate SVM halfspace constraint accuracy of 99.72% and 99.88%, respectively, with TSUC computational time reductions of 46% and 31% and negligible generation cost increases (0.63% and 0.88% on average for IEEE 57- and 118-bus systems, respectively). This shows the effectiveness of the proposed approach for practical power system operations under renewable energy uncertainty.

