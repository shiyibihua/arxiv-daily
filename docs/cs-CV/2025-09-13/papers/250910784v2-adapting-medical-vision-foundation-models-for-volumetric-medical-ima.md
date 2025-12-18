---
layout: default
title: Adapting Medical Vision Foundation Models for Volumetric Medical Image Segmentation via Active Learning and Selective Semi-supervised Fine-tuning
---

# Adapting Medical Vision Foundation Models for Volumetric Medical Image Segmentation via Active Learning and Selective Semi-supervised Fine-tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10784" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10784v2</a>
  <a href="https://arxiv.org/pdf/2509.10784.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10784v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10784v2', 'Adapting Medical Vision Foundation Models for Volumetric Medical Image Segmentation via Active Learning and Selective Semi-supervised Fine-tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jin Yang, Daniel S. Marcus, Aristeidis Sotiras

**分类**: eess.IV, cs.CV

**发布日期**: 2025-09-13 (更新: 2025-10-21)

**备注**: 17 pages, 5 figures, 8 tables

---

## 💡 一句话要点

**提出ASFDA方法，通过主动学习和选择性半监督微调，高效适配医学视觉基础模型进行医学图像分割。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学图像分割` `主动学习` `半监督学习` `领域自适应` `医学视觉基础模型`

## 📋 核心要点

1. 现有方法随机选择样本微调医学视觉基础模型，效率低，无法保证目标域的最佳性能。
2. ASFDA方法通过主动学习选择信息量大的样本，并结合选择性半监督微调，提升模型在目标域的分割性能。
3. 该方法设计了DKD和ASD两种查询指标，分别衡量源-目标知识差距和解剖分割难度，指导样本选择。

## 📝 摘要（中文）

医学视觉基础模型(Med-VFMs)由于通过大量未标注图像的自监督预训练学习到的知识，具有卓越的医学图像理解能力。为了提高它们在自适应下游评估（尤其是分割）中的性能，通常会随机选择目标领域的一些样本进行微调。然而，目前缺乏探索如何高效地调整Med-VFMs以在目标领域上实现最佳性能的工作。因此，迫切需要设计一种有效的微调Med-VFMs的方法，通过选择信息量大的样本来最大化它们在目标领域上的适应性能。为了实现这一目标，我们提出了一种主动无源域自适应(ASFDA)方法，以有效地将Med-VFMs适应于目标领域的体积医学图像分割。该ASFDA采用了一种新颖的主动学习(AL)方法，从目标领域中选择信息量最大的样本来微调Med-VFMs，而无需访问源预训练样本，从而以最小的选择预算最大化它们的性能。在该AL方法中，我们设计了一种主动测试时样本查询策略，通过两个查询指标从目标域中选择样本，包括多样化知识散度(DKD)和解剖分割难度(ASD)。DKD旨在衡量源-目标知识差距和域内多样性。它利用预训练的知识来指导从目标域中查询源不相似和语义多样的样本。ASD旨在通过自适应地测量前景区域的预测熵来评估解剖结构分割的难度。此外，我们的ASFDA方法采用选择性半监督微调，通过识别未查询样本中具有高可靠性的样本来提高微调的性能和效率。

## 🔬 方法详解

**问题定义**：论文旨在解决医学视觉基础模型(Med-VFMs)在特定目标域的医学图像分割任务中，如何高效地进行模型适配的问题。现有方法通常采用随机选择样本进行微调，但这种方法忽略了样本的信息量差异，导致微调效率低下，且无法保证模型在目标域上的最佳性能。现有方法的痛点在于缺乏一种有效的样本选择策略，以最小的标注代价实现模型性能的最大化提升。

**核心思路**：论文的核心思路是通过主动学习(Active Learning)来选择信息量最大的样本进行微调，并结合选择性半监督微调来进一步提升性能和效率。主动学习能够从目标域中挑选出对模型学习最有帮助的样本，从而减少标注成本，提高微调效率。选择性半监督微调则利用未标注样本中置信度高的预测结果，进一步增强模型的泛化能力。

**技术框架**：ASFDA方法主要包含以下几个阶段：
1. **主动测试时样本查询(Active Test Time Sample Query)**：利用DKD和ASD两种查询指标，从目标域中选择信息量最大的样本。
2. **模型微调(Fine-tuning)**：使用主动学习选择的样本对Med-VFMs进行微调。
3. **选择性半监督微调(Selective Semi-supervised Fine-tuning)**：从剩余未标注样本中选择置信度高的样本，与已标注样本一起进行半监督微调。

**关键创新**：该方法最重要的技术创新点在于提出了结合多样化知识散度(DKD)和解剖分割难度(ASD)的主动学习样本选择策略。DKD用于衡量源域和目标域之间的知识差距以及目标域内部的多样性，确保选择的样本既能弥补知识差距，又能覆盖目标域的多种情况。ASD则用于评估解剖结构分割的难度，优先选择难以分割的样本，从而提高模型对复杂结构的分割能力。

**关键设计**：
* **多样化知识散度(DKD)**：具体计算方法未知，但其目的是选择与源域差异大且语义多样的样本。
* **解剖分割难度(ASD)**：通过自适应地测量前景区域的预测熵来评估分割难度，熵越高表示分割越困难。
* **选择性半监督微调**：具体选择标准未知，但其目的是选择预测置信度高的未标注样本。

## 📊 实验亮点

论文提出了ASFDA方法，通过主动学习和选择性半监督微调，有效提升了医学视觉基础模型在目标域的分割性能。虽然具体实验数据未知，但该方法在降低标注成本、提高微调效率方面具有显著优势，有望在实际应用中取得良好效果。与随机选择样本的微调方法相比，ASFDA方法能够更有效地利用有限的标注资源，实现更高的分割精度。

## 🎯 应用场景

该研究成果可广泛应用于医学图像分析领域，例如疾病诊断、手术规划和疗效评估。通过高效地适配医学视觉基础模型，可以降低标注成本，提高分割精度，从而辅助医生进行更准确、更快速的诊断和治疗。未来，该方法有望推广到其他医学图像模态和临床应用场景。

## 📄 摘要（原文）

> Medical Vision Foundation Models (Med-VFMs) have superior capabilities of interpreting medical images due to the knowledge learned from self-supervised pre-training with extensive unannotated images. To improve their performance on adaptive downstream evaluations, especially segmentation, a few samples from target domains are selected randomly for fine-tuning them. However, there lacks works to explore the way of adapting Med-VFMs to achieve the optimal performance on target domains efficiently. Thus, it is highly demanded to design an efficient way of fine-tuning Med-VFMs by selecting informative samples to maximize their adaptation performance on target domains. To achieve this, we propose an Active Source-Free Domain Adaptation (ASFDA) method to efficiently adapt Med-VFMs to target domains for volumetric medical image segmentation. This ASFDA employs a novel Active Learning (AL) method to select the most informative samples from target domains for fine-tuning Med-VFMs without the access to source pre-training samples, thus maximizing their performance with the minimal selection budget. In this AL method, we design an Active Test Time Sample Query strategy to select samples from the target domains via two query metrics, including Diversified Knowledge Divergence (DKD) and Anatomical Segmentation Difficulty (ASD). DKD is designed to measure the source-target knowledge gap and intra-domain diversity. It utilizes the knowledge of pre-training to guide the querying of source-dissimilar and semantic-diverse samples from the target domains. ASD is designed to evaluate the difficulty in segmentation of anatomical structures by measuring predictive entropy from foreground regions adaptively. Additionally, our ASFDA method employs a Selective Semi-supervised Fine-tuning to improve the performance and efficiency of fine-tuning by identifying samples with high reliability from unqueried ones.

