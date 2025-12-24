---
layout: default
title: Small Lesions-aware Bidirectional Multimodal Multiscale Fusion Network for Lung Disease Classification
---

# Small Lesions-aware Bidirectional Multimodal Multiscale Fusion Network for Lung Disease Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04205" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04205v1</a>
  <a href="https://arxiv.org/pdf/2508.04205.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04205v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04205v1', 'Small Lesions-aware Bidirectional Multimodal Multiscale Fusion Network for Lung Disease Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianxun Yu, Ruiquan Ge, Zhipeng Wang, Cheng Yang, Chenyu Lin, Xianjun Fu, Jikui Liu, Ahmed Elazab, Changmiao Wang

**分类**: cs.CV

**发布日期**: 2025-08-06

**🔗 代码/项目**: [GITHUB](https://github.com/yjx1234/MMCAF-Net)

---

## 💡 一句话要点

**提出MMCAF-Net以解决小病灶误诊问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `小病灶识别` `多模态融合` `深度学习` `医学影像` `交叉注意力` `特征金字塔` `肺部疾病` `诊断准确率`

## 📋 核心要点

1. 现有医学影像诊断方法在小病灶的识别上存在误诊风险，影响临床决策。
2. 本文提出MMCAF-Net，通过特征金字塔和多尺度交叉注意力模块，有效提取和融合多模态数据特征。
3. 在Lung-PET-CT-Dx数据集上的实验结果表明，MMCAF-Net的诊断准确率显著高于现有方法。

## 📝 摘要（中文）

医学疾病的诊断面临小病灶误诊等挑战。深度学习，尤其是多模态方法，在医学疾病诊断中展现出巨大潜力。然而，医学影像与电子健康记录数据之间的维度差异给有效对齐和融合带来了困难。为了解决这些问题，本文提出了多模态多尺度交叉注意力融合网络（MMCAF-Net）。该模型采用特征金字塔结构，结合高效的3D多尺度卷积注意力模块，从3D医学图像中提取病灶特征。为了进一步增强多模态数据的整合，MMCAF-Net还引入了多尺度交叉注意力模块，解决了维度不一致的问题，从而实现更有效的特征融合。我们在Lung-PET-CT-Dx数据集上评估了MMCAF-Net，结果显示其诊断准确率显著提高，超越了当前的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决医学影像中小病灶的误诊问题，现有方法在处理多模态数据时面临维度不一致的挑战，导致特征融合效果不佳。

**核心思路**：论文提出的MMCAF-Net通过结合特征金字塔结构和多尺度交叉注意力模块，旨在有效提取和融合来自不同模态的特征，从而提高小病灶的识别准确性。

**技术框架**：MMCAF-Net的整体架构包括特征金字塔模块用于提取3D医学图像的特征，以及多尺度交叉注意力模块用于解决不同模态之间的维度不一致问题，最终实现特征的有效融合。

**关键创新**：MMCAF-Net的核心创新在于引入多尺度交叉注意力模块，解决了传统方法在多模态数据融合中的维度不一致问题，从而提升了特征融合的效果。

**关键设计**：模型设计中采用了特征金字塔结构以增强特征提取能力，损失函数设置为交叉熵损失，以优化分类性能，同时在网络结构中引入了3D卷积以适应医学影像的特性。

## 📊 实验亮点

在Lung-PET-CT-Dx数据集上的实验结果显示，MMCAF-Net的诊断准确率显著提高，超越了当前最先进的方法，具体性能提升幅度为XX%（具体数据未知）。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、肺部疾病的早期诊断和临床决策支持。通过提高小病灶的识别率，MMCAF-Net有助于改善患者的治疗效果，降低误诊率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The diagnosis of medical diseases faces challenges such as the misdiagnosis of small lesions. Deep learning, particularly multimodal approaches, has shown great potential in the field of medical disease diagnosis. However, the differences in dimensionality between medical imaging and electronic health record data present challenges for effective alignment and fusion. To address these issues, we propose the Multimodal Multiscale Cross-Attention Fusion Network (MMCAF-Net). This model employs a feature pyramid structure combined with an efficient 3D multi-scale convolutional attention module to extract lesion-specific features from 3D medical images. To further enhance multimodal data integration, MMCAF-Net incorporates a multi-scale cross-attention module, which resolves dimensional inconsistencies, enabling more effective feature fusion. We evaluated MMCAF-Net on the Lung-PET-CT-Dx dataset, and the results showed a significant improvement in diagnostic accuracy, surpassing current state-of-the-art methods. The code is available at https://github.com/yjx1234/MMCAF-Net

