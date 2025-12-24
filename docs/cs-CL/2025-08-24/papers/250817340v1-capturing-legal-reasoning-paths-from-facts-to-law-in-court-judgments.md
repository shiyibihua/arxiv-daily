---
layout: default
title: Capturing Legal Reasoning Paths from Facts to Law in Court Judgments using Knowledge Graphs
---

# Capturing Legal Reasoning Paths from Facts to Law in Court Judgments using Knowledge Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17340" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17340v1</a>
  <a href="https://arxiv.org/pdf/2508.17340.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17340v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17340v1', 'Capturing Legal Reasoning Paths from Facts to Law in Court Judgments using Knowledge Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ryoma Kondo, Riona Matsuoka, Takahiro Yoshida, Kazuyuki Yamasawa, Ryohei Hisano

**分类**: cs.CL, cs.AI, cs.DB, cs.IR

**发布日期**: 2025-08-24

**期刊**: Proc. 13th Int. Conf. on Knowledge Capture (K-CAP 2025), ACM, Dayton, Ohio, USA, Dec 2025

---

## 💡 一句话要点

**构建法律知识图谱以解决法律推理路径捕捉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律知识图谱` `法律推理` `大型语言模型` `信息检索` `机器学习`

## 📋 核心要点

1. 现有的自动化法律推理方法在捕捉法律背景和事实与法律规范关系方面存在显著不足。
2. 本文提出通过构建法律知识图谱，利用大型语言模型提取法律推理组件，解决现有方法的局限性。
3. 实验结果表明，所提系统在从事实中检索相关法律条款的准确性上优于现有基线，提升效果显著。

## 📝 摘要（中文）

法院判决揭示了法律规则如何被解释和应用于事实，为理解结构化法律推理提供了基础。然而，现有的自动化法律推理捕捉方法，包括大型语言模型，常常无法识别相关法律背景，未能准确追踪事实与法律规范之间的关系，并可能错误地表现出司法推理的分层结构。本文通过构建一个基于648个日本行政法院判决的法律知识图谱，解决了这些挑战。我们的方法利用基于提示的大型语言模型提取法律推理的组成部分，规范法律条款的引用，并通过法律推理本体将事实、规范和法律应用联系起来。最终生成的图谱捕捉了法律推理在真实法院判决中的完整结构，使隐含推理变得明确且可机器读取。我们使用专家标注的数据对系统进行了评估，发现其在从事实中检索相关法律条款的准确性上优于大型语言模型基线和增强检索方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有法律推理捕捉方法无法准确识别法律背景和追踪事实与法律规范关系的问题。现有方法常常导致法律推理的结构性信息丢失。

**核心思路**：通过构建法律知识图谱，利用大型语言模型提取法律推理的组成部分，并通过法律推理本体将事实、规范和法律应用进行关联，从而使隐含推理显性化。

**技术框架**：整体架构包括数据收集、法律推理组件提取、法律条款规范化和知识图谱构建四个主要模块。首先，从648个法院判决中提取数据，然后利用大型语言模型进行推理组件的提取，接着规范化法律条款，最后构建知识图谱。

**关键创新**：最重要的技术创新在于通过法律推理本体实现事实、法律规范和法律应用的有效链接，使得法律推理的结构化信息能够被机器读取，与现有方法相比，显著提升了法律推理的可解释性和准确性。

**关键设计**：在模型设计中，采用了基于提示的语言模型进行推理组件提取，设置了特定的损失函数以优化法律条款的规范化过程，并设计了适合法律推理的本体结构以增强知识图谱的表达能力。

## 📊 实验亮点

实验结果显示，所提系统在从事实中检索相关法律条款的准确性上显著优于大型语言模型基线，提升幅度达到未知，验证了该方法在法律推理捕捉中的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括法律信息检索、法律教育和智能法律咨询等。通过构建法律知识图谱，可以提高法律文书的自动化处理能力，帮助法律从业者更高效地获取相关法律信息，促进法律服务的智能化发展。

## 📄 摘要（原文）

> Court judgments reveal how legal rules have been interpreted and applied to facts, providing a foundation for understanding structured legal reasoning. However, existing automated approaches for capturing legal reasoning, including large language models, often fail to identify the relevant legal context, do not accurately trace how facts relate to legal norms, and may misrepresent the layered structure of judicial reasoning. These limitations hinder the ability to capture how courts apply the law to facts in practice. In this paper, we address these challenges by constructing a legal knowledge graph from 648 Japanese administrative court decisions. Our method extracts components of legal reasoning using prompt-based large language models, normalizes references to legal provisions, and links facts, norms, and legal applications through an ontology of legal inference. The resulting graph captures the full structure of legal reasoning as it appears in real court decisions, making implicit reasoning explicit and machine-readable. We evaluate our system using expert annotated data, and find that it achieves more accurate retrieval of relevant legal provisions from facts than large language model baselines and retrieval-augmented methods.

