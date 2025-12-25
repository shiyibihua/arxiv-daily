---
layout: default
title: "ORCA: Object Recognition and Comprehension for Archiving Marine Species"
---

# ORCA: Object Recognition and Comprehension for Archiving Marine Species

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21150" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21150v1</a>
  <a href="https://arxiv.org/pdf/2512.21150.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21150v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21150v1', 'ORCA: Object Recognition and Comprehension for Archiving Marine Species')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuk-Kwan Wong, Haixin Liang, Zeyu Ma, Yiwei Chen, Ziqiang Zheng, Rinaldi Gotama, Pascal Sebastian, Lauren D. Sparks, Sai-Kit Yeung

**分类**: cs.CV

**发布日期**: 2025-12-24

**备注**: Accepted by The IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), 2026

---

## 💡 一句话要点

**ORCA：用于海洋物种存档的目标识别与理解多模态基准**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `海洋物种识别` `多模态数据集` `目标检测` `实例描述` `视觉定位` `计算机视觉` `生物多样性`

## 📋 核心要点

1. 现有海洋视觉理解方法受限于数据量和任务定义，难以有效应对海洋物种识别的挑战。
2. ORCA提出一个多模态基准数据集，包含图像、边界框和实例描述，旨在促进海洋物种识别的研究。
3. 通过在ORCA上评估现有模型，揭示了物种多样性、形态重叠等挑战，为未来研究指明方向。

## 📝 摘要（中文）

海洋视觉理解对于监测和保护海洋生态系统至关重要，它能够实现自动且可扩展的生物调查。然而，有限的训练数据以及缺乏将特定领域内的海洋挑战与明确定义的计算机视觉任务对齐的系统性任务制定，阻碍了这一领域的进展，限制了模型的有效应用。为了解决这一问题，我们提出了ORCA，一个用于海洋研究的多模态基准，包含来自478个物种的14647张图像，以及42217个边界框标注和22321个专家验证的实例描述。该数据集提供了精细的视觉和文本标注，捕捉了各种海洋物种的形态学属性。为了促进方法论的进步，我们在三个任务上评估了18个最先进的模型：目标检测（闭集和开放词汇）、实例描述和视觉定位。结果突出了关键挑战，包括物种多样性、形态学重叠和专业领域需求，强调了海洋理解的难度。因此，ORCA建立了一个全面的基准，以推进海洋领域的研究。

## 🔬 方法详解

**问题定义**：现有海洋视觉理解方法面临数据稀缺和任务定义不明确的问题，导致模型在处理复杂多样的海洋物种时性能受限。缺乏一个统一的基准数据集来评估和比较不同算法的性能，阻碍了该领域的发展。现有方法难以有效应对海洋物种的形态学相似性和环境复杂性带来的挑战。

**核心思路**：ORCA的核心思路是构建一个大规模、多模态的海洋物种数据集，并定义一系列具有挑战性的视觉任务，从而促进相关算法的开发和评估。通过提供高质量的图像、边界框标注和实例描述，ORCA旨在弥合领域知识和计算机视觉技术之间的差距，推动海洋生物研究的自动化和智能化。

**技术框架**：ORCA数据集包含14647张图像，涵盖478个海洋物种。数据集提供了42217个边界框标注，用于目标检测任务，以及22321个专家验证的实例描述，用于实例描述和视觉定位任务。研究人员在ORCA上评估了18个最先进的模型，涵盖目标检测（闭集和开放词汇）、实例描述和视觉定位三个任务。

**关键创新**：ORCA的主要创新在于其数据集的规模、多样性和多模态特性。它不仅提供了大量的图像和标注，还包含了专家验证的实例描述，从而能够更全面地捕捉海洋物种的特征。此外，ORCA还定义了一系列具有挑战性的视觉任务，旨在推动相关算法的创新。

**关键设计**：ORCA数据集的设计考虑了海洋物种的多样性和形态学相似性。数据集的标注由领域专家进行验证，以确保标注的准确性和一致性。在评估现有模型时，研究人员采用了标准的评估指标，如平均精度（mAP）和CIDEr，以客观地比较不同算法的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21150v1/images/pipeline.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21150v1/images/annotation_quantities.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21150v1/images/caption_tokens_length.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在ORCA数据集上，研究人员评估了18个最先进的模型，结果表明现有模型在处理海洋物种识别任务时仍面临诸多挑战，尤其是在物种多样性、形态学重叠和专业领域需求方面。例如，在目标检测任务中，现有模型的平均精度（mAP）相对较低，表明模型难以准确识别和定位各种海洋物种。这些结果突出了ORCA数据集的价值，并为未来研究指明了方向。

## 🎯 应用场景

ORCA数据集和基准的潜在应用领域包括海洋生物多样性监测、生态系统评估、渔业资源管理和海洋保护。通过自动识别和理解海洋物种，可以更有效地进行生物调查，评估生态系统的健康状况，并制定更科学的保护策略。ORCA的未来影响在于推动海洋生物研究的自动化和智能化，为可持续的海洋资源管理提供技术支持。

## 📄 摘要（原文）

> Marine visual understanding is essential for monitoring and protecting marine ecosystems, enabling automatic and scalable biological surveys. However, progress is hindered by limited training data and the lack of a systematic task formulation that aligns domain-specific marine challenges with well-defined computer vision tasks, thereby limiting effective model application. To address this gap, we present ORCA, a multi-modal benchmark for marine research comprising 14,647 images from 478 species, with 42,217 bounding box annotations and 22,321 expert-verified instance captions. The dataset provides fine-grained visual and textual annotations that capture morphology-oriented attributes across diverse marine species. To catalyze methodological advances, we evaluate 18 state-of-the-art models on three tasks: object detection (closed-set and open-vocabulary), instance captioning, and visual grounding. Results highlight key challenges, including species diversity, morphological overlap, and specialized domain demands, underscoring the difficulty of marine understanding. ORCA thus establishes a comprehensive benchmark to advance research in marine domain. Project Page: http://orca.hkustvgd.com/.

