---
layout: default
title: Towards Understanding the Cognitive Habits of Large Reasoning Models
---

# Towards Understanding the Cognitive Habits of Large Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21571" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21571v2</a>
  <a href="https://arxiv.org/pdf/2506.21571.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21571v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21571v2', 'Towards Understanding the Cognitive Habits of Large Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianshuo Dong, Yujia Fu, Chuanrui Hu, Chao Zhang, Han Qiu

**分类**: cs.CL, cs.AI, cs.CR

**发布日期**: 2025-06-13 (更新: 2025-07-06)

**🔗 代码/项目**: [GITHUB](https://github.com/jianshuod/CogTest)

---

## 💡 一句话要点

**提出CogTest以评估大型推理模型的认知习惯**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型推理模型` `认知习惯` `CogTest` `推理思维链` `模型监控` `安全性评估` `人机交互`

## 📋 核心要点

1. 现有大型语言模型（LLMs）在推理能力和行为监控方面存在不足，缺乏对其认知习惯的深入理解。
2. 提出CogTest基准，通过16种认知习惯和25个任务的实例化，系统评估LRMs的认知习惯。
3. 实验结果表明，LRMs展现出人类认知习惯，并能根据任务自适应调整，尤其在安全任务中表现出特定习惯与有害响应的关联。

## 📝 摘要（中文）

大型推理模型（LRMs）在生成最终响应之前，能够自主产生推理思维链（CoT），为理解和监控模型行为提供了新方法。本文基于人类成功解决问题的认知习惯框架，提出了CogTest基准，旨在评估LRMs的认知习惯。CogTest包含16种认知习惯，每种习惯通过25个多样化任务进行实例化，并采用证据优先的提取方法以确保习惯识别的可靠性。研究发现，LRMs不仅展现出人类般的习惯，还能根据不同任务自适应地运用这些习惯。进一步分析揭示了LRMs认知习惯特征的相似性与差异性，尤其是在不同模型家族之间的相似性。研究还扩展到安全相关任务，发现某些习惯与有害响应的生成密切相关。

## 🔬 方法详解

**问题定义**：本文旨在解决对大型推理模型（LRMs）认知习惯的理解不足，现有方法未能有效监控和解释模型行为的根本原因。

**核心思路**：通过引入CogTest基准，系统化评估LRMs的认知习惯，借鉴人类成功问题解决的认知习惯框架，提供可靠的评估工具。

**技术框架**：CogTest包括16种认知习惯，每种习惯通过25个多样化任务进行评估，采用证据优先的提取方法确保习惯识别的准确性。

**关键创新**：CogTest的设计使得对LRMs的认知习惯进行系统评估成为可能，揭示了LRMs与传统LLMs在认知习惯上的显著差异。

**关键设计**：在CogTest中，任务设计多样化，确保覆盖不同场景，采用证据优先的提取方法以提高习惯识别的可靠性。

## 📊 实验亮点

实验结果显示，LRMs在认知习惯的表现上显著优于传统LLMs，尤其在安全相关任务中，某些习惯如“承担责任的风险”与有害响应生成之间存在强关联。这为理解和改进模型行为提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括人工智能模型的安全性评估、行为监控以及人机交互优化。通过深入理解LRMs的认知习惯，可以为模型的设计和应用提供指导，提升其在复杂任务中的表现和安全性。

## 📄 摘要（原文）

> Large Reasoning Models (LRMs), which autonomously produce a reasoning Chain of Thought (CoT) before producing final responses, offer a promising approach to interpreting and monitoring model behaviors. Inspired by the observation that certain CoT patterns -- e.g., ``Wait, did I miss anything?'' -- consistently emerge across tasks, we explore whether LRMs exhibit human-like cognitive habits. Building on Habits of Mind, a well-established framework of cognitive habits associated with successful human problem-solving, we introduce CogTest, a principled benchmark designed to evaluate LRMs' cognitive habits. CogTest includes 16 cognitive habits, each instantiated with 25 diverse tasks, and employs an evidence-first extraction method to ensure reliable habit identification. With CogTest, we conduct a comprehensive evaluation of 16 widely used LLMs (13 LRMs and 3 non-reasoning ones). Our findings reveal that LRMs, unlike conventional LLMs, not only exhibit human-like habits but also adaptively deploy them according to different tasks. Finer-grained analyses further uncover patterns of similarity and difference in LRMs' cognitive habit profiles, particularly certain inter-family similarity (e.g., Qwen-3 models and DeepSeek-R1). Extending the study to safety-related tasks, we observe that certain habits, such as Taking Responsible Risks, are strongly associated with the generation of harmful responses. These findings suggest that studying persistent behavioral patterns in LRMs' CoTs is a valuable step toward deeper understanding of LLM misbehavior. The code is available at: https://github.com/jianshuod/CogTest.

