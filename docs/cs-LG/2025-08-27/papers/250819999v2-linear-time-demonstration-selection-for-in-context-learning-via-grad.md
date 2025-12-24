---
layout: default
title: Linear-Time Demonstration Selection for In-Context Learning via Gradient Estimation
---

# Linear-Time Demonstration Selection for In-Context Learning via Gradient Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19999" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19999v2</a>
  <a href="https://arxiv.org/pdf/2508.19999.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19999v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19999v2', 'Linear-Time Demonstration Selection for In-Context Learning via Gradient Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziniu Zhang, Zhenshuo Zhang, Dongyue Li, Lu Wang, Jennifer Dy, Hongyang R. Zhang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-27 (更新: 2025-11-04)

**备注**: 19 pages. EMNLP'25

---

## 💡 一句话要点

**提出线性时间示例选择算法以优化上下文学习**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文学习` `示例选择` `梯度估计` `模型推理` `自然语言处理` `高效算法` `深度学习`

## 📋 核心要点

1. 现有方法在上下文学习中选择示例时，主要依赖token嵌入的相似性，效率较低且计算复杂度高。
2. 本文提出了一种基于输出梯度的示例选择方法，通过一阶近似估计模型输出，优化了选择过程。
3. 实验结果显示，该方法在多个数据集上误差低于1%，并在大规模模型上显著提升选择效率，超越现有方法。

## 📝 摘要（中文）

本文介绍了一种算法，用于快速选择示例以支持查询集的上下文学习。给定n个示例，如何快速选择k个最适合下游推理的条件示例？现有方法主要基于token嵌入的相似性，而本文提出了一种基于输入嵌入空间中输出梯度的新方法。通过一阶近似估计模型输出，并对多个随机采样子集进行应用，最终聚合结果形成影响评分，从而选择出k个最相关的示例。该方法仅需一次预计算模型输出和梯度，具有线性时间复杂度。实验表明，该方法在多个模型和数据集上表现出色，误差低于1%，并且在参数高达340亿的模型上，选择效率提升可达37.7倍，平均超越现有基于输入嵌入的选择方法11%。

## 🔬 方法详解

**问题定义**：本文解决的是在上下文学习中如何快速选择k个示例以优化下游推理的问题。现有方法主要依赖于token嵌入的相似性，计算复杂度高，效率低下。

**核心思路**：本文的核心思路是基于输入嵌入空间中输出的梯度进行示例选择。通过一阶近似来估计模型输出，从而快速评估不同示例的影响力。

**技术框架**：整体流程包括：首先预计算模型的输出和梯度；然后对多个随机采样的子集进行输出估计；最后聚合这些估计结果，形成每个示例的影响评分，并选择出k个最相关的示例。

**关键创新**：最重要的创新在于使用输出梯度进行示例选择，这与传统基于token嵌入的选择方法有本质区别，显著提高了选择效率。

**关键设计**：在实现中，关键参数包括随机采样的子集数量和影响评分的计算方式，确保了算法的高效性和准确性。

## 📊 实验亮点

实验结果表明，本文提出的梯度估计方法在六个数据集上的误差低于1%，在参数高达340亿的模型上，选择效率提升可达37.7倍，且在平均性能上超越现有基于输入嵌入的选择方法11%。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的提示调优和链式推理等场景。通过优化示例选择过程，可以在大规模模型中实现更高效的推理，提升模型在实际应用中的响应速度和准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This paper introduces an algorithm to select demonstration examples for in-context learning of a query set. Given a set of $n$ examples, how can we quickly select $k$ out of $n$ to best serve as the conditioning for downstream inference? This problem has broad applications in prompt tuning and chain-of-thought reasoning. Since model weights remain fixed during in-context learning, previous work has sought to design methods based on the similarity of token embeddings. This work proposes a new approach based on gradients of the output taken in the input embedding space. Our approach estimates model outputs through a first-order approximation using the gradients. Then, we apply this estimation to multiple randomly sampled subsets. Finally, we aggregate the sampled subset outcomes to form an influence score for each demonstration, and select $k$ most relevant examples. This procedure only requires pre-computing model outputs and gradients once, resulting in a linear-time algorithm relative to model and training set sizes. Extensive experiments across various models and datasets validate the efficiency of our approach. We show that the gradient estimation procedure yields approximations of full inference with less than ${1}\%$ error across six datasets. This allows us to scale up subset selection that would otherwise run full inference by up to ${37.7}\times$ on models with up to $34$ billion parameters, and outperform existing selection methods based on input embeddings by ${11}\%$ on average.

