---
layout: default
title: Harmony: Harmonizing Audio and Video Generation through Cross-Task Synergy
---

# Harmony: Harmonizing Audio and Video Generation through Cross-Task Synergy

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.21579" target="_blank" class="toolbar-btn">arXiv: 2511.21579v2</a>
    <a href="https://arxiv.org/pdf/2511.21579.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21579v2" 
            onclick="toggleFavorite(this, '2511.21579v2', 'Harmony: Harmonizing Audio and Video Generation through Cross-Task Synergy')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Teng Hu, Zhentao Yu, Guozhen Zhang, Zihan Su, Zhengguang Zhou, Youliang Zhang, Yuan Zhou, Qinglin Lu, Ran Yi

**分类**: cs.CV

**发布日期**: 2025-11-26 (更新: 2025-11-28)

---

## 💡 一句话要点

**Harmony：通过跨任务协同实现音视频生成和谐统一**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `音视频生成` `跨模态学习` `扩散模型` `音视频同步` `生成式AI`

## 📋 核心要点

1. 现有音视频生成模型在音视频对齐方面存在困难，主要原因是联合扩散过程中的对应漂移、低效的全局注意力以及无分类器引导的模内偏差。
2. Harmony框架通过跨任务协同训练、全局-局部解耦交互模块和同步增强CFG，从机制上强制执行音视频同步，从而解决上述问题。
3. 实验结果表明，Harmony在音视频生成保真度和细粒度音视频同步方面均显著优于现有方法，达到了新的state-of-the-art。

## 📝 摘要（中文）

同步音视频内容的生成是生成式AI中的一个关键挑战，开源模型在鲁棒的音视频对齐方面面临挑战。我们的分析表明，这个问题源于联合扩散过程中的三个基本挑战：（1）对应漂移，即并发演化的噪声潜在变量阻碍了对齐的稳定学习；（2）低效的全局注意力机制，无法捕捉细粒度的时间线索；（3）传统无分类器引导（CFG）的模内偏差，增强了条件性，但没有增强跨模态同步。为了克服这些挑战，我们引入了Harmony，这是一个新颖的框架，从机制上强制执行音视频同步。我们首先提出了一种跨任务协同训练范式，通过利用来自音频驱动视频和视频驱动音频生成任务的强监督信号来减轻漂移。然后，我们设计了一个全局-局部解耦交互模块，用于高效和精确的时间风格对齐。最后，我们提出了一种新颖的同步增强CFG（SyncCFG），它在推理过程中显式地隔离和放大对齐信号。大量的实验表明，Harmony建立了一个新的最先进水平，在生成保真度方面显著优于现有方法，并且关键在于实现了细粒度的音视频同步。

## 🔬 方法详解

**问题定义**：论文旨在解决音视频生成中音视频同步问题，现有方法在联合扩散过程中存在对应漂移，全局注意力机制无法捕捉细粒度时间线索，且无分类器引导存在模内偏差，导致音视频无法有效对齐。

**核心思路**：论文的核心思路是通过跨任务协同训练，利用音频驱动视频和视频驱动音频生成任务的强监督信号来减轻对应漂移；设计全局-局部解耦交互模块，实现高效精确的时间风格对齐；并提出同步增强CFG，显式地隔离和放大对齐信号，从而实现音视频的和谐统一。

**技术框架**：Harmony框架主要包含三个部分：1) Cross-Task Synergy training paradigm（跨任务协同训练范式），利用音频驱动视频和视频驱动音频生成任务的监督信号；2) Global-Local Decoupled Interaction Module（全局-局部解耦交互模块），用于高效和精确的时间风格对齐；3) Synchronization-Enhanced CFG (SyncCFG)（同步增强CFG），在推理过程中显式地隔离和放大对齐信号。整体流程是先通过跨任务协同训练增强模型对齐能力，然后利用全局-局部解耦交互模块进行细粒度对齐，最后通过同步增强CFG在推理阶段进一步提升同步效果。

**关键创新**：论文的关键创新在于：1) 提出了Cross-Task Synergy training paradigm，通过跨任务学习缓解对应漂移问题；2) 设计了Global-Local Decoupled Interaction Module，能够更有效地捕捉时间信息并进行风格对齐；3) 提出了Synchronization-Enhanced CFG，在推理阶段显式增强同步信号。与现有方法相比，Harmony从机制上强制执行音视频同步，而非仅仅依赖于数据驱动的学习。

**关键设计**：Cross-Task Synergy training paradigm的具体实现方式是同时训练音频到视频和视频到音频两个生成模型，并共享部分参数。Global-Local Decoupled Interaction Module采用解耦的设计，分别处理全局和局部信息，然后进行融合。Synchronization-Enhanced CFG通过修改CFG的计算方式，显式地引入同步信号，具体细节未知。

## 📊 实验亮点

Harmony在音视频生成任务上取得了显著的性能提升，大幅超越了现有方法。具体性能数据未知，但论文强调在生成保真度和细粒度音视频同步方面均达到了state-of-the-art。实验结果证明了跨任务协同训练、全局-局部解耦交互模块和同步增强CFG的有效性。

## 🎯 应用场景

该研究成果可广泛应用于音视频内容创作、虚拟现实、游戏开发、电影制作等领域。通过生成高质量且同步的音视频内容，可以提升用户体验，降低创作成本，并为新兴应用提供技术支持。未来，该技术有望进一步扩展到更复杂的多模态内容生成，例如带有触觉反馈的沉浸式体验。

## 📄 摘要（原文）

> The synthesis of synchronized audio-visual content is a key challenge in generative AI, with open-source models facing challenges in robust audio-video alignment. Our analysis reveals that this issue is rooted in three fundamental challenges of the joint diffusion process: (1) Correspondence Drift, where concurrently evolving noisy latents impede stable learning of alignment; (2) inefficient global attention mechanisms that fail to capture fine-grained temporal cues; and (3) the intra-modal bias of conventional Classifier-Free Guidance (CFG), which enhances conditionality but not cross-modal synchronization. To overcome these challenges, we introduce Harmony, a novel framework that mechanistically enforces audio-visual synchronization. We first propose a Cross-Task Synergy training paradigm to mitigate drift by leveraging strong supervisory signals from audio-driven video and video-driven audio generation tasks. Then, we design a Global-Local Decoupled Interaction Module for efficient and precise temporal-style alignment. Finally, we present a novel Synchronization-Enhanced CFG (SyncCFG) that explicitly isolates and amplifies the alignment signal during inference. Extensive experiments demonstrate that Harmony establishes a new state-of-the-art, significantly outperforming existing methods in both generation fidelity and, critically, in achieving fine-grained audio-visual synchronization.

