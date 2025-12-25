---
layout: default
title: "One Tool Is Enough: Reinforcement Learning for Repository-Level LLM Agents"
---

# One Tool Is Enough: Reinforcement Learning for Repository-Level LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20957" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20957v1</a>
  <a href="https://arxiv.org/pdf/2512.20957.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20957v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20957v1', 'One Tool Is Enough: Reinforcement Learning for Repository-Level LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaoxi Zhang, Yitong Duan, Yanzhi Zhang, Yiming Xu, Jiyan He, Yunfang Wu

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**RepoNavigator：基于强化学习的单工具LLM智能体，用于仓库级代码定位**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码定位` `大型语言模型` `强化学习` `软件仓库` `代码导航`

## 📋 核心要点

1. 现有方法在大型代码仓库中定位问题时，依赖多个工具，忽略代码执行逻辑，导致模型控制复杂。
2. RepoNavigator 采用单一的、执行感知的工具（跳转到符号定义），并通过强化学习进行端到端训练。
3. 实验结果表明，RepoNavigator 在仓库级问题定位上取得了 SOTA 性能，甚至超越了更大的模型和闭源模型。

## 📝 摘要（中文）

由于大型开源软件(OSS)仓库的规模和结构复杂性，定位需要修改的文件和函数极具挑战。现有基于大型语言模型(LLM)的方法通常将其视为仓库级检索任务，并依赖多个辅助工具，忽略了代码执行逻辑并使模型控制复杂化。我们提出了RepoNavigator，一个配备单一执行感知工具（跳转到被调用符号的定义）的LLM智能体。这种统一的设计反映了代码执行的实际流程，同时简化了工具操作。RepoNavigator通过强化学习(RL)直接从预训练模型进行端到端训练，无需任何闭源知识蒸馏。实验表明，经过RL训练的RepoNavigator实现了最先进的性能，7B模型优于14B基线模型，14B模型超越32B竞争对手，甚至32B模型超过了诸如Claude-3.7等闭源模型。这些结果证实，将单一的、结构化的工具与RL训练相结合，为仓库级问题定位提供了一种高效且可扩展的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决大型开源软件仓库中，难以快速准确地定位需要修改的文件和函数的问题。现有方法通常将此问题视为信息检索任务，依赖多个辅助工具，但这些工具忽略了代码的实际执行逻辑，导致模型控制复杂，效率低下。

**核心思路**：论文的核心思路是设计一个配备单一工具的LLM智能体，该工具能够模拟代码执行的实际流程，即跳转到被调用符号的定义。通过这种方式，智能体可以沿着代码的调用链逐步探索代码库，从而更有效地定位问题。

**技术框架**：RepoNavigator 的整体框架包括以下几个关键部分：首先，使用一个预训练的LLM作为基础模型。然后，设计一个单一的工具，即“跳转到定义”的功能，允许智能体在代码库中导航。最后，使用强化学习算法对智能体进行端到端训练，使其能够学会如何有效地使用该工具来解决问题。智能体通过观察代码库的状态、执行动作（跳转到定义），并根据是否成功定位问题获得奖励。

**关键创新**：最重要的创新点在于将问题定位任务简化为一个单一工具的强化学习问题。与现有方法依赖多个工具相比，这种方法更加简洁高效，并且能够更好地模拟代码执行的实际流程。此外，通过强化学习进行端到端训练，使得智能体能够自动学习如何有效地使用该工具，而无需人工设计复杂的规则或策略。

**关键设计**：RepoNavigator 的关键设计包括：1) 使用预训练的LLM作为基础模型，利用其强大的语言理解和代码生成能力。2) 设计单一的“跳转到定义”工具，简化工具操作，并模拟代码执行流程。3) 使用强化学习算法（具体算法未知）进行端到端训练，优化智能体的策略。4) 奖励函数的设计至关重要，需要能够有效地引导智能体学习如何定位问题。具体的参数设置、损失函数和网络结构等细节在论文中可能有所描述，但此处未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20957v1/navigator.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20957v1/navigator_main.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20957v1/qwen_ablation_rewards.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

RepoNavigator 通过强化学习训练，在仓库级问题定位任务上取得了显著的性能提升。7B 模型超越了 14B 的基线模型，14B 模型超越了 32B 的竞争对手，甚至 32B 模型超越了 Claude-3.7 等闭源模型。这些结果表明，单一工具结合强化学习是一种高效且可扩展的解决方案。

## 🎯 应用场景

RepoNavigator 有潜力应用于各种软件开发场景，例如代码维护、缺陷修复、代码审查和知识共享。它可以帮助开发人员快速定位代码库中的问题，提高开发效率，降低维护成本。此外，该研究思路也可以推广到其他领域，例如知识图谱推理和文档检索。

## 📄 摘要（原文）

> Locating the files and functions requiring modification in large open-source software (OSS) repositories is challenging due to their scale and structural complexity. Existing large language model (LLM)-based methods typically treat this as a repository-level retrieval task and rely on multiple auxiliary tools, which overlook code execution logic and complicate model control. We propose RepoNavigator, an LLM agent equipped with a single execution-aware tool-jumping to the definition of an invoked symbol. This unified design reflects the actual flow of code execution while simplifying tool manipulation. RepoNavigator is trained end-to-end via Reinforcement Learning (RL) directly from a pretrained model, without any closed-source distillation. Experiments demonstrate that RL-trained RepoNavigator achieves state-of-the-art performance, with the 7B model outperforming 14B baselines, the 14B model surpassing 32B competitors, and even the 32B model exceeding closed-source models such as Claude-3.7. These results confirm that integrating a single, structurally grounded tool with RL training provides an efficient and scalable solution for repository-level issue localization.

