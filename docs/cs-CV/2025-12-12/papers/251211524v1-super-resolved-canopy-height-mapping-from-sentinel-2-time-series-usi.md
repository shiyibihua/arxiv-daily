---
layout: default
title: Super-Resolved Canopy Height Mapping from Sentinel-2 Time Series Using LiDAR HD Reference Data across Metropolitan France
---

# Super-Resolved Canopy Height Mapping from Sentinel-2 Time Series Using LiDAR HD Reference Data across Metropolitan France

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.11524" target="_blank" class="toolbar-btn">arXiv: 2512.11524v1</a>
    <a href="https://arxiv.org/pdf/2512.11524.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11524v1" 
            onclick="toggleFavorite(this, '2512.11524v1', 'Super-Resolved Canopy Height Mapping from Sentinel-2 Time Series Using LiDAR HD Reference Data across Metropolitan France')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ekaterina Kalinicheva, Florian Helen, Stéphane Mermoz, Florian Mouret, Milena Planells

**分类**: cs.CV, cs.LG

**发布日期**: 2025-12-12

**🔗 代码/项目**: [GITHUB](https://github.com/Global-Earth-Observation/threasure-net)

---

## 💡 一句话要点

**提出THREASURE-Net，利用Sentinel-2时间序列和LiDAR数据进行高分辨率森林冠层高度制图。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `森林监测` `冠层高度` `超分辨率` `Sentinel-2` `LiDAR` `深度学习` `时间序列分析` `遥感`

## 📋 核心要点

1. 精细尺度的森林监测对于理解冠层结构及其动态至关重要，而冠层结构是碳储量、生物多样性和森林健康的关键指标。
2. THREASURE-Net通过整合光谱、时间和空间信号来反映冠层结构，利用深度学习进行树高回归和超分辨率重建。
3. 实验结果表明，该方法优于现有的基于Sentinel数据的先进方法，并且与基于高分辨率影像的方法相比也具有竞争力。

## 📝 摘要（中文）

本文提出了一种名为THREASURE-Net的端到端框架，用于树高回归和超分辨率重建。该模型利用Sentinel-2时间序列数据，并以法国都市区多分辨率的LiDAR高清数据作为参考，生成年度高度图。我们评估了三种模型变体，分别生成2.5米、5米和10米分辨率的树高预测。THREASURE-Net不依赖于任何预训练模型或高分辨率光学影像来训练其超分辨率模块，而是仅从LiDAR导出的高度信息中学习。我们的方法优于现有的基于Sentinel数据的先进方法，并且与基于高分辨率影像的方法相比也具有竞争力。该方法可用于生成高精度的年度冠层高度图，在2.5米、5米和10米分辨率下，平均绝对误差分别为2.62米、2.72米和2.88米。这些结果突显了THREASURE-Net在仅使用免费卫星数据的情况下，对温带森林进行可扩展且经济高效的结构监测的潜力。THREASURE-Net的源代码可在https://github.com/Global-Earth-Observation/threasure-net 获取。

## 🔬 方法详解

**问题定义**：论文旨在解决利用低分辨率遥感数据（Sentinel-2）生成高分辨率冠层高度图的问题。现有方法或者依赖高分辨率影像，成本高昂，或者精度不足，难以满足精细化森林监测的需求。

**核心思路**：论文的核心思路是利用深度学习模型，直接从Sentinel-2时间序列数据中学习到高分辨率冠层高度信息。通过结合LiDAR数据作为训练标签，模型能够学习到低分辨率影像与高分辨率高度之间的映射关系，实现超分辨率重建。

**技术框架**：THREASURE-Net是一个端到端的深度学习框架，主要包含以下模块：数据预处理模块（Sentinel-2时间序列数据清洗和校正）、特征提取模块（提取Sentinel-2影像的光谱和时间特征）、超分辨率重建模块（利用深度神经网络将低分辨率特征映射到高分辨率高度图）、损失计算模块（计算预测高度与LiDAR参考高度之间的误差）。整体流程是从Sentinel-2数据输入到高分辨率冠层高度图输出。

**关键创新**：该方法最重要的创新点在于，它不依赖于任何预训练模型或高分辨率光学影像来训练其超分辨率模块，而是完全从LiDAR导出的高度信息中学习。这降低了对额外数据的依赖，提高了模型的泛化能力和适用性。

**关键设计**：模型采用了一种特定的卷积神经网络结构，用于从Sentinel-2时间序列中提取时空特征，并进行超分辨率重建。损失函数的设计考虑了不同分辨率高度图的特点，可能采用了L1损失、L2损失或其变体。具体的网络结构和参数设置（如卷积核大小、层数、激活函数等）在论文中应该有详细描述（未知）。

## 📊 实验亮点

THREASURE-Net在法国都市区进行了实验验证，结果表明该方法优于现有的基于Sentinel数据的先进方法，并且与基于高分辨率影像的方法相比也具有竞争力。在2.5米、5米和10米分辨率下，平均绝对误差分别为2.62米、2.72米和2.88米。这些结果表明，该方法能够利用免费的Sentinel-2数据生成高精度的冠层高度图。

## 🎯 应用场景

该研究成果可广泛应用于森林资源调查、碳储量评估、生物多样性保护、森林健康监测、自然灾害风险评估等领域。通过生成高精度的年度冠层高度图，可以为政府部门、科研机构和企业提供重要的决策支持，促进可持续森林管理和生态环境保护。未来，该方法可以推广到其他类型的植被和区域，实现更大范围的精细化遥感监测。

## 📄 摘要（原文）

> Fine-scale forest monitoring is essential for understanding canopy structure and its dynamics, which are key indicators of carbon stocks, biodiversity, and forest health. Deep learning is particularly effective for this task, as it integrates spectral, temporal, and spatial signals that jointly reflect the canopy structure. To address this need, we introduce THREASURE-Net, a novel end-to-end framework for Tree Height Regression And Super-Resolution. The model is trained on Sentinel-2 time series using reference height metrics derived from LiDAR HD data at multiple spatial resolutions over Metropolitan France to produce annual height maps. We evaluate three model variants, producing tree-height predictions at 2.5 m, 5 m, and 10 m resolution. THREASURE-Net does not rely on any pretrained model nor on reference very high resolution optical imagery to train its super-resolution module; instead, it learns solely from LiDAR-derived height information. Our approach outperforms existing state-of-the-art methods based on Sentinel data and is competitive with methods based on very high resolution imagery. It can be deployed to generate high-precision annual canopy-height maps, achieving mean absolute errors of 2.62 m, 2.72 m, and 2.88 m at 2.5 m, 5 m, and 10 m resolution, respectively. These results highlight the potential of THREASURE-Net for scalable and cost-effective structural monitoring of temperate forests using only freely available satellite data. The source code for THREASURE-Net is available at: https://github.com/Global-Earth-Observation/threasure-net.

