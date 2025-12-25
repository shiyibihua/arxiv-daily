---
layout: default
title: Assessing the Software Security Comprehension of Large Language Models
---

# Assessing the Software Security Comprehension of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21238" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21238v1</a>
  <a href="https://arxiv.org/pdf/2512.21238.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21238v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21238v1', 'Assessing the Software Security Comprehension of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammed Latif Siddiq, Natalie Sekerak, Antonio Karam, Maria Leal, Arvin Islam-Gomes, Joanna C. S. Santos

**分类**: cs.SE, cs.CR, cs.LG

**发布日期**: 2025-12-24

**备注**: Submitted to Empirical Software Engineering (EMSE) journal

---

## 💡 一句话要点

**系统评估大型语言模型在软件安全理解方面的能力，揭示其知识边界与常见误解。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `软件安全` `能力评估` `布鲁姆分类法` `知识边界`

## 📋 核心要点

1. 现有方法难以全面评估LLMs在软件安全领域的专业知识水平，尤其是在高阶认知能力方面。
2. 论文采用布鲁姆分类法作为框架，系统评估LLMs在软件安全领域的六个认知维度上的能力。
3. 实验结果揭示了LLMs在不同认知层次上的表现差异，并识别了其知识边界和常见的安全误解。

## 📝 摘要（中文）

本文系统地评估了五个领先的大型语言模型（LLMs）：GPT-4o-Mini、GPT-5-Mini、Gemini-2.5-Flash、Llama-3.1和Qwen-2.5在软件安全方面的理解能力。评估框架基于布鲁姆分类法，涵盖六个认知维度：记忆、理解、应用、分析、评估和创造。该研究整合了多样的数据集，包括精选的多项选择题、易受攻击的代码片段（SALLM）、软件安全导论课程的评估、真实案例研究（XBOW）以及安全软件工程课程中的项目创建任务。结果表明，LLMs在较低层次的认知任务（如回忆事实和识别已知漏洞）上表现良好，但在需要推理、架构评估和安全系统创建等较高层次的任务上，性能显著下降。此外，本文提出了一个软件安全知识边界，用于识别模型能够持续保持可靠性能的最高认知水平，并识别了LLMs在布鲁姆分类法的各个层次上表现出的51种常见误解模式。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在软件安全领域知识掌握程度评估的问题。现有方法缺乏系统性和全面性，难以准确评估LLMs在高阶认知能力（如分析、评估和创造）方面的表现，也难以识别LLMs在软件安全方面的知识盲点和常见误解。

**核心思路**：论文的核心思路是利用布鲁姆分类法作为评估框架，将软件安全知识划分为六个认知维度（记忆、理解、应用、分析、评估和创造），并设计相应的评估任务，从而全面评估LLMs在不同认知层次上的软件安全能力。通过分析LLMs在不同任务上的表现，可以确定其知识边界和常见误解。

**技术框架**：该研究的技术框架包括以下几个主要组成部分：1) 选择五个代表性的LLMs：GPT-4o-Mini、GPT-5-Mini、Gemini-2.5-Flash、Llama-3.1和Qwen-2.5；2) 构建多样化的数据集，包括多项选择题、易受攻击的代码片段（SALLM）、软件安全课程评估、真实案例研究（XBOW）和项目创建任务；3) 设计与布鲁姆分类法六个认知维度相对应的评估任务；4) 分析LLMs在不同任务上的表现，计算准确率等指标；5) 识别LLMs的知识边界和常见误解模式。

**关键创新**：论文的关键创新在于：1) 系统地将布鲁姆分类法应用于LLMs的软件安全能力评估；2) 构建了多样化的数据集，涵盖了不同类型的软件安全知识和技能；3) 提出了软件安全知识边界的概念，用于量化LLMs的软件安全能力；4) 识别了LLMs在软件安全方面存在的51种常见误解模式。

**关键设计**：论文的关键设计包括：1) 数据集的选择，确保涵盖不同类型的软件安全知识和技能，并与布鲁姆分类法的六个认知维度相对应；2) 评估任务的设计，确保能够有效评估LLMs在不同认知层次上的表现；3) 知识边界的定义，采用统计方法确定模型能够持续保持可靠性能的最高认知水平；4) 误解模式的识别，通过人工分析LLMs的错误答案和解释，总结出常见的错误模式。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21238v1/figures/framework.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21238v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21238v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，LLMs在较低层次的认知任务（如回忆事实和识别已知漏洞）上表现良好，但在需要推理、架构评估和安全系统创建等较高层次的任务上，性能显著下降。研究识别了LLMs在布鲁姆分类法的各个层次上表现出的51种常见误解模式，为后续改进LLMs的软件安全能力提供了重要参考。

## 🎯 应用场景

该研究成果可用于指导LLMs在软件开发中的安全应用，帮助开发者了解LLMs的安全能力边界，避免过度依赖LLMs处理复杂的安全问题。同时，该研究也为LLMs的软件安全能力提升提供了方向，例如可以通过针对性地训练来弥补LLMs在高阶认知能力方面的不足，减少其在软件安全方面的误解。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used in software development, but their level of software security expertise remains unclear. This work systematically evaluates the security comprehension of five leading LLMs: GPT-4o-Mini, GPT-5-Mini, Gemini-2.5-Flash, Llama-3.1, and Qwen-2.5, using Blooms Taxonomy as a framework. We assess six cognitive dimensions: remembering, understanding, applying, analyzing, evaluating, and creating. Our methodology integrates diverse datasets, including curated multiple-choice questions, vulnerable code snippets (SALLM), course assessments from an Introduction to Software Security course, real-world case studies (XBOW), and project-based creation tasks from a Secure Software Engineering course. Results show that while LLMs perform well on lower-level cognitive tasks such as recalling facts and identifying known vulnerabilities, their performance degrades significantly on higher-order tasks that require reasoning, architectural evaluation, and secure system creation. Beyond reporting aggregate accuracy, we introduce a software security knowledge boundary that identifies the highest cognitive level at which a model consistently maintains reliable performance. In addition, we identify 51 recurring misconception patterns exhibited by LLMs across Blooms levels.

