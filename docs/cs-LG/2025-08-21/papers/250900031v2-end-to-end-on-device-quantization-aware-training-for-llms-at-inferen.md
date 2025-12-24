---
layout: default
title: End-to-End On-Device Quantization-Aware Training for LLMs at Inference Cost
---

# End-to-End On-Device Quantization-Aware Training for LLMs at Inference Cost

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00031" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00031v2</a>
  <a href="https://arxiv.org/pdf/2509.00031.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00031v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00031v2', 'End-to-End On-Device Quantization-Aware Training for LLMs at Inference Cost')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qitao Tan, Xiaoying Song, Jin Lu, Guoming Li, Jun Liu, Lingzi Hong, Caiwen Ding, Jundong Li, Xiaoming Zhai, Shaoyi Huang, Wei Niu, Geng Yuan

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-21 (更新: 2025-09-29)

---

## 💡 一句话要点

**提出ZeroQAT以解决LLMs量化训练中的高内存消耗问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化训练` `大型语言模型` `边缘计算` `内存优化` `深度学习`

## 📋 核心要点

1. 现有的后训练量化方法在微调模型参数时存在局限性，导致在低位宽场景下准确性显著下降。
2. 本文提出的ZeroQAT框架通过前向梯度估计消除反向传播，降低了内存和计算开销，支持权重和激活的量化。
3. 实验结果表明，ZeroQAT在内存需求显著降低的情况下，能够在单个8GB GPU上对13B模型进行微调，甚至在OnePlus 12手机上微调6.7B模型。

## 📝 摘要（中文）

量化是一种有效降低大型语言模型（LLMs）部署成本的技术，而后训练量化（PTQ）因其高效性受到广泛研究。然而，现有PTQ方法无法微调模型参数，且在低位宽场景下常遭遇显著的准确性损失。量化感知训练（QAT）提供了更为合理的解决方案，但其依赖反向传播导致的高内存消耗限制了其在LLM部署中的实用性。为了解决这些挑战，本文提出了ZeroQAT，一个基于零阶优化的QAT框架，支持权重和激活的量化。ZeroQAT利用前向梯度估计消除了反向传播，显著降低了计算和内存开销，同时保留了端到端优化的优势。实验表明，ZeroQAT在内存需求显著降低的情况下，始终优于代表性的PTQ和QAT基线。

## 🔬 方法详解

**问题定义**：本文旨在解决现有量化训练方法在低位宽场景下的准确性损失及高内存消耗问题。现有的后训练量化方法无法微调模型参数，导致性能下降，而量化感知训练方法又因反向传播带来高内存开销，限制了其实用性。

**核心思路**：ZeroQAT框架采用零阶优化方法，通过前向梯度估计来替代反向传播，从而显著降低计算和内存开销，同时实现权重和激活的量化。这样的设计使得在资源受限的边缘设备上进行端到端的量化训练成为可能。

**技术框架**：ZeroQAT的整体架构包括前向梯度估计模块、量化模块和优化模块。前向梯度估计模块负责计算梯度，而量化模块则对权重和激活进行量化，优化模块则进行模型参数的更新。

**关键创新**：ZeroQAT的主要创新在于其采用的前向梯度估计方法，消除了对反向传播的依赖，这与传统的QAT方法形成了本质区别，显著降低了内存和计算需求。

**关键设计**：在ZeroQAT中，模型参数的冻结和预量化设计使得大部分参数在微调过程中保持不变，从而进一步减少内存使用。此外，框架的损失函数和优化策略经过精心设计，以确保在量化过程中尽可能保留模型的性能。

## 📊 实验亮点

实验结果显示，ZeroQAT在内存需求显著降低的情况下，能够在单个8GB GPU上对13B模型进行微调，且在极低位宽（如2-4位）下表现出色。此外，ZeroQAT还成功在OnePlus 12手机上微调6.7B模型，展示了其在边缘设备上的实用性。

## 🎯 应用场景

ZeroQAT框架在资源受限的边缘设备上具有广泛的应用潜力，特别是在移动设备和嵌入式系统中，可以有效地部署大型语言模型。其降低的内存需求和计算开销使得在实际应用中实现高效的量化训练成为可能，推动了智能设备的智能化进程。

## 📄 摘要（原文）

> Quantization is an effective technique to reduce the deployment cost of large language models (LLMs), and post-training quantization (PTQ) has been widely studied due to its efficiency. However, existing PTQ methods are limited by their inability to fine-tune model parameters and often suffer significant accuracy loss in low-bit scenarios. Quantization-aware training (QAT) provides a more principled solution, but its reliance on backpropagation incurs prohibitive memory costs, limiting its practicality for LLM deployment. To address these challenges, we propose ZeroQAT, a zeroth-order optimization-based QAT framework that supports both weight and activation quantization. ZeroQAT leverages forward-only gradient estimation to eliminate backpropagation, substantially reducing computational and memory overhead while retaining the benefits of end-to-end optimization. We further introduce a lightweight variant of ZeroQAT for quantized fine-tuning, which freezes and pre-quantizes most parameters to further cut memory usage. Experiments show that ZeroQAT consistently outperforms representative PTQ and QAT baselines while requiring significantly less memory. For example, ZeroQAT enables fine-tuning of a 13B model at extremely low bit-widths (e.g., 2-4 bits) on a single 8GB GPU, and even allows fine-tuning a 6.7B model on a OnePlus 12 smartphone, demonstrating its practicality for end-to-end QAT on resource-limited edge devices.

