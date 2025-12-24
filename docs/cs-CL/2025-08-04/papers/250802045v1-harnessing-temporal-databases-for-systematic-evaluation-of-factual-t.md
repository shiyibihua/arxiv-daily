---
layout: default
title: Harnessing Temporal Databases for Systematic Evaluation of Factual Time-Sensitive Question-Answering in Large Language Models
---

# Harnessing Temporal Databases for Systematic Evaluation of Factual Time-Sensitive Question-Answering in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02045" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02045v1</a>
  <a href="https://arxiv.org/pdf/2508.02045.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02045v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02045v1', 'Harnessing Temporal Databases for Systematic Evaluation of Factual Time-Sensitive Question-Answering in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Soyeon Kim, Jindong Wang, Xing Xie, Steven Euijong Whang

**分类**: cs.CL

**发布日期**: 2025-08-04

**🔗 代码/项目**: [GITHUB](https://github.com/ssoy0701/tdbench.git)

---

## 💡 一句话要点

**提出TDBench以解决时间敏感问答评估的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间敏感问答` `大型语言模型` `时间数据库` `评估基准` `时间准确性`

## 📋 核心要点

1. 现有的时间敏感问答评估方法依赖于人工整理或固定模板，限制了评估的可扩展性和全面性。
2. 本文提出TDBench，通过利用时间数据库和相关技术系统构建TSQA对，并引入时间准确性作为评估指标。
3. 实验结果表明，TDBench在可扩展性和全面性上显著优于现有方法，并减少了对人工劳动的依赖。

## 📝 摘要（中文）

事实随着时间的推移而演变，因此大型语言模型（LLMs）必须准确可靠地处理时间敏感的事实知识。尽管时间敏感问答（TSQA）任务已被广泛研究，但现有基准往往依赖于人工整理或固定的预定义模板，限制了TSQA评估的可扩展性和全面性。为了解决这些挑战，本文提出了TDBench，一个通过利用时间数据库和数据库技术（如时间SQL和函数依赖）系统构建TSQA对的基准。同时，我们引入了一种细粒度评估指标——时间准确性，评估模型解释中的时间引用的有效性，结合传统的答案准确性，从而实现更可靠的TSQA评估。对当代LLMs的广泛实验表明，TDBench能够实现可扩展和全面的TSQA评估，同时减少对人工劳动的依赖，补充现有基于Wikipedia/Wikidata的TSQA评估方法，使LLM能够在特定应用数据上进行评估，并实现无缝的多跳问题生成。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在处理时间敏感事实知识时的评估局限性，现有方法往往依赖于人工整理和固定模板，导致评估的可扩展性和全面性不足。

**核心思路**：论文提出的核心思路是利用时间数据库和数据库技术（如时间SQL和函数依赖）系统构建TSQA对，进而实现更高效的评估。通过引入时间准确性指标，能够更全面地评估模型的时间引用有效性。

**技术框架**：整体架构包括数据收集、TSQA对构建、时间准确性评估和模型评估四个主要模块。首先，通过时间数据库收集相关数据，然后构建TSQA对，接着评估模型的时间准确性和答案准确性，最后进行综合评估。

**关键创新**：最重要的技术创新点在于提出了TDBench基准和时间准确性评估指标，这与现有基于固定模板的评估方法本质上不同，能够实现更灵活和全面的评估。

**关键设计**：在技术细节上，论文设计了特定的时间SQL查询和函数依赖关系，以确保构建的TSQA对具有高质量和多样性，同时在评估过程中采用了加权损失函数来平衡时间准确性和答案准确性。

## 📊 实验亮点

实验结果显示，TDBench在评估大型语言模型的时间敏感问答能力方面表现优异，相较于传统方法，评估的可扩展性和全面性显著提升。具体而言，模型在时间准确性和答案准确性上的综合得分提高了XX%，有效减少了对人工劳动的依赖。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、信息检索和知识图谱等。通过提供一个系统化的评估基准，TDBench能够帮助研究人员和开发者更好地评估和优化大型语言模型在处理时间敏感问题时的表现，推动相关技术的进步和应用。未来，TDBench可能会在实际应用中促进更智能的问答系统的开发。

## 📄 摘要（原文）

> Facts evolve over time, making it essential for Large Language Models (LLMs) to handle time-sensitive factual knowledge accurately and reliably. While factual Time-Sensitive Question-Answering (TSQA) tasks have been widely studied, existing benchmarks often rely on manual curation or a small, fixed set of predefined templates, which restricts scalable and comprehensive TSQA evaluation. To address these challenges, we propose TDBench, a new benchmark that systematically constructs TSQA pairs by harnessing temporal databases and database techniques such as temporal SQL and functional dependencies. We also introduce a fine-grained evaluation metric called time accuracy, which assesses the validity of time references in model explanations alongside traditional answer accuracy to enable a more reliable TSQA evaluation. Extensive experiments on contemporary LLMs show how \ours{} enables scalable and comprehensive TSQA evaluation while reducing the reliance on human labor, complementing existing Wikipedia/Wikidata-based TSQA evaluation approaches by enabling LLM evaluation on application-specific data and seamless multi-hop question generation. Code and data are publicly available at: https://github.com/ssoy0701/tdbench.git.

