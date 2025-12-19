---
layout: default
title: VIVA: VLM-Guided Instruction-Based Video Editing with Reward Optimization
---

# VIVA: VLM-Guided Instruction-Based Video Editing with Reward Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16906" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16906v1</a>
  <a href="https://arxiv.org/pdf/2512.16906.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16906v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16906v1', 'VIVA: VLM-Guided Instruction-Based Video Editing with Reward Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyan Cong, Haotian Yang, Angtian Wang, Yizhi Wang, Yiding Yang, Canyu Zhang, Chongyang Ma

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**VIVA：基于VLM引导和奖励优化的指令驱动视频编辑框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频编辑` `指令驱动` `视觉语言模型` `扩散模型` `奖励优化`

## 📋 核心要点

1. 现有基于扩散模型的视频编辑方法在处理复杂指令时泛化能力有限，主要受限于训练数据简单。
2. VIVA利用VLM提取视觉对齐的指令表示，并采用Edit-GRPO进行奖励优化，提升编辑质量和指令遵循度。
3. 实验表明，VIVA在指令遵循、泛化能力和编辑质量上超越了现有技术水平，效果显著。

## 📝 摘要（中文）

本文提出VIVA，一个可扩展的指令驱动视频编辑框架，它利用VLM引导的编码和奖励优化来解决现有方法泛化能力不足的问题。该框架包含一个基于VLM的指导器，它将文本指令、源视频首帧和可选的参考图像编码为视觉对齐的指令表示，为扩散Transformer主干网络提供细粒度的空间和语义上下文。此外，提出了Edit-GRPO后训练阶段，将Group Relative Policy Optimization应用于视频编辑领域，使用相对奖励直接优化模型，使其生成符合指令、保持内容一致且美观的编辑结果。同时，设计了一个数据构建流程，用于合成生成多样且高质量的视频-指令对数据。大量实验表明，VIVA在指令遵循、泛化能力和编辑质量方面优于现有方法。

## 🔬 方法详解

**问题定义**：指令驱动的视频编辑旨在根据自然语言指令修改输入视频，同时保持内容一致性和时间连贯性。现有基于扩散模型的方法通常在简单的编辑操作配对数据上训练，这限制了它们泛化到多样化和复杂的真实世界指令的能力。

**核心思路**：VIVA的核心思路是利用视觉语言模型（VLM）来更好地理解指令，并结合奖励优化来提升编辑质量。VLM能够将文本指令与视频内容对齐，提供更丰富的上下文信息。奖励优化则直接驱动模型生成更符合人类偏好的编辑结果。

**技术框架**：VIVA框架主要包含两个阶段：VLM引导的编码阶段和Edit-GRPO后训练阶段。在编码阶段，VLM将文本指令、源视频首帧和可选的参考图像编码为视觉对齐的指令表示。然后，这些表示被输入到扩散Transformer主干网络中进行视频编辑。在Edit-GRPO阶段，使用相对奖励优化模型，使其生成更符合指令、保持内容一致且美观的编辑结果。

**关键创新**：VIVA的关键创新在于以下两点：1) 利用VLM进行指令编码，从而更好地理解指令的语义和视觉信息；2) 提出Edit-GRPO后训练方法，直接优化模型的编辑质量，使其更符合人类偏好。与现有方法相比，VIVA能够更好地处理复杂指令，并生成更高质量的编辑结果。

**关键设计**：VLM指导器使用预训练的视觉语言模型，并针对视频编辑任务进行微调。Edit-GRPO采用Group Relative Policy Optimization，通过比较不同编辑结果的相对质量来优化模型。此外，还设计了一个数据构建流程，用于合成生成多样且高质量的视频-指令对数据，以增强模型的泛化能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16906v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16906v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16906v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，VIVA在多个视频编辑任务上取得了显著的性能提升。与现有最先进的方法相比，VIVA在指令遵循度、内容一致性和编辑质量方面均有明显优势。具体性能数据和对比基线信息请参考论文原文。

## 🎯 应用场景

VIVA技术可应用于电影制作、广告设计、社交媒体内容生成等领域，实现快速、高质量的视频编辑。该技术能够降低视频编辑的门槛，让用户通过简单的自然语言指令即可完成复杂的编辑任务，具有广阔的应用前景和商业价值。

## 📄 摘要（原文）

> Instruction-based video editing aims to modify an input video according to a natural-language instruction while preserving content fidelity and temporal coherence. However, existing diffusion-based approaches are often trained on paired data of simple editing operations, which fundamentally limits their ability to generalize to diverse and complex, real-world instructions. To address this generalization gap, we propose VIVA, a scalable framework for instruction-based video editing that leverages VLM-guided encoding and reward optimization. First, we introduce a VLM-based instructor that encodes the textual instruction, the first frame of the source video, and an optional reference image into visually-grounded instruction representations, providing fine-grained spatial and semantic context for the diffusion transformer backbone. Second, we propose a post-training stage, Edit-GRPO, which adapts Group Relative Policy Optimization to the domain of video editing, directly optimizing the model for instruction-faithful, content-preserving, and aesthetically pleasing edits using relative rewards. Furthermore, we propose a data construction pipeline designed to synthetically generate diverse, high-fidelity paired video-instruction data of basic editing operations. Extensive experiments show that VIVA achieves superior instruction following, generalization, and editing quality over state-of-the-art methods. Website: https://viva-paper.github.io

