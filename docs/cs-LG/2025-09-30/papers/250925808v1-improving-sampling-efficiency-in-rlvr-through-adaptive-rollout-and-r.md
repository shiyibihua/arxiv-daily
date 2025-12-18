---
layout: default
title: Improving Sampling Efficiency in RLVR through Adaptive Rollout and Response Reuse
---

# Improving Sampling Efficiency in RLVR through Adaptive Rollout and Response Reuse

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25808" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25808v1</a>
  <a href="https://arxiv.org/pdf/2509.25808.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25808v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25808v1', 'Improving Sampling Efficiency in RLVR through Adaptive Rollout and Response Reuse')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuheng Zhang, Wenlin Yao, Changlong Yu, Yao Liu, Qingyu Yin, Bing Yin, Hyokun Yun, Lihong Li

**分类**: cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**AR3PO：通过自适应Rollout和响应复用提升RLVR采样效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `采样效率` `自适应Rollout` `响应复用` `RLVR` `策略优化` `后训练`

## 📋 核心要点

1. 现有RLVR方法如GRPO在响应组内奖励相同时存在优势消失问题，限制了训练效率。
2. AR3PO通过自适应Rollout动态分配计算资源，并复用已有正确响应，提升采样效率。
3. 实验表明，AR3PO在多个基准测试中优于GRPO，并能以更低的Rollout成本匹配或超越DAPO。

## 📝 摘要（中文）

大型语言模型（LLMs）在推理性能方面取得了显著进展，而基于可验证奖励的强化学习（RLVR）已成为后训练的标准范式。一种代表性算法，即群体相对策略优化（GRPO），通过对响应组内的结果奖励进行归一化来计算优势，但当组内所有响应获得相同奖励时，会遇到优势消失的问题。为了解决这个问题，我们提出了自适应Rollout和响应复用策略优化（AR3PO），这是一种采样高效的RLVR算法，引入了两项新技术：自适应Rollout，它动态地为困难的提示分配更多响应，同时节省简单提示的计算；以及响应复用，它利用先前生成的正确响应来提供有用的训练信号。我们使用两个不同的基础模型系列，在多个代表性基准上将AR3PO与强大的RLVR基线进行比较。在7B和8B模型上，AR3PO始终优于GRPO，并且达到或超过DAPO的性能，同时将Rollout成本降低高达4.2倍。在更大的32B模型上，AR3PO在相似的训练步骤中实现了与DAPO相当的性能，同时保持了显著更低的Rollout成本。

## 🔬 方法详解

**问题定义**：论文旨在解决RLVR（Reinforcement Learning with Verifiable Rewards）中采样效率低下的问题。具体来说，现有的GRPO算法在处理所有响应获得相同奖励的prompt时，会面临优势消失的问题，导致训练效率降低。此外，对所有prompt都采用相同的rollout策略，忽略了prompt难度的差异，造成了计算资源的浪费。

**核心思路**：AR3PO的核心思路是通过自适应地调整rollout策略和复用已有的高质量响应来提高采样效率。自适应rollout根据prompt的难度动态分配计算资源，对困难的prompt进行更多的采样，而对简单的prompt则减少采样。响应复用则利用之前生成的正确响应作为训练信号，避免重复生成相同的响应，从而提高训练效率。

**技术框架**：AR3PO的整体框架包括以下几个主要模块：1）Prompt难度评估模块：用于评估每个prompt的难度，并根据难度动态调整rollout的数量。2）自适应Rollout模块：根据prompt难度评估结果，动态分配rollout的数量，对困难的prompt进行更多的采样。3）响应复用模块：维护一个响应池，存储之前生成的正确响应，并在训练过程中复用这些响应，避免重复生成。4）策略优化模块：使用强化学习算法（如GRPO）对策略进行优化，利用自适应rollout和响应复用提供的数据进行训练。

**关键创新**：AR3PO的关键创新在于提出了自适应rollout和响应复用两种技术，这两种技术能够有效地提高RLVR的采样效率。自适应rollout能够根据prompt的难度动态分配计算资源，避免了对简单prompt的过度采样，从而节省了计算资源。响应复用则能够利用之前生成的正确响应作为训练信号，避免了重复生成相同的响应，从而提高了训练效率。

**关键设计**：在自适应rollout中，可以使用多种方法来评估prompt的难度，例如可以使用模型对prompt的预测置信度作为难度指标。在响应复用中，需要维护一个响应池，并设计合适的策略来选择哪些响应可以被复用。例如，可以只复用奖励最高的响应，或者可以根据响应的多样性来选择复用哪些响应。具体的损失函数和网络结构与GRPO等基线方法保持一致，主要关注于采样策略的优化。

## 📊 实验亮点

AR3PO在7B和8B模型上始终优于GRPO，并达到或超过DAPO的性能，同时将Rollout成本降低高达4.2倍。在更大的32B模型上，AR3PO在相似的训练步骤中实现了与DAPO相当的性能，同时保持了显著更低的Rollout成本。这些结果表明AR3PO在提高RLVR采样效率方面具有显著优势。

## 🎯 应用场景

AR3PO可应用于各种需要通过强化学习进行后训练的大型语言模型，尤其是在计算资源有限的情况下。例如，可以用于优化LLM在问答、文本生成、代码生成等任务中的性能，提高模型的准确性和效率，并降低训练成本。该方法在教育、客服、内容创作等领域具有广泛的应用前景。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved impressive reasoning performance, with reinforcement learning with verifiable rewards (RLVR) emerging as a standard paradigm for post-training. A representative algorithm, group relative policy optimization (GRPO) (Shao et al., 2024), computes advantages by normalizing outcome rewards within response groups, but suffers from a vanishing advantage issue when all responses in a group receive identical rewards. To address this issue, we propose Adaptive Rollout and Response Reuse Policy Optimization (AR3PO), a sampling efficient RLVR algorithm that introduces two novel techniques: adaptive rollout, which dynamically allocates more responses to difficult prompts while saving computation on easier ones, and response reuse, which leverages previously generated correct responses to provide useful training signals. We compare AR3PO with strong RLVR baselines on multiple representative benchmarks using two different families of base models. Across the 7B and 8B models, AR3PO consistently outperforms GRPO and matches or surpasses DAPO (Yu et al., 2025), reducing rollout cost by up to 4.2x. On the larger 32B model, AR3PO achieves comparable performance to DAPO at similar training steps while maintaining substantially lower rollout cost.

