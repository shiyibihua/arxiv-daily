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

**提出AV3DOD，实现无需用户干预的自动词汇3D目标检测**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D目标检测` `开放词汇` `视觉-语言模型` `自动类别生成` `语义理解`

## 📋 核心要点

1. 现有开放词汇3D目标检测方法依赖用户指定的类别，限制了其自动化程度和泛化能力。
2. AV3DOD框架利用2D视觉-语言模型自动生成类别名称，无需人工干预，提升了检测的灵活性。
3. 实验表明，AV3DOD在ScanNetV2和SUNRGB-D数据集上，定位精度和语义质量均超越现有技术水平。

## 📝 摘要（中文）

开放词汇3D目标检测方法能够定位训练期间未见过的类别的3D框。然而，现有方法在训练和推理时都依赖于用户指定的类别。本文研究了自动词汇3D目标检测（AV3DOD），其中类别是为检测到的对象自动生成的，无需任何用户输入。为此，本文引入了语义分数（SS）来评估生成的类名称的质量。然后，开发了一个新的框架AV3DOD，该框架利用2D视觉-语言模型（VLMs）通过图像字幕、伪3D框生成和特征空间语义扩展来生成丰富的语义候选。AV3DOD在ScanNetV2和SUNRGB-D数据集上的定位（mAP）和语义质量（SS）方面均达到了最先进的（SOTA）性能。值得注意的是，它超过了SOTA方法CoDA，在ScanNetV2上总体mAP提高了3.48，SS相对提高了24.5%。

## 🔬 方法详解

**问题定义**：现有开放词汇3D目标检测方法需要用户预先定义类别，这限制了其在实际应用中的灵活性和自动化程度。当面对未知的场景或物体时，这些方法无法有效工作，因为它们无法生成或识别新的类别。因此，如何实现无需用户干预的自动类别生成是当前面临的关键问题。

**核心思路**：AV3DOD的核心思路是利用2D视觉-语言模型（VLMs）的强大语义理解能力，从图像中自动生成与3D物体相关的类别名称。通过将2D图像信息与3D几何信息相结合，可以为每个检测到的3D物体生成丰富的语义候选，从而实现自动词汇的3D目标检测。这种方法避免了对预定义类别的依赖，提高了检测系统的泛化能力。

**技术框架**：AV3DOD框架主要包含以下几个阶段：1) 图像字幕生成：使用2D VLM为场景图像生成字幕，提取场景的整体语义信息。2) 伪3D框生成：根据2D检测结果和深度信息生成伪3D框，为每个物体提供初步的3D定位。3) 特征空间语义扩展：利用VLM将2D图像特征映射到语义空间，并结合3D几何特征，为每个3D物体生成更丰富的语义候选。4) 语义分数评估：引入语义分数（SS）来评估生成的类别名称的质量，选择最佳的类别名称。

**关键创新**：AV3DOD最重要的技术创新点在于实现了完全自动化的类别生成，无需任何用户输入。与现有方法相比，AV3DOD不再依赖预定义的类别集合，而是能够根据场景中的实际物体自动生成类别名称。此外，语义分数（SS）的引入为评估生成类别的质量提供了一种有效的手段。

**关键设计**：在图像字幕生成阶段，使用了预训练的2D VLM模型，并针对3D场景进行了微调。在特征空间语义扩展阶段，采用了对比学习的方法，将2D图像特征和3D几何特征映射到同一个语义空间。语义分数（SS）的计算综合考虑了生成类别的相关性、准确性和简洁性。

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

AV3DOD在ScanNetV2数据集上取得了显著的性能提升，总体mAP超过了SOTA方法CoDA 3.48，并且在语义质量（SS）方面实现了24.5%的相对提升。这些结果表明，AV3DOD在自动类别生成和3D目标检测方面具有显著的优势，能够有效地提高检测的准确性和语义理解能力。

## 🎯 应用场景

AV3DOD在机器人导航、自动驾驶、智能家居等领域具有广泛的应用前景。它可以帮助机器人更好地理解周围环境，识别未知的物体，并做出更智能的决策。例如，在智能家居场景中，AV3DOD可以自动识别新的家具或物品，并将其添加到家居控制系统中。未来，该技术有望推动3D场景理解和人机交互的发展。

## 📄 摘要（原文）

> Open-vocabulary 3D object detection methods are able to localize 3D boxes of classes unseen during training. Despite the name, existing methods rely on user-specified classes both at training and inference. We propose to study Auto-Vocabulary 3D Object Detection (AV3DOD), where the classes are automatically generated for the detected objects without any user input. To this end, we introduce Semantic Score (SS) to evaluate the quality of the generated class names. We then develop a novel framework, AV3DOD, which leverages 2D vision-language models (VLMs) to generate rich semantic candidates through image captioning, pseudo 3D box generation, and feature-space semantics expansion. AV3DOD achieves the state-of-the-art (SOTA) performance on both localization (mAP) and semantic quality (SS) on the ScanNetV2 and SUNRGB-D datasets. Notably, it surpasses the SOTA, CoDA, by 3.48 overall mAP and attains a 24.5% relative improvement in SS on ScanNetV2.

