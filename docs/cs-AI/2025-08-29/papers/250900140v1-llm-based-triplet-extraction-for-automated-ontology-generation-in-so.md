---
layout: default
title: LLM-based Triplet Extraction for Automated Ontology Generation in Software Engineering Standards
---

# LLM-based Triplet Extraction for Automated Ontology Generation in Software Engineering Standards

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00140" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00140v1</a>
  <a href="https://arxiv.org/pdf/2509.00140.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00140v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00140v1', 'LLM-based Triplet Extraction for Automated Ontology Generation in Software Engineering Standards')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Songhui Yue

**分类**: cs.SE, cs.AI

**发布日期**: 2025-08-29

---

## 💡 一句话要点

**提出基于LLM的三元组提取方法以实现软件工程标准的自动本体生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动本体生成` `三元组提取` `大型语言模型` `软件工程标准` `知识表示` `关系推断` `文档分割`

## 📋 核心要点

1. 现有的自动本体生成方法在处理软件工程标准中的长文本和领域特定术语时面临高噪声和结构不清晰的问题。
2. 本研究提出了一种基于LLM的三元组提取方法，结合文档分割和关系推断，旨在提高本体生成的效率和准确性。
3. 实验结果表明，所提方法在三元组提取的性能上与OpenIE方法相当，且在某些方面表现出更好的效果。

## 📝 摘要（中文）

本研究探讨了本体在知识表示和白盒推理中的重要性，并提出了一种基于大型语言模型（LLM）的自动化本体生成（AOG）方法，专注于软件工程标准（SES）的三元组提取。该方法通过文档分割、候选术语挖掘、基于LLM的关系推断、术语规范化和交叉对齐等步骤，构建了一个有效的AOG工作流程。研究中构建了三个粒度的黄金标准基准，以评估生成的本体，结果显示该方法在三元组提取上与OpenIE方法相当，甚至可能更具优势。

## 🔬 方法详解

**问题定义**：本研究旨在解决软件工程标准中长文本的自动本体生成问题，现有方法在处理高噪声和领域特定术语时效果不佳，导致提取的三元组质量低下。

**核心思路**：本研究通过引入大型语言模型（LLM）来辅助三元组提取，强调LLM在构建本体中的作用，旨在通过更智能的关系推断提高提取的准确性和效率。

**技术框架**：整体流程包括文档分割、候选术语挖掘、基于LLM的关系推断、术语规范化和交叉对齐等多个模块，形成一个完整的自动化本体生成工作流。

**关键创新**：本研究的主要创新在于将LLM引入三元组提取过程，区别于传统的仅依赖提示工程的方法，从而提升了本体生成的质量和效率。

**关键设计**：在设计中，采用了多层次的文档分割策略，结合LLM的上下文理解能力进行关系推断，并通过交叉对齐确保提取结果的一致性和准确性。具体的参数设置和损失函数设计尚未详细披露。

## 📊 实验亮点

实验结果显示，所提方法在三元组提取的性能上与OpenIE方法相当，且在某些情况下表现出更好的效果，具体性能数据尚未披露。此研究为自动本体生成提供了一种新的思路，具有较高的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括软件工程标准的自动化处理、知识图谱构建以及智能问答系统等。通过提高本体生成的效率和准确性，该方法能够为相关领域的知识管理和信息检索提供重要支持，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Ontologies have supported knowledge representation and whitebox reasoning for decades; thus, the automated ontology generation (AOG) plays a crucial role in scaling their use. Software engineering standards (SES) consist of long, unstructured text (with high noise) and paragraphs with domain-specific terms. In this setting, relation triple extraction (RTE), together with term extraction, constitutes the first stage toward AOG. This work proposes an open-source large language model (LLM)-assisted approach to RTE for SES. Instead of solely relying on prompt-engineering-based methods, this study promotes the use of LLMs as an aid in constructing ontologies and explores an effective AOG workflow that includes document segmentation, candidate term mining, LLM-based relation inference, term normalization, and cross-section alignment. Golden-standard benchmarks at three granularities are constructed and used to evaluate the ontology generated from the study. The results show that it is comparable and potentially superior to the OpenIE method of triple extraction.

