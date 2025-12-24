---
layout: default
title: Many-Turn Jailbreaking
---

# Many-Turn Jailbreaking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06755" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06755v1</a>
  <a href="https://arxiv.org/pdf/2508.06755.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06755v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06755v1', 'Many-Turn Jailbreaking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianjun Yang, Liqiang Xiao, Shiyang Li, Faisal Ladhak, Hyokun Yun, Linda Ruth Petzold, Yi Xu, William Yang Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-09

---

## 💡 一句话要点

**提出多轮越狱基准以应对大型语言模型的安全威胁**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `越狱攻击` `大型语言模型` `安全性评估` `基准测试`

## 📋 核心要点

1. 现有的越狱研究仅关注单轮对话，未能考虑用户可能的后续提问，导致安全隐患未被充分揭示。
2. 本文提出多轮越狱的概念，构建了多轮越狱基准（MTJ-Bench），以评估LLMs在多轮对话中的表现。
3. 通过对多个开源和闭源模型的测试，揭示了LLMs在多轮对话中存在的安全漏洞，呼吁加强安全性研究。

## 📝 摘要（中文）

当前对大型语言模型（LLMs）的越狱研究主要集中在单轮对话中引发不安全输出。然而，先进的LLMs能够处理极长的上下文并进行多轮对话。因此，本文提出了多轮越狱的概念，强调在多轮对话中测试越狱模型的必要性。我们构建了一个多轮越狱基准（MTJ-Bench），用于评估这一新设定，并揭示了这一安全威胁的新脆弱性。通过这一研究，我们希望促使社区共同努力，构建更安全的LLMs，并深入理解LLMs的越狱机制。

## 🔬 方法详解

**问题定义**：本文旨在解决当前越狱研究仅限于单轮对话的问题，强调多轮对话中可能出现的安全漏洞。现有方法未能考虑用户的后续提问，导致潜在风险未被充分识别。

**核心思路**：提出多轮越狱的概念，强调在多轮对话中测试越狱模型的重要性。通过构建多轮越狱基准（MTJ-Bench），为评估LLMs在多轮对话中的表现提供了标准。

**技术框架**：整体架构包括数据收集、模型测试和结果分析三个主要模块。首先收集多轮对话数据，然后对多种LLMs进行越狱测试，最后分析模型在多轮对话中的表现和安全性。

**关键创新**：最重要的创新点在于首次提出多轮越狱的概念，并构建相应的基准，填补了现有研究的空白。与传统的单轮越狱方法相比，本文的方法更全面地评估了模型的安全性。

**关键设计**：在基准构建中，设置了多种对话场景和问题类型，确保测试的全面性和有效性。采用了多样化的模型进行评估，以验证不同模型在多轮对话中的表现差异。

## 📊 实验亮点

实验结果表明，在多轮对话中，越狱模型的安全性显著下降，部分模型在后续提问中仍然产生不安全输出。通过与基线模型的对比，发现多轮越狱的影响更为严重，呼吁对LLMs的安全性进行更深入的研究。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的安全性评估、对话系统的设计与优化等。通过深入理解多轮越狱的机制，可以为开发更安全的对话系统提供理论支持，减少模型被滥用的风险，提升用户信任度。

## 📄 摘要（原文）

> Current jailbreaking work on large language models (LLMs) aims to elicit unsafe outputs from given prompts. However, it only focuses on single-turn jailbreaking targeting one specific query. On the contrary, the advanced LLMs are designed to handle extremely long contexts and can thus conduct multi-turn conversations. So, we propose exploring multi-turn jailbreaking, in which the jailbroken LLMs are continuously tested on more than the first-turn conversation or a single target query. This is an even more serious threat because 1) it is common for users to continue asking relevant follow-up questions to clarify certain jailbroken details, and 2) it is also possible that the initial round of jailbreaking causes the LLMs to respond to additional irrelevant questions consistently. As the first step (First draft done at June 2024) in exploring multi-turn jailbreaking, we construct a Multi-Turn Jailbreak Benchmark (MTJ-Bench) for benchmarking this setting on a series of open- and closed-source models and provide novel insights into this new safety threat. By revealing this new vulnerability, we aim to call for community efforts to build safer LLMs and pave the way for a more in-depth understanding of jailbreaking LLMs.

