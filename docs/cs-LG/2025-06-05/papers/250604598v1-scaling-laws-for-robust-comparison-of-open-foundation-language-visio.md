---
layout: default
title: Scaling Laws for Robust Comparison of Open Foundation Language-Vision Models and Datasets
---

# Scaling Laws for Robust Comparison of Open Foundation Language-Vision Models and Datasets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04598" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04598v1</a>
  <a href="https://arxiv.org/pdf/2506.04598.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04598v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04598v1', 'Scaling Laws for Robust Comparison of Open Foundation Language-Vision Models and Datasets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marianna Nezhurina, Tomer Porian, Giovanni Pucceti, Tommie Kerssies, Romain Beaumont, Mehdi Cherti, Jenia Jitsev

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-06-05

**备注**: Preprint. In Review

**🔗 代码/项目**: [GITHUB](https://github.com/LAION-AI/scaling-laws-for-comparison)

---

## 💡 一句话要点

**提出缩放法则以比较语言-视觉模型与数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `缩放法则` `模型比较` `多模态学习` `CLIP` `MaMMUT` `样本效率` `开放数据集` `预训练模型`

## 📋 核心要点

1. 现有方法在模型和数据集比较时缺乏系统性，容易导致误导性结论。
2. 本文提出通过缩放法则推导进行模型和数据集比较，确保预训练过程的选择更为合理。
3. 实验结果表明，MaMMUT在多个任务上表现优于CLIP，且在样本效率上具有显著提升。

## 📝 摘要（中文）

在可迁移学习研究中，缩放法则被用于预测基础模型在更大规模下的性能。本文首次基于密集测量推导出完整的缩放法则，比较了CLIP和MaMMUT两种语言-视觉学习方法，发现MaMMUT在规模和样本效率上优于标准CLIP。通过对多种下游任务和开放数据集的分析，验证了缩放法则的有效性，并提供了一种在恒定学习率下进行比较的方法，降低了计算成本。所有预训练模型及其中间检查点均已发布，推动了开放基础模型和数据集的系统比较与改进。

## 🔬 方法详解

**问题定义**：本文旨在解决现有模型和数据集比较方法的不足，特别是如何在不同规模下进行有效比较，以避免基于单一参考尺度的误导性结论。

**核心思路**：通过推导缩放法则，提供了一种系统化的比较框架，使得在不同规模下的模型和数据集性能能够被准确评估，从而指导预训练过程的选择。

**技术框架**：整体架构包括缩放法则的推导、模型性能的比较以及多种下游任务的验证。主要模块包括数据集选择、模型训练、性能评估和结果分析。

**关键创新**：首次在CLIP和MaMMUT模型上推导出完整的缩放法则，证明了MaMMUT在规模和样本效率上的优势，提供了新的比较方法。

**关键设计**：采用恒定学习率调度进行缩放法则推导，确保了计算成本的降低；在模型训练中使用对比损失和文本生成损失的组合，以提升模型性能。

## 📊 实验亮点

实验结果显示，openMaMMUT-L/14在ImageNet-1k的零-shot准确率达到了80.3%，在12.8B样本的训练下，表现出比标准CLIP更强的规模提升和样本效率，验证了缩放法则的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉和自然语言处理的交叉领域，尤其在多模态学习、模型选择和数据集构建方面具有重要价值。未来，基于缩放法则的比较方法可能推动更高效的模型设计和训练策略的开发。

## 📄 摘要（原文）

> In studies of transferable learning, scaling laws are obtained for various important foundation models to predict their properties and performance at larger scales. We show here how scaling law derivation can also be used for model and dataset comparison, allowing to decide which procedure is to be preferred for pre-training. For the first time, full scaling laws based on dense measurements across a wide span of model and samples seen scales are derived for two important language-vision learning procedures, CLIP and MaMMUT, that use either contrastive only or contrastive and captioning text generative loss. Ensuring sufficient prediction accuracy for held out points, we use derived scaling laws to compare both models, obtaining evidence for MaMMUT's stronger improvement with scale and better sample efficiency than standard CLIP. To strengthen validity of the comparison, we show scaling laws for various downstream tasks, classification, retrieval, and segmentation, and for different open datasets, DataComp, DFN and Re-LAION, observing consistently the same trends. We show that comparison can also be performed when deriving scaling laws with a constant learning rate schedule, reducing compute cost. Accurate derivation of scaling laws provides thus means to perform model and dataset comparison across scale spans, avoiding misleading conclusions based on measurements from single reference scales only, paving the road for systematic comparison and improvement of open foundation models and datasets for their creation. We release all the pre-trained models with their intermediate checkpoints, including openMaMMUT-L/14, which achieves $80.3\%$ zero-shot ImageNet-1k accuracy, trained on 12.8B samples from DataComp-1.4B. Code for reproducing experiments in the paper and raw experiments data can be found at https://github.com/LAION-AI/scaling-laws-for-comparison.

