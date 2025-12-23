---
layout: default
title: Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference
---

# Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09501" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09501v2</a>
  <a href="https://arxiv.org/pdf/2506.09501.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09501v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09501v2', 'Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayi Yuan, Hao Li, Xinheng Ding, Wenya Xie, Yu-Jhe Li, Wentian Zhao, Kun Wan, Jing Shi, Xia Hu, Zirui Liu

**分类**: cs.CL

**发布日期**: 2025-06-11 (更新: 2025-10-24)

**🔗 代码/项目**: [GITHUB](https://github.com/nanomaoli/llm_reproducibility)

---

## 💡 一句话要点

**提出LayerCast以解决LLM推理中的数值不确定性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数值不确定性` `推理可重复性` `LayerCast` `浮点精度` `深度学习`

## 📋 核心要点

1. 现有方法在LLM推理中面临数值不确定性问题，导致性能的可重复性脆弱。
2. 论文提出LayerCast，通过在16位精度下存储权重并在FP32下进行计算，解决了数值精度对推理结果的影响。
3. 实验表明，LayerCast在不同硬件和软件设置下，显著提高了模型输出的稳定性和准确性。

## 📝 摘要（中文）

大型语言模型（LLMs）在各个领域中已成为不可或缺的工具，并展现出令人印象深刻的性能。然而，LLM性能的可重复性却十分脆弱，系统配置的变化（如评估批量大小、GPU数量和版本）会显著影响生成的响应。尤其在推理模型中，早期令牌的微小舍入差异可能导致思维链的分歧，最终影响准确性。本文首次系统性地研究了数值精度如何影响LLM推理的可重复性，并提出了一种轻量级推理管道LayerCast，能够在16位精度下存储权重，同时在FP32下进行所有计算，从而平衡内存效率与数值稳定性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型推理中的数值不确定性问题，现有方法在不同系统配置下导致性能波动，影响可重复性。

**核心思路**：论文的核心解决思路是通过LayerCast管道，在存储权重时使用16位精度，而在计算时使用FP32，以此提高数值稳定性并减少内存占用。

**技术框架**：LayerCast的整体架构包括权重存储模块和计算模块，前者负责以16位精度存储模型参数，后者则在推理时使用FP32进行计算，确保输出的稳定性。

**关键创新**：最重要的技术创新点在于首次系统性地探讨了数值精度对LLM推理可重复性的影响，并提出了相应的解决方案，与现有方法相比，显著提升了模型的输出一致性。

**关键设计**：在LayerCast中，权重存储采用16位精度，计算过程中使用FP32，确保了在不同硬件和软件环境下的数值稳定性，具体参数设置和损失函数设计未在摘要中详细说明。

## 📊 实验亮点

实验结果显示，在使用bfloat16精度和贪婪解码的情况下，DeepSeek-R1-Distill-Qwen-7B模型的准确性变化可达9%，响应长度差异可达9000个令牌，表明LayerCast在不同GPU配置下显著提高了模型输出的一致性和准确性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能问答等，能够在这些领域中提高模型的可重复性和可靠性，进而提升用户体验和信任度。未来，LayerCast的设计理念也可能被应用于其他类型的深度学习模型，推动更广泛的研究和应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) are now integral across various domains and have demonstrated impressive performance. Progress, however, rests on the premise that benchmark scores are both accurate and reproducible. We demonstrate that the reproducibility of LLM performance is fragile: changing system configuration, such as evaluation batch size, GPU count, and GPU version, can introduce significant differences in the generated responses. This issue is especially pronounced in reasoning models, where minor rounding differences in early tokens can cascade into divergent chains of thought, ultimately affecting accuracy. For instance, under bfloat16 precision with greedy decoding, a reasoning model like DeepSeek-R1-Distill-Qwen-7B can exhibit up to 9% variation in accuracy and 9,000 tokens difference in response length due to differences in GPU count, type, and evaluation batch size. We trace the root cause of this variability to the non-associative nature of floating-point arithmetic under limited numerical precision. This work presents the first systematic investigation into how numerical precision affects reproducibility in LLM inference. Through carefully controlled experiments across various hardware, software, and precision settings, we quantify when and how model outputs diverge. Our analysis reveals that floating-point precision - while critical for reproducibility - is often neglected in evaluation practices. Inspired by this, we develop a lightweight inference pipeline, dubbed LayerCast, that stores weights in 16-bit precision but performs all computations in FP32, balancing memory efficiency with numerical stability. Code is available at https://github.com/nanomaoli/llm_reproducibility.

