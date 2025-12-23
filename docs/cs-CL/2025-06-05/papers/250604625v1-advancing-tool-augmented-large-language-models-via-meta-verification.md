---
layout: default
title: Advancing Tool-Augmented Large Language Models via Meta-Verification and Reflection Learning
---

# Advancing Tool-Augmented Large Language Models via Meta-Verification and Reflection Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04625" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04625v1</a>
  <a href="https://arxiv.org/pdf/2506.04625.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04625v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04625v1', 'Advancing Tool-Augmented Large Language Models via Meta-Verification and Reflection Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyuan Ma, Jiayu Liu, Xianzhen Luo, Zhenya Huang, Qingfu Zhu, Wanxiang Che

**分类**: cs.CL

**发布日期**: 2025-06-05

**备注**: Accepted at the Research Track of KDD 2025

**DOI**: [10.1145/3711896.3736835](https://doi.org/10.1145/3711896.3736835)

---

## 💡 一句话要点

**提出Tool-MVR以解决工具利用能力不足的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `工具增强` `元验证` `反思学习` `错误修正` `系统2推理` `API调用`

## 📋 核心要点

1. 现有大型语言模型在工具规划和调用方面存在不可靠性，主要源于低质量的指令数据集和静态学习方式。
2. 本文提出Tool-MVR，通过多代理元验证和基于探索的反思学习，提升工具的规划、调用和反思能力。
3. 实验结果显示，Tool-MVR在多个基准测试中表现优异，超越了现有模型，并显著降低了API调用次数。

## 📝 摘要（中文）

赋能大型语言模型（LLMs）有效利用工具的能力对于使AI代理解决复杂问题至关重要。然而，当前模型面临两个主要限制：一是由于低质量指令数据集导致的工具规划和调用不可靠，二是静态模仿学习导致的工具反思能力弱。为了解决这些关键限制，本文提出了Tool-MVR，一个新颖的工具增强LLM，通过多代理元验证（MAMV）和基于探索的反思学习（EXPLORE）实现全面的系统2推理。实验表明，Tool-MVR在StableToolBench上超越了ToolLLM和GPT-4，并在RefineToolBench上实现了58.9%的错误修正率，显著提升了工具反思能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在工具利用中的不可靠性和反思能力不足的问题。现有方法面临低质量指令数据集导致的工具规划和调用不准确，以及静态模仿学习导致的反思能力弱，超过90%的错误无法纠正。

**核心思路**：论文提出Tool-MVR，通过引入多代理元验证（MAMV）和基于探索的反思学习（EXPLORE）来增强工具的利用能力。MAMV系统性地验证API、查询和推理轨迹，EXPLORE则通过动态的“错误->反思->纠正”学习范式来提升反思能力。

**技术框架**：Tool-MVR的整体架构包括两个主要模块：MAMV用于构建高质量的指令数据集ToolBench-V，EXPLORE用于生成反思数据集ToolBench-R。通过对开源LLM（如Qwen-7B）进行微调，Tool-MVR实现了全面的系统2推理能力。

**关键创新**：最重要的技术创新在于引入了系统化的多代理元验证和动态反思学习机制。这与现有方法的静态模仿学习形成鲜明对比，显著提升了工具的规划和反思能力。

**关键设计**：在设计中，MAMV采用了严格的验证流程，确保生成的指令数据集高质量；EXPLORE则通过反馈机制不断优化反思过程，提升了错误修正率。

## 📊 实验亮点

Tool-MVR在StableToolBench上超越了ToolLLM 23.9%和GPT-4 15.3%的性能，同时API调用次数减少了31.4%。在RefineToolBench上，Tool-MVR实现了58.9%的错误修正率，显著高于ToolLLM的9.1%。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化工具和复杂问题求解等。通过提升大型语言模型的工具利用能力，能够在更广泛的场景中实现更高效的任务执行，推动AI技术在实际应用中的落地与发展。

## 📄 摘要（原文）

> Empowering large language models (LLMs) with effective tool utilization capabilities is crucial for enabling AI agents to solve complex problems. However, current models face two major limitations: (1) unreliable tool planning and invocation due to low-quality instruction datasets (e.g., widespread hallucinated API calls), and (2) weak tool reflection abilities (over 90% of errors cannot be corrected) resulting from static imitation learning. To address these critical limitations, we propose Tool-MVR, a novel Tool-Augmented LLM that achieves comprehensive System 2 reasoning through two key innovations. Specifically, we first introduce Multi-Agent Meta-Verification (MAMV), a systematic pipeline that rigorously validates APIs, queries, and reasoning trajectories to construct ToolBench-V, a new high-quality instruction dataset that addresses the limitation of unreliable tool planning and invocation. Second, we propose Exploration-based Reflection Learning (EXPLORE), which enhances tool reflection capabilities by leveraging tool feedback through a dynamic "Error -> Reflection -> Correction" learning paradigm, resulting in our reflection dataset ToolBench-R and addressing the critical weakness in tool reflection. Finally, we obtain Tool-MVR by finetuning open-source LLMs (e.g., Qwen-7B) on both ToolBench-V and ToolBench-R. Our experiments demonstrate that Tool-MVR achieves state-of-the-art performance on StableToolBench, surpassing both ToolLLM (by 23.9%) and GPT-4 (by 15.3%) while reducing API calls by 31.4%, with strong generalization capabilities across unseen tools and scenarios. Additionally, on our proposed RefineToolBench, the first benchmark specifically designed to evaluate tool reflection capabilities, Tool-MVR achieves a 58.9% error correction rate, significantly outperforming ToolLLM's 9.1%.

