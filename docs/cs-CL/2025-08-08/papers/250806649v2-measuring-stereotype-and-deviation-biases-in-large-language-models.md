---
layout: default
title: Measuring Stereotype and Deviation Biases in Large Language Models
---

# Measuring Stereotype and Deviation Biases in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06649" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06649v2</a>
  <a href="https://arxiv.org/pdf/2508.06649.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06649v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06649v2', 'Measuring Stereotype and Deviation Biases in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniel Wang, Eli Brignac, Minjia Mao, Xiao Fang

**分类**: cs.CL

**发布日期**: 2025-08-08 (更新: 2025-08-18)

---

## 💡 一句话要点

**研究大型语言模型中的刻板印象与偏差偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `刻板印象偏见` `偏差偏见` `内容生成` `公平性`

## 📋 核心要点

1. 现有大型语言模型在生成内容时可能存在刻板印象和偏差偏见，影响其应用的公平性与准确性。
2. 本研究通过生成个体档案的方式，系统性地分析了LLMs在不同人口群体上的偏见表现。
3. 实验结果表明，所有测试的LLMs在多个群体上均存在显著的偏见，揭示了其生成内容的潜在风险。

## 📝 摘要（中文）

大型语言模型（LLMs）在多个领域的广泛应用引发了对其局限性和潜在风险的关注。本研究调查了LLMs可能表现出的两种偏见：刻板印象偏见和偏差偏见。刻板印象偏见指的是LLMs持续将特定特征与特定人口群体关联，而偏差偏见则反映了LLM生成内容中的人口分布与现实世界人口分布之间的差异。通过让四个先进的LLMs生成个体档案，我们考察了每个群体与政治倾向、宗教和性取向等属性之间的关联。实验结果显示，所有被检验的LLMs对多个群体均表现出显著的刻板印象偏见和偏差偏见，揭示了LLMs推断用户属性时可能出现的偏见及其潜在危害。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在生成内容时可能存在的刻板印象偏见和偏差偏见。现有方法未能充分识别和量化这些偏见，导致生成内容的公平性受到质疑。

**核心思路**：通过让多个LLMs生成不同人口群体的个体档案，分析其对特定属性（如政治倾向、宗教和性取向）的关联，从而揭示其潜在的偏见表现。

**技术框架**：研究采用实验设计，首先选择四个先进的LLMs，然后针对每个模型生成多组个体档案，最后对生成内容进行分析和比较，以识别偏见。

**关键创新**：本研究的创新在于系统性地量化和比较不同LLMs在刻板印象和偏差偏见方面的表现，填补了现有文献中的空白。

**关键设计**：在实验中，设计了特定的生成任务和评估标准，以确保对偏见的准确测量，采用了多样化的人口特征和属性组合进行分析。

## 📊 实验亮点

实验结果显示，所有测试的LLMs在多个群体上均表现出显著的刻板印象偏见和偏差偏见，具体表现为与真实世界人口分布存在明显差异。这一发现强调了在使用LLMs时需谨慎对待生成内容的潜在偏见。

## 🎯 应用场景

该研究的结果对大型语言模型的应用具有重要的指导意义，尤其是在社交媒体、招聘系统和内容生成等领域。通过识别和量化偏见，开发者可以更好地调整模型，减少潜在的社会风险，提升模型的公平性和可靠性。

## 📄 摘要（原文）

> Large language models (LLMs) are widely applied across diverse domains, raising concerns about their limitations and potential risks. In this study, we investigate two types of bias that LLMs may display: stereotype bias and deviation bias. Stereotype bias refers to when LLMs consistently associate specific traits with a particular demographic group. Deviation bias reflects the disparity between the demographic distributions extracted from LLM-generated content and real-world demographic distributions. By asking four advanced LLMs to generate profiles of individuals, we examine the associations between each demographic group and attributes such as political affiliation, religion, and sexual orientation. Our experimental results show that all examined LLMs exhibit both significant stereotype bias and deviation bias towards multiple groups. Our findings uncover the biases that occur when LLMs infer user attributes and shed light on the potential harms of LLM-generated outputs.

