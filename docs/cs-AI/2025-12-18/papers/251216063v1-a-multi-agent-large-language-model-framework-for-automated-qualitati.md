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

**提出CoTI多Agent LLM框架，自动化定性分析，提升患者体验研究效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多Agent系统` `大型语言模型` `定性分析` `主题分析` `患者体验` `自然语言处理`

## 📋 核心要点

1. 定性主题分析在患者体验研究中至关重要，但其劳动密集、主观且难以规模化是主要挑战。
2. 论文提出CoTI框架，利用多Agent LLM协同工作，自动化主题识别、代码手册生成等定性分析流程。
3. 实验表明，CoTI在心力衰竭患者访谈分析中，结果与资深研究员更接近，优于初级研究员和基线模型。

## 📝 摘要（中文）

理解患者体验对于提升以患者为中心的护理至关重要，尤其是在需要持续沟通的慢性疾病中。然而，定性主题分析作为探索这些体验的主要方法，仍然劳动密集、主观且难以扩展。本研究开发了一个多Agent大型语言模型框架，通过三个Agent（指导者、主题化者、代码手册生成器）自动化定性主题分析，命名为协同主题识别Agent（CoTI）。我们将CoTI应用于12个心力衰竭患者访谈，以分析他们对药物强度的看法。CoTI识别的关键短语、主题和代码手册与资深研究员的结果更相似，优于初级研究员和基线NLP模型。我们还将CoTI集成到面向用户的应用程序中，以实现AI人机交互在定性分析中的应用。然而，CoTI与初级研究员之间的协作仅提供了边际收益，表明他们可能过度依赖CoTI并限制了其独立的批判性思维。

## 🔬 方法详解

**问题定义**：论文旨在解决定性研究中主题分析耗时、主观且难以规模化的问题。现有方法依赖人工，效率低且易受研究者主观影响，难以保证结果的一致性和可重复性。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的强大自然语言处理能力，构建一个多Agent协作框架，模拟人类研究者的分析过程，从而实现定性分析的自动化。通过将复杂的分析任务分解为多个Agent，每个Agent负责不同的子任务，协同完成整体分析。

**技术框架**：CoTI框架包含三个主要Agent：
1. **Instructor (指导者)**：负责整体流程的控制和协调，指导其他Agent完成任务。
2. **Thematizer (主题化者)**：负责从访谈文本中识别关键短语和主题。
3. **CodebookGenerator (代码手册生成器)**：负责根据识别出的主题生成代码手册，用于后续的编码和分析。

整体流程为：Instructor接收访谈文本，指导Thematizer提取主题，然后指导CodebookGenerator生成代码手册。最终，Instructor整合所有结果，输出最终的分析报告。

**关键创新**：该论文的关键创新在于提出了一个多Agent协作的LLM框架，将定性分析任务分解为多个Agent，每个Agent负责不同的子任务，通过协同工作实现自动化。这种多Agent架构能够更好地模拟人类研究者的分析过程，提高分析的效率和准确性。

**关键设计**：论文中没有详细说明关键参数设置、损失函数、网络结构等技术细节。但从描述来看，每个Agent都基于LLM构建，可能使用了不同的prompt engineering技巧来引导LLM完成特定的任务。具体的LLM选择和prompt设计可能对最终结果有较大影响，但论文中未明确说明。

## 📊 实验亮点

CoTI在心力衰竭患者访谈分析中，识别的关键短语、主题和代码手册与资深研究员的结果更相似，优于初级研究员和基线NLP模型。这表明CoTI能够更准确地捕捉到访谈文本中的关键信息，并生成更符合专家认知的分析结果。然而，CoTI与初级研究员的协作收益有限，提示需要关注AI辅助工具对研究者独立思考的影响。

## 🎯 应用场景

该研究成果可应用于医疗健康领域，例如患者体验研究、药物依从性分析等。通过自动化定性分析，可以更高效地理解患者需求，优化医疗服务，并为政策制定提供依据。未来，该框架还可扩展到其他领域，如市场调研、社会科学研究等，具有广阔的应用前景。

## 📄 摘要（原文）

> Understanding patients experiences is essential for advancing patient centered care, especially in chronic diseases that require ongoing communication. However, qualitative thematic analysis, the primary approach for exploring these experiences, remains labor intensive, subjective, and difficult to scale. In this study, we developed a multi agent large language model framework that automates qualitative thematic analysis through three agents (Instructor, Thematizer, CodebookGenerator), named Collaborative Theme Identification Agent (CoTI). We applied CoTI to 12 heart failure patient interviews to analyze their perceptions of medication intensity. CoTI identified key phrases, themes, and codebook that were more similar to those of the senior investigator than both junior investigators and baseline NLP models. We also implemented CoTI into a user-facing application to enable AI human interaction in qualitative analysis. However, collaboration between CoTI and junior investigators provided only marginal gains, suggesting they may overrely on CoTI and limit their independent critical thinking.

