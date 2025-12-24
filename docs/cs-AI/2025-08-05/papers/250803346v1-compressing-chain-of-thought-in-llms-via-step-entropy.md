---
layout: default
title: Compressing Chain-of-Thought in LLMs via Step Entropy
---

# Compressing Chain-of-Thought in LLMs via Step Entropy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03346" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03346v1</a>
  <a href="https://arxiv.org/pdf/2508.03346.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03346v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03346v1', 'Compressing Chain-of-Thought in LLMs via Step Entropy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeju Li, Jianyuan Zhong, Ziyang Zheng, Xiangyu Wen, Zhijian Xu, Yingying Cheng, Fan Zhang, Qiang Xu

**分类**: cs.AI

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出基于步骤熵的链式思维压缩方法以提高LLM推理效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `链式思维` `步骤熵` `推理效率` `模型压缩` `强化学习` `自然语言处理` `深度学习`

## 📋 核心要点

1. 现有的链式思维方法在推理过程中产生大量冗余步骤，导致推理效率低下。
2. 本文提出了一种基于步骤熵的压缩框架，通过识别低熵步骤来减少冗余，优化推理过程。
3. 实验结果表明，80%的低熵步骤可以被有效修剪，且对最终答案的准确性影响微乎其微。

## 📝 摘要（中文）

大型语言模型（LLMs）在复杂推理任务中表现出色，但其链式思维（CoT）提示生成的推理过程冗长且存在显著冗余，导致推理成本增加和效率降低。本文提出了一种基于步骤熵的新型CoT压缩框架，该框架通过量化个别推理步骤的信息贡献来识别冗余。理论分析和大量实验证明，低熵步骤高度冗余，实验显示在DeepSeek-R1-7B、14B和Qwen3-8B上，80%的低熵中间步骤可以被修剪，且最终答案准确性仅有轻微下降。此外，提出的两阶段训练策略结合了监督微调（SFT）和群体相对策略优化（GRPO）强化学习，使LLMs能够在推理过程中自主学习生成压缩的CoTs，显著提高推理效率并严格保持准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在使用链式思维提示时产生的冗余推理步骤问题。现有方法在推理过程中往往生成冗长且低效的思维过程，导致推理成本增加和效率降低。

**核心思路**：论文的核心思路是利用步骤熵这一指标来量化推理步骤的信息贡献，从而识别并去除冗余步骤。通过理论分析和实验证明，低熵步骤通常具有较高的冗余性。

**技术框架**：整体架构包括两个主要阶段：第一阶段是通过步骤熵分析识别冗余步骤，第二阶段是结合监督微调和群体相对策略优化的强化学习，训练模型生成压缩的链式思维。

**关键创新**：最重要的技术创新在于提出了基于步骤熵的压缩框架，并通过两阶段训练策略使模型能够自主学习生成压缩的推理过程，这与传统的随机或高熵修剪方法有本质区别。

**关键设计**：在设计中，关键参数包括步骤熵的计算方法，损失函数的设置，以及在强化学习阶段如何有效地引入[SKIP]标记以实现推理步骤的压缩。具体的网络结构和训练流程也经过精心设计，以确保模型在压缩推理的同时保持准确性。

## 📊 实验亮点

实验结果显示，在DeepSeek-R1-7B、14B和Qwen3-8B模型上，80%的低熵中间步骤可以被有效修剪，且最终答案的准确性仅有轻微下降。这一发现与随机或高熵修剪方法形成鲜明对比，后者会严重影响推理性能，证明了本文方法的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、自动化推理工具以及各类需要高效推理的自然语言处理任务。通过提高推理效率，能够在实际应用中降低计算成本，提升用户体验，并为未来的LLM部署提供重要的理论支持和实践指导。

## 📄 摘要（原文）

> Large Language Models (LLMs) using Chain-of-Thought (CoT) prompting excel at complex reasoning but generate verbose thought processes with considerable redundancy, leading to increased inference costs and reduced efficiency. We introduce a novel CoT compression framework based on step entropy, a metric that quantifies the informational contribution of individual reasoning steps to identify redundancy. Through theoretical analysis and extensive empirical validation on mathematical reasoning benchmarks, we demonstrate that steps with low entropy are indeed highly redundant. Our experiments reveal that an astonishing 80\% of low-entropy intermediate steps can be pruned with minor degradation in the final answer accuracy across DeepSeek-R1-7B, 14B and Qwen3-8B. This finding sharply contrasts with random or high-entropy pruning, which severely impairs reasoning performance. Building on this, we propose a novel two-stage training strategy combining Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO) reinforcement learning. This approach enables LLMs to autonomously learn to generate compressed COTs during inference by strategically incorporating [SKIP] tokens. Our method significantly enhances LLM inference efficiency while rigorously preserving accuracy, offering profound implications for practical LLM deployment and a deeper understanding of reasoning structures.

