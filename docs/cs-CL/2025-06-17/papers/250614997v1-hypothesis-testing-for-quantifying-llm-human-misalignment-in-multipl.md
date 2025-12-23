---
layout: default
title: Hypothesis Testing for Quantifying LLM-Human Misalignment in Multiple Choice Settings
---

# Hypothesis Testing for Quantifying LLM-Human Misalignment in Multiple Choice Settings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14997" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14997v1</a>
  <a href="https://arxiv.org/pdf/2506.14997.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14997v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14997v1', 'Hypothesis Testing for Quantifying LLM-Human Misalignment in Multiple Choice Settings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Harbin Hong, Sebastian Caldas, Liu Leqi

**分类**: cs.CY, cs.CL, cs.LG

**发布日期**: 2025-06-17

---

## 💡 一句话要点

**提出假设检验框架以量化LLM与人类行为的不一致性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `假设检验` `人类行为模拟` `社会科学研究` `多项选择调查`

## 📋 核心要点

1. 核心问题：现有的LLM在模拟人类行为时存在显著的不一致性，尤其是在多项选择调查中表现不佳。
2. 方法要点：论文提出了一种基于假设检验的定量框架，以评估LLM与人类行为之间的对齐程度。
3. 实验或效果：应用该框架后发现，流行的语言模型在模拟特定人群的意见时效果不佳，提示需要改进LLM的使用方法。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在社会科学研究中的广泛应用（如经济学和市场营销），评估这些模型如何复制人类行为变得至关重要。本文通过假设检验，提出了一种定量框架，用于评估LLM模拟与实际人类行为在多项选择调查中的不一致性。该框架能够以原则性方式判断特定语言模型是否能够有效模拟人类的意见、决策和通过多项选择选项表现出的行为。我们将该框架应用于一种流行的语言模型，发现其在模拟不同种族、年龄和收入的争议性问题时，表现不佳。这引发了对该语言模型与被测试人群之间一致性的质疑，强调了在社会科学研究中使用LLM时需要超越简单的人类主体模拟的新实践。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLMs）在多项选择调查中模拟人类行为时的对齐问题。现有方法往往未能准确反映不同人群的真实意见和决策，导致结果的不可靠性。

**核心思路**：论文提出通过假设检验的方式，建立一个定量框架来评估LLM与人类行为的对齐程度。这种方法允许研究者以系统化的方式判断模型的有效性，避免了主观判断的偏差。

**技术框架**：整体架构包括数据收集、模型模拟、假设检验和结果分析四个主要模块。首先收集多项选择调查数据，然后使用LLM进行模拟，接着进行假设检验以评估模拟结果与实际数据的差异，最后分析结果以得出结论。

**关键创新**：最重要的技术创新在于将假设检验引入LLM的行为评估中，使得对齐程度的评估更加科学和量化。这与传统的定性分析方法形成鲜明对比，提供了更为严谨的评估手段。

**关键设计**：在框架中，关键参数包括假设检验的显著性水平、样本选择的多样性以及模型的选择标准。损失函数设计上，强调了模拟结果与实际结果之间的距离，以确保模型的输出尽可能接近真实人类行为。

## 📊 实验亮点

实验结果显示，所测试的流行语言模型在模拟不同种族、年龄和收入的公众意见时，表现出显著的不一致性。具体而言，在处理争议性问题时，该模型的模拟结果与实际人类行为之间的差异达到了统计显著性，提示其在特定人群中的应用效果不佳。

## 🎯 应用场景

该研究的潜在应用领域包括社会科学、市场研究和政策制定等。通过提供一种量化评估LLM与人类行为对齐程度的方法，研究者可以更好地理解和利用LLM在模拟人类决策中的局限性，从而提升研究的准确性和可靠性。未来，该框架可能推动LLM在社会科学领域的更广泛应用，促进更为科学的研究方法。

## 📄 摘要（原文）

> As Large Language Models (LLMs) increasingly appear in social science research (e.g., economics and marketing), it becomes crucial to assess how well these models replicate human behavior. In this work, using hypothesis testing, we present a quantitative framework to assess the misalignment between LLM-simulated and actual human behaviors in multiple-choice survey settings. This framework allows us to determine in a principled way whether a specific language model can effectively simulate human opinions, decision-making, and general behaviors represented through multiple-choice options. We applied this framework to a popular language model for simulating people's opinions in various public surveys and found that this model is ill-suited for simulating the tested sub-populations (e.g., across different races, ages, and incomes) for contentious questions. This raises questions about the alignment of this language model with the tested populations, highlighting the need for new practices in using LLMs for social science studies beyond naive simulations of human subjects.

