---
layout: default
title: Generics and Default Reasoning in Large Language Models
---

# Generics and Default Reasoning in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13718" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13718v1</a>
  <a href="https://arxiv.org/pdf/2508.13718.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13718v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13718v1', 'Generics and Default Reasoning in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: James Ravi Kirkpatrick, Rachel Katharine Sterken

**分类**: cs.CL, cs.AI, cs.LO

**发布日期**: 2025-08-19

**备注**: 33 pages, 26 figures

---

## 💡 一句话要点

**评估大型语言模型在默认推理中的表现与局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `默认推理` `可推翻推理` `一般化` `自然语言处理` `推理能力` `模型评估`

## 📋 核心要点

1. 核心问题：现有大型语言模型在处理可推翻推理时表现不均，且难以区分可推翻推理与演绎推理。
2. 方法要点：通过评估28种LLMs在20种推理模式下的表现，分析不同提示方式对模型性能的影响。
3. 实验或效果：研究发现，少量示例提示对某些模型有提升，但链式推理提示导致性能下降，平均准确率下降11.14%。

## 📝 摘要（中文）

本文评估了28种大型语言模型（LLMs）在处理20种涉及一般化的可推翻推理模式（如“鸟会飞”、“乌鸦是黑色的”）的能力。这些一般化在非单调逻辑中具有重要意义，因其复杂的例外允许行为及其在默认推理、认知和概念获取中的核心地位。研究发现，尽管一些前沿模型在处理许多默认推理问题时表现良好，但模型间的性能差异显著，且提示方式对结果影响较大。少量示例提示对某些模型的性能有适度提升，但链式推理提示常导致性能显著下降（平均准确率下降11.14%）。大多数模型在区分可推翻推理与演绎推理方面存在困难，或将一般化误解为普遍性陈述。这些发现突显了当前LLMs在默认推理中的潜力与局限性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在默认推理中的表现不均和对一般化的误解。现有方法在处理可推翻推理时，模型间性能差异显著，且难以有效区分不同推理类型。

**核心思路**：通过系统评估28种大型语言模型在20种可推翻推理模式下的表现，探索不同提示方式对推理能力的影响，旨在揭示模型的潜力与局限性。

**技术框架**：研究采用了多种提示方式（如少量示例提示和链式推理提示），并对模型在零-shot和few-shot条件下的表现进行了比较，分析其准确率和推理能力。

**关键创新**：本文的主要创新在于系统性地评估了多种大型语言模型在处理复杂推理任务中的能力，特别是对一般化的理解与应用，填补了现有研究的空白。

**关键设计**：研究中使用了不同的提示策略，包括少量示例和链式推理，分析了这些策略对模型性能的影响，发现链式推理提示会导致平均准确率下降11.14%。

## 📊 实验亮点

实验结果显示，尽管一些前沿模型在处理默认推理问题时表现良好，但性能差异显著。少量示例提示对某些模型有适度提升，而链式推理提示导致平均准确率下降11.14%，这表明提示方式对模型性能有重要影响。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和教育技术等。通过改进大型语言模型在推理任务中的表现，可以提升机器理解和生成自然语言的能力，进而推动智能系统在复杂推理场景中的应用。

## 📄 摘要（原文）

> This paper evaluates the capabilities of 28 large language models (LLMs) to reason with 20 defeasible reasoning patterns involving generic generalizations (e.g., 'Birds fly', 'Ravens are black') central to non-monotonic logic. Generics are of special interest to linguists, philosophers, logicians, and cognitive scientists because of their complex exception-permitting behaviour and their centrality to default reasoning, cognition, and concept acquisition. We find that while several frontier models handle many default reasoning problems well, performance varies widely across models and prompting styles. Few-shot prompting modestly improves performance for some models, but chain-of-thought (CoT) prompting often leads to serious performance degradation (mean accuracy drop -11.14%, SD 15.74% in models performing above 75% accuracy in zero-shot condition, temperature 0). Most models either struggle to distinguish between defeasible and deductive inference or misinterpret generics as universal statements. These findings underscore both the promise and limits of current LLMs for default reasoning.

