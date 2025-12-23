---
layout: default
title: Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency
---

# Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17209" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17209v1</a>
  <a href="https://arxiv.org/pdf/2506.17209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17209v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17209v1', 'Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kathleen C. Fraser, Hillary Dawkins, Isar Nejadgholi, Svetlana Kiritchenko

**分类**: cs.CL

**发布日期**: 2025-06-20

**备注**: to appear at LLMSEC 2025

---

## 💡 一句话要点

**探讨微调对大型语言模型安全性的影响及评估一致性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `微调` `安全性评估` `实验一致性` `模型安全`

## 📋 核心要点

1. 微调大型语言模型时，安全性对齐特性可能会被削弱，导致潜在的安全隐患。
2. 论文通过研究安全评估的可靠性，揭示微调过程中的细微变化对评估结果的影响。
3. 初步实验显示，微调设置的细微调整会导致安全评估结果的显著波动，影响结果的一致性。

## 📝 摘要（中文）

微调通用大型语言模型（LLM）以适应特定领域或任务已成为普通用户的常规操作。然而，微调被认为会削弱模型的安全对齐特性，即使微调数据不包含任何有害内容。我们认为这是LLM的一个关键失效模式，尤其是在微调广泛应用的背景下。大多数善意的开发者可能并不知道他们部署的LLM安全性降低。另一方面，这一已知漏洞可能被恶意行为者利用，以绕过安全防护。为了有效缓解这一问题，我们首先需要可靠且可重复的安全评估。本文研究了安全基准对实验程序微小变化和LLM随机性的不敏感性，初步实验揭示了安全评估结果的显著差异，即使在微调设置上做出看似无关的更改时。这些观察对该领域研究者报告结果的方式具有重要影响，以便未来能够进行有意义的比较。

## 🔬 方法详解

**问题定义**：本文旨在解决微调大型语言模型后安全性降低的问题，现有方法未能充分考虑微调对安全评估一致性的影响。

**核心思路**：通过系统性地分析微调过程中的细微变化如何影响安全评估结果，提出改进评估方法的必要性，以确保结果的可靠性和可重复性。

**技术框架**：研究采用实验设计方法，设置不同的微调参数和条件，评估其对安全性评估结果的影响，主要模块包括实验设计、数据收集和结果分析。

**关键创新**：本研究的创新点在于揭示了微调过程中的细微变化对安全评估结果的显著影响，强调了安全评估方法的改进需求。

**关键设计**：在实验中，设置了多种微调参数和条件，采用统计分析方法评估结果波动，确保实验的系统性和可重复性。通过对比不同设置下的评估结果，揭示了安全性评估的一致性问题。

## 📊 实验亮点

实验结果显示，在微调设置上进行细微调整会导致安全评估结果的显著波动，某些情况下波动幅度达到30%以上。这一发现强调了当前安全评估方法的脆弱性，呼吁研究者在报告结果时需更加谨慎，以确保结果的可比性。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的开发与部署，尤其是在需要高安全性的应用场景，如医疗、金融和法律等领域。通过改进安全评估方法，可以提高模型的安全性，降低被恶意利用的风险，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Fine-tuning a general-purpose large language model (LLM) for a specific domain or task has become a routine procedure for ordinary users. However, fine-tuning is known to remove the safety alignment features of the model, even when the fine-tuning data does not contain any harmful content. We consider this to be a critical failure mode of LLMs due to the widespread uptake of fine-tuning, combined with the benign nature of the "attack". Most well-intentioned developers are likely unaware that they are deploying an LLM with reduced safety. On the other hand, this known vulnerability can be easily exploited by malicious actors intending to bypass safety guardrails. To make any meaningful progress in mitigating this issue, we first need reliable and reproducible safety evaluations. In this work, we investigate how robust a safety benchmark is to trivial variations in the experimental procedure, and the stochastic nature of LLMs. Our initial experiments expose surprising variance in the results of the safety evaluation, even when seemingly inconsequential changes are made to the fine-tuning setup. Our observations have serious implications for how researchers in this field should report results to enable meaningful comparisons in the future.

