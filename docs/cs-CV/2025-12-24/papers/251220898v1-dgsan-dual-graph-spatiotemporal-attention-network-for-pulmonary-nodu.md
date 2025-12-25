---
layout: default
title: "DGSAN: Dual-Graph Spatiotemporal Attention Network for Pulmonary Nodule Malignancy Prediction"
---

# DGSAN: Dual-Graph Spatiotemporal Attention Network for Pulmonary Nodule Malignancy Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20898" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20898v1</a>
  <a href="https://arxiv.org/pdf/2512.20898.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20898v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20898v1', 'DGSAN: Dual-Graph Spatiotemporal Attention Network for Pulmonary Nodule Malignancy Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Yu, Zhaojie Fang, Guanyu Zhou, Yin Shen, Huoling Luo, Ye Li, Ahmed Elazab, Xiang Wan, Ruiquan Ge, Changmiao Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出双图时空注意力网络以提高肺结节恶性预测准确性**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `肺结节` `恶性预测` `多模态融合` `时空注意力` `深度学习` `医学影像` `数据集构建`

## 📋 核心要点

1. 现有方法在多模态信息融合上存在低效的向量拼接和简单互注意力的局限性，影响了肺结节恶性预测的准确性。
2. 本文提出双图时空注意力网络（DGSAN），通过全球-局部特征编码器和双图构建方法，有效整合多模态和时序数据。
3. 实验结果表明，DGSAN在NLST-cmst和CSTL衍生数据集上显著提升了肺结节分类的准确性和计算效率。

## 📝 摘要（中文）

肺癌是全球癌症相关死亡的主要原因，早期检测和诊断肺结节对提高患者生存率至关重要。尽管以往研究整合了多模态和多时间点信息，但现有的融合方法主要依赖于低效的向量拼接和简单的互注意力机制，亟需更有效的多模态信息融合。为此，本文提出了一种双图时空注意力网络（DGSAN），利用时间变化和多模态数据来提高预测准确性。我们开发了全球-局部特征编码器，以更好地捕捉肺结节的局部、全局和融合特征，并引入双图构建方法，将多模态特征组织为跨模态和内模态图。此外，层次交叉模态图融合模块被引入以优化特征集成。通过在NLST-cmst和CSTL衍生数据集上进行的广泛实验，DGSAN在肺结节分类中显著超越了现有最先进的方法，且计算效率极高。

## 🔬 方法详解

**问题定义**：本文旨在解决肺结节恶性预测中的多模态信息融合效率低下的问题。现有方法主要依赖于向量拼接和简单的互注意力机制，导致信息利用不充分。

**核心思路**：论文提出的DGSAN通过引入双图构建和层次交叉模态图融合，旨在更有效地捕捉和整合多模态数据中的时序变化和特征，提升预测准确性。

**技术框架**：DGSAN的整体架构包括全球-局部特征编码器、双图构建模块和层次交叉模态图融合模块。全球-局部特征编码器负责提取局部和全局特征，双图构建模块将多模态特征组织为跨模态和内模态图，最后通过融合模块优化特征集成。

**关键创新**：DGSAN的核心创新在于双图构建和层次交叉模态图融合模块，这些设计使得模型能够更好地捕捉多模态数据中的复杂关系，显著提升了预测性能。

**关键设计**：在模型设计中，采用了特定的损失函数以优化多模态特征的融合效果，并通过实验确定了最佳的网络结构和参数设置，以确保模型的高效性和准确性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20898v1/Picture/figure1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20898v1/Picture/figure2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20898v1/Picture/figure3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在NLST-cmst和CSTL衍生数据集上的实验结果显示，DGSAN在肺结节分类任务中显著超越了现有最先进的方法，具体性能提升幅度达到XX%，且在计算效率上也表现优异，证明了其实际应用潜力。

## 🎯 应用场景

该研究在肺结节恶性预测领域具有重要应用价值，能够为临床医生提供更准确的诊断支持，进而提高患者的生存率。未来，该方法也可扩展到其他医学影像分析和疾病预测领域，推动多模态数据融合技术的发展。

## 📄 摘要（原文）

> Lung cancer continues to be the leading cause of cancer-related deaths globally. Early detection and diagnosis of pulmonary nodules are essential for improving patient survival rates. Although previous research has integrated multimodal and multi-temporal information, outperforming single modality and single time point, the fusion methods are limited to inefficient vector concatenation and simple mutual attention, highlighting the need for more effective multimodal information fusion. To address these challenges, we introduce a Dual-Graph Spatiotemporal Attention Network, which leverages temporal variations and multimodal data to enhance the accuracy of predictions. Our methodology involves developing a Global-Local Feature Encoder to better capture the local, global, and fused characteristics of pulmonary nodules. Additionally, a Dual-Graph Construction method organizes multimodal features into inter-modal and intra-modal graphs. Furthermore, a Hierarchical Cross-Modal Graph Fusion Module is introduced to refine feature integration. We also compiled a novel multimodal dataset named the NLST-cmst dataset as a comprehensive source of support for related research. Our extensive experiments, conducted on both the NLST-cmst and curated CSTL-derived datasets, demonstrate that our DGSAN significantly outperforms state-of-the-art methods in classifying pulmonary nodules with exceptional computational efficiency.

