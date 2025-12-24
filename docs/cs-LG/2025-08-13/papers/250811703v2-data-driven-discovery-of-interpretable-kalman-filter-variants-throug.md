---
layout: default
title: Data-Driven Discovery of Interpretable Kalman Filter Variants through Large Language Models and Genetic Programming
---

# Data-Driven Discovery of Interpretable Kalman Filter Variants through Large Language Models and Genetic Programming

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11703" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11703v2</a>
  <a href="https://arxiv.org/pdf/2508.11703.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11703v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11703v2', 'Data-Driven Discovery of Interpretable Kalman Filter Variants through Large Language Models and Genetic Programming')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vasileios Saketos, Sebastian Kaltenbach, Sergey Litvinov, Petros Koumoutsakos

**分类**: cs.NE, cs.LG

**发布日期**: 2025-08-13 (更新: 2025-08-25)

---

## 💡 一句话要点

**通过大语言模型和遗传编程提出可解释的卡尔曼滤波器变体**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `卡尔曼滤波器` `遗传编程` `大语言模型` `算法发现` `可解释性`

## 📋 核心要点

1. 现有的算法发现方法往往依赖于人类的创造力和大量实验，效率低下且难以扩展。
2. 本文提出了一种结合笛卡尔遗传编程和大语言模型的自动化进化框架，以发现卡尔曼滤波器的可解释变体。
3. 实验结果表明，在满足卡尔曼最优性假设时，框架能够收敛到近似最优解，且在假设被违反时，进化出的替代方案性能更佳。

## 📝 摘要（中文）

算法发现传统上依赖于人类的创造力和广泛的实验。本文研究了如何通过自动化、数据驱动的进化过程发现卡尔曼滤波器，利用笛卡尔遗传编程（CGP）和大语言模型（LLM）。我们评估了这两种模式在不同条件下发现卡尔曼滤波器的贡献。结果表明，当卡尔曼最优性假设成立时，CGP和LLM辅助进化框架能够收敛到近似最优解；当这些假设被违反时，该框架能够进化出可解释的替代方案，且性能超越卡尔曼滤波器。这些结果表明，将进化算法与生成模型结合用于可解释的数据驱动简单计算模块的合成，是科学计算中算法发现的有效方法。

## 🔬 方法详解

**问题定义**：本文旨在解决如何通过自动化和数据驱动的方法发现卡尔曼滤波器的可解释变体。现有方法依赖于人工设计和实验，效率低且难以适应复杂环境。

**核心思路**：通过结合笛卡尔遗传编程（CGP）和大语言模型（LLM），实现算法的自动发现与优化。CGP用于进化算法的结构设计，而LLM则用于生成和评估算法的可解释性。

**技术框架**：整体框架包括数据收集、CGP进化过程和LLM辅助评估三个主要模块。首先收集相关数据，然后通过CGP生成候选算法，最后利用LLM对这些算法进行评估和优化。

**关键创新**：最重要的创新在于将CGP与LLM结合，形成了一种新的算法发现机制。这种机制不仅能发现高效算法，还能确保其可解释性，与传统的人工设计方法形成鲜明对比。

**关键设计**：在参数设置上，CGP的遗传操作和选择机制经过精心设计，以确保多样性和收敛性。损失函数则结合了算法性能和可解释性，确保进化出的算法在实际应用中具有良好的表现。网络结构方面，LLM用于生成算法描述和评估标准，增强了算法的可解释性。

## 📊 实验亮点

实验结果显示，在满足卡尔曼最优性假设的情况下，框架能够收敛到近似最优解；而在假设被违反时，进化出的可解释替代方案的性能超越了传统卡尔曼滤波器，展示了显著的提升效果。

## 🎯 应用场景

该研究的潜在应用领域包括自动化控制、信号处理和机器人导航等。通过自动发现可解释的卡尔曼滤波器变体，可以提高系统的智能化水平和适应性，降低人工设计的复杂性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Algorithmic discovery has traditionally relied on human ingenuity and extensive experimentation. Here we investigate whether a prominent scientific computing algorithm, the Kalman Filter, can be discovered through an automated, data-driven, evolutionary process that relies on Cartesian Genetic Programming (CGP) and Large Language Models (LLM). We evaluate the contributions of both modalities (CGP and LLM) in discovering the Kalman filter under varying conditions. Our results demonstrate that our framework of CGP and LLM-assisted evolution converges to near-optimal solutions when Kalman optimality assumptions hold. When these assumptions are violated, our framework evolves interpretable alternatives that outperform the Kalman filter. These results demonstrate that combining evolutionary algorithms and generative models for interpretable, data-driven synthesis of simple computational modules is a potent approach for algorithmic discovery in scientific computing.

