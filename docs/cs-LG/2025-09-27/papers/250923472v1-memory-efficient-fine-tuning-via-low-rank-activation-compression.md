---
layout: default
title: Memory-Efficient Fine-Tuning via Low-Rank Activation Compression
---

# Memory-Efficient Fine-Tuning via Low-Rank Activation Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23472" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23472v1</a>
  <a href="https://arxiv.org/pdf/2509.23472.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23472v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23472v1', 'Memory-Efficient Fine-Tuning via Low-Rank Activation Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiang-Xin Shi, Wen-Da Wei, Jin-Fei Qi, Xuanyu Chen, Tong Wei, Yu-Feng Li

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-27

**🔗 代码/项目**: [GITHUB](https://github.com/shijxcs/meft)

---

## 💡 一句话要点

**提出LoRAct，通过低秩激活压缩实现高效的参数微调，显著降低内存占用。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `参数高效微调` `低秩激活压缩` `内存优化` `模型部署` `正交分解`

## 📋 核心要点

1. 现有参数高效微调方法虽然减少了可训练参数，但内存开销仍然巨大，限制了实际部署。
2. LoRAct通过观察到激活的低秩特性，提出在线低秩激活压缩，无需校准数据，更灵活通用。
3. LoRAct采用新型采样正交分解算法，提升计算效率，并减少了80%的激活内存，性能有竞争力。

## 📝 摘要（中文）

随着基础模型的发展，参数高效微调范式受到了广泛关注。尽管已经提出了许多减少可训练参数数量的方法，但其巨大的内存开销仍然是阻碍实际部署的关键瓶颈。本文观察到，模型激活构成了内存消耗的主要来源，尤其是在大批量和长上下文长度下；然而，激活的秩始终保持较低。受此启发，我们提出了一种内存高效的微调方法：低秩激活压缩（LoRAct）。与先前的工作不同，LoRAct提供了一种更灵活和通用的压缩策略，可以在前向传播期间在线应用，而无需任何校准数据。此外，LoRAct还包含一种专门为低秩矩阵设计的新型基于采样的正交分解算法，与广泛使用的RSVD相比，提供了更高的计算效率和更严格的误差界限。在视觉和语言任务上的实验证明了LoRAct的有效性。值得注意的是，与广泛采用的LoRA方法相比，LoRAct进一步减少了约80%的激活内存，同时保持了具有竞争力的性能。源代码可在https://github.com/shijxcs/meft获取。

## 🔬 方法详解

**问题定义**：论文旨在解决参数高效微调中模型激活带来的巨大内存开销问题。现有方法虽然减少了可训练参数的数量，但忽略了激活所占用的内存，尤其是在大批量和长上下文场景下，这成为了模型部署的瓶颈。

**核心思路**：论文的核心思路是利用模型激活的低秩特性，通过低秩矩阵分解和压缩技术，在不显著影响模型性能的前提下，大幅降低激活所占用的内存空间。核心在于在线压缩，避免了离线校准的需要。

**技术框架**：LoRAct的核心框架是在前向传播过程中，对模型的激活进行低秩分解和压缩。具体流程包括：1) 激活采样：从激活矩阵中采样一部分列；2) 正交分解：对采样得到的矩阵进行正交分解，得到低秩表示；3) 激活重构：利用低秩表示重构激活矩阵，并进行后续计算。整个过程在线进行，无需额外的校准数据。

**关键创新**：LoRAct的关键创新在于：1) 提出了一种灵活通用的在线低秩激活压缩策略，无需校准数据；2) 设计了一种基于采样的正交分解算法，专门针对低秩矩阵优化，提高了计算效率，并提供了更严格的误差界限。这种算法优于传统的随机奇异值分解（RSVD）。

**关键设计**：LoRAct的关键设计包括：1) 采样策略：如何选择最具代表性的激活列进行采样，以保证重构的准确性；2) 低秩维度选择：如何确定低秩表示的维度，以在内存占用和性能之间取得平衡；3) 正交分解算法：具体采用哪种正交分解算法，以及如何优化算法的计算效率。论文提出的采样正交分解算法是关键。

## 📊 实验亮点

实验结果表明，LoRAct在视觉和语言任务上均表现出色。与LoRA相比，LoRAct进一步减少了约80%的激活内存，同时保持了具有竞争力的性能。这表明LoRAct是一种有效的内存高效微调方法，可以在不牺牲性能的前提下，显著降低内存占用。

## 🎯 应用场景

LoRAct可应用于各种需要高效微调的大型模型，尤其是在资源受限的设备上，例如移动设备和边缘计算设备。该方法可以降低模型部署的内存需求，使得在这些设备上运行大型模型成为可能。此外，LoRAct还可以加速模型的训练和推理过程，提高模型的效率。

## 📄 摘要（原文）

> The parameter-efficient fine-tuning paradigm has garnered significant attention with the advancement of foundation models. Although numerous methods have been proposed to reduce the number of trainable parameters, their substantial memory overhead remains a critical bottleneck that hinders practical deployment. In this paper, we observe that model activations constitute a major source of memory consumption, especially under large batch sizes and long context lengths; however, the rank of the activations remains consistently low. Motivated by this insight, we propose a memory-efficient fine-tuning approach Low-Rank Activation Compression (LoRAct). Unlike prior work, LoRAct provides a more flexible and versatile compressing strategy that can be applied online during the forward pass without the need for any calibration data. Moreover, LoRAct incorporates a novel sampling-based orthogonal decomposition algorithm specifically designed for low-rank matrices, offering improved computational efficiency and a tighter error bound compared to the widely used RSVD. Experiments on both vision and language tasks demonstrate the effectiveness of LoRAct. Notably, LoRAct further reduces activation memory by approximately 80% in comparison with the widely adopted LoRA method, while maintaining competitive performance. The source code is available at https://github.com/shijxcs/meft.

