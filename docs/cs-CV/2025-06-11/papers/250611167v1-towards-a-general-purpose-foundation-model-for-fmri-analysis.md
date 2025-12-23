---
layout: default
title: Towards a general-purpose foundation model for fMRI analysis
---

# Towards a general-purpose foundation model for fMRI analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11167" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11167v1</a>
  <a href="https://arxiv.org/pdf/2506.11167.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11167v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11167v1', 'Towards a general-purpose foundation model for fMRI analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheng Wang, Yu Jiang, Zhihao Peng, Chenxin Li, Changbae Bang, Lin Zhao, Jinglei Lv, Jorge Sepulcre, Carl Yang, Lifang He, Tianming Liu, Daniel Barron, Quanzheng Li, Randy Hirschtick, Byung-Hoon Kim, Xiang Li, Yixuan Yuan

**分类**: cs.CV, cs.LG

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出NeuroSTORM以解决fMRI分析的可重复性与迁移性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `功能性磁共振成像` `神经影像` `基础模型` `时空优化` `迁移学习` `临床研究` `数据预处理`

## 📋 核心要点

1. 现有fMRI分析方法面临可重复性和迁移性问题，主要由于复杂的预处理和任务特定模型。
2. NeuroSTORM框架通过直接学习4D fMRI体积，结合时空优化预训练和任务特定提示调优，提升了模型的迁移能力。
3. 在多个任务上，NeuroSTORM超越了现有方法，尤其在临床数据集上表现出色，提升了疾病诊断和认知表型预测的准确性。

## 📝 摘要（中文）

功能性磁共振成像（fMRI）在研究大脑功能和诊断神经疾病中至关重要，但现有分析方法因复杂的预处理和任务特定模型而面临可重复性和迁移性问题。我们提出了NeuroSTORM（神经影像基础模型与时空优化表示建模），这是一个可泛化的框架，能够直接从4D fMRI体积中学习，并在多种应用中实现高效的知识迁移。NeuroSTORM在来自50,000多名受试者的2865万帧fMRI数据上进行预训练，展示了在年龄/性别预测、表型预测、疾病诊断等五个任务中的优越性能，尤其在疾病诊断和认知表型预测方面表现突出。

## 🔬 方法详解

**问题定义**：论文旨在解决fMRI分析中现有方法的可重复性和迁移性不足的问题。现有方法通常依赖复杂的预处理和特定任务的模型，导致在不同应用场景中的效果不佳。

**核心思路**：NeuroSTORM通过构建一个可泛化的框架，直接从4D fMRI数据中学习，旨在实现高效的知识迁移。该方法结合了时空优化的预训练策略和任务特定的提示调优，以提高模型在不同任务中的表现。

**技术框架**：NeuroSTORM的整体架构包括数据预处理、时空优化的预训练、任务特定的提示调优和最终的模型评估。使用Mamba骨干网络和移位扫描策略，能够高效处理完整的4D体积数据。

**关键创新**：NeuroSTORM的主要创新在于其时空优化的预训练方法和任务特定的提示调优，这些设计使得模型能够在多种任务中实现更好的迁移能力，显著提升了分析的准确性和效率。

**关键设计**：在模型设计中，NeuroSTORM采用了特定的损失函数和网络结构，以适应4D fMRI数据的特点。同时，使用了大规模的多中心数据集进行预训练，确保模型的泛化能力。

## 📊 实验亮点

NeuroSTORM在五个任务上均超越了现有方法，尤其在疾病诊断和认知表型预测中表现突出。在来自美国、韩国和澳大利亚的临床数据集上，模型达到了最佳性能，显示出显著的临床实用性。

## 🎯 应用场景

该研究的潜在应用领域包括神经科学研究、临床诊断和个性化医疗。通过提供一个标准化的开源基础模型，NeuroSTORM能够促进fMRI相关临床研究的可重复性和迁移性，推动大脑疾病的早期诊断和治疗策略的制定。

## 📄 摘要（原文）

> Functional Magnetic Resonance Imaging (fMRI) is essential for studying brain function and diagnosing neurological disorders, but current analysis methods face reproducibility and transferability issues due to complex pre-processing and task-specific models. We introduce NeuroSTORM (Neuroimaging Foundation Model with Spatial-Temporal Optimized Representation Modeling), a generalizable framework that directly learns from 4D fMRI volumes and enables efficient knowledge transfer across diverse applications. NeuroSTORM is pre-trained on 28.65 million fMRI frames (>9,000 hours) from over 50,000 subjects across multiple centers and ages 5 to 100. Using a Mamba backbone and a shifted scanning strategy, it efficiently processes full 4D volumes. We also propose a spatial-temporal optimized pre-training approach and task-specific prompt tuning to improve transferability. NeuroSTORM outperforms existing methods across five tasks: age/gender prediction, phenotype prediction, disease diagnosis, fMRI-to-image retrieval, and task-based fMRI classification. It demonstrates strong clinical utility on datasets from hospitals in the U.S., South Korea, and Australia, achieving top performance in disease diagnosis and cognitive phenotype prediction. NeuroSTORM provides a standardized, open-source foundation model to improve reproducibility and transferability in fMRI-based clinical research.

