---
layout: default
title: Transformers Can Learn Connectivity in Some Graphs but Not Others
---

# Transformers Can Learn Connectivity in Some Graphs but Not Others

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22343" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22343v1</a>
  <a href="https://arxiv.org/pdf/2509.22343.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22343v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22343v1', 'Transformers Can Learn Connectivity in Some Graphs but Not Others')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amit Roy, Abulhair Saparov

**分类**: cs.CL, cs.AI, cs.LG, cs.LO

**发布日期**: 2025-09-26

**备注**: Under Review

---

## 💡 一句话要点

**研究表明Transformer在网格状图上学习连通性，但在复杂图上存在困难**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Transformer` `图神经网络` `连通性` `传递关系` `图推理` `模型泛化` `网格图`

## 📋 核心要点

1. 现有研究缺乏对Transformer模型从训练样本中学习传递关系（图连通性）能力的深入探索，以及模型规模对该能力的影响。
2. 本文通过生成不同类型的有向图，训练不同规模的Transformer模型，研究其学习图连通性的能力。
3. 实验表明，Transformer擅长学习低维网格图的连通性，但难以处理高维或包含大量不连通组件的复杂图，且模型规模对网格图学习有积极影响。

## 📝 摘要（中文）

本研究探讨了Transformer模型学习有向图连通性的能力，这对于确保基于Transformer的大型语言模型（LLM）推理的正确性至关重要。以往研究主要关注Transformer通过上下文学习进行传递关系推理，而忽略了从训练样本中学习的能力以及模型规模的影响。本文通过生成不同大小的有向图来训练不同规模的Transformer模型，并评估其在不同图大小下推断传递关系的能力。研究发现，Transformer能够学习“网格状”有向图的连通性，其中每个节点可以嵌入到低维子空间中，并且连通性可以从节点的嵌入中轻松推断出来。网格图的维度是Transformer学习连通性任务能力的一个强预测指标，高维网格图比低维网格图更具挑战性。此外，增加模型规模可以更好地泛化到网格图上的连通性推断。然而，如果图不是网格图，并且包含许多不连通的组件，则Transformer很难学习连通性任务，尤其是在组件数量很大时。

## 🔬 方法详解

**问题定义**：论文旨在研究Transformer模型学习有向图连通性的能力。现有方法主要关注Transformer的上下文学习能力，忽略了其从训练数据中学习连通性的能力，以及模型规模对学习效果的影响。此外，现有研究缺乏对不同类型图结构下Transformer学习能力的系统性分析。

**核心思路**：论文的核心思路是通过控制图的结构，特别是图的维度和连通性，来研究Transformer模型学习连通性的能力。通过比较Transformer在不同类型图上的表现，揭示其学习连通性的内在机制和局限性。核心假设是Transformer更擅长学习具有规则结构的图，例如低维网格图。

**技术框架**：论文的技术框架主要包括以下几个步骤：1) 生成不同类型的有向图，包括网格图和随机图；2) 使用生成的图数据训练不同规模的Transformer模型；3) 评估训练后的Transformer模型在测试集上的连通性预测准确率；4) 分析模型规模、图结构和连通性预测准确率之间的关系。

**关键创新**：论文的关键创新在于系统性地研究了Transformer模型在不同类型图结构下学习连通性的能力。通过控制图的结构，揭示了Transformer模型更擅长学习具有规则结构的图，例如低维网格图。此外，论文还探讨了模型规模对学习效果的影响，发现增加模型规模可以提高在网格图上的泛化能力。

**关键设计**：论文的关键设计包括：1) 使用不同维度的网格图来控制图的结构；2) 使用随机图来模拟更复杂的图结构；3) 使用不同规模的Transformer模型来研究模型规模的影响；4) 使用准确率作为评估连通性预测性能的指标。

## 📊 实验亮点

实验结果表明，Transformer模型能够有效学习低维网格图的连通性，且模型规模越大，泛化能力越强。然而，在高维网格图和包含大量不连通组件的随机图上，Transformer模型的学习效果显著下降。这些发现揭示了Transformer模型在学习图结构化数据方面的局限性，并为未来的研究方向提供了指导。

## 🎯 应用场景

该研究成果可应用于提升大型语言模型在知识图谱推理、因果关系推断等任务中的能力。通过理解Transformer模型在不同图结构下的学习特性，可以设计更有效的训练策略和模型架构，从而提高LLM在复杂推理任务中的准确性和可靠性。此外，该研究对于开发更高效的图神经网络也具有一定的借鉴意义。

## 📄 摘要（原文）

> Reasoning capability is essential to ensure the factual correctness of the responses of transformer-based Large Language Models (LLMs), and robust reasoning about transitive relations is instrumental in many settings, such as causal inference. Hence, it is essential to investigate the capability of transformers in the task of inferring transitive relations (e.g., knowing A causes B and B causes C, then A causes C). The task of inferring transitive relations is equivalent to the task of connectivity in directed graphs (e.g., knowing there is a path from A to B, and there is a path from B to C, then there is a path from A to C). Past research focused on whether transformers can learn to infer transitivity from in-context examples provided in the input prompt. However, transformers' capability to infer transitive relations from training examples and how scaling affects the ability is unexplored. In this study, we seek to answer this question by generating directed graphs to train transformer models of varying sizes and evaluate their ability to infer transitive relations for various graph sizes. Our findings suggest that transformers are capable of learning connectivity on "grid-like'' directed graphs where each node can be embedded in a low-dimensional subspace, and connectivity is easily inferable from the embeddings of the nodes. We find that the dimensionality of the underlying grid graph is a strong predictor of transformers' ability to learn the connectivity task, where higher-dimensional grid graphs pose a greater challenge than low-dimensional grid graphs. In addition, we observe that increasing the model scale leads to increasingly better generalization to infer connectivity over grid graphs. However, if the graph is not a grid graph and contains many disconnected components, transformers struggle to learn the connectivity task, especially when the number of components is large.

