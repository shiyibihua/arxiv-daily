---
layout: default
title: Outlier-Safe Pre-Training for Robust 4-Bit Quantization of Large Language Models
---

# Outlier-Safe Pre-Training for Robust 4-Bit Quantization of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19697" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19697v1</a>
  <a href="https://arxiv.org/pdf/2506.19697.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19697v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19697v1', 'Outlier-Safe Pre-Training for Robust 4-Bit Quantization of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jungwoo Park, Taewhoo Lee, Chanwoong Yoon, Hyeon Hwang, Jaewoo Kang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-24

**🔗 代码/项目**: [GITHUB](https://github.com/dmis-lab/Outlier-Safe-Pre-Training)

---

## 💡 一句话要点

**提出Outlier-Safe预训练以解决大语言模型量化中的异常值问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `量化` `异常值处理` `优化算法` `深度学习`

## 📋 核心要点

1. 现有方法在处理大型语言模型的量化时，极端激活异常值导致性能下降，影响设备端的高效部署。
2. 本文提出Outlier-Safe预训练（OSP），通过主动防止异常值形成，结合Muon优化器、单尺度RMSNorm和可学习的嵌入投影。
3. 在1万亿个标记上训练的OSP模型，在4位量化下平均得分为35.7，显著高于传统模型的26.5，且训练开销仅增加2%。

## 📝 摘要（中文）

在大型语言模型（LLMs）中，极端激活异常值严重影响量化性能，阻碍高效的设备端部署。现有的通道操作和自适应梯度缩放被认为是导致异常值的原因，但实际的缓解措施仍然具有挑战性。本文提出了Outlier-Safe预训练（OSP），通过主动防止异常值的形成来解决这一问题。OSP结合了三项关键创新：Muon优化器、单尺度RMSNorm和可学习的嵌入投影。通过在1万亿个标记上训练一个14亿参数的模型，验证了OSP的有效性。该模型在激进的4位量化下，在10个基准测试中平均得分为35.7，相较于Adam训练模型的26.5，且仅增加了2%的训练开销。OSP模型的超额峰度接近零，显著改变了LLM的量化行为。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在量化过程中因极端激活异常值导致的性能下降问题。现有方法主要依赖后期缓解措施，难以有效应对异常值的形成。

**核心思路**：提出Outlier-Safe预训练（OSP），通过主动防止异常值的生成，提升量化性能。OSP的设计理念是通过优化训练过程，避免异常值的产生，而不是事后处理。

**技术框架**：OSP包括三个主要模块：Muon优化器、单尺度RMSNorm和可学习的嵌入投影。Muon优化器消除了特权基，保持训练效率；单尺度RMSNorm防止通道级别的放大；可学习的嵌入投影重新分配来自嵌入矩阵的激活幅度。

**关键创新**：OSP的最大创新在于其主动防止异常值的策略，而非依赖后期修正。这一方法从根本上改变了LLM的训练策略，表明异常值并非LLM固有特性，而是训练策略的结果。

**关键设计**：在OSP中，Muon优化器的设计避免了特权基的使用，单尺度RMSNorm的参数设置确保了通道激活的稳定性，而可学习的嵌入投影则通过动态调整激活幅度来优化模型性能。

## 📊 实验亮点

实验结果显示，OSP模型在10个基准测试中的平均得分为35.7，相较于使用Adam优化器训练的模型得分26.5，提升幅度达34.5%。此外，OSP模型的超额峰度接近零，显著改善了量化行为，展示了其在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能助手和其他需要高效部署大型语言模型的场景。通过减少量化过程中的异常值，OSP为在资源受限的设备上运行大型模型提供了新的可能性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Extreme activation outliers in Large Language Models (LLMs) critically degrade quantization performance, hindering efficient on-device deployment. While channel-wise operations and adaptive gradient scaling are recognized causes, practical mitigation remains challenging. We introduce Outlier-Safe Pre-Training (OSP), a practical guideline that proactively prevents outlier formation rather than relying on post-hoc mitigation. OSP combines three key innovations: (1) the Muon optimizer, eliminating privileged bases while maintaining training efficiency; (2) Single-Scale RMSNorm, preventing channel-wise amplification; and (3) a learnable embedding projection, redistributing activation magnitudes originating from embedding matrices. We validate OSP by training a 1.4B-parameter model on 1 trillion tokens, which is the first production-scale LLM trained without such outliers. Under aggressive 4-bit quantization, our OSP model achieves a 35.7 average score across 10 benchmarks (compared to 26.5 for an Adam-trained model), with only a 2% training overhead. Remarkably, OSP models exhibit near-zero excess kurtosis (0.04) compared to extreme values (1818.56) in standard models, fundamentally altering LLM quantization behavior. Our work demonstrates that outliers are not inherent to LLMs but are consequences of training strategies, paving the way for more efficient LLM deployment. The source code and pretrained checkpoints are available at https://github.com/dmis-lab/Outlier-Safe-Pre-Training.

