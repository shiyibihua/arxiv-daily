---
layout: default
title: Physics-Constrained Fine-Tuning of Flow-Matching Models for Generation and Inverse Problems
---

# Physics-Constrained Fine-Tuning of Flow-Matching Models for Generation and Inverse Problems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09156" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09156v1</a>
  <a href="https://arxiv.org/pdf/2508.09156.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09156v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09156v1', 'Physics-Constrained Fine-Tuning of Flow-Matching Models for Generation and Inverse Problems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jan Tauberschmidt, Sophie Fellenz, Sebastian J. Vollmer, Andrew B. Duncan

**分类**: cs.LG, cs.AI, stat.AP

**发布日期**: 2025-08-05

**备注**: 7 pages main content, 10 pages appendices

---

## 💡 一句话要点

**提出物理约束微调流匹配模型以解决逆问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `流匹配模型` `物理约束` `逆问题` `偏微分方程` `生成模型` `科学推断` `数据驱动`

## 📋 核心要点

1. 现有方法在处理逆问题时往往缺乏物理一致性，导致生成结果不符合实际物理规律。
2. 本研究提出了一种微调流匹配生成模型的方法，通过后训练过程最小化偏微分方程的残差，确保生成结果的物理合理性。
3. 实验结果表明，该方法在经典PDE基准测试中显著提高了对PDE约束的满足程度，并准确恢复了潜在系数。

## 📝 摘要（中文）

我们提出了一种框架，用于微调流匹配生成模型，以强制执行物理约束并解决科学系统中的逆问题。从在低保真度或观测数据上训练的模型出发，我们应用可微分的后训练过程，最小化控制偏微分方程（PDE）的弱形式残差，促进物理一致性并遵循边界条件，而不扭曲基础学习分布。为了推断未知的物理输入，如源项、材料参数或边界数据，我们通过可学习的潜在参数预测器增强生成过程，并提出联合优化策略。结果模型生成物理有效的场解，同时提供隐藏参数的合理估计，有效应对数据驱动但考虑物理的病态逆问题。我们在经典PDE基准上验证了该方法，展示了对PDE约束的更好满足和潜在系数的准确恢复。该方法架起了生成建模与科学推断之间的桥梁，为模拟增强发现和物理系统的数据高效建模开辟了新途径。

## 🔬 方法详解

**问题定义**：本论文旨在解决科学系统中的逆问题，现有方法在生成模型时往往忽视物理约束，导致生成结果与实际物理规律不符。

**核心思路**：我们提出了一种微调流匹配生成模型的框架，通过可微分的后训练过程来最小化控制偏微分方程的残差，从而确保生成结果的物理一致性。

**技术框架**：整体架构包括初始生成模型的训练、后训练的微调过程以及潜在参数预测器的引入。后训练阶段通过优化PDE残差来增强模型的物理约束。

**关键创新**：本研究的创新在于将物理约束与生成模型结合，通过后训练过程有效地解决了逆问题，确保生成结果符合物理规律。与现有方法相比，我们的方法在物理一致性和生成质量上有显著提升。

**关键设计**：在模型设计中，我们采用了可微分的损失函数来最小化PDE残差，并引入了可学习的潜在参数预测器，以增强生成过程的灵活性和准确性。

## 📊 实验亮点

实验结果显示，我们的方法在经典PDE基准测试中，PDE约束的满足程度提高了显著，潜在系数的恢复精度也得到了提升，验证了方法的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括物理系统的模拟、工程设计优化以及科学发现等。通过结合生成建模与物理约束，该方法能够在数据稀缺的情况下有效推断未知参数，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We present a framework for fine-tuning flow-matching generative models to enforce physical constraints and solve inverse problems in scientific systems. Starting from a model trained on low-fidelity or observational data, we apply a differentiable post-training procedure that minimizes weak-form residuals of governing partial differential equations (PDEs), promoting physical consistency and adherence to boundary conditions without distorting the underlying learned distribution. To infer unknown physical inputs, such as source terms, material parameters, or boundary data, we augment the generative process with a learnable latent parameter predictor and propose a joint optimization strategy. The resulting model produces physically valid field solutions alongside plausible estimates of hidden parameters, effectively addressing ill-posed inverse problems in a data-driven yet physicsaware manner. We validate our method on canonical PDE benchmarks, demonstrating improved satisfaction of PDE constraints and accurate recovery of latent coefficients. Our approach bridges generative modelling and scientific inference, opening new avenues for simulation-augmented discovery and data-efficient modelling of physical systems.

