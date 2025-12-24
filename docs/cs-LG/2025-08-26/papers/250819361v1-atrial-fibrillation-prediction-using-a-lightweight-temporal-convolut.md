---
layout: default
title: Atrial Fibrillation Prediction Using a Lightweight Temporal Convolutional and Selective State Space Architecture
---

# Atrial Fibrillation Prediction Using a Lightweight Temporal Convolutional and Selective State Space Architecture

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19361" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19361v1</a>
  <a href="https://arxiv.org/pdf/2508.19361.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19361v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19361v1', 'Atrial Fibrillation Prediction Using a Lightweight Temporal Convolutional and Selective State Space Architecture')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yongbin Lee, Ki H. Chon

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-26

**备注**: 4 pages, 2 figures, 4 table, IEEE-EMBS International Conference on Body Sensor Networks (IEEE-EMBS BSN 2025)

---

## 💡 一句话要点

**提出轻量级深度学习模型以实现心房颤动的早期预测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `心房颤动` `深度学习` `时间卷积网络` `选择性状态空间模型` `早期预测` `心血管疾病` `机器学习`

## 📋 核心要点

1. 现有AF检测方法在识别阵发性AF方面存在不足，导致早期进展常被忽视，增加了严重并发症的风险。
2. 本文提出了一种结合时间卷积网络和选择性状态空间模型的轻量级深度学习模型，旨在提高AF的早期预测能力。
3. 实验结果表明，该模型在灵敏度、特异性和AUROC等指标上均优于传统的CNN-RNN方法，且计算效率显著提升。

## 📝 摘要（中文）

心房颤动（AF）是最常见的心律失常，增加中风和心力衰竭等心血管并发症的风险。尽管现有的AF检测算法在识别持续性AF方面表现良好，但早期阶段的进展，如阵发性AF（PAF），常常因其突发性和短暂性而未被检测。本文提出了一种轻量级深度学习模型，仅使用RR间期（RRI），结合时间卷积网络（TCN）和选择性状态空间模型Mamba，以实现AF的早期预测。实验结果显示，该模型在灵敏度、特异性和F1分数等指标上均表现优异，且计算效率高，参数量和计算量远低于传统方法。

## 🔬 方法详解

**问题定义**：本文旨在解决心房颤动（AF）早期预测的问题，现有方法在识别阵发性AF（PAF）时存在灵敏度不足的痛点，导致未能及时干预。

**核心思路**：提出的模型通过结合时间卷积网络（TCN）和选择性状态空间模型Mamba，利用RR间期（RRI）进行高效的序列建模，从而实现AF的早期预测。

**技术框架**：模型整体架构包括输入层（RR间期数据）、时间卷积网络模块（用于位置编码）、选择性状态空间模型（用于序列建模）以及输出层（AF预测结果）。

**关键创新**：该研究的主要创新在于提出了一种轻量级的深度学习模型，参数量仅为73.5千，计算量为38.3 MFLOPs，显著优于传统的CNN-RNN方法，且在准确性和模型紧凑性上均有提升。

**关键设计**：模型的关键设计包括使用TCN进行位置编码，选择性状态空间模型用于高效建模，以及通过优化损失函数来提升预测性能。

## 📊 实验亮点

实验结果显示，该模型在灵敏度达到0.908，特异性为0.933，F1分数为0.930，AUROC为0.972，AUPRC为0.932，表现优于传统的CNN-RNN方法。此外，该模型能够在输入30分钟的数据基础上，提前两小时预测AF，为临床干预提供了充足的时间。

## 🎯 应用场景

该研究的潜在应用领域包括心血管疾病的早期诊断和干预，尤其是在高风险人群中。通过实现AF的早期预测，能够为临床提供足够的干预时间，从而降低心血管并发症的发生率，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Atrial fibrillation (AF) is the most common arrhythmia, increasing the risk of stroke, heart failure, and other cardiovascular complications. While AF detection algorithms perform well in identifying persistent AF, early-stage progression, such as paroxysmal AF (PAF), often goes undetected due to its sudden onset and short duration. However, undetected PAF can progress into sustained AF, increasing the risk of mortality and severe complications. Early prediction of AF offers an opportunity to reduce disease progression through preventive therapies, such as catecholamine-sparing agents or beta-blockers. In this study, we propose a lightweight deep learning model using only RR Intervals (RRIs), combining a Temporal Convolutional Network (TCN) for positional encoding with Mamba, a selective state space model, to enable early prediction of AF through efficient parallel sequence modeling. In subject-wise testing results, our model achieved a sensitivity of 0.908, specificity of 0.933, F1-score of 0.930, AUROC of 0.972, and AUPRC of 0.932. Additionally, our method demonstrates high computational efficiency, with only 73.5 thousand parameters and 38.3 MFLOPs, outperforming traditional Convolutional Neural Network-Recurrent Neural Network (CNN-RNN) approaches in both accuracy and model compactness. Notably, the model can predict AF up to two hours in advance using just 30 minutes of input data, providing enough lead time for preventive interventions.

