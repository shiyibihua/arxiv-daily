---
layout: default
title: Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training
---

# Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13996" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13996v1</a>
  <a href="https://arxiv.org/pdf/2512.13996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13996v1" onclick="toggleFavorite(this, '2512.13996v1', 'Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Can Jin, Hongwu Peng, Mingcan Xiang, Qixin Zhang, Xiangchi Yuan, Amit Hasan, Ohiremen Dibua, Yifan Gong, Yan Kang, Dimitris N. Metaxas

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出DTop-p MoE，实现稀疏性可控的动态Top-p路由，提升大模型预训练效果。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `MoE` `Top-p路由` `动态稀疏性` `PI控制器` `大模型预训练` `Transformer` `路由归一化`

## 📋 核心要点

1. 现有Top-k MoE路由策略稀疏性固定，忽略了token难度的差异，而固定阈值的Top-p路由计算成本不可控且对超参数敏感。
2. DTop-p MoE利用PI控制器动态调整Top-p概率阈值，使激活专家稀疏性与目标对齐，并引入动态路由归一化以适应不同层的专家选择。
3. 实验表明，DTop-p在大型语言模型和扩散Transformer上优于Top-k和固定阈值Top-p，并展现出良好的缩放特性。

## 📝 摘要（中文）

稀疏混合专家(MoE)架构通过仅激活每个输入token的专家子集来有效地扩展模型容量。然而，标准的Top-k路由策略施加了一种统一的稀疏模式，忽略了token难度的变化。虽然Top-p路由提供了一种灵活的替代方案，但现有的实现通常依赖于固定的全局概率阈值，这导致了不可控的计算成本和对超参数选择的敏感性。本文提出了DTop-p MoE，一种稀疏性可控的动态Top-p路由机制。为了解决优化不可微阈值的挑战，我们利用比例-积分(PI)控制器动态调整概率阈值，使运行激活的专家稀疏性与指定的target对齐。此外，我们引入了一种动态路由归一化机制，该机制自适应地调整层级的路由logits，允许不同的层学习不同的专家选择模式，同时使用全局概率阈值。在大型语言模型和扩散Transformer上的大量实验表明，DTop-p始终优于Top-k和固定阈值Top-p基线。我们的分析证实，DTop-p保持对激活专家数量的精确控制，同时自适应地在不同的token和层之间分配资源。此外，DTop-p在专家粒度、专家容量、模型大小和数据集大小方面表现出强大的缩放特性，为大规模MoE预训练提供了一个鲁棒的框架。

## 🔬 方法详解

**问题定义**：现有MoE模型中的Top-k路由策略对所有token采用相同的稀疏度，无法根据token的难易程度动态调整计算资源分配。而Top-p路由虽然可以自适应地选择专家，但现有方法依赖于固定的全局概率阈值，导致计算开销难以控制，且对超参数的选择非常敏感。这限制了MoE模型在大规模预训练中的应用。

**核心思路**：DTop-p MoE的核心思路是通过一个比例-积分(PI)控制器动态地调整Top-p路由中的概率阈值，从而实现对激活专家数量的精确控制。同时，引入动态路由归一化机制，允许不同层学习不同的专家选择模式，从而更好地适应不同层的特征分布。

**技术框架**：DTop-p MoE的整体框架包括以下几个主要模块：1) 路由logits生成：与传统MoE类似，通过一个路由网络为每个token生成针对不同专家的logits。2) 动态Top-p选择：使用PI控制器动态调整概率阈值，根据logits选择Top-p的专家。3) 动态路由归一化：自适应地调整层级的路由logits，允许不同层学习不同的专家选择模式。4) 专家计算：被选中的专家对token进行处理。5) 结果融合：将不同专家的输出进行加权融合。

**关键创新**：DTop-p MoE的关键创新在于：1) 提出了一种基于PI控制器的动态Top-p路由机制，实现了对激活专家数量的精确控制，解决了固定阈值Top-p路由计算开销不可控的问题。2) 引入了动态路由归一化机制，允许不同层学习不同的专家选择模式，提高了模型的灵活性和适应性。

**关键设计**：1) PI控制器的设计：PI控制器根据当前激活专家数量与目标数量的差值，动态调整概率阈值。2) 动态路由归一化：通过学习一个缩放因子来调整每一层的路由logits，使得不同层可以学习到不同的专家选择模式。3) 损失函数：除了常规的预训练损失外，还可以添加辅助损失来鼓励专家之间的负载均衡。

## 📊 实验亮点

实验结果表明，DTop-p MoE在大型语言模型和扩散Transformer上均优于Top-k和固定阈值Top-p基线。DTop-p能够精确控制激活专家数量，并自适应地在不同token和层之间分配计算资源。此外，DTop-p在专家粒度、专家容量、模型大小和数据集大小方面表现出强大的缩放特性。

## 🎯 应用场景

DTop-p MoE可应用于大规模语言模型、视觉Transformer等模型的预训练，尤其适用于计算资源受限的场景。通过动态控制稀疏性，可以在保证模型性能的同时，降低计算成本，加速模型训练。该方法还可用于模型压缩和知识蒸馏等领域，提升模型效率。

## 📄 摘要（原文）

> Sparse Mixture-of-Experts (MoE) architectures effectively scale model capacity by activating only a subset of experts for each input token. However, the standard Top-k routing strategy imposes a uniform sparsity pattern that ignores the varying difficulty of tokens. While Top-p routing offers a flexible alternative, existing implementations typically rely on a fixed global probability threshold, which results in uncontrolled computational costs and sensitivity to hyperparameter selection. In this paper, we propose DTop-p MoE, a sparsity-controllable dynamic Top-p routing mechanism. To resolve the challenge of optimizing a non-differentiable threshold, we utilize a Proportional-Integral (PI) Controller that dynamically adjusts the probability threshold to align the running activated-expert sparsity with a specified target. Furthermore, we introduce a dynamic routing normalization mechanism that adapts layer-wise routing logits, allowing different layers to learn distinct expert-selection patterns while utilizing a global probability threshold. Extensive experiments on Large Language Models and Diffusion Transformers demonstrate that DTop-p consistently outperforms both Top-k and fixed-threshold Top-p baselines. Our analysis confirms that DTop-p maintains precise control over the number of activated experts while adaptively allocating resources across different tokens and layers. Furthermore, DTop-p exhibits strong scaling properties with respect to expert granularity, expert capacity, model size, and dataset size, offering a robust framework for large-scale MoE pre-training.

