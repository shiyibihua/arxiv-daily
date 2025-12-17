---
layout: default
title: TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs
---

# TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14698" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14698v1</a>
  <a href="https://arxiv.org/pdf/2512.14698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14698v1" onclick="toggleFavorite(this, '2512.14698v1', 'TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jun Zhang, Teng Wang, Yuying Ge, Yixiao Ge, Xinhao Li, Ying Shan, Limin Wang

**分类**: cs.CV, cs.AI, cs.CL, cs.MM

**发布日期**: 2025-12-16

**备注**: Project Page: https://timelens-arc-lab.github.io/

---

## 💡 一句话要点

**提出TimeLens以提升视频时间定位的准确性与可靠性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频时间定位` `多模态大语言模型` `数据质量提升` `算法设计优化` `强化学习` `模型评估` `视频理解` `自动注释`

## 📋 核心要点

1. 现有视频时间定位方法在数据质量和算法设计上存在显著不足，导致评估标准不可靠。
2. 论文提出TimeLens，通过重新注释数据集和优化算法设计，提升多模态大语言模型在VTG任务中的表现。
3. 实验结果表明，TimeLens模型在VTG性能上超越了开源和一些专有模型，展示了显著的提升幅度。

## 📝 摘要（中文）

本文并未提出新方法，而是为视频时间定位（VTG）建立了一个简单、渐进且重要的基准。尽管多模态大语言模型（MLLMs）在视频理解任务中表现出色，但优化它们以适应VTG的方案仍未得到充分探索。我们首先揭示了现有VTG基准中的关键质量问题，并引入了TimeLens-Bench，包含经过严格质量标准重新注释的三个流行基准。我们的分析显示，与传统基准相比，模型的重新排名发生了显著变化，确认了先前评估标准的不可靠性。此外，我们通过自动重新注释管道解决了噪声训练数据问题，生成了大规模高质量训练数据集TimeLens-100K。在此基础上，我们深入探讨了算法设计原则，提出了一系列有意义的见解和有效的实践，最终形成了在开源模型中具有最先进VTG性能的TimeLens模型。

## 🔬 方法详解

**问题定义**：本文旨在解决视频时间定位（VTG）中的数据质量和算法设计不足的问题。现有方法在评估标准和训练数据的可靠性上存在显著缺陷，影响了模型的性能和应用。

**核心思路**：论文的核心思路是通过建立高质量的数据集和优化算法设计，提升多模态大语言模型在VTG任务中的能力。通过重新注释现有基准和引入新的训练数据集，确保模型训练的有效性和可靠性。

**技术框架**：整体架构包括两个主要模块：数据质量提升和算法设计优化。首先，通过TimeLens-Bench和TimeLens-100K提供高质量的训练数据；其次，采用新的算法设计原则，如交错文本编码和无思考强化学习（RLVR）训练范式。

**关键创新**：最重要的技术创新在于引入了严格的重新注释标准和高质量的训练数据集，显著提高了模型的评估可靠性。此外，RLVR训练范式的设计使得模型在训练过程中能够获得可验证的奖励，提升了学习效率。

**关键设计**：在参数设置上，采用了交错文本编码以增强时间表示的能力；损失函数设计上，结合了RLVR的奖励机制；网络结构上，优化了模型的层次和连接方式，以提高训练效果和推理速度。

## 📊 实验亮点

实验结果显示，TimeLens模型在视频时间定位任务中取得了最先进的性能，超越了开源模型和一些专有模型，如GPT-5和Gemini-2.5-Flash。具体而言，模型在多个基准测试中表现出显著的提升，验证了新数据集和算法设计的有效性。

## 🎯 应用场景

该研究在视频理解、智能监控、自动视频摘要等领域具有广泛的应用潜力。通过提升视频时间定位的准确性，能够为视频内容检索、事件检测等任务提供更可靠的支持，推动相关技术的进步与应用。未来，TimeLens的研究成果有望在多模态学习和视频分析领域产生深远影响。

## 📄 摘要（原文）

> This paper does not introduce a novel method but instead establishes a straightforward, incremental, yet essential baseline for video temporal grounding (VTG), a core capability in video understanding. While multimodal large language models (MLLMs) excel at various video understanding tasks, the recipes for optimizing them for VTG remain under-explored. In this paper, we present TimeLens, a systematic investigation into building MLLMs with strong VTG ability, along two primary dimensions: data quality and algorithmic design. We first expose critical quality issues in existing VTG benchmarks and introduce TimeLens-Bench, comprising meticulously re-annotated versions of three popular benchmarks with strict quality criteria. Our analysis reveals dramatic model re-rankings compared to legacy benchmarks, confirming the unreliability of prior evaluation standards. We also address noisy training data through an automated re-annotation pipeline, yielding TimeLens-100K, a large-scale, high-quality training dataset. Building on our data foundation, we conduct in-depth explorations of algorithmic design principles, yielding a series of meaningful insights and effective yet efficient practices. These include interleaved textual encoding for time representation, a thinking-free reinforcement learning with verifiable rewards (RLVR) approach as the training paradigm, and carefully designed recipes for RLVR training. These efforts culminate in TimeLens models, a family of MLLMs with state-of-the-art VTG performance among open-source models and even surpass proprietary models such as GPT-5 and Gemini-2.5-Flash. All codes, data, and models will be released to facilitate future research.

