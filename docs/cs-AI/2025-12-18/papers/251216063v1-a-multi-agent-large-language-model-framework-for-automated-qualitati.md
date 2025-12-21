---
layout: default
title: A Multi-Agent Large Language Model Framework for Automated Qualitative Analysis
---

# A Multi-Agent Large Language Model Framework for Automated Qualitative Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16063" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16063v1</a>
  <a href="https://arxiv.org/pdf/2512.16063.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16063v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16063v1', 'A Multi-Agent Large Language Model Framework for Automated Qualitative Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qidi Xu, Nuzha Amjad, Grace Giles, Alexa Cumming, De'angelo Hermesky, Alexander Wen, Min Ji Kwak, Yejin Kim

**分类**: cs.HC, cs.AI

**发布日期**: 2025-12-18

**备注**: 42 pages, 5 figures

---

## 💡 一句话要点

**提出CoTI：一个基于多Agent LLM的自动化定性分析框架，应用于心力衰竭患者访谈分析。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多Agent系统` `定性分析` `主题识别` `自然语言处理`

## 📋 核心要点

1. 定性主题分析在患者体验研究中至关重要，但其劳动密集和主观性限制了应用范围。
2. 论文提出CoTI框架，利用多Agent LLM协同工作，自动化主题识别、代码手册生成等流程。
3. 实验表明，CoTI在心力衰竭患者访谈分析中，结果与资深研究员更接近，优于传统NLP模型。

## 📝 摘要（中文）

理解患者体验对于推进以患者为中心的护理至关重要，尤其是在需要持续沟通的慢性疾病中。然而，定性主题分析是探索这些体验的主要方法，但仍然劳动密集、主观且难以扩展。本研究开发了一个多Agent大型语言模型框架，通过三个Agent（指导者、主题化者、代码手册生成器）自动化定性主题分析，命名为协同主题识别Agent（CoTI）。我们将CoTI应用于12个心力衰竭患者访谈，以分析他们对药物强度的看法。CoTI识别的关键短语、主题和代码手册与资深研究员的结果比初级研究员和基线NLP模型更相似。我们还将CoTI集成到面向用户的应用程序中，以实现AI人机交互的定性分析。然而，CoTI与初级研究员之间的协作仅提供了边际收益，表明他们可能过度依赖CoTI并限制了他们的独立批判性思维。

## 🔬 方法详解

**问题定义**：论文旨在解决定性研究中主题分析耗时耗力、主观性强、难以规模化的问题。现有方法依赖人工，效率低且易受研究者个人偏见影响。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的强大自然语言处理能力，构建多个智能Agent协同完成主题分析任务，从而降低人工干预，提高分析效率和一致性。通过Agent之间的协作，模拟专家团队进行分析的过程。

**技术框架**：CoTI框架包含三个主要Agent：Instructor（指导者）、Thematizer（主题化者）和CodebookGenerator（代码手册生成器）。Instructor负责引导整个分析流程，Thematizer负责从访谈文本中提取主题，CodebookGenerator负责生成代码手册。这三个Agent通过协同工作，完成从原始访谈数据到主题和代码手册的自动化生成。

**关键创新**：CoTI的关键创新在于其多Agent协同架构，它将复杂的定性分析任务分解为多个Agent负责的子任务，并通过Agent之间的交互实现整体分析。这种架构能够更好地利用LLM的能力，并提高分析结果的质量和一致性。与传统的单模型方法相比，CoTI更具模块化和可扩展性。

**关键设计**：论文中没有详细描述关键参数设置、损失函数或网络结构等技术细节。但可以推测，每个Agent都使用了预训练的LLM作为基础模型，并通过提示工程（Prompt Engineering）来指导其行为。Agent之间的交互方式和信息传递机制是CoTI设计的关键，但具体实现细节未知。

## 📊 实验亮点

实验结果表明，CoTI在心力衰竭患者访谈分析中，识别的关键短语、主题和代码手册与资深研究员的结果更相似，优于初级研究员和基线NLP模型。这表明CoTI能够有效地模拟专家进行定性分析，并提高分析结果的质量。

## 🎯 应用场景

CoTI框架可应用于医疗健康领域，例如患者反馈分析、临床试验数据挖掘等。它还可以扩展到其他需要定性分析的领域，如市场调研、社会科学研究等。通过自动化定性分析，CoTI可以帮助研究人员更高效地理解数据，发现有价值的见解，并为决策提供支持。

## 📄 摘要（原文）

> Understanding patients experiences is essential for advancing patient centered care, especially in chronic diseases that require ongoing communication. However, qualitative thematic analysis, the primary approach for exploring these experiences, remains labor intensive, subjective, and difficult to scale. In this study, we developed a multi agent large language model framework that automates qualitative thematic analysis through three agents (Instructor, Thematizer, CodebookGenerator), named Collaborative Theme Identification Agent (CoTI). We applied CoTI to 12 heart failure patient interviews to analyze their perceptions of medication intensity. CoTI identified key phrases, themes, and codebook that were more similar to those of the senior investigator than both junior investigators and baseline NLP models. We also implemented CoTI into a user-facing application to enable AI human interaction in qualitative analysis. However, collaboration between CoTI and junior investigators provided only marginal gains, suggesting they may overrely on CoTI and limit their independent critical thinking.

