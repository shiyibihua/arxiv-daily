---
layout: default
title: TurboDiffusion: Accelerating Video Diffusion Models by 100-200 Times
---

# TurboDiffusion: Accelerating Video Diffusion Models by 100-200 Times

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16093" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16093v1</a>
  <a href="https://arxiv.org/pdf/2512.16093.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16093v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16093v1', 'TurboDiffusion: Accelerating Video Diffusion Models by 100-200 Times')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jintao Zhang, Kaiwen Zheng, Kai Jiang, Haoxu Wang, Ion Stoica, Joseph E. Gonzalez, Jianfei Chen, Jun Zhu

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/thu-ml/TurboDiffusion)

---

## 💡 一句话要点

**TurboDiffusion：通过多重加速策略实现视频扩散模型100-200倍的加速。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频生成` `扩散模型` `模型加速` `注意力机制` `模型量化` `步骤蒸馏` `稀疏注意力`

## 📋 核心要点

1. 现有视频扩散模型计算复杂度高，生成速度慢，难以满足实时性要求。
2. TurboDiffusion通过注意力加速、步骤蒸馏和模型量化等多重策略，显著降低计算量。
3. 实验表明，TurboDiffusion在保证视频质量的同时，实现了100-200倍的加速效果。

## 📝 摘要（中文）

TurboDiffusion是一个视频生成加速框架，能够在保持视频质量的同时，将端到端扩散生成速度提高100-200倍。TurboDiffusion主要依赖于以下几个加速组件：（1）注意力加速：TurboDiffusion使用低比特SageAttention和可训练的稀疏线性注意力（SLA）来加速注意力计算。（2）步骤蒸馏：TurboDiffusion采用rCM进行高效的步骤蒸馏。（3）W8A8量化：TurboDiffusion将模型参数和激活量化为8位，以加速线性层并压缩模型。此外，TurboDiffusion还包含其他一些工程优化。我们在Wan2.2-I2V-14B-720P、Wan2.1-T2V-1.3B-480P、Wan2.1-T2V-14B-720P和Wan2.1-T2V-14B-480P模型上进行了实验。实验结果表明，即使在单个RTX 5090 GPU上，TurboDiffusion也能实现100-200倍的视频生成加速，同时保持相当的视频质量。包含模型检查点和易于使用的代码的GitHub存储库可在https://github.com/thu-ml/TurboDiffusion上找到。

## 🔬 方法详解

**问题定义**：现有视频扩散模型在生成高质量视频时，计算复杂度极高，生成速度慢，难以满足实际应用中对实时性的需求。尤其是在高分辨率视频生成方面，计算瓶颈更加突出。因此，如何加速视频扩散模型的生成速度，同时保持视频质量，是一个重要的研究问题。

**核心思路**：TurboDiffusion的核心思路是通过多方面的优化，降低视频扩散模型的计算复杂度，从而加速生成过程。具体来说，它从注意力机制、模型蒸馏和模型量化三个主要方面入手，并结合其他工程优化手段，实现了显著的加速效果。这种多管齐下的方法能够有效地解决视频扩散模型速度慢的问题。

**技术框架**：TurboDiffusion的整体框架主要包含以下几个模块：1) **注意力加速模块**：使用低比特SageAttention和可训练的稀疏线性注意力（SLA）来降低注意力计算的复杂度。2) **步骤蒸馏模块**：采用rCM方法进行高效的步骤蒸馏，减少扩散过程所需的迭代次数。3) **模型量化模块**：将模型参数和激活量化为8位（W8A8），以加速线性层计算并压缩模型大小。4) **工程优化模块**：包含其他一些工程优化手段，进一步提升生成速度。

**关键创新**：TurboDiffusion的关键创新在于其综合性的加速策略。它不仅仅依赖于单一的优化方法，而是将注意力加速、步骤蒸馏和模型量化等多种技术结合起来，形成一个完整的加速框架。这种综合性的方法能够充分利用各种优化技术的优势，从而实现更高的加速效果。此外，可训练的稀疏线性注意力（SLA）也是一个重要的创新点，它能够在降低计算复杂度的同时，保持模型的表达能力。

**关键设计**：在注意力加速方面，SageAttention的具体比特数选择以及SLA的稀疏模式设计是关键。在步骤蒸馏方面，rCM的具体参数设置会影响蒸馏效果。在模型量化方面，W8A8量化的具体实现方式，例如量化范围和舍入策略，会影响模型的精度。此外，损失函数的选择和优化器的设置也会影响模型的训练效果。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16093v1/src/figs/original/outputs_1.3B/frames/12-1.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16093v1/src/figs/turbodiffusion/outputs_1.3B/frames/12-1.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16093v1/src/figs/i2v/original/outputs_A14B_720p/frames/1-1.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TurboDiffusion在多个视频生成模型上实现了100-200倍的加速，同时保持了与原始模型相当的视频质量。即使在单张RTX 5090 GPU上，也能达到如此显著的加速效果，证明了该框架的有效性和实用性。开源代码和模型权重也为后续研究和应用提供了便利。

## 🎯 应用场景

TurboDiffusion的加速技术可广泛应用于视频生成、视频编辑、虚拟现实、游戏开发等领域。它能够降低视频生成的时间成本和硬件需求，使得高质量视频内容的创作更加便捷。未来，TurboDiffusion有望推动视频生成技术在移动设备和边缘计算平台上的应用，实现更广泛的普及。

## 📄 摘要（原文）

> We introduce TurboDiffusion, a video generation acceleration framework that can speed up end-to-end diffusion generation by 100-200x while maintaining video quality. TurboDiffusion mainly relies on several components for acceleration: (1) Attention acceleration: TurboDiffusion uses low-bit SageAttention and trainable Sparse-Linear Attention (SLA) to speed up attention computation. (2) Step distillation: TurboDiffusion adopts rCM for efficient step distillation. (3) W8A8 quantization: TurboDiffusion quantizes model parameters and activations to 8 bits to accelerate linear layers and compress the model. In addition, TurboDiffusion incorporates several other engineering optimizations.
>   We conduct experiments on the Wan2.2-I2V-14B-720P, Wan2.1-T2V-1.3B-480P, Wan2.1-T2V-14B-720P, and Wan2.1-T2V-14B-480P models. Experimental results show that TurboDiffusion achieves 100-200x speedup for video generation even on a single RTX 5090 GPU, while maintaining comparable video quality. The GitHub repository, which includes model checkpoints and easy-to-use code, is available at https://github.com/thu-ml/TurboDiffusion.

