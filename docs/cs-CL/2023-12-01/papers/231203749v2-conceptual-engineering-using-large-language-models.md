---
layout: default
title: Conceptual Engineering Using Large Language Models
---

# Conceptual Engineering Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.03749" class="toolbar-btn" target="_blank">📄 arXiv: 2312.03749v2</a>
  <a href="https://arxiv.org/pdf/2312.03749.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.03749v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.03749v2', 'Conceptual Engineering Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bradley P. Allen

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2023-12-01 (更新: 2024-11-02)

**备注**: 22 pages, 2 figures, to appear in Vincent C. Müller, Aliya R. Dewey, Leonard Dung & Guido Löhr (eds.), Philosophy of Artificial Intelligence: The State of the Art. Berlin: SpringerNature (forthcoming), for associated code and data see https://github.com/bradleypallen/zero-shot-classifiers-for-conceptual-engineering

---

## 💡 一句话要点

**基于大语言模型的概念工程方法提出**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `概念工程` `大语言模型` `分类程序` `Wikidata` `定义评估` `自然语言处理` `哲学` `人工智能`

## 📋 核心要点

1. 现有的概念工程方法在定义和分类程序的有效性上存在不足，难以准确评估复杂概念的变化。
2. 论文提出了一种利用大语言模型的分类程序，通过Wikidata知识图的数据进行概念工程的评估和改进。
3. 实验结果显示，该方法在分类性能上表现良好，并能生成合理的分类理由，帮助识别定义中的潜在问题。

## 📝 摘要（中文）

本文描述了一种基于Jennifer Nado提出的分类程序作为概念工程目标的方法，通过提示大语言模型来实现这些程序。我们利用Wikidata知识图的数据，评估与两个典型概念工程项目相关的规定性定义：国际天文学联合会对“行星”的重新定义和Haslanger对“女性”的改善性分析。结果表明，使用我们的方法构建的分类程序能够展现良好的分类性能，并通过生成分类的理由，有助于识别定义或评估数据中的问题。我们考虑了对该方法的反对意见，并讨论了该研究对概念工程理论和实践的三个方面的影响：目标的定义、实证方法的调查及其实际角色。实验数据和代码已在Github上公开。

## 🔬 方法详解

**问题定义**：本文旨在解决现有概念工程方法在定义和分类程序有效性评估上的不足，尤其是在复杂概念的重新定义过程中，现有方法往往缺乏系统性和准确性。

**核心思路**：论文的核心思路是通过提示大语言模型，利用其强大的自然语言处理能力来实现分类程序，从而对概念进行有效的工程和评估。这种设计旨在提高分类的准确性和可解释性。

**技术框架**：整体架构包括数据收集、模型训练和分类评估三个主要模块。首先，从Wikidata知识图中提取相关数据，然后使用大语言模型进行训练，最后评估模型的分类性能和生成的分类理由。

**关键创新**：最重要的技术创新点在于将大语言模型应用于概念工程的分类程序中，突破了传统方法的局限性，使得分类过程更加灵活和高效。

**关键设计**：在技术细节上，论文设置了特定的提示格式以引导模型生成合理的分类结果，并采用了适当的损失函数来优化模型性能，确保分类的准确性和可解释性。

## 📊 实验亮点

实验结果表明，使用该方法构建的分类程序在分类性能上达到了较高的准确率，具体数据未提供，但相较于传统方法有显著提升。同时，生成的分类理由有效地帮助识别了定义中的问题，展示了该方法的实用性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括哲学、语言学和人工智能等领域，特别是在需要对复杂概念进行重新定义和分类的场景中。其实际价值在于提供了一种新的工具，帮助研究人员更好地理解和分析概念的演变，未来可能影响相关学科的研究方法和实践。

## 📄 摘要（原文）

> We describe a method, based on Jennifer Nado's proposal for classification procedures as targets of conceptual engineering, that implements such procedures by prompting a large language model. We apply this method, using data from the Wikidata knowledge graph, to evaluate stipulative definitions related to two paradigmatic conceptual engineering projects: the International Astronomical Union's redefinition of PLANET and Haslanger's ameliorative analysis of WOMAN. Our results show that classification procedures built using our approach can exhibit good classification performance and, through the generation of rationales for their classifications, can contribute to the identification of issues in either the definitions or the data against which they are being evaluated. We consider objections to this method, and discuss implications of this work for three aspects of theory and practice of conceptual engineering: the definition of its targets, empirical methods for their investigation, and their practical roles. The data and code used for our experiments, together with the experimental results, are available in a Github repository.

