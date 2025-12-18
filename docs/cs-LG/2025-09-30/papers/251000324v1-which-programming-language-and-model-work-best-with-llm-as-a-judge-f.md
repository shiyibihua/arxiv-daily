---
layout: default
title: Which Programming Language and Model Work Best With LLM-as-a-Judge For Code Retrieval?
---

# Which Programming Language and Model Work Best With LLM-as-a-Judge For Code Retrieval?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00324" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00324v1</a>
  <a href="https://arxiv.org/pdf/2510.00324.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00324v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00324v1', 'Which Programming Language and Model Work Best With LLM-as-a-Judge For Code Retrieval?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lucas Roberts, Denisa Roberts

**分类**: cs.SE, cs.IR, cs.LG

**发布日期**: 2025-09-30

**备注**: Accepted as a full paper at SIGIR-AP 2025

**DOI**: [10.1145/3767695.3769503](https://doi.org/10.1145/3767695.3769503)

**🔗 代码/项目**: [GITHUB](https://github.com/rlucas7/code-searcher/)

---

## 💡 一句话要点

**利用大型语言模型优化代码检索与注释生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码检索` `大型语言模型` `编程语言` `人工智能` `信息检索` `软件工程` `自动注释生成`

## 📋 核心要点

1. 现有代码检索方法面临高昂的人为注释成本，限制了其在实际应用中的有效性。
2. 本研究提出利用大型语言模型进行代码检索和注释生成，比较不同编程语言和检索器的影响。
3. 实验结果表明，选择合适的检索器和编程语言可以显著提高人类与AI的相关性判断一致性。

## 📝 摘要（中文）

代码检索是信息检索中的重要应用，能够加速新开发者的入门、降低软件维护成本并提高对大型代码库的理解。然而，尽管搜索算法和基准测试有所改进，代码检索领域仍然滞后，主要原因在于代码查询和答案的人为注释成本高昂。本研究探讨了使用大型语言模型（LLMs）在函数级别检索代码并生成注释的可行性。通过比较稀疏与语义检索器、编程语言及LLM的影响，发现选择的检索器和编程语言之间存在可利用的亲和性，从而改善人类与AI的相关性判断。研究还提出使用转译器来构建可扩展的代码检索基准数据集，并展示了人类与AI的相关性一致性率与人类之间的一致性相匹配。

## 🔬 方法详解

**问题定义**：本研究旨在解决代码检索中高昂的人为注释成本问题。现有方法在处理代码查询和答案时，缺乏有效的自动化手段，导致效率低下。

**核心思路**：本研究的核心思路是利用大型语言模型（LLMs）来自动检索代码并生成注释，从而减少对人工注释的依赖。通过比较不同的编程语言和检索器，探索其对检索效果的影响。

**技术框架**：整体架构包括数据收集、LLM检索、注释生成和效果评估四个主要模块。首先收集实现常见数据结构的代码库，然后使用LLMs进行代码检索和注释生成，最后通过人类标注进行效果评估。

**关键创新**：本研究的关键创新在于提出了利用LLMs进行代码检索的框架，并发现不同编程语言和检索器之间的亲和性可以显著改善人类与AI的相关性判断一致性。这一发现为代码检索领域提供了新的思路。

**关键设计**：在实验中，采用了稀疏和语义检索器的对比，设置了多种编程语言（如C、Java、JavaScript、Go和Python），并通过转译器构建可扩展的基准数据集，确保了实验的全面性和有效性。具体的参数设置和损失函数设计在论文中有详细描述。

## 📊 实验亮点

实验结果显示，选择合适的检索器和编程语言可以显著提高人类与AI的相关性判断一致性，达到与人类之间一致性相匹配的水平。此外，稀疏与语义检索器在不同编程语言上的表现差异也为后续研究提供了新的方向。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、代码维护和教育等。通过提高代码检索的效率，能够帮助开发者更快地找到所需代码，降低学习曲线，并提升软件维护的便捷性。未来，随着技术的进一步发展，该方法有望在更广泛的编程语言和场景中得到应用。

## 📄 摘要（原文）

> Code search is an important information retrieval application. Benefits of better code search include faster new developer on-boarding, reduced software maintenance, and ease of understanding for large repositories. Despite improvements in search algorithms and search benchmarks, the domain of code search has lagged behind. One reason is the high cost of human annotation for code queries and answers. While humans may annotate search results in general text QA systems, code annotations require specialized knowledge of a programming language (PL), as well as domain specific software engineering knowledge. In this work we study the use of Large Language Models (LLMs) to retrieve code at the level of functions and to generate annotations for code search results. We compare the impact of the retriever representation (sparse vs. semantic), programming language, and LLM by comparing human annotations across several popular languages (C, Java, Javascript, Go, and Python). We focus on repositories that implement common data structures likely to be implemented in any PLs. For the same human annotations, we compare several LLM-as-a-Judge models to evaluate programming language and other affinities between LLMs. We find that the chosen retriever and PL exhibit affinities that can be leveraged to improve alignment of human and AI relevance determinations, with significant performance implications. We also find differences in representation (sparse vs. semantic) across PLs that impact alignment of human and AI relevance determinations. We propose using transpilers to bootstrap scalable code search benchmark datasets in other PLs and in a case study demonstrate that human-AI relevance agreement rates largely match the (worst case) human-human agreement under study. The application code used in this work is available at \href{https://github.com/rlucas7/code-searcher/}{this github repo}.

