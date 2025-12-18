---
layout: default
title: Learning to Reason with Mixture of Tokens
---

# Learning to Reason with Mixture of Tokens

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21482" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21482v1</a>
  <a href="https://arxiv.org/pdf/2509.21482.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21482v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21482v1', 'Learning to Reason with Mixture of Tokens')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adit Jain, Brendan Rappazzo

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-25

**备注**: 30 page

---

## 💡 一句话要点

**提出混合Token生成方法，提升LLM在可验证奖励强化学习中的推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `推理能力` `混合Token生成` `可验证奖励`

## 📋 核心要点

1. 现有基于可验证奖励强化学习的LLM推理方法忽略了模型概率分布中的丰富信息，限制了推理搜索空间。
2. 提出混合Token生成（MoT-G）方法，在强化学习中利用token的混合表示，扩展了推理的搜索空间。
3. 实验表明，MoT-G方法在推理任务上取得了显著提升，并提高了训练效率，减少了所需的轨迹数量。

## 📝 摘要（中文）

本文研究了在可验证奖励强化学习（RLVR）中利用混合Token生成（MoT-G）方法来提升大型语言模型（LLM）的推理能力。现有方法通常基于Group Relative Policy Optimization，通过采样多个推理过程，相互评分并调整策略。但这些方法在每一步推理中都采样离散的token，忽略了模型概率分布中丰富的分布信息。本文提出了一个统一的框架，推广了现有的MoT-G方法，并扩展了RLVR，使其可以直接在连续混合空间中生成思维链。在Reasoning-Gym上的评估表明，MoT-G方法在10个任务中的7个上取得了显著的改进（5-35%的增益），同时使用一半的轨迹数量就达到了与标准解码相当的精度，表明训练效率得到了提高。通过全面的隐藏状态和token级别分析，证明MoT-G的优势可能源于其在整个推理过程中保持更高的隐藏状态熵和促进token空间探索的能力。

## 🔬 方法详解

**问题定义**：现有基于可验证奖励强化学习（RLVR）的方法，如Group Relative Policy Optimization，在生成推理链时，每一步都只采样一个离散的token。这种做法忽略了模型在每个token上的概率分布信息，导致搜索空间受限，可能错过更优的推理路径。现有方法的痛点在于无法有效利用模型提供的全部信息，导致推理效率和准确性不高。

**核心思路**：本文的核心思路是利用混合Token生成（MoT-G）方法，不再局限于采样单个token，而是将多个token的embedding进行加权混合，形成一个连续的混合表示。这样可以保留模型在每个token上的概率分布信息，扩展搜索空间，从而找到更优的推理路径。这样设计的目的是为了克服现有方法的信息损失问题，更充分地利用模型的能力。

**技术框架**：本文提出了一个统一的MoT-G框架，该框架可以概括现有的MoT-G方法，包括那些无需训练的方法，这些方法将混合嵌入构建为token嵌入的加权和。该框架扩展了RLVR，使其可以直接在连续混合空间中生成思维链。整体流程包括：1）使用LLM生成token的概率分布；2）根据概率分布对token的embedding进行加权混合，生成混合token表示；3）使用混合token表示进行推理；4）使用RLVR对策略进行优化。

**关键创新**：最重要的技术创新点在于将混合token生成方法引入到可验证奖励强化学习中。与现有方法只采样单个token不同，MoT-G方法利用了token的概率分布信息，生成混合token表示，从而扩展了搜索空间，提高了推理的效率和准确性。本质区别在于，现有方法是离散的token采样，而MoT-G方法是连续的混合表示。

**关键设计**：关键设计包括：1）混合权重计算方法：可以使用模型输出的概率分布作为权重，也可以使用其他方法计算权重。2）奖励函数设计：需要设计合适的奖励函数来指导模型学习如何生成更有效的混合token表示。3）模型架构：可以使用现有的LLM模型，只需要修改token生成部分，使其支持混合token生成。

## 📊 实验亮点

实验结果表明，MoT-G方法在Reasoning-Gym的10个任务中的7个上取得了显著的改进（5-35%的增益），与标准解码相比，使用一半的轨迹数量就达到了相当的精度，表明训练效率得到了提高。这表明MoT-G方法能够更有效地利用模型的信息，提高推理的效率和准确性。

## 🎯 应用场景

该研究成果可应用于各种需要复杂推理的自然语言处理任务，例如问答系统、对话系统、知识图谱推理等。通过提升LLM的推理能力，可以提高这些应用的性能和可靠性，使其能够更好地理解和解决复杂问题。未来，该方法还可以应用于其他领域，例如机器人控制、自动驾驶等，提升智能系统的决策能力。

## 📄 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has become a leading approach for improving large language model (LLM) reasoning capabilities. Most current methods follow variants of Group Relative Policy Optimization, which samples multiple reasoning completions, scores them relative to each other, and adjusts the policy accordingly. However, these approaches invariably sample discrete tokens at each reasoning step, discarding the rich distributional information in the model's probability distribution over candidate tokens. While preserving and utilizing this distributional information has proven beneficial in non-RL settings, current RLVR methods seem to be unnecessarily constraining the reasoning search space by not using this information. To address this limitation, we investigate mixture-of-token generation (MoT-G) in RLVR. We present a unified framework that generalizes existing MoT-G approaches, including existing training-free methods that construct mixture embeddings as weighted sums over token embeddings, and extend RLVR to operate directly in this continuous mixture space for generating chain-of-thought. Evaluating two MoT-G variants on Reasoning-Gym, a suite of reasoning-intensive language tasks, we find that MoT--G methods achieve substantial improvements (5--35 \% gains on 7 out of 10 tasks) compared to standard decoding with the Qwen2.5-1.5B model, while reaching comparable accuracy with half the number of trajectories, suggesting improved training efficiency. Through comprehensive hidden-state and token-level analyses, we provide evidence that MoT--G's benefits may stem from its ability to maintain higher hidden-state entropy throughout the reasoning process and promote exploration in token space.

