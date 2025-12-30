---
layout: default
title: "LiveTalk: Real-Time Multimodal Interactive Video Diffusion via Improved On-Policy Distillation"
---

# LiveTalk: Real-Time Multimodal Interactive Video Diffusion via Improved On-Policy Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23576" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23576v1</a>
  <a href="https://arxiv.org/pdf/2512.23576.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23576v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23576v1', 'LiveTalk: Real-Time Multimodal Interactive Video Diffusion via Improved On-Policy Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ethan Chern, Zhulin Hu, Bohao Tang, Jiadi Su, Steffi Chern, Zhijie Deng, Pengfei Liu

**分类**: cs.CV

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出改进的On-Policy蒸馏方法，实现多模态交互式实时视频扩散**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `实时视频生成` `多模态交互` `扩散模型` `On-Policy蒸馏` `人机交互`

## 📋 核心要点

1. 现有扩散模型在实时视频生成中面临挑战，特别是多模态条件下的交互式应用，主要原因是其双向注意力和迭代采样过程。
2. 论文提出改进的On-Policy蒸馏方法，通过优化条件输入质量和蒸馏过程，显著提升了多模态条件下的视频生成效率和质量。
3. 实验结果表明，该方法在保证视觉质量的同时，显著降低了推理成本和延迟，并在多轮交互场景中优于现有先进模型。

## 📝 摘要（中文）

本文旨在解决多模态交互式AI系统中实时视频生成的问题。现有的扩散模型由于其迭代过程中的双向注意力机制，难以实现实时交互。虽然蒸馏方法可以通过自回归建模和减少采样步骤来缓解这个问题，但它们主要集中在文本到视频的生成，导致人机交互不自然且效率低下。本文提出了一种改进的蒸馏方法，重点关注条件输入的质量以及On-Policy优化的初始化和调度，以实现基于文本、图像和音频等多模态上下文的实时交互式视频扩散。在HDTF、AVSpeech和CelebV-HQ等数据集上的实验表明，该模型在视觉质量上与全步、双向基线模型相当，同时推理成本和延迟降低了20倍。此外，该模型集成了音频语言模型和Anchor-Heavy Identity Sinks长视频推理技术，构建了LiveTalk实时多模态交互式化身系统。系统级评估表明，LiveTalk在多轮视频连贯性和内容质量方面优于Sora2和Veo3等模型，并将响应延迟从1-2分钟降低到实时生成，从而实现无缝的人机多模态交互。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态交互式AI系统中实时视频生成的问题。现有扩散模型由于其迭代过程中的双向注意力机制，难以实现实时交互。现有的蒸馏方法虽然可以加速生成，但在多模态条件下的效果不佳，容易出现视觉伪影，如闪烁、黑帧和质量下降。

**核心思路**：论文的核心思路是通过改进On-Policy蒸馏方法，提高多模态条件下的视频生成质量和效率。关键在于优化条件输入的质量，并改进On-Policy优化的初始化和调度策略。通过高质量的条件输入和更有效的蒸馏过程，可以生成更逼真、更连贯的视频。

**技术框架**：整体框架包括一个多模态条件编码器，用于将文本、图像和音频信息编码为潜在表示。然后，使用改进的On-Policy蒸馏方法训练一个自回归扩散模型，该模型能够根据潜在表示生成视频帧。最后，将该模型集成到LiveTalk系统中，实现实时多模态交互。

**关键创新**：最重要的技术创新点在于改进的On-Policy蒸馏方法，该方法特别关注条件输入的质量以及蒸馏过程的优化。与传统的蒸馏方法相比，该方法能够更好地处理多模态条件，并生成更高质量的视频。此外，LiveTalk系统的集成也展示了该方法在实际应用中的潜力。

**关键设计**：论文中关键的设计包括：(1) 使用高质量的多模态数据进行训练，确保条件输入的准确性；(2) 改进On-Policy优化的初始化策略，避免训练初期出现不稳定的情况；(3) 调整蒸馏过程中的调度策略，平衡生成速度和视频质量；(4) 使用Anchor-Heavy Identity Sinks技术，提高长视频的连贯性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23576v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23576v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23576v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该模型在HDTF、AVSpeech和CelebV-HQ等数据集上，在视觉质量上与全步、双向基线模型相当，同时推理成本和延迟降低了20倍。在多轮交互场景中，LiveTalk系统在视频连贯性和内容质量方面优于Sora2和Veo3等模型，并将响应延迟从1-2分钟降低到实时生成。

## 🎯 应用场景

该研究成果可广泛应用于虚拟化身、在线会议、游戏、教育等领域。通过实时多模态交互，可以创建更自然、更具吸引力的用户体验。例如，用户可以与虚拟化身进行实时对话，并根据用户的语音、表情和文本输入，生成相应的视频内容。未来，该技术有望进一步发展，实现更高级的人机交互。

## 📄 摘要（原文）

> Real-time video generation via diffusion is essential for building general-purpose multimodal interactive AI systems. However, the simultaneous denoising of all video frames with bidirectional attention via an iterative process in diffusion models prevents real-time interaction. While existing distillation methods can make the model autoregressive and reduce sampling steps to mitigate this, they focus primarily on text-to-video generation, leaving the human-AI interaction unnatural and less efficient. This paper targets real-time interactive video diffusion conditioned on a multimodal context, including text, image, and audio, to bridge the gap. Given the observation that the leading on-policy distillation approach Self Forcing encounters challenges (visual artifacts like flickering, black frames, and quality degradation) with multimodal conditioning, we investigate an improved distillation recipe with emphasis on the quality of condition inputs as well as the initialization and schedule for the on-policy optimization. On benchmarks for multimodal-conditioned (audio, image, and text) avatar video generation including HDTF, AVSpeech, and CelebV-HQ, our distilled model matches the visual quality of the full-step, bidirectional baselines of similar or larger size with 20x less inference cost and latency. Further, we integrate our model with audio language models and long-form video inference technique Anchor-Heavy Identity Sinks to build LiveTalk, a real-time multimodal interactive avatar system. System-level evaluation on our curated multi-turn interaction benchmark shows LiveTalk outperforms state-of-the-art models (Sora2, Veo3) in multi-turn video coherence and content quality, while reducing response latency from 1 to 2 minutes to real-time generation, enabling seamless human-AI multimodal interaction.

