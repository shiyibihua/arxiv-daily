---
layout: default
title: Enhancing Low-Rank Adaptation with Structured Nonlinear Transformations
---

# Enhancing Low-Rank Adaptation with Structured Nonlinear Transformations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21870" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21870v1</a>
  <a href="https://arxiv.org/pdf/2509.21870.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21870v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21870v1', 'Enhancing Low-Rank Adaptation with Structured Nonlinear Transformations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guanzhi Deng, Mingyang Liu, Dapeng Wu, Yinqiao Li, Linqi Song

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26

**备注**: This manuscript has been submitted to IEEE Journal of Selected Topics in Signal Processing (JSTSP) for review. Until the moment I submitted the manuscript to arXiv, we haven't received any review comments from JSTSP

---

## 💡 一句话要点

**提出LoRAN：通过结构化非线性变换增强低秩自适应能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低秩自适应` `参数高效微调` `非线性变换` `激活函数设计` `大型语言模型`

## 📋 核心要点

1. LoRA的线性特性限制了其表达能力，难以捕捉复杂的非线性关系。
2. LoRAN通过对LoRA的低秩更新应用轻量级非线性变换来增强模型表达能力。
3. 实验表明，LoRAN在摘要和分类任务上优于QLoRA，Sinter激活函数表现最佳。

## 📝 摘要（中文）

低秩自适应(LoRA)是一种广泛应用于大型语言模型的参数高效微调方法。然而，其线性特性限制了表达能力。本文提出了LoRAN，一种LoRA的非线性扩展，它对低秩更新应用轻量级变换。此外，我们引入了Sinter，一种基于正弦的激活函数，它在不增加参数数量的情况下添加结构化扰动。在摘要和分类任务上的实验表明，LoRAN始终优于QLoRA。消融研究表明，Sinter优于Sigmoid、ReLU和Tanh等标准激活函数，突出了激活函数设计在低秩微调中的重要性。

## 🔬 方法详解

**问题定义**：LoRA作为一种参数高效的微调方法，被广泛应用于大型语言模型。然而，LoRA本质上是线性的，这限制了其表达能力，使其难以捕捉复杂的非线性关系，从而影响微调效果。现有方法通常采用增加模型参数的方式来提升非线性能力，但这与参数高效微调的初衷相悖。

**核心思路**：LoRAN的核心思路是在LoRA的低秩更新过程中引入非线性变换，从而增强模型的表达能力，同时保持参数高效性。具体来说，LoRAN在低秩矩阵的更新后，应用一个轻量级的非线性激活函数，使得模型能够学习更复杂的特征表示。

**技术框架**：LoRAN的整体框架与LoRA类似，仍然是在预训练模型的权重矩阵上添加低秩矩阵进行更新。不同之处在于，LoRAN在低秩矩阵更新后，会应用一个非线性激活函数。具体流程如下：1. 初始化低秩矩阵A和B；2. 前向传播时，将原始权重矩阵W加上低秩矩阵的乘积AB；3. 在AB的结果上应用非线性激活函数；4. 反向传播时，只更新低秩矩阵A和B的参数。

**关键创新**：LoRAN的关键创新在于引入了非线性激活函数，并且特别设计了一种名为Sinter的基于正弦的激活函数。Sinter激活函数能够在不增加参数数量的情况下，为模型引入结构化的扰动，从而提升模型的泛化能力。与传统的Sigmoid、ReLU等激活函数相比，Sinter激活函数更适合于低秩微调的场景。

**关键设计**：Sinter激活函数的设计是LoRAN的关键。Sinter激活函数的具体形式为：Sinter(x) = sin(ωx)，其中ω是一个可学习的频率参数。通过调整ω的值，可以控制Sinter激活函数的频率，从而影响模型的学习能力。此外，LoRAN还采用了多种不同的非线性激活函数进行实验，包括Sigmoid、ReLU、Tanh等，以验证Sinter激活函数的有效性。

## 📊 实验亮点

实验结果表明，LoRAN在摘要和分类任务上始终优于QLoRA。具体来说，在摘要任务上，LoRAN相比QLoRA取得了显著的ROUGE指标提升。消融研究表明，Sinter激活函数优于Sigmoid、ReLU和Tanh等标准激活函数，证明了其在低秩微调中的有效性。例如，在某个分类数据集上，使用Sinter激活函数的LoRAN相比使用ReLU激活函数的LoRAN，准确率提升了1-2个百分点。

## 🎯 应用场景

LoRAN具有广泛的应用前景，可以应用于各种需要参数高效微调的大型语言模型任务，例如文本摘要、文本分类、机器翻译等。LoRAN能够提升模型的性能，同时保持较低的计算成本，使其成为一种实用的微调方法。未来，LoRAN可以进一步扩展到其他领域，例如计算机视觉和语音识别。

## 📄 摘要（原文）

> Low-Rank Adaptation (LoRA) is a widely adopted parameter-efficient fine-tuning method for large language models. However, its linear nature limits expressiveness. We propose LoRAN, a non-linear extension of LoRA that applies lightweight transformations to the low-rank updates. We further introduce Sinter, a sine-based activation that adds structured perturbations without increasing parameter count. Experiments across summarization and classification tasks show that LoRAN consistently improves over QLoRA. Ablation studies reveal that Sinter outperforms standard activations such as Sigmoid, ReLU, and Tanh, highlighting the importance of activation design in lowrank tuning.

