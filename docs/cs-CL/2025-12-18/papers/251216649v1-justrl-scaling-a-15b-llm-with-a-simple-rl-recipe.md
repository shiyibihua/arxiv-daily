---
layout: default
title: JustRL: Scaling a 1.5B LLM with a Simple RL Recipe
---

# JustRL: Scaling a 1.5B LLM with a Simple RL Recipe

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16649" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16649v1</a>
  <a href="https://arxiv.org/pdf/2512.16649.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16649v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16649v1', 'JustRL: Scaling a 1.5B LLM with a Simple RL Recipe')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingxiang He, Zekai Qu, Zeyuan Liu, Yinghao Chen, Yuxin Zuo, Cheng Qian, Kaiyan Zhang, Weize Chen, Chaojun Xiao, Ganqu Cui, Ning Ding, Zhiyuan Liu

**分类**: cs.CL

**发布日期**: 2025-12-18

**备注**: 12 pages, 3 figures

---

## 💡 一句话要点

**JustRL：通过简单强化学习方法扩展15亿参数LLM，实现数学推理SOTA**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `数学推理` `单阶段训练` `固定超参数` `模型简化` `计算效率`

## 📋 核心要点

1. 现有LLM强化学习方法过于复杂，包含多阶段训练和动态超参数调整，缺乏对必要性的深入研究。
2. JustRL采用单阶段训练和固定超参数，避免复杂调整，旨在探索简化强化学习流程在LLM中的潜力。
3. 实验表明，JustRL在数学推理任务上达到SOTA，且计算量更少，并发现一些常用技巧可能适得其反。

## 📝 摘要（中文）

大型语言模型（LLM）的强化学习研究日益复杂，包括多阶段训练流程、动态超参数调整和课程学习策略。本文提出一个根本问题：这种复杂性是必要的吗？我们提出了JustRL，一种极简方法，使用单阶段训练和固定超参数，在两个15亿参数的推理模型上实现了最先进的性能（在九个数学基准测试中平均准确率分别为54.9％和64.3％），同时计算量仅为复杂方法的2倍。相同的超参数无需调整即可在两个模型之间迁移，并且训练过程表现出平滑的单调改进，超过4,000多个步骤，没有通常需要干预的崩溃或停滞。关键的是，消融实验表明，添加诸如显式长度惩罚和鲁棒验证器之类的“标准技巧”可能会因探索崩溃而降低性能。这些结果表明，该领域可能正在增加复杂性来解决随着稳定、规模化的基线而消失的问题。我们发布了我们的模型和代码，以建立一个简单、经过验证的社区基线。

## 🔬 方法详解

**问题定义**：现有的大型语言模型强化学习方法通常采用复杂的多阶段训练流程、动态超参数调整以及课程学习策略，这增加了训练的难度和计算成本。论文旨在探究这些复杂性是否是必要的，并尝试使用更简单的方法来实现更好的性能。现有方法的痛点在于训练流程复杂，计算资源消耗大，且对超参数敏感。

**核心思路**：论文的核心思路是采用极简的强化学习方法，即JustRL，使用单阶段训练和固定的超参数。作者认为，通过稳定和规模化的基线，可以避免一些复杂方法试图解决的问题。这种方法旨在降低训练的复杂性，提高训练的稳定性，并减少计算资源的消耗。

**技术框架**：JustRL的整体框架非常简单，主要包含以下几个步骤：首先，使用一个预训练的1.5B参数的语言模型作为基础模型。然后，使用强化学习算法（具体算法未知，但从描述来看，可能是PPO或类似的算法）对模型进行单阶段的训练。在训练过程中，使用固定的超参数，避免动态调整。最后，在数学推理任务上评估模型的性能。

**关键创新**：论文最重要的技术创新点在于其极简的设计理念。与现有方法相比，JustRL避免了复杂的多阶段训练流程和动态超参数调整，而是采用单阶段训练和固定的超参数。这种设计理念简化了训练流程，提高了训练的稳定性，并减少了计算资源的消耗。此外，论文还发现，一些常用的技巧，如显式长度惩罚和鲁棒验证器，可能会因探索崩溃而降低性能。

**关键设计**：论文的关键设计在于单阶段训练和固定超参数的使用。具体的参数设置未知，但作者强调，相同的超参数可以在不同的模型之间迁移，而无需进行调整。损失函数未知，但可能是标准的强化学习损失函数，如PPO损失函数。网络结构是基于一个预训练的1.5B参数的语言模型，没有进行特殊的修改。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16649v1/figures/fig1_aime24_curves_added.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16649v1/figures/fig2_training_dynamics.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16649v1/figures/fig3_training_dynamics.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

JustRL在两个15亿参数的推理模型上实现了最先进的性能，在九个数学基准测试中平均准确率分别达到54.9％和64.3％，同时计算量仅为复杂方法的2倍。更重要的是，相同的超参数无需调整即可在两个模型之间迁移，训练过程表现出平滑的单调改进，超过4,000多个步骤，没有出现崩溃或停滞。

## 🎯 应用场景

JustRL的研究成果可应用于各种需要复杂推理能力的场景，例如数学问题求解、代码生成、知识问答等。通过简化强化学习流程，降低训练成本，使得更多研究者和开发者能够训练出高性能的LLM，加速相关技术的普及和应用。此外，该研究也为未来的LLM强化学习研究提供了一个新的方向，即关注简单性和稳定性。

## 📄 摘要（原文）

> Recent advances in reinforcement learning for large language models have converged on increasing complexity: multi-stage training pipelines, dynamic hyperparameter schedules, and curriculum learning strategies. This raises a fundamental question: \textbf{Is this complexity necessary?} We present \textbf{JustRL}, a minimal approach using single-stage training with fixed hyperparameters that achieves state-of-the-art performance on two 1.5B reasoning models (54.9\% and 64.3\% average accuracy across nine mathematical benchmarks) while using 2$\times$ less compute than sophisticated approaches. The same hyperparameters transfer across both models without tuning, and training exhibits smooth, monotonic improvement over 4,000+ steps without the collapses or plateaus that typically motivate interventions. Critically, ablations reveal that adding ``standard tricks'' like explicit length penalties and robust verifiers may degrade performance by collapsing exploration. These results suggest that the field may be adding complexity to solve problems that disappear with a stable, scaled-up baseline. We release our models and code to establish a simple, validated baseline for the community.

