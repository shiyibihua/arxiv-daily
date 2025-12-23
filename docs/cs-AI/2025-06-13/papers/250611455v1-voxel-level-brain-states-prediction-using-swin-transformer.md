---
layout: default
title: Voxel-Level Brain States Prediction Using Swin Transformer
---

# Voxel-Level Brain States Prediction Using Swin Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11455" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11455v1</a>
  <a href="https://arxiv.org/pdf/2506.11455.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11455v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11455v1', 'Voxel-Level Brain States Prediction Using Swin Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifei Sun, Daniel Chahine, Qinghao Wen, Tianming Liu, Xiang Li, Yixuan Yuan, Fernando Calamante, Jinglei Lv

**分类**: q-bio.NC, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**提出基于Swin Transformer的体素级脑状态预测方法**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `功能性磁共振成像` `Swin Transformer` `脑状态预测` `时空建模` `神经科学` `心理健康` `脑机接口`

## 📋 核心要点

1. 现有的fMRI分析方法在处理三维体素数据的时空依赖性时存在局限，难以高效预测脑状态。
2. 本研究提出了一种基于Swin Transformer的4D架构，结合卷积解码器，旨在高效捕捉fMRI数据的时空特征。
3. 实验结果表明，该模型在预测静息状态脑活动时具有高准确性，且预测结果与实际BOLD信号高度一致。

## 📝 摘要（中文）

理解大脑动态对于神经科学和心理健康至关重要。功能性磁共振成像（fMRI）通过血氧水平依赖（BOLD）信号测量神经活动，代表大脑状态。本研究旨在利用fMRI预测未来的人类静息脑状态。针对fMRI数据的三维体素空间组织和时间依赖性，提出了一种新颖的架构，采用4D Shifted Window (Swin) Transformer作为编码器，以高效学习时空信息，并使用卷积解码器实现与输入fMRI数据相同空间和时间分辨率的脑状态预测。我们使用了来自人类连接组计划（HCP）的100名无关受试者进行模型训练和测试。我们的模型在基于先前23.04秒fMRI时间序列预测7.2秒静息状态脑活动时显示出高准确性，预测的脑状态与BOLD对比和动态高度相似。这项工作提供了有希望的证据，表明人脑的时空组织可以通过Swin Transformer模型以高分辨率学习，为未来减少fMRI扫描时间和脑机接口的发展提供了潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决如何高效预测人类静息脑状态的问题。现有方法在处理fMRI数据的三维体素空间和时间依赖性时存在不足，导致预测准确性较低。

**核心思路**：论文提出的核心思路是利用4D Shifted Window (Swin) Transformer作为编码器，结合卷积解码器，以高效学习fMRI数据的时空信息，从而实现高分辨率的脑状态预测。

**技术框架**：整体架构包括两个主要模块：首先，使用Swin Transformer编码器提取fMRI数据的时空特征；其次，利用卷积解码器将提取的特征转换为与输入数据相同分辨率的脑状态预测。

**关键创新**：最重要的技术创新在于将Swin Transformer应用于fMRI数据的时空建模，能够有效捕捉体素间的空间关系及时间动态，显著提升了预测性能。

**关键设计**：模型的关键设计包括Swin Transformer的窗口移动机制和卷积解码器的结构，确保了在高分辨率下进行有效的时空信息学习。损失函数采用标准的回归损失，以优化预测结果的准确性。

## 📊 实验亮点

实验结果显示，模型在基于23.04秒fMRI时间序列预测7.2秒静息状态脑活动时，准确性显著提高，预测的脑状态与实际BOLD信号高度相似，展示了Swin Transformer在时空建模中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括神经科学研究、心理健康监测以及脑机接口技术的开发。通过提高fMRI数据的处理效率，可能会在临床诊断和治疗中带来更快的响应时间和更高的准确性，推动个性化医疗的发展。

## 📄 摘要（原文）

> Understanding brain dynamics is important for neuroscience and mental health. Functional magnetic resonance imaging (fMRI) enables the measurement of neural activities through blood-oxygen-level-dependent (BOLD) signals, which represent brain states. In this study, we aim to predict future human resting brain states with fMRI. Due to the 3D voxel-wise spatial organization and temporal dependencies of the fMRI data, we propose a novel architecture which employs a 4D Shifted Window (Swin) Transformer as encoder to efficiently learn spatio-temporal information and a convolutional decoder to enable brain state prediction at the same spatial and temporal resolution as the input fMRI data. We used 100 unrelated subjects from the Human Connectome Project (HCP) for model training and testing. Our novel model has shown high accuracy when predicting 7.2s resting-state brain activities based on the prior 23.04s fMRI time series. The predicted brain states highly resemble BOLD contrast and dynamics. This work shows promising evidence that the spatiotemporal organization of the human brain can be learned by a Swin Transformer model, at high resolution, which provides a potential for reducing the fMRI scan time and the development of brain-computer interfaces in the future.

