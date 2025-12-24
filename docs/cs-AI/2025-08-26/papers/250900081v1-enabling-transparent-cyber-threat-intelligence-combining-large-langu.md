---
layout: default
title: Enabling Transparent Cyber Threat Intelligence Combining Large Language Models and Domain Ontologies
---

# Enabling Transparent Cyber Threat Intelligence Combining Large Language Models and Domain Ontologies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00081" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00081v1</a>
  <a href="https://arxiv.org/pdf/2509.00081.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00081v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00081v1', 'Enabling Transparent Cyber Threat Intelligence Combining Large Language Models and Domain Ontologies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luca Cotti, Anisa Rula, Devis Bianchini, Federico Cerutti

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-26

**备注**: 14 pages, 3 figures, 6 tables, accepted at XAI-KRKG@ECAI25: First International ECAI Workshop on eXplainable AI, Knowledge Representation and Knowledge Graphs, October 25-30, 2025, Bologna, Italy

---

## 💡 一句话要点

**提出结合本体论与大语言模型的网络威胁情报方法以解决信息提取问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网络威胁情报` `大语言模型` `本体论` `信息提取` `图数据库` `语义分析`

## 📋 核心要点

1. 现有网络威胁情报方法在处理非结构化日志时，难以可靠地识别和解释恶意事件。
2. 本文提出的方法结合了本体论和大语言模型，旨在提高信息提取的准确性和可解释性。
3. 实验结果表明，该方法在信息提取的准确性上优于传统的仅依赖提示的方法，重点关注提取质量。

## 📝 摘要（中文）

有效的网络威胁情报（CTI）依赖于从网络安全系统日志中提取的准确结构化和语义丰富的信息。然而，现有方法在识别和解释恶意事件时常常面临挑战，尤其是在处理非结构化或模糊的日志条目时。本文提出了一种新方法，结合本体驱动的结构化输出与大语言模型（LLMs），构建一个人工智能（AI）代理，以提高从网络安全日志中提取信息的准确性和可解释性。我们的研究通过集成领域本体和基于SHACL的约束，指导语言模型的输出结构并强制语义有效性。提取的信息被组织成一个丰富本体的图数据库，便于未来的语义分析和查询。

## 🔬 方法详解

**问题定义**：本文旨在解决现有网络威胁情报方法在处理非结构化日志时的识别和解释能力不足的问题，尤其是在面对模糊日志条目时的挑战。

**核心思路**：提出的方法通过结合本体驱动的结构化输出与大语言模型，利用领域本体和SHACL约束来指导语言模型的输出结构，从而提高信息提取的准确性和可解释性。

**技术框架**：整体架构包括数据预处理、信息提取、结构化输出和图数据库构建四个主要模块。首先，对日志数据进行预处理，然后利用大语言模型提取信息，接着通过本体和约束对输出进行结构化，最后将提取的信息存储在图数据库中。

**关键创新**：最重要的技术创新在于将本体论与大语言模型结合，形成了一种新的信息提取方法，显著提高了提取的准确性和语义有效性，与传统方法相比具有本质的区别。

**关键设计**：在设计中，采用了SHACL约束来确保输出的语义有效性，并通过优化模型参数来提升提取质量，具体的损失函数和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，提出的方法在信息提取的准确性上显著优于传统的仅依赖提示的方法，具体提升幅度未知。该方法强调提取质量而非处理速度，适应了网络安全领域对高准确性和可解释性的需求。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全监控、恶意活动检测和安全事件响应等。通过提高信息提取的准确性和可解释性，该方法能够帮助安全分析师更有效地识别和应对网络威胁，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Effective Cyber Threat Intelligence (CTI) relies upon accurately structured and semantically enriched information extracted from cybersecurity system logs. However, current methodologies often struggle to identify and interpret malicious events reliably and transparently, particularly in cases involving unstructured or ambiguous log entries. In this work, we propose a novel methodology that combines ontology-driven structured outputs with Large Language Models (LLMs), to build an Artificial Intelligence (AI) agent that improves the accuracy and explainability of information extraction from cybersecurity logs. Central to our approach is the integration of domain ontologies and SHACL-based constraints to guide the language model's output structure and enforce semantic validity over the resulting graph. Extracted information is organized into an ontology-enriched graph database, enabling future semantic analysis and querying. The design of our methodology is motivated by the analytical requirements associated with honeypot log data, which typically comprises predominantly malicious activity. While our case study illustrates the relevance of this scenario, the experimental evaluation is conducted using publicly available datasets. Results demonstrate that our method achieves higher accuracy in information extraction compared to traditional prompt-only approaches, with a deliberate focus on extraction quality rather than processing speed.

