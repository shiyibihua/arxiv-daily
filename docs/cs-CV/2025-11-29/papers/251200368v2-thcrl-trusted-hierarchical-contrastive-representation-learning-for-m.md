---
layout: default
title: THCRL: Trusted Hierarchical Contrastive Representation Learning for Multi-View Clustering
---

# THCRL: Trusted Hierarchical Contrastive Representation Learning for Multi-View Clustering

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.00368" target="_blank" class="toolbar-btn">arXiv: 2512.00368v2</a>
    <a href="https://arxiv.org/pdf/2512.00368.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00368v2" 
            onclick="toggleFavorite(this, '2512.00368v2', 'THCRL: Trusted Hierarchical Contrastive Representation Learning for Multi-View Clustering')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jian Zhu

**分类**: cs.CV

**发布日期**: 2025-11-29 (更新: 2025-12-10)

---

## 💡 一句话要点

**提出THCRL，解决多视图聚类中不可信融合问题，提升聚类性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多视图聚类` `对比学习` `深度学习` `表示学习` `数据融合`

## 📋 核心要点

1. 现有MVC方法忽略了视图内的噪声，导致融合结果不可靠，影响聚类性能。
2. THCRL通过DSHF模块进行可信融合，并利用AKCL模块对齐融合表示和视图表示。
3. 实验结果表明，THCRL在深度MVC任务中取得了state-of-the-art的性能。

## 📝 摘要（中文）

多视图聚类(MVC)近年来受到越来越多的关注。它通过学习一致性表示将数据样本划分为不同的组。然而，一个重要的挑战仍然存在：不可信融合问题。这个问题主要源于两个关键因素：1)现有方法通常忽略单个视图中固有的噪声；2)在传统的基于对比学习(CL)的MVC方法中，相似性计算通常依赖于同一实例的不同视图，而忽略了同一集群内最近邻的结构信息。因此，这导致了多视图融合的错误方向。为了解决这个问题，我们提出了一种新的可信分层对比表示学习(THCRL)。它由两个关键模块组成。具体来说，我们提出了深度对称分层融合(DSHF)模块，该模块利用集成了多个去噪机制的UNet架构来实现多视图数据的可信融合。此外，我们提出了平均K近邻对比学习(AKCL)模块，以将融合表示与特定视图表示对齐。与传统策略不同，AKCL增强了属于同一集群的样本之间的表示相似性，而不仅仅是关注跨视图的相同样本，从而增强了融合表示的置信度。大量的实验表明，THCRL在深度MVC任务中实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决多视图聚类中由于视图噪声和传统对比学习方法缺陷导致的不可信融合问题。现有方法忽略了单个视图中固有的噪声，并且在对比学习中仅关注同一实例的不同视图，忽略了同一簇内近邻的结构信息，导致融合方向错误，影响聚类效果。

**核心思路**：论文的核心思路是通过可信的分层对比表示学习，减轻视图噪声的影响，并利用同一簇内近邻的结构信息来指导融合过程。具体来说，通过深度对称分层融合(DSHF)模块进行去噪融合，并通过平均K近邻对比学习(AKCL)模块对齐融合表示和视图表示。

**技术框架**：THCRL包含两个主要模块：DSHF和AKCL。DSHF模块使用UNet架构，并集成多个去噪机制，实现多视图数据的可信融合。AKCL模块则通过增强同一簇内样本的表示相似性，对齐融合表示和视图表示。整体流程是先通过DSHF进行融合，然后利用AKCL进行对比学习，最终得到更可靠的聚类结果。

**关键创新**：论文的关键创新在于提出了DSHF和AKCL两个模块，分别解决了视图噪声和对比学习方向错误的问题。DSHF通过UNet和去噪机制实现可信融合，AKCL则利用同一簇内近邻信息进行对比学习，避免了传统方法仅关注同一实例不同视图的局限性。

**关键设计**：DSHF模块的关键设计在于UNet架构的选择和去噪机制的集成，UNet能够有效提取多尺度特征，去噪机制则能够减轻视图噪声的影响。AKCL模块的关键设计在于平均K近邻策略，通过计算K近邻的平均表示，增强了同一簇内样本的相似性。

## 📊 实验亮点

论文通过大量实验验证了THCRL的有效性，在多个数据集上取得了state-of-the-art的性能。相较于现有方法，THCRL在聚类准确率和归一化互信息等指标上均有显著提升，证明了其在解决多视图聚类问题上的优越性。

## 🎯 应用场景

该研究成果可应用于图像聚类、视频分析、社交网络分析等领域。例如，在多模态图像聚类中，可以有效融合不同模态的信息，提高聚类准确率。在社交网络分析中，可以结合用户的多种社交行为信息，更准确地识别用户群体。

## 📄 摘要（原文）

> Multi-View Clustering (MVC) has garnered increasing attention in recent years. It is capable of partitioning data samples into distinct groups by learning a consensus representation. However, a significant challenge remains: the problem of untrustworthy fusion. This problem primarily arises from two key factors: 1) Existing methods often ignore the presence of inherent noise within individual views; 2) In traditional MVC methods using Contrastive Learning (CL), similarity computations typically rely on different views of the same instance, while neglecting the structural information from nearest neighbors within the same cluster. Consequently, this leads to the wrong direction for multi-view fusion. To address this problem, we present a novel Trusted Hierarchical Contrastive Representation Learning (THCRL). It consists of two key modules. Specifically, we propose the Deep Symmetry Hierarchical Fusion (DSHF) module, which leverages the UNet architecture integrated with multiple denoising mechanisms to achieve trustworthy fusion of multi-view data. Furthermore, we present the Average K-Nearest Neighbors Contrastive Learning (AKCL) module to align the fused representation with the view-specific representation. Unlike conventional strategies, AKCL enhances representation similarity among samples belonging to the same cluster, rather than merely focusing on the same sample across views, thereby reinforcing the confidence of the fused representation. Extensive experiments demonstrate that THCRL achieves the state-of-the-art performance in deep MVC tasks.

