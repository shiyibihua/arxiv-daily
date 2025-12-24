---
layout: default
title: Trainable Dynamic Mask Sparse Attention
---

# Trainable Dynamic Mask Sparse Attention

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02124" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02124v6</a>
  <a href="https://arxiv.org/pdf/2508.02124.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02124v6" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02124v6', 'Trainable Dynamic Mask Sparse Attention')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingze Shi, Yifan Wu, Yiran Peng, Bingheng Wu, Liangdong Wang, Guang Liu, Yuyu Luo

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-08-04 (更新: 2025-11-16)

**备注**: 26 pages

**🔗 代码/项目**: [GITHUB](https://github.com/SmallDoges/flash-dmattn)

---

## 💡 一句话要点

**提出可训练动态掩码稀疏注意力机制以解决长上下文建模问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文建模` `稀疏注意力` `动态掩码` `深度学习` `自然语言处理`

## 📋 核心要点

1. 现有的稀疏注意力方法在处理长上下文时存在适应性不足和可微性差的问题。
2. 本文提出的动态掩码注意力机制通过生成内容感知的动态掩码和硬件友好的稀疏权重来解决上述问题。
3. 实验结果表明，DMA在多个基准任务上均优于现有稀疏注意力基线，并实现了高达10倍的速度提升。

## 📝 摘要（中文）

随着大型语言模型（LLMs）对长上下文建模需求的增加，标准自注意力机制的平方复杂度成为瓶颈。虽然稀疏注意力方法被提出以缓解这一问题，但现有的基于位置的稀疏注意力方法缺乏对多样化查询上下文的适应性，而基于内容的稀疏注意力方法依赖启发式的键值选择，限制了完全可微性。本文提出了一种可训练的动态掩码稀疏注意力机制（DMA），通过三项关键创新实现了位置感知和内容感知方法的优势融合。DMA通过生成内容感知的动态掩码，计算硬件友好的位置感知稀疏权重，并支持端到端训练，展示了其在多项任务中的优越性能和高达10倍的速度提升。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长上下文建模中面临的计算复杂度问题，现有方法在适应性和可微性方面存在不足。

**核心思路**：提出的动态掩码注意力机制（DMA）结合了位置感知和内容感知的优点，通过动态生成掩码来适应不同的查询上下文。

**技术框架**：DMA的整体架构包括三个主要模块：内容感知动态掩码生成、硬件友好的位置感知稀疏权重计算和支持端到端训练的梯度流动设计。

**关键创新**：DMA的核心创新在于其动态掩码的生成方式和稀疏权重的计算方法，能够有效跳过不必要的计算区域，同时保持模型的可微性。

**关键设计**：在设计中，DMA使用值向量表示生成动态掩码，并通过优化的稀疏权重计算来提高计算效率，确保在训练过程中梯度不被阻塞。

## 📊 实验亮点

实验结果显示，DMA在多个任务中均优于最先进的稀疏注意力基线，尤其在多查询关联记忆和标准基准测试中表现突出，整体速度提升高达10倍。这些结果表明DMA在效率与长上下文建模能力之间实现了有效平衡。

## 🎯 应用场景

该研究的动态掩码稀疏注意力机制在自然语言处理、机器翻译和长文本理解等领域具有广泛的应用潜力。通过提高模型的计算效率和长上下文处理能力，DMA能够为实际应用提供更快的响应时间和更高的准确性，推动相关技术的发展和应用。

## 📄 摘要（原文）

> The increasing demand for long-context modeling in large language models (LLMs) is bottlenecked by the quadratic complexity of the standard self-attention mechanism. The community has proposed sparse attention to mitigate this issue. However, position-aware sparse attention methods rely on static sparse structures that lack adaptability to diverse query contexts, while content-aware sparse attention methods depend on heuristic key-value selection, hindering full differentiability. We introduce a trainable dynamic mask sparse attention mechanism, a method that merges the advantages of both position-aware and content-aware approaches. Dynamic Mask Attention (DMA) achieves this through three key innovations: First, it leverages value vector representations to generate content-aware dynamic masks, enabling the model to adaptively identify and attend to critical information. Second, it computes position-aware sparse weights in a hardware-friendly manner, efficiently skipping unnecessary computational regions. Finally, we demonstrate that the introduced dynamic mask and sparse weights do not obstruct gradients, supporting end-to-end training. We have validated the performance of DMA through comprehensive experiments. A large body of experimental evidence shows that DMA consistently holds a Pareto advantage over state-of-the-art sparse attention baselines in tasks including scaling laws, multi-query associative recall, standard benchmarks, and needle in a haystack tests, while also delivering up to a 10x overall speedup. These results highlight its ability to effectively balance model efficiency with long-context modeling capabilities. Our computational kernel code is now open-source at https://github.com/SmallDoges/flash-dmattn to encourage further research and application by the community.

