---
layout: default
title: Causal-Entity Reflected Egocentric Traffic Accident Video Synthesis
---

# Causal-Entity Reflected Egocentric Traffic Accident Video Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23263" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23263v1</a>
  <a href="https://arxiv.org/pdf/2506.23263.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23263v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23263v1', 'Causal-Entity Reflected Egocentric Traffic Accident Video Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lei-lei Li, Jianwu Fang, Junbin Xiao, Shanmin Pang, Hongkai Yu, Chen Lv, Jianru Xue, Tat-Seng Chua

**分类**: cs.CV

**发布日期**: 2025-06-29

**备注**: Accepted by ICCV2025

---

## 💡 一句话要点

**提出Causal-VidSyn以解决交通事故视频合成中的因果关系问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `交通事故视频合成` `因果关系` `扩散模型` `第一人称视角` `驾驶员注视点` `数据集构建` `视频生成` `自动驾驶安全`

## 📋 核心要点

1. 现有方法在合成交通事故视频时难以有效融入现实中的因果关系，导致合成视频的真实性不足。
2. 本文提出的Causal-VidSyn模型通过结合事故原因描述和驾驶员注视点，精准识别事故参与者及其行为，从而提升合成视频的质量。
3. 实验结果显示，Causal-VidSyn在事故视频编辑、正常到事故视频扩散和文本到视频生成等任务中，均优于现有的扩散模型。

## 📝 摘要（中文）

理解交通事故的因果关系对于自动驾驶汽车的安全至关重要，而合成反映因果关系的事故视频可以帮助测试应对不可承受事故的能力。然而，将现实视频中的因果关系融入合成视频仍然面临挑战。本文提出了一种新颖的扩散模型Causal-VidSyn，用于合成第一人称视角的交通事故视频。该模型利用事故原因描述和驾驶员注视点来识别事故参与者及其行为，并通过事故原因回答和注视条件选择模块进行支持。实验结果表明，Causal-VidSyn在视频帧质量和因果敏感性方面超越了现有的扩散模型。

## 🔬 方法详解

**问题定义**：本文旨在解决合成交通事故视频时如何有效融入现实中的因果关系的问题。现有方法在识别事故参与者及其行为方面存在不足，导致合成视频缺乏真实性和有效性。

**核心思路**：Causal-VidSyn模型的核心思路是通过结合事故原因描述和驾驶员的注视点信息，来精准识别事故参与者及其行为。这种设计可以更好地反映真实事故场景中的因果关系。

**技术框架**：Causal-VidSyn的整体架构包括多个模块：事故原因回答模块、注视条件选择模块，以及视频扩散生成模块。这些模块协同工作，以实现高质量的事故视频合成。

**关键创新**：Causal-VidSyn的主要创新在于其因果实体的定位能力，通过结合驾驶员的注视点和事故原因描述，显著提升了合成视频的因果敏感性和真实感。这与现有方法的单一视频生成方式形成了明显对比。

**关键设计**：在模型设计中，采用了特定的损失函数来优化视频帧的质量，并通过大规模的Drive-Gaze数据集进行训练，确保模型能够有效学习驾驶员的注视行为。

## 📊 实验亮点

实验结果表明，Causal-VidSyn在视频帧质量和因果敏感性方面显著优于现有的扩散模型。在事故视频编辑任务中，Causal-VidSyn的性能提升幅度达到XX%，在正常到事故视频扩散和文本到视频生成任务中也表现出色，具体性能数据为XX。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车的安全测试、交通事故分析和虚拟现实场景构建。通过合成高质量的交通事故视频，能够为自动驾驶系统提供更真实的训练数据，从而提升其应对复杂交通情况的能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Egocentricly comprehending the causes and effects of car accidents is crucial for the safety of self-driving cars, and synthesizing causal-entity reflected accident videos can facilitate the capability test to respond to unaffordable accidents in reality. However, incorporating causal relations as seen in real-world videos into synthetic videos remains challenging. This work argues that precisely identifying the accident participants and capturing their related behaviors are of critical importance. In this regard, we propose a novel diffusion model, Causal-VidSyn, for synthesizing egocentric traffic accident videos. To enable causal entity grounding in video diffusion, Causal-VidSyn leverages the cause descriptions and driver fixations to identify the accident participants and behaviors, facilitated by accident reason answering and gaze-conditioned selection modules. To support Causal-VidSyn, we further construct Drive-Gaze, the largest driver gaze dataset (with 1.54M frames of fixations) in driving accident scenarios. Extensive experiments show that Causal-VidSyn surpasses state-of-the-art video diffusion models in terms of frame quality and causal sensitivity in various tasks, including accident video editing, normal-to-accident video diffusion, and text-to-video generation.

