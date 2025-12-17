---
layout: default
title: PAN: A World Model for General, Interactable, and Long-Horizon World Simulation
---

# PAN: A World Model for General, Interactable, and Long-Horizon World Simulation

**arXiv**: [2511.09057v3](https://arxiv.org/abs/2511.09057) | [PDF](https://arxiv.org/pdf/2511.09057.pdf)

**作者**: PAN Team, Jiannan Xiang, Yi Gu, Zihan Liu, Zeyu Feng, Qiyue Gao, Yiyan Hu, Benhao Huang, Guangyi Liu, Yichi Yang, Kun Zhou, Davit Abrahamyan, Arif Ahmad, Ganesh Bannur, Junrong Chen, Kimi Chen, Mingkai Deng, Ruobing Han, Xinqi Huang, Haoqiang Kang, Zheqi Liu, Enze Ma, Hector Ren, Yashowardhan Shinde, Rohan Shingre, Ramsundar Tanikella, Kaiming Tao, Dequan Yang, Xinle Yu, Cong Zeng, Binglin Zhou, Zhengzhong Liu, Zhiting Hu, Eric P. Xing

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-11-12 (更新: 2025-11-15)

---

## 💡 一句话要点

**PAN：通用、可交互、长时程世界模拟的世界模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `世界模型` `视频生成` `大型语言模型` `扩散模型` `动作条件模拟` `长时程预测` `通用人工智能`

## 📋 核心要点

1. 现有世界模型在泛化性、交互性和长期一致性方面存在不足，难以应用于复杂环境。
2. PAN模型利用生成潜在预测架构，结合大型语言模型和视频扩散模型，实现基于语言动作条件的高质量视频模拟。
3. 实验表明，PAN在动作条件世界模拟和长时程预测方面优于现有模型，为通用世界模型发展奠定基础。

## 📝 摘要（中文）

世界模型使智能体能够想象、预测和推理世界如何响应其行为而演变，并据此进行规划和制定策略。虽然最近的视频生成模型可以生成逼真的视觉序列，但它们通常以提示到完整视频的方式运行，缺乏因果控制、交互性或长期一致性，而这些对于有目的的推理是必需的。现有的世界建模工作通常侧重于受限领域（例如，物理、游戏或3D场景动态），深度和可控性有限，并且难以推广到不同的环境和交互形式。本文介绍了PAN，一种通用、可交互和长时程的世界模型，它通过高质量的视频模拟来预测未来的世界状态，该模拟以历史和自然语言动作为条件。PAN采用生成潜在预测（GLP）架构，该架构结合了基于大型语言模型（LLM）的自回归潜在动态骨干，这使模拟基于广泛的基于文本的知识并能够以语言指定的动作为条件，以及视频扩散解码器，该解码器重建感知上详细且时间上连贯的视觉观察，以实现潜在空间推理（想象）和可实现的世界动态（现实）之间的统一。PAN在跨越不同领域的大规模视频-动作对上进行训练，支持具有连贯的长期动态的开放域、动作条件模拟。大量的实验表明，与其他视频生成器和世界模型相比，PAN在动作条件世界模拟、长时程预测和模拟推理方面取得了强大的性能，朝着实现能够预测模拟未来世界状态以进行推理和行动的通用世界模型迈出了一步。

## 🔬 方法详解

**问题定义**：现有世界模型通常局限于特定领域，例如物理模拟或游戏环境，缺乏在开放域中进行通用模拟的能力。它们在处理复杂交互和维持长期一致性方面也存在挑战，无法满足智能体进行有效推理和规划的需求。现有方法的痛点在于缺乏通用性、交互性和长期一致性。

**核心思路**：PAN的核心思路是将大型语言模型（LLM）的知识推理能力与视频扩散模型的视觉生成能力相结合，构建一个能够理解语言指令并生成高质量、长期一致视频的世界模型。通过在潜在空间中进行推理，PAN能够更好地模拟世界的动态变化，并预测未来状态。

**技术框架**：PAN采用生成潜在预测（GLP）架构，主要包含以下模块：1) **LLM-based Latent Dynamics Backbone**: 使用大型语言模型作为自回归模型，学习潜在空间中的动态变化规律，并以语言动作作为条件。2) **Video Diffusion Decoder**: 将潜在空间中的表示解码为高质量的视频帧，保证视觉细节和时间连贯性。整个流程是，首先将历史视频帧和语言动作编码到潜在空间，然后利用LLM预测未来的潜在状态，最后通过视频扩散解码器生成对应的视频帧。

