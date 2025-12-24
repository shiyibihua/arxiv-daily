---
layout: default
title: Enhancing Vision-Language Model Training with Reinforcement Learning in Synthetic Worlds for Real-World Success
---

# Enhancing Vision-Language Model Training with Reinforcement Learning in Synthetic Worlds for Real-World Success

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04280" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04280v1</a>
  <a href="https://arxiv.org/pdf/2508.04280.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04280v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04280v1', 'Enhancing Vision-Language Model Training with Reinforcement Learning in Synthetic Worlds for Real-World Success')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: George Bredis, Stanislav Dereka, Viacheslav Sinii, Ruslan Rakhimov, Daniil Gavrilov

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出VL-DAC以解决现有视觉语言模型训练不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `强化学习` `多模态智能体` `合成环境` `泛化能力`

## 📋 核心要点

1. 现有的视觉语言模型在将视觉信息转化为语言条件动作序列方面存在明显不足，缺乏有效的泛化能力。
2. 本文提出的VL-DAC算法通过解耦动作和价值学习，避免了复杂的超参数调优，提升了训练效率和稳定性。
3. 在多个基准测试中，VL-DAC训练的模型在真实图像的代理控制、空间推理和网络导航任务上均取得了显著的性能提升。

## 📝 摘要（中文）

交互式多模态智能体必须将原始视觉观察转化为连贯的语言条件动作序列，而当前的视觉语言模型（VLMs）在这方面仍显不足。以往的强化学习（RL）尝试虽然理论上可以赋予VLMs此能力，但很少测试所学行为是否能超越训练模拟器，且通常依赖脆弱的超参数调优或低状态变异性的稠密奖励环境。本文提出了一种轻量级、无超参数的RL算法——视觉语言解耦演员-评论家（VL-DAC），该算法在动作令牌上应用PPO更新，同时仅在环境步骤级别学习价值。这种简单的解耦消除了不稳定的加权项，带来了更快、更可靠的收敛。在一个便宜的模拟器中训练单个VLM，已能产生广泛泛化的策略，且在多个基准测试中均有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉语言模型在训练过程中缺乏泛化能力的问题。以往的强化学习方法往往依赖于复杂的超参数调优和低变异性的环境，导致模型在真实场景中的表现不佳。

**核心思路**：本文提出的VL-DAC算法通过将动作令牌的更新与环境步骤的价值学习解耦，简化了训练过程，避免了不稳定的加权项，从而实现更快的收敛和更高的稳定性。

**技术框架**：VL-DAC的整体架构包括两个主要模块：动作更新模块和价值学习模块。动作更新模块使用PPO算法对动作令牌进行优化，而价值学习模块则在每个环境步骤中独立学习状态价值。

**关键创新**：VL-DAC的主要创新在于其轻量级设计和无超参数的特性，这与传统的强化学习方法形成鲜明对比。通过这种解耦设计，VL-DAC能够在低成本的合成环境中有效训练VLMs，并实现良好的泛化能力。

**关键设计**：VL-DAC在训练过程中不依赖于复杂的超参数设置，且采用了简单的损失函数设计，确保了训练过程的高效性和稳定性。

## 📊 实验亮点

实验结果显示，使用VL-DAC训练的模型在BALROG基准测试中相较于基线提升了50%的相对性能，在VSI-Bench的最难部分提升了5%，在VisualWebBench中提升了2%。这些结果表明，VL-DAC能够在不降低图像理解准确性的前提下，显著提高模型的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、虚拟助手等多模态交互系统。通过在合成环境中有效训练视觉语言模型，能够提升这些系统在真实世界中的表现，推动人机交互的智能化进程。

## 📄 摘要（原文）

> Interactive multimodal agents must convert raw visual observations into coherent sequences of language-conditioned actions -- a capability that current vision-language models (VLMs) still lack. Earlier reinforcement-learning (RL) efforts could, in principle, endow VLMs with such skills, but they have seldom tested whether the learned behaviours generalize beyond their training simulators, and they depend either on brittle hyperparameter tuning or on dense-reward environments with low state variability. We introduce Vision-Language Decoupled Actor-Critic (VL-DAC), a lightweight, hyperparameter-free RL algorithm. VL-DAC applies PPO updates to action tokens while learning value only at the environment-step level: an arrangement, to our knowledge, not previously explored for large VLMs or LLMs. This simple decoupling removes unstable weighting terms and yields faster, more reliable convergence. Training a single VLM with VL-DAC in one inexpensive simulator at a time (MiniWorld, Gym-Cards, ALFWorld, or WebShop) already produces policies that generalize widely: +50\% relative on BALROG (game-centric agentic control), +5\% relative on the hardest part of VSI-Bench (spatial planning), and +2\% on VisualWebBench (web navigation), all without degrading general image understanding accuracy. These results provide the first evidence that a simple RL algorithm can train VLMs entirely in cheap synthetic worlds while delivering measurable gains on real-image agentic, spatial-reasoning, and web-navigation benchmarks.

