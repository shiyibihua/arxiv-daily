---
layout: default
title: A Minimalist Optimizer Design for LLM Pretraining
---

# A Minimalist Optimizer Design for LLM Pretraining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16659" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16659v2</a>
  <a href="https://arxiv.org/pdf/2506.16659.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16659v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16659v2', 'A Minimalist Optimizer Design for LLM Pretraining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Athanasios Glentis, Jiaxiang Li, Andi Han, Mingyi Hong

**分类**: cs.LG, cs.AI, math.OC

**发布日期**: 2025-06-20 (更新: 2025-12-10)

---

## 💡 一句话要点

**提出SCALE优化器以提高LLM预训练效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大规模语言模型` `优化器设计` `内存效率` `SGD` `深度学习` `自然语言处理` `模型训练`

## 📋 核心要点

1. 现有的自适应优化器如Adam在内存和计算效率上存在不足，尤其在大规模语言模型的训练中。
2. 论文提出了SCALE优化器，通过列向梯度归一化和对输出层应用一阶动量，显著提升SGD的性能。
3. 实验结果显示，SCALE在多个LLaMA模型上超越了Adam和其他内存高效优化器，表现出色。

## 📝 摘要（中文）

大规模语言模型（LLM）的训练通常依赖于自适应优化器如Adam，这些优化器需要额外的操作并消耗大量内存来维护一阶和二阶矩。尽管已有研究提出了状态压缩变体以降低内存消耗，但仍需探讨对SGD的最小修改以匹配最先进的预训练性能。本文通过自下而上的方法，提出了两种简单而高效的技术：列向梯度归一化和仅对输出层应用一阶动量。结合这两种技术，形成了SCALE优化器，在多个LLaMA模型上，SCALE的性能与Adam相当或更优，同时仅使用35-45%的总内存，成为在内存限制下进行大规模预训练的有力候选者。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模语言模型预训练中自适应优化器的内存和计算效率问题。现有的优化器如Adam需要大量内存来维护梯度的动量信息，限制了其在资源受限环境下的应用。

**核心思路**：论文提出的SCALE优化器通过引入列向梯度归一化和仅对输出层应用一阶动量，减少了内存消耗，同时保持或提升了模型的训练性能。这种设计旨在最大化SGD的效率，减少对复杂优化器的依赖。

**技术框架**：SCALE优化器的整体架构包括两个主要模块：首先是列向梯度归一化模块，该模块对输出维度的梯度进行归一化；其次是动量应用模块，仅在输出层计算一阶动量。这种结构使得优化过程更加高效。

**关键创新**：SCALE的核心创新在于其简单性和高效性，通过对SGD的最小修改实现了与Adam相当的性能，且显著降低了内存需求。这与现有的复杂自适应优化器形成鲜明对比。

**关键设计**：在SCALE中，列向梯度归一化的实现方式确保了梯度在每次更新时都能保持一致性，而动量的选择仅限于输出层则有效减少了计算开销。具体参数设置和损失函数设计未在摘要中详细说明，需参考论文的具体内容。

## 📊 实验亮点

实验结果表明，SCALE在多个LLaMA模型（60M-1B）上与Adam的性能相当或更优，同时仅使用35-45%的内存。此外，SCALE在LLaMA 7B模型上超越了APOLLO和Muon等最先进的内存高效方法，在困惑度和内存消耗方面均表现出色。

## 🎯 应用场景

该研究的潜在应用领域包括大规模语言模型的训练，尤其是在内存受限的环境中。SCALE优化器的设计可以为研究人员和工程师提供一种高效的训练方案，推动自然语言处理和其他相关领域的发展。未来，SCALE可能会被广泛应用于各种深度学习任务，尤其是在需要优化计算资源的场景中。

## 📄 摘要（原文）

> Training large language models (LLMs) typically relies on adaptive optimizers such as Adam, which introduce extra operations and require significant more memory to maintain first- and second-order moments than SGD. While recent works such as GaLore, Fira and APOLLO have proposed state-compressed variants to reduce memory consumption, a fundamental question remains: What are the minimum modifications to plain SGD needed to match state-of-the-art pretraining performance? We systematically investigate this question using a bottom-up approach, and identify two simple yet highly (memory- and compute-) efficient techniques: (1) column-wise gradient normalization (normalizing the gradient along the output dimension), which boosts SGD performance without momentum; and (2) applying first-order momentum only to the output layer, where gradient variance is highest. Combining these two techniques lead to SCALE (Stochastic Column-normAlized Last-layer momEntum), a simple optimizer for memory efficient pretraining. Across multiple LLaMA models (60M-1B), SCALE matches or exceeds the performance of Adam while using only 35-45% of the total memory. It also consistently outperforms memory-efficient optimizers such as GaLore, Fira and APOLLO, making it a strong candidate for large-scale pretraining under memory constraints. For LLaMA 7B model, SCALE outperforms the state-of-the-art memory-efficient methods APOLLO and Muon, in terms of both perplexity and memory consumption.

