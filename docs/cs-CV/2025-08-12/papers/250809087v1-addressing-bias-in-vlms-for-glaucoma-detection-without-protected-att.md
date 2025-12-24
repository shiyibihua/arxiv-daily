---
layout: default
title: Addressing Bias in VLMs for Glaucoma Detection Without Protected Attribute Supervision
---

# Addressing Bias in VLMs for Glaucoma Detection Without Protected Attribute Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09087" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09087v1</a>
  <a href="https://arxiv.org/pdf/2508.09087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09087v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09087v1', 'Addressing Bias in VLMs for Glaucoma Detection Without Protected Attribute Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ahsan Habib Akash, Greg Murray, Annahita Amireskandari, Joel Palko, Carol Laxson, Binod Bhattarai, Prashnna Gyawali

**分类**: cs.CV

**发布日期**: 2025-08-12

**备注**: 3rd Workshop in Data Engineering in Medical Imaging (DEMI), MICCAI-2025 Workshop

---

## 💡 一句话要点

**提出无监督属性去偏见方法以改善青光眼检测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `青光眼检测` `视觉语言模型` `去偏见` `无监督学习` `多模态学习` `医疗影像分析` `公平性评估`

## 📋 核心要点

1. 现有视觉语言模型在青光眼检测中存在人口统计偏见，尤其是在缺乏保护属性监督的情况下。
2. 本文提出了一种无监督的去偏见方法，通过聚类推断子群体并计算梯度相似性权重来改善模型性能。
3. 实验结果显示，该方法在多个公平性指标上表现优异，显著减少了不同子群体间的性能差异。

## 📝 摘要（中文）

视觉语言模型（VLMs）在多模态任务中取得了显著成功，但在缺乏明确保护属性的训练下，仍可能表现出人口统计偏见。本文聚焦于自动青光眼筛查，提出了一种基于重加权的对比学习框架，采用无监督聚类推断代理子群体，并计算CLIP风格多模态损失与SimCLR风格图像对比损失之间的梯度相似性权重。通过在联合的加权目标中应用这些权重，本文的方法能够自适应地针对表现不佳的子群体，从而减少群体间的差异。我们在哈佛FairVLMed青光眼子集上评估了该方法，报告了均衡几率距离（EOD）、均衡子群体AUC（ES AUC）和群体AUC，以展示在推断的人口子群体间的公平性能。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型在青光眼检测中存在的人口统计偏见问题。现有方法在缺乏保护属性监督的情况下，容易导致模型对某些群体的表现不佳，从而影响公平性。

**核心思路**：论文提出了一种无监督的去偏见方法，利用图像嵌入的无监督聚类推断代理子群体，并通过计算梯度相似性权重来增强模型对表现不佳子群体的关注。

**技术框架**：整体架构包括三个主要模块：首先，通过无监督聚类推断图像嵌入的子群体；其次，计算CLIP风格多模态损失与SimCLR风格图像对比损失之间的梯度相似性权重；最后，将这些权重应用于加权目标，以提升表现不佳的子群体的权重。

**关键创新**：最重要的创新在于提出了一种无监督的去偏见方法，能够在没有明确标签的情况下，自动识别并调整模型对不同子群体的关注程度，从而改善公平性。

**关键设计**：在损失函数设计上，采用了加权的多模态损失和对比损失，确保模型能够自适应地关注表现不佳的子群体。此外，聚类算法的选择和参数设置也对最终效果有重要影响。

## 📊 实验亮点

实验结果表明，所提出的方法在哈佛FairVLMed青光眼子集上显著提升了模型的公平性指标，包括均衡几率距离（EOD）和均衡子群体AUC（ES AUC），有效减少了不同子群体间的性能差异，展示了该方法的有效性和实用性。

## 🎯 应用场景

该研究在医疗影像分析领域具有重要应用潜力，尤其是在青光眼等眼科疾病的自动筛查中。通过减少模型的偏见，能够提高对不同人群的诊断准确性，进而改善医疗服务的公平性和可及性。未来，该方法还可扩展到其他疾病的检测和筛查中，推动智能医疗的发展。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have achieved remarkable success on multimodal tasks such as image-text retrieval and zero-shot classification, yet they can exhibit demographic biases even when explicit protected attributes are absent during training. In this work, we focus on automated glaucoma screening from retinal fundus images, a critical application given that glaucoma is a leading cause of irreversible blindness and disproportionately affects underserved populations. Building on a reweighting-based contrastive learning framework, we introduce an attribute-agnostic debiasing method that (i) infers proxy subgroups via unsupervised clustering of image-image embeddings, (ii) computes gradient-similarity weights between the CLIP-style multimodal loss and a SimCLR-style image-pair contrastive loss, and (iii) applies these weights in a joint, top-$k$ weighted objective to upweight underperforming clusters. This label-free approach adaptively targets the hardest examples, thereby reducing subgroup disparities. We evaluate our method on the Harvard FairVLMed glaucoma subset, reporting Equalized Odds Distance (EOD), Equalized Subgroup AUC (ES AUC), and Groupwise AUC to demonstrate equitable performance across inferred demographic subgroups.

