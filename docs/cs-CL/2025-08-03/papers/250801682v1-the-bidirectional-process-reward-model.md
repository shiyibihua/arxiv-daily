---
layout: default
title: The Bidirectional Process Reward Model
---

# The Bidirectional Process Reward Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01682" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01682v1</a>
  <a href="https://arxiv.org/pdf/2508.01682.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01682v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01682v1', 'The Bidirectional Process Reward Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingyin Zhang, Jun Gao, Xiaoxue Ren, Ziqiang Cao

**分类**: cs.CL

**发布日期**: 2025-08-03

---

## 💡 一句话要点

**提出双向过程奖励模型以提升大语言模型推理质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `过程奖励模型` `双向评估` `大语言模型` `推理质量` `数学推理` `自然语言处理` `智能问答`

## 📋 核心要点

1. 现有的过程奖励模型主要采用单向评估，无法充分利用全局上下文，导致推理一致性验证困难。
2. 本文提出双向过程奖励模型（BiPRM），通过引入并行的从右到左评估流，实时评估早期推理步骤。
3. 实验结果显示，BiPRM在多个基准测试中表现优异，步进奖励评估提升幅度最高达31.9%。

## 📝 摘要（中文）

过程奖励模型（PRMs）作为一种新兴方法，通过对解决方案轨迹中的中间推理步骤赋予细粒度评分，提升了大语言模型（LLMs）的推理质量。然而，现有的PRMs主要采用单向的从左到右（L2R）评估模式，限制了其利用全局上下文的能力，导致难以根据后续步骤验证早期步骤的一致性。为此，本文提出了一种新颖的双向评估模式，称为双向过程奖励模型（BiPRM）。BiPRM在传统L2R流的基础上，增设了并行的从右到左（R2L）评估流，使得后续推理步骤能够实时帮助评估早期步骤。值得注意的是，内置的R2L评估仅通过反转原始推理轨迹的提示修改实现，无需引入额外参数或推理延迟，从而确保BiPRM的高效性和与现有PRM研究的广泛兼容性。我们在两个数学推理基准上进行了广泛实验，结果表明BiPRM在所有设置中均优于单向基线，步进奖励评估提升幅度最高可达31.9%。

## 🔬 方法详解

**问题定义**：现有的过程奖励模型（PRMs）在推理过程中主要采用单向评估，限制了其利用全局上下文的能力，导致难以验证早期推理步骤的一致性。

**核心思路**：本文提出双向过程奖励模型（BiPRM），通过并行的从右到左（R2L）评估流，允许后续推理步骤实时影响早期步骤的评估，从而提升整体推理质量。

**技术框架**：BiPRM的整体架构包括两个主要评估流：传统的从左到右（L2R）流和新引入的从右到左（R2L）流。R2L流通过简单的提示修改实现，无需额外的参数或推理延迟。

**关键创新**：BiPRM的核心创新在于其双向评估机制，使得后续步骤能够实时反馈和调整早期步骤的评估，这一设计显著提升了推理的一致性和准确性。

**关键设计**：在实现上，BiPRM通过反转推理轨迹的提示来构建R2L流，确保了与现有PRM方法的兼容性，同时保持了高效的推理速度。

## 📊 实验亮点

在多个数学推理基准测试中，BiPRM在步进奖励评估上表现优异，相较于单向基线，提升幅度最高可达31.9%。这一结果表明BiPRM在推理质量和一致性验证方面的显著优势。

## 🎯 应用场景

该研究的双向过程奖励模型（BiPRM）具有广泛的应用潜力，尤其在需要复杂推理和决策支持的领域，如数学推理、自然语言处理和智能问答系统等。通过提升推理质量，BiPRM能够为实际应用提供更为可靠的支持，推动相关技术的发展。

## 📄 摘要（原文）

> Process Reward Models (PRMs) have emerged as a promising approach to enhance the reasoning quality of Large Language Models (LLMs) by assigning fine-grained scores to intermediate reasoning steps within a solution trajectory. However, existing PRMs predominantly adopt a unidirectional left-to-right (L2R) evaluation paradigm, which limits their ability to leverage global context, making it challenging to verify the consistency of earlier steps based on later ones. In light of these challenges, we propose a novel bidirectional evaluation paradigm, named Bidirectional Process Reward Model (BiPRM). BiPRM seamlessly incorporates a parallel right-to-left (R2L) evaluation stream alongside the conventional L2R flow, enabling later reasoning steps to help assess earlier ones in real time. Notably, the built-in R2L evaluation is implemented solely through prompt modifications that reverse the original reasoning trajectory, without any additional parameters or inference latency introduced. This ensures BiPRM remains both efficient and broadly compatible with existing PRM studies. We conduct extensive experiments on two mathematical reasoning benchmarks using samples generated by three different policy models. Our method, BiPRM, is evaluated across three backbones and three distinct PRM objectives. Across all settings, BiPRM consistently outperforms unidirectional baselines, achieving up to a 31.9% improvement in stepwise reward evaluation. Generally, our results highlight BiPRM's effectiveness, robustness, and general applicability, offering a promising new direction for process-based reward modeling.

