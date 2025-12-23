---
layout: default
title: A Dataset and Preliminary Study of Using GPT-5 for Code-change Impact Analysis
---

# A Dataset and Preliminary Study of Using GPT-5 for Code-change Impact Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19481" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19481v1</a>
  <a href="https://arxiv.org/pdf/2512.19481.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19481v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19481v1', 'A Dataset and Preliminary Study of Using GPT-5 for Code-change Impact Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Katharina Stengg, Christian Macho, Martin Pinzger

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-22

**备注**: 6 pages

---

## 💡 一句话要点

**构建代码变更影响分析数据集，初步评估GPT-5在代码影响预测中的能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码变更影响分析` `大型语言模型` `GPT-5` `软件开发` `数据集构建`

## 📋 核心要点

1. 手动分析代码变更的影响耗时，现有数据集缺乏种子变更和受影响代码实体的关键信息。
2. 论文旨在评估GPT-5和GPT-5-mini在预测代码变更影响方面的能力，并构建包含种子变更信息的数据集。
3. 实验结果表明，GPT-5和GPT-5-mini在代码变更影响预测方面表现不佳，但提供diff hunk能略微提升性能。

## 📝 摘要（中文）

理解源代码变更及其对其他代码实体的影响是软件开发中的一项关键技能。然而，代码变更及其影响的分析通常是手动执行的，因此非常耗时。人工智能，特别是大型语言模型（LLM）的最新进展，显示出帮助开发人员完成各种代码分析任务的潜力。然而，这种潜力在理解代码变更及其影响方面的利用程度尚未得到充分探索。为了弥补这一差距，我们研究了GPT-5和GPT-5-mini预测给定源代码变更所影响的代码实体的能力。我们构建了一个数据集，其中包含每个提交的种子变更、变更对和变更类型的信息。现有数据集缺乏关于种子变更和受影响代码实体的关键信息。我们的实验在两种配置中评估LLM：（1）种子变更信息和父提交树；（2）种子变更信息、父提交树和每个种子变更的diff hunk。我们发现，两种LLM在这两个实验中的表现都很差，但GPT-5优于GPT-5-mini。此外，提供diff hunk有助于两个模型略微提高其性能。

## 🔬 方法详解

**问题定义**：论文旨在解决软件开发中代码变更影响分析的自动化问题。现有方法主要依赖人工分析，效率低下且容易出错。现有数据集缺乏关于种子变更和受影响代码实体的详细信息，阻碍了基于机器学习的自动化分析方法的发展。

**核心思路**：论文的核心思路是利用大型语言模型（LLM），特别是GPT-5和GPT-5-mini，来预测给定代码变更所影响的代码实体。通过构建包含种子变更、变更对和变更类型等信息的数据集，并结合父提交树和diff hunk等上下文信息，来训练和评估LLM在代码变更影响分析任务中的性能。

**技术框架**：论文的技术框架主要包括以下几个部分：1) 构建代码变更影响分析数据集，该数据集包含种子变更、变更对、变更类型、父提交树和diff hunk等信息。2) 使用GPT-5和GPT-5-mini作为模型，在构建的数据集上进行训练和评估。3) 设计两种实验配置：第一种配置仅使用种子变更信息和父提交树，第二种配置则额外使用diff hunk信息。4) 评估LLM在不同配置下的性能，并分析结果。

**关键创新**：论文的关键创新在于：1) 构建了一个新的代码变更影响分析数据集，该数据集包含更全面的信息，例如种子变更和受影响代码实体。2) 首次尝试使用GPT-5和GPT-5-mini等大型语言模型来解决代码变更影响分析问题。3) 通过实验评估了LLM在不同配置下的性能，并分析了diff hunk信息对模型性能的影响。

**关键设计**：论文的关键设计包括：1) 数据集的构建方式，如何选择和标注种子变更、变更对和变更类型等信息。2) 实验配置的设计，如何选择合适的输入特征（例如父提交树和diff hunk）以及如何评估模型的性能。3) 模型训练和评估的细节，例如如何选择合适的损失函数和优化器，以及如何避免过拟合等问题。具体参数设置和网络结构细节未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19481v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19481v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，GPT-5和GPT-5-mini在代码变更影响预测任务中表现不佳，这表明现有LLM在理解代码变更的语义和上下文方面仍存在挑战。尽管如此，GPT-5的性能优于GPT-5-mini，并且提供diff hunk信息可以略微提高模型的性能。这些发现为未来研究如何利用LLM进行代码变更影响分析提供了有价值的参考。

## 🎯 应用场景

该研究成果可应用于软件开发过程中的代码变更管理、缺陷预测和代码审查等领域。通过自动化代码变更影响分析，可以帮助开发人员更快速、准确地理解代码变更的影响范围，从而减少错误、提高开发效率和软件质量。未来，该研究可以扩展到更复杂的代码变更场景，并与其他代码分析技术相结合，构建更智能化的软件开发工具。

## 📄 摘要（原文）

> Understanding source code changes and their impact on other code entities is a crucial skill in software development. However, the analysis of code changes and their impact is often performed manually and therefore is time-consuming. Recent advancements in AI, and in particular large language models (LLMs) show promises to help developers in various code analysis tasks. However, the extent to which this potential can be utilized for understanding code changes and their impact is underexplored. To address this gap, we study the capabilities of GPT-5 and GPT-5-mini to predict the code entities impacted by given source code changes. We construct a dataset containing information about seed-changes, change pairs, and change types for each commit. Existing datasets lack crucial information about seed changes and impacted code entities. Our experiments evaluate the LLMs in two configurations: (1) seed-change information and the parent commit tree and (2) seed-change information, the parent commit tree, and the diff hunk of each seed change. We found that both LLMs perform poorly in the two experiments, whereas GPT-5 outperforms GPT-5-mini. Furthermore, the provision of the diff hunks helps both models to slightly improve their performance.

