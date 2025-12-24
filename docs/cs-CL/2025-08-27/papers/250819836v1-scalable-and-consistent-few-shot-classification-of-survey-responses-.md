---
layout: default
title: Scalable and consistent few-shot classification of survey responses using text embeddings
---

# Scalable and consistent few-shot classification of survey responses using text embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19836" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19836v1</a>
  <a href="https://arxiv.org/pdf/2508.19836.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19836v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19836v1', 'Scalable and consistent few-shot classification of survey responses using text embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jonas Timmann Mjaaland, Markus Fleten Kreutzer, Halvor Tyseng, Rebeckah K. Fussell, Gina Passante, N. G. Holmes, Anders Malthe-Sørenssen, Tor Ole B. Odden

**分类**: cs.CL, physics.ed-ph

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出基于文本嵌入的分类框架以解决开放式调查响应分析问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本嵌入` `定性分析` `开放式调查` `机器学习` `自然语言处理` `分类框架` `社会科学` `数据审计`

## 📋 核心要点

1. 现有的定性分析方法耗时且容易产生不一致，限制了开放式调查响应的有效分析。
2. 本文提出了一种基于文本嵌入的分类框架，能够在少量示例的基础上进行有效分类，适应定性研究的工作流程。
3. 实验结果显示，该框架在与人类专家的分析对比中，Cohen's Kappa值达到0.74至0.83，表现出色。

## 📝 摘要（中文）

开放式调查响应的定性分析是社会科学中常用的研究方法，但传统编码方法往往耗时且不一致。现有的自然语言处理解决方案如监督分类器、主题建模技术和生成性大语言模型在定性分析中的适用性有限，因为它们需要大量标注数据，打乱既定的定性工作流程，或产生可变结果。本文提出了一种基于文本嵌入的分类框架，仅需少量示例即可进行分类，并与标准定性工作流程相契合。在对2899个开放式响应的概念物理调查进行基准测试时，该框架与专家编码者的全面编码方案相比，Cohen's Kappa值在0.74到0.83之间。我们还展示了通过微调文本嵌入模型可以提高框架的性能，并且该方法可用于审计先前分析的数据集。这些发现表明，文本嵌入辅助编码能够灵活扩展到数千个响应，而不牺牲可解释性，为大规模的演绎定性分析开辟了新途径。

## 🔬 方法详解

**问题定义**：本文旨在解决开放式调查响应的定性分析中，传统编码方法耗时且不一致的问题。现有的自然语言处理技术在此领域的应用受到标注数据需求和工作流程干扰的限制。

**核心思路**：提出的框架利用文本嵌入技术，仅需少量示例进行分类，能够与现有的定性分析流程兼容，提升分析效率和一致性。

**技术框架**：该框架包括文本嵌入生成、分类模型训练和结果分析三个主要模块。首先，通过文本嵌入将开放式响应转化为向量表示，然后使用少量标注数据训练分类模型，最后对结果进行分析和审计。

**关键创新**：最重要的创新在于框架的可扩展性和与定性分析流程的兼容性，能够在不牺牲可解释性的情况下处理大量响应，区别于传统方法的高标注需求。

**关键设计**：框架中的文本嵌入模型经过微调以提高性能，采用适合定性分析的损失函数和网络结构，确保分类结果的准确性和一致性。具体参数设置和模型选择在实验中进行了优化。

## 📊 实验亮点

实验结果表明，提出的框架在与人类专家的分析对比中，Cohen's Kappa值达到0.74至0.83，显示出良好的分类一致性。通过微调文本嵌入模型，框架的性能得到了显著提升，展示了其在大规模数据分析中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括社会科学、市场研究和用户反馈分析等，能够帮助研究人员和分析师高效处理和分析开放式调查数据。其灵活性和可扩展性使得大规模定性分析成为可能，未来可能对相关领域的研究方法产生深远影响。

## 📄 摘要（原文）

> Qualitative analysis of open-ended survey responses is a commonly-used research method in the social sciences, but traditional coding approaches are often time-consuming and prone to inconsistency. Existing solutions from Natural Language Processing such as supervised classifiers, topic modeling techniques, and generative large language models have limited applicability in qualitative analysis, since they demand extensive labeled data, disrupt established qualitative workflows, and/or yield variable results. In this paper, we introduce a text embedding-based classification framework that requires only a handful of examples per category and fits well with standard qualitative workflows. When benchmarked against human analysis of a conceptual physics survey consisting of 2899 open-ended responses, our framework achieves a Cohen's Kappa ranging from 0.74 to 0.83 as compared to expert human coders in an exhaustive coding scheme. We further show how performance of this framework improves with fine-tuning of the text embedding model, and how the method can be used to audit previously-analyzed datasets. These findings demonstrate that text embedding-assisted coding can flexibly scale to thousands of responses without sacrificing interpretability, opening avenues for deductive qualitative analysis at scale.

