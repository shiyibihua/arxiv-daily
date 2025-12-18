---
layout: default
title: Generalist Multi-Class Anomaly Detection via Distillation to Two Heterogeneous Student Networks
---

# Generalist Multi-Class Anomaly Detection via Distillation to Two Heterogeneous Student Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24448" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24448v1</a>
  <a href="https://arxiv.org/pdf/2509.24448.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24448v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24448v1', 'Generalist Multi-Class Anomaly Detection via Distillation to Two Heterogeneous Student Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hangil Park, Yongmin Seo, Tae-Kyun Kim

**分类**: cs.CV

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出基于知识蒸馏的双异构学生网络，用于通用多类异常检测。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `异常检测` `知识蒸馏` `双模型集成` `通用异常检测` `多类异常检测`

## 📋 核心要点

1. 现有异常检测方法在工业和语义异常检测之间泛化性不足，且对数据集和单类任务敏感。
2. 利用知识蒸馏，构建双异构学生网络，分别针对工业和语义异常进行优化，提升泛化能力。
3. 实验结果表明，该方法在多个数据集上，单类和多类设置下均达到SOTA，显著提升了AUROC。

## 📝 摘要（中文）

异常检测(AD)在各种实际应用中扮演着重要角色。然而，目前AD的进展通常偏向于工业检测，难以推广到更广泛的任务，如语义异常检测，反之亦然。尽管最近的方法试图解决通用异常检测问题，但它们的性能仍然对数据集特定的设置和单类任务敏感。本文提出了一种基于知识蒸馏(KD)的新型双模型集成方法来弥合这一差距。我们的框架由一个教师模型和两个学生模型组成：一个擅长检测工业AD中patch级别微小缺陷的Encoder-Decoder模型和一个针对语义AD优化的Encoder-Encoder模型。两个模型都利用共享的预训练编码器(DINOv2)来提取高质量的特征表示。使用Noisy-OR目标联合学习双模型，并通过各自模型导出的局部和语义异常分数，使用联合概率获得最终的异常分数。我们在单类和多类设置下，在八个公共基准上评估了我们的方法：用于工业检测的MVTec-AD、MVTec-LOCO、VisA和Real-IAD，以及用于语义异常检测的CIFAR-10/100、FMNIST和View。所提出的方法在多类和单类设置下，在两个领域都实现了最先进的精度，证明了在异常检测的多个领域中的泛化能力。我们的模型在MVTec-AD上实现了99.7%的图像级AUROC，在CIFAR-10上实现了97.8%，明显优于之前的多类设置下的通用AD模型，甚至高于各个基准上最好的专家模型。

## 🔬 方法详解

**问题定义**：现有异常检测方法通常针对特定领域（如工业检测或语义异常检测）进行优化，缺乏通用性。此外，它们在处理多类异常检测问题时性能下降，对数据集的特定设置也较为敏感。因此，需要一种能够同时处理工业和语义异常，并且在多类场景下也能保持高性能的通用异常检测方法。

**核心思路**：论文的核心思路是利用知识蒸馏，将一个强大的教师模型（例如，预训练的DINOv2）的知识传递给两个异构的学生模型。这两个学生模型分别针对工业异常检测（patch级别缺陷）和语义异常检测进行优化。通过这种方式，可以使两个学生模型分别学习到不同领域的特征表示，从而提高整体的泛化能力。

**技术框架**：该框架包含一个教师模型和两个学生模型。教师模型通常是一个预训练的视觉模型，用于提取高质量的特征表示。两个学生模型分别是：1) Encoder-Decoder模型，专门用于检测工业异常中的patch级别缺陷；2) Encoder-Encoder模型，专门用于语义异常检测。两个学生模型共享教师模型的预训练编码器。训练过程中，使用Noisy-OR目标函数联合学习两个学生模型。最终的异常分数通过结合两个学生模型的输出得到，从而综合考虑局部和语义信息。

**关键创新**：该方法最重要的创新点在于使用了双异构学生网络结构，并结合知识蒸馏进行训练。这种结构允许模型同时学习到工业和语义异常的特征表示，从而提高了泛化能力。此外，使用Noisy-OR目标函数可以有效地融合两个学生模型的输出，从而提高整体的检测性能。

**关键设计**：关键设计包括：1) 使用DINOv2作为预训练的编码器，以提取高质量的特征表示；2) 设计Encoder-Decoder和Encoder-Encoder两种不同的学生网络结构，以分别适应工业和语义异常检测任务；3) 使用Noisy-OR目标函数，将两个学生模型的输出进行融合；4) 通过调整损失函数的权重，平衡两个学生模型的贡献。

## 📊 实验亮点

该方法在MVTec-AD数据集上取得了99.7%的图像级AUROC，在CIFAR-10数据集上取得了97.8%的图像级AUROC，显著优于现有的通用异常检测模型。在多类异常检测任务中，该方法也超越了专门针对单类异常检测的模型，证明了其优越的泛化能力。

## 🎯 应用场景

该研究成果可广泛应用于工业质检、医疗影像分析、自动驾驶等领域。在工业质检中，可用于检测产品表面的缺陷。在医疗影像分析中，可用于辅助医生诊断疾病。在自动驾驶中，可用于检测道路上的异常物体，提高行车安全性。该方法具有很高的实际应用价值和潜力。

## 📄 摘要（原文）

> Anomaly detection (AD) plays an important role in various real-world applications. Recent advancements in AD, however, are often biased towards industrial inspection, struggle to generalize to broader tasks like semantic anomaly detection and vice versa. Although recent methods have attempted to address general anomaly detection, their performance remains sensitive to dataset-specific settings and single-class tasks. In this paper, we propose a novel dual-model ensemble approach based on knowledge distillation (KD) to bridge this gap. Our framework consists of a teacher and two student models: an Encoder-Decoder model, specialized in detecting patch-level minor defects for industrial AD and an Encoder-Encoder model, optimized for semantic AD. Both models leverage a shared pre-trained encoder (DINOv2) to extract high-quality feature representations. The dual models are jointly learned using the Noisy-OR objective, and the final anomaly score is obtained using the joint probability via local and semantic anomaly scores derived from the respective models. We evaluate our method on eight public benchmarks under both single-class and multi-class settings: MVTec-AD, MVTec-LOCO, VisA and Real-IAD for industrial inspection and CIFAR-10/100, FMNIST and View for semantic anomaly detection. The proposed method achieved state-of-the-art accuracies in both domains, in multi-class as well as single-class settings, demonstrating generalization across multiple domains of anomaly detection. Our model achieved an image-level AUROC of 99.7% on MVTec-AD and 97.8% on CIFAR-10, which is significantly better than the prior general AD models in multi-class settings and even higher than the best specialist models on individual benchmarks.

