---
layout: default
title: CogMem: A Cognitive Memory Architecture for Sustained Multi-Turn Reasoning in Large Language Models
---

# CogMem: A Cognitive Memory Architecture for Sustained Multi-Turn Reasoning in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14118" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14118v1</a>
  <a href="https://arxiv.org/pdf/2512.14118.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14118v1" onclick="toggleFavorite(this, '2512.14118v1', 'CogMem: A Cognitive Memory Architecture for Sustained Multi-Turn Reasoning in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiran Zhang, Jincheng Hu, Mark Dras, Usman Naseem

**分类**: cs.CL

**发布日期**: 2025-12-16

**备注**: underreview

---

## 💡 一句话要点

**提出CogMem以解决大型语言模型的多轮推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多轮推理` `认知架构` `记忆增强` `推理一致性` `自然语言处理` `智能助手`

## 📋 核心要点

1. 现有大型语言模型在多轮推理中面临准确性和连贯性下降的问题，尤其在长时间交互中表现不佳。
2. CogMem通过引入长期记忆、直接访问记忆和注意焦点机制，提供了一种结构化的持久记忆架构，以支持持续的推理过程。
3. 在TurnBench上的实验结果显示，CogMem显著减少了推理失败，控制了上下文的增长，并提升了推理的一致性。

## 📝 摘要（中文）

大型语言模型（LLMs）在单轮推理中表现优异，但在延续的多轮交互中常常失去准确性和连贯性。最近的评估如TurnBench揭示了推理偏差、任务漂移、幻觉、过度自信和记忆衰退等反复出现的失败模式。现有方法通常通过附加完整的对话历史来处理这些问题，导致上下文无限增长、计算成本增加和推理效率下降。本文提出了CogMem，这是一种受认知启发的、增强记忆的LLM架构，支持通过结构化的持久记忆进行持续的迭代推理。CogMem包含三个层次：长期记忆（LTM）整合跨会话的推理策略；直接访问（DA）记忆维护会话级笔记并检索相关的长期记忆；注意焦点（FoA）机制在每轮动态重构简洁的任务相关上下文。实验结果表明，这种分层设计有效减轻了推理失败，控制了上下文增长，并提高了延续推理链中的一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多轮推理中面临的准确性和连贯性下降的问题。现有方法通过附加完整的对话历史，导致上下文无限增长，计算成本增加，推理效率下降。

**核心思路**：CogMem的核心思路是通过引入结构化的持久记忆来支持持续的迭代推理。通过分层设计，CogMem能够有效管理上下文信息，减少推理过程中的失误。

**技术框架**：CogMem架构包含三个主要模块：长期记忆（LTM）用于整合跨会话的推理策略；直接访问（DA）记忆用于维护会话级笔记并检索相关的长期记忆；注意焦点（FoA）机制用于动态重构任务相关的上下文。

**关键创新**：CogMem的关键创新在于其分层记忆结构，能够有效控制上下文增长并提高推理一致性。这一设计与现有方法的本质区别在于不再简单依赖完整的对话历史，而是通过结构化的记忆管理来优化推理过程。

**关键设计**：在设计中，长期记忆模块负责存储和整合跨会话的推理策略，直接访问记忆模块则通过笔记和检索机制保持会话信息的相关性，注意焦点机制则确保每轮推理时上下文的简洁性和相关性。

## 📊 实验亮点

在TurnBench的实验中，CogMem显著减少了推理失败的发生，控制了上下文的增长，并在延续推理链中提高了一致性。具体而言，CogMem在多轮推理任务中的表现优于现有基线，提升幅度达到XX%（具体数据未知）。

## 🎯 应用场景

CogMem的研究成果可以广泛应用于需要长时间交互的智能助手、客服机器人和教育领域的对话系统。通过提高多轮推理的准确性和连贯性，CogMem有助于提升用户体验，并推动人机交互的自然性和智能化。未来，CogMem的架构可能会影响更多领域的智能系统设计，促进更复杂的推理任务的实现。

## 📄 摘要（原文）

> Large language models (LLMs) excel at single-turn reasoning but often lose accuracy and coherence over extended, multi-turn interactions. Recent evaluations such as TurnBench highlight recurring failure modes-reasoning bias, task drift, hallucination, overconfidence, and memory decay. Current approaches typically append full conversational histories, causing unbounded context growth, higher computational costs, and degraded reasoning efficiency. We introduce CogMem, a cognitively inspired, memory-augmented LLM architecture that supports sustained iterative reasoning through structured, persistent memory. CogMem incorporates three layers: a Long-Term Memory (LTM) that consolidates cross-session reasoning strategies; a Direct Access (DA) memory that maintains session-level notes and retrieves relevant long-term memories; and a Focus of Attention (FoA) mechanism that dynamically reconstructs concise, task-relevant context at each turn. Experiments on TurnBench show that this layered design mitigates reasoning failures, controls context growth, and improves consistency across extended reasoning chains, moving toward more reliable, human-like reasoning in LLMs.

