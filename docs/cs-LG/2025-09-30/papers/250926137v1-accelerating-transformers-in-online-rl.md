---
layout: default
title: Accelerating Transformers in Online RL
---

# Accelerating Transformers in Online RL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26137" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26137v1</a>
  <a href="https://arxiv.org/pdf/2509.26137.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26137v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26137v1', 'Accelerating Transformers in Online RL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniil Zelezetsky, Alexey K. Kovalev, Aleksandr I. Panov

**分类**: cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出加速器策略训练Transformer，解决在线强化学习中Transformer训练不稳定问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Transformer` `强化学习` `在线学习` `行为克隆` `加速器策略`

## 📋 核心要点

1. Transformer在强化学习中面临训练不稳定问题，尤其是在线强化学习中，现有算法难以直接应用。
2. 论文提出使用“加速器”策略，先通过行为克隆预训练Transformer，再进行在线交互，提高训练稳定性。
3. 实验表明，该方法能稳定训练Transformer，减少图像环境训练时间，并显著降低重放缓冲区大小。

## 📝 摘要（中文）

本文提出了一种在在线强化学习中加速Transformer训练的方法。由于Transformer模型的不稳定性，现有的学习算法难以直接应用于基于Transformer的模型。本文提出的方法使用一个更简单、更稳定的“加速器”策略作为Transformer的训练器。在算法的第一阶段，加速器独立地与环境交互，同时通过行为克隆训练Transformer。在第二阶段，预训练的Transformer开始在完全在线的环境中交互。实验结果表明，该算法不仅能够稳定地训练Transformer，而且在基于图像的环境中，训练时间最多可减少一半。此外，它还将离策略方法所需的重放缓冲区大小减少到10-20千，从而显著降低了整体计算需求。实验在基于状态和图像的ManiSkill环境以及MDP和POMDP设置下的MuJoCo任务上进行。

## 🔬 方法详解

**问题定义**：现有基于Transformer的强化学习模型，尤其是在线强化学习中，存在训练不稳定、收敛速度慢的问题。直接将Transformer应用于在线强化学习，容易出现梯度爆炸或消失，导致策略崩溃。此外，Transformer通常需要大量的训练数据，对计算资源要求高。

**核心思路**：论文的核心思路是利用一个更简单、更稳定的策略（即“加速器”）来辅助训练Transformer。加速器先与环境交互，收集数据，并利用这些数据通过行为克隆的方式预训练Transformer。这样可以避免Transformer直接与环境交互带来的不稳定性，并提供一个较好的初始化状态。

**技术框架**：该算法包含两个主要阶段：
1. **加速器训练阶段**：加速器策略（通常是一个简单的模型，如MLP）与环境交互，收集经验数据。同时，使用收集到的数据，通过行为克隆的方式训练Transformer策略，使其模仿加速器的行为。
2. **在线微调阶段**：预训练的Transformer策略开始与环境交互，并使用标准的强化学习算法（如SAC、PPO等）进行在线微调。此时，Transformer已经具备一定的策略能力，可以更稳定地进行在线学习。

**关键创新**：该方法的核心创新在于引入了“加速器”策略，将Transformer的训练过程分解为预训练和在线微调两个阶段。这种方式有效地解决了Transformer在在线强化学习中训练不稳定的问题，并加速了训练过程。与直接在线训练Transformer相比，该方法能够更快地收敛到较好的策略。

**关键设计**：
*   **加速器策略的选择**：加速器策略通常选择一个简单的模型，如多层感知机（MLP），以保证其训练的稳定性和效率。
*   **行为克隆损失函数**：使用均方误差（MSE）或交叉熵损失函数来衡量Transformer策略与加速器策略之间的行为差异。
*   **重放缓冲区大小**：由于预训练阶段已经提供了较好的初始化，在线微调阶段可以显著减小重放缓冲区的大小，从而降低计算资源需求。

## 📊 实验亮点

实验结果表明，该算法在基于图像的ManiSkill环境中，训练时间最多可减少一半。此外，它还将离策略方法所需的重放缓冲区大小减少到10-20千，相比于传统方法所需的数十万甚至数百万的缓冲区大小，显著降低了计算需求。在MuJoCo任务中，该方法也表现出更快的收敛速度和更高的性能。

## 🎯 应用场景

该研究成果可应用于机器人控制、自动驾驶、游戏AI等领域。通过加速Transformer的训练，可以更高效地训练复杂的机器人技能，例如物体抓取、导航等。此外，该方法还可以降低对计算资源的需求，使得在资源受限的平台上部署Transformer成为可能。未来，该方法有望推动Transformer在更多实际场景中的应用。

## 📄 摘要（原文）

> The appearance of transformer-based models in Reinforcement Learning (RL) has expanded the horizons of possibilities in robotics tasks, but it has simultaneously brought a wide range of challenges during its implementation, especially in model-free online RL. Some of the existing learning algorithms cannot be easily implemented with transformer-based models due to the instability of the latter. In this paper, we propose a method that uses the Accelerator policy as a transformer's trainer. The Accelerator, a simpler and more stable model, interacts with the environment independently while simultaneously training the transformer through behavior cloning during the first stage of the proposed algorithm. In the second stage, the pretrained transformer starts to interact with the environment in a fully online setting. As a result, this model-free algorithm accelerates the transformer in terms of its performance and helps it to train online in a more stable and faster way. By conducting experiments on both state-based and image-based ManiSkill environments, as well as on MuJoCo tasks in MDP and POMDP settings, we show that applying our algorithm not only enables stable training of transformers but also reduces training time on image-based environments by up to a factor of two. Moreover, it decreases the required replay buffer size in off-policy methods to 10-20 thousand, which significantly lowers the overall computational demands.

