---
layout: default
title: LLMs on a Budget? Say HOLA
---

# LLMs on a Budget? Say HOLA

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18952" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18952v2</a>
  <a href="https://arxiv.org/pdf/2506.18952.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18952v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18952v2', 'LLMs on a Budget? Say HOLA')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zohaib Hasan Siddiqui, Jiechao Gao, Ebad Shabbir, Mohammad Anas Azeez, Rafiq Ali, Gautam Siddharth Kashyap, Usman Naseem

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-23 (更新: 2025-10-09)

**备注**: Accepted at EMNLP 2025 (Industry Track)

---

## 💡 一句话要点

**提出HOLA框架以高效部署大型语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `边缘计算` `推理优化` `自适应检索` `结构化剪枝` `量化技术` `实时应用`

## 📋 核心要点

1. 现有方法在边缘设备上运行大型语言模型面临高计算和内存需求的挑战，限制了实时应用的推广。
2. HOLA框架通过分层推测解码和自适应检索复杂度调整，实现了高效的LLM推理和部署。
3. 实验结果显示，HOLA在多个基准测试中显著提升了性能，并有效降低了边缘设备的延迟和内存占用。

## 📝 摘要（中文）

在边缘设备上运行大型语言模型（LLMs）受到高计算和内存需求的限制，这对医疗、教育和嵌入式系统等实时应用构成障碍。现有的解决方案如量化、剪枝和检索增强生成（RAG）仅提供部分优化，且常常在速度或准确性上妥协。本文提出HOLA，一个端到端的优化框架，旨在实现高效的LLM部署。HOLA内部利用分层推测解码（HSD）加速推理而不损失质量，外部则通过AdaComp-RAG根据上下文需求调整检索复杂度。结合结构化剪枝（LoRA）和量化的LoBi，HOLA在GSM8K上实现了17.6%的EMA，在ARC上实现了10.5%的MCA，并在Jetson Nano等边缘设备上降低了延迟和内存使用，证明了其可扩展性和生产就绪性。

## 🔬 方法详解

**问题定义**：本文旨在解决在边缘设备上运行大型语言模型时面临的高计算和内存需求问题。现有方法如量化和剪枝虽然有所帮助，但往往无法兼顾速度和准确性。

**核心思路**：HOLA框架通过引入分层推测解码（HSD）和自适应检索复杂度（AdaComp-RAG），实现了高效推理，同时保持模型质量。这样的设计使得模型在不同上下文下能够灵活调整计算资源。

**技术框架**：HOLA的整体架构包括三个主要模块：分层推测解码（HSD）、自适应检索复杂度（AdaComp-RAG）和结合结构化剪枝与量化的LoBi。HSD负责加速推理，AdaComp-RAG根据上下文需求调整检索复杂度，而LoBi则优化模型的存储和计算效率。

**关键创新**：HOLA的核心创新在于将HSD与AdaComp-RAG结合，形成一个端到端的优化框架。这种组合不仅提高了推理速度，还确保了模型的准确性，显著优于传统的单一优化方法。

**关键设计**：在HOLA中，HSD采用了分层的解码策略，以减少计算复杂度；AdaComp-RAG通过上下文感知的方式动态调整检索策略；LoBi则结合了结构化剪枝（LoRA）和量化技术，以降低内存占用和延迟。

## 📊 实验亮点

HOLA在多个基准测试中表现出色，GSM8K上实现了17.6%的EMA，ARC上实现了10.5%的MCA。此外，HOLA在Jetson Nano等边缘设备上显著降低了延迟和内存使用，证明了其高效性和可扩展性。

## 🎯 应用场景

HOLA框架的潜在应用领域包括医疗、教育和嵌入式系统等需要实时处理的场景。通过在边缘设备上高效部署大型语言模型，HOLA能够支持智能助手、实时翻译和个性化学习等应用，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> Running Large Language Models (LLMs) on edge devices is constrained by high compute and memory demands posing a barrier for real-time applications in sectors like healthcare, education, and embedded systems. Current solutions such as quantization, pruning, and retrieval-augmented generation (RAG) offer only partial optimizations and often compromise on speed or accuracy. We introduce HOLA, an end-to-end optimization framework for efficient LLM deployment. Internally, it leverages Hierarchical Speculative Decoding (HSD) for faster inference without quality loss. Externally, AdaComp-RAG adjusts retrieval complexity based on context needs. Together with LoBi, which blends structured pruning (LoRA) and quantization, HOLA delivers significant gains: 17.6% EMA on GSM8K, 10.5% MCA on ARC, and reduced latency and memory on edge devices like Jetson Nano--proving both scalable and production-ready.

