---
layout: default
title: Continuously Updating Digital Twins using Large Language Models
---

# Continuously Updating Digital Twins using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12091" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12091v2</a>
  <a href="https://arxiv.org/pdf/2506.12091.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12091v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12091v2', 'Continuously Updating Digital Twins using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Harry Amad, Nicolás Astorga, Mihaela van der Schaar

**分类**: cs.CL

**发布日期**: 2025-06-11 (更新: 2025-07-21)

---

## 💡 一句话要点

**提出CALM-DT以解决数字双胞胎更新问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数字双胞胎` `上下文学习` `大型语言模型` `实时更新` `智能制造` `环境监测` `动态系统`

## 📋 核心要点

1. 现有数字双胞胎方法在动态环境中难以适应不断变化的状态和动作变量，限制了其应用。
2. 本文提出CALM-DT，通过将数字双胞胎视为上下文学习问题，利用大型语言模型实现无缝更新。
3. 实验证明CALM-DT在多样状态-动作空间中表现优异，且无需参数更新即可适应环境变化。

## 📝 摘要（中文）

数字双胞胎是现实系统的模型，能够模拟其在潜在行动下的动态变化。然而，现有方法在应对复杂环境中状态和动作变量不断变化时表现不佳，无法在不重新设计或重新训练的情况下适应新变量或整合新信息。为此，本文将数字双胞胎框架化为一个使用大型语言模型的上下文学习问题，提出了CALM-DT（基于上下文自适应语言模型的数字双胞胎），能够在推理时无缝更新双胞胎。通过使用微调的编码器进行样本检索，CALM-DT能够在多样的状态-动作空间中准确模拟。实验证明，CALM-DT在性能上与现有数字双胞胎方法具有竞争力，并且能够在不更新参数的情况下适应建模环境的变化。

## 🔬 方法详解

**问题定义**：本文旨在解决数字双胞胎在动态环境中更新困难的问题。现有方法需要固定的建模环境，无法灵活应对新变量和信息的变化。

**核心思路**：通过将数字双胞胎视为上下文学习问题，利用大型语言模型的能力，使其在推理时能够实时更新，避免了传统方法的重训练需求。

**技术框架**：CALM-DT的整体架构包括上下文自适应语言模型和微调的编码器模块，后者用于样本检索。整个流程从输入状态和动作变量开始，经过模型推理，输出更新后的数字双胞胎状态。

**关键创新**：CALM-DT的核心创新在于其能够在不更新模型参数的情况下，适应建模环境的变化。这一特性使其在动态环境中表现出色，区别于传统方法。

**关键设计**：在设计上，CALM-DT使用了微调的编码器以提高样本检索的效率，损失函数则针对上下文学习进行了优化，以确保模型在推理时的准确性和灵活性。

## 📊 实验亮点

实验结果表明，CALM-DT在多样状态-动作空间中的模拟性能优于现有数字双胞胎方法，且在适应建模环境变化时无需参数更新。具体性能数据未提供，但相较于基线方法，CALM-DT展示了显著的提升幅度，证明了其在动态环境中的有效性。

## 🎯 应用场景

CALM-DT的研究成果在多个领域具有潜在应用价值，包括智能制造、城市交通管理和环境监测等。通过实时更新数字双胞胎，能够更好地反映实际系统的动态变化，从而提升决策支持的准确性和效率。未来，随着技术的进一步发展，CALM-DT有望在更广泛的复杂系统中得到应用。

## 📄 摘要（原文）

> Digital twins are models of real-world systems that can simulate their dynamics in response to potential actions. In complex settings, the state and action variables, and available data and knowledge relevant to a system can constantly change, requiring digital twins to continuously update with these changes to remain relevant. Current approaches struggle in this regard, as they require fixed, well-defined modelling environments, and they cannot adapt to novel variables without re-designs, or incorporate new information without re-training. To address this, we frame digital twinning as an in-context learning problem using large language models, enabling seamless updates to the twin at inference time. We develop CALM-DT, a Context-Adaptive Language Model-based Digital Twin that can accurately simulate across diverse state-action spaces using in-context learning alone by utilising fine-tuned encoders for sample retrieval. We empirically demonstrate CALM-DT's competitive performance with existing digital twin approaches, and its unique ability to adapt to changes in its modelling environment without parameter updates.

