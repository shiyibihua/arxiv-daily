---
layout: default
title: "GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation"
---

# GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23180" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23180v1</a>
  <a href="https://arxiv.org/pdf/2512.23180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23180v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23180v1', 'GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianchen Deng, Xuefeng Chen, Yi Chen, Qu Chen, Yuyao Xu, Lijin Yang, Le Xu, Yu Zhang, Bo Zhang, Wuxiong Huang, Hesheng Wang

**分类**: cs.CV

**发布日期**: 2025-12-29

**🔗 代码/项目**: [GITHUB](https://github.com/dtc111111/GaussianDWM)

---

## 💡 一句话要点

**提出基于3D高斯表示的驾驶世界模型GaussianDWM，实现统一的场景理解和多模态生成。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `驾驶世界模型` `3D高斯表示` `场景理解` `多模态生成` `视觉语言融合` `自动驾驶` `语言引导采样`

## 📋 核心要点

1. 现有驾驶世界模型缺乏3D场景理解能力，且只能根据输入数据生成内容，无法解释或推理驾驶环境。
2. 提出基于3D高斯场景表示的统一DWM框架，通过将语言特征嵌入高斯基元实现早期模态对齐。
3. 设计任务感知语言引导采样策略和双条件多模态生成模型，并在nuScenes等数据集上验证了有效性。

## 📝 摘要（中文）

本文提出了一种新颖的统一驾驶世界模型（DWM）框架，该框架基于3D高斯场景表示，能够实现3D场景理解和多模态场景生成，同时增强了对理解和生成任务的上下文丰富性。该方法通过将丰富的语言特征嵌入到每个高斯基元中，直接将文本信息与3D场景对齐，从而实现早期模态对齐。此外，设计了一种新颖的、任务感知的语言引导采样策略，该策略移除冗余的3D高斯并向LLM注入准确且紧凑的3D token。进一步地，设计了一个双条件多模态生成模型，其中视觉-语言模型捕获的信息被用作高级语言条件，并结合低级图像条件，共同指导多模态生成过程。在nuScenes和NuInteract数据集上进行了全面的研究，验证了该框架的有效性。该方法取得了最先进的性能，代码将在GitHub上公开。

## 🔬 方法详解

**问题定义**：现有驾驶世界模型（DWMs）无法有效理解3D场景，并且缺乏将文本信息与3D空间信息精确对齐的能力。它们通常依赖于点云或BEV特征，这限制了模型对驾驶环境的解释和推理能力。此外，现有模型主要关注条件生成，而忽略了对场景的深层理解。

**核心思路**：本文的核心思路是利用3D高斯表示作为统一的场景表示，将视觉和语言信息融合到高斯基元中，从而实现3D场景的理解和多模态生成。通过将语言特征嵌入到每个3D高斯中，实现早期模态对齐，并利用语言引导采样策略来优化3D场景的表示。

**技术框架**：GaussianDWM框架包含以下主要模块：1) 3D高斯场景表示模块：将3D场景表示为一组3D高斯基元，每个高斯基元包含位置、形状、颜色等属性。2) 视觉-语言嵌入模块：将图像和文本信息嵌入到3D高斯基元中，实现视觉和语言信息的融合。3) 任务感知语言引导采样模块：根据任务需求，利用语言信息对3D高斯基元进行采样，去除冗余信息，保留关键信息。4) 双条件多模态生成模块：利用视觉和语言信息作为条件，生成多模态场景内容。

**关键创新**：该论文的关键创新在于：1) 提出了一种基于3D高斯表示的统一DWM框架，能够同时实现3D场景理解和多模态生成。2) 提出了一种早期模态对齐方法，通过将语言特征嵌入到3D高斯基元中，实现了视觉和语言信息的有效融合。3) 设计了一种任务感知语言引导采样策略，能够根据任务需求优化3D场景的表示。

**关键设计**：任务感知语言引导采样策略是关键设计之一，它利用语言信息对3D高斯基元进行采样，去除冗余信息，保留关键信息。具体来说，该策略首先利用语言模型对场景进行描述，然后根据描述信息对3D高斯基元进行重要性排序，最后选择最重要的3D高斯基元作为场景的表示。双条件多模态生成模块利用视觉和语言信息作为条件，生成多模态场景内容。该模块采用Transformer架构，将视觉和语言信息作为输入，生成图像、文本等多种模态的内容。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23180v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23180v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23180v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在nuScenes和NuInteract数据集上取得了state-of-the-art的性能。具体而言，该方法在3D场景理解和多模态生成任务上均取得了显著的提升，证明了该框架的有效性。代码将在GitHub上公开。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、虚拟现实等领域。通过对驾驶环境的理解和推理，可以提高自动驾驶系统的安全性和可靠性。在机器人导航中，可以帮助机器人更好地理解周围环境，从而实现更智能的导航。在虚拟现实中，可以生成更逼真的虚拟场景，提高用户体验。

## 📄 摘要（原文）

> Driving World Models (DWMs) have been developing rapidly with the advances of generative models. However, existing DWMs lack 3D scene understanding capabilities and can only generate content conditioned on input data, without the ability to interpret or reason about the driving environment. Moreover, current approaches represent 3D spatial information with point cloud or BEV features do not accurately align textual information with the underlying 3D scene. To address these limitations, we propose a novel unified DWM framework based on 3D Gaussian scene representation, which enables both 3D scene understanding and multi-modal scene generation, while also enabling contextual enrichment for understanding and generation tasks. Our approach directly aligns textual information with the 3D scene by embedding rich linguistic features into each Gaussian primitive, thereby achieving early modality alignment. In addition, we design a novel task-aware language-guided sampling strategy that removes redundant 3D Gaussians and injects accurate and compact 3D tokens into LLM. Furthermore, we design a dual-condition multi-modal generation model, where the information captured by our vision-language model is leveraged as a high-level language condition in combination with a low-level image condition, jointly guiding the multi-modal generation process. We conduct comprehensive studies on the nuScenes, and NuInteract datasets to validate the effectiveness of our framework. Our method achieves state-of-the-art performance. We will release the code publicly on GitHub https://github.com/dtc111111/GaussianDWM.

