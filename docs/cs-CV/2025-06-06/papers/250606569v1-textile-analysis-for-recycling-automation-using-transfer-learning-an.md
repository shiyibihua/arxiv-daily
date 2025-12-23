---
layout: default
title: Textile Analysis for Recycling Automation using Transfer Learning and Zero-Shot Foundation Models
---

# Textile Analysis for Recycling Automation using Transfer Learning and Zero-Shot Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06569" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06569v1</a>
  <a href="https://arxiv.org/pdf/2506.06569.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06569v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06569v1', 'Textile Analysis for Recycling Automation using Transfer Learning and Zero-Shot Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yannis Spyridis, Vasileios Argyriou

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-06

**期刊**: IEEE DCOSS IoTi5 2025

---

## 💡 一句话要点

**提出基于迁移学习和零样本模型的纺织品回收自动化分析方法**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `纺织品回收` `迁移学习` `零样本学习` `计算机视觉` `自动化分拣` `深度学习` `特征分割`

## 📋 核心要点

1. 现有方法在纺织品回收中面临材料成分识别和污染物检测的准确性挑战，限制了自动化分拣的效率。
2. 本文提出了一种利用标准RGB图像进行纺织品分类和非纺织特征分割的自动化系统，采用迁移学习和零样本模型。
3. 实验结果显示，EfficientNetB0在分类任务中达到了81.25%的准确率，而零样本分割方法的mIoU达到了0.90，显著提升了性能。

## 📝 摘要（中文）

自动化分拣对提高纺织品回收的效率和可扩展性至关重要，但从传感器数据中准确识别材料成分和检测污染物仍然具有挑战性。本文探讨了使用标准RGB图像作为一种经济有效的传感方式，在自动化系统中进行关键预处理任务。我们设计了计算机视觉组件，旨在在传送带设置中执行四种常见纺织品类型的分类和非纺织特征（如纽扣和拉链）的分割。通过迁移学习和交叉验证评估了多种预训练架构，EfficientNetB0在保留的测试集上取得了81.25%的最佳准确率。对于特征分割，采用了结合Grounding DINO开放词汇检测器与Segment Anything Model (SAM)的零样本方法，生成的掩码与真实值的mIoU达到了0.90，表现出色。此研究展示了结合现代深度学习技术的RGB图像在自动化纺织品回收管道中进行关键分析步骤的可行性。

## 🔬 方法详解

**问题定义**：本文旨在解决纺织品回收过程中材料成分识别和污染物检测的准确性问题。现有方法在处理传感器数据时，往往无法有效区分不同类型的纺织品和非纺织特征，导致自动化分拣效率低下。

**核心思路**：论文提出利用标准RGB图像作为传感器数据，通过迁移学习进行纺织品分类，并结合零样本学习方法进行特征分割，以提高自动化系统的准确性和效率。这样的设计旨在降低成本，同时保持高性能。

**技术框架**：整体架构包括两个主要模块：一是基于迁移学习的分类模块，使用EfficientNetB0架构进行四种常见纺织品的分类；二是基于零样本学习的分割模块，结合Grounding DINO和Segment Anything Model (SAM)进行非纺织特征的分割。

**关键创新**：本研究的创新点在于将迁移学习与零样本学习相结合，利用RGB图像进行纺织品分类和特征分割，突破了传统方法在材料识别和污染物检测上的局限性。

**关键设计**：在分类任务中，采用EfficientNetB0作为基础网络，通过迁移学习进行微调，优化了模型的准确性。在分割任务中，使用Grounding DINO进行开放词汇检测，结合SAM生成高质量的分割掩码，确保了mIoU的高达0.90。

## 📊 实验亮点

实验结果显示，EfficientNetB0在分类任务中达到了81.25%的准确率，显著优于其他预训练模型。同时，结合Grounding DINO和SAM的零样本分割方法在特征分割任务中实现了0.90的mIoU，展现了极高的性能和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括纺织品回收行业的自动化分拣系统，能够有效提高回收效率和降低人工成本。通过实现高精度的材料识别和污染物检测，未来可能推动更广泛的可持续发展实践，促进循环经济的发展。

## 📄 摘要（原文）

> Automated sorting is crucial for improving the efficiency and scalability of textile recycling, but accurately identifying material composition and detecting contaminants from sensor data remains challenging. This paper investigates the use of standard RGB imagery, a cost-effective sensing modality, for key pre-processing tasks in an automated system. We present computer vision components designed for a conveyor belt setup to perform (a) classification of four common textile types and (b) segmentation of non-textile features such as buttons and zippers. For classification, several pre-trained architectures were evaluated using transfer learning and cross-validation, with EfficientNetB0 achieving the best performance on a held-out test set with 81.25\% accuracy. For feature segmentation, a zero-shot approach combining the Grounding DINO open-vocabulary detector with the Segment Anything Model (SAM) was employed, demonstrating excellent performance with a mIoU of 0.90 for the generated masks against ground truth. This study demonstrates the feasibility of using RGB images coupled with modern deep learning techniques, including transfer learning for classification and foundation models for zero-shot segmentation, to enable essential analysis steps for automated textile recycling pipelines.

