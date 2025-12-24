---
layout: default
title: Benchmarking the Medical Understanding and Reasoning of Large Language Models in Arabic Healthcare Tasks
---

# Benchmarking the Medical Understanding and Reasoning of Large Language Models in Arabic Healthcare Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15797" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15797v1</a>
  <a href="https://arxiv.org/pdf/2508.15797.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15797v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15797v1', 'Benchmarking the Medical Understanding and Reasoning of Large Language Models in Arabic Healthcare Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nouar AlDahoul, Yasir Zaki

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-13

**备注**: 5 pages, 2 figures

---

## 💡 一句话要点

**评估大型语言模型在阿拉伯医疗任务中的理解与推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `阿拉伯医疗NLP` `基准测试` `多项选择题` `开放式问题` `语义对齐` `医疗智能问答`

## 📋 核心要点

1. 现有大型语言模型在阿拉伯医疗NLP领域的有效性研究较少，缺乏系统评估。
2. 本研究通过基准测试评估多种LLMs在阿拉伯医疗任务中的表现，提出了基于多数投票的解决方案。
3. 实验结果显示，提出的方法在多项选择题任务中表现优异，并在开放式问题中实现了高语义对齐度。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在阿拉伯自然语言处理（NLP）应用中展现了显著的能力。然而，它们在阿拉伯医疗NLP领域的有效性尚未得到充分研究。本研究评估了当前最先进的LLMs在阿拉伯医疗任务中的知识表达能力，基于AraHealthQA挑战中的医疗数据集进行基准测试。研究结果显示，LLMs在多项选择题和开放式问题的回答准确性上存在显著差异，提出的多数投票解决方案在多项选择题任务中达到了77%的准确率，并在Arahealthqa 2025挑战中获得第一名。对于开放式问题，多个LLMs在语义对齐方面表现出色，最高BERTScore达到86.44%。

## 🔬 方法详解

**问题定义**：本研究旨在评估大型语言模型在阿拉伯医疗NLP任务中的理解与推理能力，现有方法在准确性和语义对齐方面存在不足。

**核心思路**：通过基准测试多种LLMs，特别是采用多数投票机制来提高多项选择题的回答准确性，旨在充分挖掘模型的潜力。

**技术框架**：整体架构包括数据集准备、模型选择、评估指标设定及结果分析，主要模块包括多项选择题和开放式问题的处理。

**关键创新**：提出的多数投票方案结合了三种基础模型（Gemini Flash 2.5、Gemini Pro 2.5和GPT o3），在多项选择题任务中显著提升了准确率，体现了模型组合的优势。

**关键设计**：在实验中，设置了多项选择题和开放式问题的评估标准，采用BERTScore作为语义对齐的衡量指标，确保结果的科学性和可靠性。

## 📊 实验亮点

实验结果显示，提出的多数投票方案在多项选择题任务中达到了77%的准确率，位列Arahealthqa 2025挑战第一名。同时，在开放式问题任务中，多个LLMs的最高BERTScore达到了86.44%，展现了良好的语义对齐能力。

## 🎯 应用场景

该研究的成果可广泛应用于阿拉伯地区的医疗信息系统、智能问答系统以及医疗教育等领域，提升医疗服务的智能化水平。未来，随着技术的进步，LLMs在医疗领域的应用将更加深入，推动个性化医疗和智能诊断的发展。

## 📄 摘要（原文）

> Recent progress in large language models (LLMs) has showcased impressive proficiency in numerous Arabic natural language processing (NLP) applications. Nevertheless, their effectiveness in Arabic medical NLP domains has received limited investigation. This research examines the degree to which state-of-the-art LLMs demonstrate and articulate healthcare knowledge in Arabic, assessing their capabilities across a varied array of Arabic medical tasks. We benchmark several LLMs using a medical dataset proposed in the Arabic NLP AraHealthQA challenge in MedArabiQ2025 track. Various base LLMs were assessed on their ability to accurately provide correct answers from existing choices in multiple-choice questions (MCQs) and fill-in-the-blank scenarios. Additionally, we evaluated the capacity of LLMs in answering open-ended questions aligned with expert answers. Our results reveal significant variations in correct answer prediction accuracy and low variations in semantic alignment of generated answers, highlighting both the potential and limitations of current LLMs in Arabic clinical contexts. Our analysis shows that for MCQs task, the proposed majority voting solution, leveraging three base models (Gemini Flash 2.5, Gemini Pro 2.5, and GPT o3), outperforms others, achieving up to 77% accuracy and securing first place overall in the Arahealthqa 2025 shared task-track 2 (sub-task 1) challenge. Moreover, for the open-ended questions task, several LLMs were able to demonstrate excellent performance in terms of semantic alignment and achieve a maximum BERTScore of 86.44%.

