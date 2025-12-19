---
layout: default
title: Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning
---

# Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16917" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16917v1</a>
  <a href="https://arxiv.org/pdf/2512.16917.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16917v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16917v1', 'Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qihao Liu, Luoxin Ye, Wufei Ma, Yu-Cheng Chou, Alan Yuille

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出生成对抗推理器，通过对抗强化学习提升LLM的推理能力，尤其在数学问题上。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `对抗学习` `数学推理` `信用分配` `奖励塑造` `在线学习`

## 📋 核心要点

1. 现有LLM在数学推理中存在过程错误，如计算错误、逻辑脆弱和表面合理但无效的步骤，影响了推理的可靠性。
2. 提出生成对抗推理器，通过对抗强化学习协同训练LLM推理器和判别器，利用判别器的反馈来提升推理器的逻辑一致性。
3. 实验表明，该方法在数学基准测试中显著提升了LLM的推理性能，例如在AIME24数据集上取得了显著的准确率提升。

## 📝 摘要（中文）

本文提出了一种名为生成对抗推理器（Generative Adversarial Reasoner）的在线联合训练框架，旨在通过对抗强化学习协同进化LLM推理器和基于LLM的判别器，从而增强LLM的推理能力。该框架采用计算高效的审查机制，将每个推理链划分为逻辑上完整的、长度相当的片段，判别器使用简洁、结构化的理由评估每个片段的合理性。学习过程耦合了互补信号：LLM推理器因产生逻辑一致且能得出正确答案的步骤而获得奖励，而判别器因正确检测到推理过程中的错误或区分推理轨迹而获得奖励。这产生了密集的、校准良好的在线步骤级奖励，补充了稀疏的精确匹配信号，改善了信用分配，提高了样本效率，并增强了LLM的整体推理质量。在各种数学基准测试中，该方法相对于使用标准RL后训练的强大基线，实现了持续的收益。具体而言，在AIME24上，DeepSeek-R1-Distill-Qwen-7B从54.0提高到61.3（+7.3），DeepSeek-R1-Distill-Llama-8B从43.7提高到53.7（+10.0）。模块化判别器还能够灵活地进行奖励塑造，以实现诸如教师知识蒸馏、偏好对齐和基于数学证明的推理等目标。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在数学推理过程中出现的逻辑错误、计算错误以及推理步骤不合理等问题。现有方法通常依赖于稀疏的奖励信号（例如，最终答案是否正确），导致信用分配困难，训练效率低下，难以有效提升LLM的推理能力。

**核心思路**：论文的核心思路是通过对抗强化学习，同时训练一个LLM推理器和一个LLM判别器。推理器负责生成推理步骤，判别器负责评估每个推理步骤的合理性。通过这种对抗的方式，推理器可以学习到更细粒度的奖励信号，从而更好地优化推理过程。

**技术框架**：整体框架包含两个主要模块：LLM推理器和LLM判别器。推理器负责生成推理步骤，判别器负责评估每个推理步骤的合理性，并给出结构化的理由。训练过程采用在线强化学习的方式，推理器根据判别器的反馈调整策略，判别器根据推理器的表现调整评估标准。一个关键组件是“审查机制”，它将推理链分割成逻辑完整的片段，以便判别器能够更有效地评估每个片段的合理性。

**关键创新**：最重要的创新点在于引入了对抗学习的思想，将推理过程建模成一个生成对抗的过程。判别器的存在为推理器提供了更密集、更细粒度的奖励信号，解决了传统强化学习中信用分配困难的问题。此外，模块化的判别器设计使得可以灵活地进行奖励塑造，以适应不同的目标，例如知识蒸馏、偏好对齐等。

**关键设计**：论文设计了一个计算高效的审查机制，将推理链分割成逻辑完整的片段，并让判别器评估每个片段的合理性。判别器输出简洁、结构化的理由，为推理器提供更丰富的反馈信息。推理器和判别器都使用LLM作为基础模型，并通过强化学习算法进行训练。具体的损失函数包括推理器的策略梯度损失和判别器的交叉熵损失。奖励函数的设计考虑了推理步骤的逻辑一致性和最终答案的正确性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16917v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16917v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16917v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在AIME24等数学基准测试中取得了显著的性能提升。例如，DeepSeek-R1-Distill-Qwen-7B模型在该数据集上的准确率从54.0%提高到61.3%（+7.3%），DeepSeek-R1-Distill-Llama-8B模型从43.7%提高到53.7%（+10.0%）。这些结果表明，该方法能够有效提升LLM的推理能力。

## 🎯 应用场景

该研究成果可应用于各种需要复杂推理能力的场景，例如数学问题求解、科学研究、智能问答系统等。通过提升LLM的推理能力，可以提高这些应用场景的准确性和可靠性，并有望推动人工智能在更广泛领域的应用。

## 📄 摘要（原文）

> Large language models (LLMs) with explicit reasoning capabilities excel at mathematical reasoning yet still commit process errors, such as incorrect calculations, brittle logic, and superficially plausible but invalid steps. In this paper, we introduce Generative Adversarial Reasoner, an on-policy joint training framework designed to enhance reasoning by co-evolving an LLM reasoner and an LLM-based discriminator through adversarial reinforcement learning. A compute-efficient review schedule partitions each reasoning chain into logically complete slices of comparable length, and the discriminator evaluates each slice's soundness with concise, structured justifications. Learning couples complementary signals: the LLM reasoner is rewarded for logically consistent steps that yield correct answers, while the discriminator earns rewards for correctly detecting errors or distinguishing traces in the reasoning process. This produces dense, well-calibrated, on-policy step-level rewards that supplement sparse exact-match signals, improving credit assignment, increasing sample efficiency, and enhancing overall reasoning quality of LLMs. Across various mathematical benchmarks, the method delivers consistent gains over strong baselines with standard RL post-training. Specifically, on AIME24, we improve DeepSeek-R1-Distill-Qwen-7B from 54.0 to 61.3 (+7.3) and DeepSeek-R1-Distill-Llama-8B from 43.7 to 53.7 (+10.0). The modular discriminator also enables flexible reward shaping for objectives such as teacher distillation, preference alignment, and mathematical proof-based reasoning.

