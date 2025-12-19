---
layout: default
title: Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics
---

# Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16602" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16602v1</a>
  <a href="https://arxiv.org/pdf/2512.16602.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16602v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16602v1', 'Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Iker García-Ferrero, David Montero, Roman Orus

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出拒绝引导方法以控制大型语言模型的拒绝行为**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `拒绝行为` `内容审核` `政治敏感话题` `深度学习` `模型控制` `推理时调整` `岭回归`

## 📋 核心要点

1. 现有方法在处理政治敏感话题时，拒绝行为的检测依赖于脆弱的模式匹配，导致控制效果不佳。
2. 本文提出的拒绝引导方法通过引入大型语言模型作为判断者，利用拒绝置信度分数实现对拒绝行为的精细控制。
3. 实验结果显示，该方法在消除政治敏感话题的拒绝行为的同时，保持了安全性和接近基线的性能，具有良好的泛化能力。

## 📝 摘要（中文）

本文介绍了一种名为拒绝引导（Refusal Steering）的方法，旨在对大型语言模型在政治敏感话题上的拒绝行为进行细粒度控制，而无需重新训练。该方法通过用大型语言模型作为判断者来替代脆弱的基于模式的拒绝检测，分配拒绝置信度分数，并提出了一种岭回归变体来计算更好地隔离拒绝与合规方向的引导向量。在Qwen3-Next-80B-A3B-Thinking模型上，我们的方法消除了模型在政治敏感话题上的拒绝行为，同时在JailbreakBench上保持安全性，并在一般基准测试中接近基线性能。该方法在4B和80B模型中具有良好的泛化能力，并能够在需要时诱导有针对性的拒绝。我们分析了引导向量，表明拒绝信号集中在变换器的深层，并分布在多个维度上。这些结果表明，激活引导可以消除政治拒绝行为，同时保持对有害内容的安全对齐，为推理时可控、透明的内容审核提供了实际路径。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在处理政治敏感话题时的拒绝行为控制问题。现有方法依赖于脆弱的模式匹配，难以有效识别和调整拒绝行为。

**核心思路**：提出拒绝引导方法，通过将大型语言模型作为判断者，利用其生成的拒绝置信度分数来实现对拒绝行为的细粒度控制，避免了重新训练的复杂性。

**技术框架**：该方法的整体架构包括拒绝置信度评分模块和引导向量计算模块。首先，模型评估输入内容的拒绝置信度，然后计算引导向量以调整模型的输出。

**关键创新**：最重要的创新在于引入岭回归变体来计算引导向量，这一设计使得拒绝与合规方向的隔离更加有效，显著提升了拒绝行为的控制能力。

**关键设计**：在参数设置上，采用了岭回归的正则化技术，以优化引导向量的计算。此外，分析表明拒绝信号主要集中在变换器的深层，并在多个维度上分布，提供了新的理解模型行为的视角。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16602v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16602v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16602v1/images/top_layer_pca_2d_chinabadWRMD.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，拒绝引导方法在Qwen3-Next-80B-A3B-Thinking模型上有效消除了政治敏感话题的拒绝行为，同时在JailbreakBench上保持了安全性，且在一般基准测试中接近基线性能，展示了良好的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、在线问答系统和任何涉及敏感话题的自动化对话系统。通过实现对拒绝行为的可控性，能够提高系统的透明度和用户信任度，减少误解和不当内容的传播。

## 📄 摘要（原文）

> We introduce Refusal Steering, an inference-time method to exercise fine-grained control over Large Language Models refusal behaviour on politically sensitive topics without retraining. We replace fragile pattern-based refusal detection with an LLM-as-a-judge that assigns refusal confidence scores and we propose a ridge-regularized variant to compute steering vectors that better isolate the refusal--compliance direction. On Qwen3-Next-80B-A3B-Thinking, our method removes the refusal behaviour of the model around politically sensitive topics while maintaining safety on JailbreakBench and near-baseline performance on general benchmarks. The approach generalizes across 4B and 80B models and can also induce targeted refusals when desired. We analize the steering vectors and show that refusal signals concentrate in deeper layers of the transformer and are distributed across many dimensions. Together, these results demonstrate that activation steering can remove political refusal behaviour while retaining safety alignment for harmful content, offering a practical path to controllable, transparent moderation at inference time.

