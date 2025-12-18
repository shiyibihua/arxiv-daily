---
layout: default
title: Building a General SimCLR Self-Supervised Foundation Model Across Neurological Diseases to Advance 3D Brain MRI Diagnoses
---

# Building a General SimCLR Self-Supervised Foundation Model Across Neurological Diseases to Advance 3D Brain MRI Diagnoses

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10620" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10620v1</a>
  <a href="https://arxiv.org/pdf/2509.10620.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10620v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10620v1', 'Building a General SimCLR Self-Supervised Foundation Model Across Neurological Diseases to Advance 3D Brain MRI Diagnoses')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Emily Kaczmarek, Justin Szeto, Brennan Nichyporuk, Tal Arbel

**分类**: cs.CV, cs.LG

**发布日期**: 2025-09-12

**备注**: Accepted to ICCV 2025 Workshop CVAMD

**🔗 代码/项目**: [GITHUB](https://github.com/emilykaczmarek/3D-Neuro-SimCLR)

---

## 💡 一句话要点

**构建通用SimCLR自监督脑MRI基础模型，提升3D脑部疾病诊断**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自监督学习` `3D脑MRI` `SimCLR` `基础模型` `神经系统疾病`

## 📋 核心要点

1. 现有深度学习模型在3D脑MRI分析中表现出潜力，但通常针对特定任务定制，泛化能力有限，且依赖大量标注数据。
2. 论文提出基于SimCLR的自监督学习框架，利用大量未标注的脑MRI数据进行预训练，构建通用的3D脑MRI基础模型。
3. 实验结果表明，该模型在多种下游任务中优于其他模型，即使在少量标注数据下也能有效预测阿尔茨海默病。

## 📝 摘要（中文）

本研究提出了一种通用的、高分辨率的基于SimCLR的自监督学习（SSL）基础模型，用于3D脑部结构磁共振成像（MRI）。该模型在包含11个公开数据集的18759名患者（44958个扫描）上进行了预训练，这些数据集涵盖了多种神经系统疾病。研究将该模型与掩码自编码器（MAE）以及两个监督学习基线模型在四个不同的下游预测任务中进行了比较，包括同分布和异分布设置。结果表明，经过微调的SimCLR模型在所有任务中均优于其他模型。值得注意的是，即使仅使用20%的标记训练样本来预测阿尔茨海默病，该模型仍然表现出色。代码和数据已公开，训练好的模型已发布在https://github.com/emilykaczmarek/3D-Neuro-SimCLR，为临床脑MRI分析提供了一个广泛适用且易于访问的基础模型。

## 🔬 方法详解

**问题定义**：现有3D脑MRI分析的深度学习模型通常针对特定任务设计，缺乏跨任务和跨人群的泛化能力。此外，标注数据的获取成本高昂，限制了模型的性能提升。因此，如何利用大量未标注的3D脑MRI数据构建通用的、高性能的基础模型是一个关键问题。

**核心思路**：论文的核心思路是利用自监督学习（SSL）方法，特别是SimCLR框架，从未标注的3D脑MRI数据中学习通用的表征。通过对比学习，模型能够学习到对不同神经系统疾病具有区分性的特征，从而提高在各种下游任务中的性能。

**技术框架**：整体框架包括两个主要阶段：预训练阶段和微调阶段。在预训练阶段，使用SimCLR框架从未标注的3D脑MRI数据中学习表征。具体来说，对每个3D脑MRI扫描进行两次随机数据增强，然后通过编码器网络提取特征向量。通过对比学习损失函数，使来自同一扫描的不同增强视图的特征向量尽可能接近，而来自不同扫描的特征向量尽可能远离。在微调阶段，使用少量标注数据对预训练的编码器网络进行微调，以适应特定的下游任务。

**关键创新**：该论文的关键创新在于构建了一个通用的、高分辨率的3D脑MRI基础模型，该模型在包含多种神经系统疾病的大规模数据集上进行了预训练。与现有的3D脑MRI基础模型相比，该模型具有更高的分辨率、更广的应用范围和更好的可访问性。此外，该研究还验证了该模型在多种下游任务中的有效性，证明了其泛化能力。

**关键设计**：论文使用了SimCLR框架，并针对3D脑MRI数据进行了优化。具体来说，使用了3D卷积神经网络作为编码器网络，并采用了多种数据增强方法，例如随机旋转、缩放和裁剪。对比学习损失函数采用了InfoNCE损失，并设置了合适的温度参数。此外，为了提高模型的泛化能力，使用了权重衰减和dropout等正则化技术。

## 📊 实验亮点

实验结果表明，经过微调的SimCLR模型在所有四个下游任务中均优于其他模型，包括MAE和两个监督学习基线。例如，在阿尔茨海默病预测任务中，即使仅使用20%的标记训练样本进行微调，SimCLR模型仍然取得了优异的性能。这表明该模型具有很强的泛化能力和数据效率。

## 🎯 应用场景

该研究成果可广泛应用于神经系统疾病的诊断、预后和治疗监测。通过使用该基础模型，可以减少对大量标注数据的依赖，加速新疾病的诊断模型开发，并提高现有模型的性能。该模型还可以用于研究不同神经系统疾病之间的关联，以及开发个性化的治疗方案。未来，该模型有望成为临床脑MRI分析的重要工具。

## 📄 摘要（原文）

> 3D structural Magnetic Resonance Imaging (MRI) brain scans are commonly acquired in clinical settings to monitor a wide range of neurological conditions, including neurodegenerative disorders and stroke. While deep learning models have shown promising results analyzing 3D MRI across a number of brain imaging tasks, most are highly tailored for specific tasks with limited labeled data, and are not able to generalize across tasks and/or populations. The development of self-supervised learning (SSL) has enabled the creation of large medical foundation models that leverage diverse, unlabeled datasets ranging from healthy to diseased data, showing significant success in 2D medical imaging applications. However, even the very few foundation models for 3D brain MRI that have been developed remain limited in resolution, scope, or accessibility. In this work, we present a general, high-resolution SimCLR-based SSL foundation model for 3D brain structural MRI, pre-trained on 18,759 patients (44,958 scans) from 11 publicly available datasets spanning diverse neurological diseases. We compare our model to Masked Autoencoders (MAE), as well as two supervised baselines, on four diverse downstream prediction tasks in both in-distribution and out-of-distribution settings. Our fine-tuned SimCLR model outperforms all other models across all tasks. Notably, our model still achieves superior performance when fine-tuned using only 20% of labeled training samples for predicting Alzheimer's disease. We use publicly available code and data, and release our trained model at https://github.com/emilykaczmarek/3D-Neuro-SimCLR, contributing a broadly applicable and accessible foundation model for clinical brain MRI analysis.

