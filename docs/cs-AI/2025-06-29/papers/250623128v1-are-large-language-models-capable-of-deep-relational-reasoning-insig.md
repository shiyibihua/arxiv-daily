---
layout: default
title: Are Large Language Models Capable of Deep Relational Reasoning? Insights from DeepSeek-R1 and Benchmark Comparisons
---

# Are Large Language Models Capable of Deep Relational Reasoning? Insights from DeepSeek-R1 and Benchmark Comparisons

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23128" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23128v1</a>
  <a href="https://arxiv.org/pdf/2506.23128.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23128v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23128v1', 'Are Large Language Models Capable of Deep Relational Reasoning? Insights from DeepSeek-R1 and Benchmark Comparisons')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chi Chiu So, Yueyue Sun, Jun-Min Wang, Siu Pang Yung, Anthony Wai Keung Loh, Chun Pong Chau

**分类**: cs.AI

**发布日期**: 2025-06-29

**备注**: 10 pages, 0 figures, accepted by 2025 IEEE international conference on artificial intelligence testing (AITest)

**🔗 代码/项目**: [GITHUB](https://github.com/kelvinhkcs/Deep-Relational-Reasoning)

---

## 💡 一句话要点

**评估大型语言模型在深层关系推理中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `深层关系推理` `逻辑推理` `基准任务` `推理能力`

## 📋 核心要点

1. 现有大型语言模型在处理复杂推理任务时面临显著挑战，尤其是在问题复杂性增加时表现不佳。
2. 论文通过设计一系列基准任务，评估并比较了三种前沿大型语言模型的推理能力，提出了DeepSeek-R1的独特策略。
3. 实验结果表明，DeepSeek-R1在多个任务中取得了最高的F1分数，但在复杂问题上仍存在推理不完整的问题。

## 📝 摘要（中文）

本文探讨大型语言模型（LLMs）在深层关系推理中的表现，评估了DeepSeek-R1、DeepSeek-V3和GPT-4o三种前沿模型在家谱和一般图推理任务中的推理能力。实验结果显示，DeepSeek-R1在多个任务和问题规模中均取得了最高的F1分数，展现出强大的逻辑推理和关系推断能力。然而，所有评估模型在问题复杂性增加时均表现不佳，主要受到令牌长度限制和输出结构不完整的影响。对DeepSeek-R1的长链思维响应的详细分析揭示了其独特的规划和验证策略，但也突显了推理不连贯或不完整的实例，强调了对LLMs内部推理动态的深入审查的必要性。本文还讨论了未来工作的关键方向，包括多模态推理的角色和推理失败的系统性检验。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在深层关系推理中的能力不足，尤其是在面对复杂推理任务时的表现不佳。现有方法在处理复杂问题时常常受到令牌长度限制和输出结构不完整的影响。

**核心思路**：论文提出通过设计一系列基准任务来评估和比较不同大型语言模型的推理能力，特别关注DeepSeek-R1的长链思维策略，以揭示其推理过程中的优缺点。

**技术框架**：整体架构包括任务设计、模型评估和结果分析三个主要模块。首先，设计了一系列家谱和图推理任务；其次，评估三种模型在这些任务上的表现；最后，分析模型的推理过程和结果。

**关键创新**：DeepSeek-R1在逻辑推理和关系推断方面展现出强大的能力，尤其是在多个任务中取得了最高的F1分数。其独特的规划和验证策略是与现有方法的本质区别。

**关键设计**：在模型设计中，DeepSeek-R1采用了长链思维的响应机制，尽管在复杂问题上仍存在推理不连贯的情况，但其整体结构和参数设置为推理提供了新的视角。具体的损失函数和网络结构细节尚未明确。

## 📊 实验亮点

实验结果显示，DeepSeek-R1在多个任务中均取得了最高的F1分数，表现出色。然而，所有模型在面对复杂问题时均显著下降，强调了推理能力的局限性。具体而言，DeepSeek-R1在某些任务中F1分数提升幅度达到了XX%，但在复杂任务中仍存在推理不完整的情况。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、知识图谱构建和复杂决策支持等。通过提升大型语言模型在深层关系推理中的能力，可以为多种实际应用提供更为准确和可靠的推理支持，推动人工智能在复杂任务中的应用价值。

## 📄 摘要（原文）

> How far are Large Language Models (LLMs) in performing deep relational reasoning? In this paper, we evaluate and compare the reasoning capabilities of three cutting-edge LLMs, namely, DeepSeek-R1, DeepSeek-V3 and GPT-4o, through a suite of carefully designed benchmark tasks in family tree and general graph reasoning. Our experiments reveal that DeepSeek-R1 consistently achieves the highest F1-scores across multiple tasks and problem sizes, demonstrating strong aptitude in logical deduction and relational inference. However, all evaluated models, including DeepSeek-R1, struggle significantly as problem complexity increases, largely due to token length limitations and incomplete output structures. A detailed analysis of DeepSeek-R1's long Chain-of-Thought responses uncovers its unique planning and verification strategies, but also highlights instances of incoherent or incomplete reasoning, calling attention to the need for deeper scrutiny into LLMs' internal inference dynamics. We further discuss key directions for future work, including the role of multimodal reasoning and the systematic examination of reasoning failures. Our findings provide both empirical insights and theoretical implications for advancing LLMs' reasoning abilities, particularly in tasks that demand structured, multi-step logical inference. Our code repository will be publicly available at https://github.com/kelvinhkcs/Deep-Relational-Reasoning.

