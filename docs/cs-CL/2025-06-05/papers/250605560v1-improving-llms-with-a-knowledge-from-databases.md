---
layout: default
title: Improving LLMs with a knowledge from databases
---

# Improving LLMs with a knowledge from databases

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05560" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05560v1</a>
  <a href="https://arxiv.org/pdf/2506.05560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05560v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05560v1', 'Improving LLMs with a knowledge from databases')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Petr Máša

**分类**: cs.CL

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出基于增强关联规则的LLM知识改进方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `增强关联规则` `检索增强生成` `数据集` `可解释机器学习` `智能问答` `安全性`

## 📋 核心要点

1. 现有的LLM方法在处理结构化数据时存在安全性和控制不足的问题。
2. 论文提出通过增强关联规则生成规则集，并将其转化为文本形式以改进LLM的回答能力。
3. 实验结果表明，该方法在回答基于数据集的问题时，相较于ChatGPT有显著提升。

## 📝 摘要（中文）

大型语言模型（LLMs）正在迅速取得显著进展，许多先进技术如检索增强生成（RAG）和工具被广泛接受。本文探讨了一种新方法，通过可解释的机器学习方法——增强关联规则，基于数据集/数据库改进LLM的回答。该方法生成基于定义知识模式的规则集，并通过规则到文本转换器将规则转换为文本形式，作为RAG的一部分纳入LLM中。与ChatGPT的对比实验显示，该方法在基于数据集回答问题时显著提升了效果，未来可通过引入其他模式和规则挖掘等进一步改进。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型在处理结构化数据时的回答准确性和安全性问题。现有方法在生成命令时缺乏控制，可能导致安全隐患。

**核心思路**：提出一种基于增强关联规则的方法，通过生成规则集并将其转化为文本形式，增强LLM的回答能力，尤其是在处理结构化数据时。

**技术框架**：整体流程包括定义知识模式、生成规则集、使用规则到文本转换器将规则转化为文本，最后将结果作为RAG纳入LLM中。主要模块包括知识模式定义、规则生成和文本转换。

**关键创新**：最重要的创新在于将增强关联规则与RAG技术结合，形成了一种新的知识增强方法，显著提升了LLM在特定任务上的表现。

**关键设计**：在规则生成过程中，设置了生成规则的数量和质量参数，确保生成的规则具有较高的相关性和可解释性。

## 📊 实验亮点

实验结果显示，所提出的方法在回答基于数据集的问题时，相较于ChatGPT有显著提升，具体提升幅度未知。该方法的有效性为未来的研究提供了新的方向。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、数据分析和决策支持等。通过将增强关联规则应用于LLM，可以提高模型在处理结构化数据时的准确性和安全性，未来可能在多个行业中产生深远影响。

## 📄 摘要（原文）

> Large language models (LLMs) are achieving significant progress almost every moment now. Many advanced techniques have been introduced and widely accepted, like retrieval-augmentation generation (RAG), agents, and tools. Tools can query the database to answer questions from structured data files or perform groupings or other statistics. This unlocks huge opportunities, such as it can answer any question, but also poses threats, such as safety, because there is no control over the commands that are created. We would like to discuss whether we can create a new method that improves answers based on dataset/database via some interpretable ML methods, namely enhanced association rules. The advantage would be if the method can be also used in some safe technique like RAG. Association rules have a sound history. Since the introduction of CN2 and aproiri, many enhancements have been made. In parallel, enhanced association rules have been introduced and evolved over the last 40 years. The general problem is typically that there are too many rules. There are some techniques for handling it, but when LLM emerged, it turned out to be the best use case for the RAG technique for LLMs. We proposed a method that generates a ruleset based on defined knowledge patterns, then converts rules into text form via a rule-to-text converter, and includes the result as an RAG into LLM. We compared this method with ChatGPT (even with using agents) and we have discovered a significant improvement in answering questions based on the dataset. We have also tried several strategies how much rules to generate. We found this improvement interesting. Moreover, it can also be improved in many ways as future work, like incorporating other patterns, the use of rule mining as an agent, and many others.

