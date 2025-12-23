---
layout: default
title: Real-Time Streamable Generative Speech Restoration with Flow Matching
---

# Real-Time Streamable Generative Speech Restoration with Flow Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19442" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19442v1</a>
  <a href="https://arxiv.org/pdf/2512.19442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19442v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19442v1', 'Real-Time Streamable Generative Speech Restoration with Flow Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Simon Welker, Bunlong Lay, Maris Hillemann, Tal Peer, Timo Gerkmann

**分类**: eess.SP, cs.LG, cs.SD

**发布日期**: 2025-12-22

**备注**: This work has been submitted to the IEEE for possible publication

---

## 💡 一句话要点

**提出Stream.FM：一种实时流式生成语音恢复Flow Matching模型，延迟低至48ms。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `流式语音处理` `语音增强` `Flow Matching` `实时通信` `生成模型` `低延迟` `语音恢复`

## 📋 核心要点

1. 现有基于扩散的语音生成模型计算量大，难以应用于实时通信场景。
2. 提出Stream.FM，一种基于Flow Matching的流式生成模型，降低延迟并优化模型结构。
3. 实验表明，Stream.FM在多种语音处理任务上达到SOTA，且延迟远低于现有方法。

## 📝 摘要（中文）

近年来，基于扩散的生成模型对语音处理领域产生了巨大影响，展现出高度的语音自然度，并催生了一个新的研究方向。然而，由于其计算密集型特性，涉及多次调用大型DNN，它们在实时通信中的应用仍然滞后。本文提出Stream.FM，一种帧因果的基于流的生成模型，算法延迟为32毫秒（ms），总延迟为48毫秒，为实时通信中的生成语音处理铺平了道路。我们提出了一种缓冲流式推理方案和优化的DNN架构，展示了如何通过学习的少步数值求解器在固定的计算预算下提高输出质量，探索了模型权重压缩以找到计算/质量权衡的有利点，并贡献了一个总延迟为24毫秒的语音增强任务模型变体。我们的工作超越了理论延迟，表明高质量的流式生成语音处理可以在当今可用的消费级GPU上实现。Stream.FM可以以流式方式解决各种语音处理任务：语音增强、去混响、编解码器后滤波、带宽扩展、STFT相位检索和Mel声码器。正如我们通过全面的评估和MUSHRA听力测试所验证的那样，Stream.FM为生成流式语音恢复建立了最先进的水平，与非流式变体相比，质量仅有合理的降低，并且在更低的延迟下优于我们最近在生成流式语音增强方面的工作（Diffusion Buffer）。

## 🔬 方法详解

**问题定义**：论文旨在解决实时通信中生成语音处理的延迟问题。现有的基于扩散的生成模型虽然能产生高质量的语音，但由于计算复杂度高，难以满足实时性要求，限制了其在实时语音增强、去混响等场景的应用。

**核心思路**：论文的核心思路是利用Flow Matching模型，并结合流式推理和模型优化，在保证语音质量的前提下，显著降低模型的延迟。Flow Matching相比扩散模型，训练和推理效率更高，更适合实时应用。

**技术框架**：Stream.FM的整体框架包括以下几个主要部分：1) 帧因果的Flow Matching模型：使用Flow Matching作为生成模型的核心，保证模型的生成能力。2) 缓冲流式推理方案：通过缓冲输入帧，实现流式推理，降低延迟。3) 优化的DNN架构：设计高效的DNN结构，减少计算量。4) 少步数值求解器：学习高效的数值求解器，在有限的计算资源下提升输出质量。5) 模型权重压缩：通过模型压缩，进一步降低计算量和延迟。

**关键创新**：论文的关键创新在于将Flow Matching模型应用于流式语音处理，并提出了一系列优化方法，包括缓冲流式推理、优化的DNN架构、少步数值求解器和模型权重压缩。这些创新使得Stream.FM能够在保证语音质量的前提下，实现极低的延迟，满足实时通信的需求。

**关键设计**：在模型设计上，论文采用了帧因果的结构，保证了流式处理的实时性。在训练过程中，使用了特定的损失函数来优化模型的生成质量和稳定性。在推理过程中，通过调整缓冲大小和数值求解器的步数，可以灵活地权衡计算量和语音质量。此外，论文还探索了不同的模型权重压缩方法，以进一步降低模型的计算复杂度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19442v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19442v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19442v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Stream.FM实现了48ms的总延迟，算法延迟为32ms，在生成流式语音恢复任务上达到了SOTA水平。与非流式变体相比，质量仅有合理的降低。在语音增强任务上，Stream.FM在更低的延迟下优于Diffusion Buffer。MUSHRA听力测试验证了Stream.FM的优越性能。

## 🎯 应用场景

Stream.FM具有广泛的应用前景，可用于实时语音增强、去混响、编解码器后滤波、带宽扩展、STFT相位检索和Mel声码器等领域。该技术可以提升实时通信的语音质量和清晰度，改善用户体验，尤其是在网络条件较差或设备性能有限的情况下，其价值更为突出。未来，Stream.FM有望应用于在线会议、语音助手、游戏语音等多种场景。

## 📄 摘要（原文）

> Diffusion-based generative models have greatly impacted the speech processing field in recent years, exhibiting high speech naturalness and spawning a new research direction. Their application in real-time communication is, however, still lagging behind due to their computation-heavy nature involving multiple calls of large DNNs.
>   Here, we present Stream.FM, a frame-causal flow-based generative model with an algorithmic latency of 32 milliseconds (ms) and a total latency of 48 ms, paving the way for generative speech processing in real-time communication. We propose a buffered streaming inference scheme and an optimized DNN architecture, show how learned few-step numerical solvers can boost output quality at a fixed compute budget, explore model weight compression to find favorable points along a compute/quality tradeoff, and contribute a model variant with 24 ms total latency for the speech enhancement task.
>   Our work looks beyond theoretical latencies, showing that high-quality streaming generative speech processing can be realized on consumer GPUs available today. Stream.FM can solve a variety of speech processing tasks in a streaming fashion: speech enhancement, dereverberation, codec post-filtering, bandwidth extension, STFT phase retrieval, and Mel vocoding. As we verify through comprehensive evaluations and a MUSHRA listening test, Stream.FM establishes a state-of-the-art for generative streaming speech restoration, exhibits only a reasonable reduction in quality compared to a non-streaming variant, and outperforms our recent work (Diffusion Buffer) on generative streaming speech enhancement while operating at a lower latency.

