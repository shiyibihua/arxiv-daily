---
layout: default
title: Evaluating New AI Cell Foundation Models on Challenging Kidney Pathology Cases Unaddressed by Previous Foundation Models
---

# Evaluating New AI Cell Foundation Models on Challenging Kidney Pathology Cases Unaddressed by Previous Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01287" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01287v1</a>
  <a href="https://arxiv.org/pdf/2510.01287.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01287v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01287v1', 'Evaluating New AI Cell Foundation Models on Challenging Kidney Pathology Cases Unaddressed by Previous Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Runchen Wang, Junlin Guo, Siqi Lu, Ruining Deng, Zhengyi Lu, Yanfan Zhu, Yuechen Yang, Chongyu Qu, Yu Wang, Shilin Zhao, Catie Chang, Mitchell Wilkes, Mengmeng Yin, Haichun Yang, Yuankai Huo

**分类**: q-bio.QM, cs.AI

**发布日期**: 2025-10-01

---

## 💡 一句话要点

**评估新型AI细胞分割模型在肾脏病理疑难案例中的性能，解决先前模型未解决的问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `细胞分割` `肾脏病理` `AI基础模型` `模型融合` `深度学习` `医学图像分析` `CellViT++`

## 📋 核心要点

1. 肾脏病理图像中细胞核分割面临形态多样性和成像差异的挑战，现有方法难以有效处理。
2. 论文评估了最新的AI细胞分割基础模型，并提出融合策略以提升疑难案例的分割精度。
3. 实验表明，CellViT++模型表现最佳，融合模型显著提升分割质量，尤其在疑难案例上。

## 📝 摘要（中文）

精确的细胞核分割对于肾脏病理学中的下游任务至关重要，但由于肾脏组织形态的多样性和成像的可变性，仍然是一个主要的挑战。虽然我们之前的工作已经评估了早期AI细胞基础模型在该领域的性能，但最近的细胞基础模型的有效性仍不清楚。在本研究中，我们使用包含大量肾脏图像块的多样化数据集，在一个人工参与的评估框架中，对包括CellViT++变体和Cellpose-SAM在内的先进AI细胞基础模型（2025）与2024年之前开发的三种广泛使用的细胞基础模型进行了基准测试。我们进一步进行了基于融合的集成评估和模型一致性分析，以评估不同模型的分割能力。结果表明，CellViT++ [Virchow] 产生了最高的独立性能，在精心策划的2,091个具有挑战性的样本集中，有40.3%的预测被评为“良好”，优于所有先前的模型。此外，我们的融合模型实现了62.2%的“良好”预测和仅0.4%的“差”预测，大大减少了分割错误。值得注意的是，融合模型（2025）成功解决了我们之前研究中未解决的大部分具有挑战性的案例。这些发现证明了AI细胞基础模型在肾脏病理学中开发的潜力，并提供了一个具有挑战性的样本的精选数据集，以支持未来特定于肾脏的模型改进。

## 🔬 方法详解

**问题定义**：论文旨在解决肾脏病理图像中细胞核分割的难题，特别是现有AI细胞分割模型在处理形态多样、成像差异大的肾脏组织时，分割精度不足的问题。现有方法的痛点在于对复杂病理图像的泛化能力较弱，容易出现分割错误，影响下游病理分析的准确性。

**核心思路**：论文的核心解决思路是评估和融合最新的AI细胞分割基础模型，利用不同模型的优势互补，从而提高对复杂肾脏病理图像的分割精度和鲁棒性。通过人工评估和模型一致性分析，筛选出表现优异的模型，并采用融合策略进一步提升性能。

**技术框架**：整体框架包括数据收集与预处理、模型选择与训练、人工评估与模型融合、以及结果分析与验证。主要模块包括：1) 基于大规模肾脏病理图像数据集训练的多个AI细胞分割模型；2) 人工参与的评估框架，用于对模型预测结果进行质量评估；3) 基于模型预测结果的融合策略，旨在结合不同模型的优势；4) 模型一致性分析，用于评估不同模型之间的预测一致性。

**关键创新**：论文的关键创新在于：1) 系统性地评估了最新的AI细胞分割基础模型在肾脏病理图像分割中的性能；2) 提出了基于融合的集成策略，有效提升了分割精度，尤其是在疑难案例上；3) 构建了一个包含大量具有挑战性的肾脏病理图像的精选数据集，为未来模型改进提供了基础。

**关键设计**：论文的关键设计包括：1) 选择了CellViT++和Cellpose-SAM等先进的AI细胞分割模型；2) 采用了人工参与的评估框架，确保评估结果的可靠性；3) 设计了基于模型预测结果的融合策略，例如加权平均或投票机制，以结合不同模型的优势；4) 针对肾脏病理图像的特点，可能采用了特定的数据增强方法或损失函数，以提高模型的泛化能力（具体细节未知）。

## 📊 实验亮点

实验结果表明，CellViT++ [Virchow] 在独立测试中表现最佳，在具有挑战性的样本集中达到了40.3%的“良好”预测率，优于所有先前的模型。更重要的是，融合模型实现了62.2%的“良好”预测和仅0.4%的“差”预测，显著减少了分割错误，并成功解决了之前研究中未解决的大部分疑难案例。这表明融合策略能够有效提升肾脏病理图像分割的精度和鲁棒性。

## 🎯 应用场景

该研究成果可应用于肾脏疾病的辅助诊断、病理分析和药物研发等领域。通过提高细胞核分割的准确性，可以帮助病理学家更准确地评估肾脏组织的病变程度，从而为患者提供更精准的治疗方案。此外，该研究构建的精选数据集可用于训练和评估新的肾脏病理图像分割模型，推动相关领域的发展。

## 📄 摘要（原文）

> Accurate cell nuclei segmentation is critical for downstream tasks in kidney pathology and remains a major challenge due to the morphological diversity and imaging variability of renal tissues. While our prior work has evaluated early-generation AI cell foundation models in this domain, the effectiveness of recent cell foundation models remains unclear. In this study, we benchmark advanced AI cell foundation models (2025), including CellViT++ variants and Cellpose-SAM, against three widely used cell foundation models developed prior to 2024, using a diverse large-scale set of kidney image patches within a human-in-the-loop rating framework. We further performed fusion-based ensemble evaluation and model agreement analysis to assess the segmentation capabilities of the different models. Our results show that CellViT++ [Virchow] yields the highest standalone performance with 40.3% of predictions rated as "Good" on a curated set of 2,091 challenging samples, outperforming all prior models. In addition, our fused model achieves 62.2% "Good" predictions and only 0.4% "Bad", substantially reducing segmentation errors. Notably, the fusion model (2025) successfully resolved the majority of challenging cases that remained unaddressed in our previous study. These findings demonstrate the potential of AI cell foundation model development in renal pathology and provide a curated dataset of challenging samples to support future kidney-specific model refinement.

