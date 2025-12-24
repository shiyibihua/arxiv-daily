---
layout: default
title: Integrating Machine Learning with Multimodal Monitoring System Utilizing Acoustic and Vision Sensing to Evaluate Geometric Variations in Laser Directed Energy Deposition
---

# Integrating Machine Learning with Multimodal Monitoring System Utilizing Acoustic and Vision Sensing to Evaluate Geometric Variations in Laser Directed Energy Deposition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02847" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02847v1</a>
  <a href="https://arxiv.org/pdf/2508.02847.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02847v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02847v1', 'Integrating Machine Learning with Multimodal Monitoring System Utilizing Acoustic and Vision Sensing to Evaluate Geometric Variations in Laser Directed Energy Deposition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ke Xu, Chaitanya Krishna Prasad Vallabh, Souran Manoochehri

**分类**: eess.SP, eess.IV, eess.SY

**发布日期**: 2025-08-04

---

## 💡 一句话要点

**提出多模态监测框架以解决激光定向能量沉积中的几何变化评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `激光定向能量沉积` `多模态监测` `声发射传感` `视觉监测` `几何变化评估` `机器学习` `增材制造`

## 📋 核心要点

1. 现有的激光定向能量沉积增材制造方法在熔池动态和工艺变异的监测上存在不足，导致部件质量不稳定。
2. 本研究提出了一种多模态监测框架，结合声发射传感与视觉监测，能够逐层评估部件的几何变化。
3. 实验结果表明，集成的多模态策略在分类性能上达到了94.4%，显著提高了对几何变化的识别能力。

## 📝 摘要（中文）

激光定向能量沉积（DED）增材制造因复杂的熔池动态和工艺变异而面临一致性部件质量的挑战。尽管许多研究集中于缺陷检测，但针对熔池动态和工艺质量的过程监测系统验证工作较少。本研究提出了一种新颖的多模态监测框架，结合接触式声发射（AE）传感与同轴摄像头视觉，实现了对DED部件几何变化的逐层识别与评估。实验使用了三种部件配置进行测试，结果显示集成系统在分类性能上达到了94.4%，显著优于仅使用AE（87.8%）和仅使用摄像头（86.7%）的效果。

## 🔬 方法详解

**问题定义**：本论文旨在解决激光定向能量沉积（DED）过程中熔池动态和工艺变异导致的部件质量不一致问题。现有方法主要集中于缺陷检测，缺乏有效的过程监测系统来评估熔池动态和工艺质量。

**核心思路**：本研究提出了一种新颖的多模态监测框架，通过结合声发射（AE）传感和同轴摄像头视觉，能够逐层识别和评估DED部件的几何变化。这种设计旨在利用不同传感器的优势，提高对复杂动态过程的监测能力。

**技术框架**：整体架构包括两个主要模块：声发射传感器用于捕捉结构振动信号，摄像头用于获取熔池的视觉信息。数据预处理阶段包括声信号的时间域和频域特征提取，以及摄像头数据的熔池分割和形态特征提取。最后，采用多种机器学习算法进行分类。

**关键创新**：本研究的核心创新在于将声发射和视觉监测相结合，形成了一种集成的多模态监测系统。与现有方法相比，该系统能够更全面地捕捉与几何变化相关的结构和表面特征。

**关键设计**：在实验中，声信号经过滤波处理以提取特征，摄像头数据则进行熔池分割和形态特征提取。多种机器学习算法（如SVM、随机森林和XGBoost）被评估，以确定最佳分类模型。

## 📊 实验亮点

实验结果显示，集成的多模态监测系统在分类性能上达到了94.4%，相比于仅使用声发射的87.8%和仅使用摄像头的86.7%有显著提升，验证了该系统在捕捉几何变化方面的有效性。

## 🎯 应用场景

该研究的多模态监测框架可广泛应用于增材制造领域，尤其是在激光定向能量沉积过程中。通过提高对几何变化和工艺质量的监测能力，能够有效降低制造缺陷，提升产品质量，具有重要的实际价值和潜在影响。

## 📄 摘要（原文）

> Laser directed energy deposition (DED) additive manufacturing struggles with consistent part quality due to complex melt pool dynamics and process variations. While much research targets defect detection, little work has validated process monitoring systems for evaluating melt pool dynamics and process quality. This study presents a novel multimodal monitoring framework, synergistically integrating contact-based acoustic emission (AE) sensing with coaxial camera vision to enable layer-wise identification and evaluation of geometric variations in DED parts. The experimental study used three part configurations: a baseline part without holes, a part with a 3mm diameter through-hole, and one with a 5mm through-hole to test the system's discerning capabilities. Raw sensor data was preprocessed: acoustic signals were filtered for time-domain and frequency-domain feature extraction, while camera data underwent melt pool segmentation and morphological feature extraction. Multiple machine learning algorithms (including SVM, random forest, and XGBoost) were evaluated to find the optimal model for classifying layer-wise geometric variations. The integrated multimodal strategy achieved a superior classification performance of 94.4%, compared to 87.8% for AE only and 86.7% for the camera only. Validation confirmed the integrated system effectively captures both structural vibration signatures and surface morphological changes tied to the geometric variations. While this study focuses on specific geometries, the demonstrated capability to discriminate between features establishes a technical foundation for future applications in characterizing part variations like geometric inaccuracies and manufacturing-induced defects.

