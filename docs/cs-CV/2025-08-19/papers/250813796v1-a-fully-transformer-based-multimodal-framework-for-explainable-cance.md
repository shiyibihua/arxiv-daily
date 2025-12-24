---
layout: default
title: A Fully Transformer Based Multimodal Framework for Explainable Cancer Image Segmentation Using Radiology Reports
---

# A Fully Transformer Based Multimodal Framework for Explainable Cancer Image Segmentation Using Radiology Reports

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13796" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13796v1</a>
  <a href="https://arxiv.org/pdf/2508.13796.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13796v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13796v1', 'A Fully Transformer Based Multimodal Framework for Explainable Cancer Image Segmentation Using Radiology Reports')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Enobong Adahada, Isabel Sassoon, Kate Hone, Yongmin Li

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出Med-CTX以解决乳腺癌超声图像分割的可解释性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `可解释性` `医学图像分割` `深度学习` `变换器` `临床文本` `超声图像` `计算机辅助诊断`

## 📋 核心要点

1. 现有的医学图像分割方法在可解释性和性能上存在不足，尤其是在乳腺癌超声图像的处理上。
2. 论文提出的Med-CTX框架通过结合临床放射学报告和双分支视觉编码器，提升了分割的精确性和可解释性。
3. 在BUS-BRA数据集上，Med-CTX的Dice得分达到99%，IoU为95%，显著超越了U-Net、ViT和Swin等基线模型。

## 📝 摘要（中文）

我们介绍了Med-CTX，这是一种完全基于变换器的多模态框架，用于可解释的乳腺癌超声分割。通过整合临床放射学报告，Med-CTX在性能和可解释性上均有所提升。该框架采用双分支视觉编码器，结合ViT和Swin变换器，以及不确定性感知融合，实现了精确的病灶描绘。临床语言通过BioClinicalBERT进行编码，并利用跨模态注意力与视觉特征结合，使模型能够提供临床基础的生成解释。我们的研究同时生成分割掩膜、不确定性图和诊断理由，增强了计算机辅助诊断的信心和透明度。在BUS-BRA数据集上，Med-CTX的Dice得分达到99%，IoU为95%，超越了现有的基线模型U-Net、ViT和Swin。临床文本在分割精度和解释质量中起到了关键作用，消融研究表明，缺少临床文本会导致Dice得分下降5.4%，CIDEr下降31%。Med-CTX实现了良好的多模态对齐（CLIP得分：85%）和增强的置信度校准（ECE：3.2%），为可信赖的多模态医学架构设定了新的标准。

## 🔬 方法详解

**问题定义**：本论文旨在解决乳腺癌超声图像分割中的可解释性问题。现有方法往往缺乏对临床背景的理解，导致分割结果难以解释和信任。

**核心思路**：Med-CTX通过整合临床放射学报告与视觉信息，利用双分支视觉编码器和跨模态注意力机制，提升了分割的精度和可解释性。

**技术框架**：该框架包括双分支视觉编码器（结合ViT和Swin变换器）、BioClinicalBERT用于编码临床文本，以及不确定性感知融合模块，整体流程为：输入图像和文本 → 特征提取 → 跨模态融合 → 生成分割掩膜和解释。

**关键创新**：最重要的创新在于将临床文本与视觉特征的结合，通过跨模态注意力机制实现了更高的分割精度和可解释性。这一设计使得模型能够生成基于临床的解释，区别于传统方法。

**关键设计**：模型使用的损失函数包括分割损失和不确定性损失，网络结构采用双分支设计，确保视觉特征和文本特征的有效融合。

## 📊 实验亮点

Med-CTX在BUS-BRA数据集上取得了显著的性能，Dice得分达到99%，IoU为95%，超越了U-Net、ViT和Swin等现有基线模型。此外，消融研究表明，缺少临床文本会导致Dice得分下降5.4%，CIDEr下降31%，显示出临床文本在模型中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、计算机辅助诊断和个性化医疗。通过提供可解释的分割结果，Med-CTX能够帮助医生更好地理解和信任模型的决策，从而提高临床诊断的效率和准确性。未来，该框架有望扩展到其他类型的医学图像分析任务中。

## 📄 摘要（原文）

> We introduce Med-CTX, a fully transformer based multimodal framework for explainable breast cancer ultrasound segmentation. We integrate clinical radiology reports to boost both performance and interpretability. Med-CTX achieves exact lesion delineation by using a dual-branch visual encoder that combines ViT and Swin transformers, as well as uncertainty aware fusion. Clinical language structured with BI-RADS semantics is encoded by BioClinicalBERT and combined with visual features utilising cross-modal attention, allowing the model to provide clinically grounded, model generated explanations. Our methodology generates segmentation masks, uncertainty maps, and diagnostic rationales all at once, increasing confidence and transparency in computer assisted diagnosis. On the BUS-BRA dataset, Med-CTX achieves a Dice score of 99% and an IoU of 95%, beating existing baselines U-Net, ViT, and Swin. Clinical text plays a key role in segmentation accuracy and explanation quality, as evidenced by ablation studies that show a -5.4% decline in Dice score and -31% in CIDEr. Med-CTX achieves good multimodal alignment (CLIP score: 85%) and increased confi dence calibration (ECE: 3.2%), setting a new bar for trustworthy, multimodal medical architecture.

