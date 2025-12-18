---
layout: default
title: Recursive Self-Aggregation Unlocks Deep Thinking in Large Language Models
---

# Recursive Self-Aggregation Unlocks Deep Thinking in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26626" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26626v1</a>
  <a href="https://arxiv.org/pdf/2509.26626.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26626v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26626v1', 'Recursive Self-Aggregation Unlocks Deep Thinking in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siddarth Venkatraman, Vineet Jain, Sarthak Mittal, Vedant Shah, Johan Obando-Ceron, Yoshua Bengio, Brian R. Bartoldson, Bhavya Kailkhura, Guillaume Lajoie, Glen Berseth, Nikolay Malkin, Moksh Jain

**分类**: cs.LG

**发布日期**: 2025-09-30

**备注**: 24 pages, 9 figures

**🔗 代码/项目**: [GITHUB](https://github.com/HyperPotatoNeo/RSA)

---

## 💡 一句话要点

**提出递归自聚合(RSA)方法，提升大语言模型在推理时的深度思考能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理` `递归自聚合` `测试时扩展` `强化学习`

## 📋 核心要点

1. 现有大语言模型推理方法在计算资源扩展时，要么并行选择多个独立解，要么串行进行自精炼，未能充分利用中间推理过程的信息。
2. RSA方法借鉴进化算法思想，通过递归地聚合候选推理链的子集，迭代优化推理过程，从而更有效地利用计算资源。
3. 实验表明，RSA在多种任务和模型上均能显著提升性能，尤其是在计算资源有限的情况下，能达到与更大模型相媲美的效果。

## 📝 摘要（中文）

本文提出了一种名为递归自聚合(RSA)的测试时扩展方法，该方法受到进化方法的启发，结合了并行和顺序扩展的优点，旨在提高大型语言模型(LLM)的性能。RSA的每个步骤都通过聚合子集来改进候选推理链的群体，从而产生改进的解决方案群体，然后将其用作下一次迭代的候选池。RSA利用推理链中嵌入的丰富信息（不仅仅是最终答案），并能够从不同思维链中部分正确的中间步骤进行引导。实验结果表明，RSA在不同的任务、模型系列和大小上，随着计算预算的增加，性能显著提高。值得注意的是，RSA使Qwen3-4B-Instruct-2507能够实现与更大的推理模型（包括DeepSeek-R1和o3-mini (high)）相媲美的性能，同时在AIME-25、HMMT-25、Reasoning Gym、LiveCodeBench-v6和SuperGPQA上优于纯粹的并行和顺序扩展策略。此外，我们还证明了通过一种新颖的聚合感知强化学习方法训练模型来组合解决方案可以产生显著的性能提升。代码可在https://github.com/HyperPotatoNeo/RSA获取。

## 🔬 方法详解

**问题定义**：现有的大语言模型在推理时，主要采用并行或串行的计算扩展方式。并行方法独立生成多个答案，然后选择最优解，但忽略了不同答案之间的关联信息。串行方法则通过自精炼逐步改进答案，但容易陷入局部最优。这两种方法都未能充分利用推理链中蕴含的丰富信息，尤其是在中间步骤中可能存在的有价值的线索。

**核心思路**：RSA的核心思路是借鉴进化算法的思想，将推理过程视为一个种群进化过程。通过不断地聚合和选择优秀的推理链，逐步提升整体的推理能力。RSA充分利用了推理链中的中间步骤信息，允许从部分正确的中间步骤中进行引导，从而避免陷入局部最优，并更有效地利用计算资源。

**技术框架**：RSA的整体框架包含以下几个主要步骤：1) 初始化：生成一组候选推理链，作为初始种群。2) 聚合：从种群中随机选择子集，并使用聚合函数将这些子集组合成新的推理链。聚合函数可以是简单的投票或更复杂的模型。3) 选择：根据某种评价指标（例如，模型置信度或外部验证）选择优秀的推理链，作为下一代种群。4) 迭代：重复步骤2和3，直到达到预定的迭代次数或满足停止条件。

**关键创新**：RSA的关键创新在于其递归自聚合的机制。与传统的并行或串行方法不同，RSA能够充分利用推理链中的中间步骤信息，并允许从不同的推理链中提取有用的线索。此外，RSA还引入了一种聚合感知强化学习方法，用于训练模型学习如何更好地组合不同的推理链，从而进一步提升性能。

**关键设计**：RSA的关键设计包括：1) 聚合函数的选择：可以使用简单的投票机制，也可以使用更复杂的模型，例如Transformer模型，来学习如何组合不同的推理链。2) 选择策略：可以使用基于模型置信度的选择策略，也可以使用外部验证来选择更可靠的推理链。3) 迭代次数：迭代次数决定了RSA的计算复杂度，需要根据具体的任务和计算资源进行调整。4) 聚合感知强化学习：使用强化学习来训练模型学习如何更好地组合不同的推理链，奖励函数可以基于最终答案的正确性或中间步骤的质量。

## 📊 实验亮点

实验结果表明，RSA在AIME-25、HMMT-25、Reasoning Gym、LiveCodeBench-v6和SuperGPQA等多个基准测试中均取得了显著的性能提升。例如，RSA使Qwen3-4B-Instruct-2507模型在某些任务上达到了与DeepSeek-R1和o3-mini (high)等更大模型相媲美的性能，同时优于纯粹的并行和顺序扩展策略。此外，通过聚合感知强化学习训练，RSA的性能得到了进一步提升。

## 🎯 应用场景

RSA方法可应用于各种需要深度推理的大语言模型应用场景，例如数学问题求解、代码生成、逻辑推理等。该方法尤其适用于计算资源受限的场景，能够以较低的成本提升模型的推理能力。未来，RSA有望成为一种通用的测试时扩展方法，并被广泛应用于各种大语言模型应用中。

## 📄 摘要（原文）

> Test-time scaling methods improve the capabilities of large language models (LLMs) by increasing the amount of compute used during inference to make a prediction. Inference-time compute can be scaled in parallel by choosing among multiple independent solutions or sequentially through self-refinement. We propose Recursive Self-Aggregation (RSA), a test-time scaling method inspired by evolutionary methods that combines the benefits of both parallel and sequential scaling. Each step of RSA refines a population of candidate reasoning chains through aggregation of subsets to yield a population of improved solutions, which are then used as the candidate pool for the next iteration. RSA exploits the rich information embedded in the reasoning chains -- not just the final answers -- and enables bootstrapping from partially correct intermediate steps within different chains of thought. Empirically, RSA delivers substantial performance gains with increasing compute budgets across diverse tasks, model families and sizes. Notably, RSA enables Qwen3-4B-Instruct-2507 to achieve competitive performance with larger reasoning models, including DeepSeek-R1 and o3-mini (high), while outperforming purely parallel and sequential scaling strategies across AIME-25, HMMT-25, Reasoning Gym, LiveCodeBench-v6, and SuperGPQA. We further demonstrate that training the model to combine solutions via a novel aggregation-aware reinforcement learning approach yields significant performance gains. Code available at https://github.com/HyperPotatoNeo/RSA.

