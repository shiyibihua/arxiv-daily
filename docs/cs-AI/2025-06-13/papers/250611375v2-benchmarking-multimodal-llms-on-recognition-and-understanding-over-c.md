---
layout: default
title: Benchmarking Multimodal LLMs on Recognition and Understanding over Chemical Tables
---

# Benchmarking Multimodal LLMs on Recognition and Understanding over Chemical Tables

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11375" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11375v2</a>
  <a href="https://arxiv.org/pdf/2506.11375.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11375v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11375v2', 'Benchmarking Multimodal LLMs on Recognition and Understanding over Chemical Tables')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yitong Zhou, Mingyue Cheng, Qingyang Mao, Yucong Luo, Qi Liu, Yupeng Li, Xiaohan Zhang, Deguang Liu, Xin Li, Enhong Chen

**分类**: cs.AI, cs.CL

**发布日期**: 2025-06-13 (更新: 2025-12-11)

---

## 💡 一句话要点

**提出ChemTable基准以解决化学表格理解与识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `化学表格` `知识表示` `科学智能` `表格理解` `评估基准` `领域特定语义` `推理能力`

## 📋 核心要点

1. 现有评估基准主要集中在一般领域，未能反映科学研究中化学表格的结构复杂性和领域特定语义。
2. 提出ChemTable基准，基于真实文献构建，包含专家注释的布局和逻辑结构，支持表格识别与理解任务。
3. 评估结果显示，主流多模态模型在布局解析上表现良好，但在处理化学表格的关键元素时仍存在显著不足。

## 📝 摘要（中文）

随着多模态大语言模型在科学智能中的广泛应用，迫切需要更具挑战性的评估基准来评估其理解复杂科学数据的能力。科学表格作为知识表示的核心载体，结合了文本、符号和图形，形成了典型的多模态推理场景。然而，现有基准主要集中在一般领域，未能反映科学研究中固有的结构复杂性和领域特定语义。化学表格尤其具有代表性：它们将反应物、条件和产量等结构化变量与分子结构和化学公式等视觉符号交织在一起，给模型在跨模态对齐和语义解析上带来了重大挑战。为此，我们提出ChemTable——一个基于真实文献构建的大规模化学表格基准，包含专家注释的单元格布局、逻辑结构和领域特定标签。该基准支持两个核心任务：表格识别（结构和内容提取）和表格理解（描述性和基于推理的问题回答）。在ChemTable上的评估显示，尽管主流多模态模型在布局解析上表现良好，但在处理分子结构和符号约定等关键元素时仍面临显著限制。封闭源模型整体表现领先，但仍未达到人类水平的表现。这项工作为评估科学多模态理解提供了现实的测试平台，揭示了领域特定推理的当前瓶颈，推动了科学研究智能系统的发展。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多模态大语言模型在理解和识别化学表格时的不足，尤其是在处理复杂的结构化变量和视觉符号时的挑战。现有方法未能有效应对化学表格的领域特定语义和结构复杂性。

**核心思路**：论文提出ChemTable基准，通过构建一个包含真实文献的化学表格数据集，提供更具挑战性的评估任务，以促进多模态模型在科学数据理解上的能力提升。

**技术框架**：ChemTable的整体架构包括数据收集、专家注释、任务设计和评估四个主要模块。数据收集阶段从真实文献中提取化学表格，专家注释阶段对表格进行结构和内容的标注，任务设计阶段定义表格识别和理解的具体任务，评估阶段则对模型性能进行测试。

**关键创新**：ChemTable的最大创新在于其针对化学表格的专门设计，结合了结构化变量与视觉符号的复杂性，提供了一个真实且具有挑战性的评估平台，与现有的通用基准相比，能够更好地反映领域特定的推理能力。

**关键设计**：在数据集构建中，设置了详细的单元格布局和逻辑结构，采用了领域特定标签，确保模型在评估时能够准确理解和解析化学表格中的信息。

## 📊 实验亮点

在ChemTable上的评估结果显示，主流多模态模型在布局解析任务中表现良好，但在处理分子结构和符号约定等关键元素时仍存在显著不足。封闭源模型的整体表现领先，但仍未达到人类水平的表现，揭示了当前领域特定推理的瓶颈。

## 🎯 应用场景

该研究的潜在应用领域包括化学信息提取、科学文献分析和智能问答系统等。通过提供一个专门的评估基准，ChemTable能够推动多模态大语言模型在科学研究中的应用，提升其在复杂数据理解方面的能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> With the widespread application of multimodal large language models in scientific intelligence, there is an urgent need for more challenging evaluation benchmarks to assess their ability to understand complex scientific data. Scientific tables, as core carriers of knowledge representation, combine text, symbols, and graphics, forming a typical multimodal reasoning scenario. However, existing benchmarks are mostly focused on general domains, failing to reflect the unique structural complexity and domain-specific semantics inherent in scientific research. Chemical tables are particularly representative: they intertwine structured variables such as reagents, conditions, and yields with visual symbols like molecular structures and chemical formulas, posing significant challenges to models in cross-modal alignment and semantic parsing. To address this, we propose ChemTable-a large scale benchmark of chemical tables constructed from real-world literature, containing expert-annotated cell layouts, logical structures, and domain-specific labels. It supports two core tasks: (1) table recognition (structure and content extraction); and (2) table understanding (descriptive and reasoning-based question answering). Evaluation on ChemTable shows that while mainstream multimodal models perform reasonably well in layout parsing, they still face significant limitations when handling critical elements such as molecular structures and symbolic conventions. Closed-source models lead overall but still fall short of human-level performance. This work provides a realistic testing platform for evaluating scientific multimodal understanding, revealing the current bottlenecks in domain-specific reasoning and advancing the development of intelligent systems for scientific research.

