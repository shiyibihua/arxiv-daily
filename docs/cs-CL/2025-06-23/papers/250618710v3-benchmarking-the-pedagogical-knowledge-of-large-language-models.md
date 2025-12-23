---
layout: default
title: Benchmarking the Pedagogical Knowledge of Large Language Models
---

# Benchmarking the Pedagogical Knowledge of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18710" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18710v3</a>
  <a href="https://arxiv.org/pdf/2506.18710.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18710v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18710v3', 'Benchmarking the Pedagogical Knowledge of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maxime Lelièvre, Amy Waldock, Meng Liu, Natalia Valdés Aspillaga, Alasdair Mackintosh, María José Ogando Portela, Jared Lee, Paul Atherton, Robin A. A. Ince, Oliver G. B. Garrod

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-23 (更新: 2025-07-01)

---

## 💡 一句话要点

**提出教学知识基准以评估大型语言模型的教育能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `教学知识` `基准测试` `特殊教育` `教育技术` `模型评估` `跨领域知识`

## 📋 核心要点

1. 现有基准测试主要关注内容知识，缺乏对模型教学法理解的评估，导致教育应用中的关键知识缺口。
2. 本文提出了教学基准，设计了一套新颖的数据集，专注于评估模型的跨领域教学知识和特殊教育需求知识。
3. 实验结果显示，97个模型在教学知识问题上的准确率从28%到89%不等，展示了模型在教育领域的潜力和差异。

## 📝 摘要（中文）

基准测试如大规模多任务语言理解（MMLU）在评估人工智能在各领域的知识和能力方面发挥了重要作用。然而，现有基准主要集中在内容知识上，未能有效评估模型对教学法的理解。本文引入了教学基准，这是一个新颖的数据集，旨在评估大型语言模型在跨领域教学知识（CDPK）和特殊教育需求与残疾（SEND）方面的能力。基准基于专业发展考试中的问题，涵盖教学策略和评估方法等多个子领域。我们报告了97个模型的结果，准确率从28%到89%不等，并提供了在线排行榜，允许根据模型属性进行交互式探索和过滤。教育相关的基准对于衡量模型理解教学概念的能力至关重要，有助于支持有效的教学实践。

## 🔬 方法详解

**问题定义**：本文旨在解决现有基准测试未能有效评估大型语言模型在教学法理解方面的不足，特别是在教育领域的应用中存在的知识缺口。

**核心思路**：通过引入教学基准，构建一个专注于评估模型跨领域教学知识和特殊教育需求知识的数据集，以填补这一空白。

**技术框架**：整体架构包括数据集的构建、模型评估和结果分析三个主要模块。数据集由专业发展考试中的问题构成，涵盖多种教学策略和评估方法。

**关键创新**：最重要的创新在于首次系统性地评估大型语言模型的教学知识，特别是跨领域和特殊教育需求方面的能力，这与现有方法的内容知识评估形成鲜明对比。

**关键设计**：数据集中的问题经过精心策划，确保涵盖多种教学法的子领域，模型评估采用准确率作为主要指标，并提供在线排行榜以便于实时更新和交互分析。

## 📊 实验亮点

实验结果显示，97个模型在教学知识问题上的准确率从28%到89%不等，表明不同模型在教育领域的表现差异。这一发现为未来模型的优化和教育应用提供了重要参考。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和教师培训工具。通过评估模型的教学知识，能够更好地指导教育工具的开发，确保其能够满足学习者的需求，进而提升教育质量和效率。

## 📄 摘要（原文）

> Benchmarks like Massive Multitask Language Understanding (MMLU) have played a pivotal role in evaluating AI's knowledge and abilities across diverse domains. However, existing benchmarks predominantly focus on content knowledge, leaving a critical gap in assessing models' understanding of pedagogy - the method and practice of teaching. This paper introduces The Pedagogy Benchmark, a novel dataset designed to evaluate large language models on their Cross-Domain Pedagogical Knowledge (CDPK) and Special Education Needs and Disability (SEND) pedagogical knowledge. These benchmarks are built on a carefully curated set of questions sourced from professional development exams for teachers, which cover a range of pedagogical subdomains such as teaching strategies and assessment methods. Here we outline the methodology and development of these benchmarks. We report results for 97 models, with accuracies spanning a range from 28% to 89% on the pedagogical knowledge questions. We consider the relationship between cost and accuracy and chart the progression of the Pareto value frontier over time. We provide online leaderboards at https://rebrand.ly/pedagogy which are updated with new models and allow interactive exploration and filtering based on various model properties, such as cost per token and open-vs-closed weights, as well as looking at performance in different subjects. LLMs and generative AI have tremendous potential to influence education and help to address the global learning crisis. Education-focused benchmarks are crucial to measure models' capacities to understand pedagogical concepts, respond appropriately to learners' needs, and support effective teaching practices across diverse contexts. They are needed for informing the responsible and evidence-based deployment of LLMs and LLM-based tools in educational settings, and for guiding both development and policy decisions.

