---
layout: default
title: ACIT: Attention-Guided Cross-Modal Interaction Transformer for Pedestrian Crossing Intention Prediction
---

# ACIT: Attention-Guided Cross-Modal Interaction Transformer for Pedestrian Crossing Intention Prediction

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.20020" target="_blank" class="toolbar-btn">arXiv: 2511.20020v1</a>
    <a href="https://arxiv.org/pdf/2511.20020.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20020v1" 
            onclick="toggleFavorite(this, '2511.20020v1', 'ACIT: Attention-Guided Cross-Modal Interaction Transformer for Pedestrian Crossing Intention Prediction')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yuanzhe Li, Steffen Müller

**分类**: cs.CV

**发布日期**: 2025-11-25

---

## 💡 一句话要点

**提出ACIT模型，利用注意力机制和跨模态交互Transformer提升行人过街意图预测精度。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `行人意图预测` `跨模态交互` `注意力机制` `Transformer` `自动驾驶`

## 📋 核心要点

1. 现有行人意图预测方法难以有效提取和整合来自不同类型数据的互补信息。
2. ACIT模型通过注意力机制引导跨模态特征交互，并利用Transformer捕获时序依赖关系。
3. 实验结果表明，ACIT在JAAD数据集上显著优于现有方法，证明了其有效性。

## 📝 摘要（中文）

本文提出了一种基于注意力机制引导的跨模态交互Transformer (ACIT) 用于行人过街意图预测。ACIT利用六种视觉和运动模态数据，并将它们分为三个交互对：(1) 全局语义地图和全局光流，(2) 局部RGB图像和局部光流，(3) 自车速度和行人边界框。在每个视觉交互对中，双路径注意力机制通过内模态自注意力增强主要模态中的显著区域，并通过光流引导的注意力促进与辅助模态（即光流）的深度交互。在运动交互对中，采用跨模态注意力来建模跨模态动态，从而有效提取互补的运动特征。除了成对交互之外，多模态特征融合模块进一步促进每个时间步的跨模态交互。此外，引入基于Transformer的时序特征聚合模块来捕获序列依赖性。实验结果表明，ACIT优于最先进的方法，在JAADbeh和JAADall数据集上分别实现了70%和89%的准确率。此外，还进行了广泛的消融研究，以研究ACIT不同模块的贡献。

## 🔬 方法详解

**问题定义**：行人过街意图预测是自动驾驶的关键任务，旨在减少行人相关的交通事故。现有方法难以有效融合来自不同模态（如视觉和运动）的互补信息，导致预测精度受限。尤其是在复杂场景下，如何准确捕捉行人行为的时序依赖性仍然是一个挑战。

**核心思路**：ACIT的核心思路是通过注意力机制引导跨模态特征的交互，并利用Transformer模型捕获时序依赖关系。通过将视觉和运动模态进行配对，并设计相应的注意力机制，模型能够更有效地提取和融合不同模态的互补信息。Transformer模型则用于建模行人行为的时序动态，从而提高预测的准确性。

**技术框架**：ACIT的整体架构包含以下几个主要模块：1) **跨模态交互模块**：将六种模态数据分为三个交互对，分别是全局语义地图和全局光流、局部RGB图像和局部光流、自车速度和行人边界框。2) **双路径注意力机制**：在视觉交互对中，利用双路径注意力机制增强主要模态的显著区域，并通过光流引导的注意力促进与辅助模态的深度交互。3) **跨模态注意力**：在运动交互对中，采用跨模态注意力来建模跨模态动态。4) **多模态特征融合模块**：进一步促进每个时间步的跨模态交互。5) **Transformer时序特征聚合模块**：捕获序列依赖性。

**关键创新**：ACIT的关键创新在于其注意力引导的跨模态交互机制。与现有方法相比，ACIT能够更有效地提取和融合不同模态的互补信息，从而提高预测的准确性。此外，ACIT还引入了Transformer模型来捕获行人行为的时序依赖性，进一步提升了预测性能。

**关键设计**：在视觉交互对中，双路径注意力机制包含内模态自注意力和光流引导的注意力。内模态自注意力用于增强主要模态的显著区域，光流引导的注意力则用于促进与光流模态的交互。在运动交互对中，跨模态注意力采用标准的Transformer注意力机制。Transformer时序特征聚合模块采用多层Transformer编码器结构，用于捕获时序依赖性。损失函数未知。

## 📊 实验亮点

ACIT模型在JAADbeh数据集上达到了70%的准确率，在JAADall数据集上达到了89%的准确率，显著优于现有最先进的方法。消融实验表明，各个模块都对最终性能有贡献，验证了ACIT模型的有效性。

## 🎯 应用场景

该研究成果可应用于自动驾驶系统，提高车辆对行人过街意图的预测能力，从而减少交通事故。此外，该方法也可应用于智能监控、机器人导航等领域，提升系统对行人行为的理解和预测能力，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Predicting pedestrian crossing intention is crucial for autonomous vehicles to prevent pedestrian-related collisions. However, effectively extracting and integrating complementary cues from different types of data remains one of the major challenges. This paper proposes an attention-guided cross-modal interaction Transformer (ACIT) for pedestrian crossing intention prediction. ACIT leverages six visual and motion modalities, which are grouped into three interaction pairs: (1) Global semantic map and global optical flow, (2) Local RGB image and local optical flow, and (3) Ego-vehicle speed and pedestrian's bounding box. Within each visual interaction pair, a dual-path attention mechanism enhances salient regions within the primary modality through intra-modal self-attention and facilitates deep interactions with the auxiliary modality (i.e., optical flow) via optical flow-guided attention. Within the motion interaction pair, cross-modal attention is employed to model the cross-modal dynamics, enabling the effective extraction of complementary motion features. Beyond pairwise interactions, a multi-modal feature fusion module further facilitates cross-modal interactions at each time step. Furthermore, a Transformer-based temporal feature aggregation module is introduced to capture sequential dependencies. Experimental results demonstrate that ACIT outperforms state-of-the-art methods, achieving accuracy rates of 70% and 89% on the JAADbeh and JAADall datasets, respectively. Extensive ablation studies are further conducted to investigate the contribution of different modules of ACIT.

