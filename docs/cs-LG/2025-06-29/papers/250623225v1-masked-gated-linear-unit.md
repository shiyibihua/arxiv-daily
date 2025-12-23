---
layout: default
title: Masked Gated Linear Unit
---

# Masked Gated Linear Unit

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23225" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23225v1</a>
  <a href="https://arxiv.org/pdf/2506.23225.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23225v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23225v1', 'Masked Gated Linear Unit')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yukito Tajima, Nakamasa Inoue, Yusuke Sekikawa, Ikuro Sato, Rio Yokota

**分类**: cs.LG, cs.CL

**发布日期**: 2025-06-29

---

## 💡 一句话要点

**提出Masked Gated Linear Units以解决GLU的内存瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `门控线性单元` `大型语言模型` `内存效率` `推理速度` `深度学习`

## 📋 核心要点

1. 现有的Gated Linear Units（GLUs）在内存读取方面存在瓶颈，导致效率低下。
2. 本文提出Masked Gated Linear Units（MGLUs），通过共享权重矩阵和学习多个二进制掩码来优化内存使用。
3. 实验结果显示，FlashMGLU在推理速度和内存效率上显著优于传统GLUs，同时保持或超越了准确度。

## 📝 摘要（中文）

Gated Linear Units（GLUs）已成为最新大型语言模型（LLMs）前馈网络的重要组成部分。然而，由于门控和数值流使用独立的权重矩阵，GLUs的内存读取需求是无门控前馈层的两倍。为了解决这一瓶颈，本文提出了Masked Gated Linear Units（MGLUs），一种高效的GLU实现。MGLUs的核心贡献包括：混合元素级门控（MoEG）架构，通过学习多个二进制掩码，在单个共享权重矩阵上确定门控或数值分配，从而减少内存传输；FlashMGLU，一个硬件友好的内核，在RTX5090 GPU上相较于传统GLU实现提高了47%的内存效率和34%的速度，推理时间速度提升高达19.7倍。在LLM实验中，Swish激活的变体SwiMGLU在保持内存优势的同时，准确度与SwiGLU基线相当，甚至更高。

## 🔬 方法详解

**问题定义**：现有的Gated Linear Units（GLUs）在前馈网络中由于使用独立的权重矩阵，导致内存读取需求增加，从而影响了模型的效率和性能。

**核心思路**：Masked Gated Linear Units（MGLUs）通过引入混合元素级门控（MoEG）架构，利用单个共享权重矩阵和多个二进制掩码来优化门控和数值流的分配，从而减少内存传输。

**技术框架**：MGLUs的整体架构包括多个模块，首先是学习多个二进制掩码以进行元素级的门控分配，其次是实现FlashMGLU内核以提高推理速度和内存效率。

**关键创新**：MGLUs的核心创新在于通过共享权重矩阵和元素级门控机制，显著降低了内存读取需求，与传统GLUs相比，提供了更高的效率和性能。

**关键设计**：在设计中，MGLUs采用了Swish激活函数的变体SwiMGLU，并在RTX5090 GPU上进行了优化，确保在保持内存优势的同时，准确度与基线模型相当或更高。

## 📊 实验亮点

实验结果表明，FlashMGLU在推理速度上比传统的PyTorch MGLU快19.7倍，同时在内存使用上提高了47%的效率，并且速度比标准GLUs快34%。SwiMGLU在保持内存优势的同时，准确度与SwiGLU基线相当，甚至有所提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等大型语言模型的开发。通过提高内存效率和推理速度，MGLUs能够在资源受限的环境中实现更高效的模型部署，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Gated Linear Units (GLUs) have become essential components in the feed-forward networks of state-of-the-art Large Language Models (LLMs). However, they require twice as many memory reads compared to feed-forward layers without gating, due to the use of separate weight matrices for the gate and value streams. To address this bottleneck, we introduce Masked Gated Linear Units (MGLUs), a novel family of GLUs with an efficient kernel implementation. The core contribution of MGLUs include: (1) the Mixture of Element-wise Gating (MoEG) architecture that learns multiple binary masks, each determining gate or value assignments at the element level on a single shared weight matrix resulting in reduced memory transfer, and (2) FlashMGLU, a hardware-friendly kernel that yields up to a 19.7 $\times$ inference-time speed-up over a naive PyTorch MGLU and is 47% more memory-efficient and 34% faster than standard GLUs despite added architectural complexity on an RTX5090 GPU. In LLM experiments, the Swish-activated variant SwiMGLU preserves its memory advantages while matching - or even surpassing - the downstream accuracy of the SwiGLU baseline.

