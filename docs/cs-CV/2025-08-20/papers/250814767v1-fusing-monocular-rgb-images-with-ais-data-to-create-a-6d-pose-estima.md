---
layout: default
title: Fusing Monocular RGB Images with AIS Data to Create a 6D Pose Estimation Dataset for Marine Vessels
---

# Fusing Monocular RGB Images with AIS Data to Create a 6D Pose Estimation Dataset for Marine Vessels

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14767" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14767v1</a>
  <a href="https://arxiv.org/pdf/2508.14767.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14767v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14767v1', 'Fusing Monocular RGB Images with AIS Data to Create a 6D Pose Estimation Dataset for Marine Vessels')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fabian Holst, Emre Gülsoylu, Simone Frintrop

**分类**: cs.CV, cs.RO

**发布日期**: 2025-08-20

**备注**: Author version of the submission to the IEEE Journal of Oceanic Engineering

---

## 💡 一句话要点

**通过融合单目RGB图像与AIS数据解决海洋船舶的6D姿态估计问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `6D姿态估计` `单目RGB图像` `AIS数据` `船舶检测` `数据融合` `YOLOX-X` `自动识别系统` `深度学习`

## 📋 核心要点

1. 现有方法主要依赖AIS进行位置获取，存在设备可靠性差、数据操控和传输延迟等问题。
2. 论文提出通过融合单目RGB图像与AIS数据，生成船舶的6D姿态估计数据集，减少对人工标注的依赖。
3. 实验结果显示，PnP方法在投影误差上显著低于单应性方法，YOLOX-X模型在船舶检测中表现出色，mAP达到0.80。

## 📝 摘要（中文）

本文提出了一种新颖的技术，通过将单目RGB图像与自动识别系统（AIS）数据融合，创建海洋船舶的6D姿态估计数据集。该技术解决了仅依赖AIS进行位置获取的局限性，克服了设备可靠性、数据操控和传输延迟等问题。通过结合使用YOLOX-X对象检测网络获得的船舶检测结果与AIS消息，生成表示船舶6D姿态的3D边界框。实验表明，使用Perspective-n-Point（PnP）方法在投影误差上显著优于以往的单应性方法，且YOLOX-X模型在相关船舶类别上达到0.80的平均精度（mAP）。此外，我们还推出了一个包含3753张图像的公开数据集BONK-pose，供6D姿态估计网络的训练和评估使用。

## 🔬 方法详解

**问题定义**：本文旨在解决海洋船舶姿态估计中仅依赖AIS数据所带来的局限性，包括设备可靠性、数据操控和传输延迟等问题。

**核心思路**：通过将单目RGB图像与AIS数据融合，利用YOLOX-X网络进行船舶检测，从而生成表示船舶6D姿态的3D边界框，减少对人工标注的需求。

**技术框架**：整体流程包括数据采集、船舶检测、AIS数据融合和姿态估计四个主要模块。首先，通过YOLOX-X模型从图像中检测船舶，然后将检测结果与AIS数据进行对齐，最后生成3D边界框。

**关键创新**：本研究的创新点在于引入PnP方法进行AIS数据与图像坐标的对齐，相较于传统的单应性方法，PnP方法在投影误差上表现更优。

**关键设计**：在模型设计中，YOLOX-X网络的参数设置经过优化，以达到最佳的检测性能，同时在数据融合过程中，采用PnP方法来提高姿态估计的准确性。实验中使用的损失函数和评价指标也经过精心选择，以确保结果的可靠性。

## 📊 实验亮点

实验结果表明，PnP方法在投影误差上显著低于以往的单应性方法，提升幅度明显。同时，YOLOX-X模型在船舶检测中达到0.80的平均精度（mAP），为相关研究提供了强有力的支持。

## 🎯 应用场景

该研究的潜在应用领域包括海洋监测、船舶导航和自动化港口管理等。通过提供高质量的6D姿态估计数据集，可以促进相关领域的研究和技术发展，提升船舶识别和跟踪的准确性与效率。

## 📄 摘要（原文）

> The paper presents a novel technique for creating a 6D pose estimation dataset for marine vessels by fusing monocular RGB images with Automatic Identification System (AIS) data. The proposed technique addresses the limitations of relying purely on AIS for location information, caused by issues like equipment reliability, data manipulation, and transmission delays. By combining vessel detections from monocular RGB images, obtained using an object detection network (YOLOX-X), with AIS messages, the technique generates 3D bounding boxes that represent the vessels' 6D poses, i.e. spatial and rotational dimensions. The paper evaluates different object detection models to locate vessels in image space. We also compare two transformation methods (homography and Perspective-n-Point) for aligning AIS data with image coordinates. The results of our work demonstrate that the Perspective-n-Point (PnP) method achieves a significantly lower projection error compared to homography-based approaches used before, and the YOLOX-X model achieves a mean Average Precision (mAP) of 0.80 at an Intersection over Union (IoU) threshold of 0.5 for relevant vessel classes. We show indication that our approach allows the creation of a 6D pose estimation dataset without needing manual annotation. Additionally, we introduce the Boats on Nordelbe Kehrwieder (BONK-pose), a publicly available dataset comprising 3753 images with 3D bounding box annotations for pose estimation, created by our data fusion approach. This dataset can be used for training and evaluating 6D pose estimation networks. In addition we introduce a set of 1000 images with 2D bounding box annotations for ship detection from the same scene.

