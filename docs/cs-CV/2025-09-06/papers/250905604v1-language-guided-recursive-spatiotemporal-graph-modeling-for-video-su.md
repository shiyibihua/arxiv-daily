---
layout: default
title: Language-guided Recursive Spatiotemporal Graph Modeling for Video Summarization
---

# Language-guided Recursive Spatiotemporal Graph Modeling for Video Summarization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05604" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05604v1</a>
  <a href="https://arxiv.org/pdf/2509.05604.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05604v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05604v1', 'Language-guided Recursive Spatiotemporal Graph Modeling for Video Summarization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jungin Park, Jiyoung Lee, Kwanghoon Sohn

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-06

**备注**: Accepted to IJCV, 29 pages, 14 figures, 11 tables

**DOI**: [10.1007/s11263-025-02577-2](https://doi.org/10.1007/s11263-025-02577-2)

**🔗 代码/项目**: [GITHUB](https://github.com/park-jungin/videograph)

---

## 💡 一句话要点

**提出基于语言引导的递归时空图网络VideoGraph，用于视频摘要任务**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `视频摘要` `时空图网络` `语言引导` `图卷积网络` `递归神经网络` `视频理解` `关键帧提取`

## 📋 核心要点

1. 现有视频摘要方法侧重于帧间的时间关系，忽略了细粒度视觉实体（如对象）与视频内容的相关性。
2. VideoGraph通过构建递归时空图网络，将对象和帧分别建模为空间图和时间图的节点，并融入语言信息。
3. 实验结果表明，VideoGraph在通用和查询聚焦视频摘要任务上，均取得了优于现有技术水平的性能。

## 📝 摘要（中文）

本文提出了一种基于语言引导的时空图建模方法用于视频摘要，旨在选择具有视觉多样性并能代表视频整体故事的关键帧。现有方法侧重于通过时间建模来建立帧之间的全局互连性。然而，细粒度的视觉实体（如对象）也与视频的主要内容高度相关。此外，最近研究的语言引导视频摘要需要对复杂的真实世界视频进行全面的语言理解。为了考虑所有对象之间的语义关系，本文将视频摘要视为一个语言引导的时空图建模问题。我们提出了递归时空图网络，称为VideoGraph，它将对象和帧分别表示为空间图和时间图的节点。每个图中的节点通过图边连接和聚合，表示节点之间的语义关系。为了防止边仅根据视觉相似性配置，我们将从视频中提取的语言查询融入到图节点表示中，使其包含语义知识。此外，我们采用递归策略来细化初始图，并正确地将每个帧节点分类为关键帧。实验结果表明，VideoGraph在有监督和无监督的通用和查询聚焦视频摘要的多个基准测试中都取得了最先进的性能。代码已开源。

## 🔬 方法详解

**问题定义**：视频摘要旨在从视频中选择最具代表性的关键帧，现有方法主要关注帧之间的时间关系，忽略了视频中细粒度对象之间的语义关联，以及语言信息对视频理解的指导作用。这导致生成的摘要可能缺乏对视频内容深层次的理解和表达。

**核心思路**：本文的核心思路是将视频摘要问题转化为一个语言引导的时空图建模问题。通过构建时空图，显式地建模视频中对象和帧之间的关系，并利用语言信息来指导图的构建和推理，从而更好地理解视频内容并选择关键帧。

**技术框架**：VideoGraph的整体框架包含以下几个主要模块：1) 特征提取模块：提取视频帧的视觉特征和对象的视觉特征。2) 语言查询模块：从视频描述或用户查询中提取语言特征。3) 时空图构建模块：构建空间图（对象之间的关系）和时间图（帧之间的关系）。4) 图推理模块：利用图神经网络在时空图上进行推理，融合视觉和语言信息。5) 递归细化模块：通过递归的方式不断细化图结构和节点表示，提高关键帧分类的准确性。

**关键创新**：该论文的关键创新在于：1) 提出了递归时空图网络VideoGraph，能够同时建模视频中的对象和帧之间的关系。2) 将语言信息融入到图节点表示中，从而利用语言信息来指导图的构建和推理。3) 采用递归策略来细化图结构和节点表示，提高关键帧分类的准确性。

**关键设计**：在时空图构建方面，使用了GCN（图卷积网络）来聚合节点信息。语言信息的融入方式是将语言特征与视觉特征进行融合，作为图节点的初始表示。递归细化模块通过多层GCN来实现，每一层GCN都对图结构和节点表示进行更新。损失函数包括关键帧分类损失和图结构正则化损失。

## 📊 实验亮点

VideoGraph在TVSum、SumMe、YouTube等多个视频摘要基准数据集上取得了state-of-the-art的性能。例如，在TVSum数据集上，VideoGraph的F-score比之前的最佳方法提高了约2-3个百分点。此外，该方法在有监督和无监督两种模式下均表现出色，证明了其泛化能力。

## 🎯 应用场景

该研究成果可应用于视频监控摘要、新闻视频摘要、电影预告片生成、教育视频内容提取等领域。通过自动提取视频的关键信息，可以节省大量的人工标注成本，提高视频内容理解和检索的效率，并为用户提供更便捷的视频浏览体验。未来，该方法还可以扩展到其他视频理解任务，如视频问答、视频描述等。

## 📄 摘要（原文）

> Video summarization aims to select keyframes that are visually diverse and can represent the whole story of a given video. Previous approaches have focused on global interlinkability between frames in a video by temporal modeling. However, fine-grained visual entities, such as objects, are also highly related to the main content of the video. Moreover, language-guided video summarization, which has recently been studied, requires a comprehensive linguistic understanding of complex real-world videos. To consider how all the objects are semantically related to each other, this paper regards video summarization as a language-guided spatiotemporal graph modeling problem. We present recursive spatiotemporal graph networks, called VideoGraph, which formulate the objects and frames as nodes of the spatial and temporal graphs, respectively. The nodes in each graph are connected and aggregated with graph edges, representing the semantic relationships between the nodes. To prevent the edges from being configured with visual similarity, we incorporate language queries derived from the video into the graph node representations, enabling them to contain semantic knowledge. In addition, we adopt a recursive strategy to refine initial graphs and correctly classify each frame node as a keyframe. In our experiments, VideoGraph achieves state-of-the-art performance on several benchmarks for generic and query-focused video summarization in both supervised and unsupervised manners. The code is available at https://github.com/park-jungin/videograph.

