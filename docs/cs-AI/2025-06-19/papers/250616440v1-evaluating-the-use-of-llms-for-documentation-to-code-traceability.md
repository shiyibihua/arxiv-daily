---
layout: default
title: Evaluating the Use of LLMs for Documentation to Code Traceability
---

# Evaluating the Use of LLMs for Documentation to Code Traceability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16440" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16440v1</a>
  <a href="https://arxiv.org/pdf/2506.16440.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16440v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16440v1', 'Evaluating the Use of LLMs for Documentation to Code Traceability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ebube Alor, SayedHassan Khatoonabadi, Emad Shihab

**分类**: cs.SE, cs.AI, cs.LG

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**评估大型语言模型在文档与代码追踪中的应用潜力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `文档与代码追踪` `自动化工具` `软件工程` `数据集构建`

## 📋 核心要点

1. 现有方法在文档与代码之间的追踪准确性和解释质量上存在不足，尤其在多步链重构方面表现不佳。
2. 本文提出通过评估多种大型语言模型来自动化文档与代码的追踪，利用新创建的数据集进行系统性实验。
3. 实验结果表明，最佳LLM在追踪链接识别上取得79.4%和80.4%的F1分数，部分准确性超过97%，显示出LLMs在追踪发现中的潜力。

## 📝 摘要（中文）

大型语言模型（LLMs）为自动化文档与代码追踪提供了新的可能性，但其能力尚未得到充分探索。本文全面评估了LLMs（Claude 3.5 Sonnet、GPT-4o和o3-mini）在建立软件文档（包括API参考和用户指南）与源代码之间的追踪链接的能力。我们从两个开源项目（Unity Catalog和Crawl4AI）创建了两个新数据集。通过系统实验，我们评估了三个关键能力：追踪链接识别准确性、关系解释质量和多步链重构。结果显示，表现最佳的LLM在两个数据集上的F1分数分别为79.4%和80.4%，显著优于基线（TF-IDF、BM25和CodeBERT）。

## 🔬 方法详解

**问题定义**：本文旨在解决文档与代码之间追踪链接的识别和解释问题，现有方法在准确性和多步链重构方面存在明显不足。

**核心思路**：通过系统评估不同的LLMs，探索其在文档与代码追踪中的应用潜力，尤其是如何提高追踪链接的识别和解释质量。

**技术框架**：研究采用了两个新创建的数据集，分别来自Unity Catalog和Crawl4AI项目，实验分为追踪链接识别、关系解释和多步链重构三个主要模块。

**关键创新**：本文的创新在于系统性地评估了多种LLMs在追踪任务中的表现，尤其是通过任务框架设计（如一对多匹配策略）来提升性能。

**关键设计**：实验中使用了F1分数作为主要评估指标，分析了错误来源，包括命名假设、虚假链接和架构模式的过度泛化等。

## 📊 实验亮点

实验结果显示，最佳表现的LLM在两个数据集上的F1分数分别为79.4%和80.4%，显著优于基线方法（TF-IDF、BM25和CodeBERT）。此外，部分准确性超过97%，表明LLMs在捕捉基本连接方面表现出色。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、维护和文档生成等，能够显著提高开发者在理解和维护代码时的效率。未来，随着LLMs的进一步发展，可能会在自动化文档生成和代码审查等方面发挥更大作用。

## 📄 摘要（原文）

> Large Language Models (LLMs) offer new potential for automating documentation-to-code traceability, yet their capabilities remain underexplored. We present a comprehensive evaluation of LLMs (Claude 3.5 Sonnet, GPT-4o, and o3-mini) in establishing trace links between various software documentation (including API references and user guides) and source code. We create two novel datasets from two open-source projects (Unity Catalog and Crawl4AI). Through systematic experiments, we assess three key capabilities: (1) trace link identification accuracy, (2) relationship explanation quality, and (3) multi-step chain reconstruction. Results show that the best-performing LLM achieves F1-scores of 79.4% and 80.4% across the two datasets, substantially outperforming our baselines (TF-IDF, BM25, and CodeBERT). While fully correct relationship explanations range from 42.9% to 71.1%, partial accuracy exceeds 97%, indicating that fundamental connections are rarely missed. For multi-step chains, LLMs maintain high endpoint accuracy but vary in capturing precise intermediate links. Error analysis reveals that many false positives stem from naming-based assumptions, phantom links, or overgeneralization of architectural patterns. We demonstrate that task-framing, such as a one-to-many matching strategy, is critical for performance. These findings position LLMs as powerful assistants for trace discovery, but their limitations could necessitate human-in-the-loop tool design and highlight specific error patterns for future research.

