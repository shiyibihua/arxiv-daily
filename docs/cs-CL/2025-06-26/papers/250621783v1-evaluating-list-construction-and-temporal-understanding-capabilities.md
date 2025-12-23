---
layout: default
title: Evaluating List Construction and Temporal Understanding capabilities of Large Language Models
---

# Evaluating List Construction and Temporal Understanding capabilities of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21783" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21783v1</a>
  <a href="https://arxiv.org/pdf/2506.21783.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21783v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21783v1', 'Evaluating List Construction and Temporal Understanding capabilities of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexandru Dumitru, V Venktesh, Adam Jatowt, Avishek Anand

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-26

**备注**: Accepted at ICTIR 2025 co-located with SIGIR 2025, 11 pages

**🔗 代码/项目**: [GITHUB](https://github.com/elixir-research-group/TLQA)

---

## 💡 一句话要点

**提出TLQA基准以解决大语言模型的时间理解与列表构建问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `时间理解` `列表构建` `问答系统` `自然语言处理` `基准评估`

## 📋 核心要点

1. 现有大型语言模型在时间理解和列表构建任务中存在显著不足，尤其是在多实体关联和时间区间准确性方面。
2. 本文提出了时间参考列表问答（TLQA）基准，要求模型同时进行列表构建和时间理解，以填补现有研究的空白。
3. 实验结果显示，当前模型在闭卷设置下无法提供完整答案，并在开放域设置中需要改进检索能力，为未来研究指明了方向。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言任务中取得了显著进展，但在涉及多个实体的时间理解任务中仍存在幻觉和错误。这些模型在关联实体与准确时间区间、生成完整的实体列表以及推理特定时间范围内的事件方面表现不佳。现有研究未充分评估模型在列表答案构建中进行隐式和显式时间理解的能力。为此，本文提出了时间参考列表问答（TLQA）基准，要求结构化的列表格式答案与相应的时间段对齐。我们的研究揭示了当前模型在闭卷设置下无法提供完整答案和时间对齐事实的显著不足，并指出了开放域设置中检索能力的改进需求。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在时间理解和列表构建任务中的不足，特别是在多实体和时间区间关联方面的挑战。现有方法未能充分评估模型在这些任务中的表现。

**核心思路**：提出TLQA基准，要求模型生成结构化的列表答案，并与相应的时间段对齐，从而同时考察模型的列表构建和时间理解能力。这样的设计旨在填补现有基准的空白，推动相关研究的进展。

**技术框架**：TLQA基准包括多个模块，首先是问题生成模块，生成需要回答的时间相关问题；其次是答案生成模块，要求模型输出结构化的列表答案；最后是评估模块，评估模型在时间理解和列表构建方面的表现。

**关键创新**：TLQA基准的提出是本文的主要创新点，它结合了时间理解和列表构建的双重要求，填补了现有研究的空白，推动了对大型语言模型能力的深入评估。

**关键设计**：在实验中，采用了多种评估指标来衡量模型的表现，包括答案的完整性和时间对齐的准确性。同时，模型在闭卷和开放域设置下的表现也进行了对比分析，以揭示其在不同场景下的能力差异。

## 📊 实验亮点

实验结果表明，当前的语言模型在TLQA基准下表现不佳，特别是在闭卷设置中，模型无法提供完整的答案，且时间对齐的准确性显著不足。这些发现为未来的研究提供了明确的改进方向，强调了在开放域设置中提升检索能力的必要性。

## 🎯 应用场景

该研究的TLQA基准可广泛应用于自然语言处理领域，特别是在需要时间理解和列表构建的任务中，如信息检索、问答系统和知识图谱构建等。通过提升模型在这些任务中的表现，能够为实际应用提供更准确和结构化的信息，推动智能助手和自动化系统的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated immense advances in a wide range of natural language tasks. However, these models are susceptible to hallucinations and errors on particularly temporal understanding tasks involving multiple entities in answers. In such tasks, they fail to associate entities with accurate time intervals, generate a complete list of entities in answers or reason about events associated with specific temporal bounds. Existing works do not extensively evaluate the abilities of the model to perform implicit and explicit temporal understanding in a list answer construction setup. To bridge this gap, we propose the Time referenced List based Question Answering or TLQA benchmark that requires structured answers in list format aligned with corresponding time periods. Our TLQA benchmark, requires both list construction and temporal understanding simultaneously, which to the best of our knowledge has not been explored in prior benchmarks. We investigate the temporal understanding and list construction capabilities of state-of-the-art generative models on TLQA in closed-book and open-domain settings. Our findings reveal significant shortcomings in current models, particularly their inability to provide complete answers and temporally align facts in a closed-book setup and the need to improve retrieval in open-domain setup, providing clear future directions for research on TLQA. The benchmark and code at https://github.com/elixir-research-group/TLQA.

