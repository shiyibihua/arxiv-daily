---
layout: default
title: Which Direction to Choose? An Analysis on the Representation Power of Self-Supervised ViTs in Downstream Tasks
---

# Which Direction to Choose? An Analysis on the Representation Power of Self-Supervised ViTs in Downstream Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15272" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15272v1</a>
  <a href="https://arxiv.org/pdf/2509.15272.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15272v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15272v1', 'Which Direction to Choose? An Analysis on the Representation Power of Self-Supervised ViTs in Downstream Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yannis Kaltampanidis, Alexandros Doumanoglou, Dimitrios Zarpalas

**分类**: cs.CV

**发布日期**: 2025-09-18

**备注**: 24 pages, XAI 2025

---

## 💡 一句话要点

**分析自监督ViT在下游任务中的表征能力，探究最优特征选择策略。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自监督学习` `Vision Transformer` `特征表征` `下游任务` `图像分类` `图像分割` `少样本学习` `预训练模型`

## 📋 核心要点

1. 现有方法通常对预训练ViT特征进行额外处理，缺乏对原始ViT特征内在表征能力的深入分析。
2. 本研究系统评估了未经修改的ViT特征在图像分类和分割任务中的性能，探索最优特征选择策略。
3. 实验结果揭示了不同token类型和决策规则在不同任务和预训练目标下的适用性，为ViT特征选择提供了指导。

## 📝 摘要（中文）

近年来，自监督学习(SSL)的Vision Transformer (ViT)作为一种预训练策略，在图像分类、分割等多种计算机视觉任务中展现出巨大潜力，尤其是在标准和少样本下游任务中。对比学习和掩码图像建模是SSL技术领域中的两种主要目标。从最终Transformer注意力块提取的特征（或tokens），特别是键(keys)、查询(queries)和值(values)，以及最终前馈层之后的特征，已成为解决下游任务的常见基础。然而，在许多现有方法中，这些预训练的ViT特征会通过额外的转换层进一步处理，通常涉及轻量级头部或与蒸馏结合，以实现卓越的任务性能。尽管这些方法可以改善任务结果，但据我们所知，尚未对未经修改的ViT特征的内在表征能力进行全面分析。本研究旨在通过在标准和少样本环境中，系统地评估这些未经修改的特征在图像分类和分割任务中的应用来弥补这一差距。我们使用的分类和分割规则是基于超平面的（如逻辑回归）或基于余弦相似度的，两者都依赖于ViT潜在空间中可解释方向的存在。基于上述规则，在不使用额外特征转换的情况下，我们对token类型、任务和预训练的ViT模型进行了分析。本研究深入了解了基于任务、上下文和预训练目标的最优token类型和决策规则选择，同时报告了两个广泛使用的数据集的详细发现。

## 🔬 方法详解

**问题定义**：现有方法在利用自监督学习预训练的ViT模型时，通常会添加额外的特征转换层（如轻量级头部或蒸馏）来提升下游任务的性能。然而，这种做法掩盖了原始ViT特征本身的表征能力，缺乏对不同ViT特征（如keys, queries, values）在不同任务下的适用性的系统研究。因此，需要研究未经修改的ViT特征在下游任务中的表现，从而更好地理解和利用ViT的内在表征能力。

**核心思路**：本研究的核心思路是直接利用预训练ViT模型提取的原始特征，而不进行额外的特征转换。通过系统地评估不同类型的ViT特征（keys, queries, values以及最终前馈层输出）在图像分类和分割任务中的表现，并结合不同的决策规则（基于超平面或余弦相似度），来分析不同特征的表征能力。这种方法旨在揭示不同特征在不同任务和预训练目标下的最优选择策略。

**技术框架**：整体框架包括以下几个步骤：1) 使用自监督学习方法（如对比学习或掩码图像建模）预训练ViT模型。2) 从预训练的ViT模型中提取不同类型的特征（keys, queries, values, feed-forward layer output）。3) 使用提取的特征进行下游任务的训练和评估，包括图像分类和分割。4) 采用不同的决策规则（基于超平面或余弦相似度）进行分类和分割。5) 对不同特征、任务和决策规则的组合进行系统性的实验分析，从而确定最优的特征选择策略。

**关键创新**：本研究的关键创新在于对未经修改的ViT特征的内在表征能力进行了系统性的分析。与现有方法不同，本研究避免了额外的特征转换，直接评估了原始ViT特征在下游任务中的表现。通过对比不同类型的特征和决策规则，揭示了不同特征在不同任务和预训练目标下的适用性，为ViT特征选择提供了新的视角。

**关键设计**：本研究的关键设计包括：1) 选择了两种常用的自监督学习方法（对比学习和掩码图像建模）进行ViT预训练。2) 提取了ViT模型中不同位置的特征，包括keys, queries, values以及最终前馈层输出。3) 采用了两种不同的决策规则：基于超平面的规则（如逻辑回归）和基于余弦相似度的规则。4) 在两个广泛使用的数据集上进行了实验，包括标准和少样本设置。通过这些设计，本研究能够全面地评估不同特征和决策规则的性能，并确定最优的特征选择策略。

## 📊 实验亮点

该研究通过实验发现，不同类型的ViT特征在不同任务和预训练目标下表现出不同的性能。例如，某些特征在图像分类任务中表现更好，而另一些特征在图像分割任务中更有效。此外，研究还发现，基于超平面的决策规则在某些情况下优于基于余弦相似度的规则，反之亦然。这些发现为ViT特征选择提供了重要的参考依据。

## 🎯 应用场景

该研究成果可应用于各种计算机视觉任务，如图像分类、目标检测、图像分割等。通过选择合适的ViT特征，可以提高下游任务的性能，尤其是在资源受限或需要快速部署的场景下。此外，该研究还有助于更好地理解ViT模型的内部机制，为未来的模型设计和优化提供指导。

## 📄 摘要（原文）

> Self-Supervised Learning (SSL) for Vision Transformers (ViTs) has recently demonstrated considerable potential as a pre-training strategy for a variety of computer vision tasks, including image classification and segmentation, both in standard and few-shot downstream contexts. Two pre-training objectives dominate the landscape of SSL techniques: Contrastive Learning and Masked Image Modeling. Features (or tokens) extracted from the final transformer attention block -- specifically, the keys, queries, and values -- as well as features obtained after the final block's feed-forward layer, have become a common foundation for addressing downstream tasks. However, in many existing approaches, these pre-trained ViT features are further processed through additional transformation layers, often involving lightweight heads or combined with distillation, to achieve superior task performance. Although such methods can improve task outcomes, to the best of our knowledge, a comprehensive analysis of the intrinsic representation capabilities of unaltered ViT features has yet to be conducted. This study aims to bridge this gap by systematically evaluating the use of these unmodified features across image classification and segmentation tasks, in both standard and few-shot contexts. The classification and segmentation rules that we use are either hyperplane based (as in logistic regression) or cosine-similarity based, both of which rely on the presence of interpretable directions in the ViT's latent space. Based on the previous rules and without the use of additional feature transformations, we conduct an analysis across token types, tasks, and pre-trained ViT models. This study provides insights into the optimal choice for token type and decision rule based on the task, context, and the pre-training objective, while reporting detailed findings on two widely-used datasets.

