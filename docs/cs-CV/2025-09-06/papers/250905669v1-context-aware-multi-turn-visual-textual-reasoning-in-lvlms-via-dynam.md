---
layout: default
title: Context-Aware Multi-Turn Visual-Textual Reasoning in LVLMs via Dynamic Memory and Adaptive Visual Guidance
---

# Context-Aware Multi-Turn Visual-Textual Reasoning in LVLMs via Dynamic Memory and Adaptive Visual Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05669" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05669v1</a>
  <a href="https://arxiv.org/pdf/2509.05669.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05669v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05669v1', 'Context-Aware Multi-Turn Visual-Textual Reasoning in LVLMs via Dynamic Memory and Adaptive Visual Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weijie Shen, Xinrui Wang, Yuanqi Nie, Apiradee Boonmee

**分类**: cs.CV

**发布日期**: 2025-09-06

---

## 💡 一句话要点

**提出CAMVR框架以解决多轮视觉文本推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮推理` `视觉文本推理` `上下文感知` `动态记忆` `自适应引导` `跨模态学习` `大型语言模型` `视觉语言模型`

## 📋 核心要点

1. 现有的LLMs和LVLMs在多轮交互中缺乏深度的上下文理解，导致推理不连贯和信息丢失。
2. 提出的CAMVR框架通过引入VCMU和AVFG机制，动态管理视觉特征和文本语义，增强多轮推理能力。
3. 在VisDial、A-OKVQA和新提出的MTIF数据集上，CAMVR实现了领先的性能，展现了其有效性。

## 📝 摘要（中文）

当前的大型语言模型（LLMs）和视觉语言大型模型（LVLMs）在单轮任务中表现优异，但在需要深度上下文理解和复杂视觉推理的多轮交互中面临重大挑战，常导致推理碎片化、上下文丢失和幻觉现象。为了解决这些局限性，本文提出了上下文感知多轮视觉推理（CAMVR）框架，旨在增强LVLMs在多轮视觉文本推理中的能力。CAMVR引入了两个关键创新：视觉文本上下文记忆单元（VCMU）和自适应视觉聚焦引导（AVFG）机制。通过在多个数据集上的广泛实验，CAMVR展现了其在多轮推理任务中的卓越性能。

## 🔬 方法详解

**问题定义**：本文旨在解决当前LVLMs在多轮交互中面临的上下文理解不足和推理碎片化的问题。现有方法在处理复杂的视觉和文本信息时，常常无法有效整合历史信息，导致推理结果不准确。

**核心思路**：CAMVR框架通过引入视觉文本上下文记忆单元（VCMU）和自适应视觉聚焦引导（AVFG）机制，动态管理和调整视觉信息的关注点，以增强多轮推理的连贯性和准确性。

**技术框架**：CAMVR的整体架构包括VCMU作为动态记忆网络，存储每轮交互的视觉特征和文本语义表示；AVFG机制则根据VCMU的上下文动态调整视觉编码器的注意力焦点。

**关键创新**：VCMU和AVFG是CAMVR的核心创新，前者通过动态读写机制管理跨模态信息，后者则确保视觉信息的关注点与上下文相关，从而提升推理的连贯性和准确性。

**关键设计**：在设计中，VCMU采用了特定的参数设置以优化记忆的存储和检索效率，损失函数则结合了多轮推理的特性，以确保模型在训练过程中能够有效学习历史上下文。

## 📊 实验亮点

在多个挑战性数据集上进行的实验表明，CAMVR在多轮推理任务中实现了领先的性能。例如，在VisDial数据集上，CAMVR的表现超越了现有的最先进方法，提升幅度达到XX%，展示了其在复杂视觉文本交互中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、虚拟助手和多模态交互平台等。通过提升多轮视觉文本推理能力，CAMVR能够在复杂场景中提供更准确和连贯的响应，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Current Large Language Models (LLMs) and Vision-Language Large Models (LVLMs) excel in single-turn tasks but face significant challenges in multi-turn interactions requiring deep contextual understanding and complex visual reasoning, often leading to fragmented reasoning, context loss, and hallucinations. To address these limitations, we propose Context-Aware Multi-Turn Visual Reasoning (CAMVR), a novel framework designed to empower LVLMs with robust and coherent multi-turn visual-textual inference capabilities. CAMVR introduces two key innovations: a Visual-Textual Context Memory Unit (VCMU), a dynamic read-write memory network that stores and manages critical visual features, textual semantic representations, and their cross-modal correspondences from each interaction turn; and an Adaptive Visual Focus Guidance (AVFG) mechanism, which leverages the VCMU's context to dynamically adjust the visual encoder's attention to contextually relevant image regions. Our multi-level reasoning integration strategy ensures that response generation is deeply coherent with both current inputs and accumulated historical context. Extensive experiments on challenging datasets, including VisDial, an adapted A-OKVQA, and our novel Multi-Turn Instruction Following (MTIF) dataset, demonstrate that CAMVR consistently achieves state-of-the-art performance.

