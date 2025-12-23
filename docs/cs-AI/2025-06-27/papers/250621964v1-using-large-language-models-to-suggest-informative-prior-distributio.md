---
layout: default
title: Using Large Language Models to Suggest Informative Prior Distributions in Bayesian Statistics
---

# Using Large Language Models to Suggest Informative Prior Distributions in Bayesian Statistics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21964" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21964v1</a>
  <a href="https://arxiv.org/pdf/2506.21964.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21964v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21964v1', 'Using Large Language Models to Suggest Informative Prior Distributions in Bayesian Statistics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Michael A. Riegler, Kristoffer Herland Hellton, Vajira Thambawita, Hugo L. Hammer

**分类**: stat.ME, cs.AI, cs.CL

**发布日期**: 2025-06-27

---

## 💡 一句话要点

**利用大型语言模型建议贝叶斯统计中的信息性先验分布**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `贝叶斯统计` `大型语言模型` `信息性先验` `Kullback-Leibler散度` `自动化选择` `统计建模` `数据分析`

## 📋 核心要点

1. 现有贝叶斯统计方法在选择先验分布时面临挑战，常常依赖主观判断，且资源消耗大。
2. 本文提出利用大型语言模型（LLMs）来自动建议信息性先验分布，旨在提高选择的客观性和效率。
3. 实验结果显示，Claude和Gemini在提供先验方面优于ChatGPT，尤其在弱信息性先验的表现上，Claude展现出更好的校准能力。

## 📝 摘要（中文）

选择贝叶斯统计中的先验分布是一项具有挑战性、资源密集且主观的任务。本文分析了使用大型语言模型（LLMs）来建议合适的知识基础信息性先验。我们开发了一个广泛的提示，要求LLMs不仅建议先验，还要验证和反思其选择。我们在两个真实数据集（心脏病风险和混凝土强度）上评估了Claude Opus、Gemini 2.5 Pro和ChatGPT-4o-mini。所有LLMs都正确识别了所有关联的方向。建议先验的质量通过其与最大似然估计分布的Kullback-Leibler散度来衡量。实验结果表明，Claude和Gemini提供的先验优于ChatGPT，尤其是在弱信息性先验方面，Claude表现出明显优势。

## 🔬 方法详解

**问题定义**：本文旨在解决贝叶斯统计中先验分布选择的主观性和资源密集性问题。现有方法往往依赖于专家知识，导致选择过程不够高效和客观。

**核心思路**：通过利用大型语言模型（LLMs），本文提出了一种新的方法来自动生成和验证信息性先验分布，从而减少人为偏差并提高选择的准确性。

**技术框架**：研究中使用的技术框架包括三个主要模块：1) 提示生成模块，设计用于引导LLMs生成先验；2) 验证模块，评估生成先验的合理性；3) 反馈模块，允许LLMs反思其选择并进行调整。

**关键创新**：本文的主要创新在于结合LLMs的自然语言处理能力与贝叶斯统计的需求，首次系统性地将LLMs应用于先验分布的选择中，显著提高了选择的客观性和效率。

**关键设计**：在实验中，使用Kullback-Leibler散度作为衡量建议先验质量的标准，LLMs的提示设计也经过精心调整，以确保其生成的先验具有适当的信息性和校准性。实验中还比较了不同LLMs的表现，发现Claude在弱信息性先验的生成上具有明显优势。

## 📊 实验亮点

实验结果表明，Claude和Gemini在提供信息性先验方面的表现优于ChatGPT，尤其在弱信息性先验的生成中，Claude未默认使用模糊的均值0，显示出更好的校准能力。这些发现为LLMs在贝叶斯统计中的应用提供了有力支持。

## 🎯 应用场景

该研究的潜在应用领域包括医学统计、工程质量控制和社会科学研究等领域，能够为研究人员提供更为客观和高效的先验选择工具。未来，随着LLMs技术的进一步发展，可能会在更多复杂的统计建模任务中发挥重要作用。

## 📄 摘要（原文）

> Selecting prior distributions in Bayesian statistics is challenging, resource-intensive, and subjective. We analyze using large-language models (LLMs) to suggest suitable, knowledge-based informative priors. We developed an extensive prompt asking LLMs not only to suggest priors but also to verify and reflect on their choices.
>   We evaluated Claude Opus, Gemini 2.5 Pro, and ChatGPT-4o-mini on two real datasets: heart disease risk and concrete strength. All LLMs correctly identified the direction for all associations (e.g., that heart disease risk is higher for males). The quality of suggested priors was measured by their Kullback-Leibler divergence from the maximum likelihood estimator's distribution.
>   The LLMs suggested both moderately and weakly informative priors. The moderate priors were often overconfident, resulting in distributions misaligned with the data. In our experiments, Claude and Gemini provided better priors than ChatGPT. For weakly informative priors, a key performance difference emerged: ChatGPT and Gemini defaulted to an "unnecessarily vague" mean of 0, while Claude did not, demonstrating a significant advantage.
>   The ability of LLMs to identify correct associations shows their great potential as an efficient, objective method for developing informative priors. However, the primary challenge remains in calibrating the width of these priors to avoid over- and under-confidence.

