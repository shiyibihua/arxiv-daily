---
layout: default
title: Toward Effective Tool-Integrated Reasoning via Self-Evolved Preference Learning
---

# Toward Effective Tool-Integrated Reasoning via Self-Evolved Preference Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23285" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23285v2</a>
  <a href="https://arxiv.org/pdf/2509.23285.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23285v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23285v2', 'Toward Effective Tool-Integrated Reasoning via Self-Evolved Preference Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifei Chen, Guanting Dong, Zhicheng Dou

**分类**: cs.AI

**发布日期**: 2025-09-27 (更新: 2025-09-30)

---

## 💡 一句话要点

**提出Tool-Light框架，通过自进化偏好学习提升LLM工具集成推理的效率与准确性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `工具集成推理` `大型语言模型` `信息熵` `自进化学习` `偏好优化` `监督微调` `直接偏好优化` `LLM`

## 📋 核心要点

1. 现有工具集成推理方法存在工具使用效率低、准确性差等问题，难以充分发挥LLM的推理能力。
2. Tool-Light框架通过分析工具调用对信息熵的影响，指导模型更有效地利用工具，避免过度或不足的使用。
3. 实验结果表明，Tool-Light在多个数据集上显著提升了LLM在工具集成推理任务中的效率和准确性。

## 📝 摘要（中文）

本文研究了工具集成推理(TIR)中，大型语言模型(LLM)在工具使用上存在的效率和准确性问题，例如工具使用不足或过度，以及工具调用后的过度思考。通过分析工具调用对模型推理过程信息熵的影响，发现工具调用结果显著改变后续推理的信息熵，且推理链的整体熵值随工具调用次数变化。基于此，提出了Tool-Light框架，旨在鼓励LLM高效准确地执行TIR任务。该框架包含数据集构建和多阶段微调，数据集构建采用基于微调模型的连续自进化采样，融合了普通采样和熵引导采样，并建立了严格的正负样本对选择标准。训练过程采用两阶段方法，包括监督微调(SFT)和自进化直接偏好优化(DPO)。在10个数据集上的实验结果表明，Tool-Light能显著提高模型执行TIR任务的效率。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在进行工具集成推理时，常常表现出次优行为。具体表现为：工具使用不足，导致无法充分利用外部信息；工具使用过度，造成不必要的计算开销；在工具调用后出现过度思考，反而降低了推理效率和准确性。这些问题阻碍了LLM在复杂任务中的应用。

**核心思路**：本文的核心思路是通过信息熵来指导LLM的工具使用。研究发现，工具调用会显著改变后续推理过程的信息熵，因此可以通过控制信息熵的变化来优化工具的使用。具体来说，通过鼓励模型在信息熵较低时更多地利用工具，而在信息熵较高时减少工具的使用，从而提高推理的效率和准确性。

**技术框架**：Tool-Light框架包含两个主要部分：数据集构建和多阶段微调。数据集构建阶段，首先使用微调后的模型进行连续自进化采样，包括普通采样和熵引导采样。熵引导采样根据模型推理过程中的信息熵来调整采样策略。同时，建立严格的正负样本对选择标准，确保训练数据的质量。多阶段微调包括监督微调(SFT)和自进化直接偏好优化(DPO)。SFT用于初步提升模型的能力，DPO则用于优化模型的偏好，使其更倾向于高效准确的工具使用。

**关键创新**：Tool-Light的关键创新在于利用信息熵来指导工具集成推理。与现有方法相比，Tool-Light不是简单地增加或减少工具的使用，而是根据模型推理过程中的信息熵动态地调整工具的使用策略。这种方法能够更有效地利用工具，避免过度或不足的使用，从而提高推理的效率和准确性。此外，自进化采样和DPO的结合也能够更好地优化模型的偏好。

**关键设计**：在数据集构建阶段，采用了连续自进化采样，并融合了普通采样和熵引导采样。熵引导采样的具体实现方式未知，但可以推测是根据模型推理过程中每一步的信息熵来调整采样概率。在训练阶段，采用了两阶段的微调策略，包括SFT和DPO。DPO的具体实现方式未知，但可以推测是根据正负样本对来优化模型的偏好，使其更倾向于高效准确的工具使用。

## 📊 实验亮点

实验结果表明，Tool-Light在10个数据集上显著提高了LLM执行TIR任务的效率。具体性能数据未知，但论文强调了Tool-Light在提高效率方面的显著优势。与基线方法相比，Tool-Light能够更有效地利用工具，避免过度或不足的使用，从而提高推理的效率和准确性。

## 🎯 应用场景

Tool-Light框架可应用于各种需要工具集成推理的场景，例如智能客服、代码生成、科学研究等。通过提高LLM的工具使用效率和准确性，可以显著提升这些应用的性能和用户体验。未来，该研究可以进一步扩展到更复杂的任务和更多的工具类型，推动LLM在实际应用中的发展。

## 📄 摘要（原文）

> Tool-Integrated Reasoning (TIR) enables large language models (LLMs) to improve their internal reasoning ability by integrating external tools. However, models employing TIR often display suboptimal behaviors, such as insufficient or excessive tool usage and overthinking after tool calls. The challenge of incentivizing LLMs to perform TIR efficiently and accurately, while stabilizing the reasoning process, remains an open question. In this paper, we start by exploring the impact of tool calls on model reasoning from the perspective of information entropy. Our findings indicate that tool call results lead to a distinct change in the information entropy of subsequent reasoning, with the overall entropy of the reasoning chain varying based on the number of tool calls. Building on these insights, we propose Tool-Light, a framework designed to encourage LLMs to perform TIR efficiently and accurately. Our framework includes dataset construction and multi-stage fine-tuning. For dataset construction, we employ continuous self-evolved sampling using the fine-tuned model, integrating both vanilla sampling and entropy-guided sampling. Besides, we establish strict criteria for selecting positive-negative pairs during sampling. The training process involves a two-stage approach, comprising Supervised Fine-Tuning (SFT) and Self-Evolved Direct Preference Optimization (DPO). Experimental results on 10 datasets demonstrate the effectiveness of Tool-Light, significantly improving the model's efficiency in executing TIR tasks.

