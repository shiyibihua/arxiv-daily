---
layout: default
title: MMIS-Net for Retinal Fluid Segmentation and Detection
---

# MMIS-Net for Retinal Fluid Segmentation and Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13936" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13936v1</a>
  <a href="https://arxiv.org/pdf/2508.13936.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13936v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13936v1', 'MMIS-Net for Retinal Fluid Segmentation and Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nchongmaje Ndipenocha, Alina Mirona, Kezhi Wanga, Yongmin Li

**分类**: eess.IV, cs.CV

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出MMIS-Net以解决视网膜液体分割与检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学图像分割` `深度学习` `多模态融合` `相似性融合` `一热标签` `液体检测` `模型泛化`

## 📋 核心要点

1. 现有医学图像分割与检测方法多依赖单一数据源，忽视了多模态数据的协同效应，导致性能受限。
2. 提出MMIS-Net算法，通过相似性融合模块和一热标签空间，提升不同数据集间的特征融合与类一致性。
3. 在RETOUCH大挑战隐藏测试集上，MMIS-Net在液体分割任务中取得了0.83的Dice系数，液体检测任务的曲线下面积为1，表现优异。

## 📝 摘要（中文）

本研究旨在利用深度学习方法提升医学图像中疾病的分割与检测效果。现有方法通常在单一数据源、模态、器官或疾病类型上进行训练和测试，未能充分利用多种注释数据的协同潜力。为此，我们提出了一种新算法MMIS-Net（多模态医学图像分割网络），通过相似性融合模块实现特征图的融合，并创建了一种一热标签空间以处理不同数据集间的类不一致性。MMIS-Net在涵盖19个器官和2种模态的10个数据集上进行训练，评估结果显示其在RETOUCH大挑战隐藏测试集上超越了大型基础模型和其他最先进算法，液体分割任务的Dice系数达到0.83，液体检测任务的曲线下面积达到1。

## 🔬 方法详解

**问题定义**：本研究旨在解决医学图像中液体分割与检测的挑战，现有方法往往在单一数据源上训练，未能充分利用多模态数据的潜力，导致性能不足。

**核心思路**：我们提出的MMIS-Net通过相似性融合模块来整合来自不同数据集的特征，同时使用一热标签空间来处理类不一致性，确保模型能够更好地适应未见数据。

**技术框架**：MMIS-Net的整体架构包括输入层、相似性融合模块、特征提取网络和输出层。相似性融合模块负责特征图的融合，而特征提取网络则基于深度学习技术提取医学图像中的重要特征。

**关键创新**：MMIS-Net的主要创新在于引入相似性融合模块和一热标签空间，这使得模型能够有效处理不同数据集间的类不一致性，显著提升了分割与检测的准确性。

**关键设计**：模型采用了特定的损失函数以优化分割效果，并在网络结构上进行了调整，以便更好地融合多模态数据的特征，确保模型的泛化能力。通过在10个数据集上训练，模型能够学习到更全面的特征表示。

## 📊 实验亮点

在RETOUCH大挑战的隐藏测试集上，MMIS-Net在液体分割任务中取得了0.83的Dice系数，表现优于现有大型基础模型和其他最先进算法。此外，液体检测任务的曲线下面积达到了1，显示出模型在检测精度上的卓越性能。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在医学影像分析领域。MMIS-Net可以用于自动化的疾病检测与诊断，帮助医生提高工作效率和准确性。未来，该模型有望推广至其他医学图像处理任务，促进多模态数据的整合与应用。

## 📄 摘要（原文）

> Purpose: Deep learning methods have shown promising results in the segmentation, and detection of diseases in medical images. However, most methods are trained and tested on data from a single source, modality, organ, or disease type, overlooking the combined potential of other available annotated data. Numerous small annotated medical image datasets from various modalities, organs, and diseases are publicly available. In this work, we aim to leverage the synergistic potential of these datasets to improve performance on unseen data. Approach: To this end, we propose a novel algorithm called MMIS-Net (MultiModal Medical Image Segmentation Network), which features Similarity Fusion blocks that utilize supervision and pixel-wise similarity knowledge selection for feature map fusion. Additionally, to address inconsistent class definitions and label contradictions, we created a one-hot label space to handle classes absent in one dataset but annotated in another. MMIS-Net was trained on 10 datasets encompassing 19 organs across 2 modalities to build a single model. Results: The algorithm was evaluated on the RETOUCH grand challenge hidden test set, outperforming large foundation models for medical image segmentation and other state-of-the-art algorithms. We achieved the best mean Dice score of 0.83 and an absolute volume difference of 0.035 for the fluids segmentation task, as well as a perfect Area Under the Curve of 1 for the fluid detection task. Conclusion: The quantitative results highlight the effectiveness of our proposed model due to the incorporation of Similarity Fusion blocks into the network's backbone for supervision and similarity knowledge selection, and the use of a one-hot label space to address label class inconsistencies and contradictions.

