---
layout: default
title: "CricBench: A Multilingual Benchmark for Evaluating LLMs in Cricket Analytics"
---

# CricBench: A Multilingual Benchmark for Evaluating LLMs in Cricket Analytics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21877" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21877v1</a>
  <a href="https://arxiv.org/pdf/2512.21877.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21877v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21877v1', 'CricBench: A Multilingual Benchmark for Evaluating LLMs in Cricket Analytics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vaibhav Devraj, Dhruv Kumar, Jagat Sesh Challa

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-26

**备注**: Under Review

---

## 💡 一句话要点

**CricBench：一个用于评估LLM在板球分析中性能的多语言基准测试**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `板球分析` `大型语言模型` `Text-to-SQL` `多语言基准测试` `领域特定任务`

## 📋 核心要点

1. 现有方法难以满足板球分析中对领域知识、复杂模式和多语言支持的需求，导致LLM在特定领域的应用受限。
2. CricBench通过与领域专家合作，构建包含英语和印地语的板球数据基准测试，用于评估LLM在特定领域的Text-to-SQL能力。
3. 实验结果表明，通用基准测试的高性能不能保证在特定领域成功，且代码混合的印地语查询有时优于英语查询。

## 📝 摘要（中文）

板球是全球第二受欢迎的运动，拥有超过25亿的庞大粉丝群体。爱好者和分析师经常寻求高级统计见解，例如长期历史表现趋势或复杂的球员比较，这些信息通常无法通过标准网络搜索获得。虽然大型语言模型（LLM）在Text-to-SQL任务中取得了显著进展，但它们处理特定领域细微差别、复杂模式变化以及体育分析固有的多语言需求的能力仍未得到充分探索。为了研究这种潜在的能力差距，我们提出了CricBench，这是一个全面的基准测试套件，用于评估LLM在专业板球数据上的表现。为了构建“黄金标准”数据集，我们与板球和SQL领域的专家合作，手动编写复杂的查询，确保逻辑正确性。考虑到语言多样性，我们构建了英语和印地语两种语言的基准，建立了一个开放的框架，可以进一步扩展到其他区域语言。我们使用严格的评估协议评估了六个最先进的模型，包括GPT-4o、Claude 3.7 Sonnet和开源模型。我们的结果表明，在通用基准测试中的高性能并不能保证在特定领域取得成功。虽然开源推理模型DeepSeek R1实现了最先进的性能（50.6%），超过了Claude 3.7 Sonnet（47.7%）和GPT-4o（33.7%）等专有巨头，但从通用基准测试（BIRD）转移到CricBench时，其准确性仍然显著下降。此外，我们观察到，与英语相比，代码混合的印地语查询通常会产生同等或更高的准确性，这挑战了英语是专业SQL任务的最佳提示语言的假设。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM在板球分析这一特定领域，尤其是在处理复杂查询、领域知识和多语言需求方面的不足。现有方法在处理板球领域特有的数据模式、术语和多语言查询时表现不佳，通用基准测试无法充分评估LLM在这些方面的能力。

**核心思路**：论文的核心思路是构建一个专门针对板球分析的多语言基准测试数据集CricBench，该数据集包含复杂的手工编写的SQL查询，涵盖了板球领域的各种统计分析需求，并支持英语和印地语两种语言。通过在该数据集上评估LLM的性能，可以更准确地了解LLM在特定领域的Text-to-SQL能力。

**技术框架**：CricBench的构建流程主要包括以下几个阶段：1) 与板球领域专家合作，确定需要评估的查询类型和难度；2) 手动编写复杂的SQL查询，确保逻辑正确性和覆盖范围；3) 将查询翻译成印地语，并进行代码混合，以模拟真实场景；4) 构建评估框架，用于自动评估LLM生成的SQL查询的准确性。

**关键创新**：CricBench的关键创新在于：1) 它是第一个专门针对板球分析的多语言基准测试数据集；2) 它包含了复杂的手工编写的SQL查询，涵盖了板球领域的各种统计分析需求；3) 它支持英语和印地语两种语言，并进行了代码混合，更贴近实际应用场景。

**关键设计**：CricBench的关键设计包括：1) 与领域专家合作，确保数据集的质量和相关性；2) 手动编写SQL查询，避免了自动生成数据可能存在的偏差；3) 使用严格的评估协议，确保评估结果的可靠性；4) 考虑了语言多样性，支持英语和印地语两种语言。

## 📊 实验亮点

实验结果表明，DeepSeek R1在CricBench上取得了50.6%的准确率，超过了Claude 3.7 Sonnet (47.7%)和GPT-4o (33.7%)等专有模型。同时，实验还发现，代码混合的印地语查询有时会产生比英语查询更高的准确率，这挑战了英语是专业SQL任务最佳提示语言的假设。

## 🎯 应用场景

CricBench的研究成果可应用于开发更智能的体育数据分析系统，帮助板球爱好者、分析师和教练员更好地理解比赛数据，制定更有效的策略。该基准测试也可用于评估和改进LLM在其他特定领域的Text-to-SQL能力，推动LLM在各行各业的应用。

## 📄 摘要（原文）

> Cricket is the second most popular sport globally, commanding a massive following of over 2.5 billion fans globally. Enthusiasts and analysts frequently seek advanced statistical insights, such as long-term historical performance trends or complex player comparisons, that are often unavailable through standard web searches. While Large Language Models (LLMs) have advanced significantly in Text-to-SQL tasks, their capability to handle the domain-specific nuances, complex schema variations, and multilingual requirements inherent to sports analytics remains under-explored. To investigate this potential capability gap, we present CricBench, a comprehensive benchmark suite for evaluating LLMs on specialized cricket data. To curate a "Gold Standard" dataset, we collaborate with domain experts in cricket and SQL to manually author complex queries, ensuring logical correctness. Recognizing linguistic diversity, we construct the benchmark in both English and Hindi, establishing a framework that is open for further extension to other regional languages. We evaluate six state-of-the-art models, including GPT-4o, Claude 3.7 Sonnet, and open-source models, using a strict evaluation protocol. Our results reveal that high performance on general benchmarks does not guarantee success in specialized domains. While the open-weights reasoning model DeepSeek R1 achieves state-of-the-art performance (50.6%), surpassing proprietary giants like Claude 3.7 Sonnet (47.7%) and GPT-4o (33.7%), it still exhibits a significant accuracy drop when moving from general benchmarks (BIRD) to CricBench. Furthermore, we observe that code-mixed Hindi queries frequently yield parity or higher accuracy compared to English, challenging the assumption that English is the optimal prompt language for specialized SQL tasks.

