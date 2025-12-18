---
layout: default
title: Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs
---

# Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15464" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15464v1</a>
  <a href="https://arxiv.org/pdf/2509.15464.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15464v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15464v1', 'Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhong Lin, Song Wang, Xiaojie Guo, Julian Shun, Yada Zhu

**分类**: cs.LG

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**提出EvoReasoner以解决动态知识推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态知识推理` `知识图谱演变` `时间感知推理` `大型语言模型` `多跳推理` `信息检索` `智能问答系统`

## 📋 核心要点

1. 现有方法通常假设知识图谱是静态的，忽视了真实世界数据中固有的时间动态和事实不一致性。
2. 本文提出EvoReasoner算法，结合EvoKG模块，能够动态更新知识图谱并进行时间感知推理。
3. 实验结果显示，使用该方法的8B参数模型在动态问答任务中达到了671B模型的性能，显著提升了小型模型的表现。

## 📝 摘要（中文）

大型语言模型（LLMs）在许多语言理解任务中表现出色，但在处理不断演变的知识时却面临挑战。为了解决这一问题，本文提出了EvoReasoner，一种时间感知的多跳推理算法，结合了EvoKG模块以动态更新知识图谱（KG）。EvoReasoner通过全局-局部实体定位、多路径分解和时间基础评分来处理时间变化的知识，而EvoKG则通过基于置信度的矛盾解决和时间趋势跟踪来确保KG的准确性和时效性。实验结果表明，该方法在动态问答任务中优于现有的基线，缩小了小型和大型LLMs之间的性能差距。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在处理动态知识时的推理能力不足，现有方法未能有效应对知识图谱的时间变化和事实不一致性问题。

**核心思路**：提出EvoReasoner算法，通过结合时间感知的推理机制和动态更新的知识图谱，来增强LLMs在动态问答中的表现。设计的核心在于有效整合时间信息与知识图谱的演变。

**技术框架**：整体架构包括EvoReasoner和EvoKG两个主要模块。EvoReasoner负责多跳推理和时间基础评分，而EvoKG则负责从非结构化文档中增量更新知识图谱。

**关键创新**：最重要的创新在于EvoReasoner的多路径分解和全局-局部实体定位策略，以及EvoKG的噪声容忍演变机制，这些设计使得模型能够处理时间动态的知识。

**关键设计**：在EvoKG中，采用基于置信度的矛盾解决策略和时间趋势跟踪机制，确保知识图谱的准确性和时效性。模型的损失函数和网络结构经过优化，以支持动态更新和推理过程。

## 📊 实验亮点

实验结果表明，EvoReasoner在动态问答基准测试中表现优异，8B参数模型的性能与671B模型相当，显示出显著的提升幅度，缩小了小型和大型LLMs之间的性能差距。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、知识管理和信息检索等。通过结合时间推理与知识图谱演变，能够显著提升系统在处理动态信息时的准确性和响应速度，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) excel at many language understanding tasks but struggle to reason over knowledge that evolves. To address this, recent work has explored augmenting LLMs with knowledge graphs (KGs) to provide structured, up-to-date information. However, many existing approaches assume a static snapshot of the KG and overlook the temporal dynamics and factual inconsistencies inherent in real-world data. To address the challenge of reasoning over temporally shifting knowledge, we propose EvoReasoner, a temporal-aware multi-hop reasoning algorithm that performs global-local entity grounding, multi-route decomposition, and temporally grounded scoring. To ensure that the underlying KG remains accurate and up-to-date, we introduce EvoKG, a noise-tolerant KG evolution module that incrementally updates the KG from unstructured documents through confidence-based contradiction resolution and temporal trend tracking. We evaluate our approach on temporal QA benchmarks and a novel end-to-end setting where the KG is dynamically updated from raw documents. Our method outperforms both prompting-based and KG-enhanced baselines, effectively narrowing the gap between small and large LLMs on dynamic question answering. Notably, an 8B-parameter model using our approach matches the performance of a 671B model prompted seven months later. These results highlight the importance of combining temporal reasoning with KG evolution for robust and up-to-date LLM performance. Our code is publicly available at github.com/junhongmit/TREK.

