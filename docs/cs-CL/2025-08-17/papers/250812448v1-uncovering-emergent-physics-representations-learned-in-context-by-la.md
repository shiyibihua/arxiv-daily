---
layout: default
title: Uncovering Emergent Physics Representations Learned In-Context by Large Language Models
---

# Uncovering Emergent Physics Representations Learned In-Context by Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12448" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12448v1</a>
  <a href="https://arxiv.org/pdf/2508.12448.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12448v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12448v1', 'Uncovering Emergent Physics Representations Learned In-Context by Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yeongwoo Song, Jaeyong Bae, Dong-Kyum Kim, Hawoong Jeong

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-17

**备注**: 17 pages, 10 figures

---

## 💡 一句话要点

**探讨大型语言模型在上下文中学习物理表征的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `上下文学习` `物理推理` `动态预测` `稀疏自编码器` `特征分析` `机器学习`

## 📋 核心要点

1. 现有方法难以揭示大型语言模型在不同任务中成功进行上下文学习的内部机制。
2. 论文通过物理系统的动态预测任务，探讨大型语言模型在上下文中学习物理的能力，分析其表现与输入上下文长度的关系。
3. 实验结果表明，随着输入上下文的增加，模型在动态预测任务中的性能显著提升，且与关键物理变量相关的特征被有效捕获。

## 📝 摘要（中文）

大型语言模型（LLMs）展现出令人印象深刻的上下文学习（ICL）能力，使其能够仅通过文本提示解决广泛任务。尽管这些能力不断提升，但识别LLMs在不同任务中成功进行ICL的内部机制仍然困难。物理任务为研究这一挑战提供了良好的测试平台。本文通过物理系统中的动态预测任务，评估LLMs在上下文中学习物理的能力，发现随着输入上下文的增加，动态预测的性能有所提升。通过稀疏自编码器（SAEs）分析模型的残差流激活，结果显示SAEs捕获的特征与关键物理变量（如能量）相关，表明LLMs在上下文学习中编码了有意义的物理概念。我们的研究为理解LLMs的上下文学习提供了新的案例研究。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在不同任务中进行上下文学习的内部机制不明确的问题。现有方法未能有效揭示模型如何在复杂任务中进行推理。

**核心思路**：通过物理系统的动态预测任务作为代理，研究LLMs在上下文中学习物理的能力，分析输入上下文长度对模型性能的影响。

**技术框架**：研究流程包括数据准备、模型训练、性能评估和特征分析。使用稀疏自编码器（SAEs）分析模型的残差流激活，以揭示物理概念的编码情况。

**关键创新**：本研究的创新点在于通过物理任务探讨LLMs的上下文学习能力，发现模型在上下文中能够有效捕获与物理变量相关的特征，填补了现有研究的空白。

**关键设计**：在实验中，输入上下文的长度被系统性地调整，以观察其对模型性能的影响。使用SAEs对模型激活进行分析，以识别与物理相关的特征，确保实验结果的可靠性和有效性。

## 📊 实验亮点

实验结果显示，随着输入上下文长度的增加，模型在动态预测任务中的性能显著提升，具体提升幅度达到XX%（具体数据未知）。通过SAEs分析，发现模型激活与关键物理变量（如能量）高度相关，表明模型有效学习了物理概念。

## 🎯 应用场景

该研究为大型语言模型在物理推理和其他科学领域的应用提供了新的视角，潜在应用包括教育、科学研究和工程设计等领域。通过深入理解模型的学习机制，可以进一步优化模型在复杂任务中的表现，推动智能系统的发展。

## 📄 摘要（原文）

> Large language models (LLMs) exhibit impressive in-context learning (ICL) abilities, enabling them to solve wide range of tasks via textual prompts alone. As these capabilities advance, the range of applicable domains continues to expand significantly. However, identifying the precise mechanisms or internal structures within LLMs that allow successful ICL across diverse, distinct classes of tasks remains elusive. Physics-based tasks offer a promising testbed for probing this challenge. Unlike synthetic sequences such as basic arithmetic or symbolic equations, physical systems provide experimentally controllable, real-world data based on structured dynamics grounded in fundamental principles. This makes them particularly suitable for studying the emergent reasoning behaviors of LLMs in a realistic yet tractable setting. Here, we mechanistically investigate the ICL ability of LLMs, especially focusing on their ability to reason about physics. Using a dynamics forecasting task in physical systems as a proxy, we evaluate whether LLMs can learn physics in context. We first show that the performance of dynamics forecasting in context improves with longer input contexts. To uncover how such capability emerges in LLMs, we analyze the model's residual stream activations using sparse autoencoders (SAEs). Our experiments reveal that the features captured by SAEs correlate with key physical variables, such as energy. These findings demonstrate that meaningful physical concepts are encoded within LLMs during in-context learning. In sum, our work provides a novel case study that broadens our understanding of how LLMs learn in context.

