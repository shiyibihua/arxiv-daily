---
layout: default
title: Embedding-based Retrieval in Multimodal Content Moderation
---

# Embedding-based Retrieval in Multimodal Content Moderation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.01066" class="toolbar-btn" target="_blank">📄 arXiv: 2507.01066v1</a>
  <a href="https://arxiv.org/pdf/2507.01066.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.01066v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.01066v1', 'Embedding-based Retrieval in Multimodal Content Moderation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanzhong Liang, Jinghao Shi, Xiang Shen, Zixuan Wang, Vera Wen, Ardalan Mehrani, Zhiqian Chen, Yifan Wu, Zhixin Zhang

**分类**: cs.IR, cs.CV, cs.LG

**发布日期**: 2025-06-30

**备注**: Camera ready for SIGIR 2025

**DOI**: [10.1145/3726302.3731945](https://doi.org/10.1145/3726302.3731945)

---

## 💡 一句话要点

**提出嵌入式检索方法以解决短视频内容审核效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `短视频审核` `嵌入式检索` `监督对比学习` `多模态模型` `内容管理` `效率提升` `成本降低`

## 📋 核心要点

1. 现有的内容审核方法主要依赖分类，但在快速响应和成本控制方面存在挑战，特别是在趋势适应和紧急升级场景中。
2. 本文提出了一种嵌入式检索（EBR）方法，结合监督对比学习框架，训练多种嵌入模型，以提高内容审核的效率和准确性。
3. 实验结果显示，EBR在25个新兴趋势的离线实验中，ROC-AUC从0.85提升至0.99，PR-AUC从0.35提升至0.95，在线实验中行动率提高10.32%，运营成本降低超过80%。

## 📝 摘要（中文）

视频理解在短视频平台的内容审核中起着基础性作用，能够检测不当内容。尽管分类方法仍是主流，但在快速响应和成本效益要求高的场景中存在不足。为此，本文提出了一种嵌入式检索（EBR）方法，以补充传统分类方法。我们利用监督对比学习框架训练了一系列基础嵌入模型，包括单模态和多模态架构。实验表明，EBR在处理新兴趋势时显著提升了ROC-AUC和PR-AUC，并在在线实验中提高了行动率和降低了运营成本，同时增强了解释性和灵活性。

## 🔬 方法详解

**问题定义**：本文旨在解决短视频内容审核中传统分类方法在快速响应和成本效益方面的不足，尤其是在处理新兴趋势时的效率问题。

**核心思路**：提出嵌入式检索（EBR）方法，通过训练嵌入模型来实现高效的视频检索，旨在补充传统的分类方法，提升审核的灵活性和响应速度。

**技术框架**：整体架构包括两个主要模块：首先是基于监督对比学习的嵌入模型训练，其次是嵌入生成与视频检索的整合，形成高效的检索系统。

**关键创新**：最重要的创新点在于引入了嵌入式检索方法，利用对比学习框架训练的嵌入模型显著优于现有的对比学习方法（如CLIP和MoCo），在处理新兴趋势时表现出更高的准确性和效率。

**关键设计**：在模型训练中，采用了特定的损失函数和网络结构，以优化嵌入的生成效果，确保模型在多模态数据上的表现优越。

## 📊 实验亮点

实验结果显示，EBR方法在离线实验中将ROC-AUC从0.85提升至0.99，PR-AUC从0.35提升至0.95。在在线实验中，行动率提高了10.32%，运营成本降低超过80%，显示出显著的性能提升和经济效益。

## 🎯 应用场景

该研究的潜在应用领域包括短视频平台的内容审核、社交媒体内容监控以及在线教育视频的内容管理等。通过提高审核效率和降低成本，EBR方法能够为内容平台提供更灵活的应对策略，未来可能在更广泛的多模态内容管理中发挥重要作用。

## 📄 摘要（原文）

> Video understanding plays a fundamental role for content moderation on short video platforms, enabling the detection of inappropriate content. While classification remains the dominant approach for content moderation, it often struggles in scenarios requiring rapid and cost-efficient responses, such as trend adaptation and urgent escalations. To address this issue, we introduce an Embedding-Based Retrieval (EBR) method designed to complement traditional classification approaches. We first leverage a Supervised Contrastive Learning (SCL) framework to train a suite of foundation embedding models, including both single-modal and multi-modal architectures. Our models demonstrate superior performance over established contrastive learning methods such as CLIP and MoCo. Building on these embedding models, we design and implement the embedding-based retrieval system that integrates embedding generation and video retrieval to enable efficient and effective trend handling. Comprehensive offline experiments on 25 diverse emerging trends show that EBR improves ROC-AUC from 0.85 to 0.99 and PR-AUC from 0.35 to 0.95. Further online experiments reveal that EBR increases action rates by 10.32% and reduces operational costs by over 80%, while also enhancing interpretability and flexibility compared to classification-based solutions.

