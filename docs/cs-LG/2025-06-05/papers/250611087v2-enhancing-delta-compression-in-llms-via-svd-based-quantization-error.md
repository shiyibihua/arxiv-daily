---
layout: default
title: Enhancing Delta Compression in LLMs via SVD-based Quantization Error Minimization
---

# Enhancing Delta Compression in LLMs via SVD-based Quantization Error Minimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11087" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11087v2</a>
  <a href="https://arxiv.org/pdf/2506.11087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11087v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11087v2', 'Enhancing Delta Compression in LLMs via SVD-based Quantization Error Minimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boya Xiong, Shuo Wang, Weifeng Ge, Guanhua Chen, Yun Chen

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-05 (更新: 2025-09-27)

---

## 💡 一句话要点

**提出DeltaMix框架以解决LLMs的量化误差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `增量压缩` `量化误差` `混合精度` `奇异值分解` `大语言模型` `微调` `线性整数规划` `模型优化`

## 📋 核心要点

1. 现有增量压缩方法在高压缩比下表现不足，主要依赖经验，缺乏理论支持。
2. 提出DeltaMix框架，通过自适应混合精度压缩来最小化SVD空间中的量化误差，解决现有方法的局限性。
3. 实验结果显示，DeltaMix在多个基准测试中显著优于基线方法，尤其在特定任务上提升幅度显著。

## 📝 摘要（中文）

微调是将大型语言模型（LLMs）适应多样化应用的重要过程。在多租户服务等场景中，部署了大量从同一基础模型微调的LLMs以满足复杂的用户需求。近期研究探索了增量压缩方法来量化和压缩定制LLM与相应基础模型之间的增量权重。然而，这些方法在高压缩比下表现不足，主要由于其经验性质。本文提出了DeltaMix，一个自适应混合精度增量压缩框架，旨在最小化奇异值分解（SVD）空间中的量化误差，而不施加额外假设。DeltaMix为混合精度压缩的必要性提供了理论依据，并提出了一种实际的量化解决方案，涉及解决0/1线性整数规划问题及重建目标修正方法。实验结果表明，DeltaMix在多个模型和基准测试中始终优于所有基线方法，尤其在AIME2024和GQA任务中，DeltaMix在7B参数模型上分别超越最佳基线Delta-CoMe 22.3%和6.1%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有增量压缩方法在高压缩比下的量化误差问题。这些方法通常依赖经验，导致在实际应用中性能不足。

**核心思路**：DeltaMix框架的核心思想是通过自适应混合精度来优化增量权重的量化过程，避免了对额外假设的依赖，从而提高了压缩效果。

**技术框架**：DeltaMix的整体架构包括两个主要模块：首先是基于SVD的量化误差最小化，其次是通过解决0/1线性整数规划问题来实现量化目标的修正。

**关键创新**：DeltaMix的主要创新在于提供了混合精度压缩的理论依据，并提出了一种新的量化解决方案，显著提升了压缩性能。与现有方法相比，DeltaMix在理论和实践上均表现出更强的适应性和有效性。

**关键设计**：在参数设置上，DeltaMix采用了动态调整的混合精度策略，损失函数设计考虑了量化误差的影响，网络结构则基于SVD进行优化，确保了压缩后的模型性能。

## 📊 实验亮点

实验结果显示，DeltaMix在多个基准测试中表现优异，特别是在AIME2024和GQA任务上，分别超越最佳基线Delta-CoMe 22.3%和6.1%。这一显著提升证明了DeltaMix在增量压缩领域的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括多租户服务、定制化语言模型的部署和优化等。DeltaMix框架能够有效提升LLMs的压缩性能，降低存储和计算成本，具有广泛的实际价值和未来影响，尤其在资源受限的环境中尤为重要。

## 📄 摘要（原文）

> Fine-tuning is a crucial process for adapting large language models (LLMs) to diverse applications. In certain scenarios, like multi-tenant serving, a large number of LLMs finetuned from the same base model are deployed to meet complex requirements for users. Recent works explore delta-compression approaches to quantize and compress the delta weights between the customized LLM and the corresponding base model. However, they exhibit inadequate performance at high compression ratios due to their empirical nature. In this work, we introduce DeltaMix, an adaptive mixed-precision delta-compression framework designed to minimize quantization error in the singular value decomposition (SVD) space without imposing additional assumptions. DeltaMix provides a theoretical justification for the necessity of mixed-precision compression and presents a practical quantization solution that involves solving a 0/1 linear integer programming problem alongside a reconstruction target correction method. Experimental results across multiple models and benchmarks illustrate that DeltaMix consistently outperforms all baseline methods. Notably, on tasks such as AIME2024 and GQA, DeltaMix exceeds the performance of the best baseline, Delta-CoMe, by 22.3\% and 6.1\% for 7B parameter models, respectively.

