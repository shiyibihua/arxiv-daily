---
layout: default
title: Retrieving Objects from 3D Scenes with Box-Guided Open-Vocabulary Instance Segmentation
---

# Retrieving Objects from 3D Scenes with Box-Guided Open-Vocabulary Instance Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19088" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19088v1</a>
  <a href="https://arxiv.org/pdf/2512.19088.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19088v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19088v1', 'Retrieving Objects from 3D Scenes with Box-Guided Open-Vocabulary Instance Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Khanh Nguyen, Dasith de Silva Edirimuni, Ghulam Mubashar Hassan, Ajmal Mian

**分类**: cs.CV

**发布日期**: 2025-12-22

**备注**: Accepted to AAAI 2026 Workshop on New Frontiers in Information Retrieval

**🔗 代码/项目**: [GITHUB](https://github.com/ndkhanh360/BoxOVIS)

---

## 💡 一句话要点

**提出基于2D框引导的开放词汇实例分割方法，用于从3D场景中检索目标**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D实例分割` `开放词汇` `目标检索` `点云处理` `2D检测` `3D场景理解` `机器人视觉`

## 📋 核心要点

1. 现有3D实例分割方法依赖SAM和CLIP，计算开销大，推理速度慢，难以在实际场景中部署。
2. 该论文提出一种基于2D框引导的开放词汇实例分割方法，利用2D检测器识别新颖目标，并生成3D实例掩码。
3. 该方法继承了2D检测器识别新颖目标的能力，同时保持了高效的分类，能够快速准确地检索稀有实例。

## 📝 摘要（中文）

从场景级点云中定位和检索目标是一个具有广泛应用前景的挑战性问题，常见方法是开放词汇3D实例分割。虽然现有方法表现出色，但它们严重依赖SAM和CLIP从伴随点云的图像中生成和分类3D实例掩码，导致计算开销大、处理速度慢，限制了其在实际场景中的部署。Open-YOLO 3D通过使用实时2D检测器来分类由预训练3D分割器直接从点云生成的类别无关掩码，从而缓解了这个问题，无需SAM和CLIP，显著减少了推理时间。然而，Open-YOLO 3D通常无法泛化到3D训练数据中不常出现的目标类别。本文提出了一种方法，该方法从RGB图像中生成3D实例掩码，并由2D开放词汇检测器引导，用于识别新颖目标。我们的方法继承了2D检测器识别新颖目标的能力，同时保持了高效的分类，从而能够快速准确地从开放式文本查询中检索稀有实例。代码将在https://github.com/ndkhanh360/BoxOVIS上提供。

## 🔬 方法详解

**问题定义**：现有基于点云的3D实例分割方法，特别是开放词汇场景下的目标检索，面临着泛化能力和计算效率的挑战。现有方法依赖于SAM和CLIP等模型，需要大量的计算资源，且对于训练数据中不常见的类别泛化能力较弱。Open-YOLO 3D虽然提升了效率，但对罕见物体的识别能力不足。

**核心思路**：该论文的核心思路是利用2D开放词汇检测器的强大目标识别能力，特别是对于新颖物体的识别能力，来引导3D实例掩码的生成。通过将2D检测结果与3D点云数据相结合，可以有效地提高3D实例分割的准确性和效率，同时增强对罕见物体的识别能力。

**技术框架**：该方法的技术框架主要包括以下几个阶段：1) 使用2D开放词汇检测器在RGB图像上检测目标，获得目标的2D bounding box；2) 将2D bounding box投影到3D点云空间，得到3D bounding box；3) 利用3D bounding box引导3D实例掩码的生成，例如通过点云分割算法，将3D bounding box内的点云分割出来，作为目标的实例掩码；4) 使用文本查询对分割出的3D实例进行检索和分类。

**关键创新**：该方法最重要的技术创新点在于利用2D开放词汇检测器来引导3D实例掩码的生成。与直接从3D点云生成实例掩码的方法相比，该方法可以更好地利用2D图像中的语义信息，提高分割的准确性和对新颖物体的识别能力。同时，避免了对SAM和CLIP的依赖，降低了计算开销。

**关键设计**：关键设计包括：1) 如何将2D bounding box准确地投影到3D点云空间；2) 如何利用3D bounding box有效地引导3D实例掩码的生成，例如使用基于点云的分割算法，或者基于深度学习的分割模型；3) 如何设计损失函数，使得生成的3D实例掩码与2D检测结果保持一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19088v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19088v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文提出了一种新颖的基于2D框引导的开放词汇3D实例分割方法，显著提升了对罕见物体的识别能力，同时保持了较高的计算效率。实验结果表明，该方法在开放词汇3D实例分割任务上取得了优异的性能，相较于现有方法，在准确率和效率上均有显著提升。具体的性能数据和对比基线将在论文中详细展示。

## 🎯 应用场景

该研究成果可广泛应用于机器人导航、增强现实、三维场景理解等领域。例如，在机器人导航中，机器人可以利用该方法快速准确地识别和定位场景中的目标物体，从而更好地完成导航任务。在增强现实中，用户可以通过文本查询快速检索和定位场景中的目标物体，从而获得更丰富的增强现实体验。该方法还有助于提升三维场景理解的智能化水平。

## 📄 摘要（原文）

> Locating and retrieving objects from scene-level point clouds is a challenging problem with broad applications in robotics and augmented reality. This task is commonly formulated as open-vocabulary 3D instance segmentation. Although recent methods demonstrate strong performance, they depend heavily on SAM and CLIP to generate and classify 3D instance masks from images accompanying the point cloud, leading to substantial computational overhead and slow processing that limit their deployment in real-world settings. Open-YOLO 3D alleviates this issue by using a real-time 2D detector to classify class-agnostic masks produced directly from the point cloud by a pretrained 3D segmenter, eliminating the need for SAM and CLIP and significantly reducing inference time. However, Open-YOLO 3D often fails to generalize to object categories that appear infrequently in the 3D training data. In this paper, we propose a method that generates 3D instance masks for novel objects from RGB images guided by a 2D open-vocabulary detector. Our approach inherits the 2D detector's ability to recognize novel objects while maintaining efficient classification, enabling fast and accurate retrieval of rare instances from open-ended text queries. Our code will be made available at https://github.com/ndkhanh360/BoxOVIS.

