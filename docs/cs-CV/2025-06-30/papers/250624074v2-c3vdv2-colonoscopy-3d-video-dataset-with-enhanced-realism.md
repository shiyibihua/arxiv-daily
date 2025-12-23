---
layout: default
title: C3VDv2 -- Colonoscopy 3D video dataset with enhanced realism
---

# C3VDv2 -- Colonoscopy 3D video dataset with enhanced realism

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24074" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24074v2</a>
  <a href="https://arxiv.org/pdf/2506.24074.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24074v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24074v2', 'C3VDv2 -- Colonoscopy 3D video dataset with enhanced realism')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mayank V. Golhar, Lucas Sebastian Galeano Fretes, Loren Ayers, Venkata S. Akshintala, Taylor L. Bobrow, Nicholas J. Durr

**分类**: eess.IV, cs.CV

**发布日期**: 2025-06-30 (更新: 2025-09-11)

**备注**: 19 pages, 7 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://durrlab.github.io/C3VDv2/)

---

## 💡 一句话要点

**提出C3VDv2数据集以解决3D结肠镜重建算法训练不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D重建` `结肠镜` `医学影像` `数据集` `计算机视觉` `深度学习` `算法评估`

## 📋 核心要点

1. 现有的3D结肠镜数据集稀缺，限制了基于空间计算机视觉技术的诊断性能提升。
2. C3VDv2数据集通过提供高质量的3D视频和真实场景，旨在为3D结肠重建算法的开发提供支持。
3. 数据集的增强真实感使得3D重建算法的开发和评估更加稳健和具有代表性。

## 📝 摘要（中文）

空间计算机视觉技术有潜力提高结肠镜的诊断性能，但缺乏用于训练和验证的3D结肠镜数据集限制了其发展。本文介绍了C3VDv2，这是高分辨率结肠镜3D视频数据集的第二版，具有增强的真实感，旨在促进3D结肠重建算法的定量评估。数据集包含192个视频序列，总计169,371帧，捕获了60个独特的高保真硅胶结肠模型段。提供了169个结肠镜视频的真实深度、表面法线、光流、遮挡、扩散图、六自由度姿态、覆盖图和3D模型。此外，还提供了8个由胃肠病专家获取的模拟筛查结肠镜视频及其真实姿态。最后，数据集中包括15个具有结肠变形的视频用于定性评估。C3VDv2模拟了多样且具有挑战性的3D重建场景，包括粪便残留、粘液池、血液、遮挡结肠镜镜头的杂物、正面视图和快速相机运动。

## 🔬 方法详解

**问题定义**：当前缺乏高质量的3D结肠镜数据集，限制了3D重建算法的训练和验证，导致算法性能不足。

**核心思路**：C3VDv2数据集通过提供多样化的真实场景和丰富的标注信息，旨在为3D结肠重建算法提供更好的训练基础和评估标准。

**技术框架**：数据集包含192个视频序列，169,371帧，涵盖60个高保真硅胶结肠模型，提供真实深度、表面法线、光流等信息，支持算法的定量评估。

**关键创新**：C3VDv2的主要创新在于其增强的真实感和多样化场景设置，使得数据集能够模拟复杂的临床环境，显著提升了3D重建算法的训练效果。

**关键设计**：数据集提供了详细的标注，包括六自由度姿态、覆盖图和3D模型，确保算法能够在多种情况下进行有效训练和评估。

## 📊 实验亮点

C3VDv2数据集通过提供169,371帧的高质量视频和丰富的标注信息，显著提升了3D重建算法的训练效果。与现有数据集相比，该数据集在真实场景模拟和复杂情况处理上具有明显优势，为算法的开发提供了更为坚实的基础。

## 🎯 应用场景

C3VDv2数据集的潜在应用领域包括医学影像分析、计算机辅助诊断和机器人手术等。通过提供高质量的训练数据，该数据集将推动3D重建算法的研究与应用，提升结肠镜检查的准确性和效率，最终改善患者的诊断体验和治疗效果。

## 📄 摘要（原文）

> Spatial computer vision techniques have the potential to improve the diagnostic performance of colonoscopy. However, the lack of 3D colonoscopy datasets for training and validation hinders their development. This paper introduces C3VDv2, the second version (v2) of the high-definition Colonoscopy 3D Video Dataset, featuring enhanced realism designed to facilitate the quantitative evaluation of 3D colon reconstruction algorithms. 192 video sequences totaling 169,371 frames were captured by imaging 60 unique, high-fidelity silicone colon phantom segments. Ground truth depth, surface normals, optical flow, occlusion, diffuse maps, six-degree-of-freedom pose, coverage map, and 3D models are provided for 169 colonoscopy videos. Eight simulated screening colonoscopy videos acquired by a gastroenterologist are provided with ground truth poses. Lastly, the dataset includes 15 videos with colon deformations for qualitative assessment. C3VDv2 emulates diverse and challenging scenarios for 3D reconstruction algorithms, including fecal debris, mucous pools, blood, debris obscuring the colonoscope lens, en-face views, and fast camera motion. The enhanced realism of C3VDv2 will allow for more robust and representative development and evaluation of 3D reconstruction algorithms. Project Page - https://durrlab.github.io/C3VDv2/

