---
layout: default
title: Reducing Cognitive Overhead in Tool Use via Multi-Small-Agent Reinforcement Learning
---

# Reducing Cognitive Overhead in Tool Use via Multi-Small-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08882" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08882v4</a>
  <a href="https://arxiv.org/pdf/2508.08882.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08882v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08882v4', 'Reducing Cognitive Overhead in Tool Use via Multi-Small-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dayu Wang, Jiaye Yang, Weikang Li, Jiahui Liang, Yang Li

**分类**: cs.AI

**发布日期**: 2025-08-12 (更新: 2025-10-11)

---

## 💡 一句话要点

**提出MSARL框架以降低工具使用中的认知负担**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体系统` `强化学习` `工具使用` `认知负担` `推理解耦` `模仿学习` `自动化编程`

## 📋 核心要点

1. 现有的工具集成推理系统往往依赖单一大型模型，导致认知负担干扰和协调不稳定。
2. MSARL框架通过将推理与工具使用解耦，采用多个小型智能体协作，提升了系统的稳定性和准确性。
3. 在数学问题解决任务中，MSARL显著提高了推理稳定性和最终答案的准确率，相较于单智能体基线有明显提升。

## 📝 摘要（中文）

近年来，多智能体系统的进展突显了通过分工合作的专门小型智能体的潜力。然而，现有的工具集成推理系统通常遵循单智能体范式，这导致认知负担干扰和协调不稳定。本文提出了MSARL，一个多小型智能体强化学习框架，明确将推理与工具使用解耦。在MSARL中，推理智能体分解问题并规划工具调用，而多个工具智能体专注于特定外部工具，通过模仿学习和强化学习的组合进行训练，采用角色特定的奖励。在数学问题解决与代码执行的任务中，MSARL显著提高了推理的稳定性和最终答案的准确性。此外，该架构可推广到多种工具使用任务，展示了小型智能体的认知角色解耦是多智能体AI设计的可扩展蓝图。

## 🔬 方法详解

**问题定义**：本文旨在解决现有工具集成推理系统中因单一大型模型导致的认知负担干扰和协调不稳定的问题。现有方法在长时间推理和精确工具操作之间的交替使用上存在显著挑战。

**核心思路**：MSARL框架的核心思路是通过将推理与工具使用解耦，采用多个小型智能体进行协作。推理智能体负责问题分解和工具调用规划，而工具智能体则专注于特定工具的操作。

**技术框架**：MSARL的整体架构包括一个推理智能体和多个工具智能体。推理智能体负责分析问题并制定工具调用计划，工具智能体则通过模仿学习和强化学习进行训练，专注于各自的工具。

**关键创新**：MSARL的主要创新在于通过小型智能体的认知角色解耦，提升了系统的稳定性和准确性。这一设计与传统的单智能体方法本质上不同，后者往往在推理和工具操作之间难以有效协调。

**关键设计**：在MSARL中，工具智能体的训练结合了模仿学习和强化学习，采用角色特定的奖励机制，以确保每个智能体能够专注于其特定的工具操作。

## 📊 实验亮点

在数学问题解决与代码执行的实验中，MSARL框架显著提高了推理的稳定性和最终答案的准确性，相较于单智能体基线，准确率提升幅度达到XX%（具体数据未知）。

## 🎯 应用场景

该研究的潜在应用领域包括自动化编程、智能助手和复杂决策支持系统等。通过降低工具使用中的认知负担，MSARL能够提升多智能体系统在实际任务中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in multi-agent systems highlight the potential of specialized small agents that collaborate via division of labor. Existing tool-integrated reasoning systems, however, often follow a single-agent paradigm in which one large model interleaves long-horizon reasoning with precise tool operations, leading to cognitive-load interference and unstable coordination. We present MSARL, a Multi-Small-Agent Reinforcement Learning framework that explicitly decouples reasoning from tool use. In MSARL, a Reasoning Agent decomposes problems and plans tool invocations, while multiple Tool Agents specialize in specific external tools, each trained via a combination of imitation learning and reinforcement learning with role-specific rewards. On mathematical problem solving with code execution, MSARL significantly improves reasoning stability and final-answer accuracy over single-agent baselines. Moreover, the architecture generalizes to diverse tool-use tasks, demonstrating that cognitive-role decoupling with small agents is a scalable blueprint for multi-agent AI design.

