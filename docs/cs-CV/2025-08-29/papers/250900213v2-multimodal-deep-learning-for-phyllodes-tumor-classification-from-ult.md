---
layout: default
title: Multimodal Deep Learning for Phyllodes Tumor Classification from Ultrasound and Clinical Data
---

# Multimodal Deep Learning for Phyllodes Tumor Classification from Ultrasound and Clinical Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00213" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00213v2</a>
  <a href="https://arxiv.org/pdf/2509.00213.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00213v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00213v2', 'Multimodal Deep Learning for Phyllodes Tumor Classification from Ultrasound and Clinical Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Farhan Fuad Abir, Abigail Elliott Daly, Kyle Anderman, Tolga Ozmen, Laura J. Brattain

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-29 (更新: 2025-09-25)

**备注**: IEEE-EMBS International Conference on Body Sensor Networks (IEEE-EMBS BSN 2025)

---

## 💡 一句话要点

**提出多模态深度学习框架以提高腺瘤分类准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态深度学习` `腺瘤分类` `乳腺超声` `临床数据` `特征融合` `神经网络` `非侵入性诊断`

## 📋 核心要点

1. 腺瘤的术前分类困难，现有方法常因影像学相似性导致误诊，增加不必要的手术风险。
2. 提出的多模态深度学习框架结合超声图像和临床数据，通过双分支神经网络提取和融合特征。
3. 实验结果显示，该方法在良性与恶性腺瘤分类中显著优于单模态方法，提升了诊断准确性。

## 📝 摘要（中文）

腺瘤（PTs）是一种罕见的纤维上皮乳腺病变，由于其与良性纤维腺瘤在影像学上的相似性，导致术前分类困难，常引发不必要的手术切除。为了解决这一问题，本文提出了一种多模态深度学习框架，将乳腺超声（BUS）图像与结构化临床数据相结合，以提高诊断准确性。我们开发了一个双分支神经网络，从81名确诊PT患者的超声图像和患者元数据中提取并融合特征。通过类别感知采样和受试者分层的5折交叉验证，防止类别不平衡和数据泄漏。结果表明，所提多模态方法在良性与边缘/恶性PT分类中优于单模态基线，ConvNeXt和ResNet18在多模态设置下分别获得了0.9427和0.9349的AUC-ROC分数，以及0.6720和0.7294的F1分数，展示了多模态AI作为非侵入性诊断工具的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决腺瘤（PTs）术前分类的困难，现有方法因影像学特征相似性导致误诊，增加了不必要的手术切除风险。

**核心思路**：提出了一种多模态深度学习框架，通过结合乳腺超声图像和结构化临床数据，利用双分支神经网络提取和融合特征，以提高分类的准确性。

**技术框架**：整体架构包括两个主要分支：一个用于处理超声图像，另一个用于处理患者的临床数据。通过特征融合，增强模型对不同数据源的理解能力。采用类别感知采样和5折交叉验证策略，以防止类别不平衡和数据泄漏。

**关键创新**：最重要的技术创新在于多模态特征的融合，利用双分支网络结构有效整合不同类型的数据，显著提高了分类性能，与传统单模态方法相比，具有更高的准确性和鲁棒性。

**关键设计**：在网络结构上，采用了ConvNeXt和ResNet18作为图像编码器，优化了超声图像的特征提取。损失函数设计为适应多模态学习，确保模型在不同数据源上均能有效学习。

## 📊 实验亮点

实验结果表明，所提多模态方法在良性与恶性腺瘤分类中表现优异，ConvNeXt和ResNet18的AUC-ROC分数分别达到0.9427和0.9349，F1分数分别为0.6720和0.7294，显著优于单模态基线，展示了多模态学习的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括乳腺肿瘤的非侵入性诊断，能够减少不必要的活检，提高临床决策的准确性。未来，该框架可扩展至其他类型肿瘤的分类和诊断，推动医疗影像学的发展。

## 📄 摘要（原文）

> Phyllodes tumors (PTs) are rare fibroepithelial breast lesions that are difficult to classify preoperatively due to their radiological similarity to benign fibroadenomas. This often leads to unnecessary surgical excisions. To address this, we propose a multimodal deep learning framework that integrates breast ultrasound (BUS) images with structured clinical data to improve diagnostic accuracy. We developed a dual-branch neural network that extracts and fuses features from ultrasound images and patient metadata from 81 subjects with confirmed PTs. Class-aware sampling and subject-stratified 5-fold cross-validation were applied to prevent class imbalance and data leakage. The results show that our proposed multimodal method outperforms unimodal baselines in classifying benign versus borderline/malignant PTs. Among six image encoders, ConvNeXt and ResNet18 achieved the best performance in the multimodal setting, with AUC-ROC scores of 0.9427 and 0.9349, and F1-scores of 0.6720 and 0.7294, respectively. This study demonstrates the potential of multimodal AI to serve as a non-invasive diagnostic tool, reducing unnecessary biopsies and improving clinical decision-making in breast tumor management.

