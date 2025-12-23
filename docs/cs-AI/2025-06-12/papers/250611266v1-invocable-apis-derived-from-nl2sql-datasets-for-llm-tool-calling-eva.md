---
layout: default
title: Invocable APIs derived from NL2SQL datasets for LLM Tool-Calling Evaluation
---

# Invocable APIs derived from NL2SQL datasets for LLM Tool-Calling Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11266" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11266v1</a>
  <a href="https://arxiv.org/pdf/2506.11266.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11266v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11266v1', 'Invocable APIs derived from NL2SQL datasets for LLM Tool-Calling Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Benjamin Elder, Anupama Murthi, Jungkoo Kang, Ankita Rajaram Naik, Kiran Kate, Kinjal Basu, Danish Contractor

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-12

**备注**: 10+32 pages, 5 figures

---

## 💡 一句话要点

**提出NL2API数据集生成方法以评估LLM工具调用能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `API调用` `NL2SQL` `数据生成` `工具选择` `任务完成率` `企业应用` `智能系统`

## 📋 核心要点

1. 现有的LLM在与复杂API集合交互时面临工具选择和任务完成率低的问题，尤其是在企业环境中。
2. 本文提出了一种基于NL2SQL数据集生成NL2API数据集的方法，通过SQL查询语法构建API调用序列，增强LLM的工具调用能力。
3. 实验结果显示，10种公共LLM的任务完成率在7%到47%之间，使用ReACT代理后略有提升，但仍低于有效工具调用所需的水平。

## 📝 摘要（中文）

大型语言模型（LLMs）常被部署为智能系统，能够与实时环境中的工具交互以完成任务。然而，在企业环境中，这些系统需要与复杂的API集合进行交互。本文探讨如何利用现有的NL2SQL数据集自动生成NL2API数据集，提出了一种新颖的数据生成管道，通过SQL查询的语法构建功能等效的API调用序列。我们应用该管道于BIRD-SQL数据集，创建了超过2500个可调用的API，并将自然语言查询与真实API序列配对。研究发现，当前的LLM在工具选择上表现不佳，任务完成率低，表明现有工具调用LLM有显著改进空间。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在与复杂API交互时的工具选择和任务完成率低的问题。现有方法在处理API集合时表现不佳，尤其是在企业应用场景中。

**核心思路**：论文提出了一种新颖的数据生成管道，利用现有的NL2SQL数据集，通过SQL查询的语法构建功能等效的API调用序列，从而生成NL2API数据集。

**技术框架**：整体架构包括数据生成管道、API调用序列构建和自然语言查询与API序列的配对。主要模块包括数据提取、API生成和性能评估。

**关键创新**：最重要的技术创新在于利用SQL查询的语法结构自动生成API调用序列，这一方法与传统的手动构建API集合的方式有本质区别。

**关键设计**：在生成API时，考虑了API的功能性和语义一致性，设置了合适的参数以确保生成的API能够有效响应自然语言查询，同时进行了详细的消融实验以评估工具数量和名称模糊化对性能的影响。

## 📊 实验亮点

实验结果表明，10种公共LLM在任务完成率上表现不佳，最低为7%，最高为47%。使用ReACT代理后，任务完成率略微提高至50%。这些结果显示当前工具调用LLM的性能远低于实际应用所需水平，表明有显著改进空间。

## 🎯 应用场景

该研究的潜在应用领域包括企业级智能助手、数据查询系统和自动化工具调用等。通过提高LLM在API调用方面的能力，可以增强其在实际应用中的有效性和可靠性，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Large language models (LLMs) are routinely deployed as agentic systems, with access to tools that interact with live environments to accomplish tasks. In enterprise deployments these systems need to interact with API collections that can be extremely large and complex, often backed by databases. In order to create datasets with such characteristics, we explore how existing NL2SQL (Natural Language to SQL query) datasets can be used to automatically create NL2API datasets. Specifically, this work describes a novel data generation pipeline that exploits the syntax of SQL queries to construct a functionally equivalent sequence of API calls. We apply this pipeline to one of the largest NL2SQL datasets, BIRD-SQL to create a collection of over 2500 APIs that can be served as invocable tools or REST-endpoints. We pair natural language queries from BIRD-SQL to ground-truth API sequences based on this API pool. We use this collection to study the performance of 10 public LLMs and find that all models struggle to determine the right set of tools (consisting of tasks of intent detection, sequencing with nested function calls, and slot-filling). We find that models have extremely low task completion rates (7-47 percent - depending on the dataset) which marginally improves to 50 percent when models are employed as ReACT agents that interact with the live API environment. The best task completion rates are far below what may be required for effective general-use tool-calling agents, suggesting substantial scope for improvement in current state-of-the-art tool-calling LLMs. We also conduct detailed ablation studies, such as assessing the impact of the number of tools available as well as the impact of tool and slot-name obfuscation. We compare the performance of models on the original SQL generation tasks and find that current models are sometimes able to exploit SQL better than APIs.

