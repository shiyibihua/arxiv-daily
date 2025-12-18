---
layout: default
title: Virtual Fusion with Contrastive Learning for Single Sensor-based Activity Recognition
---

# Virtual Fusion with Contrastive Learning for Single Sensor-based Activity Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.02185" class="toolbar-btn" target="_blank">📄 arXiv: 2312.02185v1</a>
  <a href="https://arxiv.org/pdf/2312.02185.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.02185v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.02185v1', 'Virtual Fusion with Contrastive Learning for Single Sensor-based Activity Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Duc-Anh Nguyen, Cuong Pham, Nhien-An Le-Khac

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2023-12-01

**DOI**: [10.1109/JSEN.2024.3412397](https://doi.org/10.1109/JSEN.2024.3412397)

---

## 💡 一句话要点

**提出虚拟融合方法以解决单传感器活动识别问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人类活动识别` `虚拟融合` `对比学习` `单传感器` `多传感器融合` `隐私保护` `智能监测`

## 📋 核心要点

1. 现有的单传感器活动识别方法在捕捉用户动作时存在局限性，导致预测不准确。
2. 本文提出的虚拟融合方法通过对比学习利用多个传感器的未标记数据，推理时仅需一个传感器。
3. 实验结果表明，虚拟融合在准确率和F1-score上超越了单传感器训练，甚至在某些情况下优于实际的多传感器融合。

## 📝 摘要（中文）

人类活动识别（HAR）可以使用多种传感器，但单一传感器往往无法全面捕捉用户动作，导致错误预测。为了解决这一问题，本文提出了一种名为虚拟融合的新方法，该方法在训练过程中利用多个时间同步传感器的未标记数据，而在推理时仅需一个传感器。通过对比学习，虚拟融合能够有效利用传感器之间的相关性，显著提高识别准确率，甚至在某些情况下超越实际的多传感器融合。我们还将该方法扩展为实际融合中的虚拟融合（AFVF），在推理时使用部分训练传感器。该方法在UCI-HAR和PAMAP2基准数据集上达到了最先进的准确率和F1-score。

## 🔬 方法详解

**问题定义**：本文旨在解决单一传感器在活动识别中的局限性，现有方法在用户动作捕捉上存在不足，导致错误预测。

**核心思路**：提出虚拟融合方法，通过对比学习充分利用多个传感器的未标记数据，在推理阶段仅依赖一个传感器，从而降低成本和隐私风险。

**技术框架**：该方法包括数据收集、对比学习模块和推理阶段。训练过程中，多个传感器的数据被同步收集并用于模型训练，而推理时只需使用一个传感器进行活动识别。

**关键创新**：虚拟融合的核心创新在于利用未标记数据和对比学习来增强模型的泛化能力，显著提高了识别准确率，尤其是在缺乏标记数据的情况下。

**关键设计**：在模型设计中，采用了特定的损失函数以优化对比学习过程，确保传感器间的相关性被有效利用，同时在网络结构上进行了优化，以适应单传感器的推理需求。

## 📊 实验亮点

实验结果显示，虚拟融合方法在UCI-HAR和PAMAP2数据集上达到了最先进的准确率和F1-score，具体提升幅度超过了传统单传感器训练，且在某些情况下优于实际的多传感器融合，展现了其强大的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、健康监测和运动分析等。通过降低对多传感器的依赖，虚拟融合方法能够在保护用户隐私的同时，提供高效的活动识别解决方案，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Various types of sensors can be used for Human Activity Recognition (HAR), and each of them has different strengths and weaknesses. Sometimes a single sensor cannot fully observe the user's motions from its perspective, which causes wrong predictions. While sensor fusion provides more information for HAR, it comes with many inherent drawbacks like user privacy and acceptance, costly set-up, operation, and maintenance. To deal with this problem, we propose Virtual Fusion - a new method that takes advantage of unlabeled data from multiple time-synchronized sensors during training, but only needs one sensor for inference. Contrastive learning is adopted to exploit the correlation among sensors. Virtual Fusion gives significantly better accuracy than training with the same single sensor, and in some cases, it even surpasses actual fusion using multiple sensors at test time. We also extend this method to a more general version called Actual Fusion within Virtual Fusion (AFVF), which uses a subset of training sensors during inference. Our method achieves state-of-the-art accuracy and F1-score on UCI-HAR and PAMAP2 benchmark datasets. Implementation is available upon request.

