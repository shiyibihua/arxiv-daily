---
layout: default
title: Evaluating Foundation Models with Pathological Concept Learning for Kidney Cancer
---

# Evaluating Foundation Models with Pathological Concept Learning for Kidney Cancer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25552" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25552v1</a>
  <a href="https://arxiv.org/pdf/2509.25552.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25552v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25552v1', 'Evaluating Foundation Models with Pathological Concept Learning for Kidney Cancer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shangqi Gao, Sihan Wang, Yibo Gao, Boming Wang, Xiahai Zhuang, Anne Warren, Grant Stewart, James Jones, Mireia Crispin-Ortuzar

**分类**: cs.AI

**发布日期**: 2025-09-29

**备注**: Best Paper Award at MICCAI AMAI 2025

**🔗 代码/项目**: [GITHUB](https://github.com/shangqigao/RadioPath)

---

## 💡 一句话要点

**利用病理概念学习评估肾癌Foundation Model的转化能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `肾癌` `病理图像分析` `Foundation Model` `图神经网络` `病理概念学习`

## 📋 核心要点

1. 现有方法难以有效利用病理图像中的空间信息和病理概念进行肾癌风险评估。
2. 论文提出一种基于病理概念学习的方法，利用Foundation Model提取特征，构建病理图，并使用图神经网络进行概念识别。
3. 实验表明，该方法在肾癌生存分析中表现出色，能够有效识别高低风险患者，并具有良好的可解释性和公平性。

## 📝 摘要（中文）

为了评估Foundation Model的转化能力，我们开发了一种针对肾癌的病理概念学习方法。通过利用TNM分期指南和病理报告，我们构建了全面的肾癌病理概念。然后，我们使用Foundation Model从全切片图像中提取深度特征，构建病理图以捕获空间相关性，并训练图神经网络来识别这些概念。最后，我们证明了该方法在肾癌生存分析中的有效性，突出了其在识别低风险和高风险患者方面的可解释性和公平性。源代码已在https://github.com/shangqigao/RadioPath上发布。

## 🔬 方法详解

**问题定义**：论文旨在解决肾癌生存分析中，如何有效利用病理图像信息，特别是空间关系和病理概念的问题。现有方法通常难以充分利用这些信息，导致风险评估的准确性和可解释性不足。

**核心思路**：论文的核心思路是利用Foundation Model强大的特征提取能力，从病理图像中提取深度特征，然后构建病理图来建模细胞间的空间关系，最后通过图神经网络学习病理概念，从而实现更准确和可解释的肾癌风险评估。

**技术框架**：整体框架包括以下几个主要阶段：1) 使用Foundation Model（具体模型未知）从全切片图像中提取深度特征。2) 基于提取的特征构建病理图，节点代表图像区域，边代表区域间的空间关系。3) 使用图神经网络（GNN）在病理图上进行学习，识别预定义的病理概念。4) 将学习到的病理概念用于肾癌生存分析，例如预测患者的生存风险。

**关键创新**：该方法的主要创新在于将Foundation Model的特征提取能力与图神经网络的空间关系建模能力相结合，并将其应用于病理概念学习，从而实现更有效的肾癌风险评估。与传统方法相比，该方法能够更好地利用病理图像中的空间信息和病理概念。

**关键设计**：具体的Foundation Model选择、病理图的构建方式（例如，节点和边的定义、连接方式）、图神经网络的结构（例如，GCN、GAT等）以及损失函数等关键设计细节在摘要中未提及，属于未知信息。TNM分期指南和病理报告被用于构建病理概念，但具体如何构建也未详细说明。

## 📊 实验亮点

论文通过实验证明了该方法在肾癌生存分析中的有效性，能够有效识别高低风险患者，并具有良好的可解释性和公平性。具体的性能数据（例如，C-index、AUC等）以及与基线方法的对比结果在摘要中未提及，属于未知信息。

## 🎯 应用场景

该研究成果可应用于肾癌的辅助诊断和预后评估，帮助医生更准确地判断患者的风险等级，制定个性化的治疗方案。此外，该方法也为其他癌症类型的病理图像分析提供了新的思路，具有潜在的临床应用价值。

## 📄 摘要（原文）

> To evaluate the translational capabilities of foundation models, we develop a pathological concept learning approach focused on kidney cancer. By leveraging TNM staging guidelines and pathology reports, we build comprehensive pathological concepts for kidney cancer. Then, we extract deep features from whole slide images using foundation models, construct pathological graphs to capture spatial correlations, and trained graph neural networks to identify these concepts. Finally, we demonstrate the effectiveness of this approach in kidney cancer survival analysis, highlighting its explainability and fairness in identifying low- and high-risk patients. The source code has been released by https://github.com/shangqigao/RadioPath.

