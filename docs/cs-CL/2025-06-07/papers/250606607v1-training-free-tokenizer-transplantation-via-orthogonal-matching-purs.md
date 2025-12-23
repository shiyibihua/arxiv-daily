---
layout: default
title: Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit
---

# Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06607" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06607v1</a>
  <a href="https://arxiv.org/pdf/2506.06607.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06607v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06607v1', 'Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Charles Goddard, Fernando Fernandes Neto

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-07

---

## 💡 一句话要点

**提出无训练的标记器移植方法以解决大语言模型的标记器不匹配问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `标记器移植` `正交匹配追踪` `大语言模型` `零-shot学习` `知识蒸馏`

## 📋 核心要点

1. 现有方法在处理不同标记器之间的嵌入不匹配时，往往需要额外的训练，导致性能下降。
2. 论文提出通过正交匹配追踪（OMP）方法，实现无训练的标记器移植，利用稀疏线性组合重构标记嵌入。
3. 在Llama到Mistral NeMo和Qwen到Llama的跨标记器任务中，OMP方法在多个基准测试中表现出最佳的零-shot性能保持。

## 📝 摘要（中文）

我们提出了一种无训练的方法，通过正交匹配追踪（OMP）在预训练的大语言模型（LLMs）中移植标记器，重构未见的标记嵌入。具体而言，我们将每个超出词汇表的标记近似为共享标记的稀疏线性组合，分为两个阶段：首先，使用一小组共享锚定标记计算新标记在捐赠者嵌入空间中的表示，然后将这些稀疏系数转移回基础模型的嵌入空间。在两个具有挑战性的跨标记器任务上，我们展示了OMP在多个基准测试中实现了最佳的零-shot性能保持，而其他零-shot方法显著下降。与基线方法相比，OMP始终实现最佳整体性能，有效弥合了大型标记器之间的差异，而无需梯度更新。

## 🔬 方法详解

**问题定义**：本论文旨在解决预训练大语言模型中不同标记器之间的嵌入不匹配问题。现有方法通常需要额外的训练，导致模型性能显著下降，尤其是在跨标记器任务中。

**核心思路**：论文的核心思路是通过正交匹配追踪（OMP）方法，无需训练即可实现标记器的移植。具体而言，利用共享标记的稀疏线性组合来近似未见的标记嵌入，从而保持模型性能。

**技术框架**：整体流程分为两个主要阶段：第一阶段，使用一小组共享锚定标记计算新标记在捐赠者嵌入空间中的表示；第二阶段，将这些稀疏系数转移回基础模型的嵌入空间。

**关键创新**：最重要的技术创新在于提出了无训练的标记器移植方法，利用OMP有效地弥合了大型标记器之间的差异。这一方法与现有的需要训练的标记器移植方法本质上不同。

**关键设计**：在实现过程中，关键设计包括选择合适的共享锚定标记字典，以及在稀疏线性组合中如何有效计算和转移系数。这些设计确保了模型在不进行梯度更新的情况下，依然能够保持良好的性能。

## 📊 实验亮点

在Llama到Mistral NeMo（12B）和Qwen到Llama（1B）的跨标记器任务中，OMP方法在多个基准测试中实现了最佳的零-shot性能保持，相较于基线方法（如零初始化、均值初始化及现有方法WECHSEL、FOCUS、ZETT），OMP表现出显著的性能提升，证明了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括跨标记器知识蒸馏、推测解码、集成、合并以及特定领域词汇的适配。通过直接重用预训练模型权重，研究成果能够显著提高模型在不同标记器下的适应性和性能，推动自然语言处理领域的进步。

## 📄 摘要（原文）

> We present a training-free method to transplant tokenizers in pretrained large language models (LLMs) by reconstructing unseen token embeddings via Orthogonal Matching Pursuit (OMP). Specifically, we approximate each out-of-vocabulary token as a sparse linear combination of shared tokens, in two phases: first, compute each new token's representation in the donor embedding space with a small dictionary of shared anchor tokens, then transfer these same sparse coefficients back into the base model's embedding space.
>   On two challenging cross-tokenizer tasks--Llama$\to$Mistral NeMo (12B) and Qwen$\to$Llama (1B)--we show that OMP achieves best zero-shot preservation of the base model's performance across multiple benchmarks, while other zero-shot approaches degrade significantly. Compared to baselines (zero-init, mean-init, and existing approaches like WECHSEL, FOCUS, ZETT), OMP consistently achieves the best overall performance, effectively bridging large tokenizer discrepancies without gradient updates. Our analysis further identifies mismatched numerical tokenization schemes as a critical challenge for preserving mathematical reasoning capabilities. This technique enables direct reuse of pretrained model weights with new tokenizers, facilitating cross-tokenizer knowledge distillation, speculative decoding, ensembling, merging, and domain-specific vocabulary adaptations. We integrate our method into the open-source mergekit-tokensurgeon tool for post hoc vocabulary realignment.

