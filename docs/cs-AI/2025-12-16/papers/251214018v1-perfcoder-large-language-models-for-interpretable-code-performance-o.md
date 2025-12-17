---
layout: default
title: PerfCoder: Large Language Models for Interpretable Code Performance Optimization
---

# PerfCoder: Large Language Models for Interpretable Code Performance Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14018" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14018v1</a>
  <a href="https://arxiv.org/pdf/2512.14018.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14018v1" onclick="toggleFavorite(this, '2512.14018v1', 'PerfCoder: Large Language Models for Interpretable Code Performance Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiuding Yang, Shengyao Lu, Hongxuan Liu, Shayan Shirahmad Gale Bagi, Zahra Fazel, Tomasz Czajkowski, Di Niu

**分类**: cs.SE, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**PerfCoder：基于大语言模型的可解释代码性能优化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码性能优化` `大语言模型` `强化学习` `可解释性` `代码生成`

## 📋 核心要点

1. 现有大语言模型在生成高性能代码方面存在不足，缺乏有效指导性能改进的监督信号。
2. PerfCoder通过在优化轨迹上微调LLM，并使用运行时测量进行强化学习，实现可解释的代码性能优化。
3. 实验表明，PerfCoder在代码性能基准测试中超越现有模型，并能提升更大规模LLM的优化能力。

## 📝 摘要（中文）

大语言模型（LLM）在自动代码生成方面取得了显著进展，但其生成高性能代码的能力仍然有限，这在实际软件系统中至关重要。我们认为，当前LLM的不足不仅在于数据稀缺，更重要的是缺乏指导可解释且有效的性能改进的监督。本文提出了PerfCoder，一个专门设计用于通过可解释的、定制的优化从源代码生成性能增强代码的LLM家族。PerfCoder在一个包含人类可读注释的真实优化轨迹集合上进行微调，并通过使用运行时测量的强化微调进行偏好对齐，使其能够提出特定于输入的改进策略并直接应用它们，而无需依赖迭代细化。在PIE代码性能基准测试中，PerfCoder在运行时加速和有效优化率方面均超过了所有现有模型，表明性能优化不能仅通过规模来实现，还需要优化策略意识。此外，PerfCoder可以生成关于源代码的可解释反馈，当作为输入提供给更大的LLM时，可以在规划器和优化器协同工作流程中进一步改善结果。具体来说，我们将32B模型和GPT-5在代码优化方面的性能提升到了新的水平，大大超过了它们原来的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型在代码生成中，难以生成高性能代码的问题。现有方法要么依赖数据规模，要么缺乏对代码性能优化的明确指导，导致生成的代码效率低下。

**核心思路**：PerfCoder的核心思路是通过学习真实世界的代码优化轨迹，使LLM具备可解释的性能优化能力。通过提供人类可读的优化注释和运行时测量反馈，引导模型学习有效的优化策略。

**技术框架**：PerfCoder的训练框架包含两个主要阶段：首先，在包含代码优化轨迹和对应注释的数据集上进行微调，使模型学习优化策略。然后，使用运行时测量作为奖励信号，通过强化学习对模型进行偏好对齐，使其能够生成更高效的代码。

**关键创新**：PerfCoder的关键创新在于其训练数据的构建和强化学习策略。通过收集真实世界的优化轨迹，并提供可解释的注释，模型能够学习到人类专家的优化经验。使用运行时测量作为奖励信号，能够直接优化代码的实际性能。

**关键设计**：PerfCoder使用了标准的Transformer架构作为基础模型。在微调阶段，使用了交叉熵损失函数来学习优化轨迹。在强化学习阶段，使用了PPO算法来优化模型的策略，奖励函数基于代码的运行时性能。

## 📊 实验亮点

PerfCoder在PIE代码性能基准测试中，运行时加速和有效优化率均超越了所有现有模型，证明了其优化策略的有效性。此外，PerfCoder生成的可解释反馈可以提升32B模型和GPT-5在代码优化方面的性能，显著超越其原始性能。

## 🎯 应用场景

PerfCoder可应用于各种软件开发场景，例如自动代码优化、编译器优化、以及为开发者提供代码性能改进建议。该研究有助于提升软件系统的性能和效率，并降低开发和维护成本。未来，该技术可能被集成到IDE或CI/CD流程中，实现自动化性能优化。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved remarkable progress in automatic code generation, yet their ability to produce high-performance code remains limited--a critical requirement in real-world software systems. We argue that current LLMs struggle not only due to data scarcity but, more importantly, because they lack supervision that guides interpretable and effective performance improvements. In this work, we introduce PerfCoder, a family of LLMs specifically designed to generate performance-enhanced code from source code via interpretable, customized optimizations. PerfCoder is fine-tuned on a curated collection of real-world optimization trajectories with human-readable annotations, and preference-aligned by reinforcement fine-tuning using runtime measurements, enabling it to propose input-specific improvement strategies and apply them directly without relying on iterative refinement. On the PIE code performance benchmark, PerfCoder surpasses all existing models in both runtime speedup and effective optimization rate, demonstrating that performance optimization cannot be achieved by scale alone but requires optimization stratetgy awareness. In addition, PerfCoder can generate interpretable feedback about the source code, which, when provided as input to a larger LLM in a planner-and-optimizer cooperative workflow, can further improve outcomes. Specifically, we elevate the performance of 32B models and GPT-5 to new levels on code optimization, substantially surpassing their original performance.

