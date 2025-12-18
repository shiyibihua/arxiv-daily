---
layout: default
title: Parking Availability Prediction via Fusing Multi-Source Data with A Self-Supervised Learning Enhanced Spatio-Temporal Inverted Transformer
---

# Parking Availability Prediction via Fusing Multi-Source Data with A Self-Supervised Learning Enhanced Spatio-Temporal Inverted Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04362" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04362v1</a>
  <a href="https://arxiv.org/pdf/2509.04362.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04362v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04362v1', 'Parking Availability Prediction via Fusing Multi-Source Data with A Self-Supervised Learning Enhanced Spatio-Temporal Inverted Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yin Huang, Yongqi Dong, Youhua Tang, Li Li

**分类**: cs.LG, cs.AI, stat.ML

**发布日期**: 2025-09-04

**备注**: 25 pages, 5 figures, under review for journal publication

---

## 💡 一句话要点

**提出SST-iTransformer，融合多源数据和自监督学习，用于精准预测停车位可用性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `停车位预测` `时空预测` `自监督学习` `Transformer` `多源数据融合` `交通需求预测` `智能交通`

## 📋 核心要点

1. 现有方法在建模时空依赖性和利用多源数据方面存在局限性，难以准确预测停车位可用性。
2. 提出SST-iTransformer，通过自监督学习增强时空表示，并采用双分支注意力机制建模复杂依赖关系。
3. 在成都数据集上，SST-iTransformer显著优于现有模型，在MSE指标上取得了最佳性能。

## 📝 摘要（中文）

针对城市停车难题，本研究提出一种新颖的SST-iTransformer方法，旨在提升停车位可用性预测的准确性和有效性。该方法利用K-means聚类建立停车集群区域(PCZ)，提取并整合来自多种交通模式（地铁、公交、网约车和出租车）的交通需求特征。SST-iTransformer在iTransformer基础上进行了升级，集成了基于掩码重建的自监督时空表示学习预训练任务，并采用创新的双分支注意力机制：序列注意力通过分块操作捕获长期时间依赖性，通道注意力通过反转维度建模跨变量交互。在成都真实数据集上的实验表明，SST-iTransformer优于其他深度学习模型，实现了最低的均方误差(MSE)和具有竞争力的平均绝对误差(MAE)。消融研究揭示了不同数据源的重要性：网约车数据增益最大，其次是出租车，而固定线路公交特征（公交/地铁）的贡献较小。空间相关性分析进一步证实，排除PCZ内相关停车场的历史数据会导致性能显著下降，突显了建模空间依赖性的重要性。

## 🔬 方法详解

**问题定义**：论文旨在解决城市停车位可用性预测问题。现有方法在建模复杂的时空依赖关系以及有效融合多源异构数据方面存在不足，导致预测精度不高。尤其是在捕捉长期时间依赖性和跨变量交互方面表现欠佳。

**核心思路**：论文的核心思路是利用自监督学习增强时空表示，并设计一种能够有效建模长期时间依赖性和跨变量交互的Transformer变体。通过融合多种交通模式的数据，更全面地反映停车需求，从而提高预测准确性。

**技术框架**：整体框架包括以下几个主要步骤：1) 利用K-means聚类将停车场划分为停车集群区域(PCZ)。2) 从多种交通模式（地铁、公交、网约车、出租车）提取交通需求特征。3) 使用SST-iTransformer模型进行训练和预测。SST-iTransformer包含一个自监督学习模块和一个双分支注意力模块。自监督学习模块通过掩码重建任务学习时空表示。双分支注意力模块包括序列注意力和通道注意力，分别用于建模长期时间依赖性和跨变量交互。

**关键创新**：论文的关键创新在于：1) 提出了SST-iTransformer，一种改进的Transformer模型，能够更有效地建模时空依赖关系。2) 引入了基于掩码重建的自监督学习方法，用于增强时空表示学习。3) 设计了双分支注意力机制，分别捕捉长期时间依赖性和跨变量交互。

**关键设计**：SST-iTransformer的关键设计包括：1) 自监督学习模块的掩码比例和重建损失函数。2) 序列注意力中的分块大小和滑动窗口大小。3) 通道注意力中的维度反转方式。4) 损失函数采用均方误差(MSE)和平均绝对误差(MAE)的组合，以平衡预测精度和鲁棒性。具体参数设置在论文中有详细描述，但具体数值未知。

## 📊 实验亮点

实验结果表明，SST-iTransformer在成都真实数据集上取得了state-of-the-art的性能，显著优于Informer、Autoformer、Crossformer和iTransformer等基线模型。具体而言，SST-iTransformer实现了最低的均方误差(MSE)，并在平均绝对误差(MAE)方面表现出竞争力。消融研究表明，网约车数据对性能提升贡献最大，其次是出租车数据。

## 🎯 应用场景

该研究成果可应用于智能交通管理系统，帮助用户实时了解停车位可用情况，缓解城市交通拥堵，提高停车效率。此外，该方法还可以为城市规划者提供决策支持，优化停车设施布局，提升城市可持续发展能力。

## 📄 摘要（原文）

> The rapid growth of private car ownership has worsened the urban parking predicament, underscoring the need for accurate and effective parking availability prediction to support urban planning and management. To address key limitations in modeling spatio-temporal dependencies and exploiting multi-source data for parking availability prediction, this study proposes a novel approach with SST-iTransformer. The methodology leverages K-means clustering to establish parking cluster zones (PCZs), extracting and integrating traffic demand characteristics from various transportation modes (i.e., metro, bus, online ride-hailing, and taxi) associated with the targeted parking lots. Upgraded on vanilla iTransformer, SST-iTransformer integrates masking-reconstruction-based pretext tasks for self-supervised spatio-temporal representation learning, and features an innovative dual-branch attention mechanism: Series Attention captures long-term temporal dependencies via patching operations, while Channel Attention models cross-variate interactions through inverted dimensions. Extensive experiments using real-world data from Chengdu, China, demonstrate that SST-iTransformer outperforms baseline deep learning models (including Informer, Autoformer, Crossformer, and iTransformer), achieving state-of-the-art performance with the lowest mean squared error (MSE) and competitive mean absolute error (MAE). Comprehensive ablation studies quantitatively reveal the relative importance of different data sources: incorporating ride-hailing data provides the largest performance gains, followed by taxi, whereas fixed-route transit features (bus/metro) contribute marginally. Spatial correlation analysis further confirms that excluding historical data from correlated parking lots within PCZs leads to substantial performance degradation, underscoring the importance of modeling spatial dependencies.

