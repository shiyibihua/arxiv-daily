---
layout: default
title: Intelligent Sampling of Extreme-Scale Turbulence Datasets for Accurate and Efficient Spatiotemporal Model Training
---

# Intelligent Sampling of Extreme-Scale Turbulence Datasets for Accurate and Efficient Spatiotemporal Model Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03872" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03872v3</a>
  <a href="https://arxiv.org/pdf/2508.03872.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03872v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03872v3', 'Intelligent Sampling of Extreme-Scale Turbulence Datasets for Accurate and Efficient Spatiotemporal Model Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wesley Brewer, Murali Meena Gopalakrishnan, Matthias Maiterth, Aditya Kashi, Jong Youl Choi, Pei Zhang, Stephen Nichols, Riccardo Balin, Miles Couchman, Stephen de Bruyn Kops, P. K. Yeung, Daniel Dotson, Rohini Uma-Vaideswaran, Sarp Oral, Feiyi Wang

**分类**: cs.LG, cs.AI, cs.DC

**发布日期**: 2025-08-05 (更新: 2025-10-23)

**备注**: 13 pages, 9 figures, 2 tables

**DOI**: [10.1145/3731599.3767340](https://doi.org/10.1145/3731599.3767340)

---

## 💡 一句话要点

**提出SICKLE框架以高效训练大规模湍流数据模型**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `湍流数据` `智能采样` `最大熵采样` `模型训练` `能耗评估` `深度学习` `数据预处理`

## 📋 核心要点

1. 核心问题：现有的模型训练方法在数据量庞大的情况下效率低下，难以满足高效学习的需求。
2. 方法要点：提出SICKLE框架，通过最大熵采样方法实现智能子采样，以减少训练数据量并提高模型性能。
3. 实验或效果：在Frontier平台上进行的实验表明，SICKLE能够在降低能耗的同时提升模型准确性，能耗减少幅度可达38倍。

## 📝 摘要（中文）

随着摩尔定律和Dennard缩放的结束，数据量的高效利用变得愈发重要。本文提出了一种名为SICKLE的稀疏智能策划框架，旨在通过智能子采样显著减少训练数据量。SICKLE采用了一种新颖的最大熵采样方法，并在大规模直接数值模拟（DNS）湍流数据集上进行评估。实验结果表明，作为预处理步骤的子采样在许多情况下能够提高模型的准确性，并显著降低能耗，观察到的能耗减少幅度高达38倍。

## 🔬 方法详解

**问题定义**：本文旨在解决在大规模湍流数据集上进行模型训练时，数据量过大导致的训练效率低下问题。现有方法往往依赖于大量数据进行训练，难以实现高效学习。

**核心思路**：论文提出的SICKLE框架通过智能子采样来减少训练数据量，采用最大熵采样方法，以期在保证模型性能的前提下，显著降低数据需求和能耗。

**技术框架**：SICKLE框架包括数据预处理、最大熵采样、模型训练和能耗评估等主要模块。首先对原始数据进行预处理，然后应用最大熵采样选择最具代表性的数据子集，最后进行模型训练并评估能耗。

**关键创新**：SICKLE的最大熵采样方法是其核心创新，与传统的随机采样和相位空间采样相比，能够更有效地选择数据，从而提高模型的准确性和训练效率。

**关键设计**：在设计中，SICKLE框架的参数设置经过精心调优，损失函数采用适应性调整策略，网络结构则基于深度学习模型的最佳实践进行设计，以确保在不同数据集上的良好表现。

## 📊 实验亮点

实验结果显示，SICKLE框架在Frontier平台上进行的评估中，子采样作为预处理步骤能够在许多情况下显著提高模型的准确性，并将能耗降低至原来的38倍，展示了其在高效学习中的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括气象预测、流体动力学模拟以及其他需要处理大规模时空数据的科学研究。通过高效的数据采样和模型训练，SICKLE框架能够帮助研究人员在资源有限的情况下，快速获得高质量的模型，推动相关领域的发展。

## 📄 摘要（原文）

> With the end of Moore's law and Dennard scaling, efficient training increasingly requires rethinking data volume. Can we train better models with significantly less data via intelligent subsampling? To explore this, we develop SICKLE, a sparse intelligent curation framework for efficient learning, featuring a novel maximum entropy (MaxEnt) sampling approach, scalable training, and energy benchmarking. We compare MaxEnt with random and phase-space sampling on large direct numerical simulation (DNS) datasets of turbulence. Evaluating SICKLE at scale on Frontier, we show that subsampling as a preprocessing step can, in many cases, improve model accuracy and substantially lower energy consumption, with observed reductions of up to 38x.

