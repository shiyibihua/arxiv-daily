---
layout: default
title: Unsupervised Document and Template Clustering using Multimodal Embeddings
---

# Unsupervised Document and Template Clustering using Multimodal Embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12116" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12116v3</a>
  <a href="https://arxiv.org/pdf/2506.12116.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12116v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12116v3', 'Unsupervised Document and Template Clustering using Multimodal Embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Phillipe R. Sampaio, Helene Maxcici

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-06-13 (更新: 2025-10-26)

**备注**: 24 pages, 12 figures

---

## 💡 一句话要点

**提出无监督文档与模板聚类方法以解决文档组织问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无监督学习` `文档聚类` `多模态编码` `HDBSCAN` `文本处理` `视觉特征` `聚类算法`

## 📋 核心要点

1. 现有的文档聚类方法在处理多模态信息时存在不足，尤其是在模板发现和类别识别方面的挑战。
2. 论文提出了一种无监督聚类的模型无关流程，利用多模态编码器生成文档向量并进行有效聚类。
3. 实验结果表明，融合编码器在不同文档类型上的聚类性能优于单一模态编码器，尤其是在处理降质文档时。

## 📝 摘要（中文）

本研究探讨了使用冻结的多模态编码器和经典聚类算法在类别和模板层面上对文档进行无监督聚类的方法。我们系统化了一个模型无关的流程，该流程将来自文本-布局-视觉编码器的异构最后一层状态投影为令牌类型感知的文档向量，并使用质心或基于密度的方法进行聚类，包括HDBSCAN + k-NN分配以消除未标记点。我们在五个语料库上评估了八种编码器，结果显示视觉特征在干净页面上几乎解决了模板发现，而文本在协变量转移下占主导地位，融合编码器提供了最佳平衡。

## 🔬 方法详解

**问题定义**：本论文旨在解决文档的无监督聚类问题，尤其是在多模态信息（文本、布局、视觉）融合时的挑战。现有方法往往无法有效处理不同模态之间的差异，导致聚类效果不佳。

**核心思路**：论文提出的核心思路是利用冻结的多模态编码器生成令牌类型感知的文档向量，并结合经典聚类算法进行聚类，以实现更高效的文档组织。

**技术框架**：整体架构包括两个主要模块：首先是将异构编码器的最后一层状态投影为文档向量，其次是应用质心或基于密度的聚类方法（如HDBSCAN + k-NN）进行聚类。

**关键创新**：最重要的技术创新在于提出了一种模型无关的聚类流程，能够有效整合多模态信息，并通过消除未标记点来提高聚类的准确性。

**关键设计**：在参数设置上，论文详细描述了使用的聚类算法（如k-Means、DBSCAN、HDBSCAN + k-NN、BIRCH）及其适用场景，并提供了可重复的调优协议和评估设置。

## 📊 实验亮点

实验结果显示，融合编码器在处理干净页面时几乎能够完全解决模板发现问题，而在面对协变量转移时，文本特征的表现更为突出。与基线方法相比，融合模型在聚类准确性上有显著提升，尤其是在处理降质文档时表现优异。

## 🎯 应用场景

该研究的潜在应用场景包括文档管理系统、自动化发票处理、电子证件识别等领域。通过有效的文档聚类，可以显著提高信息检索和组织的效率，降低人工干预的需求，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We study unsupervised clustering of documents at both the category and template levels using frozen multimodal encoders and classical clustering algorithms. We systematize a model-agnostic pipeline that (i) projects heterogeneous last-layer states from text-layout-vision encoders into token-type-aware document vectors and (ii) performs clustering with centroid- or density-based methods, including an HDBSCAN + $k$-NN assignment to eliminate unlabeled points. We evaluate eight encoders (text-only, layout-aware, vision-only, and vision-language) with $k$-Means, DBSCAN, HDBSCAN + $k$-NN, and BIRCH on five corpora spanning clean synthetic invoices, their heavily degraded print-and-scan counterparts, scanned receipts, and real identity and certificate documents. The study reveals modality-specific failure modes and a robustness-accuracy trade-off, with vision features nearly solving template discovery on clean pages while text dominates under covariate shift, and fused encoders offering the best balance. We detail a reproducible, oracle-free tuning protocol and the curated evaluation settings to guide future work on unsupervised document organization.

