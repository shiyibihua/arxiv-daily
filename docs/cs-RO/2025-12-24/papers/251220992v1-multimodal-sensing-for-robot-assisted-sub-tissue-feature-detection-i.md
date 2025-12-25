---
layout: default
title: Multimodal Sensing for Robot-Assisted Sub-Tissue Feature Detection in Physiotherapy Palpation
---

# Multimodal Sensing for Robot-Assisted Sub-Tissue Feature Detection in Physiotherapy Palpation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20992" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20992v1</a>
  <a href="https://arxiv.org/pdf/2512.20992.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20992v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20992v1', 'Multimodal Sensing for Robot-Assisted Sub-Tissue Feature Detection in Physiotherapy Palpation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tian-Ao Ren, Jorge Garcia, Seongheon Hong, Jared Grinberg, Hojung Choi, Julia Di, Hao Li, Dmitry Grinberg, Mark R. Cutkosky

**分类**: cs.RO

**发布日期**: 2025-12-24

**备注**: 6 pages, 9 figures, submitted to DMD2026

---

## 💡 一句话要点

**提出一种多模态触觉传感器，用于机器人辅助的理疗触诊中亚组织特征检测。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人触诊` `多模态传感` `触觉成像` `力/力矩传感` `亚组织特征检测`

## 📋 核心要点

1. 软组织触诊中，单纯依靠力反馈难以准确识别亚组织特征，易受环境变化影响。
2. 设计多模态传感器融合触觉图像与力/力矩数据，提升亚组织特征识别的鲁棒性。
3. 实验表明，该方法在检测硅胶模型中的肌腱几何特征方面优于仅使用力反馈的方法。

## 📝 摘要（中文）

本文提出了一种紧凑的多模态传感器，它集成了基于视觉的高分辨率触觉成像和一个六轴力/力矩传感器。机器人触诊依赖于力感应，但在软组织环境中，力信号是可变的，无法可靠地揭示细微的地下特征。在具有不同地下肌腱几何形状的硅胶模型上的实验表明，单独的力信号经常产生模糊的响应，而触觉图像则揭示了在存在、直径、深度、交叉和多重性方面的清晰结构差异。然而，精确的力跟踪对于在理疗互动期间保持安全、一致的接触仍然至关重要。初步结果表明，结合触觉和力模态能够实现鲁棒的地下特征检测和受控的机器人触诊。

## 🔬 方法详解

**问题定义**：机器人辅助理疗触诊中，准确检测软组织下的细微特征（如肌腱的形状、位置等）至关重要。然而，单独使用力传感器进行触诊时，由于软组织的复杂性和力信号的易变性，很难可靠地识别这些特征。现有的方法难以区分不同几何形状的亚组织结构，导致诊断精度下降。

**核心思路**：本文的核心思路是将高分辨率的触觉图像与六轴力/力矩传感器的数据进行融合。触觉图像能够提供更直观的表面形变信息，弥补力传感器在识别细微结构方面的不足。通过结合两种模态的信息，可以更准确地检测亚组织特征。

**技术框架**：该方法的核心是一个紧凑的多模态传感器，它包含两个主要模块：1) 基于视觉的触觉成像模块，用于捕捉高分辨率的触觉图像；2) 六轴力/力矩传感器，用于测量接触力的大小和方向。在触诊过程中，传感器与软组织表面接触，同时获取触觉图像和力/力矩数据。然后，将这两种模态的数据进行融合，用于亚组织特征的检测。

**关键创新**：该方法最重要的创新点在于将视觉触觉成像与力/力矩传感相结合，形成一种多模态的触诊方案。与传统的仅依赖力反馈的触诊方法相比，该方法能够提供更丰富、更可靠的信息，从而提高亚组织特征检测的准确性和鲁棒性。

**关键设计**：触觉成像模块采用高分辨率相机和弹性体材料，以捕捉细微的表面形变。力/力矩传感器采用六轴设计，能够测量三个方向的力和三个方向的力矩。数据融合方面，论文可能采用了简单的特征拼接或者更复杂的机器学习方法（具体细节未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20992v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20992v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20992v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在检测硅胶模型中的肌腱几何特征时，结合触觉图像和力/力矩数据的多模态方法明显优于仅使用力反馈的方法。触觉图像能够清晰地揭示肌腱的存在、直径、深度、交叉和多重性等结构差异，而单独的力信号经常产生模糊的响应。具体的性能提升数据未知，但实验结果表明该方法具有很强的潜力。

## 🎯 应用场景

该研究成果可应用于机器人辅助的物理治疗、康复训练和医疗诊断等领域。通过更精确的亚组织特征检测，医生可以更好地评估患者的病情，制定个性化的治疗方案。此外，该技术还可以用于远程医疗，使专家能够远程指导机器人进行触诊操作，从而提高医疗服务的可及性。

## 📄 摘要（原文）

> Robotic palpation relies on force sensing, but force signals in soft-tissue environments are variable and cannot reliably reveal subtle subsurface features. We present a compact multimodal sensor that integrates high-resolution vision-based tactile imaging with a 6-axis force-torque sensor. In experiments on silicone phantoms with diverse subsurface tendon geometries, force signals alone frequently produce ambiguous responses, while tactile images reveal clear structural differences in presence, diameter, depth, crossings, and multiplicity. Yet accurate force tracking remains essential for maintaining safe, consistent contact during physiotherapeutic interaction. Preliminary results show that combining tactile and force modalities enables robust subsurface feature detection and controlled robotic palpation.

