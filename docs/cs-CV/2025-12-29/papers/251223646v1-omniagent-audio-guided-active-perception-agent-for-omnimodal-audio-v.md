---
layout: default
title: "OmniAgent: Audio-Guided Active Perception Agent for Omnimodal Audio-Video Understanding"
---

# OmniAgent: Audio-Guided Active Perception Agent for Omnimodal Audio-Video Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23646" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23646v1</a>
  <a href="https://arxiv.org/pdf/2512.23646.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23646v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23646v1', 'OmniAgent: Audio-Guided Active Perception Agent for Omnimodal Audio-Video Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keda Tao, Wenjie Du, Bohan Yu, Weiqiang Wang, Jian Liu, Huan Wang

**分类**: cs.CV

**发布日期**: 2025-12-29

**备注**: Website:https://kd-tao.github.io/OmniAgent/

---

## 💡 一句话要点

**OmniAgent：一种音频引导的主动感知Agent，用于全模态音视频理解**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音视频理解` `主动感知` `多模态融合` `音频引导` `动态规划`

## 📋 核心要点

1. 现有全模态大语言模型在音视频理解中缺乏细粒度的跨模态理解和多模态对齐能力。
2. OmniAgent通过音频引导的主动感知，动态编排工具调用，实现由粗到精的音视频理解。
3. 实验结果表明，OmniAgent在音视频理解任务上取得了显著提升，超越现有模型10%-20%的准确率。

## 📝 摘要（中文）

本文提出OmniAgent，一个完全由音频引导的主动感知Agent，旨在提升全模态大语言模型在音视频理解中的细粒度跨模态理解和多模态对齐能力。与依赖静态工作流和密集帧字幕的方法不同，OmniAgent实现了从被动响应生成到主动多模态查询的范式转变。它采用动态规划，自主地按需编排工具调用，并将感知注意力集中在任务相关的线索上。该方法的核心是一种新颖的由粗到精的音频引导感知范式，利用音频线索来定位时间事件，并指导后续的推理。在三个音视频理解基准上的大量实验评估表明，OmniAgent实现了最先进的性能，超越了领先的开源和专有模型，准确率提高了10%-20%。

## 🔬 方法详解

**问题定义**：现有全模态大语言模型在音视频理解任务中，通常采用静态的工作流程和密集的帧字幕方式，缺乏对音频和视频信息之间细粒度关联的理解能力，难以实现精准的多模态对齐。这导致模型在复杂场景下的推理能力受限，无法有效利用音频信息引导视觉感知。

**核心思路**：OmniAgent的核心思路是利用音频信息作为引导，主动地进行多模态感知和推理。通过动态规划工具调用，模型可以根据音频线索自主地选择合适的工具进行处理，并将注意力集中在与任务相关的视觉信息上，从而实现更精准的音视频理解。

**技术框架**：OmniAgent的整体架构包含以下几个主要模块：1) 音频事件检测模块，用于从音频中提取关键事件信息；2) 动态规划模块，根据音频事件信息，规划工具调用顺序；3) 多模态感知模块，利用选定的工具对视频进行处理，提取相关视觉特征；4) 推理模块，结合音频和视觉信息进行推理，完成最终任务。整个流程是由粗到精的，首先通过音频定位关键事件，然后引导视觉感知。

**关键创新**：OmniAgent的关键创新在于其主动感知的模式和由粗到精的音频引导策略。与传统的被动式模型不同，OmniAgent可以根据音频信息主动地选择合适的工具进行处理，并将注意力集中在与任务相关的视觉信息上。这种主动感知的模式使得模型能够更有效地利用多模态信息，提高理解能力。由粗到精的策略则保证了模型能够高效地定位关键信息，避免了对所有帧进行密集处理。

**关键设计**：OmniAgent的关键设计包括：1) 音频事件检测模块的设计，需要选择合适的音频特征和模型结构，以保证能够准确地检测到关键事件；2) 动态规划模块的设计，需要定义合适的奖励函数和搜索策略，以保证能够找到最优的工具调用顺序；3) 多模态感知模块的设计，需要选择合适的视觉特征提取器和融合策略，以保证能够有效地利用视觉信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23646v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23646v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23646v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

OmniAgent在三个音视频理解基准测试中均取得了state-of-the-art的性能，相比于领先的开源和商业模型，准确率提升了10%-20%。这表明OmniAgent在音视频理解方面具有显著的优势，能够有效地利用多模态信息进行推理。

## 🎯 应用场景

OmniAgent在智能监控、智能家居、自动驾驶等领域具有广泛的应用前景。例如，在智能监控中，可以通过分析监控视频中的声音事件（如玻璃破碎、呼救声等）来自动识别异常情况并报警。在自动驾驶中，可以通过分析车辆周围的声音信息（如警笛声、喇叭声等）来辅助驾驶决策，提高安全性。

## 📄 摘要（原文）

> Omnimodal large language models have made significant strides in unifying audio and visual modalities; however, they often lack the fine-grained cross-modal understanding and have difficulty with multimodal alignment. To address these limitations, we introduce OmniAgent, a fully audio-guided active perception agent that dynamically orchestrates specialized tools to achieve more fine-grained audio-visual reasoning. Unlike previous works that rely on rigid, static workflows and dense frame-captioning, this paper demonstrates a paradigm shift from passive response generation to active multimodal inquiry. OmniAgent employs dynamic planning to autonomously orchestrate tool invocation on demand, strategically concentrating perceptual attention on task-relevant cues. Central to our approach is a novel coarse-to-fine audio-guided perception paradigm, which leverages audio cues to localize temporal events and guide subsequent reasoning. Extensive empirical evaluations on three audio-video understanding benchmarks demonstrate that OmniAgent achieves state-of-the-art performance, surpassing leading open-source and proprietary models by substantial margins of 10% - 20% accuracy.

