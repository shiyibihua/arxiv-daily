---
layout: default
title: Token Constraint Decoding Improves Robustness on Question Answering for Large Language Models
---

# Token Constraint Decoding Improves Robustness on Question Answering for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09408" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09408v1</a>
  <a href="https://arxiv.org/pdf/2506.09408.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09408v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09408v1', 'Token Constraint Decoding Improves Robustness on Question Answering for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jui-Ming Yao, Hao-Yuan Chen, Zi-Xian Tang, Bing-Jia Tan, Sheng-Wei Peng, Bing-Cheng Xie, Shun-Feng Su

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出Token约束解码以提升大语言模型的问答鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `问答系统` `鲁棒性` `Token约束解码` `输入噪声` `模型无关` `性能提升`

## 📋 核心要点

1. 现有的大语言模型在面对输入噪声时表现出高度脆弱性，导致问答性能显著下降。
2. 本文提出Token约束解码（TCD），通过强制对齐token级预测来提升模型在噪声环境中的鲁棒性。
3. 实验结果表明，TCD与提示工程结合使用时，能够为较弱模型带来高达39%的性能提升，显著改善了问答效果。

## 📝 摘要（中文）

大语言模型（LLMs）在多选题问答（MCQA）基准测试中表现出色，但对输入微小扰动高度敏感。本文提出并评估了Token约束解码（TCD），这一简单而有效的推理时算法通过强制对齐token级预测来增强在噪声环境中的鲁棒性。通过在CommonsenseQA、MMLU和MMLU-Pro上的广泛实验，我们展示了TCD，尤其是与提示工程（PE）结合时，显著恢复了因输入噪声而下降的性能，为较弱模型如Gemma3 1B带来了高达39%的绝对增益。惩罚扫掠分析进一步揭示TCD隐式正则化了过于自信的输出，不同模型需要不同的惩罚调度以最大化鲁棒性。我们的研究确立了TCD作为一种实用的、模型无关的方法，以提高在现实世界缺陷下的推理稳定性，为LLMs在安全关键或用户面对的应用中的可靠部署铺平了道路。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在多选题问答中对输入微小扰动的脆弱性，现有方法在噪声环境下表现不佳，导致性能下降。

**核心思路**：论文提出Token约束解码（TCD），通过在推理阶段强制对齐token级预测，从而增强模型在噪声条件下的鲁棒性。这样的设计旨在减少模型对输入扰动的敏感性，提高问答的稳定性。

**技术框架**：TCD的整体架构包括输入处理、token预测对齐和输出生成三个主要模块。在输入处理阶段，模型接收经过扰动的输入；在token预测对齐阶段，TCD通过约束机制确保生成的token之间的一致性；最后，在输出生成阶段，模型基于对齐后的token生成最终答案。

**关键创新**：TCD的主要创新在于其模型无关性和简单性，能够适用于不同的语言模型，并且通过对token级别的约束来提升鲁棒性，这与传统方法的处理方式有本质区别。

**关键设计**：在TCD中，设计了特定的惩罚调度策略，以适应不同模型的需求。此外，损失函数的设计也考虑了对过于自信输出的正则化，从而提高了模型的整体表现。通过惩罚机制，模型能够在面对噪声时保持更好的输出稳定性。

## 📊 实验亮点

实验结果显示，TCD在CommonsenseQA、MMLU和MMLU-Pro上显著提升了模型性能，尤其是对于较弱模型Gemma3 1B，性能提升高达39%。此外，惩罚扫掠分析表明，TCD有效地正则化了过于自信的输出，增强了模型的鲁棒性。

## 🎯 应用场景

该研究的潜在应用场景包括安全关键的问答系统、用户交互式应用以及需要高鲁棒性的自然语言处理任务。通过提升大语言模型在噪声环境下的稳定性，TCD能够为实际应用提供更可靠的支持，尤其是在用户体验和安全性至关重要的领域。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated impressive performance on multiple-choice question answering (MCQA) benchmarks, yet they remain highly vulnerable to minor input perturbations. In this paper, we introduce and evaluate Token Constraint Decoding (TCD). This simple yet effective inference-time algorithm enforces alignment between token-level predictions to enhance robustness in noisy settings. Through extensive experiments on CommonsenseQA, MMLU, and MMLU-Pro, we show that TCD, especially when paired with prompt engineering (PE) fixes, significantly restores performance degraded by input noise, yielding up to +39\% absolute gains for weaker models like Gemma3 1B. Penalty sweep analyses further reveal that TCD implicitly regularizes overconfident outputs, with different models requiring distinct penalty schedules to maximize resilience. Our findings establish TCD as a practical, model-agnostic approach for improving reasoning stability under real-world imperfections and pave the way for more reliable deployment of LLMs in safety-critical or user-facing applications.

