---
layout: default
title: Chain-of-Thought Enhanced Shallow Transformers for Wireless Symbol Detection
---

# Chain-of-Thought Enhanced Shallow Transformers for Wireless Symbol Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21093" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21093v1</a>
  <a href="https://arxiv.org/pdf/2506.21093.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21093v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21093v1', 'Chain-of-Thought Enhanced Shallow Transformers for Wireless Symbol Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Li Fan, Peng Wang, Jing Yang, Cong Shen

**分类**: cs.LG, cs.IT, eess.SP, stat.ML

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出CHOOSE框架以解决无线符号检测中的计算资源限制问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无线通信` `变压器` `符号检测` `上下文学习` `浅层模型` `自回归推理` `计算效率` `移动设备`

## 📋 核心要点

1. 现有的ICL基础变压器模型依赖于深层架构，导致高昂的存储和计算成本。
2. 提出CHOOSE框架，通过在隐藏空间中引入自回归推理步骤，增强浅层变压器的推理能力。
3. 实验结果显示，CHOOSE在性能上优于传统浅层变压器，并与深层变压器相当，同时保持高效的存储和计算性能。

## 📝 摘要（中文）

变压器在解决无线通信问题方面展现了潜力，特别是在上下文学习（ICL）中，模型通过提示适应新任务而无需更新模型。然而，现有基于ICL的变压器模型依赖于深层架构以实现满意的性能，导致存储和计算成本高昂。本文提出了CHain Of thOught Symbol dEtection（CHOOSE），一种增强的浅层变压器框架，用于无线符号检测。通过在隐藏空间中引入自回归潜在推理步骤，CHOOSE显著提高了浅层模型（1-2层）的推理能力，而无需增加模型深度。这一设计使得轻量级变压器能够实现与更深模型相当的检测性能，适合在资源受限的移动设备上部署。实验结果表明，我们的方法优于传统的浅层变压器，并且在存储和计算效率上保持优势。

## 🔬 方法详解

**问题定义**：本文旨在解决无线符号检测中的计算资源限制问题。现有的ICL基础变压器模型通常需要深层架构以获得良好性能，导致存储和计算负担过重。

**核心思路**：论文提出的CHOOSE框架通过引入自回归潜在推理步骤，增强了浅层变压器的推理能力，从而在不增加模型深度的情况下提升性能。

**技术框架**：CHOOSE框架由1-2层的浅层变压器构成，结合自回归推理步骤，形成一个高效的推理过程。该框架能够在隐藏空间中进行有效的推理，适应不同的无线符号检测任务。

**关键创新**：CHOOSE的核心创新在于通过自回归推理步骤增强浅层模型的推理能力，这与传统深层变压器依赖于多层结构的方式形成鲜明对比。

**关键设计**：在设计中，CHOOSE采用了1-2层的浅层变压器结构，并通过特定的损失函数和参数设置优化推理过程，以确保在资源受限的环境中仍能实现高效的性能。

## 📊 实验亮点

实验结果表明，CHOOSE框架在无线符号检测任务中，性能优于传统的浅层变压器，并与深层变压器的性能相当。具体而言，CHOOSE在存储和计算效率上保持了显著优势，展现出良好的应用前景。

## 🎯 应用场景

该研究的潜在应用领域包括移动通信设备、物联网设备及其他资源受限的无线接收器。通过实现高效的无线符号检测，CHOOSE框架能够在实际应用中提高数据传输的可靠性和效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Transformers have shown potential in solving wireless communication problems, particularly via in-context learning (ICL), where models adapt to new tasks through prompts without requiring model updates. However, prior ICL-based Transformer models rely on deep architectures with many layers to achieve satisfactory performance, resulting in substantial storage and computational costs. In this work, we propose CHain Of thOught Symbol dEtection (CHOOSE), a CoT-enhanced shallow Transformer framework for wireless symbol detection. By introducing autoregressive latent reasoning steps within the hidden space, CHOOSE significantly improves the reasoning capacity of shallow models (1-2 layers) without increasing model depth. This design enables lightweight Transformers to achieve detection performance comparable to much deeper models, making them well-suited for deployment on resource-constrained mobile devices. Experimental results demonstrate that our approach outperforms conventional shallow Transformers and achieves performance comparable to that of deep Transformers, while maintaining storage and computational efficiency. This represents a promising direction for implementing Transformer-based algorithms in wireless receivers with limited computational resources.

