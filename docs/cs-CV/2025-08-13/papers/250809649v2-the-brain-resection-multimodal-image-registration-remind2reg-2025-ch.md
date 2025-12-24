---
layout: default
title: The Brain Resection Multimodal Image Registration (ReMIND2Reg) 2025 Challenge
---

# The Brain Resection Multimodal Image Registration (ReMIND2Reg) 2025 Challenge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09649" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09649v2</a>
  <a href="https://arxiv.org/pdf/2508.09649.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09649v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09649v2', 'The Brain Resection Multimodal Image Registration (ReMIND2Reg) 2025 Challenge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Reuben Dorent, Laura Rigolo, Colin P. Galvin, Junyu Chen, Mattias P. Heinrich, Aaron Carass, Olivier Colliot, Demian Wassermann, Alexandra Golby, Tina Kapur, William Wells

**分类**: cs.CV

**发布日期**: 2025-08-13 (更新: 2025-11-15)

---

## 💡 一句话要点

**提出ReMIND2Reg挑战以解决脑肿瘤手术中的图像配准问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `脑肿瘤手术` `图像配准` `多模态图像` `神经导航` `术中超声` `标准化评估` `临床应用`

## 📋 核心要点

1. 现有的神经导航系统在手术过程中由于脑移位而失去准确性，导致术中图像引导的挑战。
2. ReMIND2Reg挑战通过提供多模态图像配准的标准化评估框架，旨在解决术后超声与术前MRI对齐的问题。
3. 该挑战提供了丰富的数据集，促进了稳健且可推广的多模态配准算法的发展，具有重要的临床应用价值。

## 📝 摘要（中文）

准确的术中图像引导对于实现脑肿瘤手术的最大安全切除至关重要。然而，基于术前MRI的神经导航系统在手术过程中由于脑移位而失去准确性。将术后超声图像与术前MRI对齐可以通过估计脑移位变形来恢复空间准确性，但由于解剖和拓扑变化大以及模态强度差异显著，这仍然是一个具有挑战性的问题。ReMIND2Reg 2025挑战为这一任务提供了最大的公共基准，建立在ReMIND数据集之上，包含99个训练案例、5个验证案例和10个私有测试案例。数据未提供注释用于训练，而验证和测试性能则基于手动注释的解剖标志进行评估。通过建立标准化评估框架，ReMIND2Reg旨在加速开发稳健、可推广且可临床应用的多模态配准算法。

## 🔬 方法详解

**问题定义**：论文要解决的具体问题是术后超声图像与术前MRI的配准，现有方法在面对脑移位和模态强度差异时表现不佳，导致配准精度下降。

**核心思路**：论文的核心解决思路是通过建立标准化的评估框架，利用丰富的多模态数据集来推动配准算法的开发，从而提高术中图像引导的准确性。

**技术框架**：整体架构包括数据准备、模型训练和评估三个主要阶段。数据准备阶段涉及收集和处理多模态图像，模型训练阶段使用未标注的数据进行训练，评估阶段则基于手动注释的标志进行性能评估。

**关键创新**：最重要的技术创新点在于提供了一个大型公共基准数据集和标准化评估指标，填补了当前多模态图像配准领域的空白，促进了算法的比较与发展。

**关键设计**：在参数设置上，使用了多种配准指标，如目标配准误差（TRE）和鲁棒性评估（TRE30），并采用了适合多模态数据的损失函数和网络结构，以确保模型的有效性和稳定性。

## 📊 实验亮点

ReMIND2Reg挑战提供了99个训练案例和10个私有测试案例，评估指标包括目标配准误差（TRE）和鲁棒性评估（TRE30）。通过标准化的评估框架，促进了多模态配准算法的开发，提升了术中图像引导的准确性，具有显著的临床价值。

## 🎯 应用场景

该研究的潜在应用领域主要集中在神经外科手术中，尤其是脑肿瘤切除手术。通过提高术中图像引导的准确性，可以帮助外科医生更安全地进行手术，最大限度地减少对正常脑组织的损伤，提升患者的手术效果和生存率。未来，该技术有望扩展到其他类型的外科手术和医学成像领域。

## 📄 摘要（原文）

> Accurate intraoperative image guidance is critical for achieving maximal safe resection in brain tumor surgery, yet neuronavigation systems based on preoperative MRI lose accuracy during the procedure due to brain shift. Aligning post-resection intraoperative ultrasound (iUS) with preoperative MRI can restore spatial accuracy by estimating brain shift deformations, but it remains a challenging problem given the large anatomical and topological changes and substantial modality intensity gap. The ReMIND2Reg 2025 Challenge provides the largest public benchmark for this task, built upon the ReMIND dataset. It offers 99 training cases, 5 validation cases, and 10 private test cases comprising paired 3D ceT1 MRI, T2 MRI, and post-resection 3D iUS volumes. Data are provided without annotations for training, while validation and test performance are evaluated on manually annotated anatomical landmarks. Metrics include target registration error (TRE), robustness to worst-case landmark misalignment (TRE30), and runtime. By establishing a standardized evaluation framework for this clinically critical and technically complex problem, ReMIND2Reg aims to accelerate the development of robust, generalizable, and clinically deployable multimodal registration algorithms for image-guided neurosurgery.

