---
layout: default
title: Parts-Mamba: Augmenting Joint Context with Part-Level Scanning for Occluded Human Skeleton
---

# Parts-Mamba: Augmenting Joint Context with Part-Level Scanning for Occluded Human Skeleton

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.16860" target="_blank" class="toolbar-btn">arXiv: 2511.16860v1</a>
    <a href="https://arxiv.org/pdf/2511.16860.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16860v1" 
            onclick="toggleFavorite(this, '2511.16860v1', 'Parts-Mamba: Augmenting Joint Context with Part-Level Scanning for Occluded Human Skeleton')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Tianyi Shen, Huijuan Xu, Nilesh Ahuja, Omesh Tickoo, Philip Shin, Vijaykrishnan Narayanan

**分类**: cs.CV

**发布日期**: 2025-11-21

---

## 💡 一句话要点

**提出Parts-Mamba模型，增强骨骼动作识别在遮挡场景下的性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `骨骼动作识别` `图卷积网络` `Mamba架构` `遮挡处理` `长程依赖` `上下文建模` `部位信息融合`

## 📋 核心要点

1. 现有GCN模型在骨骼动作识别中，面对遮挡导致局部上下文缺失时性能显著下降。
2. Parts-Mamba模型通过特定部位扫描和部位-身体融合，增强了对远处关节上下文信息的捕获和保持能力。
3. 实验结果表明，在遮挡场景下，Parts-Mamba在NTU RGB+D 60和120数据集上准确率提升高达12.9%。

## 📝 摘要（中文）

骨骼动作识别旨在通过人体骨骼数据识别动作。图卷积网络（GCNs）的使用推动了该任务的重大进展。然而，在实际场景中，由于人体部位的遮挡或通信质量不佳，捕获的骨骼并不总是完美或完整，导致骨骼中缺少部分或视频中缺少帧。在这种非理想情况下，由于缺少局部上下文，现有的GCN模型表现不佳。为了解决这个限制，我们提出了Parts-Mamba，一种混合GCN-Mamba模型，旨在增强捕获和保持来自远处关节的上下文信息的能力。所提出的Parts-Mamba模型通过其特定部位的扫描特征有效地捕获特定部位的信息，并通过部位-身体融合模块保留非相邻关节的上下文。我们提出的模型在不同的遮挡设置下，在NTU RGB+D 60和NTU RGB+D 120数据集上进行了评估，准确率提高了高达12.9%。

## 🔬 方法详解

**问题定义**：论文旨在解决骨骼动作识别中，由于人体遮挡或数据缺失导致的局部上下文信息不足，进而影响动作识别准确率的问题。现有GCN模型在处理此类问题时，由于依赖完整的局部连接，性能会显著下降。

**核心思路**：论文的核心思路是利用Mamba架构的长程依赖建模能力，结合GCN的局部特征提取优势，构建一个混合模型Parts-Mamba。通过特定部位的扫描特征提取部位信息，并利用部位-身体融合模块保留非相邻关节的上下文信息，从而提升模型在遮挡情况下的鲁棒性。

**技术框架**：Parts-Mamba模型整体架构包含以下几个主要模块：1) GCN模块：用于提取局部骨骼特征。2) Parts-Specific Scanning模块：针对不同身体部位进行扫描，提取特定部位的信息。3) Parts-Body Fusion模块：将部位信息与整体身体信息进行融合，保留非相邻关节的上下文。4) Mamba模块：利用Mamba架构建模长程依赖关系，增强上下文信息的捕获能力。

**关键创新**：该论文的关键创新在于将GCN和Mamba架构进行有效融合，提出了Parts-Mamba模型。通过Parts-Specific Scanning模块和Parts-Body Fusion模块，模型能够更好地处理遮挡情况下的骨骼动作识别问题。与传统GCN模型相比，Parts-Mamba能够更好地捕获和保持来自远处关节的上下文信息。

**关键设计**：Parts-Specific Scanning模块的设计允许模型关注特定身体部位，例如头部、手臂、腿部等，分别进行特征提取。Parts-Body Fusion模块采用加权融合的方式，将部位信息和整体身体信息进行结合，权重参数可以通过学习得到。Mamba模块采用选择性状态空间模型（Selective State Space Model, S6）来建模长程依赖关系。

## 📊 实验亮点

实验结果表明，Parts-Mamba模型在NTU RGB+D 60和NTU RGB+D 120数据集上，针对不同遮挡设置，准确率提升高达12.9%。相较于传统的GCN模型，Parts-Mamba在遮挡场景下表现出更强的鲁棒性和更高的识别精度。该结果验证了Parts-Mamba模型在处理不完整骨骼数据方面的有效性。

## 🎯 应用场景

该研究成果可应用于视频监控、人机交互、康复训练等领域。在视频监控中，即使人体部分被遮挡，也能准确识别动作行为。在人机交互中，可以提升系统对用户意图的理解。在康复训练中，可以辅助评估患者的运动能力。未来，该技术有望进一步扩展到其他需要处理不完整或遮挡数据的场景。

## 📄 摘要（原文）

> Skeleton action recognition involves recognizing human action from human skeletons. The use of graph convolutional networks (GCNs) has driven major advances in this recognition task. In real-world scenarios, the captured skeletons are not always perfect or complete because of occlusions of parts of the human body or poor communication quality, leading to missing parts in skeletons or videos with missing frames. In the presence of such non-idealities, existing GCN models perform poorly due to missing local context. To address this limitation, we propose Parts-Mamba, a hybrid GCN-Mamba model designed to enhance the ability to capture and maintain contextual information from distant joints. The proposed Parts-Mamba model effectively captures part-specific information through its parts-specific scanning feature and preserves non-neighboring joint context via a parts-body fusion module. Our proposed model is evaluated on the NTU RGB+D 60 and NTU RGB+D 120 datasets under different occlusion settings, achieving up to 12.9% improvement in accuracy.

