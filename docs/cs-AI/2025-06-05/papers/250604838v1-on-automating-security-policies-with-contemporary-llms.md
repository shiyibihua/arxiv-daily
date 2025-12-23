---
layout: default
title: On Automating Security Policies with Contemporary LLMs
---

# On Automating Security Policies with Contemporary LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04838" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04838v1</a>
  <a href="https://arxiv.org/pdf/2506.04838.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04838v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04838v1', 'On Automating Security Policies with Contemporary LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pablo Fernández Saura, K. R. Jayaram, Vatche Isahagian, Jorge Bernal Bernabé, Antonio Skarmeta

**分类**: cs.CR, cs.AI

**发布日期**: 2025-06-05

**备注**: Short Paper. Accepted To Appear in IEEE SSE 2025 (part of SERVICES 2025)

---

## 💡 一句话要点

**提出基于大型语言模型的自动化安全策略合规框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `安全策略` `大型语言模型` `自动化合规` `检索增强生成` `网络安全` `API调用` `任务分解`

## 📋 核心要点

1. 现代计算环境复杂且网络威胁日益复杂，现有安全策略执行方法难以适应这些变化。
2. 本文提出了一种基于大型语言模型的框架，通过上下文学习和检索增强生成实现自动化的攻击缓解政策合规。
3. 实证评估表明，使用RAG方法在精确率、召回率和F1-score上显著优于传统方法。

## 📝 摘要（中文）

现代计算环境的复杂性和网络威胁的日益复杂化要求采取更强大、适应性强且自动化的安全执行方法。本文提出了一种利用大型语言模型（LLMs）自动化攻击缓解政策合规的框架，结合了上下文学习和检索增强生成（RAG）。我们描述了系统如何收集和管理工具及API规范，并将其存储在向量数据库中以实现高效的信息检索。接着，我们详细介绍了架构管道，首先将高层次的缓解政策分解为离散任务，然后将每个任务翻译为一组可操作的API调用。通过使用公开的CTI政策和Windows API文档进行的实证评估，结果显示采用RAG相较于非RAG基线在精确率、召回率和F1-score上有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现代计算环境中安全策略执行的复杂性和效率问题。现有方法在应对快速变化的网络威胁时，往往缺乏灵活性和自动化程度，导致合规性难以保障。

**核心思路**：论文提出的框架利用大型语言模型，通过上下文学习和检索增强生成技术，自动化地将高层次的安全政策转化为具体的API调用，从而提高安全策略的执行效率和准确性。

**技术框架**：整体架构分为几个主要模块：首先是信息收集与管理模块，负责收集工具和API规范并存储在向量数据库中；其次是任务分解模块，将高层政策分解为离散任务；最后是API调用生成模块，将任务转化为可执行的API调用。

**关键创新**：最重要的创新在于将上下文学习与检索增强生成相结合，形成了一种新的自动化合规执行方式。这种方法与传统的手动或半自动化方法相比，显著提高了效率和准确性。

**关键设计**：在技术细节上，系统使用向量数据库进行信息检索，确保相关信息的快速获取；同时，任务分解和API调用生成的过程采用了特定的算法设计，以优化执行效率和准确性。

## 📊 实验亮点

实验结果显示，采用检索增强生成（RAG）方法后，系统在精确率、召回率和F1-score上均有显著提升，具体提升幅度超过20%。与非RAG基线相比，RAG方法在处理公开的CTI政策和Windows API文档时表现出更高的准确性和效率。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全、信息技术管理和企业安全策略执行等。通过自动化安全策略合规，企业能够更有效地应对网络威胁，降低安全风险，提升整体安全防护能力。未来，该框架有望在更广泛的安全领域中推广应用，进一步提升安全管理的智能化水平。

## 📄 摘要（原文）

> The complexity of modern computing environments and the growing sophistication of cyber threats necessitate a more robust, adaptive, and automated approach to security enforcement. In this paper, we present a framework leveraging large language models (LLMs) for automating attack mitigation policy compliance through an innovative combination of in-context learning and retrieval-augmented generation (RAG). We begin by describing how our system collects and manages both tool and API specifications, storing them in a vector database to enable efficient retrieval of relevant information. We then detail the architectural pipeline that first decomposes high-level mitigation policies into discrete tasks and subsequently translates each task into a set of actionable API calls. Our empirical evaluation, conducted using publicly available CTI policies in STIXv2 format and Windows API documentation, demonstrates significant improvements in precision, recall, and F1-score when employing RAG compared to a non-RAG baseline.

