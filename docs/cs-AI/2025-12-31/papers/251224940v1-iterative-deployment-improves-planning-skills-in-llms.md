---
layout: default
title: Iterative Deployment Improves Planning Skills in LLMs
---

# Iterative Deployment Improves Planning Skills in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24940" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24940v1</a>
  <a href="https://arxiv.org/pdf/2512.24940.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24940v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24940v1', 'Iterative Deployment Improves Planning Skills in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Augusto B. Corrêa, Yoav Gelberg, Luckeciano C. Melo, Ilia Shumailov, André G. Pereira, Yarin Gal

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**迭代部署提升大型语言模型在规划任务中的能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `迭代部署` `强化学习` `规划任务` `泛化能力`

## 📋 核心要点

1. 现有LLM在复杂规划任务中面临泛化能力不足的挑战，难以发现长程依赖关系。
2. 论文提出迭代部署方法，通过用户筛选数据微调模型，隐式地进行强化学习。
3. 实验表明，迭代部署能显著提升LLM的规划能力，涌现出更强的泛化能力。

## 📝 摘要（中文）

本文提出了一种迭代部署大型语言模型（LLM）的方法，通过让用户精心筛选先前模型部署产生的数据，并以此微调后续模型，从而显著改变模型的属性。在多个规划领域进行的测试表明，这种机制可以大幅提升模型的规划能力，后续模型能够涌现出更强的泛化能力，发现比初始模型更长的计划。进一步的理论分析表明，迭代部署实际上在外部循环中实现了强化学习（RL）训练，并带有一个隐式的奖励函数。与强化学习的这种联系具有两个重要意义：首先，对于人工智能安全领域，由于重复部署所带来的奖励函数没有被明确定义，可能会对未来模型部署的属性产生意想不到的影响。其次，本文强调的这种机制可以被视为一种替代显式强化学习的训练方式，它依赖于数据管理而非显式奖励。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在复杂规划任务中表现出的泛化能力不足的问题。现有的方法通常依赖于预训练数据或显式的强化学习奖励，但前者难以覆盖所有可能的规划场景，后者则需要精心设计的奖励函数，这在复杂任务中往往难以实现。因此，如何让LLM在没有明确奖励信号的情况下，通过与环境的交互逐步提升规划能力是一个关键挑战。

**核心思路**：论文的核心思路是利用迭代部署的方式，让用户扮演“环境”的角色，通过筛选和反馈LLM生成的计划，隐式地提供奖励信号。具体来说，每次部署后，用户会选择表现良好的计划，并用这些数据微调下一个版本的LLM。通过多次迭代，LLM逐渐学会生成更符合用户期望的计划。这种方法避免了显式定义奖励函数的困难，而是通过数据驱动的方式，让LLM自动学习规划策略。

**技术框架**：整体框架包含以下几个主要步骤：1. 初始LLM部署：首先，使用一个预训练的LLM作为起点。2. 计划生成：LLM根据给定的规划任务生成多个候选计划。3. 用户筛选：用户根据一定的标准（例如计划的长度、可行性等）筛选出表现良好的计划。4. 模型微调：使用用户筛选出的数据对LLM进行微调，得到下一个版本的LLM。5. 迭代部署：重复步骤2-4，直到达到预期的性能。

**关键创新**：该论文最重要的技术创新在于将迭代部署与强化学习联系起来，证明迭代部署实际上在外部循环中实现了一种隐式的强化学习过程。这种方法避免了显式定义奖励函数的困难，而是通过用户筛选数据的方式，让LLM自动学习规划策略。此外，论文还观察到，通过迭代部署，LLM能够涌现出更强的泛化能力，发现比初始模型更长的计划。

**关键设计**：论文的关键设计在于用户筛选数据的标准和微调策略。用户需要根据具体的规划任务，制定合理的筛选标准，例如计划的长度、可行性、效率等。微调策略则需要根据LLM的类型和数据量进行调整，例如学习率、batch size、训练轮数等。此外，论文还探讨了不同用户筛选策略对模型性能的影响，例如只选择最优计划、选择多个较好计划等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24940v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24940v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，通过迭代部署，LLM在多个规划领域都取得了显著的性能提升。例如，在某些任务中，迭代后的LLM能够发现比初始模型长数倍的计划。此外，实验还表明，迭代部署能够使LLM涌现出更强的泛化能力，能够适应不同的规划场景。

## 🎯 应用场景

该研究成果可应用于各种需要复杂规划能力的场景，如机器人导航、任务调度、游戏AI等。通过迭代部署，可以使LLM在没有明确奖励信号的情况下，逐步提升规划能力，从而降低开发成本和难度。此外，该方法还可以用于探索LLM的涌现能力，发现新的规划策略和算法。

## 📄 摘要（原文）

> We show that iterative deployment of large language models (LLMs), each fine-tuned on data carefully curated by users from the previous models' deployment, can significantly change the properties of the resultant models. By testing this mechanism on various planning domains, we observe substantial improvements in planning skills, with later models displaying emergent generalization by discovering much longer plans than the initial models. We then provide theoretical analysis showing that iterative deployment effectively implements reinforcement learning (RL) training in the outer-loop (i.e. not as part of intentional model training), with an implicit reward function. The connection to RL has two important implications: first, for the field of AI safety, as the reward function entailed by repeated deployment is not defined explicitly, and could have unexpected implications to the properties of future model deployments. Second, the mechanism highlighted here can be viewed as an alternative training regime to explicit RL, relying on data curation rather than explicit rewards.

