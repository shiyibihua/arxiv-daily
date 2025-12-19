---
layout: default
title: N3D-VLM: Native 3D Grounding Enables Accurate Spatial Reasoning in Vision-Language Models
---

# N3D-VLM: Native 3D Grounding Enables Accurate Spatial Reasoning in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16561" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16561v1</a>
  <a href="https://arxiv.org/pdf/2512.16561.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16561v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16561v1', 'N3D-VLM: Native 3D Grounding Enables Accurate Spatial Reasoning in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxin Wang, Lei Ke, Boqiang Zhang, Tianyuan Qu, Hanxun Yu, Zhenpeng Huang, Meng Yu, Dan Xu, Dong Yu

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project Page: https://n3d-vlm.github.io

---

## 💡 一句话要点

**N3D-VLM：原生3D感知赋能视觉语言模型精确空间推理**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D感知` `视觉语言模型` `空间推理` `3D grounding` `深度估计`

## 📋 核心要点

1. 现有视觉语言模型缺乏对3D场景的内在感知，难以理解空间关系和深度信息，限制了其应用。
2. N3D-VLM通过集成原生3D物体感知和3D感知视觉推理，实现精确的3D定位和可解释的空间理解。
3. 该方法在3D grounding和空间推理任务上均取得了SOTA性能，并构建了大规模3D标注数据集。

## 📝 摘要（中文）

当前的多模态模型虽然可以基于2D图像回答问题，但缺乏内在的3D物体感知能力，限制了其理解3D场景中的空间关系和深度线索的能力。本文提出了N3D-VLM，一种新颖的统一框架，它无缝集成了原生3D物体感知和3D感知视觉推理，从而实现了精确的3D grounding和可解释的空间理解。与直接从RGB/RGB-D输入预测答案的传统端到端模型不同，我们的方法赋予模型原生的3D物体感知能力，使其能够基于文本描述直接在3D空间中定位物体。在精确的3D物体定位的基础上，该模型进一步执行显式的3D推理，从而实现更可解释和结构化的空间理解。为了支持这些能力的稳健训练，我们开发了一个可扩展的数据构建流程，该流程利用深度估计将大规模2D标注提升到3D空间，显著增加了3D物体grounding数据的多样性和覆盖范围，产生了比现有最大的单图像3D检测数据集大六倍以上的数据集。此外，该流程还生成了针对3D中的思维链（CoT）推理的空间问答数据集，从而促进了3D物体定位和3D空间推理的联合训练。实验结果表明，我们的统一框架不仅在3D grounding任务上实现了最先进的性能，而且在视觉语言模型中的3D空间推理方面始终优于现有方法。

## 🔬 方法详解

**问题定义**：现有视觉语言模型主要基于2D图像进行推理，缺乏对3D场景的理解能力，无法准确感知物体间的空间关系和深度信息。这限制了模型在需要空间推理的任务中的表现，例如理解物体间的相对位置、距离等。现有方法通常直接从RGB或RGB-D图像预测答案，缺乏可解释性，且难以进行精确的3D定位。

**核心思路**：N3D-VLM的核心思路是赋予模型原生的3D物体感知能力，使其能够直接在3D空间中定位物体，并在此基础上进行显式的3D空间推理。通过将2D图像信息提升到3D空间，并结合文本描述，模型可以更准确地理解场景中的空间关系，从而提高空间推理的准确性和可解释性。

**技术框架**：N3D-VLM包含以下主要模块：1) 3D物体感知模块：该模块负责将2D图像信息转换为3D表示，并根据文本描述定位3D空间中的物体。这通常涉及深度估计、3D物体检测等技术。2) 3D空间推理模块：该模块基于3D物体定位的结果，进行显式的空间推理，例如计算物体间的距离、相对位置等。3) 视觉语言模型：该模型负责将文本描述和3D场景信息融合，并生成最终的答案。整个流程是端到端可训练的，可以联合优化3D物体感知和3D空间推理的能力。

**关键创新**：N3D-VLM最重要的技术创新点在于其原生3D物体感知能力。与现有方法不同，N3D-VLM不是直接从2D图像预测答案，而是首先在3D空间中定位物体，然后再进行推理。这种方法可以更准确地理解场景中的空间关系，并提高空间推理的准确性和可解释性。此外，该论文还提出了一个可扩展的数据构建流程，可以生成大规模的3D标注数据集，为模型的训练提供了充足的数据支持。

**关键设计**：该论文的关键设计包括：1) 使用深度估计技术将2D标注提升到3D空间，从而生成大规模的3D物体grounding数据集。2) 构建针对3D中的思维链（CoT）推理的空间问答数据集，促进了3D物体定位和3D空间推理的联合训练。3) 具体网络结构和损失函数细节未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16561v1/x3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16561v1/x4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16561v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

N3D-VLM在3D grounding任务上取得了SOTA性能，并且在3D空间推理方面始终优于现有方法。论文构建了一个比现有最大的单图像3D检测数据集大六倍以上的数据集，为3D视觉语言模型的研究提供了重要的数据支持。具体的性能提升数据未知。

## 🎯 应用场景

N3D-VLM在机器人导航、自动驾驶、虚拟现实等领域具有广泛的应用前景。它可以帮助机器人理解周围环境，进行更智能的导航和交互。在自动驾驶领域，它可以提高车辆对复杂场景的理解能力，从而提高驾驶安全性。在虚拟现实领域，它可以增强用户的沉浸感和交互性，创造更逼真的虚拟体验。

## 📄 摘要（原文）

> While current multimodal models can answer questions based on 2D images, they lack intrinsic 3D object perception, limiting their ability to comprehend spatial relationships and depth cues in 3D scenes. In this work, we propose N3D-VLM, a novel unified framework that seamlessly integrates native 3D object perception with 3D-aware visual reasoning, enabling both precise 3D grounding and interpretable spatial understanding. Unlike conventional end-to-end models that directly predict answers from RGB/RGB-D inputs, our approach equips the model with native 3D object perception capabilities, enabling it to directly localize objects in 3D space based on textual descriptions. Building upon accurate 3D object localization, the model further performs explicit reasoning in 3D, achieving more interpretable and structured spatial understanding. To support robust training for these capabilities, we develop a scalable data construction pipeline that leverages depth estimation to lift large-scale 2D annotations into 3D space, significantly increasing the diversity and coverage for 3D object grounding data, yielding over six times larger than the largest existing single-image 3D detection dataset. Moreover, the pipeline generates spatial question-answering datasets that target chain-of-thought (CoT) reasoning in 3D, facilitating joint training for both 3D object localization and 3D spatial reasoning. Experimental results demonstrate that our unified framework not only achieves state-of-the-art performance on 3D grounding tasks, but also consistently surpasses existing methods in 3D spatial reasoning in vision-language model.

