---
layout: default
title: I Think, Therefore I Am Under-Qualified? A Benchmark for Evaluating Linguistic Shibboleth Detection in LLM Hiring Evaluations
---

# I Think, Therefore I Am Under-Qualified? A Benchmark for Evaluating Linguistic Shibboleth Detection in LLM Hiring Evaluations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04939" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04939v1</a>
  <a href="https://arxiv.org/pdf/2508.04939.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04939v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04939v1', 'I Think, Therefore I Am Under-Qualified? A Benchmark for Evaluating Linguistic Shibboleth Detection in LLM Hiring Evaluations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Julia Kharchenko, Tanya Roosta, Aman Chadha, Chirag Shah

**分类**: cs.CL

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出语言标记检测基准以评估LLM招聘评估中的偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `语言偏见` `招聘评估` `公平性` `自动化决策` `语言标记` `模型评估`

## 📋 核心要点

1. 核心问题：现有的招聘评估方法可能存在对某些语言模式的偏见，导致不公平的评价结果。
2. 方法要点：本文提出了一种基准，通过控制语言变体来评估LLMs对语言标记的反应，确保语义等价性。
3. 实验或效果：研究显示，模糊语言的回答平均评分低25.6%，有效识别了模型特定的偏见。

## 📝 摘要（中文）

本文介绍了一个全面的基准，用于评估大型语言模型（LLMs）对语言标记的响应，这些标记可能无意中揭示性别、社会阶层或地区背景等人口属性。通过构建100个经过验证的问题-回答对的面试模拟，我们展示了LLMs如何系统性地惩罚某些语言模式，尤其是模糊语言，尽管内容质量相当。我们的基准生成受控的语言变体，能够精确测量自动评估系统中的人口偏见。研究表明，模糊回答的平均评分低25.6%，并有效识别模型特定的偏见，为检测和衡量AI系统中的语言歧视奠定了基础框架，具有广泛的公平性应用潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在招聘评估中对语言标记的偏见问题。现有方法未能有效识别和量化这种偏见，导致不公平的评估结果。

**核心思路**：论文的核心思路是构建一个基准，通过设计受控的语言变体来评估LLMs对不同语言模式的反应，从而精确测量人口偏见。这样的设计能够确保语义的一致性，同时突出不同语言模式的影响。

**技术框架**：整体架构包括数据收集、问题设计、模型评估和结果分析四个主要模块。首先，收集100个经过验证的问题-回答对，然后通过控制语言变体进行模拟评估，最后分析模型的评分结果。

**关键创新**：最重要的技术创新在于生成受控的语言变体，能够在保持语义等价的同时，隔离特定的语言现象。这与现有方法的本质区别在于，后者往往无法有效控制变量，导致偏见评估的不准确。

**关键设计**：关键设计包括选择合适的语言模式进行变体生成，设置损失函数以优化模型对不同语言模式的响应，以及确保评估过程中的语义一致性。

## 📊 实验亮点

实验结果显示，使用模糊语言的回答在评分上平均低25.6%，有效识别了模型特定的偏见。这一发现为改进招聘评估中的公平性提供了重要依据。

## 🎯 应用场景

该研究的潜在应用领域包括招聘系统、教育评估和其他自动化决策系统，能够帮助识别和减少因语言偏见导致的不公平现象。未来，该基准有望推动更公平的AI系统设计，促进社会公正。

## 📄 摘要（原文）

> This paper introduces a comprehensive benchmark for evaluating how Large Language Models (LLMs) respond to linguistic shibboleths: subtle linguistic markers that can inadvertently reveal demographic attributes such as gender, social class, or regional background. Through carefully constructed interview simulations using 100 validated question-response pairs, we demonstrate how LLMs systematically penalize certain linguistic patterns, particularly hedging language, despite equivalent content quality. Our benchmark generates controlled linguistic variations that isolate specific phenomena while maintaining semantic equivalence, which enables the precise measurement of demographic bias in automated evaluation systems. We validate our approach along multiple linguistic dimensions, showing that hedged responses receive 25.6% lower ratings on average, and demonstrate the benchmark's effectiveness in identifying model-specific biases. This work establishes a foundational framework for detecting and measuring linguistic discrimination in AI systems, with broad applications to fairness in automated decision-making contexts.

