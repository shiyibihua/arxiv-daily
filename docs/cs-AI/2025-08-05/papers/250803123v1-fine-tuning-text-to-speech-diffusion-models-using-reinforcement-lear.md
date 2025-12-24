---
layout: default
title: Fine-Tuning Text-to-Speech Diffusion Models Using Reinforcement Learning with Human Feedback
---

# Fine-Tuning Text-to-Speech Diffusion Models Using Reinforcement Learning with Human Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03123" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03123v1</a>
  <a href="https://arxiv.org/pdf/2508.03123.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03123v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03123v1', 'Fine-Tuning Text-to-Speech Diffusion Models Using Reinforcement Learning with Human Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingyi Chen, Ju Seung Byun, Micha Elsner, Pichao Wang, Andrew Perrault

**分类**: cs.SD, cs.AI, eess.AS

**发布日期**: 2025-08-05

**备注**: 4 pages, 1 figure, INTERSPEECH 2025. arXiv admin note: text overlap with arXiv:2405.14632

**期刊**: INTERSPEECH 2025

---

## 💡 一句话要点

**提出DLPO框架以提升TTS扩散模型的实时性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散模型` `语音合成` `强化学习` `人类反馈` `自然度评分` `实时应用` `优化策略`

## 📋 核心要点

1. 现有的扩散模型在生成高质量语音时效率低下，尤其是在实时应用中，去噪步骤过长且难以建模声调和节奏。
2. 本文提出的DLPO框架通过将训练损失纳入奖励函数，结合强化学习与人类反馈，优化了TTS扩散模型的性能。
3. 实验结果显示，DLPO在WaveGrad 2模型上显著提升了语音质量，客观指标和主观评估均有显著改善。

## 📝 摘要（中文）

扩散模型能够生成高保真语音，但由于去噪步骤长和声调、节奏建模的挑战，实时使用效率低下。为此，本文提出了Diffusion Loss-Guided Policy Optimization（DLPO），这是一个基于人类反馈的强化学习框架，旨在优化TTS扩散模型。DLPO将原始训练损失整合进奖励函数中，保留生成能力的同时减少低效。通过自然度评分作为反馈，DLPO使奖励优化与扩散模型结构对齐，从而提升语音质量。实验结果表明，DLPO在WaveGrad 2模型上显著提高了客观指标（UTMOS 3.65，NISQA 4.02）和主观评估，DLPO生成的音频在67%的时间内被偏好。这些发现展示了DLPO在实时、资源有限环境中实现高效高质量扩散TTS的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散模型在实时语音合成中的低效问题，现有方法在去噪步骤和声调、节奏建模方面存在显著挑战。

**核心思路**：DLPO框架通过将原始训练损失整合到奖励函数中，利用强化学习与人类反馈相结合的方式，优化生成过程，提升语音合成的自然度和效率。

**技术框架**：DLPO的整体架构包括奖励函数设计、反馈机制和优化策略。首先，通过自然度评分获取人类反馈，然后将其与训练损失结合，形成新的奖励信号，最后通过强化学习算法进行优化。

**关键创新**：DLPO的核心创新在于将传统的训练损失与奖励信号结合，形成了一种新的优化策略，使得模型在保持生成能力的同时，显著提高了效率。与现有方法相比，DLPO更好地适应了扩散模型的结构特性。

**关键设计**：在DLPO中，奖励函数的设计至关重要，采用自然度评分作为反馈，确保优化过程与人类感知一致。此外，模型的参数设置和网络结构经过精心设计，以适应强化学习的需求。具体细节包括对损失函数的调整和对模型训练过程的动态调整。

## 📊 实验亮点

实验结果表明，DLPO在WaveGrad 2模型上的客观指标显著提升，UTMOS达到3.65，NISQA达到4.02。同时，主观评估显示，DLPO生成的音频在67%的时间内被用户偏好，展示了其在语音合成质量上的显著改进。

## 🎯 应用场景

该研究的潜在应用领域包括实时语音合成、虚拟助手、语音翻译等。通过提升扩散模型的效率，DLPO能够在资源有限的环境中实现高质量的语音生成，具有广泛的实际价值和应用前景。未来，随着技术的进一步发展，DLPO可能会在更多的语音交互场景中得到应用，推动智能语音技术的进步。

## 📄 摘要（原文）

> Diffusion models produce high-fidelity speech but are inefficient for real-time use due to long denoising steps and challenges in modeling intonation and rhythm. To improve this, we propose Diffusion Loss-Guided Policy Optimization (DLPO), an RLHF framework for TTS diffusion models. DLPO integrates the original training loss into the reward function, preserving generative capabilities while reducing inefficiencies. Using naturalness scores as feedback, DLPO aligns reward optimization with the diffusion model's structure, improving speech quality. We evaluate DLPO on WaveGrad 2, a non-autoregressive diffusion-based TTS model. Results show significant improvements in objective metrics (UTMOS 3.65, NISQA 4.02) and subjective evaluations, with DLPO audio preferred 67\% of the time. These findings demonstrate DLPO's potential for efficient, high-quality diffusion TTS in real-time, resource-limited settings.

