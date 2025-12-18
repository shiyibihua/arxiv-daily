---
layout: default
title: Hyperspectral Mamba for Hyperspectral Object Tracking
---

# Hyperspectral Mamba for Hyperspectral Object Tracking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08265" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08265v1</a>
  <a href="https://arxiv.org/pdf/2509.08265.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08265v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08265v1', 'Hyperspectral Mamba for Hyperspectral Object Tracking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Long Gao, Yunhe Zhang, Yan Jiang, Weiying Xie, Yunsong Li

**分类**: cs.CV

**发布日期**: 2025-09-10

**🔗 代码/项目**: [GITHUB](https://github.com/lgao001/HyMamba)

---

## 💡 一句话要点

**提出基于Mamba的HyMamba网络，用于高光谱目标跟踪，提升复杂场景下的跟踪精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `高光谱图像` `目标跟踪` `Mamba` `状态空间模型` `序列建模`

## 📋 核心要点

1. 现有高光谱目标跟踪方法难以有效捕捉光谱信息、时间依赖和跨深度交互，限制了跟踪性能。
2. HyMamba通过光谱状态集成（SSI）模块和高光谱Mamba（HSM）模块，统一建模光谱、跨深度和时间信息。
3. 实验表明，HyMamba在多个数据集上取得了SOTA性能，例如在HOTC2020数据集上AUC达到73.0%。

## 📝 摘要（中文）

本文提出了一种新的高光谱目标跟踪网络HyMamba，该网络配备了Mamba结构，旨在解决现有高光谱跟踪器无法有效捕获内在光谱信息、时间依赖性和跨深度交互的问题。HyMamba通过状态空间模块（SSM）统一了光谱、跨深度和时间建模。其核心是光谱状态集成（SSI）模块，该模块能够以跨深度和时间光谱信息逐步细化和传播光谱特征。每个SSI中嵌入了高光谱Mamba（HSM）模块，通过三个方向扫描的SSM同步学习空间和光谱信息。基于SSI和HSM，HyMamba构建了来自伪彩色和高光谱输入的联合特征，并通过与从原始高光谱图像中提取的原始光谱特征进行交互来增强这些特征。在七个基准数据集上进行的大量实验表明，HyMamba实现了最先进的性能。例如，在HOTC2020数据集上，它达到了73.0%的AUC分数和96.3%的DP@20分数。

## 🔬 方法详解

**问题定义**：高光谱目标跟踪旨在利用高光谱图像丰富的光谱信息进行精确的目标定位。现有方法主要存在以下痛点：一是将高光谱数据转换为伪彩色图像，损失了原始光谱信息；二是采用模态融合策略，但忽略了光谱信息内在的关联性、时序依赖以及跨深度之间的交互，导致跟踪精度受限。

**核心思路**：HyMamba的核心思路是利用Mamba架构强大的序列建模能力，同时捕捉高光谱图像的空间、光谱和时间信息。通过设计光谱状态集成（SSI）模块和高光谱Mamba（HSM）模块，实现光谱特征的精细化提取、跨深度信息融合和时序依赖建模，从而提升高光谱目标跟踪的准确性和鲁棒性。

**技术框架**：HyMamba的整体架构包含以下几个主要模块：1) 特征提取模块：分别从伪彩色图像和原始高光谱图像中提取特征；2) 光谱状态集成（SSI）模块：通过迭代的方式，融合跨深度和时间维度的光谱信息，逐步细化特征表示；3) 高光谱Mamba（HSM）模块：嵌入在SSI模块中，利用三个方向扫描的SSM同步学习空间和光谱信息；4) 联合特征融合模块：将伪彩色特征、高光谱特征以及原始光谱特征进行融合，得到最终的特征表示，用于目标跟踪。

**关键创新**：HyMamba的关键创新在于：1) 提出了光谱状态集成（SSI）模块，能够有效地融合跨深度和时间维度的光谱信息，实现光谱特征的精细化表示；2) 引入了高光谱Mamba（HSM）模块，利用三个方向扫描的SSM同步学习空间和光谱信息，避免了传统方法中空间和光谱信息分离处理的问题；3) 将Mamba架构引入高光谱目标跟踪领域，充分利用了Mamba强大的序列建模能力。

**关键设计**：HSM模块采用三个方向扫描的SSM，分别捕捉水平、垂直和光谱维度的信息。SSI模块通过迭代的方式，逐步融合跨深度和时间维度的光谱信息。损失函数未知，网络结构细节未知，参数设置未知。

## 📊 实验亮点

HyMamba在七个基准数据集上进行了实验，结果表明其性能优于现有方法。例如，在HOTC2020数据集上，HyMamba的AUC得分达到73.0%，DP@20得分达到96.3%，显著优于其他算法。这些结果验证了HyMamba在复杂场景下高光谱目标跟踪的有效性。

## 🎯 应用场景

HyMamba在高光谱目标跟踪领域具有广泛的应用前景，例如遥感图像分析、精准农业、环境监测、军事侦察等。通过精确跟踪目标，可以实现对地物目标的识别、行为分析和状态监测，为相关领域的决策提供支持。未来，该方法有望应用于无人机、卫星等平台，实现实时高光谱目标跟踪。

## 📄 摘要（原文）

> Hyperspectral object tracking holds great promise due to the rich spectral information and fine-grained material distinctions in hyperspectral images, which are beneficial in challenging scenarios. While existing hyperspectral trackers have made progress by either transforming hyperspectral data into false-color images or incorporating modality fusion strategies, they often fail to capture the intrinsic spectral information, temporal dependencies, and cross-depth interactions. To address these limitations, a new hyperspectral object tracking network equipped with Mamba (HyMamba), is proposed. It unifies spectral, cross-depth, and temporal modeling through state space modules (SSMs). The core of HyMamba lies in the Spectral State Integration (SSI) module, which enables progressive refinement and propagation of spectral features with cross-depth and temporal spectral information. Embedded within each SSI, the Hyperspectral Mamba (HSM) module is introduced to learn spatial and spectral information synchronously via three directional scanning SSMs. Based on SSI and HSM, HyMamba constructs joint features from false-color and hyperspectral inputs, and enhances them through interaction with original spectral features extracted from raw hyperspectral images. Extensive experiments conducted on seven benchmark datasets demonstrate that HyMamba achieves state-of-the-art performance. For instance, it achieves 73.0\% of the AUC score and 96.3\% of the DP@20 score on the HOTC2020 dataset. The code will be released at https://github.com/lgao001/HyMamba.

