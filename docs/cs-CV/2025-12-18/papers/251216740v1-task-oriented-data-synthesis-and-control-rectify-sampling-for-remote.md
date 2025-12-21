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

**关键词**: `遥感语义分割` `数据合成` `可控生成` `扩散模型` `多模态学习`

## 📋 核心要点

1. 遥感图像语义分割依赖大量标注数据，但人工标注成本高昂，可控数据生成是潜在解决方案。
2. TODSynth框架利用多模态扩散Transformer和任务反馈采样策略，提升合成数据的质量和任务相关性。
3. 实验表明，该方法在少样本和复杂场景下，显著优于现有可控生成方法，提升了遥感语义分割性能。

## 📝 摘要（中文）

随着可控生成技术的快速发展，训练数据合成已成为扩展遥感（RS）标注数据集和缓解人工标注负担的一种有前景的方法。然而，语义掩码控制的复杂性和采样质量的不确定性常常限制了合成数据在下游语义分割任务中的效用。为了解决这些挑战，我们提出了一个面向任务的数据合成框架（TODSynth），包括一个具有统一三重注意力的多模态扩散Transformer（MM-DiT）和一个由任务反馈指导的即插即用采样策略。基于强大的DiT生成基础模型，我们系统地评估了不同的控制方案，表明文本-图像-掩码联合注意力方案与图像和掩码分支的完全微调相结合，显著增强了遥感语义分割数据合成的有效性，尤其是在少样本和复杂场景中。此外，我们提出了一种控制校正流匹配（CRFM）方法，该方法在早期高可塑性阶段动态调整采样方向，由语义损失引导，从而减轻了生成图像的不稳定性，并弥合了合成数据与下游分割任务之间的差距。大量实验表明，我们的方法始终优于最先进的可控生成方法，为遥感语义分割生成更稳定和面向任务的合成数据。

## 🔬 方法详解

**问题定义**：遥感图像语义分割任务需要大量的标注数据，而人工标注成本高、效率低。现有的数据合成方法难以有效控制生成数据的语义信息，且合成数据的质量和下游任务的相关性不足，导致其在实际应用中效果不佳。尤其是在少样本和复杂场景下，问题更为突出。

**核心思路**：本文的核心思路是提出一个面向任务的数据合成框架TODSynth，通过多模态扩散模型和任务反馈机制，实现对生成数据的精确控制和优化。具体来说，利用文本、图像和掩码等多模态信息，指导扩散模型的生成过程，并引入下游分割任务的损失函数，动态调整采样方向，从而生成更符合任务需求的合成数据。

**技术框架**：TODSynth框架主要包含两个核心模块：多模态扩散Transformer（MM-DiT）和控制校正流匹配（CRFM）。MM-DiT是一个基于DiT的生成模型，通过统一的三重注意力机制，融合文本、图像和掩码等多模态信息。CRFM则是一种采样策略，它在扩散模型的采样过程中，利用下游分割任务的语义损失，动态调整采样方向，从而优化生成数据的质量。整体流程是：首先，利用MM-DiT生成初步的合成数据；然后，通过CRFM策略，利用下游分割任务的反馈，对生成数据进行优化，最终得到高质量的合成数据。

**关键创新**：本文的关键创新在于：1) 提出了一个统一的三重注意力机制，能够有效融合文本、图像和掩码等多模态信息，实现对生成数据的精确控制。2) 提出了控制校正流匹配（CRFM）方法，利用下游分割任务的反馈，动态调整采样方向，从而优化生成数据的质量，弥合了合成数据与真实数据之间的差距。

**关键设计**：MM-DiT采用DiT作为基础模型，并引入了统一的三重注意力机制，将文本、图像和掩码信息融合到Transformer的每一层。CRFM的关键在于语义损失的计算和采样方向的调整。具体来说，利用下游分割模型的预测结果，计算生成数据与真实数据之间的语义损失，然后利用该损失的梯度，调整扩散模型的采样方向。此外，还设计了一系列参数，用于控制CRFM的强度和优化过程。

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

实验结果表明，TODSynth框架在遥感语义分割任务中取得了显著的性能提升。与现有最先进的可控生成方法相比，TODSynth能够生成更稳定、更面向任务的合成数据。具体来说，在少样本场景下，TODSynth的性能提升尤为明显，能够有效缓解数据稀缺带来的问题。此外，TODSynth在复杂场景下的表现也优于其他方法，表明其具有更强的泛化能力。

## 🎯 应用场景

该研究成果可广泛应用于遥感图像语义分割领域，尤其是在缺乏标注数据或标注成本高昂的情况下。例如，可以用于城市规划、环境监测、灾害评估等领域。通过合成高质量的训练数据，可以显著提升遥感图像语义分割模型的性能，降低人工标注的成本，加速相关技术的应用和发展。

## 📄 摘要（原文）

> With the rapid progress of controllable generation, training data synthesis has become a promising way to expand labeled datasets and alleviate manual annotation in remote sensing (RS). However, the complexity of semantic mask control and the uncertainty of sampling quality often limit the utility of synthetic data in downstream semantic segmentation tasks. To address these challenges, we propose a task-oriented data synthesis framework (TODSynth), including a Multimodal Diffusion Transformer (MM-DiT) with unified triple attention and a plug-and-play sampling strategy guided by task feedback. Built upon the powerful DiT-based generative foundation model, we systematically evaluate different control schemes, showing that a text-image-mask joint attention scheme combined with full fine-tuning of the image and mask branches significantly enhances the effectiveness of RS semantic segmentation data synthesis, particularly in few-shot and complex-scene scenarios. Furthermore, we propose a control-rectify flow matching (CRFM) method, which dynamically adjusts sampling directions guided by semantic loss during the early high-plasticity stage, mitigating the instability of generated images and bridging the gap between synthetic data and downstream segmentation tasks. Extensive experiments demonstrate that our approach consistently outperforms state-of-the-art controllable generation methods, producing more stable and task-oriented synthetic data for RS semantic segmentation.

