---
layout: default
title: "MUSIC: MUlti-Step Instruction Contrast for Multi-Turn Reward Models"
---

# MUSIC: MUlti-Step Instruction Contrast for Multi-Turn Reward Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24693" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24693v1</a>
  <a href="https://arxiv.org/pdf/2512.24693.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24693v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24693v1', 'MUSIC: MUlti-Step Instruction Contrast for Multi-Turn Reward Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenzhe Li, Shujian Zhang, Wenxuan Zhou, John Lambert, Chi Jin, Andrew Hard, Rajiv Mathews, Lun Wang

**分类**: cs.CL

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**提出MUSIC：多步指令对比方法，提升多轮对话奖励模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `奖励模型` `数据增强` `指令对比` `无监督学习`

## 📋 核心要点

1. 现有奖励模型在多轮对话评估中表现不足，因为标准偏好数据集缺乏足够的多轮交互信号。
2. MUSIC通过无监督数据增强，合成跨多轮的对比对话对，从而增强奖励模型对多轮交互的理解。
3. 实验表明，MUSIC增强的奖励模型在多轮对话评估中与LLM judges的判断更一致，且不影响单轮性能。

## 📝 摘要（中文）

评估多轮对话的质量对于开发强大的大型语言模型（LLMs）至关重要，但仍然是一个巨大的挑战，通常需要昂贵的人工评估。多轮奖励模型（RMs）提供了一种可扩展的替代方案，并且可以为指导LLM训练提供有价值的信号。虽然最近的工作已经推进了多轮	extit{训练}技术，但专门针对多轮交互的有效自动化	extit{评估}仍然滞后。我们观察到，标准的偏好数据集通常仅基于最终对话轮次来对比响应，提供的信号不足以捕捉多轮交互的细微差别。相反，我们发现，纳入跨越	extit{多个}轮次的对比对于构建稳健的多轮RM至关重要。受此发现的启发，我们提出了一种无监督数据增强策略，即	extbf{MU}lti-	extbf{S}tep 	extbf{I}nstruction 	extbf{C}ontrast (MUSIC)，它合成了在多个轮次中表现出差异的对比对话对。利用Skywork偏好数据集上的MUSIC，我们训练了一个基于Gemma-2-9B-Instruct模型的多轮RM。经验结果表明，我们的MUSIC增强RM优于基线方法，在多轮对话中实现了与高级专有LLM judges的判断更高的一致性，关键是，没有影响标准单轮RM基准上的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决多轮对话奖励模型训练数据不足的问题，现有奖励模型通常基于单轮对话数据训练，无法有效捕捉多轮对话中的上下文依赖和细微差别。这导致奖励模型在评估多轮对话质量时表现不佳，与人类判断的一致性较低。

**核心思路**：论文的核心思路是通过无监督数据增强，生成包含多轮交互信息的对比样本。具体来说，MUSIC方法通过修改对话历史中的多个轮次，生成具有细微差异的对话对，从而迫使奖励模型学习区分不同对话策略的优劣。这种多步指令对比能够更全面地捕捉多轮对话的复杂性。

**技术框架**：MUSIC方法主要包含以下几个步骤：1) 从现有对话数据集中选择对话样本；2) 随机选择对话中的多个轮次；3) 使用指令改写模型对选定的轮次进行修改，生成对比样本；4) 将原始对话和修改后的对话组成对比对，用于训练奖励模型。整个过程是无监督的，不需要人工标注。

**关键创新**：MUSIC的关键创新在于其多步指令对比策略。与以往仅关注最终轮次对比的方法不同，MUSIC通过修改对话历史中的多个轮次，生成更具挑战性的对比样本，从而迫使奖励模型学习捕捉多轮对话中的长期依赖关系。这种方法能够更有效地利用现有数据，提升奖励模型的性能。

**关键设计**：MUSIC方法的关键设计包括：1) 使用高质量的指令改写模型，确保生成的对比样本具有语义一致性和合理性；2) 随机选择修改的轮次数量和位置，增加对比样本的多样性；3) 使用合适的损失函数，例如hinge loss或margin ranking loss，鼓励奖励模型区分不同对话策略的优劣。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24693v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24693v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，MUSIC增强的奖励模型在多轮对话评估中显著优于基线方法。具体来说，MUSIC在与高级专有LLM judges的判断一致性方面取得了显著提升，同时保持了在标准单轮RM基准上的性能。这表明MUSIC能够有效提升奖励模型对多轮对话的理解能力，而不会牺牲其在单轮对话上的性能。

## 🎯 应用场景

MUSIC方法可以广泛应用于多轮对话系统的训练和评估。它可以用于训练更准确的奖励模型，从而指导对话策略的学习和优化。此外，MUSIC还可以用于评估不同对话系统的性能，为系统改进提供依据。该方法在智能客服、聊天机器人、虚拟助手等领域具有重要的应用价值。

## 📄 摘要（原文）

> Evaluating the quality of multi-turn conversations is crucial for developing capable Large Language Models (LLMs), yet remains a significant challenge, often requiring costly human evaluation. Multi-turn reward models (RMs) offer a scalable alternative and can provide valuable signals for guiding LLM training. While recent work has advanced multi-turn \textit{training} techniques, effective automated \textit{evaluation} specifically for multi-turn interactions lags behind. We observe that standard preference datasets, typically contrasting responses based only on the final conversational turn, provide insufficient signal to capture the nuances of multi-turn interactions. Instead, we find that incorporating contrasts spanning \textit{multiple} turns is critical for building robust multi-turn RMs. Motivated by this finding, we propose \textbf{MU}lti-\textbf{S}tep \textbf{I}nstruction \textbf{C}ontrast (MUSIC), an unsupervised data augmentation strategy that synthesizes contrastive conversation pairs exhibiting differences across multiple turns. Leveraging MUSIC on the Skywork preference dataset, we train a multi-turn RM based on the Gemma-2-9B-Instruct model. Empirical results demonstrate that our MUSIC-augmented RM outperforms baseline methods, achieving higher alignment with judgments from advanced proprietary LLM judges on multi-turn conversations, crucially, without compromising performance on standard single-turn RM benchmarks.

