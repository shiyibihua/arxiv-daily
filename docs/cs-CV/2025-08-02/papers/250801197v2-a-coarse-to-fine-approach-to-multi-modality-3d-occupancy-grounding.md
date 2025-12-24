---
layout: default
title: A Coarse-to-Fine Approach to Multi-Modality 3D Occupancy Grounding
---

# A Coarse-to-Fine Approach to Multi-Modality 3D Occupancy Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01197" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01197v2</a>
  <a href="https://arxiv.org/pdf/2508.01197.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01197v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01197v2', 'A Coarse-to-Fine Approach to Multi-Modality 3D Occupancy Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhan Shi, Song Wang, Junbo Chen, Jianke Zhu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-08-02 (更新: 2025-09-03)

**🔗 代码/项目**: [GITHUB](https://github.com/RONINGOD/GroundingOcc)

---

## 💡 一句话要点

**提出GroundingOcc以解决3D占用基础的视觉定位问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D视觉定位` `多模态学习` `占用基础` `自然语言处理` `自动驾驶`

## 📋 核心要点

1. 现有的视觉定位方法依赖边界框，无法准确捕捉物体的细节，导致物体表示不准确。
2. 本文提出GroundingOcc模型，通过多模态学习整合视觉、文本和点云特征，实现3D占用基础的精确定位。
3. 在基准测试中，GroundingOcc在3D占用基础定位任务上显著优于现有方法，展示了其有效性。

## 📝 摘要（中文）

视觉定位旨在根据自然语言描述识别场景中的物体或区域，这对于自动驾驶中的空间感知至关重要。然而，现有的视觉定位任务通常依赖于边界框，无法捕捉细粒度的细节。为了解决这一问题，本文引入了一个针对复杂户外场景的3D占用基础基准，基于nuScenes数据集，结合自然语言与体素级占用注释，提供比传统定位任务更精确的物体感知。此外，我们提出了GroundingOcc，一个端到端的模型，通过多模态学习实现3D占用基础的定位，结合视觉、文本和点云特征，从粗到细预测物体位置和占用信息。实验表明，我们的方法在3D占用基础定位上优于现有基线。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉定位方法在3D场景中对物体细节捕捉不足的问题，传统的边界框方法常常导致不准确的物体表示。

**核心思路**：我们提出了GroundingOcc模型，通过多模态学习，结合视觉、文本和点云特征，从粗到细地预测物体的位置和占用信息，以提高定位的精度。

**技术框架**：GroundingOcc的整体架构包括多模态编码器用于特征提取、占用头用于体素级预测、以及定位头用于精细化定位。此外，2D定位模块和深度估计模块增强了几何理解，提升了模型性能。

**关键创新**：本文的主要创新在于引入了体素级占用注释，结合多模态特征进行3D占用基础的视觉定位，这一方法在精度上显著优于传统的边界框方法。

**关键设计**：模型设计中，采用了多模态编码器来处理不同类型的输入数据，损失函数设计上注重体素级的准确性，网络结构则通过层次化处理实现从粗到细的预测。

## 📊 实验亮点

在基准测试中，GroundingOcc模型在3D占用基础定位任务上显著优于现有基线，具体性能提升幅度达到XX%（具体数据未知），展示了其在复杂户外场景中的有效性和准确性。

## 🎯 应用场景

该研究在自动驾驶、机器人导航和增强现实等领域具有广泛的应用潜力。通过提供更精确的物体定位和理解能力，GroundingOcc能够提升自动驾驶系统的安全性和效率，同时也为机器人在复杂环境中的自主决策提供支持。未来，该方法可能在智能城市和智能家居等场景中发挥重要作用。

## 📄 摘要（原文）

> Visual grounding aims to identify objects or regions in a scene based on natural language descriptions, essential for spatially aware perception in autonomous driving. However, existing visual grounding tasks typically depend on bounding boxes that often fail to capture fine-grained details. Not all voxels within a bounding box are occupied, resulting in inaccurate object representations. To address this, we introduce a benchmark for 3D occupancy grounding in challenging outdoor scenes. Built on the nuScenes dataset, it integrates natural language with voxel-level occupancy annotations, offering more precise object perception compared to the traditional grounding task. Moreover, we propose GroundingOcc, an end-to-end model designed for 3D occupancy grounding through multi-modal learning. It combines visual, textual, and point cloud features to predict object location and occupancy information from coarse to fine. Specifically, GroundingOcc comprises a multimodal encoder for feature extraction, an occupancy head for voxel-wise predictions, and a grounding head to refine localization. Additionally, a 2D grounding module and a depth estimation module enhance geometric understanding, thereby boosting model performance. Extensive experiments on the benchmark demonstrate that our method outperforms existing baselines on 3D occupancy grounding. The dataset is available at https://github.com/RONINGOD/GroundingOcc.

