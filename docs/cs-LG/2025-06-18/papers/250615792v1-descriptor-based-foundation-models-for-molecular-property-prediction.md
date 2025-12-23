---
layout: default
title: Descriptor-based Foundation Models for Molecular Property Prediction
---

# Descriptor-based Foundation Models for Molecular Property Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15792" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15792v1</a>
  <a href="https://arxiv.org/pdf/2506.15792.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15792v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15792v1', 'Descriptor-based Foundation Models for Molecular Property Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jackson Burns, Akshat Zalte, William Green

**分类**: cs.LG, physics.chem-ph

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出CheMeleon模型以提高分子性质预测的准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分子性质预测` `基础模型` `有向消息传递神经网络` `低噪声描述符` `化学数据集`

## 📋 核心要点

1. 现有方法通常依赖噪声实验数据或量子力学模拟，导致分子性质预测的准确性不足。
2. CheMeleon模型通过使用低噪声的分子描述符，结合有向消息传递神经网络，学习丰富的分子表示。
3. 在58个基准数据集上，CheMeleon在Polaris和MoleculeACE任务中均表现优异，胜率显著高于传统基线模型。

## 📝 摘要（中文）

快速且准确的分子性质预测对于科学进步至关重要。本文提出了一种新型分子基础模型CheMeleon，该模型基于Mordred包中的确定性分子描述符进行预训练，并利用有向消息传递神经网络在无噪声环境下预测这些描述符。与依赖噪声实验数据或偏见量子力学模拟的传统方法不同，CheMeleon使用低噪声分子描述符学习丰富的分子表示。在58个基准数据集上评估后，CheMeleon在Polaris任务中获得79%的胜率，显著优于随机森林（46%）、fastprop（39%）和Chemprop（36%），在MoleculeACE实验中则获得97%的胜率，超越随机森林（63%）及其他基础模型。尽管在区分活性悬崖方面表现不佳，但t-SNE投影显示其有效捕捉化学系列的结构细微差别，展示了描述符预训练在分子性质预测中的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决分子性质预测中现有方法依赖噪声数据和偏见模拟的问题，导致预测准确性不足。

**核心思路**：CheMeleon模型通过使用低噪声的分子描述符进行预训练，结合有向消息传递神经网络，旨在学习更为丰富的分子表示，从而提高预测性能。

**技术框架**：CheMeleon的整体架构包括数据预处理阶段（提取低噪声分子描述符）、模型训练阶段（使用有向消息传递神经网络进行学习）和评估阶段（在多个基准数据集上进行性能测试）。

**关键创新**：CheMeleon的主要创新在于其基于确定性分子描述符的预训练方法，区别于传统方法依赖噪声数据的做法，从而实现更高的预测准确性。

**关键设计**：模型设计中使用了特定的损失函数以优化描述符预测，网络结构采用了有向消息传递神经网络，确保了信息在分子图中的有效传播。

## 📊 实验亮点

CheMeleon在58个基准数据集上表现出色，在Polaris任务中获得79%的胜率，远超随机森林（46%）等基线模型；在MoleculeACE实验中，胜率高达97%，显著优于随机森林（63%）和其他基础模型。这些结果表明该模型在分子性质预测中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括药物发现、材料科学和化学合成等。通过提高分子性质预测的准确性，CheMeleon模型能够加速新材料和药物的开发，推动相关领域的科学研究和技术进步。未来，研究者可以进一步探索不同的描述符集和未标记数据集，以提升模型的泛化能力。

## 📄 摘要（原文）

> Fast and accurate prediction of molecular properties with machine learning is pivotal to scientific advancements across myriad domains. Foundation models in particular have proven especially effective, enabling accurate training on small, real-world datasets. This study introduces CheMeleon, a novel molecular foundation model pre-trained on deterministic molecular descriptors from the Mordred package, leveraging a Directed Message-Passing Neural Network to predict these descriptors in a noise-free setting. Unlike conventional approaches relying on noisy experimental data or biased quantum mechanical simulations, CheMeleon uses low-noise molecular descriptors to learn rich molecular representations. Evaluated on 58 benchmark datasets from Polaris and MoleculeACE, CheMeleon achieves a win rate of 79% on Polaris tasks, outperforming baselines like Random Forest (46%), fastprop (39%), and Chemprop (36%), and a 97% win rate on MoleculeACE assays, surpassing Random Forest (63%) and other foundation models. However, it struggles to distinguish activity cliffs like many of the tested models. The t-SNE projection of CheMeleon's learned representations demonstrates effective separation of chemical series, highlighting its ability to capture structural nuances. These results underscore the potential of descriptor-based pre-training for scalable and effective molecular property prediction, opening avenues for further exploration of descriptor sets and unlabeled datasets.

