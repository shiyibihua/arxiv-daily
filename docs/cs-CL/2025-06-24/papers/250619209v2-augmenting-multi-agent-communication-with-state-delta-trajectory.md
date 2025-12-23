---
layout: default
title: Augmenting Multi-Agent Communication with State Delta Trajectory
---

# Augmenting Multi-Agent Communication with State Delta Trajectory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19209" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19209v2</a>
  <a href="https://arxiv.org/pdf/2506.19209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19209v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19209v2', 'Augmenting Multi-Agent Communication with State Delta Trajectory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yichen Tang, Weihang Su, Yujia Zhou, Yiqun Liu, Min Zhang, Shaoping Ma, Qingyao Ai

**分类**: cs.CL

**发布日期**: 2025-06-24 (更新: 2025-09-24)

**备注**: 22 pages, 5 figures

---

## 💡 一句话要点

**提出状态增量轨迹以增强多智能体通信**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `状态增量编码` `推理逻辑` `自然语言处理` `信息传递` `复杂任务` `通信协议`

## 📋 核心要点

1. 现有多智能体系统主要使用自然语言进行通信，导致信息在传递过程中不可避免地损失，尤其是在复杂推理任务中。
2. 本文提出了一种新的通信协议，结合自然语言标记和状态转移轨迹，以更全面地传递信息，解决了信息损失的问题。
3. 实验结果显示，采用状态增量编码（SDE）的方法在多智能体系统中实现了SOTA性能，特别是在复杂推理任务上有显著提升。

## 📝 摘要（中文）

多智能体技术如角色扮演或多轮辩论已被证明能有效提升大型语言模型（LLMs）在下游任务中的表现。然而，现有的多智能体系统主要依赖自然语言进行通信，这在简洁性和可解释性上有优势，但也导致信息损失，尤其是在传递推理逻辑或抽象思想时。为了解决这一问题，本文提出了一种新的通信协议，能够同时传递自然语言标记和逐标记状态转移轨迹。我们发现，相较于实际状态值，LLMs在生成每个标记后的状态变化序列能更好地反映推理过程中的隐含信息。实验结果表明，采用状态增量编码（SDE）方法的多智能体系统在复杂推理任务中表现出色，达到了SOTA性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多智能体系统中因使用自然语言进行通信而导致的信息损失问题，尤其是在推理逻辑和抽象思想的传递上存在显著不足。

**核心思路**：提出了一种新的通信协议，允许智能体在传递信息时同时发送自然语言标记和状态转移轨迹，从而更全面地反映推理过程中的信息。

**技术框架**：整体架构包括两个主要模块：一是状态增量编码（SDE）模块，用于表示状态转移轨迹；二是通信模块，负责在智能体之间传递自然语言和状态信息。

**关键创新**：最重要的创新在于引入状态增量编码（SDE），通过捕捉状态变化序列来增强信息传递的有效性，这一方法与传统的单一自然语言传递方式本质上不同。

**关键设计**：在设计中，SDE模块采用了特定的参数设置，以确保状态转移的准确性，同时在损失函数中考虑了信息的完整性和推理的连贯性。

## 📊 实验亮点

实验结果表明，采用状态增量编码（SDE）的多智能体系统在复杂推理任务中达到了SOTA性能，相较于其他通信协议，性能提升幅度显著，具体数据未提供，但表明了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能对话系统、自动化推理和协作机器人等。通过增强多智能体之间的通信能力，可以提升系统在复杂任务中的表现，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Multi-agent techniques such as role playing or multi-turn debates have been shown to be effective in improving the performance of large language models (LLMs) in downstream tasks. Despite their differences in workflows, existing multi-agent systems constructed from a single base LLM mostly use natural language for agent communication. While this is appealing for its simplicity and interpretability, it also introduces inevitable information loss as one model must down sample its continuous state vectors to discrete tokens before transferring them to the other model. Such losses are particularly significant when the information to transfer is not simple facts, but reasoning logics or abstractive thoughts. To tackle this problem, we propose a new communication protocol that transfers both natural language tokens and token-wise state transition trajectory from one agent to another. Particularly, compared to the actual state value, we find that the sequence of state changes in LLMs after generating each token can better reflect the information hidden behind the inference process. We propose a State Delta Encoding (SDE) method to represent state transition trajectories. The experimental results show that multi-agent systems with SDE achieve SOTA performance compared to other communication protocols, particularly in tasks that involve complex reasoning.

