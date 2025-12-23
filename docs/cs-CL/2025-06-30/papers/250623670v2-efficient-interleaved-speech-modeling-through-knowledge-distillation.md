---
layout: default
title: Efficient Interleaved Speech Modeling through Knowledge Distillation
---

# Efficient Interleaved Speech Modeling through Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23670" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23670v2</a>
  <a href="https://arxiv.org/pdf/2506.23670.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23670v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23670v2', 'Efficient Interleaved Speech Modeling through Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammadmahdi Nouriborji, Morteza Rohanian

**分类**: cs.SD, cs.CL, eess.AS

**发布日期**: 2025-06-30 (更新: 2025-10-21)

---

## 💡 一句话要点

**提出TinyWave以解决语音生成模型体积与延迟问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音生成` `蒸馏训练` `多模态变换器` `模型压缩` `实时应用` `低资源环境` `TinyWave` `语音识别`

## 📋 核心要点

1. 现有的语音生成模型在体积和延迟方面存在显著限制，难以满足实时应用需求。
2. 本文提出通过层对齐蒸馏技术，压缩大型多模态变换器，构建紧凑的语音生成模型TinyWave。
3. TinyWave在多个任务中表现出色，准确率接近教师模型，且在资源使用上更为高效。

## 📝 摘要（中文）

当前的语音语言模型在许多部署环境中超出了大小和延迟的限制。本文通过层对齐蒸馏构建紧凑且表达力强的语音生成模型，压缩大型多模态变换器的体积达到3倍，同时性能损失最小。我们提出了TinyWave，一个包含20亿参数的模型系列，支持语音到语音及交错语音文本生成，经过50,000小时公共音频训练。TinyWave在Libri-Light上的评估显示，其归一化困惑度与教师模型相差仅1.4点，在口语StoryCloze和SALMon任务中的准确率达到教师模型的93-97%。这些模型针对商品硬件进行了优化，适用于实时对话代理、辅助技术和低资源环境。我们发布了模型、训练代码和评估脚本，以支持可重复的紧凑语音生成研究。

## 🔬 方法详解

**问题定义**：当前的语音生成模型通常体积庞大，延迟高，难以在实时应用中部署，限制了其实际应用场景。

**核心思路**：本文提出通过层对齐蒸馏技术，匹配隐藏状态、注意力图和软化的logits，从而有效压缩大型多模态变换器，同时保持性能损失在可接受范围内。

**技术框架**：TinyWave模型系列由多个模块组成，包括语音生成模块和交错文本生成模块，支持语音和混合语音文本的生成。训练过程中使用了50,000小时的公共音频数据，确保模型的表达能力和泛化能力。

**关键创新**：最重要的创新在于层对齐蒸馏方法，通过精确匹配教师模型的内部表示，显著提高了压缩效率，与传统的蒸馏方法相比，性能损失更小。

**关键设计**：在模型设计中，TinyWave采用了20亿参数的结构，使用了特定的损失函数来优化蒸馏过程，并在训练过程中进行了多种超参数调优，以确保模型在不同任务中的表现。

## 📊 实验亮点

TinyWave在Libri-Light数据集上的评估结果显示，其归一化困惑度仅比教师模型高出1.4点，且在口语StoryCloze和SALMon任务中准确率达到93-97%。与同类基线相比，TinyWave在性能上有显著提升，同时在模型体积上实现了3倍的压缩，展现出优越的效率。

## 🎯 应用场景

TinyWave模型的设计使其在实时对话代理、辅助技术和低资源环境中具有广泛的应用潜力。其紧凑的结构和高效的性能能够支持多种语音生成任务，提升用户体验，尤其是在资源受限的设备上。未来，该模型有望推动语音交互技术的发展，促进人机交互的自然性和流畅性。

## 📄 摘要（原文）

> Current speech language models exceed the size and latency constraints of many deployment environments. We build compact, expressive speech generation models through layer-aligned distillation, matching hidden states, attention maps, and softened logits to compress large multimodal transformers by 3x with minimal loss in performance. We introduce TinyWave, a family of 2B-parameter models for speech-to-speech and interleaved speech-text generation, trained on 50,000 hours of public audio. TinyWave supports (i) speech-only generation using phonetic or expressive tokens and (ii) mixed speech-text continuations. Evaluation on Libri-Light shows TinyWave within 1.4 normalized perplexity points of its teacher. Accuracy on spoken StoryCloze and SALMon reaches 93-97% of the teacher's performance, outperforming size-matched baselines. These models are optimized for deployment on commodity hardware, enabling applications in real-time conversational agents, assistive technologies, and low-resource environments. We release models, training code, and evaluation scripts to support reproducible research on compact, expressive speech generation.

