---
layout: default
title: Orthogonal Finetuning Made Scalable
---

# Orthogonal Finetuning Made Scalable

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19847" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19847v2</a>
  <a href="https://arxiv.org/pdf/2506.19847.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19847v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19847v2', 'Orthogonal Finetuning Made Scalable')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeju Qiu, Weiyang Liu, Adrian Weller, Bernhard Schölkopf

**分类**: cs.LG, cs.AI, cs.CL, cs.CV

**发布日期**: 2025-06-24 (更新: 2025-10-14)

**备注**: EMNLP 2025 Main (18 pages, 7 figures, project page: https://spherelab.ai/oftv2/)

---

## 💡 一句话要点

**提出OFTv2以解决正交微调的计算瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `正交微调` `计算效率` `深度学习` `量化模型` `Cayley-Neumann参数化`

## 📋 核心要点

1. 现有的正交微调方法在计算和内存需求上存在显著瓶颈，限制了其实际应用。
2. 论文提出OFTv2，通过输入中心的重构和矩阵-向量乘法，显著降低计算复杂度。
3. 实验结果表明，OFTv2在训练速度和内存使用上均有显著提升，且在量化模型微调中表现优越。

## 📝 摘要（中文）

正交微调（OFT）提供了高效的参数适应能力，同时防止灾难性遗忘，但其高运行时和内存需求限制了实际应用。我们识别出OFT的核心计算瓶颈在于其以权重为中心的实现，依赖于代价高昂的矩阵乘法，复杂度为立方。为此，我们提出了OFTv2，一种以输入为中心的重构方法，利用矩阵-向量乘法（即无矩阵计算），将计算成本降低到平方级别。此外，我们引入了Cayley-Neumann参数化，这是一种高效的正交参数化方法，通过截断的Neumann级数近似Cayley变换中的矩阵逆。这些修改使OFTv2在不影响性能的情况下，实现了训练速度提高至10倍，GPU内存使用降低至3倍。我们还扩展了OFTv2以支持量化基础模型的微调，并显示其在训练稳定性、效率和内存使用方面优于流行的QLoRA。

## 🔬 方法详解

**问题定义**：本论文旨在解决正交微调（OFT）在实际应用中面临的高计算和内存需求问题。现有方法依赖于复杂度为立方的矩阵乘法，导致运行效率低下。

**核心思路**：论文提出OFTv2，通过将计算重心转向输入，采用矩阵-向量乘法来降低计算复杂度至平方级别，从而提高训练效率和降低内存消耗。

**技术框架**：OFTv2的整体架构包括输入重构模块和Cayley-Neumann参数化模块。输入重构模块负责将输入数据转化为适合的格式，而Cayley-Neumann模块则用于高效地进行正交参数化。

**关键创新**：OFTv2的主要创新在于其输入中心的重构方法和Cayley-Neumann参数化，这与传统的权重中心方法形成鲜明对比，显著提升了计算效率。

**关键设计**：在OFTv2中，采用了矩阵-向量乘法替代矩阵乘法，设计了高效的Cayley-Neumann参数化来近似矩阵逆，确保在降低计算复杂度的同时保持模型性能。具体的参数设置和损失函数设计在实验中进行了优化。

## 📊 实验亮点

OFTv2在训练速度上实现了最高10倍的提升，同时GPU内存使用降低至3倍。与流行的QLoRA相比，OFTv2在训练稳定性、效率和内存使用方面均表现出显著优势，证明了其在量化模型微调中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、计算机视觉等需要高效微调的深度学习模型。OFTv2的高效性使其能够在资源受限的环境中进行大规模模型的微调，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Orthogonal finetuning (OFT) offers highly parameter-efficient adaptation while preventing catastrophic forgetting, but its high runtime and memory demands limit practical deployment. We identify the core computational bottleneck in OFT as its weight-centric implementation, which relies on costly matrix-matrix multiplications with cubic complexity. To overcome this, we propose OFTv2, an input-centric reformulation that instead uses matrix-vector multiplications (i.e., matrix-free computation), reducing the computational cost to quadratic. We further introduce the Cayley-Neumann parameterization, an efficient orthogonal parameterization that approximates the matrix inversion in the Cayley transform via a truncated Neumann series. These modifications allow OFTv2 to achieve up to 10x faster training and 3x lower GPU memory usage without compromising performance. In addition, we extend OFTv2 to support finetuning quantized foundation models and show that it outperforms the popular QLoRA in training stability, efficiency, and memory usage.