**关键创新**：PAN的关键创新在于将大型语言模型引入世界模型，从而利用LLM的知识推理能力和语言理解能力，实现更通用、更可控的世界模拟。此外，PAN采用视频扩散模型作为解码器，能够生成更高质量、更逼真的视频，克服了传统生成模型在视觉细节和时间连贯性方面的不足。将LLM的推理能力和扩散模型的生成能力结合是其核心创新。

**关键设计**：PAN的关键设计包括：1) **Latent Space Representation**: 如何有效地将视频帧和语言动作编码到潜在空间，并保证信息的完整性和可解释性。2) **LLM Training**: 如何训练LLM，使其能够准确地预测潜在空间中的动态变化，并对语言动作做出合理的响应。3) **Diffusion Decoder Training**: 如何训练视频扩散解码器，使其能够生成高质量、时间连贯的视频帧。具体的参数设置、损失函数和网络结构等细节在论文中有详细描述，这里不再赘述。

## 📊 实验亮点

PAN在多个实验中表现出色，在动作条件世界模拟、长时程预测和模拟推理方面均优于其他视频生成器和世界模型。具体而言，PAN能够生成更逼真、更连贯的视频，并且能够更好地响应语言动作的指令。实验结果表明，PAN在模拟复杂环境和预测长期动态方面具有显著优势。

## 🎯 应用场景

PAN具有广泛的应用前景，例如机器人控制、自动驾驶、游戏AI和虚拟现实。它可以帮助机器人更好地理解环境，预测行为后果，从而做出更明智的决策。在自动驾驶领域，PAN可以用于模拟各种交通场景，提高自动驾驶系统的安全性和可靠性。在游戏AI领域，PAN可以用于生成更智能、更逼真的游戏角色。在虚拟现实领域，PAN可以用于创建更沉浸式的虚拟体验。

## 📄 摘要（原文）

> A world model enables an intelligent agent to imagine, predict, and reason about how the world evolves in response to its actions, and accordingly to plan and strategize. While recent video generation models produce realistic visual sequences, they typically operate in the prompt-to-full-video manner without causal control, interactivity, or long-horizon consistency required for purposeful reasoning. Existing world modeling efforts, on the other hand, often focus on restricted domains (e.g., physical, game, or 3D-scene dynamics) with limited depth and controllability, and struggle to generalize across diverse environments and interaction formats. In this work, we introduce PAN, a general, interactable, and long-horizon world model that predicts future world states through high-quality video simulation conditioned on history and natural language actions. PAN employs the Generative Latent Prediction (GLP) architecture that combines an autoregressive latent dynamics backbone based on a large language model (LLM), which grounds simulation in extensive text-based knowledge and enables conditioning on language-specified actions, with a video diffusion decoder that reconstructs perceptually detailed and temporally coherent visual observations, to achieve a unification between latent space reasoning (imagination) and realizable world dynamics (reality). Trained on large-scale video-action pairs spanning diverse domains, PAN supports open-domain, action-conditioned simulation with coherent, long-term dynamics. Extensive experiments show that PAN achieves strong performance in action-conditioned world simulation, long-horizon forecasting, and simulative reasoning compared to other video generators and world models, taking a step towards general world models that enable predictive simulation of future world states for reasoning and acting.

