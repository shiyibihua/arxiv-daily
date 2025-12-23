---
layout: default
title: Rectified Sparse Attention
---

# Rectified Sparse Attention

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04108" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04108v2</a>
  <a href="https://arxiv.org/pdf/2506.04108.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04108v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04108v2', 'Rectified Sparse Attention')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yutao Sun, Tianzhu Ye, Li Dong, Yuqing Xia, Jian Chen, Yizhao Gao, Shijie Cao, Jianyong Wang, Furu Wei

**分类**: cs.CL

**发布日期**: 2025-06-04 (更新: 2025-06-05)

---

## 💡 一句话要点

**提出Rectified Sparse Attention以解决长序列生成效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长序列生成` `稀疏注意力` `KV缓存` `生成模型` `自然语言处理` `效率提升`

## 📋 核心要点

1. 现有的稀疏解码方法在长序列生成中效率提升有限，且KV缓存对齐不准确导致生成质量下降。
2. 本文提出的ReSA方法通过结合块稀疏注意力与周期性密集校正，有效减少了误差累积。
3. 实验结果显示，ReSA在多个任务中实现了接近无损的生成质量，并在256K序列长度下提高了2.42倍的速度。

## 📝 摘要（中文）

高效的长序列生成是大型语言模型面临的关键挑战。尽管近期的稀疏解码方法提高了效率，但它们存在KV缓存对齐不准确的问题，导致近似误差累积并降低生成质量。本文提出了Rectified Sparse Attention（ReSA），一种将块稀疏注意力与周期性密集校正相结合的简单有效的方法。通过在固定间隔内使用密集前向传递刷新KV缓存，ReSA限制了误差累积并保持与预训练分布的对齐。实验结果表明，ReSA在数学推理、语言建模和检索任务中实现了接近无损的生成质量，并显著提高了效率。特别是在256K序列长度下，ReSA实现了高达2.42倍的端到端加速，成为可扩展长上下文推理的实用解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长序列生成中的效率问题，现有稀疏解码方法由于KV缓存对齐不准确，导致生成质量下降和误差累积。

**核心思路**：ReSA的核心思路是将块稀疏注意力与周期性密集校正结合，通过定期刷新KV缓存来限制误差的累积，从而保持生成质量。

**技术框架**：ReSA的整体架构包括两个主要模块：块稀疏注意力模块和密集校正模块。块稀疏注意力负责高效处理长序列，而密集校正模块则在固定时间间隔内进行KV缓存的刷新。

**关键创新**：ReSA的创新在于其周期性密集校正机制，这一设计有效解决了传统稀疏解码方法中的KV缓存对齐问题，显著提高了生成质量和效率。

**关键设计**：在参数设置上，ReSA采用了适当的块大小和校正频率，以平衡计算效率和生成质量。此外，损失函数设计上也考虑了生成质量与计算效率之间的权衡。

## 📊 实验亮点

实验结果表明，ReSA在多个任务中实现了接近无损的生成质量，特别是在256K序列长度下，ReSA实现了高达2.42倍的端到端加速，相较于传统方法表现出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用场景包括自然语言处理中的长文本生成、对话系统以及信息检索等领域。通过提高长序列生成的效率，ReSA可以在实际应用中显著提升用户体验，尤其是在需要处理大规模数据的场景中。未来，ReSA可能会推动更多高效生成模型的研究与应用。

## 📄 摘要（原文）

> Efficient long-sequence generation is a critical challenge for Large Language Models. While recent sparse decoding methods improve efficiency, they suffer from KV cache misalignment, where approximation errors accumulate and degrade generation quality. In this work, we propose Rectified Sparse Attention (ReSA), a simple yet effective method that combines block-sparse attention with periodic dense rectification. By refreshing the KV cache at fixed intervals using a dense forward pass, ReSA bounds error accumulation and preserves alignment with the pretraining distribution. Experiments across math reasoning, language modeling, and retrieval tasks demonstrate that ReSA achieves near-lossless generation quality with significantly improved efficiency. Notably, ReSA delivers up to 2.42$\times$ end-to-end speedup under decoding at 256K sequence length, making it a practical solution for scalable long-context inference. Code is available at https://aka.ms/ReSA-LM.

