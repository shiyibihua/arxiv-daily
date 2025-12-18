---
layout: default
title: Evaluating Open-Source Large Language Models for Technical Telecom Question Answering
---

# Evaluating Open-Source Large Language Models for Technical Telecom Question Answering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21949" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21949v1</a>
  <a href="https://arxiv.org/pdf/2509.21949.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21949v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21949v1', 'Evaluating Open-Source Large Language Models for Technical Telecom Question Answering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arina Caraus, Alessio Buscemi, Sumit Kumar, Ion Turcanu

**分类**: cs.NI, cs.CL

**发布日期**: 2025-09-26

**备注**: Accepted at the IEEE GLOBECOM Workshops 2025: "Large AI Model over Future Wireless Networks"

---

## 💡 一句话要点

**评估开源大语言模型在电信技术问答中的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `电信技术` `问答系统` `性能评估` `开源模型`

## 📋 核心要点

1. 现有大型语言模型在电信等技术领域的性能评估不足，缺乏针对性基准。
2. 论文构建电信领域问答基准，评估Gemma和DeepSeek两个开源LLM的性能。
3. 实验结果表明，Gemma在语义保真度上更优，DeepSeek在词汇一致性上略胜一筹，但都存在局限性。

## 📝 摘要（中文）

大型语言模型（LLM）在各个领域都展现出了卓越的能力。然而，它们在电信等技术领域的性能仍有待探索。本文评估了两个开源LLM，Gemma 3 27B和DeepSeek R1 32B，在基于高级无线通信材料的事实性和推理性问题上的表现。我们构建了一个包含105个问答对的基准，并使用词汇指标、语义相似性和LLM-as-a-judge评分来评估性能。我们还通过源属性和分数方差分析了一致性、判断可靠性和幻觉。结果表明，Gemma在语义保真度和LLM评分的正确性方面表现出色，而DeepSeek在词汇一致性方面略高。其他发现强调了当前电信应用的局限性，以及对领域自适应模型的需求，以支持工程领域中值得信赖的人工智能（AI）助手。

## 🔬 方法详解

**问题定义**：论文旨在评估通用大型语言模型在电信技术问答任务中的表现。现有方法缺乏对LLM在特定技术领域（如电信）的深入评估，并且缺乏专门的基准数据集来衡量其性能。现有通用LLM可能无法充分理解电信领域的专业知识，导致回答不准确或产生幻觉。

**核心思路**：论文的核心思路是构建一个专门针对电信领域的问答基准，并使用多种评估指标（包括词汇指标、语义相似性和LLM-as-a-judge评分）来全面评估LLM的性能。通过分析LLM在不同指标上的表现，可以深入了解其在电信领域的优势和局限性。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 构建电信领域问答基准数据集，包含105个问答对，涵盖事实性和推理性问题。2) 选择两个开源LLM（Gemma 3 27B和DeepSeek R1 32B）进行评估。3) 使用词汇指标（如BLEU）、语义相似性指标（如BERTScore）和LLM-as-a-judge评分来评估LLM的性能。4) 分析LLM的一致性、判断可靠性和幻觉，通过源属性和分数方差进行评估。

**关键创新**：论文的关键创新在于构建了一个专门针对电信领域的问答基准数据集，这填补了现有研究的空白。此外，论文还采用了多种评估指标，包括LLM-as-a-judge评分，从而更全面地评估了LLM的性能。与现有方法相比，该研究更注重对LLM在特定技术领域的深入评估。

**关键设计**：基准数据集包含105个问答对，涵盖高级无线通信材料。评估指标包括：BLEU (Bilingual Evaluation Understudy) 用于评估词汇一致性，BERTScore 用于评估语义相似性，以及使用 GPT-4 作为裁判的 LLM-as-a-judge 评分来评估答案的正确性。此外，还通过分析答案的来源和分数方差来评估 LLM 的幻觉和一致性。

## 📊 实验亮点

实验结果表明，Gemma在语义保真度方面表现出色，而DeepSeek在词汇一致性方面略胜一筹。具体来说，Gemma在LLM-as-a-judge评分中表现更好，表明其生成的答案更符合人类专家的判断。然而，两个模型都存在幻觉和不一致性问题，表明需要进一步的领域自适应训练才能满足电信领域的需求。

## 🎯 应用场景

该研究成果可应用于开发电信领域的智能问答系统、技术支持助手和教育工具。通过领域自适应训练，可以提升LLM在电信领域的专业知识和推理能力，从而为工程师和技术人员提供更准确、可靠的信息支持，并促进电信技术的创新和发展。未来的研究可以探索如何利用这些模型来自动化电信网络的设计、优化和故障排除。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown remarkable capabilities across various fields. However, their performance in technical domains such as telecommunications remains underexplored. This paper evaluates two open-source LLMs, Gemma 3 27B and DeepSeek R1 32B, on factual and reasoning-based questions derived from advanced wireless communications material. We construct a benchmark of 105 question-answer pairs and assess performance using lexical metrics, semantic similarity, and LLM-as-a-judge scoring. We also analyze consistency, judgment reliability, and hallucination through source attribution and score variance. Results show that Gemma excels in semantic fidelity and LLM-rated correctness, while DeepSeek demonstrates slightly higher lexical consistency. Additional findings highlight current limitations in telecom applications and the need for domain-adapted models to support trustworthy Artificial Intelligence (AI) assistants in engineering.

