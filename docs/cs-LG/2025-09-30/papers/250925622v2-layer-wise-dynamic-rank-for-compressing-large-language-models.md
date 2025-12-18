---
layout: default
title: Layer-wise dynamic rank for compressing large language models
---

# Layer-wise dynamic rank for compressing large language models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25622" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25622v2</a>
  <a href="https://arxiv.org/pdf/2509.25622.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25622v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25622v2', 'Layer-wise dynamic rank for compressing large language models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhendong Mi, Bian Sun, Grace Li Zhang, Shaoyi Huang

**分类**: cs.LG

**发布日期**: 2025-09-30 (更新: 2025-10-04)

**备注**: 10 pages, 5 figures

---

## 💡 一句话要点

**提出D-Rank：一种层级动态秩分配框架，用于压缩大型语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型压缩` `奇异值分解` `动态秩分配` `模型优化` `后训练压缩`

## 📋 核心要点

1. 现有SVD压缩方法对LLM各层采用统一压缩率，忽略了层间信息密度差异，导致压缩效率受限。
2. D-Rank通过有效秩度量信息密度，并基于拉格朗日乘数优化，动态分配各层压缩秩，提升压缩性能。
3. 实验表明，D-Rank在多种LLM上优于现有方法，显著降低困惑度，提高零样本推理精度和吞吐量。

## 📝 摘要（中文）

大型语言模型(LLMs)的规模迅速扩大，带来了严重的内存和计算挑战，阻碍了它们的部署。基于奇异值分解(SVD)的压缩已成为一种有吸引力的LLM后训练压缩技术，但大多数现有方法在所有层上应用统一的压缩率，隐含地假设不同层中包含同质信息。这忽略了LLM中观察到的显著的层内异质性，其中中间层倾向于编码更丰富的信息，而早期和后期层则更加冗余。在这项工作中，我们重新审视了现有的基于SVD的压缩方法，并提出了D-Rank，一个具有层级平衡动态秩分配的LLM压缩框架。我们首先引入有效秩作为一种原则性度量来衡量权重矩阵的信息密度，然后通过基于拉格朗日乘数的优化方案来分配秩，以便在固定的压缩率下自适应地为具有更高信息密度的组分配更多容量。此外，我们重新平衡注意力层之间分配的秩，以考虑它们不同的重要性，并将D-Rank扩展到具有分组查询注意力的最新LLM。在具有不同规模的各种LLM上，跨多个压缩率进行的大量实验表明，D-Rank始终优于SVD-LLM、ASVD和Basis Sharing，在C4数据集上以20%的压缩率使用LLaMA-3-8B模型实现了超过15的更低困惑度，并且在40%的压缩率下使用LLaMA-7B模型实现了高达5%的更高的零样本推理精度，同时实现了更高的吞吐量。

## 🔬 方法详解

**问题定义**：现有基于SVD的LLM压缩方法通常采用统一的压缩率，忽略了LLM不同层之间信息密度的差异。这种均匀压缩策略导致信息密度高的层压缩不足，而信息冗余的层过度压缩，从而影响整体性能。现有方法无法有效利用LLM各层之间的异质性，导致压缩效率低下。

**核心思路**：D-Rank的核心思路是根据LLM各层的信息密度动态地分配压缩秩。通过引入“有效秩”这一指标来衡量权重矩阵的信息密度，并利用拉格朗日乘数优化算法，在满足整体压缩率约束的前提下，为信息密度更高的层分配更多的秩，从而更有效地保留模型的重要信息。

**技术框架**：D-Rank框架主要包含以下几个阶段：1) **有效秩计算**：计算LLM每一层权重矩阵的有效秩，作为信息密度的度量。2) **秩分配优化**：利用拉格朗日乘数法，在给定整体压缩率约束下，优化各层的秩分配方案，使得信息密度高的层获得更多的秩。3) **秩重平衡**：针对注意力层，根据其重要性重新平衡分配的秩。4) **SVD压缩**：根据优化后的秩分配方案，对每一层进行SVD分解和压缩。

**关键创新**：D-Rank最重要的技术创新点在于提出了层级动态秩分配的思想，并将其应用于LLM的压缩。与现有方法采用的统一压缩率不同，D-Rank能够根据各层的信息密度自适应地调整压缩率，从而更有效地保留模型的重要信息，提高压缩性能。此外，D-Rank还考虑了注意力层的重要性差异，并对其进行了秩重平衡。

**关键设计**：D-Rank的关键设计包括：1) **有效秩的计算方法**：论文中具体描述了有效秩的计算公式，该公式能够有效地反映权重矩阵的信息密度。2) **拉格朗日乘数优化**：论文详细介绍了如何利用拉格朗日乘数法求解秩分配优化问题，并给出了具体的优化算法。3) **注意力层秩重平衡策略**：论文提出了针对注意力层的秩重平衡策略，该策略能够根据注意力层的重要性调整其秩分配。

## 📊 实验亮点

实验结果表明，D-Rank在各种LLM上均优于现有压缩方法。例如，在C4数据集上，使用LLaMA-3-8B模型，D-Rank在20%的压缩率下实现了超过15的更低困惑度。在使用LLaMA-7B模型时，D-Rank在40%的压缩率下实现了高达5%的更高的零样本推理精度。此外，D-Rank还能够提高模型的吞吐量。

## 🎯 应用场景

D-Rank技术可广泛应用于各种需要部署大型语言模型的场景，例如移动设备、边缘计算设备和资源受限的服务器。通过有效压缩模型大小，D-Rank能够降低部署成本，提高推理速度，并使LLM能够在更多平台上运行。该技术对于推动LLM在实际应用中的普及具有重要意义。

## 📄 摘要（原文）

> Large language models (LLMs) have rapidly scaled in size, bringing severe memory and computational challenges that hinder their deployment. Singular Value Decomposition (SVD)-based compression has emerged as an appealing post-training compression technique for LLMs, yet most existing methods apply a uniform compression ratio across all layers, implicitly assuming homogeneous information included in various layers. This overlooks the substantial intra-layer heterogeneity observed in LLMs, where middle layers tend to encode richer information while early and late layers are more redundant. In this work, we revisit the existing SVD-based compression method and propose D-Rank, a framework with layer-wise balanced Dynamic Rank allocation for LLMs compression. We first introduce effective rank as a principled metric to measure the information density of weight matrices, and then allocate ranks via a Lagrange multiplier-based optimization scheme to adaptively assign more capacity to groups with higher information density under a fixed compression ratio. Moreover, we rebalance the allocated ranks across attention layers to account for their varying importance and extend D-Rank to latest LLMs with grouped-query attention. Extensive experiments on various LLMs with different scales across multiple compression ratios demonstrate that D-Rank consistently outperforms SVD-LLM, ASVD, and Basis Sharing, achieving more than 15 lower perplexity with LLaMA-3-8B model on C4 datasets at 20% compression ratio and up to 5% higher zero-shot reasoning accuracy with LLaMA-7B model at 40% compression ratio while achieving even higher throughput.

