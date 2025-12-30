---
layout: default
title: SoulX-LiveTalk Technical Report
---

# SoulX-LiveTalk Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23379" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23379v1</a>
  <a href="https://arxiv.org/pdf/2512.23379.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23379v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23379v1', 'SoulX-LiveTalk Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Le Shen, Qiao Qian, Tan Yu, Ke Zhou, Tianhang Yu, Yu Zhan, Zhenjie Wang, Ming Tao, Shunshun Yin, Siyuan Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-29

**备注**: 12 pages, 6 figures

---

## 💡 一句话要点

**提出SoulX-LiveTalk框架，实现高保真实时音频驱动的数字人生成。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `数字人生成` `实时渲染` `扩散模型` `双向注意力` `自校正机制` `模型蒸馏` `推理加速` `音频驱动`

## 📋 核心要点

1. 现有方法在实时数字人生成中，为满足延迟约束，常牺牲视觉保真度，例如采用单向注意力或降低模型容量。
2. SoulX-LiveTalk采用自校正双向蒸馏，保留时空相关性，并引入多步回顾自校正机制，确保生成稳定性。
3. SoulX-LiveTalk实现了0.87秒的启动延迟和32 FPS的实时吞吐量，为140亿参数规模系统设立了新标准。

## 📝 摘要（中文）

本文提出SoulX-LiveTalk，一个参数量为140亿的框架，专为高保真实时流媒体应用优化。针对大规模扩散模型在实时、无限时长、音频驱动的数字人生成中面临的计算负载与严格延迟约束之间的矛盾，该框架采用自校正双向蒸馏策略，在视频块内保留双向注意力，从而保留关键的时空相关性，显著增强运动连贯性和视觉细节。为了确保无限生成过程中的稳定性，引入多步回顾自校正机制，使模型能够自主地从累积误差中恢复并防止崩溃。此外，还设计了全栈推理加速套件，包括混合序列并行、并行VAE和内核级优化。实验结果表明，SoulX-LiveTalk是首个实现亚秒级启动延迟（0.87秒）并达到32 FPS实时吞吐量的140亿参数规模系统，为高保真交互式数字人合成树立了新标准。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模扩散模型在实时、无限时长、音频驱动的数字人生成任务中，计算负载高和延迟要求严格之间的矛盾。现有方法为了满足实时性，通常会牺牲生成质量，例如采用严格的单向注意力机制或者降低模型容量，导致生成的数字人在运动连贯性和视觉细节上表现不佳。

**核心思路**：SoulX-LiveTalk的核心思路是在保证实时性的前提下，尽可能保留模型的表达能力和生成质量。为此，论文提出了自校正双向蒸馏策略，以保留视频块内的双向注意力，从而捕捉更丰富的时空信息。同时，为了解决无限生成过程中可能出现的误差累积和模型崩溃问题，引入了多步回顾自校正机制。

**技术框架**：SoulX-LiveTalk的整体框架包含以下几个主要模块：1) 音频特征提取模块：用于提取输入音频的特征表示。2) 扩散模型：基于扩散模型的生成器，负责将音频特征转化为高保真的数字人视频。3) 自校正双向蒸馏模块：在训练阶段，通过双向注意力机制学习更丰富的时空信息，并通过蒸馏的方式将这些信息传递给推理阶段的模型。4) 多步回顾自校正模块：在推理阶段，定期回顾之前的生成结果，并进行自校正，以防止误差累积和模型崩溃。5) 推理加速套件：包括混合序列并行、并行VAE和内核级优化，用于加速模型的推理过程。

**关键创新**：SoulX-LiveTalk的关键创新在于以下几个方面：1) 自校正双向蒸馏策略：突破了传统单向注意力机制的限制，保留了更丰富的时空信息，从而提高了生成质量。2) 多步回顾自校正机制：解决了无限生成过程中可能出现的误差累积和模型崩溃问题，保证了生成过程的稳定性。3) 全栈推理加速套件：通过多种优化手段，显著提高了模型的推理速度，使其能够满足实时性要求。

**关键设计**：在自校正双向蒸馏中，采用了教师-学生模型的蒸馏方式，教师模型使用双向注意力，学生模型则在推理时使用单向注意力，以保证实时性。多步回顾自校正机制中，设置了回顾的频率和校正的强度等参数，以平衡生成质量和计算开销。在推理加速方面，混合序列并行将模型参数分布在多个GPU上，并行VAE则同时处理多个VAE的计算，内核级优化则针对关键算子进行了手工优化。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23379v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23379v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23379v1/figs/visual_quality1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SoulX-LiveTalk在实验中表现出色，实现了0.87秒的亚秒级启动延迟，并达到了32 FPS的实时吞吐量。这是首个达到如此高性能的140亿参数规模的数字人生成系统。相比于现有方法，SoulX-LiveTalk在生成质量和实时性方面都取得了显著的提升，为高保真交互式数字人合成树立了新的标杆。

## 🎯 应用场景

SoulX-LiveTalk在虚拟主播、在线教育、远程会议、游戏娱乐等领域具有广泛的应用前景。它可以用于创建高度逼真的虚拟形象，并根据用户的语音实时生成相应的视频内容，从而提供更具沉浸感和互动性的用户体验。该技术还有潜力应用于医疗健康、心理咨询等领域，为患者提供个性化的虚拟助手。

## 📄 摘要（原文）

> Deploying massive diffusion models for real-time, infinite-duration, audio-driven avatar generation presents a significant engineering challenge, primarily due to the conflict between computational load and strict latency constraints. Existing approaches often compromise visual fidelity by enforcing strictly unidirectional attention mechanisms or reducing model capacity. To address this problem, we introduce \textbf{SoulX-LiveTalk}, a 14B-parameter framework optimized for high-fidelity real-time streaming. Diverging from conventional unidirectional paradigms, we use a \textbf{Self-correcting Bidirectional Distillation} strategy that retains bidirectional attention within video chunks. This design preserves critical spatiotemporal correlations, significantly enhancing motion coherence and visual detail. To ensure stability during infinite generation, we incorporate a \textbf{Multi-step Retrospective Self-Correction Mechanism}, enabling the model to autonomously recover from accumulated errors and preventing collapse. Furthermore, we engineered a full-stack inference acceleration suite incorporating hybrid sequence parallelism, Parallel VAE, and kernel-level optimizations. Extensive evaluations confirm that SoulX-LiveTalk is the first 14B-scale system to achieve a \textbf{sub-second start-up latency (0.87s)} while reaching a real-time throughput of \textbf{32 FPS}, setting a new standard for high-fidelity interactive digital human synthesis.

