---
layout: default
title: Bridging the Gap Between Promise and Performance for Microscaling FP4 Quantization
---

# Bridging the Gap Between Promise and Performance for Microscaling FP4 Quantization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23202" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23202v2</a>
  <a href="https://arxiv.org/pdf/2509.23202.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23202v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23202v2', 'Bridging the Gap Between Promise and Performance for Microscaling FP4 Quantization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vage Egiazarian, Roberto L. Castro, Denis Kuznedelev, Andrei Panferov, Eldar Kurtic, Shubhra Pandit, Alexandre Marques, Mark Kurtz, Saleh Ashkboos, Torsten Hoefler, Dan Alistarh

**分类**: cs.LG

**发布日期**: 2025-09-27 (更新: 2025-10-16)

---

## 💡 一句话要点

**提出MR-GPTQ，针对FP4量化特性优化GPTQ算法，提升LLM推理性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `FP4量化` `GPTQ` `大型语言模型` `模型推理` `硬件加速`

## 📋 核心要点

1. 现有方法在FP4量化中面临挑战，NVFP4的小组大小限制了离群值缓解，MXFP4的二次幂缩放量化引入了高误差。
2. MR-GPTQ通过块状Hadamard变换和格式特定优化，为FP4量身定制量化过程，解决了现有方法的局限性。
3. 实验表明，MR-GPTQ在NVIDIA B200和RTX5090上实现了显著的加速，并提升了MXFP4的精度，接近NVFP4的水平。

## 📝 摘要（中文）

本文全面研究了NVIDIA和AMD GPU上硬件加速的微缩放4位浮点格式MXFP4和NVFP4在大型语言模型（LLM）推理中的应用，揭示了其承诺与实际性能之间的差距。分析表明，由于NVFP4的小组大小抵消了传统的离群值缓解技术，以及MXFP4的二次幂缩放量化导致的高误差，现有方法在FP4上表现不佳。为此，本文提出了一种名为Micro-Rotated-GPTQ（MR-GPTQ）的GPTQ量化算法变体，通过块状Hadamard变换和特定于格式的优化，专门针对FP4的独特属性定制量化过程。通过高性能GPU内核，MR-GPTQ格式实现了可忽略的开销，并通过旋转融合到权重中以及快速在线计算激活来实现。在NVIDIA B200上，层级加速高达3.6倍，端到端加速高达2.2倍；在RTX5090上，层级加速高达6倍，端到端加速高达4倍。实验结果表明，MR-GPTQ匹配或优于最先进的精度，显著提升了MXFP4的性能，使其接近NVFP4的精度。结论是，FP4并非INT4的自动升级，但像MR-GPTQ这样针对格式的专用方法可以开启精度-性能权衡的新前沿。

## 🔬 方法详解

**问题定义**：论文旨在解决在大型语言模型（LLM）推理中使用微缩放4位浮点格式（FP4，具体包括MXFP4和NVFP4）进行量化时，现有方法无法充分发挥其硬件加速优势的问题。现有方法在FP4量化中面临精度损失和性能瓶颈，无法实现理论上的加速效果。NVFP4的小组大小限制了离群值缓解策略的应用，而MXFP4的二次幂缩放量化引入了较大的量化误差。

**核心思路**：论文的核心思路是针对FP4格式的特性，定制量化算法。通过引入Micro-Rotated-GPTQ (MR-GPTQ)，一种基于GPTQ的变体，利用块状Hadamard变换和格式特定的优化，来减少量化误差并提高推理速度。这种定制化的方法旨在弥合FP4的理论性能与实际性能之间的差距。

**技术框架**：MR-GPTQ的整体框架基于GPTQ算法，主要包含以下几个阶段：1) 权重预处理：使用块状Hadamard变换对权重进行旋转，以减少量化误差。2) 量化：使用针对MXFP4和NVFP4格式优化的量化方法，将权重转换为FP4格式。3) 推理：使用优化的GPU内核进行推理，将旋转融合到权重中，并快速在线计算激活。

**关键创新**：论文的关键创新在于针对FP4格式的特性，对GPTQ算法进行了定制化修改。具体包括：1) 块状Hadamard变换：通过旋转权重，减少量化误差，提高精度。2) 格式特定优化：针对MXFP4和NVFP4的特性，设计了不同的量化策略，以最大程度地减少量化误差。3) 高性能GPU内核：开发了优化的GPU内核，实现了旋转融合和快速激活计算，提高了推理速度。

**关键设计**：MR-GPTQ的关键设计包括：1) 块大小的选择：Hadamard变换的块大小需要根据模型的结构和FP4格式的特性进行调整。2) 量化策略：针对MXFP4的二次幂缩放特性，设计了特定的量化策略，以减少量化误差。3) 损失函数：使用GPTQ的损失函数，以最小化量化后的模型与原始模型之间的差异。

## 📊 实验亮点

实验结果表明，MR-GPTQ在NVIDIA B200上实现了高达3.6倍的层级加速和2.2倍的端到端加速，在RTX5090上实现了高达6倍的层级加速和4倍的端到端加速。此外，MR-GPTQ显著提升了MXFP4的精度，使其接近NVFP4的水平，证明了其在FP4量化方面的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要低精度量化的大型语言模型推理场景，例如边缘设备部署、资源受限环境下的模型加速等。通过提升FP4量化的精度和性能，可以降低模型部署的成本，并提高推理效率，从而推动LLM在更广泛领域的应用。

## 📄 摘要（原文）

> The recent hardware-accelerated microscaling 4-bit floating-point formats such as MXFP4 and NVFP4, supported on NVIDIA and AMD GPUs, promise to revolutionize large language model (LLM) inference. Yet, their practical benefits remain unproven. We present the first comprehensive study of MXFP4 and NVFP4 for post-training quantization, revealing gaps between their promise and real-world performance. Our analysis shows that state-of-the-art methods struggle with FP4, due to two key issues: (1) NVFP4's small group size provably neutralizes traditional outlier mitigation techniques; (2) MXFP4's power-of-two scale quantization severely degrades accuracy due to high induced error. To bridge this gap, we introduce Micro-Rotated-GPTQ (MR-GPTQ), a variant of the classic GPTQ quantization algorithm that tailors the quantization process to FP4's unique properties, by using block-wise Hadamard transforms and format-specific optimizations. We support our proposal with a set of high-performance GPU kernels that enable the MR-GPTQ format with negligible overhead, by rotation fusion into the weights, and fast online computation of the activations. This leads to speedups vs. FP16 of up to 3.6x layer-wise, and 2.2x end-to-end on NVIDIA B200, and of 6x layer-wise and 4x end-to-end on RTX5090. Our extensive empirical evaluation demonstrates that MR-GPTQ matches or outperforms state-of-the-art accuracy, significantly boosting MXFP4, to the point where it can near the accuracy that of NVFP4. We conclude that, while FP4 is not an automatic upgrade over INT4, format-specialized methods like MR-GPTQ can unlock a new frontier of accuracy-performance trade-offs.

