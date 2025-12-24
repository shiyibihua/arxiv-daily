---
layout: default
title: Leveraging Large Language Models for Rare Disease Named Entity Recognition
---

# Leveraging Large Language Models for Rare Disease Named Entity Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09323" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09323v1</a>
  <a href="https://arxiv.org/pdf/2508.09323.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09323v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09323v1', 'Leveraging Large Language Models for Rare Disease Named Entity Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nan Miles Xi, Yu Deng, Lin Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**利用大型语言模型解决稀有疾病命名实体识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `命名实体识别` `稀有疾病` `大型语言模型` `提示优化` `生物医学` `低资源学习` `机器学习`

## 📋 核心要点

1. 稀有疾病NER面临标注数据稀缺、语义模糊和长尾分布等挑战，现有方法难以有效应对。
2. 本研究提出了一种结构化提示框架，结合多种提示策略和领域知识，提升NER性能。
3. 实验结果显示，GPT-4o在RareDis语料库上超越BioClinicalBERT，任务级微调实现了SOTA效果。

## 📝 摘要（中文）

稀有疾病领域的命名实体识别（NER）面临着有限标注数据、实体类型之间的语义模糊和长尾分布等独特挑战。本研究评估了GPT-4o在低资源环境下进行稀有疾病NER的能力，采用了零-shot提示、少量示例学习、检索增强生成（RAG）和任务级微调等多种基于提示的策略。我们设计了一个结构化的提示框架，编码了领域特定知识和四种实体类型的消歧规则。实验结果表明，GPT-4o在RareDis语料库上表现出竞争力或优越的性能，任务级微调实现了新的最先进（SOTA）结果。

## 🔬 方法详解

**问题定义**：本研究旨在解决稀有疾病领域命名实体识别中的数据稀缺和语义模糊问题。现有方法在处理有限标注数据时表现不佳，难以准确识别不同类型的实体。

**核心思路**：论文提出了一种基于大型语言模型的提示优化策略，通过结构化提示框架引入领域知识和消歧规则，以提高NER的准确性和效率。

**技术框架**：整体架构包括多个模块：首先是提示生成模块，利用零-shot和few-shot策略；其次是检索增强生成（RAG）模块，最后是任务级微调模块，针对特定任务进行优化。

**关键创新**：最重要的创新在于设计了结构化提示框架和语义引导的few-shot示例选择方法，显著提升了模型在低资源环境下的表现，与传统监督模型相比具有更好的可扩展性。

**关键设计**：在参数设置上，采用了适应性学习率和特定的损失函数，网络结构上结合了Transformer架构，确保了模型在处理复杂语义时的灵活性和准确性。

## 📊 实验亮点

实验结果表明，GPT-4o在RareDis语料库上的表现超越了BioClinicalBERT，任务级微调实现了新的最先进（SOTA）结果。此外，少量示例提示策略在低标记预算下提供了高回报，而RAG的边际收益相对较小。

## 🎯 应用场景

该研究的潜在应用领域包括医疗文本分析、电子健康记录中的信息提取以及稀有疾病的研究与诊断。通过提供高效的NER工具，能够帮助研究人员和临床医生更好地识别和理解稀有疾病相关信息，推动相关领域的发展。

## 📄 摘要（原文）

> Named Entity Recognition (NER) in the rare disease domain poses unique challenges due to limited labeled data, semantic ambiguity between entity types, and long-tail distributions. In this study, we evaluate the capabilities of GPT-4o for rare disease NER under low-resource settings, using a range of prompt-based strategies including zero-shot prompting, few-shot in-context learning, retrieval-augmented generation (RAG), and task-level fine-tuning. We design a structured prompting framework that encodes domain-specific knowledge and disambiguation rules for four entity types. We further introduce two semantically guided few-shot example selection methods to improve in-context performance while reducing labeling effort. Experiments on the RareDis Corpus show that GPT-4o achieves competitive or superior performance compared to BioClinicalBERT, with task-level fine-tuning yielding new state-of-the-art (SOTA) results. Cost-performance analysis reveals that few-shot prompting delivers high returns at low token budgets, while RAG offers marginal additional benefit. An error taxonomy highlights common failure modes such as boundary drift and type confusion, suggesting opportunities for post-processing and hybrid refinement. Our results demonstrate that prompt-optimized LLMs can serve as effective, scalable alternatives to traditional supervised models in biomedical NER, particularly in rare disease applications where annotated data is scarce.

