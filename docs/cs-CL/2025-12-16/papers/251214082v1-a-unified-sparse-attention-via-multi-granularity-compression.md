---
layout: default
title: A Unified Sparse Attention via Multi-Granularity Compression
---

# A Unified Sparse Attention via Multi-Granularity Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14082" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14082v1</a>
  <a href="https://arxiv.org/pdf/2512.14082.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14082v1" onclick="toggleFavorite(this, '2512.14082v1', 'A Unified Sparse Attention via Multi-Granularity Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siran Liu, Zane Cao, Yongchao He

**分类**: cs.CL

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**UniSparse：一种通过多粒度压缩实现的统一稀疏注意力机制，加速LLM长文本处理。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏注意力` `长文本处理` `多粒度压缩` `大型语言模型` `自注意力机制`

## 📋 核心要点

1. 现有稀疏注意力方法在效率、通用性和训练成本之间存在权衡，限制了其在长文本处理中的应用。
2. UniSparse通过引入复合token和多粒度压缩，实现了动态、高效且硬件友好的稀疏注意力构建。
3. 实验表明，UniSparse在多种模态和任务中，显著提升了效率和准确率，优于现有稀疏注意力方法。

## 📝 摘要（中文）

为了提升大型语言模型（LLM）在多轮对话和程序分析等应用中对长上下文的理解和推理能力，本文提出了一种名为UniSparse的统一稀疏注意力机制。现有稀疏注意力方法存在权衡：基于训练的方法成本高昂，不能直接作为加速插件应用于其他模型；而推理时方法通常会牺牲效率或跨模态通用性。UniSparse引入了复合token的概念，即聚合多粒度上下文信息的紧凑表示。基于此，UniSparse通过多粒度压缩和块级选择动态构建稀疏注意力，从而在GPU上实现高效且硬件友好的执行。在从合成基准到实际应用的多种模态和任务中，UniSparse始终优于最先进的稀疏注意力方法（如MInference、XAttention、FlexPrefill），在达到≥99%的完整注意力准确率的同时，注意力计算速度比FlashAttention快高达2.61倍。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在处理长文本时，自注意力机制的计算复杂度呈平方增长，成为性能瓶颈。现有的稀疏注意力方法，要么需要额外的训练成本，要么在效率和通用性上有所妥协，难以同时满足高性能和易用性的需求。

**核心思路**：UniSparse的核心在于引入“复合token”的概念，将多个token压缩成一个更紧凑的表示，从而降低注意力计算的规模。通过多粒度压缩，模型可以灵活地选择不同粒度的上下文信息，在效率和信息损失之间取得平衡。

**技术框架**：UniSparse主要包含以下几个阶段：1) **多粒度压缩**：将原始token序列压缩成不同粒度的复合token序列。2) **块级选择**：根据一定的策略，选择重要的复合token块进行注意力计算。3) **注意力计算**：在选定的复合token块上执行稀疏注意力计算。4) **信息聚合**：将复合token的信息解压并聚合到原始token上。

**关键创新**：UniSparse的关键创新在于其统一的框架，能够通过多粒度压缩动态地构建稀疏注意力。与以往方法相比，UniSparse无需额外的训练，即可作为插件式加速模块应用于各种模型，并且在多种模态和任务中都表现出良好的性能。

**关键设计**：UniSparse的关键设计包括：1) **多粒度压缩策略**：可以使用平均池化、最大池化等方法进行压缩，也可以使用可学习的压缩模块。2) **块级选择策略**：可以使用基于重要性的选择、基于距离的选择等策略。3) **注意力计算方式**：可以使用标准的自注意力机制，也可以使用其他高效的注意力变体。

## 📊 实验亮点

UniSparse在多个模态和任务上都取得了显著的性能提升。例如，在合成基准测试中，UniSparse达到了≥99%的完整注意力准确率，同时注意力计算速度比FlashAttention快高达2.61倍。在实际应用中，UniSparse也优于其他稀疏注意力方法，例如MInference、XAttention和FlexPrefill。

## 🎯 应用场景

UniSparse具有广泛的应用前景，可以应用于各种需要处理长文本的场景，例如多轮对话、程序分析、文档摘要、机器翻译等。通过降低计算复杂度，UniSparse可以显著提升LLM在这些场景中的性能和效率，并降低部署成本。未来，UniSparse有望成为LLM长文本处理的标准加速模块。

## 📄 摘要（原文）

> Efficient long-context understanding and reasoning are increasingly vital for large language model (LLM) applications such as multi-turn dialogue and program analysis. However, the core self-attention mechanism scales quadratically with sequence length, creating a fundamental computational bottleneck. Existing sparse attention methods alleviate this issue but face trade-offs: training-based methods are costly and cannot be directly applied as acceleration plugins for other models, while inference-time methods often compromise efficiency or cross-modal generality. To address these limitations, we present UniSparse, a unified mechanism that introduces the notion of composite tokens--compact representations that aggregate multi-granularity contextual information. Building on this abstraction, UniSparse dynamically constructs sparse attention through multi-granularity compression and block-level selection, enabling efficient and hardware-friendly execution on GPU. Across multiple modalities and tasks ranging from synthetic benchmarks to real-world applications, UniSparse consistently surpasses state-of-the-art sparse attention methods (e.g., MInference, XAttention, FlexPrefill) in both accuracy and efficiency, achieving $\ge$ 99% of full-attention accuracy and up to 2.61$\times$ faster attention computation than FlashAttention.

