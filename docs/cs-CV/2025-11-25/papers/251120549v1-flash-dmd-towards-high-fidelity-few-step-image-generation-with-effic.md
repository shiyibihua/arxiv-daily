---
layout: default
title: Flash-DMD: Towards High-Fidelity Few-Step Image Generation with Efficient Distillation and Joint Reinforcement Learning
---

# Flash-DMD: Towards High-Fidelity Few-Step Image Generation with Efficient Distillation and Joint Reinforcement Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.20549" target="_blank" class="toolbar-btn">arXiv: 2511.20549v1</a>
    <a href="https://arxiv.org/pdf/2511.20549.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20549v1" 
            onclick="toggleFavorite(this, '2511.20549v1', 'Flash-DMD: Towards High-Fidelity Few-Step Image Generation with Efficient Distillation and Joint Reinforcement Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Guanjie Chen, Shirui Huang, Kai Liu, Jianchen Zhu, Xiaoye Qu, Peng Chen, Yu Cheng, Yifu Sun

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-25

---

## 💡 一句话要点

**Flash-DMD：通过高效蒸馏与联合强化学习实现高保真快速图像生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散模型` `图像生成` `时间步蒸馏` `强化学习` `联合训练` `快速采样` `模型加速`

## 📋 核心要点

1. 扩散模型生成图像质量高但采样速度慢，时间步蒸馏是加速方法，但训练成本高且质量易下降。
2. Flash-DMD提出高效的时间步感知蒸馏策略，降低训练成本并提升图像真实感，同时避免质量下降。
3. Flash-DMD采用联合训练方案，将强化学习微调与蒸馏训练结合，利用蒸馏损失稳定强化学习过程。

## 📝 摘要（中文）

扩散模型已成为领先的生成模型，但其迭代采样过程计算成本高昂。时间步蒸馏是一种很有前景的加速生成技术，但它通常需要大量的训练，并导致图像质量下降。此外，使用强化学习（RL）对这些蒸馏模型进行微调以实现特定目标（如美学吸引力或用户偏好）非常不稳定，并且容易陷入奖励利用。本文介绍了一种新颖的框架Flash-DMD，该框架能够通过蒸馏和基于联合RL的细化实现快速收敛。具体来说，我们首先提出了一种高效的、时间步感知的蒸馏策略，该策略显著降低了训练成本并增强了真实感，仅用DMD2的2.1%的训练成本就超越了它。其次，我们引入了一种联合训练方案，其中模型在RL目标下进行微调，同时时间步蒸馏训练持续进行。我们证明了来自持续蒸馏的稳定、定义明确的损失充当了强大的正则化器，有效地稳定了RL训练过程并防止策略崩溃。在基于分数的模型和流匹配模型上的大量实验表明，我们提出的Flash-DMD不仅收敛速度显著加快，而且在少步采样机制中实现了最先进的生成质量，在视觉质量、人类偏好和文本-图像对齐指标方面均优于现有方法。我们的工作为训练高效、高保真和稳定的生成模型提供了一种有效的范例。

## 🔬 方法详解

**问题定义**：扩散模型生成图像质量高，但需要多次迭代采样，计算成本高昂。时间步蒸馏旨在减少采样步骤，加速生成过程，但现有蒸馏方法通常需要大量的训练资源，并且容易导致生成图像质量下降，同时，使用强化学习对蒸馏后的模型进行微调以适应特定目标时，容易出现训练不稳定和奖励利用的问题。

**核心思路**：Flash-DMD的核心思路是通过高效的蒸馏策略降低训练成本，并利用联合训练的方式，将时间步蒸馏与强化学习微调相结合。蒸馏过程提供稳定的损失函数，作为强化学习的正则化项，从而稳定强化学习的训练过程，避免策略崩溃。

**技术框架**：Flash-DMD包含两个主要阶段：高效的时间步感知蒸馏和联合强化学习微调。首先，使用提出的蒸馏策略训练一个快速采样的生成模型。然后，在蒸馏训练的同时，使用强化学习对模型进行微调，以优化特定目标（如美学评分）。蒸馏损失作为强化学习的正则化项，确保训练过程的稳定。

**关键创新**：Flash-DMD的关键创新在于：1) 提出了一种高效的时间步感知蒸馏策略，显著降低了训练成本，同时保持了图像质量。2) 引入了一种联合训练方案，将时间步蒸馏与强化学习微调相结合，利用蒸馏损失作为强化学习的正则化项，稳定了强化学习的训练过程。

**关键设计**：在时间步感知蒸馏中，设计了特定的损失函数，以更好地保留不同时间步的信息。在联合训练中，强化学习的奖励函数与蒸馏损失函数进行加权组合，权重系数需要仔细调整，以平衡生成质量和特定目标优化。具体的网络结构和参数设置取决于所使用的扩散模型架构。

## 📊 实验亮点

Flash-DMD在少步采样机制中实现了最先进的生成质量，在视觉质量、人类偏好和文本-图像对齐指标方面均优于现有方法。例如，在相同的训练成本下，Flash-DMD的生成质量显著优于DMD2，并且能够稳定地进行强化学习微调，避免策略崩溃。实验结果表明，Flash-DMD是一种高效、高保真和稳定的图像生成方法。

## 🎯 应用场景

Flash-DMD可应用于各种需要快速图像生成的场景，例如：游戏开发、虚拟现实、内容创作、图像编辑等。该方法能够以较低的计算成本生成高质量的图像，并可以根据用户偏好进行定制，具有广泛的应用前景。未来，该技术可能被用于实时图像生成、个性化内容推荐等领域。

## 📄 摘要（原文）

> Diffusion Models have emerged as a leading class of generative models, yet their iterative sampling process remains computationally expensive. Timestep distillation is a promising technique to accelerate generation, but it often requires extensive training and leads to image quality degradation. Furthermore, fine-tuning these distilled models for specific objectives, such as aesthetic appeal or user preference, using Reinforcement Learning (RL) is notoriously unstable and easily falls into reward hacking. In this work, we introduce Flash-DMD, a novel framework that enables fast convergence with distillation and joint RL-based refinement. Specifically, we first propose an efficient timestep-aware distillation strategy that significantly reduces training cost with enhanced realism, outperforming DMD2 with only $2.1\%$ its training cost. Second, we introduce a joint training scheme where the model is fine-tuned with an RL objective while the timestep distillation training continues simultaneously. We demonstrate that the stable, well-defined loss from the ongoing distillation acts as a powerful regularizer, effectively stabilizing the RL training process and preventing policy collapse. Extensive experiments on score-based and flow matching models show that our proposed Flash-DMD not only converges significantly faster but also achieves state-of-the-art generation quality in the few-step sampling regime, outperforming existing methods in visual quality, human preference, and text-image alignment metrics. Our work presents an effective paradigm for training efficient, high-fidelity, and stable generative models. Codes are coming soon.

