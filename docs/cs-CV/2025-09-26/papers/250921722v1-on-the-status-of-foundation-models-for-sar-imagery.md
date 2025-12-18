---
layout: default
title: On the Status of Foundation Models for SAR Imagery
---

# On the Status of Foundation Models for SAR Imagery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21722" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21722v1</a>
  <a href="https://arxiv.org/pdf/2509.21722.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21722v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21722v1', 'On the Status of Foundation Models for SAR Imagery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nathan Inkawhich

**分类**: cs.CV, eess.IV

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**探索SAR图像的Foundation Model：自监督微调DINOv2实现目标识别新SOTA**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `SAR图像` `目标识别` `自监督学习` `Foundation Model` `DINOv2` `迁移学习` `合成孔径雷达` `深度学习`

## 📋 核心要点

1. 现有视觉基础模型在SAR图像目标识别中表现不佳，无法直接提取有效的语义特征。
2. 采用自监督学习微调策略，利用SAR数据对现有SSL模型进行适配，提升特征提取能力。
3. AFRL-DINOv2在SAR目标识别任务上取得了显著的性能提升，超越了当前最佳SAR领域模型。

## 📝 摘要（中文）

本文研究了基础AI/ML模型在合成孔径雷达(SAR)目标识别任务中的可行性。受到自然图像领域巨大进展的启发，该领域通过自监督学习(SSL)在网络规模数据集上训练大型模型。这些模型能够以极少的标注数据进行下游任务适配，对分布偏移更具鲁棒性，且特征具有高度可迁移性。本文首先评估了DINOv2、DINOv3和PE-Core等视觉基础模型在SAR图像上的表现，发现它们在提取语义相关的SAR目标特征方面存在不足。然后，通过对公开的SSL模型进行SAR数据自监督微调，验证了AFRL-DINOv2的可行性，并建立了新的SAR基础模型SOTA，显著优于现有最佳SAR领域模型SARATR-X。实验进一步分析了不同骨干网络与下游任务适配方案的性能权衡，并监测了模型在下游环境中克服挑战的能力。希望这项工作能够为未来的SAR基础模型构建者提供参考。

## 🔬 方法详解

**问题定义**：论文旨在解决SAR图像目标识别问题，现有方法依赖大量标注数据，泛化能力弱，且难以适应复杂的操作环境。直接应用自然图像领域预训练的视觉基础模型，无法有效提取SAR图像的语义特征，导致识别精度较低。

**核心思路**：论文的核心思路是利用自监督学习(SSL)的预训练模型，通过在SAR数据集上进行微调，使模型能够学习到SAR图像特有的特征表示。这种方法旨在利用大规模无标注SAR数据，提升模型在少量标注数据下的性能，并增强模型的泛化能力。

**技术框架**：整体框架包括以下几个阶段：1) 选择合适的视觉基础模型（如DINOv2）；2) 利用公开的SAR数据集进行自监督微调，训练AFRL-DINOv2模型；3) 在下游SAR目标识别任务上评估微调后的模型性能；4) 分析不同骨干网络和下游任务适配方案的性能权衡。

**关键创新**：关键创新在于将自监督学习的预训练模型成功应用于SAR图像领域，并通过微调显著提升了SAR目标识别的性能。此外，论文还系统地分析了不同骨干网络和下游任务适配方案对性能的影响，为后续研究提供了指导。

**关键设计**：论文的关键设计包括：1) 选择DINOv2作为基础模型，因为它在自然图像领域表现出色，具有良好的特征提取能力；2) 使用自监督学习方法进行微调，以充分利用无标注SAR数据；3) 设计合理的下游任务适配方案，以最大化模型的性能。

## 📊 实验亮点

实验结果表明，经过SAR数据自监督微调的AFRL-DINOv2模型在SAR目标识别任务上取得了显著的性能提升，超越了当前最佳SAR领域模型SARATR-X，建立了新的SOTA。这验证了自监督学习在SAR图像领域的有效性，为后续研究提供了有力的支持。

## 🎯 应用场景

该研究成果可应用于军事侦察、灾害监测、环境监测、资源勘探等领域。通过提升SAR图像目标识别的精度和效率，可以更快速、准确地获取目标信息，为决策提供支持。未来，该技术有望应用于自动驾驶、智能交通等领域，实现全天候、全天时的感知能力。

## 📄 摘要（原文）

> In this work we investigate the viability of foundational AI/ML models for Synthetic Aperture Radar (SAR) object recognition tasks. We are inspired by the tremendous progress being made in the wider community, particularly in the natural image domain where frontier labs are training huge models on web-scale datasets with unprecedented computing budgets. It has become clear that these models, often trained with Self-Supervised Learning (SSL), will transform how we develop AI/ML solutions for object recognition tasks - they can be adapted downstream with very limited labeled data, they are more robust to many forms of distribution shift, and their features are highly transferable out-of-the-box. For these reasons and more, we are motivated to apply this technology to the SAR domain. In our experiments we first run tests with today's most powerful visual foundational models, including DINOv2, DINOv3 and PE-Core and observe their shortcomings at extracting semantically-interesting discriminative SAR target features when used off-the-shelf. We then show that Self-Supervised finetuning of publicly available SSL models with SAR data is a viable path forward by training several AFRL-DINOv2s and setting a new state-of-the-art for SAR foundation models, significantly outperforming today's best SAR-domain model SARATR-X. Our experiments further analyze the performance trade-off of using different backbones with different downstream task-adaptation recipes, and we monitor each model's ability to overcome challenges within the downstream environments (e.g., extended operating conditions and low amounts of labeled data). We hope this work will inform and inspire future SAR foundation model builders, because despite our positive results, we still have a long way to go.

