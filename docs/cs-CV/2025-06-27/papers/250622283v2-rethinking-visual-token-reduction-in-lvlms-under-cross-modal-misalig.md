---
layout: default
title: Rethinking Visual Token Reduction in LVLMs under Cross-modal Misalignment
---

# Rethinking Visual Token Reduction in LVLMs under Cross-modal Misalignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22283" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22283v2</a>
  <a href="https://arxiv.org/pdf/2506.22283.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22283v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22283v2', 'Rethinking Visual Token Reduction in LVLMs under Cross-modal Misalignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Xu, Yunke Wang, Yong Luo, Bo Du

**分类**: cs.CV

**发布日期**: 2025-06-27 (更新: 2025-08-03)

---

## 💡 一句话要点

**提出VisionDrop以解决LVLM中视觉标记冗余问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `视觉标记剪枝` `多模态学习` `内部注意力` `推理效率`

## 📋 核心要点

1. 现有的视觉标记减少方法依赖文本信号，假设文本能有效捕捉视觉信息的重要性，但这种假设存在不对齐问题。
2. 本文提出VisionDrop框架，通过视觉内部注意力选择视觉标记，避免了对文本信号的依赖，提升了剪枝效果。
3. 在与LLaVA-NeXT-7B集成后，VisionDrop实现了2.7倍的推理延迟减少和6倍的FLOPs降低，同时保留了95.71%的原始性能。

## 📝 摘要（中文）

大型视觉语言模型（LVLMs）通过密集的补丁级标记序列来编码视觉输入，以捕捉细粒度语义。然而，视觉标记的数量通常远超文本标记，导致计算开销大，限制了LVLMs的可扩展性。现有的视觉标记减少方法多依赖文本条件交互，假设文本标记能可靠捕捉视觉标记的重要性。本文重新审视这一假设，揭示了跨模态不对齐的因果、语义和空间形式，影响了文本引导的视觉标记减少效果。为此，我们提出了VisionDrop，一个无训练的视觉剪枝框架，基于视觉内部注意力选择信息丰富的视觉标记，无需依赖文本信号。通过将视觉编码器和LLM视为统一系统，我们设计了渐进式剪枝管道，能够在多个阶段进行标记选择和轻量级上下文合并，保留细粒度视觉信息。实验表明，VisionDrop在多个基准上表现优异，且无需额外训练或复杂修改。

## 🔬 方法详解

**问题定义**：本文旨在解决大型视觉语言模型中视觉标记冗余的问题。现有方法多依赖文本信号进行视觉标记的选择，导致在跨模态不对齐情况下效果不佳。

**核心思路**：提出VisionDrop框架，通过视觉内部注意力机制选择信息丰富的视觉标记，避免了对文本信号的依赖，从而提高了剪枝的有效性。

**技术框架**：整体架构将视觉编码器和LLM视为统一系统，设计了渐进式剪枝管道，包含多个阶段的标记选择和上下文合并模块。

**关键创新**：VisionDrop的主要创新在于其无训练的视觉剪枝方法，基于视觉内部注意力进行标记选择，与传统依赖文本的剪枝方法本质上不同。

**关键设计**：在设计中，采用了多阶段的剪枝策略，确保在激进的标记预算下仍能保留细粒度的视觉信息，且不需要额外的训练或复杂的模型修改。

## 📊 实验亮点

实验结果显示，VisionDrop在多个基准测试中表现优异，尤其是在与LLaVA-NeXT-7B集成时，实现了2.7倍的推理延迟减少和6倍的FLOPs降低，同时保留了95.71%的原始性能，显示出其在实际应用中的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理和多模态学习等。通过优化视觉标记的处理，VisionDrop可以在资源受限的环境中提升LVLM的效率，推动智能助手、自动驾驶和图像理解等领域的发展。

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) encode visual inputs as dense sequences of patch-level tokens to capture fine-grained semantics. These visual tokens often outnumber their textual counterparts by a large margin, leading to substantial computational overhead and limiting the scalability of LVLMs in practice. Previous efforts have explored visual token reduction either prior to or within the large language models (LLMs). However, most in-LLM reduction approaches rely on text-conditioned interactions, implicitly assuming that textual tokens can reliably capture the importance of visual tokens. In this work, we revisit this assumption and reveal causal, semantic, and spatial forms of cross-modal misalignment. These misalignments undermine the effectiveness of text-guided visual token reduction. To address this, we introduce VisionDrop, a training-free, visual-only pruning framework that selects informative visual tokens based on intra-modal (visual-to-visual) attention, without relying on textual signals. To further suppress redundancy throughout the model hierarchy, we treat the visual encoder and the LLM as a unified system and design a progressive pruning pipeline. Our method performs dominant token selection and lightweight contextual merging at multiple stages, enabling fine-grained visual information to be retained even under aggressive token budgets. Extensive experiments across diverse benchmarks show that VisionDrop achieves consistent improvements over existing approaches, despite requiring no additional training or complex modifications. Notably, when integrated with LLaVA-NeXT-7B, VisionDrop achieves a 2.7x reduction in inference latency and 6x in FLOPs, while retaining 95.71% of the original performance.

