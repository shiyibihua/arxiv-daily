---
layout: default
title: Few-shot Human Action Anomaly Detection via a Unified Contrastive Learning Framework
---

# Few-shot Human Action Anomaly Detection via a Unified Contrastive Learning Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17726" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17726v1</a>
  <a href="https://arxiv.org/pdf/2508.17726.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17726v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17726v1', 'Few-shot Human Action Anomaly Detection via a Unified Contrastive Learning Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Koichiro Kamide, Shunsuke Sakai, Shun Maeda, Chunzhi Gu, Chao Zhang

**分类**: cs.CV

**发布日期**: 2025-08-25

---

## 💡 一句话要点

**提出统一对比学习框架以解决少样本人类动作异常检测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人类动作异常检测` `对比学习` `少样本学习` `生成模型` `运动增强` `数据稀缺场景`

## 📋 核心要点

1. 现有HAAD方法通常需要为每个动作类别单独训练，且依赖大量正常样本，限制了其可扩展性和实际应用。
2. 本文提出了一种统一的对比学习框架，通过构建类别无关的表示空间，支持少样本异常检测。
3. 在HumanAct12数据集上进行的广泛实验表明，所提方法在训练效率和模型可扩展性方面优于现有技术。

## 📝 摘要（中文）

人类动作异常检测（HAAD）旨在仅利用正常动作数据识别异常动作。现有方法通常采用每类一个模型的范式，需为每个动作类别单独训练，并且需要大量正常样本。这些限制妨碍了可扩展性，并限制了在数据稀缺或新类别频繁出现的实际应用中。为了解决这些问题，本文提出了一种兼容少样本场景的HAAD统一框架。该方法通过对比学习构建类别无关的表示空间，使得通过与给定的小规模正常样本集（支持集）比较来实现异常检测。为提高类别间的泛化能力和类别内的鲁棒性，本文引入了一种基于扩散模型的生成运动增强策略，以创建多样且真实的训练样本。实验结果表明，该方法在HumanAct12数据集上在已见和未见类别设置下均表现出色，展示了其在训练效率和模型可扩展性方面的优势。

## 🔬 方法详解

**问题定义**：本文解决的是在仅有正常动作数据的情况下，如何有效识别异常动作的问题。现有方法的痛点在于需要大量正常样本和每类单独训练，导致可扩展性差。

**核心思路**：本文的核心思路是构建一个统一的对比学习框架，利用类别无关的表示空间，通过与少量正常样本的比较来实现异常检测。这种设计旨在提高模型在少样本场景下的性能。

**技术框架**：整体架构包括数据预处理、对比学习模块和生成运动增强模块。首先，通过对比学习构建表示空间，然后利用生成模型增强训练样本的多样性，最后进行异常检测。

**关键创新**：本文首次引入基于扩散模型的生成运动增强策略，以增强对比学习在动作异常检测中的效果。这一创新与现有方法的本质区别在于其通过生成多样化样本来提高模型的泛化能力。

**关键设计**：在技术细节上，本文采用了特定的损失函数来优化对比学习过程，并设计了扩散模型的参数设置，以确保生成样本的多样性和真实性。

## 📊 实验亮点

在HumanAct12数据集上的实验结果显示，所提方法在已见类别和未见类别设置下均达到了最先进的效果，训练效率显著提高，模型可扩展性得到增强，具体性能指标优于现有基线。

## 🎯 应用场景

该研究的潜在应用领域包括监控系统、智能安防、运动分析等，能够有效识别异常行为，提升安全性和效率。未来，该方法有望在数据稀缺的环境中广泛应用，推动HAAD技术的实际落地。

## 📄 摘要（原文）

> Human Action Anomaly Detection (HAAD) aims to identify anomalous actions given only normal action data during training. Existing methods typically follow a one-model-per-category paradigm, requiring separate training for each action category and a large number of normal samples. These constraints hinder scalability and limit applicability in real-world scenarios, where data is often scarce or novel categories frequently appear. To address these limitations, we propose a unified framework for HAAD that is compatible with few-shot scenarios. Our method constructs a category-agnostic representation space via contrastive learning, enabling AD by comparing test samples with a given small set of normal examples (referred to as the support set). To improve inter-category generalization and intra-category robustness, we introduce a generative motion augmentation strategy harnessing a diffusion-based foundation model for creating diverse and realistic training samples. Notably, to the best of our knowledge, our work is the first to introduce such a strategy specifically tailored to enhance contrastive learning for action AD. Extensive experiments on the HumanAct12 dataset demonstrate the state-of-the-art effectiveness of our approach under both seen and unseen category settings, regarding training efficiency and model scalability for few-shot HAAD.

