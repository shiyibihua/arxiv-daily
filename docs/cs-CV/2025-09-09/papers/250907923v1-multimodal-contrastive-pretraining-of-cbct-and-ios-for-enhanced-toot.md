---
layout: default
title: Multimodal Contrastive Pretraining of CBCT and IOS for Enhanced Tooth Segmentation
---

# Multimodal Contrastive Pretraining of CBCT and IOS for Enhanced Tooth Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07923" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07923v1</a>
  <a href="https://arxiv.org/pdf/2509.07923.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07923v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07923v1', 'Multimodal Contrastive Pretraining of CBCT and IOS for Enhanced Tooth Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Moo Hyun Son, Juyoung Bae, Zelin Qiu, Jiale Peng, Kai Xin Li, Yifan Lin, Hao Chen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-09

---

## 💡 一句话要点

**提出ToothMCL，用于CBCT和IOS多模态对比预训练，提升牙齿分割精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `牙齿分割` `多模态学习` `对比学习` `CBCT` `IOS` `数字牙科` `医学影像` `预训练`

## 📋 核心要点

1. 现有牙齿分割方法缺乏充分验证，性能和临床适用性受限，难以满足数字牙科日益增长的需求。
2. ToothMCL通过多模态对比学习，融合CBCT和IOS数据，学习模态不变的牙齿解剖特征表示。
3. 实验表明，ToothMCL在CBCT和IOS分割任务上均取得SOTA性能，DSC分别提升12%和8%，泛化性更强。

## 📝 摘要（中文）

数字牙科代表了现代牙科实践的变革性转变。这种转变的基础步骤是准确的牙齿数字化表示，它来自于锥形束计算机断层扫描(CBCT)和口内扫描(IOS)的分割。尽管人们对数字牙科技术的兴趣日益浓厚，但现有的分割方法通常缺乏严格的验证，并且表现出有限的性能和临床适用性。据我们所知，这是第一个引入用于牙齿分割的多模态预训练框架的工作。我们提出了ToothMCL，一种用于预训练的牙齿多模态对比学习，它集成了体积(CBCT)和基于表面的(IOS)模态。通过多模态对比学习捕获模态不变的表示，我们的方法有效地建模了精细的解剖特征，从而实现了精确的多类分割和准确的国际牙科联合会(FDI)牙齿编号识别。伴随该框架，我们整理了CBCT-IOS3.8K，迄今为止最大的配对CBCT和IOS数据集，包含3,867名患者。然后，我们在一个全面的独立数据集集合上评估了ToothMCL，代表了迄今为止最大和最多样化的评估。我们的方法在内部和外部测试中都达到了最先进的性能，在Dice相似系数(DSC)中，CBCT分割提高了12%，IOS分割提高了8%。此外，ToothMCL在牙齿组中始终优于现有方法，并展示了在不同成像条件和临床场景中的强大泛化能力。

## 🔬 方法详解

**问题定义**：论文旨在解决牙齿CBCT和IOS图像分割精度不足的问题。现有方法通常依赖于单模态数据，忽略了不同模态之间的互补信息，导致分割精度不高，泛化能力差。此外，现有方法缺乏大规模、高质量的配对CBCT和IOS数据集进行训练，限制了模型的性能提升。

**核心思路**：论文的核心思路是利用多模态对比学习，将CBCT和IOS两种模态的数据进行融合，学习模态不变的牙齿解剖特征表示。通过对比学习，模型能够区分不同牙齿的细微差异，从而提高分割精度和泛化能力。同时，论文构建了大规模的配对CBCT和IOS数据集，为模型的训练提供了充足的数据支持。

**技术框架**：ToothMCL框架主要包含以下几个模块：1) CBCT编码器：用于提取CBCT图像的特征表示；2) IOS编码器：用于提取IOS图像的特征表示；3) 多模态对比学习模块：用于学习CBCT和IOS之间的模态不变表示；4) 分割模块：用于对牙齿进行分割。框架首先使用CBCT和IOS编码器分别提取两种模态的特征，然后通过多模态对比学习模块将两种模态的特征进行融合，最后使用分割模块对牙齿进行分割。

**关键创新**：论文的关键创新在于提出了多模态对比学习框架ToothMCL，该框架能够有效地融合CBCT和IOS两种模态的数据，学习模态不变的牙齿解剖特征表示。与现有方法相比，ToothMCL能够更好地利用不同模态之间的互补信息，从而提高分割精度和泛化能力。此外，论文构建了大规模的配对CBCT和IOS数据集，为模型的训练提供了充足的数据支持。

**关键设计**：在多模态对比学习模块中，论文采用了InfoNCE损失函数，该损失函数能够有效地学习模态不变的特征表示。具体来说，对于每个样本，模型会生成一个正样本对（来自同一颗牙齿的CBCT和IOS图像）和多个负样本对（来自不同牙齿的CBCT和IOS图像）。InfoNCE损失函数的目标是最大化正样本对之间的相似度，同时最小化负样本对之间的相似度。在网络结构方面，论文采用了U-Net作为CBCT和IOS编码器，并使用ResNet作为U-Net的骨干网络。

## 📊 实验亮点

ToothMCL在内部和外部测试中均取得了SOTA性能。在CBCT分割任务中，DSC提升了12%；在IOS分割任务中，DSC提升了8%。此外，ToothMCL在不同牙齿组上的分割性能也优于现有方法，并且在不同的成像条件和临床场景下表现出强大的泛化能力。实验结果表明，ToothMCL是一种有效且鲁棒的牙齿分割方法。

## 🎯 应用场景

ToothMCL在数字牙科领域具有广泛的应用前景，可用于辅助牙科医生进行牙齿分割、牙齿编号识别、种植牙规划、正畸治疗等。该研究成果有助于提高牙科诊断和治疗的效率和精度，改善患者的治疗体验。未来，该方法可以扩展到其他医学影像领域，例如颌面外科、口腔肿瘤等。

## 📄 摘要（原文）

> Digital dentistry represents a transformative shift in modern dental practice. The foundational step in this transformation is the accurate digital representation of the patient's dentition, which is obtained from segmented Cone-Beam Computed Tomography (CBCT) and Intraoral Scans (IOS). Despite the growing interest in digital dental technologies, existing segmentation methodologies frequently lack rigorous validation and demonstrate limited performance and clinical applicability. To the best of our knowledge, this is the first work to introduce a multimodal pretraining framework for tooth segmentation. We present ToothMCL, a Tooth Multimodal Contrastive Learning for pretraining that integrates volumetric (CBCT) and surface-based (IOS) modalities. By capturing modality-invariant representations through multimodal contrastive learning, our approach effectively models fine-grained anatomical features, enabling precise multi-class segmentation and accurate identification of Fédération Dentaire Internationale (FDI) tooth numbering. Along with the framework, we curated CBCT-IOS3.8K, the largest paired CBCT and IOS dataset to date, comprising 3,867 patients. We then evaluated ToothMCL on a comprehensive collection of independent datasets, representing the largest and most diverse evaluation to date. Our method achieves state-of-the-art performance in both internal and external testing, with an increase of 12\% for CBCT segmentation and 8\% for IOS segmentation in the Dice Similarity Coefficient (DSC). Furthermore, ToothMCL consistently surpasses existing approaches in tooth groups and demonstrates robust generalizability across varying imaging conditions and clinical scenarios.

