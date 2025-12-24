---
layout: default
title: Promoting Efficient Reasoning with Verifiable Stepwise Reward
---

# Promoting Efficient Reasoning with Verifiable Stepwise Reward

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10293" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10293v2</a>
  <a href="https://arxiv.org/pdf/2508.10293.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10293v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10293v2', 'Promoting Efficient Reasoning with Verifiable Stepwise Reward')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chuhuai Yue, Chengqi Dong, Yinan Gao, Hang He, Jiajun Chai, Guojun Yin, Wei Lin

**分类**: cs.AI

**发布日期**: 2025-08-14 (更新: 2025-08-16)

---

## 💡 一句话要点

**提出可验证的逐步奖励机制以解决推理模型过度思考问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `推理模型` `逐步奖励` `强化学习` `效率提升` `数学推理` `可验证机制` `计算资源`

## 📋 核心要点

1. 现有推理模型在简单问题上常常过度思考，导致计算效率低下。
2. 提出了一种基于规则的可验证逐步奖励机制，通过对中间状态的表现进行奖励，鼓励有效推理步骤。
3. 实验结果显示，该方法在保持推理性能的同时，显著减少了输出长度，提升了效率。

## 📝 摘要（中文）

大型推理模型（LRMs）在复杂推理任务中取得了显著进展，得益于可验证奖励的强化学习。然而，LRMs常常面临过度思考的问题，在简单问题上消耗过多计算资源，降低了效率。现有的高效推理方法通常需要准确的任务评估来预设令牌预算或选择推理模式，这限制了它们的灵活性和可靠性。本文提出了一种新颖的基于规则的可验证逐步奖励机制（VSRM），根据推理轨迹中间状态的表现分配奖励，从而有效抑制无效步骤，鼓励有效推理，显著提高了效率与准确性的平衡。实验结果表明，该方法在标准数学推理基准上实现了输出长度的显著减少，同时保持了原有的推理性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型推理模型在简单问题上过度思考的问题，现有方法依赖于准确的任务评估，导致灵活性不足。

**核心思路**：提出的可验证逐步奖励机制（VSRM）通过对推理过程中的中间状态进行奖励，鼓励有效步骤，抑制无效步骤，从而提高推理效率。

**技术框架**：该方法集成了VSRM与PPO和Reinforce++，在推理过程中动态评估中间状态的表现，形成一个反馈循环以优化推理策略。

**关键创新**：VSRM是本研究的核心创新点，它通过逐步奖励机制直接针对推理过程中的有效性进行优化，与传统方法相比，具有更高的灵活性和适应性。

**关键设计**：在实现中，VSRM设计了特定的奖励函数，结合了中间状态的表现评估，确保了奖励的及时性和准确性，同时优化了模型的训练过程。

## 📊 实验亮点

实验结果表明，采用VSRM后，模型在标准数学推理基准AIME24和AIME25上的输出长度显著减少，同时保持了推理性能，达到了效率与准确性的最佳平衡。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化推理系统和智能问答等。通过提高推理效率，能够在实际应用中节省计算资源，提升用户体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large reasoning models (LRMs) have recently achieved significant progress in complex reasoning tasks, aided by reinforcement learning with verifiable rewards. However, LRMs often suffer from overthinking, expending excessive computation on simple problems and reducing efficiency. Existing efficient reasoning methods typically require accurate task assessment to preset token budgets or select reasoning modes, which limits their flexibility and reliability. In this work, we revisit the essence of overthinking and identify that encouraging effective steps while penalizing ineffective ones is key to its solution. To this end, we propose a novel rule-based verifiable stepwise reward mechanism (VSRM), which assigns rewards based on the performance of intermediate states in the reasoning trajectory. This approach is intuitive and naturally fits the step-by-step nature of reasoning tasks. We conduct extensive experiments on standard mathematical reasoning benchmarks, including AIME24 and AIME25, by integrating VSRM with PPO and Reinforce++. Results show that our method achieves substantial output length reduction while maintaining original reasoning performance, striking an optimal balance between efficiency and accuracy. Further analysis of overthinking frequency and pass@k score before and after training demonstrates that our approach in deed effectively suppresses ineffective steps and encourages effective reasoning, fundamentally alleviating the overthinking problem. All code will be released upon acceptance.

