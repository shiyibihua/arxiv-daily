---
layout: default
title: Robust Spatiotemporally Contiguous Anomaly Detection Using Tensor Decomposition
---

# Robust Spatiotemporally Contiguous Anomaly Detection Using Tensor Decomposition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00460" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00460v1</a>
  <a href="https://arxiv.org/pdf/2510.00460.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00460v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00460v1', 'Robust Spatiotemporally Contiguous Anomaly Detection Using Tensor Decomposition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rachita Mondal, Mert Indibi, Tapabrata Maiti, Selin Aviyente

**分类**: cs.LG, stat.ME, stat.ML

**发布日期**: 2025-10-01

---

## 💡 一句话要点

**提出基于张量分解的鲁棒时空连续异常检测方法，适用于视频监控等领域。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `时空数据` `异常检测` `张量分解` `低秩稀疏分解` `总变差正则化`

## 📋 核心要点

1. 现有异常检测方法主要关注点异常，无法处理时空数据中存在的时空依赖性。
2. 论文提出一种基于张量的无监督异常检测方法，通过正则化的低秩+稀疏张量分解来捕捉异常的时空平滑性。
3. 该框架在合成数据和真实数据上进行了验证，证明了其有效性，但具体性能提升数据未知。

## 📝 摘要（中文）

本文提出了一种基于张量的无监督异常检测方法，用于解决时空数据中的异常检测问题。该方法同时考虑了异常的稀疏性和时空平滑性。异常检测问题被建模为正则化的鲁棒低秩+稀疏张量分解，其中张量关于底层空间和时间图的总变差量化了异常的时空平滑性。在提取异常特征后，引入了一种统计异常评分框架，该框架考虑了局部时空依赖性。所提出的框架在合成数据和真实数据上进行了评估。

## 🔬 方法详解

**问题定义**：论文旨在解决时空数据中的异常检测问题，例如视频监控、医学图像和城市交通监控等应用。现有方法主要关注点异常，忽略了时空依赖性，并且缺乏统计置信度评估。已有的基于张量的方法虽然可以捕捉不同模式之间的依赖关系，但大多是有监督的，并且没有充分考虑异常的特定结构。

**核心思路**：论文的核心思路是将异常检测问题建模为一个正则化的鲁棒低秩+稀疏张量分解问题。低秩部分捕捉数据的正常模式，稀疏部分捕捉异常。通过引入总变差正则化项，鼓励异常在空间和时间上保持平滑，从而更好地捕捉时空连续的异常。

**技术框架**：整体框架包括两个主要阶段：1) 基于正则化鲁棒低秩+稀疏张量分解的异常特征提取。该阶段将输入时空数据表示为一个张量，并将其分解为低秩部分和稀疏部分，其中稀疏部分对应于异常。总变差正则化项被添加到目标函数中，以鼓励异常的时空平滑性。2) 统计异常评分。该阶段利用提取的异常特征，并结合局部时空依赖性，计算每个数据点的异常得分。

**关键创新**：论文的关键创新在于同时考虑了异常的稀疏性和时空平滑性，并将其整合到张量分解框架中。此外，论文还提出了一种统计异常评分框架，该框架考虑了局部时空依赖性，从而提高了异常检测的准确性。与现有方法相比，该方法是无监督的，并且能够提供统计置信度评估。

**关键设计**：论文使用总变差（Total Variation, TV）正则化来约束异常的时空平滑性。TV正则化通过底层空间和时间图来量化异常的时空平滑性。具体的张量分解算法和优化方法未知，统计异常评分框架的具体实现细节也未知。正则化参数的选择和调整策略未知。

## 📊 实验亮点

论文在合成数据和真实数据集上验证了所提出方法的有效性。虽然摘要中没有给出具体的性能指标和对比基线，但强调了该方法能够同时考虑异常的稀疏性和时空平滑性，并提供统计置信度评估，这表明该方法在异常检测的准确性和可靠性方面具有潜在的优势。具体的实验结果和提升幅度未知。

## 🎯 应用场景

该研究成果可应用于多种时空数据异常检测场景，如视频监控中的异常事件检测、医学图像中的病灶检测、城市交通监控中的交通拥堵或事故检测等。通过自动识别这些异常事件，可以提高安全性、改善医疗诊断和优化交通管理，具有重要的实际应用价值和潜在的社会效益。

## 📄 摘要（原文）

> Anomaly detection in spatiotemporal data is a challenging problem encountered in a variety of applications, including video surveillance, medical imaging data, and urban traffic monitoring. Existing anomaly detection methods focus mainly on point anomalies and cannot deal with temporal and spatial dependencies that arise in spatio-temporal data. Tensor-based anomaly detection methods have been proposed to address this problem. Although existing methods can capture dependencies across different modes, they are primarily supervised and do not account for the specific structure of anomalies. Moreover, these methods focus mainly on extracting anomalous features without providing any statistical confidence. In this paper, we introduce an unsupervised tensor-based anomaly detection method that simultaneously considers the sparse and spatiotemporally smooth nature of anomalies. The anomaly detection problem is formulated as a regularized robust low-rank + sparse tensor decomposition where the total variation of the tensor with respect to the underlying spatial and temporal graphs quantifies the spatiotemporal smoothness of the anomalies. Once the anomalous features are extracted, we introduce a statistical anomaly scoring framework that accounts for local spatio-temporal dependencies. The proposed framework is evaluated on both synthetic and real data.

