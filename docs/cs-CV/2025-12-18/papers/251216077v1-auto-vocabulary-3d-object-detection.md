---
layout: default
title: Auto-Vocabulary 3D Object Detection
---

# Auto-Vocabulary 3D Object Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16077" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16077v1</a>
  <a href="https://arxiv.org/pdf/2512.16077.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16077v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16077v1', 'Auto-Vocabulary 3D Object Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haomeng Zhang, Kuan-Chuan Peng, Suhas Lohit, Raymond A. Yeh

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: technical report

---

## 💡 一句话要点

**提出AV3DOD框架，实现无需用户干预的自动词汇3D目标检测。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D目标检测` `开放词汇` `视觉-语言模型` `自动词汇` `语义理解`

## 📋 核心要点

1. 现有开放词汇3D目标检测方法依赖于训练和推理阶段用户指定的类别，限制了其自动化程度和泛化能力。
2. AV3DOD框架利用2D视觉-语言模型，通过图像描述、伪3D框生成和特征空间语义扩展，自动生成丰富的语义候选。
3. 实验表明，AV3DOD在ScanNetV2和SUNRGB-D数据集上，定位精度和语义质量均达到SOTA，显著优于现有方法。

## 📝 摘要（中文）

本文研究了自动词汇3D目标检测（AV3DOD），旨在无需任何用户输入，自动为检测到的对象生成类别。为此，我们引入了语义分数（SS）来评估生成的类名称的质量。然后，我们开发了一个新颖的框架AV3DOD，该框架利用2D视觉-语言模型（VLMs），通过图像字幕、伪3D框生成和特征空间语义扩展来生成丰富的语义候选。AV3DOD在ScanNetV2和SUNRGB-D数据集上实现了最先进的（SOTA）定位（mAP）和语义质量（SS）性能。值得注意的是，它超过了SOTA方法CoDA，在ScanNetV2上实现了3.48的总体mAP提升，并在SS上实现了24.5%的相对改进。

## 🔬 方法详解

**问题定义**：现有开放词汇3D目标检测方法虽然声称具有开放词汇能力，但实际上仍然需要在训练和推理阶段依赖用户预先定义的类别。这限制了模型的自动化程度和泛化能力，无法应对真实场景中未知的物体类别。因此，需要一种能够自动生成物体类别名称的3D目标检测方法。

**核心思路**：AV3DOD的核心思路是利用2D视觉-语言模型（VLM）的强大语义理解能力，从2D图像中提取丰富的语义信息，并将其迁移到3D空间中，从而自动生成3D物体的类别名称。通过图像描述生成候选类别，并利用伪3D框和特征空间语义扩展来提升类别名称的质量。

**技术框架**：AV3DOD框架主要包含以下几个模块：1) 图像字幕模块：利用2D VLM对场景图像进行描述，生成候选的物体类别名称。2) 伪3D框生成模块：根据2D检测结果和深度信息，生成伪3D框，用于关联2D语义信息和3D几何信息。3) 特征空间语义扩展模块：在特征空间中对语义信息进行扩展，进一步丰富类别名称的语义表达。4) 语义评分模块：引入语义分数（SS）来评估生成的类别名称的质量，并选择最佳的类别名称。

**关键创新**：AV3DOD的关键创新在于：1) 提出了自动词汇3D目标检测的概念，无需用户指定类别。2) 利用2D VLM生成丰富的语义候选，避免了对预定义词汇表的依赖。3) 引入语义分数（SS）来评估生成类别名称的质量。

**关键设计**：在图像字幕模块中，使用了预训练的2D VLM模型，例如CLIP或BLIP。在伪3D框生成模块中，利用了相机内外参和深度信息。在特征空间语义扩展模块中，使用了对比学习的方法，将相似物体的特征拉近。语义分数（SS）的计算方式为：SS = α * Localization Score + (1 - α) * Semantic Alignment Score，其中α是一个超参数，用于平衡定位精度和语义对齐程度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16077v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16077v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16077v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

AV3DOD在ScanNetV2数据集上，总体mAP超过SOTA方法CoDA 3.48，并在语义分数（SS）上实现了24.5%的相对改进。这些结果表明，AV3DOD在定位精度和语义质量方面均取得了显著提升，验证了该方法的有效性。

## 🎯 应用场景

AV3DOD可应用于机器人导航、自动驾驶、智能家居等领域，尤其是在需要识别未知物体的场景中。例如，机器人可以在未知环境中自动识别并标注物体，从而更好地理解环境并执行任务。该研究有助于提升3D目标检测的自动化程度和泛化能力，推动相关领域的发展。

## 📄 摘要（原文）

> Open-vocabulary 3D object detection methods are able to localize 3D boxes of classes unseen during training. Despite the name, existing methods rely on user-specified classes both at training and inference. We propose to study Auto-Vocabulary 3D Object Detection (AV3DOD), where the classes are automatically generated for the detected objects without any user input. To this end, we introduce Semantic Score (SS) to evaluate the quality of the generated class names. We then develop a novel framework, AV3DOD, which leverages 2D vision-language models (VLMs) to generate rich semantic candidates through image captioning, pseudo 3D box generation, and feature-space semantics expansion. AV3DOD achieves the state-of-the-art (SOTA) performance on both localization (mAP) and semantic quality (SS) on the ScanNetV2 and SUNRGB-D datasets. Notably, it surpasses the SOTA, CoDA, by 3.48 overall mAP and attains a 24.5% relative improvement in SS on ScanNetV2.

