---
layout: default
title: Democratizing Agentic AI with Fast Test-Time Scaling on the Edge
---

# Democratizing Agentic AI with Fast Test-Time Scaling on the Edge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00195" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00195v1</a>
  <a href="https://arxiv.org/pdf/2509.00195.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00195v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00195v1', 'Democratizing Agentic AI with Fast Test-Time Scaling on the Edge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Mark Chen, Zhiwen Mo, Guanxi Lu, Shuang Liang, Lingxiao Ma, Wayne Luk, Hongxiang Fan

**分类**: cs.LG

**发布日期**: 2025-08-29

---

## 💡 一句话要点

**提出FlashTTS以解决边缘设备上推理能力不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `边缘计算` `自主AI` `推理优化` `内存管理` `动态调度`

## 📋 核心要点

1. 现有方法在边缘设备上推理能力不足，内存限制使得只能使用较小的语言模型，导致推理效果不佳。
2. 本文提出FlashTTS，通过三项优化技术使得测试时扩展在内存受限的环境中变得可行，提升推理能力。
3. 实验结果显示FlashTTS的良好吞吐量提高了2.2倍，延迟减少了38%-68%，显著优于vLLM基线。

## 📝 摘要（中文）

在边缘设备上部署自主AI对于隐私和响应速度至关重要，但内存限制通常使这些系统只能使用较小的语言模型，导致推理能力不足。测试时扩展（TTS）可以通过在推理时增加计算资源来弥补这一差距，但现有方法在边缘硬件上开销过大。为此，本文提出FlashTTS，一个使TTS在内存受限的语言模型推理中变得实用的服务系统。FlashTTS引入了三项协同优化：推测性束扩展、非对称多模型内存分配和动态前缀感知调度。作为vLLM的即插即用库，FlashTTS使得单个消费者GPU（24 GB）上的边缘LLM能够匹配大型云模型的准确性和延迟。评估结果表明，FlashTTS的平均良好吞吐量提高了2.2倍，延迟减少了38%-68%，为边缘设备上的高性能自主AI铺平了道路。

## 🔬 方法详解

**问题定义**：本文旨在解决在边缘设备上部署自主AI时，由于内存限制导致推理能力不足的问题。现有的测试时扩展方法在边缘硬件上开销过大，无法有效应用。

**核心思路**：FlashTTS通过引入三项优化技术，使得在内存受限的环境中实现高效的推理能力。具体而言，利用动态资源分配和调度策略来提升推理效率。

**技术框架**：FlashTTS的整体架构包括三个主要模块：推测性束扩展、非对称多模型内存分配和动态前缀感知调度。推测性束扩展用于处理不规则推理路径，非对称多模型内存分配动态平衡生成与验证的内存需求，动态前缀感知调度则最大化KV缓存的重用。

**关键创新**：FlashTTS的创新在于其三项协同优化技术，尤其是推测性束扩展和动态前缀感知调度，这些设计使得在边缘设备上实现高效推理成为可能，显著降低了延迟和内存开销。

**关键设计**：在设计中，FlashTTS采用了动态内存分配策略，确保在推理过程中根据需求调整内存使用，同时优化了KV缓存的重用策略，以提高整体性能。

## 📊 实验亮点

实验结果表明，FlashTTS在性能上显著优于vLLM基线，平均良好吞吐量提高了2.2倍，延迟减少了38%-68%。这些结果表明FlashTTS在边缘设备上实现高性能自主AI的可行性，为相关领域的研究和应用提供了新的方向。

## 🎯 应用场景

FlashTTS的研究成果在多个领域具有广泛的应用潜力，包括智能家居、移动设备和边缘计算等场景。通过在资源受限的设备上实现高效的自主AI推理，能够提升用户体验，保护隐私，并支持实时响应的应用需求，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Deploying agentic AI on edge devices is crucial for privacy and responsiveness, but memory constraints typically relegate these systems to smaller Large Language Models (LLMs) with inferior reasoning capabilities. Test-Time Scaling (TTS) can bridge this reasoning gap by dedicating more compute during inference, but existing methods incur prohibitive overhead on edge hardware. To overcome this, we introduce FlashTTS, a serving system that makes TTS practical for memory-constrained LLM reasoning. FlashTTS introduces three synergistic optimizations: (i) Speculative Beam Extension to mitigate system stragglers from irregular reasoning paths; (ii) Asymmetric Multi-Model Memory Allocation to dynamically balance memory between generation and verification; and (iii) Dynamic Prefix-Aware Scheduling to maximize KV-cache reuse. Built as a plug-and-play library for vLLM, FlashTTS enables edge LLMs on a single consumer GPU (24 GB) to match the accuracy and latency of large cloud models. Our evaluation demonstrates that FlashTTS achieves an average 2.2x higher goodput and reduces latency by 38%-68% compared to a vLLM baseline, paving the way for democratized, high-performance agentic AI on edge devices.

