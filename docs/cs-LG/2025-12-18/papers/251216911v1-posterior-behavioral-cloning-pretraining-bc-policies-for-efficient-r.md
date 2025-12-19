---
layout: default
title: Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning
---

# Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16911" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16911v1</a>
  <a href="https://arxiv.org/pdf/2512.16911.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16911v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16911v1', 'Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrew Wagenmaker, Perry Dong, Raymond Tsao, Chelsea Finn, Sergey Levine

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出后验行为克隆(PostBC)方法，提升RL微调的预训练策略效果**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `后验行为克隆` `强化学习微调` `行为克隆` `机器人控制` `预训练策略` `生成模型` `策略初始化`

## 📋 核心要点

1. 现有行为克隆(BC)方法在作为强化学习(RL)微调的初始化时，无法保证覆盖演示者的所有行为，限制了微调效果。
2. 提出后验行为克隆(PostBC)，通过建模演示者行为的后验分布，确保策略覆盖演示者的行为，从而改善RL微调的初始化。
3. 实验表明，PostBC在机器人控制任务中，相较于标准BC，显著提升了RL微调的性能，并在真实机器人操作任务中验证了其有效性。

## 📝 摘要（中文）

本文研究了预训练策略如何影响强化学习(RL)微调的性能，以及如何预训练策略以确保它们是有效的微调初始化。理论上证明，标准行为克隆(BC)无法确保覆盖演示者的行为，这是有效RL微调的必要条件。因此，提出后验行为克隆(PostBC)策略，该策略训练模型以模拟给定演示数据集的演示者行为的后验分布，从而确保覆盖演示者的行为，实现更有效的微调，同时保证预训练性能不低于BC策略。PostBC可以通过现代生成模型在机器人控制领域中实际实现，仅依赖于标准监督学习，并且与标准行为克隆相比，在真实的机器人控制基准和真实机器人操作任务上，显著提高了RL微调的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决标准行为克隆(BC)作为强化学习(RL)微调的预训练策略时，无法有效覆盖演示者行为的问题。现有BC方法直接模仿演示数据中的动作，可能导致策略陷入局部最优，缺乏探索能力，从而限制了后续RL微调的性能。

**核心思路**：论文的核心思路是，与其精确拟合观察到的演示数据，不如训练一个策略来模拟给定演示数据集下演示者行为的后验分布。这种方法能够更好地捕捉演示者行为的多样性，并确保策略能够覆盖演示者的所有可能行为，从而为后续的RL微调提供更好的初始化。

**技术框架**：PostBC的整体框架包括以下几个阶段：1) 收集演示数据集；2) 使用生成模型（例如变分自编码器VAE或归一化流）对演示数据进行建模，学习演示者行为的后验分布；3) 从学习到的后验分布中采样，训练PostBC策略；4) 使用RL算法对PostBC策略进行微调。

**关键创新**：PostBC的关键创新在于，它不再是简单地模仿演示数据，而是学习演示者行为的后验分布。这种方法能够更好地捕捉演示者行为的不确定性和多样性，从而提高策略的泛化能力和探索能力。与现有BC方法相比，PostBC能够更好地覆盖演示者的行为空间，为后续的RL微调提供更有效的初始化。

**关键设计**：PostBC的关键设计包括：1) 使用合适的生成模型来建模演示者行为的后验分布，例如VAE或归一化流；2) 设计合适的损失函数来训练生成模型，例如变分下界(ELBO)或最大似然估计；3) 从学习到的后验分布中采样，生成训练数据，用于训练PostBC策略；4) 选择合适的RL算法对PostBC策略进行微调，例如PPO或SAC。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16911v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16911v1/im/corn_in_pot2.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16911v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，PostBC在多个机器人控制任务中显著优于标准BC。例如，在真实机器人操作任务中，PostBC能够更快地学习到有效的策略，并达到更高的性能。与BC相比，PostBC在RL微调后的性能提升幅度明显，验证了其作为RL微调有效初始化的优势。

## 🎯 应用场景

PostBC方法可广泛应用于机器人控制、自动驾驶、游戏AI等领域。通过预训练一个能够覆盖专家行为的策略，可以显著提高后续RL微调的效率和性能，降低对大量环境交互的需求，加速智能体的学习过程。该方法尤其适用于那些难以获取大量奖励信号或环境交互成本较高的场景。

## 📄 摘要（原文）

> Standard practice across domains from robotics to language is to first pretrain a policy on a large-scale demonstration dataset, and then finetune this policy, typically with reinforcement learning (RL), in order to improve performance on deployment domains. This finetuning step has proved critical in achieving human or super-human performance, yet while much attention has been given to developing more effective finetuning algorithms, little attention has been given to ensuring the pretrained policy is an effective initialization for RL finetuning. In this work we seek to understand how the pretrained policy affects finetuning performance, and how to pretrain policies in order to ensure they are effective initializations for finetuning. We first show theoretically that standard behavioral cloning (BC) -- which trains a policy to directly match the actions played by the demonstrator -- can fail to ensure coverage over the demonstrator's actions, a minimal condition necessary for effective RL finetuning. We then show that if, instead of exactly fitting the observed demonstrations, we train a policy to model the posterior distribution of the demonstrator's behavior given the demonstration dataset, we do obtain a policy that ensures coverage over the demonstrator's actions, enabling more effective finetuning. Furthermore, this policy -- which we refer to as the posterior behavioral cloning (PostBC) policy -- achieves this while ensuring pretrained performance is no worse than that of the BC policy. We then show that PostBC is practically implementable with modern generative models in robotic control domains -- relying only on standard supervised learning -- and leads to significantly improved RL finetuning performance on both realistic robotic control benchmarks and real-world robotic manipulation tasks, as compared to standard behavioral cloning.

