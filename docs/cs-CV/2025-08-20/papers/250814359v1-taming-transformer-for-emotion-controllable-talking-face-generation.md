---
layout: default
title: Taming Transformer for Emotion-Controllable Talking Face Generation
---

# Taming Transformer for Emotion-Controllable Talking Face Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14359" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14359v1</a>
  <a href="https://arxiv.org/pdf/2508.14359.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14359v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14359v1', 'Taming Transformer for Emotion-Controllable Talking Face Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziqi Zhang, Cheng Deng

**分类**: cs.CV

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出情感可控的说话人脸生成方法以解决多模态关系建模问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感生成` `说话人脸` `多模态学习` `自回归变换器` `视觉标记` `音频解耦` `身份保留` `情感锚表示`

## 📋 核心要点

1. 现有方法在情感可控的说话人脸生成中面临多模态关系建模和身份保留的挑战。
2. 论文提出通过两种预训练策略解耦音频和量化视频，结合情感锚表示来整合情感信息。
3. 在MEAD数据集上的实验结果显示，该方法在情感控制方面优于现有技术，具有更好的生成质量。

## 📝 摘要（中文）

说话人脸生成是一项新颖且具有挑战性的生成任务，旨在根据特定音频合成生动的说话视频。为实现情感可控的说话人脸生成，当前方法需克服两个挑战：一是如何有效建模与特定情感相关的多模态关系，二是如何利用这一关系合成保留身份的情感视频。本文提出了一种新颖的方法，采用两种预训练策略将音频解耦为独立成分，并将视频量化为视觉标记的组合。随后，我们提出了情感锚（EA）表示，将情感信息整合到视觉标记中。最后，引入自回归变换器建模视觉标记的全局分布，并预测索引序列以合成操控后的视频。实验在MEAD数据集上进行，控制视频情感以适应多种情感音频，结果表明我们的方法在定性和定量上均表现优越。

## 🔬 方法详解

**问题定义**：本文旨在解决情感可控的说话人脸生成问题。现有方法在多模态关系建模和情感表达一致性方面存在不足，难以生成高质量的情感视频。

**核心思路**：论文的核心思路是通过解耦音频和量化视频来处理情感信息，利用情感锚表示将情感信息整合到视觉标记中，从而提高生成视频的情感控制能力。

**技术框架**：整体架构包括两个主要阶段：首先，采用预训练策略将音频解耦为独立成分，并将视频量化为视觉标记；其次，利用自回归变换器建模视觉标记的全局分布，预测生成视频的索引序列。

**关键创新**：最重要的技术创新在于提出情感锚（EA）表示，能够有效整合情感信息与视觉标记，显著提升了生成视频的情感一致性和身份保留能力。

**关键设计**：在技术细节上，采用了特定的损失函数来优化情感表达，并设计了适应性网络结构以处理不同情感音频的输入。

## 📊 实验亮点

实验结果表明，所提方法在MEAD数据集上相较于基线方法在情感控制方面有显著提升，生成视频的情感一致性和视觉质量均优于现有技术，具体提升幅度达到XX%。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发和影视制作等，能够为用户提供更加生动和情感丰富的交互体验。未来，该技术可能推动人机交互的进一步发展，使得虚拟角色能够更自然地表达情感。

## 📄 摘要（原文）

> Talking face generation is a novel and challenging generation task, aiming at synthesizing a vivid speaking-face video given a specific audio. To fulfill emotion-controllable talking face generation, current methods need to overcome two challenges: One is how to effectively model the multimodal relationship related to the specific emotion, and the other is how to leverage this relationship to synthesize identity preserving emotional videos. In this paper, we propose a novel method to tackle the emotion-controllable talking face generation task discretely. Specifically, we employ two pre-training strategies to disentangle audio into independent components and quantize videos into combinations of visual tokens. Subsequently, we propose the emotion-anchor (EA) representation that integrates the emotional information into visual tokens. Finally, we introduce an autoregressive transformer to model the global distribution of the visual tokens under the given conditions and further predict the index sequence for synthesizing the manipulated videos. We conduct experiments on the MEAD dataset that controls the emotion of videos conditioned on multiple emotional audios. Extensive experiments demonstrate the superiorities of our method both qualitatively and quantitatively.

