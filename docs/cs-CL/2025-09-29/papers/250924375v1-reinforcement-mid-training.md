---
layout: default
title: Reinforcement Mid-Training
---

# Reinforcement Mid-Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24375" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24375v1</a>
  <a href="https://arxiv.org/pdf/2509.24375.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24375v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24375v1', 'Reinforcement Mid-Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yijun Tian, Shaoyu Chen, Zhichao Xu, Yawei Wang, Jinhe Bi, Peng Han, Wei Wang

**分类**: cs.CL

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出强化中训练（RMT）框架，提升大语言模型性能并加速训练。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大语言模型` `中间训练` `动态Token预算` `自适应采样`

## 📋 核心要点

1. 现有大语言模型训练流程缺乏中间强化训练阶段，导致模型推理效率低、token利用不充分。
2. 论文提出强化中训练框架RMT，通过动态token预算、自适应采样和双重训练策略提升模型性能。
3. 实验表明，RMT在语言建模和数学领域均取得显著提升，验证了强化中训练的有效性。

## 📝 摘要（中文）

本文指出，在预训练和后训练之间存在一个具有巨大性能提升潜力的中间阶段，即强化中训练。论文正式定义了该问题，并识别了三个关键挑战：过度推理步骤导致的训练效率低下、忽略不平衡的token熵分布以及token信息的未充分利用。为了解决这些挑战，论文提出了RMT，一个高效、自适应和统一的强化中训练框架，包含多种创新组件。具体而言，首先引入动态token预算机制，约束不必要的推理步骤并缓解模型过度思考。其次，设计了一种基于课程的自适应采样方法，促进从易到难的token渐进学习轨迹。最后，提出了一种结合强化学习和下一token预测的双重训练策略，确保对关键token的针对性学习并充分利用所有token信息。大量实验表明，RMT优于现有方法，在语言建模中实现了高达+64.91%的性能提升，而推理长度仅为21%。同时证明，强化中训练后获得的checkpoint可以促进后续的后训练，在数学领域产生高达+18.76%的改进。

## 🔬 方法详解

**问题定义**：现有的大语言模型训练通常分为预训练和后训练两个阶段，忽略了中间阶段的潜力。直接进行强化学习训练时，模型可能进行过多的不必要的推理步骤，导致训练效率低下。此外，模型对不同token的关注度不同，token熵分布不平衡，且现有方法未能充分利用所有token的信息。

**核心思路**：论文的核心思路是在预训练和后训练之间引入一个强化中训练阶段，通过强化学习来优化模型的推理过程，提高训练效率和模型性能。RMT框架旨在解决过度推理、token熵不平衡和token信息未充分利用的问题，从而实现更高效、自适应和统一的强化中训练。

**技术框架**：RMT框架包含三个主要组成部分：动态token预算机制、基于课程的自适应采样方法和双重训练策略。动态token预算机制限制不必要的推理步骤，避免模型过度思考。自适应采样方法根据token的难易程度进行采样，促进模型从易到难地学习。双重训练策略结合强化学习和下一token预测，确保模型对关键token进行针对性学习，并充分利用所有token的信息。

**关键创新**：RMT的关键创新在于提出了强化中训练的概念，并设计了相应的框架来解决该阶段面临的挑战。动态token预算机制、自适应采样方法和双重训练策略都是针对特定问题提出的创新解决方案，与现有方法相比，RMT能够更有效地利用计算资源，提高训练效率和模型性能。

**关键设计**：动态token预算机制通过设定一个动态变化的token数量上限来约束模型的推理长度。自适应采样方法使用课程学习的思想，根据token的熵值动态调整采样概率。双重训练策略使用强化学习奖励模型生成高质量的token，同时使用下一token预测损失来保证模型能够学习到所有token的信息。损失函数是强化学习奖励和下一token预测损失的加权和。

## 📊 实验亮点

实验结果表明，RMT在语言建模任务中实现了高达+64.91%的性能提升，同时推理长度仅为现有方法的21%。此外，使用RMT训练得到的checkpoint可以显著提升后续后训练的效果，在数学领域取得了+18.76%的性能提升。这些结果充分验证了RMT的有效性和优越性。

## 🎯 应用场景

该研究成果可广泛应用于大语言模型的训练和优化，尤其是在需要高效推理和精确控制的场景，如对话系统、代码生成、数学推理等。通过强化中训练，可以提升模型的性能和效率，降低计算成本，加速大语言模型的部署和应用。

## 📄 摘要（原文）

> The development of state-of-the-art large language models is commonly understood as a two-stage process involving pre-training and post-training. We point out the need for an additional intermediate stage called reinforcement mid-training with potential for strong performance gains. In this paper, we formally define the problem and identify three key challenges: (1) inefficient training due to excessive reasoning steps, (2) disregard of the imbalanced token entropy distribution, and (3) underutilization of token information. To address these challenges, we propose RMT, a framework for efficient, adaptive, and unified reinforcement mid-training with various innovative components. In particular, we first introduce a dynamic token budget mechanism that constrains unnecessary reasoning steps and mitigates model overthinking. Next, we design a curriculum-based adaptive sampling method that fosters a progressive learning trajectory from easy to hard tokens. Finally, we present a dual training strategy that combines reinforcement learning with next-token prediction, ensuring targeted learning on key tokens and full exploitation of all token information. Extensive experiments demonstrate the superiority of RMT over state-of-the-art methods, achieving up to +64.91% performance improvement with only 21% of the reasoning length in language modeling. We also show that checkpoints obtained after reinforcement mid-training can benefit the subsequent post-training, yielding up to +18.76% improvement in the mathematical domain.

