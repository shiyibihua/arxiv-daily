---
layout: default
title: Training Agents Inside of Scalable World Models
---

# Training Agents Inside of Scalable World Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24527" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24527v1</a>
  <a href="https://arxiv.org/pdf/2509.24527.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24527v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24527v1', 'Training Agents Inside of Scalable World Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Danijar Hafner, Wilson Yan, Timothy Lillicrap

**分类**: cs.AI, cs.LG, cs.RO, stat.ML

**发布日期**: 2025-09-29

**备注**: Website: https://danijar.com/dreamer4/

---

## 💡 一句话要点

**Dreamer 4：通过可扩展世界模型在Minecraft中实现离线钻石获取**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `世界模型` `强化学习` `离线学习` `Minecraft` `Transformer`

## 📋 核心要点

1. 现有世界模型在复杂环境中预测物体交互方面存在不足，限制了智能体的能力。
2. Dreamer 4通过学习快速且精确的世界模型，并在其中进行强化学习，从而解决控制任务。
3. Dreamer 4在Minecraft中仅使用离线数据成功获取钻石，证明了其在复杂环境中的有效性。

## 📝 摘要（中文）

本文提出了Dreamer 4，一个可扩展的智能体，它通过在快速且精确的世界模型中进行强化学习来解决控制任务。在复杂的视频游戏Minecraft中，该世界模型能够准确预测物体交互和游戏机制，显著优于以往的世界模型。该模型通过shortcut forcing objective和高效的Transformer架构，在单个GPU上实现了实时交互推理。此外，该世界模型仅需少量数据即可学习通用的动作条件，从而能够从各种未标记的视频中提取大部分知识。本文提出了一个挑战，即仅从离线数据在Minecraft中获取钻石，这与机器人等实际应用相符，因为从环境交互中学习可能不安全且缓慢。Dreamer 4通过在想象中学习行为，成为第一个仅从离线数据在Minecraft中获得钻石而无需环境交互的智能体。这项工作为想象训练提供了一个可扩展的方案，标志着朝着智能体迈出了一步。

## 🔬 方法详解

**问题定义**：现有世界模型在复杂环境中，尤其是在涉及物体交互时，预测精度不足，导致智能体难以学习有效的策略。在Minecraft这类复杂游戏中，精确预测物体交互和游戏机制是实现目标的关键。此外，从环境交互中学习可能成本高昂甚至不安全，因此需要能够从离线数据中学习的智能体。

**核心思路**：Dreamer 4的核心思路是构建一个快速且精确的世界模型，并在该模型中进行强化学习。通过学习环境的动态特性，智能体可以在想象中进行策略学习，从而避免与真实环境的直接交互。这种方法可以显著提高学习效率和安全性。

**技术框架**：Dreamer 4的整体框架包括以下几个主要模块：1) 视频编码器：将原始像素输入转换为潜在状态表示。2) 世界模型：学习环境的动态特性，包括状态转移和奖励预测。3) 策略网络：根据世界模型的预测，选择最优的动作。4) 价值网络：评估当前状态的价值，用于指导策略学习。该框架采用循环结构，智能体根据当前状态选择动作，世界模型预测下一个状态和奖励，策略和价值网络根据预测结果进行更新。

**关键创新**：Dreamer 4的关键创新在于其世界模型的架构和训练方式。首先，它采用了shortcut forcing objective，这有助于提高世界模型的预测精度。其次，它使用了高效的Transformer架构，从而实现了实时交互推理。此外，该模型能够从少量数据中学习通用的动作条件，从而可以从大量未标记的视频中提取知识。

**关键设计**：Dreamer 4的世界模型使用了VAE（Variational Autoencoder）来学习潜在状态表示。Transformer架构用于建模状态之间的转移关系。shortcut forcing objective通过在训练过程中强制模型预测真实状态，从而提高预测精度。策略和价值网络使用Actor-Critic算法进行训练。具体参数设置未知。

## 📊 实验亮点

Dreamer 4在Minecraft中仅使用离线数据成功获取钻石，这是第一个实现该目标的智能体。该模型在预测物体交互和游戏机制方面显著优于以往的世界模型，实现了实时交互推理。这些结果表明Dreamer 4在复杂环境中的学习能力和泛化能力。

## 🎯 应用场景

Dreamer 4的技术可应用于机器人、自动驾驶、游戏AI等领域。在机器人领域，可以利用离线数据训练机器人，使其能够在复杂环境中完成任务，例如物体抓取、导航等。在自动驾驶领域，可以利用模拟数据训练自动驾驶系统，提高其在各种交通场景下的安全性和可靠性。在游戏AI领域，可以开发更智能的游戏角色，提高游戏的趣味性和挑战性。

## 📄 摘要（原文）

> World models learn general knowledge from videos and simulate experience for training behaviors in imagination, offering a path towards intelligent agents. However, previous world models have been unable to accurately predict object interactions in complex environments. We introduce Dreamer 4, a scalable agent that learns to solve control tasks by reinforcement learning inside of a fast and accurate world model. In the complex video game Minecraft, the world model accurately predicts object interactions and game mechanics, outperforming previous world models by a large margin. The world model achieves real-time interactive inference on a single GPU through a shortcut forcing objective and an efficient transformer architecture. Moreover, the world model learns general action conditioning from only a small amount of data, allowing it to extract the majority of its knowledge from diverse unlabeled videos. We propose the challenge of obtaining diamonds in Minecraft from only offline data, aligning with practical applications such as robotics where learning from environment interaction can be unsafe and slow. This task requires choosing sequences of over 20,000 mouse and keyboard actions from raw pixels. By learning behaviors in imagination, Dreamer 4 is the first agent to obtain diamonds in Minecraft purely from offline data, without environment interaction. Our work provides a scalable recipe for imagination training, marking a step towards intelligent agents.

