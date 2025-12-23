---
layout: default
title: A Large Language Model Based Method for Complex Logical Reasoning over Knowledge Graphs
---

# A Large Language Model Based Method for Complex Logical Reasoning over Knowledge Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19092" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19092v1</a>
  <a href="https://arxiv.org/pdf/2512.19092.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19092v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19092v1', 'A Large Language Model Based Method for Complex Logical Reasoning over Knowledge Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyan Zhang, Chao Wang, Zhuo Chen, Lei Chen, Chiyi Li, Kai Song

**分类**: cs.CL

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出ROG框架，结合知识图谱检索与大语言模型推理，解决复杂逻辑推理难题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱推理` `大语言模型` `逻辑推理` `查询分解` `子图检索`

## 📋 核心要点

1. 现有知识图谱推理方法难以处理复杂查询，尤其是在涉及多算子、深层推理链或异构KG模式时。
2. ROG框架结合查询感知的KG邻域检索与大语言模型推理，将复杂查询分解为子查询，利用LLM进行逐步推理。
3. 实验表明，ROG在标准KG推理基准上优于基于嵌入的基线，尤其在高复杂度查询上提升显著。

## 📝 摘要（中文）

针对现实世界知识图谱（KG）的不完整性和逻辑查询结构的复杂性，论文提出了一种基于大语言模型（LLM）的ROG（Reasoning Over knowledge Graphs with large language models）框架，用于处理一阶逻辑（FOL）查询的KG推理。ROG是一种集成式框架，它结合了查询感知的KG邻域检索与基于LLM的思维链推理。该方法将复杂的FOL查询分解为一系列更简单的子查询，检索紧凑的、与查询相关的子图作为上下文证据，并使用LLM执行逐步逻辑推理，避免了对特定任务的嵌入优化的需求。在标准KG推理基准上的实验表明，ROG在平均倒数排名（MRR）方面始终优于强大的基于嵌入的基线，尤其是在高复杂度查询类型上，获得了显著的提升。这些结果表明，将结构化KG检索与LLM驱动的逻辑推理相结合，为复杂的KG推理任务提供了一种鲁棒而有效的替代方案。

## 🔬 方法详解

**问题定义**：论文旨在解决知识图谱上复杂逻辑推理的问题，特别是处理包含多重逻辑运算符和深层推理链的复杂查询。现有方法，如基于嵌入的方法，在处理简单查询时表现良好，但在面对复杂查询时，由于难以捕捉复杂的逻辑关系和KG的异构性，泛化能力不足。这些方法通常需要针对特定任务进行嵌入优化，缺乏通用性。

**核心思路**：ROG的核心思路是将复杂查询分解为一系列简单的子查询，并利用大语言模型（LLM）的强大推理能力逐步解决这些子查询。通过检索与查询相关的知识图谱子图，为LLM提供上下文信息，引导LLM进行逻辑推理。这种方法避免了直接在整个知识图谱上进行推理，降低了计算复杂度，并利用LLM的知识和推理能力来弥补知识图谱的不完整性。

**技术框架**：ROG框架主要包含以下几个阶段：1) **查询分解**：将复杂的FOL查询分解为一系列更简单的子查询。2) **子图检索**：根据每个子查询，从知识图谱中检索相关的子图作为上下文证据。3) **LLM推理**：利用LLM对检索到的子图进行推理，逐步解决子查询，最终得到最终答案。4) **结果聚合**：将各个子查询的结果进行聚合，得到最终的推理结果。

**关键创新**：ROG的关键创新在于将结构化的知识图谱检索与非结构化的大语言模型推理相结合。与传统的基于嵌入的方法不同，ROG不需要对知识图谱进行嵌入学习，而是直接利用LLM的知识和推理能力。此外，ROG通过查询分解和子图检索，有效地降低了推理的复杂性，提高了推理的效率和准确性。

**关键设计**：ROG的关键设计包括：1) **查询分解策略**：如何将复杂的FOL查询分解为一系列有效的子查询。2) **子图检索算法**：如何高效地检索与查询相关的子图，保证检索到的子图包含足够的上下文信息。3) **LLM提示工程**：如何设计合适的提示（prompt），引导LLM进行逻辑推理，并获得准确的答案。论文中可能使用了特定的提示模板或微调策略来优化LLM的推理性能。具体参数设置和损失函数等细节未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19092v1/fig1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19092v1/fig2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ROG在标准KG推理基准上显著优于基于嵌入的基线方法，尤其是在处理高复杂度查询时，MRR指标提升明显。这表明ROG在处理复杂逻辑推理任务方面具有更强的能力和更好的泛化性能。具体的性能提升幅度未知。

## 🎯 应用场景

该研究成果可应用于智能问答系统、知识图谱补全、推荐系统等领域。通过结合知识图谱的结构化信息和LLM的推理能力，可以构建更智能、更可靠的AI系统。未来，该方法有望在医疗诊断、金融风控等需要复杂推理的领域发挥重要作用。

## 📄 摘要（原文）

> Reasoning over knowledge graphs (KGs) with first-order logic (FOL) queries is challenging due to the inherent incompleteness of real-world KGs and the compositional complexity of logical query structures. Most existing methods rely on embedding entities and relations into continuous geometric spaces and answer queries via differentiable set operations. While effective for simple query patterns, these approaches often struggle to generalize to complex queries involving multiple operators, deeper reasoning chains, or heterogeneous KG schemas. We propose ROG (Reasoning Over knowledge Graphs with large language models), an ensemble-style framework that combines query-aware KG neighborhood retrieval with large language model (LLM)-based chain-of-thought reasoning. ROG decomposes complex FOL queries into sequences of simpler sub-queries, retrieves compact, query-relevant subgraphs as contextual evidence, and performs step-by-step logical inference using an LLM, avoiding the need for task-specific embedding optimization. Experiments on standard KG reasoning benchmarks demonstrate that ROG consistently outperforms strong embedding-based baselines in terms of mean reciprocal rank (MRR), with particularly notable gains on high-complexity query types. These results suggest that integrating structured KG retrieval with LLM-driven logical reasoning offers a robust and effective alternative for complex KG reasoning tasks.

