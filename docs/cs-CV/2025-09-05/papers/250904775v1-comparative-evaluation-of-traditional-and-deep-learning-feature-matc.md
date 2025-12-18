---
layout: default
title: Comparative Evaluation of Traditional and Deep Learning Feature Matching Algorithms using Chandrayaan-2 Lunar Data
---

# Comparative Evaluation of Traditional and Deep Learning Feature Matching Algorithms using Chandrayaan-2 Lunar Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04775" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04775v1</a>
  <a href="https://arxiv.org/pdf/2509.04775.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04775v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04775v1', 'Comparative Evaluation of Traditional and Deep Learning Feature Matching Algorithms using Chandrayaan-2 Lunar Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: R. Makharia, J. G. Singla, Amitabh, N. Dube, H. Sharma

**分类**: cs.CV

**发布日期**: 2025-09-05

**备注**: 27 pages, 11 figures, 3 tables

---

## 💡 一句话要点

**利用嫦娥二号月球数据，对比传统与深度学习特征匹配算法，实现精准图像配准。**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `月球图像配准` `深度学习` `特征匹配` `SuperGlue` `多模态遥感` `图像预处理` `嫦娥二号数据`

## 📋 核心要点

1. 月球多源遥感图像配准面临光照、分辨率和传感器差异等挑战，传统方法在复杂环境下表现不佳。
2. 论文提出结合预处理流程，并对比传统特征匹配算法与深度学习方法SuperGlue在月球图像配准中的性能。
3. 实验表明，SuperGlue在精度和速度上均优于传统方法，尤其在极地光照条件下表现出更强的鲁棒性。

## 📝 摘要（中文）

精确的图像配准对于月球探测至关重要，它能够支持表面测绘、资源定位和任务规划。由于分辨率、光照和传感器畸变等差异，对来自不同月球传感器的多模态数据（如光学相机、高光谱成像仪和雷达）进行配准极具挑战性。本文评估了五种特征匹配算法：SIFT、ASIFT、AKAZE、RIFT2和SuperGlue（一种基于深度学习的匹配器），使用了来自赤道和极地区域的交叉模态图像对。论文提出了一种预处理流程，包括地理配准、分辨率对齐、强度归一化以及自适应直方图均衡化、主成分分析和阴影校正等增强方法。实验结果表明，SuperGlue始终产生最低的均方根误差和最快的运行时间。SIFT和AKAZE等传统方法在赤道附近表现良好，但在极地光照条件下性能下降。研究结果强调了预处理和基于学习的方法对于在不同条件下实现鲁棒的月球图像配准的重要性。

## 🔬 方法详解

**问题定义**：论文旨在解决月球探测中多源遥感图像的精确配准问题。现有方法，如SIFT、ASIFT等传统特征匹配算法，在光照变化剧烈、图像分辨率差异大、传感器畸变严重等情况下，匹配精度显著下降，难以满足高精度月球表面测绘和资源定位的需求。

**核心思路**：论文的核心思路是利用深度学习方法SuperGlue强大的特征提取和匹配能力，结合预处理流程，提升月球图像配准的精度和鲁棒性。SuperGlue能够学习图像中的上下文信息，从而更好地处理光照变化和图像畸变等问题。

**技术框架**：论文提出的图像配准流程主要包括以下几个阶段：1) 预处理：包括地理配准、分辨率对齐、强度归一化、自适应直方图均衡化、主成分分析和阴影校正等步骤，旨在消除不同传感器数据之间的差异。2) 特征提取与匹配：使用SIFT、ASIFT、AKAZE、RIFT2和SuperGlue等算法提取图像特征并进行匹配。3) 误差评估：使用均方根误差（RMSE）评估配准精度。

**关键创新**：论文的关键创新在于将深度学习方法SuperGlue应用于月球图像配准，并验证了其在复杂光照和图像条件下优于传统方法的性能。此外，论文提出的预处理流程也对提升配准精度起到了重要作用。

**关键设计**：SuperGlue采用图神经网络进行特征匹配，通过注意力机制学习特征之间的关系，从而实现更准确的匹配。论文中没有详细说明SuperGlue的具体参数设置，但强调了预处理的重要性，例如自适应直方图均衡化用于增强图像对比度，阴影校正用于减少光照变化的影响。

## 📊 实验亮点

实验结果表明，SuperGlue在月球图像配准任务中表现最佳，始终产生最低的均方根误差和最快的运行时间。在极地光照条件下，SuperGlue的性能明显优于SIFT和AKAZE等传统方法，验证了深度学习方法在复杂环境下的鲁棒性。预处理流程也显著提升了所有算法的配准精度。

## 🎯 应用场景

该研究成果可应用于月球探测任务中的多源遥感数据融合、高精度月球表面建模、月球资源勘探与定位、以及未来月球基地的选址和规划。该方法也可推广到其他行星探测任务，例如火星探测等，具有重要的实际应用价值和科学意义。

## 📄 摘要（原文）

> Accurate image registration is critical for lunar exploration, enabling surface mapping, resource localization, and mission planning. Aligning data from diverse lunar sensors -- optical (e.g., Orbital High Resolution Camera, Narrow and Wide Angle Cameras), hyperspectral (Imaging Infrared Spectrometer), and radar (e.g., Dual-Frequency Synthetic Aperture Radar, Selene/Kaguya mission) -- is challenging due to differences in resolution, illumination, and sensor distortion. We evaluate five feature matching algorithms: SIFT, ASIFT, AKAZE, RIFT2, and SuperGlue (a deep learning-based matcher), using cross-modality image pairs from equatorial and polar regions. A preprocessing pipeline is proposed, including georeferencing, resolution alignment, intensity normalization, and enhancements like adaptive histogram equalization, principal component analysis, and shadow correction. SuperGlue consistently yields the lowest root mean square error and fastest runtimes. Classical methods such as SIFT and AKAZE perform well near the equator but degrade under polar lighting. The results highlight the importance of preprocessing and learning-based approaches for robust lunar image registration across diverse conditions.

