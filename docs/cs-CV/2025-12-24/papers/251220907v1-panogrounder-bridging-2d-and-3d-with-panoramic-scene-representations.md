---
layout: default
title: "PanoGrounder: Bridging 2D and 3D with Panoramic Scene Representations for VLM-based 3D Visual Grounding"
---

# PanoGrounder: Bridging 2D and 3D with Panoramic Scene Representations for VLM-based 3D Visual Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20907" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20907v1</a>
  <a href="https://arxiv.org/pdf/2512.20907.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20907v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20907v1', 'PanoGrounder: Bridging 2D and 3D with Panoramic Scene Representations for VLM-based 3D Visual Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seongmin Jung, Seongho Choi, Gunwoo Jeon, Minsu Cho, Jongwoo Lim

**分类**: cs.CV

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**PanoGrounder：利用全景场景表示桥接2D和3D，实现基于VLM的3D视觉定位**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D视觉定位` `全景场景表示` `视觉-语言模型` `跨模态学习` `机器人技术`

## 📋 核心要点

1. 现有3D视觉定位方法依赖大量3D视觉-语言数据，且模型推理能力弱于先进的VLM，泛化性受限。
2. PanoGrounder利用全景图作为2D和3D的桥梁，结合预训练VLM，提升视觉-语言推理能力和泛化性。
3. 实验表明，PanoGrounder在ScanRefer和Nr3D数据集上取得了SOTA结果，并对未见过的3D数据表现出更好的泛化能力。

## 📝 摘要（中文）

3D视觉定位（3DVG）是视觉-语言感知到机器人技术的关键桥梁，它需要语言理解和3D场景推理能力。传统的监督模型利用显式的3D几何信息，但由于3D视觉-语言数据集的稀缺以及与现代视觉-语言模型（VLM）相比有限的推理能力，其泛化能力受到限制。我们提出了PanoGrounder，一个通用的3DVG框架，它将多模态全景表示与预训练的2D VLM相结合，以实现强大的视觉-语言推理。全景渲染图，辅以3D语义和几何特征，作为2D和3D之间的中间表示，并提供两个主要优势：（i）它们可以通过最小的适配直接输入到VLM中，以及（ii）由于其360度视野，它们保留了长程对象到对象的关系。我们设计了一个三阶段流程，该流程考虑场景布局和几何形状来放置一组紧凑的全景视点，使用VLM在每个全景渲染图上定位文本查询，并通过提升将每个视点的预测融合为单个3D边界框。我们的方法在ScanRefer和Nr3D上实现了最先进的结果，并展示了对未见过的3D数据集和文本释义的卓越泛化能力。

## 🔬 方法详解

**问题定义**：3D视觉定位旨在根据给定的文本描述，在3D场景中定位目标物体。现有方法依赖于大量的3D视觉-语言标注数据，并且模型的视觉-语言推理能力相对较弱，导致泛化能力不足。这些方法难以适应新的场景和文本描述方式。

**核心思路**：PanoGrounder的核心思路是利用全景图作为2D和3D场景之间的桥梁。通过将3D场景渲染成多个全景图，并结合3D语义和几何信息，可以充分利用预训练的2D VLM强大的视觉-语言推理能力。全景图的360度视野也有助于捕捉场景中物体之间的长程关系。

**技术框架**：PanoGrounder包含三个主要阶段：1) 全景视点选择：根据场景布局和几何信息，选择一组紧凑的全景视点。2) 基于VLM的全景图定位：使用预训练的2D VLM在每个全景图上定位文本查询所指代的物体。3) 3D边界框融合：将每个视点的预测结果通过提升操作融合为单个3D边界框。

**关键创新**：PanoGrounder的关键创新在于使用全景图作为中间表示，桥接了2D和3D场景，从而能够充分利用预训练的2D VLM的强大能力。与直接在3D数据上训练模型相比，这种方法可以显著提高模型的泛化能力。

**关键设计**：全景视点的选择策略考虑了场景的几何信息，以确保每个视点都能覆盖场景中的关键区域。在全景图定位阶段，使用了预训练的CLIP模型进行视觉-语言匹配。在3D边界框融合阶段，使用了加权平均的方法，根据每个视点的置信度对预测结果进行加权。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20907v1/fig/hook.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20907v1/fig/pipeline.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20907v1/fig/adapter.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

PanoGrounder在ScanRefer和Nr3D数据集上取得了state-of-the-art的结果，显著优于现有的3D视觉定位方法。此外，该方法在未见过的3D数据集和文本释义上表现出更强的泛化能力，验证了其有效性和鲁棒性。实验结果表明，利用全景图作为中间表示，可以有效提升3D视觉定位的性能。

## 🎯 应用场景

PanoGrounder在机器人导航、智能家居、增强现实等领域具有广泛的应用前景。例如，机器人可以根据用户的语音指令，在复杂的室内环境中定位并抓取目标物体。该研究有助于提升机器人与人类的交互能力，并促进机器人技术在实际生活中的应用。

## 📄 摘要（原文）

> 3D Visual Grounding (3DVG) is a critical bridge from vision-language perception to robotics, requiring both language understanding and 3D scene reasoning. Traditional supervised models leverage explicit 3D geometry but exhibit limited generalization, owing to the scarcity of 3D vision-language datasets and the limited reasoning capabilities compared to modern vision-language models (VLMs). We propose PanoGrounder, a generalizable 3DVG framework that couples multi-modal panoramic representation with pretrained 2D VLMs for strong vision-language reasoning. Panoramic renderings, augmented with 3D semantic and geometric features, serve as an intermediate representation between 2D and 3D, and offer two major benefits: (i) they can be directly fed to VLMs with minimal adaptation and (ii) they retain long-range object-to-object relations thanks to their 360-degree field of view. We devise a three-stage pipeline that places a compact set of panoramic viewpoints considering the scene layout and geometry, grounds a text query on each panoramic rendering with a VLM, and fuses per-view predictions into a single 3D bounding box via lifting. Our approach achieves state-of-the-art results on ScanRefer and Nr3D, and demonstrates superior generalization to unseen 3D datasets and text rephrasings.

