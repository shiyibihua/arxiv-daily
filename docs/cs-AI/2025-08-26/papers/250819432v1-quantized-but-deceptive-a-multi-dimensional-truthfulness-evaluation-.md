---
layout: default
title: Quantized but Deceptive? A Multi-Dimensional Truthfulness Evaluation of Quantized LLMs
---

# Quantized but Deceptive? A Multi-Dimensional Truthfulness Evaluation of Quantized LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19432" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19432v1</a>
  <a href="https://arxiv.org/pdf/2508.19432.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19432v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19432v1', 'Quantized but Deceptive? A Multi-Dimensional Truthfulness Evaluation of Quantized LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yao Fu, Xianxuan Long, Runchao Li, Haotian Yu, Mu Sheng, Xiaotian Han, Yu Yin, Pan Li

**分类**: cs.AI

**发布日期**: 2025-08-26

**备注**: Accepted to EMNLP2025 main conference (poster)

---

## 💡 一句话要点

**提出TruthfulnessEval框架以评估量化LLM的真实性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化模型` `真实性评估` `逻辑推理` `常识推理` `虚假信息检测`

## 📋 核心要点

1. 现有量化LLM在生成真实响应方面的表现尚未得到充分评估，特别是在面对误导性提示时的脆弱性。
2. 本文提出TruthfulnessEval框架，综合评估量化LLM在逻辑推理、常识和模仿虚假方面的真实性。
3. 实验结果显示，量化模型在面对“欺骗性”提示时更易产生错误输出，揭示了其内部真实表征与输出之间的矛盾。

## 📝 摘要（中文）

量化技术使得大型语言模型（LLMs）在资源受限环境中高效部署，通过显著降低内存和计算成本。然而，量化LLM在生成真实或欺骗性响应方面的影响尚未得到充分探讨。本文提出了TruthfulnessEval，一个全面的评估框架，用于从逻辑推理、常识和模仿虚假三维度评估量化LLM的真实性。研究发现，尽管量化模型内部保持真实的表征，但在误导性提示下更易产生错误输出。通过对15种不同提示的测试，发现“欺骗性”提示能够覆盖真实一致的行为，而“诚实”和“中立”提示则保持稳定输出。我们的研究为未来量化感知的对齐和真实性干预设计提供了重要见解。

## 🔬 方法详解

**问题定义**：本文旨在解决量化LLM在生成真实响应时的脆弱性，尤其是在误导性提示下的表现不足。现有方法未能充分探讨量化对模型真实性的影响。

**核心思路**：提出TruthfulnessEval框架，通过三个维度评估量化LLM的真实性，旨在揭示量化模型在不同提示下的输出特性。

**技术框架**：框架包括逻辑推理、常识和模仿虚假三个评估模块，采用多种量化技术（4-bit到2-bit）对多个开源LLM进行测试。

**关键创新**：最重要的创新在于识别量化模型在面对不同类型提示时的行为差异，尤其是“欺骗性”提示对输出的影响，这在现有文献中尚未被深入探讨。

**关键设计**：通过层级探测和主成分分析（PCA）可视化，揭示量化模型内部的真实表征与输出之间的关系，设计了多种提示以测试模型的响应稳定性。

## 📊 实验亮点

实验结果表明，量化模型在面对“欺骗性”提示时，其输出的错误率显著高于“诚实”和“中立”提示，揭示了模型在真实表征与输出之间的矛盾。这一发现为量化模型的真实性评估提供了新的视角，强调了提示设计的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能对话系统和虚假信息检测等。通过改进量化LLM的真实性评估，可以提升模型在实际应用中的可靠性，尤其是在需要生成真实信息的场景中。未来，该框架可为量化模型的设计和优化提供指导，推动更高效的AI系统发展。

## 📄 摘要（原文）

> Quantization enables efficient deployment of large language models (LLMs) in resource-constrained environments by significantly reducing memory and computation costs. While quantized LLMs often maintain performance on perplexity and zero-shot tasks, their impact on truthfulness-whether generating truthful or deceptive responses-remains largely unexplored. In this work, we introduce TruthfulnessEval, a comprehensive evaluation framework for assessing the truthfulness of quantized LLMs across three dimensions: (1) Truthfulness on Logical Reasoning; (2) Truthfulness on Common Sense; and (3) Truthfulness on Imitative Falsehoods. Using this framework, we examine mainstream quantization techniques (ranging from 4-bit to extreme 2-bit) across several open-source LLMs. Surprisingly, we find that while quantized models retain internally truthful representations, they are more susceptible to producing false outputs under misleading prompts. To probe this vulnerability, we test 15 rephrased variants of "honest", "neutral" and "deceptive" prompts and observe that "deceptive" prompts can override truth-consistent behavior, whereas "honest" and "neutral" prompts maintain stable outputs. Further, we reveal that quantized models "know" the truth internally yet still produce false outputs when guided by "deceptive" prompts via layer-wise probing and PCA visualizations. Our findings provide insights into future designs of quantization-aware alignment and truthfulness interventions.

