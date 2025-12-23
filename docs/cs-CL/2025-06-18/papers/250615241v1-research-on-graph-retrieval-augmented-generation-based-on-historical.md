---
layout: default
title: Research on Graph-Retrieval Augmented Generation Based on Historical Text Knowledge Graphs
---

# Research on Graph-Retrieval Augmented Generation Based on Historical Text Knowledge Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15241" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15241v1</a>
  <a href="https://arxiv.org/pdf/2506.15241.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15241v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15241v1', 'Research on Graph-Retrieval Augmented Generation Based on Historical Text Knowledge Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Fan, Zhang Qi, Xing Wenqian, Liu Chang, Liu Liu

**分类**: cs.CL

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出Graph RAG框架以解决历史文本分析中的知识缺口问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `关系提取` `历史文本分析` `生成模型` `低资源解决方案`

## 📋 核心要点

1. 现有的通用大语言模型在历史文本分析中存在领域知识缺口，导致分析效果不佳。
2. 论文提出Graph RAG框架，通过结合思维链提示和自我指令生成，降低人工标注成本并提升知识提取效率。
3. 实验结果显示，领域特定模型在关系提取任务中显著提升性能，尤其是DeepSeek模型在开放域数据集上表现优异。

## 📝 摘要（中文）

本文针对计算人文学科和AIGC技术背景下，通用大语言模型在历史文本分析中的领域知识缺口进行研究。我们提出了Graph RAG框架，结合思维链提示、自我指令生成和过程监督，创建了最小人工标注的《四史》人物关系数据集，支持自动化历史知识提取，降低人工成本。在图增强生成阶段，引入知识图谱与检索增强生成之间的协作机制，提高了通用模型与历史知识的对齐度。实验表明，领域特定模型Xunzi-Qwen1.5-14B在简体中文输入和思维链提示下，在关系提取任务中表现最佳（F1 = 0.68）。集成GraphRAG的DeepSeek模型在开放域C-CLUE关系提取数据集上提升F1值11%（0.08-0.19），超越Xunzi-Qwen1.5-14B（0.12），有效缓解了幻觉现象，提高了可解释性。该框架为经典文本知识提取提供了低资源解决方案，推动了历史知识服务和人文学科研究。

## 🔬 方法详解

**问题定义**：本文旨在解决通用大语言模型在历史文本分析中存在的领域知识缺口问题。现有方法在处理历史文本时，往往缺乏足够的领域知识，导致分析结果不准确，且人工标注成本高。

**核心思路**：论文提出的Graph RAG框架结合了思维链提示、自我指令生成和过程监督，旨在通过最小化人工干预来实现高效的历史知识提取。通过引入知识图谱与检索增强生成的协作机制，提升了模型对历史知识的理解和应用能力。

**技术框架**：该框架主要分为两个阶段：首先是数据集的构建阶段，通过最小人工标注生成《四史》人物关系数据集；其次是图增强生成阶段，利用知识图谱与检索增强生成的协作机制来提升模型的生成能力。

**关键创新**：最重要的技术创新在于Graph RAG框架的提出，它有效结合了多种生成和提示技术，显著提升了模型在历史文本分析中的表现。与现有方法相比，该框架在知识提取的准确性和效率上具有明显优势。

**关键设计**：在模型设计中，采用了链式思维提示和自我指令生成的策略，设置了适当的损失函数以优化模型的生成效果，同时在网络结构上进行了针对性的调整，以适应历史文本的特性。通过这些设计，模型在处理复杂的历史关系时表现出更高的准确性和可解释性。

## 📊 实验亮点

实验结果显示，领域特定模型Xunzi-Qwen1.5-14B在关系提取任务中达到了F1值0.68，而集成GraphRAG的DeepSeek模型在开放域C-CLUE数据集上提升了F1值11%（从0.08提升至0.19），超越了Xunzi-Qwen1.5-14B的F1值0.12，有效缓解了幻觉现象并提高了模型的可解释性。

## 🎯 应用场景

该研究的潜在应用领域包括历史文本分析、文化遗产保护和教育等。通过提供低资源的知识提取解决方案，能够有效支持历史研究者和教育工作者在分析和教学中的需求，推动人文学科的进一步发展。未来，该框架有望在更广泛的领域中应用，提升对历史知识的理解和传播。

## 📄 摘要（原文）

> This article addresses domain knowledge gaps in general large language models for historical text analysis in the context of computational humanities and AIGC technology. We propose the Graph RAG framework, combining chain-of-thought prompting, self-instruction generation, and process supervision to create a The First Four Histories character relationship dataset with minimal manual annotation. This dataset supports automated historical knowledge extraction, reducing labor costs. In the graph-augmented generation phase, we introduce a collaborative mechanism between knowledge graphs and retrieval-augmented generation, improving the alignment of general models with historical knowledge. Experiments show that the domain-specific model Xunzi-Qwen1.5-14B, with Simplified Chinese input and chain-of-thought prompting, achieves optimal performance in relation extraction (F1 = 0.68). The DeepSeek model integrated with GraphRAG improves F1 by 11% (0.08-0.19) on the open-domain C-CLUE relation extraction dataset, surpassing the F1 value of Xunzi-Qwen1.5-14B (0.12), effectively alleviating hallucinations phenomenon, and improving interpretability. This framework offers a low-resource solution for classical text knowledge extraction, advancing historical knowledge services and humanities research.

