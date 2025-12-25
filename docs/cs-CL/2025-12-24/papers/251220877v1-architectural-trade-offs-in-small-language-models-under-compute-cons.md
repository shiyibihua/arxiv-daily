---
layout: default
title: Architectural Trade-offs in Small Language Models Under Compute Constraints
---

# Architectural Trade-offs in Small Language Models Under Compute Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20877" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20877v1</a>
  <a href="https://arxiv.org/pdf/2512.20877.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20877v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20877v1', 'Architectural Trade-offs in Small Language Models Under Compute Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shivraj Singh Bhatti

**分类**: cs.CL, cs.LG

**发布日期**: 2025-12-24

**备注**: 15 pages, 11 images

---

## 💡 一句话要点

**研究计算约束下小型语言模型的架构权衡，揭示不同架构选择对性能的影响。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `小型语言模型` `架构选择` `计算约束` `自注意力机制` `Transformer` `模型效率` `旋转位置嵌入`

## 📋 核心要点

1. 现有小型语言模型在计算约束下，架构选择对性能的影响缺乏系统性研究。
2. 通过逐步引入非线性、自注意力等模块，研究不同架构在计算效率上的权衡。
3. 实验表明，注意力机制在小规模模型中更有效，而RoPE等技术不一定适用。

## 📝 摘要（中文）

本文针对计算资源受限的小型语言模型，系统性地研究了架构选择和训练预算如何相互作用以决定模型性能。从线性下一个token预测器出发，逐步引入非线性、自注意力机制和多层Transformer架构，并在Tiny Shakespeare数据集（字符级别建模）以及Penn Treebank (PTB) 和 WikiText-2数据集（词级别建模）上进行评估。我们使用测试负对数似然（NLL）、参数数量和近似训练FLOPs来比较模型，从而表征准确率-效率的权衡。结果表明，即使在小规模下，基于注意力的模型在每FLOP效率方面也优于MLP，而增加深度或上下文长度但没有充分优化可能会降低性能。我们进一步研究了旋转位置嵌入（RoPE），发现大型语言模型中成功的架构技术不一定能迁移到小型模型中。

## 🔬 方法详解

**问题定义**：论文旨在研究在严格的计算资源约束下，小型语言模型（Small Language Models, SLMs）的架构选择对模型性能的影响。现有的研究通常集中在大型语言模型上，而忽略了小型模型在资源受限场景下的特殊性。因此，如何为小型模型选择合适的架构，以在有限的计算预算下最大化模型性能，是一个重要的挑战。

**核心思路**：论文的核心思路是通过系统性的实验，比较不同架构选择（例如，MLP、自注意力机制、Transformer等）在小型语言模型上的性能表现。通过控制训练预算（FLOPs），分析不同架构的效率，从而揭示在计算约束下，架构选择与模型性能之间的权衡关系。

**技术框架**：研究从一个简单的线性下一个token预测器开始，逐步增加模型的复杂度，包括引入非线性激活函数、自注意力机制和多层Transformer架构。在每个阶段，都评估模型在字符级别的Tiny Shakespeare数据集和词级别的Penn Treebank (PTB) 和 WikiText-2数据集上的性能。评估指标包括测试负对数似然（NLL）、参数数量和近似训练FLOPs。

**关键创新**：该研究的关键创新在于对小型语言模型进行了系统性的架构探索，并量化了不同架构在计算效率上的差异。此外，研究还发现，在大模型上有效的技术（如RoPE）不一定适用于小型模型，这为小型模型的架构设计提供了新的视角。

**关键设计**：研究中关键的设计包括：1) 逐步增加模型复杂度，以便隔离不同架构选择的影响；2) 使用FLOPs作为主要的计算预算约束，以便公平地比较不同架构的效率；3) 在多个数据集上进行评估，以验证结果的泛化性；4) 探索了旋转位置嵌入（RoPE）在小型模型上的效果，并发现其性能不如预期。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20877v1/images/tiny_train_val_loss.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20877v1/images/linear_ctx_vs_loss.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20877v1/images/mlp_hidden_vs_loss.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在计算资源受限的情况下，基于注意力的模型在每FLOP效率方面优于MLP。同时，研究发现，增加模型深度或上下文长度，但没有进行充分的优化，反而会降低模型性能。此外，RoPE等在大模型上有效的技术，在小型模型上的效果并不理想，这为小型语言模型的架构设计提供了重要的参考。

## 🎯 应用场景

该研究成果可应用于资源受限的边缘计算设备、移动设备或嵌入式系统中，例如智能家居设备、可穿戴设备等。通过选择合适的模型架构，可以在有限的计算资源下部署高性能的语言模型，从而实现本地化的自然语言处理功能，提高用户体验和数据安全性。

## 📄 摘要（原文）

> We present a systematic empirical study of small language models under strict compute constraints, analyzing how architectural choices and training budget interact to determine performance. Starting from a linear next-token predictor, we progressively introduce nonlinearities, self-attention, and multi-layer transformer architectures, evaluating each on character-level modeling of Tiny Shakespeare and word-level modeling of Penn Treebank (PTB) and WikiText-2. We compare models using test negative log-likelihood (NLL), parameter count, and approximate training FLOPs to characterize accuracy-efficiency trade-offs. Our results show that attention-based models dominate MLPs in per-FLOP efficiency even at small scale, while increasing depth or context without sufficient optimization can degrade performance. We further examine rotary positional embeddings (RoPE), finding that architectural techniques successful in large language models do not necessarily transfer to small-model regimes.

