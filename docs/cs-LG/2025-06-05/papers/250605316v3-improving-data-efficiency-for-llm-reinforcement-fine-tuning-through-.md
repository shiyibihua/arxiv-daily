---
layout: default
title: Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay
---

# Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05316" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05316v3</a>
  <a href="https://arxiv.org/pdf/2506.05316.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05316v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05316v3', 'Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Sun, Jingyan Shen, Yibin Wang, Tianyu Chen, Zhendong Wang, Mingyuan Zhou, Huan Zhang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-05 (更新: 2025-10-28)

**备注**: Accepted at NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/ASTRAL-Group/data-efficient-llm-rl)

---

## 💡 一句话要点

**提出难度针对的在线数据选择与回放重放以提高LLM强化微调的数据效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `数据选择` `回放重放` `自适应难度` `大型语言模型`

## 📋 核心要点

1. 现有的LLM强化微调方法在数据效率上存在显著不足，导致资源消耗高且训练时间长。
2. 本文提出的难度针对的在线数据选择和回放重放技术，旨在通过自适应难度引导数据选择，优化学习信号的获取。
3. 实验结果显示，所提方法在6个LLM-数据集组合中将微调时间减少了23%至62%，且性能与原GRPO算法相当。

## 📝 摘要（中文）

强化学习（RL）已成为微调大型语言模型（LLM）的有效方法，尤其是在增强推理能力方面。然而，RL微调仍然高度依赖资源，现有研究在数据效率问题上关注不足。本文提出两种技术以提高LLM RL微调的数据效率：难度针对的在线数据选择和回放重放。我们引入自适应难度的概念来指导在线数据选择，优先选择中等难度的问题，以获取更具信息量的学习信号。为高效估计自适应难度，我们开发了一种基于注意力的框架，仅需对小型参考问题集进行回放。剩余问题的自适应难度则基于与该集的相似性进行估算。为进一步降低回放成本，我们引入了受传统RL中经验回放启发的回放重放机制，重用近期的回放，降低每步计算量，同时保持稳定更新。实验表明，我们的方法在6个LLM-数据集组合中将RL微调时间减少了23%至62%，同时达到与原GRPO算法相同的性能水平。

## 🔬 方法详解

**问题定义**：本文旨在解决LLM强化微调过程中的数据效率低下问题。现有方法往往忽视了如何有效选择数据，导致资源浪费和训练时间延长。

**核心思路**：论文提出通过自适应难度来指导在线数据选择，优先选择中等难度的问题，以获取更具信息量的学习信号。同时，采用回放重放机制以降低计算成本。

**技术框架**：整体架构包括两个主要模块：1）难度针对的在线数据选择模块，通过注意力机制估计问题的自适应难度；2）回放重放模块，重用近期的回放以降低每步计算量。

**关键创新**：最重要的创新在于引入自适应难度的概念和回放重放机制，这与传统的RL微调方法在数据选择和计算效率上有本质区别。

**关键设计**：在自适应难度估计中，使用小型参考集进行回放，剩余问题的难度通过与参考集的相似性进行估算。回放重放机制则通过重用近期的回放来降低计算开销。具体的参数设置和损失函数设计在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，所提出的方法在6个LLM-数据集组合中，微调时间减少了23%至62%，同时在性能上与原GRPO算法持平，展示了显著的效率提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能问答等。通过提高LLM的微调效率，可以加速模型的开发与部署，降低计算资源的需求，从而在实际应用中具有重要的经济价值和社会影响。

## 📄 摘要（原文）

> Reinforcement learning (RL) has become an effective approach for fine-tuning large language models (LLMs), particularly to enhance their reasoning capabilities. However, RL fine-tuning remains highly resource-intensive, and existing work has largely overlooked the problem of data efficiency. In this paper, we propose two techniques to improve data efficiency in LLM RL fine-tuning: difficulty-targeted online data selection and rollout replay. We introduce the notion of adaptive difficulty to guide online data selection, prioritizing questions of moderate difficulty that are more likely to yield informative learning signals. To estimate adaptive difficulty efficiently, we develop an attention-based framework that requires rollouts for only a small reference set of questions. The adaptive difficulty of the remaining questions is then estimated based on their similarity to this set. To further reduce rollout cost, we introduce a rollout replay mechanism inspired by experience replay in traditional RL. This technique reuses recent rollouts, lowering per-step computation while maintaining stable updates. Experiments across 6 LLM-dataset combinations show that our method reduces RL fine-tuning time by 23% to 62% while reaching the same level of performance as the original GRPO algorithm. Our code is available at https://github.com/ASTRAL-Group/data-efficient-llm-rl.

