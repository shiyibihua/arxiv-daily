---
layout: default
title: Exploring Layer-wise Information Effectiveness for Post-Training Quantization in Small Language Models
---

# Exploring Layer-wise Information Effectiveness for Post-Training Quantization in Small Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03332" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03332v1</a>
  <a href="https://arxiv.org/pdf/2508.03332.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03332v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03332v1', 'Exploring Layer-wise Information Effectiveness for Post-Training Quantization in Small Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: He Xiao, Qingyao Yang, Dirui Xie, Wendong Xu, Wenyong Zhou, Haobo Liu, Zhengwu Liu, Ngai Wong

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-05

**备注**: low-bit quantization

---

## 💡 一句话要点

**提出LieQ框架以解决小型语言模型的后训练量化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `后训练量化` `小型语言模型` `模型压缩` `层级诊断` `比特宽度分配` `边缘计算` `资源优化`

## 📋 核心要点

1. 现有方法在2-3比特精度下会严重降低准确性，难以满足小型语言模型在资源受限环境中的应用需求。
2. LieQ框架通过引入层级诊断指标，自动分配比特宽度，避免了梯度更新，从而在低比特压缩下保持模型性能。
3. 在多个零-shot推理任务中，LieQ在压缩-准确性权衡上表现出色，显著提高了小型语言模型的实用性。

## 📝 摘要（中文）

大型语言模型通常存在过度配置的问题，许多层的贡献有限，却占用了大量内存和能量。本文提出了LieQ，一个基于指标驱动的后训练量化框架，旨在在极低比特压缩下保持小型模型的准确性。该方法引入了三种互补的层级诊断指标，揭示了层之间的典型分工，从而实现自动比特宽度分配。LieQ在Qwen3-4B模型上以2.05比特量化恢复了95.9%的FP16基线性能，超越了现有方法，且在LLaMA3.2-3B上以2.07比特精度保持了98.2%的基线准确性，同时实现了4倍的内存减少。

## 🔬 方法详解

**问题定义**：本文旨在解决小型语言模型在极低比特压缩下保持准确性的问题。现有方法在低比特精度下通常会导致显著的准确性下降，难以满足实际应用需求。

**核心思路**：LieQ框架的核心思想是通过引入三种层级诊断指标（困惑度下降、表示紧凑性和Top-k能量增益），揭示层之间的分工，从而实现自动的比特宽度分配，避免了传统方法中的梯度更新过程。

**技术框架**：LieQ的整体架构包括三个主要模块：层级诊断模块、比特宽度分配模块和量化模块。层级诊断模块负责计算各层的性能指标，比特宽度分配模块根据诊断结果自动分配比特宽度，量化模块则执行实际的模型量化操作。

**关键创新**：LieQ的最大创新在于其指标驱动的量化方法，通过层级诊断实现了比特宽度的自动分配，与现有方法相比，显著提高了低比特量化下的模型性能。

**关键设计**：在设计中，LieQ使用了特定的损失函数来平衡压缩率与准确性，同时在比特宽度分配时考虑了各层的特征重要性，确保了模型在量化后的性能稳定性。

## 📊 实验亮点

LieQ在Qwen3-4B模型上以2.05比特量化恢复了95.9%的FP16基线性能，超越了GPTQ和AWQ，分别提高了19.7%和18.1%。在LLaMA3.2-3B模型上，LieQ以2.07比特精度保持了98.2%的基线准确性，同时实现了4倍的内存减少，展现了优越的压缩-准确性权衡。

## 🎯 应用场景

该研究的潜在应用领域包括资源受限的边缘设备和移动设备上的小型语言模型部署。通过有效的后训练量化，LieQ能够在保持高准确性的同时显著减少内存占用，为实际应用提供了新的可能性，推动了小型语言模型的广泛应用。

## 📄 摘要（原文）

> Large language models with billions of parameters are often over-provisioned: many layers contribute little unique information yet dominate the memory and energy footprint during inference. We present LieQ, a metric-driven post-training quantization framework that addresses the critical challenge of maintaining accuracy in sub-7B models under extreme low-bit compression. Our method introduces three complementary layer-wise diagnostics-Perplexity Drop, Representational Compactness, and Top-k Energy Gain -that reveal a canonical division of labour across layers, enabling automatic bit-width allocation without gradient updates. Unlike existing approaches that suffer severe accuracy degradation at 2-3 bits precision, LieQ achieves state-of-the-art compression-accuracy trade-offs: on Qwen3-4B, it recovers 95.9% of FP16 baseline performance at 2.05-bit quantization, outperforming GPTQ by 19.7% and AWQ by 18.1% on average across seven zero-shot reasoning tasks. Applied to LLaMA3.2-3B, LieQ maintains 98.2% of baseline accuracy at 2.07-bit precision while enabling 4x memory reduction, establishing new paradigms for deploying small language models on resource-constrained edge devices.

