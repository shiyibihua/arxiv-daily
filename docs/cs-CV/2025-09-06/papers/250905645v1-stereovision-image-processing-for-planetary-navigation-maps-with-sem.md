---
layout: default
title: Stereovision Image Processing for Planetary Navigation Maps with Semi-Global Matching and Superpixel Segmentation
---

# Stereovision Image Processing for Planetary Navigation Maps with Semi-Global Matching and Superpixel Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05645" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05645v1</a>
  <a href="https://arxiv.org/pdf/2509.05645.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05645v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05645v1', 'Stereovision Image Processing for Planetary Navigation Maps with Semi-Global Matching and Superpixel Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yan-Shan Lu, Miguel Arana-Catania, Saurabh Upadhyay, Leonard Felicetti

**分类**: astro-ph.IM, astro-ph.EP, cs.CV, cs.RO

**发布日期**: 2025-09-06

**备注**: 8 pages, 6 figures, 2 tables. ESA ASTRA 2025

---

## 💡 一句话要点

**提出基于半全局匹配和超像素分割的立体视觉行星导航地图方法，提升火星探测精度。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `立体视觉` `半全局匹配` `超像素分割` `行星导航` `火星探测`

## 📋 核心要点

1. 现有火星探测方法在低纹理、遮挡和重复图案区域表现不佳，原因是局部块匹配缺乏对场景上下文的理解。
2. 论文提出结合半全局匹配（SGM）与超像素分割的方法，利用上下文信息细化深度图，提升地形建模的准确性和鲁棒性。
3. 实验结果表明，该方法在火星模拟环境和其他数据集上均表现出更好的结构一致性和细节捕捉能力，更适合自主导航。

## 📝 摘要（中文）

火星探测需要精确可靠的地形模型，以确保探测车在不可预测且危险的地形中安全导航。立体视觉在探测车的感知中起着关键作用，通过立体匹配生成精确的深度图来实现场景重建。目前火星探测采用传统的局部块匹配，在方形窗口上聚合代价，并通过平滑约束细化视差。然而，这种方法在低纹理图像、遮挡和重复模式下表现不佳，因为它只考虑有限的相邻像素，缺乏对场景上下文的理解。本文采用半全局匹配（SGM）与基于超像素的细化相结合，以减轻固有的块伪影并恢复丢失的细节。该方法平衡了SGM的效率和准确性，并增加了上下文感知的分割，以支持更连贯的深度推断。该方法在三个数据集上进行了评估，并取得了成功的结果：在火星模拟环境中，获得的地形图显示出改进的结构一致性，尤其是在倾斜或容易发生遮挡的区域。原始视差输出中常见的岩石后面的大间隙减少，并且更准确地捕获了小岩石和边缘等表面细节。另外两个数据集用于测试该方法的一般鲁棒性和适应性，显示出更精确的视差图和更一致的地形模型，更适合火星自主导航的需求，并在非遮挡和全图像误差指标上具有竞争力的准确性。本文概述了从寻找对应特征到生成最终2D导航地图的整个地形建模过程，提供了一个完整的流程，适合集成到未来的行星探测任务中。

## 🔬 方法详解

**问题定义**：论文旨在解决火星探测车在复杂地形中导航时，传统立体视觉方法因低纹理、遮挡和重复图案等问题导致的深度图精度不足的问题。现有方法主要采用局部块匹配，仅考虑有限的邻域像素，缺乏对全局场景上下文的理解，容易产生块状伪影，丢失细节信息。

**核心思路**：论文的核心思路是将半全局匹配（SGM）与超像素分割相结合。SGM通过考虑多个方向上的像素关系来提高匹配精度，而超像素分割则利用图像的上下文信息，将像素聚合成具有相似特征的区域，从而在深度估计时能够更好地保持边缘和结构信息。

**技术框架**：该方法包含以下主要阶段：1) 立体图像获取；2) 基于SGM的初始视差图生成；3) 超像素分割，将图像分割成多个具有相似特征的区域；4) 基于超像素的视差图细化，利用超像素内的像素信息对视差值进行优化，减少噪声和伪影；5) 地形建模，将视差图转换为三维地形模型，并生成二维导航地图。

**关键创新**：该方法最重要的创新点在于将SGM与超像素分割相结合，利用超像素提供的上下文信息来约束视差估计，从而提高深度图的精度和鲁棒性。与传统的局部块匹配方法相比，该方法能够更好地处理低纹理、遮挡和重复图案等问题，并能够更准确地捕捉地形的细节信息。

**关键设计**：在SGM中，使用了多个方向的代价聚合路径，以提高匹配的准确性。超像素分割采用了SLIC算法，该算法能够生成紧凑且规则的超像素。在视差图细化阶段，使用了基于超像素的平滑约束，以保证视差值在超像素内部的一致性，并使用了边缘保持的权重，以避免过度平滑边缘区域。

## 📊 实验亮点

该方法在火星模拟环境数据集上表现出改进的结构一致性，尤其是在倾斜或容易发生遮挡的区域，减少了岩石后面的大间隙，并更准确地捕获了小岩石和边缘等表面细节。在另外两个数据集上，该方法也显示出更精确的视差图和更一致的地形模型，并在非遮挡和全图像误差指标上具有竞争力的准确性。

## 🎯 应用场景

该研究成果可应用于火星探测车的自主导航系统，提高其在复杂地形中的导航能力和安全性。此外，该方法也可推广到其他需要高精度深度估计的领域，如自动驾驶、机器人导航、三维重建等，具有广泛的应用前景和实际价值，有助于推动相关领域的技术发展。

## 📄 摘要（原文）

> Mars exploration requires precise and reliable terrain models to ensure safe rover navigation across its unpredictable and often hazardous landscapes. Stereoscopic vision serves a critical role in the rover's perception, allowing scene reconstruction by generating precise depth maps through stereo matching. State-of-the-art Martian planetary exploration uses traditional local block-matching, aggregates cost over square windows, and refines disparities via smoothness constraints. However, this method often struggles with low-texture images, occlusion, and repetitive patterns because it considers only limited neighbouring pixels and lacks a wider understanding of scene context. This paper uses Semi-Global Matching (SGM) with superpixel-based refinement to mitigate the inherent block artefacts and recover lost details. The approach balances the efficiency and accuracy of SGM and adds context-aware segmentation to support more coherent depth inference. The proposed method has been evaluated in three datasets with successful results: In a Mars analogue, the terrain maps obtained show improved structural consistency, particularly in sloped or occlusion-prone regions. Large gaps behind rocks, which are common in raw disparity outputs, are reduced, and surface details like small rocks and edges are captured more accurately. Another two datasets, evaluated to test the method's general robustness and adaptability, show more precise disparity maps and more consistent terrain models, better suited for the demands of autonomous navigation on Mars, and competitive accuracy across both non-occluded and full-image error metrics. This paper outlines the entire terrain modelling process, from finding corresponding features to generating the final 2D navigation maps, offering a complete pipeline suitable for integration in future planetary exploration missions.

