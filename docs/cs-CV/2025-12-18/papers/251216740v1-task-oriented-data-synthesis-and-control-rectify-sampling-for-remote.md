---
layout: default
title: Task-Oriented Data Synthesis and Control-Rectify Sampling for Remote Sensing Semantic Segmentation
---

# Task-Oriented Data Synthesis and Control-Rectify Sampling for Remote Sensing Semantic Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16740" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16740v1</a>
  <a href="https://arxiv.org/pdf/2512.16740.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16740v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16740v1', 'Task-Oriented Data Synthesis and Control-Rectify Sampling for Remote Sensing Semantic Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunkai Yang, Yudong Zhang, Kunquan Zhang, Jinxiao Zhang, Xinying Chen, Haohuan Fu, Runmin Dong

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出TODSynth框架，用于遥感语义分割任务的数据合成与控制优化。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感图像语义分割` `数据合成` `可控生成` `扩散模型` `Transformer`

## 📋 核心要点

1. 遥感图像语义分割依赖大量标注数据，人工标注成本高昂，合成数据是潜在解决方案。
2. 提出TODSynth框架，包含MM-DiT和CRFM，利用任务反馈指导数据合成，提升数据质量。
3. 实验表明，该方法优于现有可控生成方法，生成的数据更稳定，更适合遥感语义分割任务。

## 📝 摘要（中文）

随着可控生成技术的快速发展，训练数据合成已成为扩展遥感（RS）标注数据集和减少人工标注的一种有前景的方法。然而，语义掩码控制的复杂性和采样质量的不确定性通常限制了合成数据在下游语义分割任务中的效用。为了应对这些挑战，我们提出了一个面向任务的数据合成框架（TODSynth），包括一个具有统一三重注意力的多模态扩散Transformer（MM-DiT）和一个由任务反馈指导的即插即用采样策略。基于强大的DiT生成基础模型，我们系统地评估了不同的控制方案，表明文本-图像-掩码联合注意力方案与图像和掩码分支的完全微调相结合，显著提高了遥感语义分割数据合成的有效性，尤其是在少样本和复杂场景中。此外，我们提出了一种控制校正流匹配（CRFM）方法，该方法在早期高可塑性阶段动态调整由语义损失引导的采样方向，从而减轻了生成图像的不稳定性，并弥合了合成数据与下游分割任务之间的差距。大量实验表明，我们的方法始终优于最先进的可控生成方法，为遥感语义分割生成更稳定和面向任务的合成数据。

## 🔬 方法详解

**问题定义**：遥感图像语义分割任务需要大量的标注数据，而人工标注成本高昂。现有的数据合成方法在控制语义掩码的复杂性和保证采样质量方面存在挑战，导致合成数据在下游语义分割任务中的效用受限。具体来说，如何有效地融合文本、图像和掩码信息，以及如何保证合成数据的质量和稳定性是亟待解决的问题。

**核心思路**：论文的核心思路是提出一个面向任务的数据合成框架TODSynth，该框架通过多模态扩散Transformer（MM-DiT）实现对文本、图像和掩码的联合控制，并通过控制校正流匹配（CRFM）方法动态调整采样方向，从而生成更稳定和面向任务的合成数据。这种设计旨在弥合合成数据与真实数据之间的差距，提高合成数据在下游语义分割任务中的有效性。

**技术框架**：TODSynth框架主要包含两个核心模块：MM-DiT和CRFM。MM-DiT是一个基于扩散Transformer的生成模型，它采用统一的三重注意力机制，能够有效地融合文本、图像和掩码信息。CRFM是一种采样策略，它在扩散模型的采样过程中，利用语义损失动态调整采样方向，从而提高生成图像的质量和稳定性。整个流程包括：首先，使用MM-DiT生成合成图像和对应的语义掩码；然后，使用CRFM方法优化生成过程，提高合成数据的质量；最后，将合成数据用于训练遥感图像语义分割模型。

**关键创新**：论文的关键创新在于以下几个方面：1) 提出了MM-DiT，它采用统一的三重注意力机制，能够有效地融合文本、图像和掩码信息，实现对合成数据的精确控制。2) 提出了CRFM方法，它在扩散模型的采样过程中，利用语义损失动态调整采样方向，从而提高生成图像的质量和稳定性。3) 系统地评估了不同的控制方案，并证明了文本-图像-掩码联合注意力方案与图像和掩码分支的完全微调相结合，能够显著提高遥感语义分割数据合成的有效性。

**关键设计**：MM-DiT的关键设计包括：采用DiT作为生成骨干网络，并在此基础上引入统一的三重注意力机制，用于融合文本、图像和掩码信息。CRFM的关键设计包括：在扩散模型的采样过程中，计算生成图像的语义损失，并利用该损失动态调整采样方向。此外，论文还对不同的控制方案进行了系统评估，并选择了文本-图像-掩码联合注意力方案与图像和掩码分支的完全微调相结合的方案。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16740v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16740v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16740v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，TODSynth框架在遥感语义分割数据合成方面优于现有方法。具体来说，该方法能够生成更稳定、更面向任务的合成数据，从而显著提高下游语义分割任务的性能。在少样本和复杂场景下，TODSynth的优势更加明显，能够有效缓解数据稀缺问题，提升分割精度。

## 🎯 应用场景

该研究成果可应用于遥感图像语义分割领域，通过合成数据增强训练集，降低人工标注成本，提高分割精度。尤其在少样本或复杂场景下，该方法具有显著优势，可用于灾害监测、城市规划、农业估产等领域，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> With the rapid progress of controllable generation, training data synthesis has become a promising way to expand labeled datasets and alleviate manual annotation in remote sensing (RS). However, the complexity of semantic mask control and the uncertainty of sampling quality often limit the utility of synthetic data in downstream semantic segmentation tasks. To address these challenges, we propose a task-oriented data synthesis framework (TODSynth), including a Multimodal Diffusion Transformer (MM-DiT) with unified triple attention and a plug-and-play sampling strategy guided by task feedback. Built upon the powerful DiT-based generative foundation model, we systematically evaluate different control schemes, showing that a text-image-mask joint attention scheme combined with full fine-tuning of the image and mask branches significantly enhances the effectiveness of RS semantic segmentation data synthesis, particularly in few-shot and complex-scene scenarios. Furthermore, we propose a control-rectify flow matching (CRFM) method, which dynamically adjusts sampling directions guided by semantic loss during the early high-plasticity stage, mitigating the instability of generated images and bridging the gap between synthetic data and downstream segmentation tasks. Extensive experiments demonstrate that our approach consistently outperforms state-of-the-art controllable generation methods, producing more stable and task-oriented synthetic data for RS semantic segmentation.

