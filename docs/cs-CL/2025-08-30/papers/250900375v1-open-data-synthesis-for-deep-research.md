---
layout: default
title: Open Data Synthesis For Deep Research
---

# Open Data Synthesis For Deep Research

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00375" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00375v1</a>
  <a href="https://arxiv.org/pdf/2509.00375.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00375v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00375v1', 'Open Data Synthesis For Deep Research')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyi Xia, Kun Luo, Hongjin Qian, Zheng Liu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-30

**🔗 代码/项目**: [GITHUB](https://github.com/VectorSpaceLab/InfoSeek)

---

## 💡 一句话要点

**提出InfoSeek框架以解决复杂深度研究任务的合成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度研究` `层次约束满足` `信息合成` `多步推理` `自然语言处理`

## 📋 核心要点

1. 现有的基准测试未能有效捕捉深度研究任务的复杂性，导致模型在处理多步骤推理时表现不佳。
2. 提出InfoSeek框架，通过双代理系统构建研究树，生成需要完整层次推理的问题，从而提升模型的推理能力。
3. 实验结果显示，基于InfoSeek训练的模型在BrowseComp-Plus基准上超越了更大规模的模型，展现出显著的性能提升。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越被期望能够处理超越简单事实查询的深度研究任务，这些任务需要将问题分解为子问题、协调多步推理，并从多种来源综合证据。我们将具有可验证答案的深度研究任务形式化为层次约束满足问题（HCSPs），与现有的单约束、多跳或平面CSP形式有根本区别。现有基准（如Natural Questions、HotpotQA）未能捕捉这种复杂性，而最近的合成数据集往往引入了捷径推理、知识泄漏或缺乏足够的结构深度。为了解决这一问题，我们提出了InfoSeek，一个可扩展的框架，用于合成复杂的深度研究任务。InfoSeek使用双代理系统从大规模网页递归构建研究树，将中间节点模糊化为有效的子问题，并将这些树转换为需要遍历完整层次的自然语言问题。实验表明，基于InfoSeek训练的模型在多个基准上表现优异。

## 🔬 方法详解

**问题定义**：本论文旨在解决深度研究任务的合成问题，现有方法在处理复杂推理时存在知识泄漏和结构深度不足的痛点。

**核心思路**：通过构建研究树的方式，将复杂问题分解为有效的子问题，并生成需要多层次推理的自然语言问题，以此提升模型的推理能力。

**技术框架**：InfoSeek框架采用双代理系统，首先从大规模网页中递归构建研究树，然后将树中的中间节点模糊化为子问题，最后将这些树转换为自然语言问题。

**关键创新**：InfoSeek的核心创新在于其层次约束满足问题（HCSPs）的形式化定义，区别于传统的单约束或平面CSP方法，能够更好地处理复杂的推理任务。

**关键设计**：在设计中，InfoSeek保留了中间步骤和检索标签等元信息，支持复合奖励设计和轨迹级探索等高级优化策略。

## 📊 实验亮点

在BrowseComp-Plus基准测试中，基于InfoSeek优化的3B LLM模型超越了更大规模的32B模型和轻量级商业API（如Gemini2.5-Flash），并且在性能上与更强大的API（如Gemini2.5-Pro）相当，展现出显著的性能优势。

## 🎯 应用场景

该研究的潜在应用领域包括教育、信息检索和智能问答系统等，能够帮助用户更高效地获取和整合信息，提升决策支持能力。未来，InfoSeek框架可能推动更复杂的推理任务的研究和应用，促进人工智能在深度理解和推理方面的进步。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly expected to go beyond simple factual queries toward Deep Research-tasks that require decomposing questions into sub-problems, coordinating multi-step reasoning, and synthesizing evidence from diverse sources. We formalize Deep Research tasks with verifiable answers as Hierarchical Constraint Satisfaction Problems (HCSPs), which are fundamentally different from single-constraint, multi-hop, or flat CSP formulations. However, existing benchmarks (e.g., Natural Questions, HotpotQA) fail to capture this complexity, while recent synthetic datasets often introduce shortcut reasoning, knowledge leakage, or lack sufficient structural depth. To address this gap, we introduce InfoSeek, a scalable framework for synthesizing complex Deep Research tasks. InfoSeek uses a dual-agent system to recursively build a Research Tree from large-scale webpages, blurring intermediate nodes into valid sub-problems, and converting these trees into natural language questions that require traversing the full hierarchy. It also enables rapid scaling, yielding over 50K training examples, a curated test set, and reasoning trajectories generated via reject sampling. Experiments show that models trained on InfoSeek consistently outperform strong baselines. On a challenging benchmark BrowseComp-Plus, 3B LLMs optimized with InfoSeek surpass much larger 32B models and lightweight commercial APIs (e.g., Gemini2.5-Flash), while achieving performance comparable to stronger APIs (e.g., Gemini2.5-Pro). By preserving meta-information such as intermediate steps and retrieval labels, InfoSeek further supports advanced optimization strategies, including compound reward design and trajectory-level exploration. We provide our codes and datasets in \href{https://github.com/VectorSpaceLab/InfoSeek}{this repository}.

