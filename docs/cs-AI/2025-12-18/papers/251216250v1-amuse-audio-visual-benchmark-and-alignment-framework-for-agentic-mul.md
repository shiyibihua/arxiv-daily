---
layout: default
title: AMUSE: Audio-Visual Benchmark and Alignment Framework for Agentic Multi-Speaker Understanding
---

# AMUSE: Audio-Visual Benchmark and Alignment Framework for Agentic Multi-Speaker Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16250" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16250v1</a>
  <a href="https://arxiv.org/pdf/2512.16250.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16250v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16250v1', 'AMUSE: Audio-Visual Benchmark and Alignment Framework for Agentic Multi-Speaker Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sanjoy Chowdhury, Karren D. Yang, Xudong Liu, Fartash Faghri, Pavan Kumar Anasosalu Vasu, Oncel Tuzel, Dinesh Manocha, Chun-Liang Li, Raviteja Vemulapalli

**分类**: cs.AI, cs.MA

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**AMUSE：用于Agentic多说话人理解的音视频基准和对齐框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多说话人理解` `音视频分析` `Agentic推理` `多模态学习` `基准测试` `奖励优化` `自评估`

## 📋 核心要点

1. 现有多模态大模型在多说话人对话场景中，缺乏有效的agentic推理能力，难以跟踪说话人、理解角色和事件。
2. 论文提出AMUSE基准测试模型在agentic任务上的表现，并设计RAFT框架，通过奖励优化和自评估提升模型性能。
3. 实验结果表明，RAFT框架在AMUSE基准上显著提升了多模态大模型的性能，相对精度提升高达39.52%。

## 📝 摘要（中文）

本文提出了AMUSE，一个旨在评估多模态大型语言模型（MLLM）在多说话人、以对话为中心的场景下agentic推理能力的基准。现有MLLM如GPT-4o和Qwen3-Omni在感知方面表现出色，但在需要跟踪说话人、维护角色以及理解跨时间事件的场景中表现不足。AMUSE包含零样本、引导和agentic三种模式，以及六个任务族，包括时空说话人定位和多模态对话摘要。实验表明，现有模型在多说话人推理方面表现较弱，且在不同评估模式下行为不一致。此外，本文提出了RAFT，一个数据高效的agentic对齐框架，它结合了奖励优化、内在多模态自评估以及选择性参数调整。使用RAFT，在AMUSE基准上取得了高达39.52%的相对精度提升。AMUSE和RAFT共同为研究多模态模型中的agentic推理并提升其能力提供了一个实用平台。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLM）在处理多说话人音视频对话场景时，缺乏有效的agentic推理能力的问题。现有MLLM在感知方面表现良好，但在需要理解谁在说话、角色是什么以及事件如何随时间演变等复杂场景中表现不足。这些场景对于会话视频助手和会议分析等应用至关重要。现有方法难以将复杂的音视频交互分解为规划、定位和反思等步骤。

**核心思路**：论文的核心思路是构建一个专门用于评估和提升MLLM在agentic多说话人理解方面的基准（AMUSE）和一个对齐框架（RAFT）。通过AMUSE，可以系统地评估现有模型的不足，并利用RAFT框架，通过奖励优化和内在自评估，提升模型在这些任务上的性能。RAFT框架旨在使模型能够更好地理解和推理多说话人对话场景中的复杂交互。

**技术框架**：整体框架包含两个主要部分：AMUSE基准和RAFT对齐框架。AMUSE基准包含六个任务族，涵盖时空说话人定位、多模态对话摘要等。RAFT框架则包含奖励优化模块，该模块利用奖励信号来指导模型的学习；内在多模态自评估模块，用于评估模型自身的表现；以及选择性参数调整模块，用于高效地更新模型参数。整个流程旨在使模型能够更好地理解和推理多说话人对话场景中的复杂交互。

**关键创新**：论文的关键创新在于提出了AMUSE基准和RAFT对齐框架。AMUSE基准专门设计用于评估MLLM在agentic多说话人理解方面的能力，而RAFT框架则提供了一种数据高效的方法来提升模型在这些任务上的性能。RAFT框架结合了奖励优化、内在自评估和选择性参数调整，使其能够更有效地利用数据，并避免过度拟合。

**关键设计**：RAFT框架的关键设计包括：1) 使用奖励模型来评估模型的行为，并提供奖励信号；2) 使用内在多模态自评估来评估模型自身的表现，并提供反馈；3) 使用选择性参数调整来高效地更新模型参数，避免过度拟合。具体的参数设置、损失函数和网络结构等细节在论文中进行了详细描述，例如，奖励模型的设计、自评估指标的选择以及参数更新策略的制定。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16250v1/figures/teaser.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16250v1/figures/eval-modes-short.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16250v1/figures/raft-revised.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RAFT框架在AMUSE基准上取得了显著的性能提升。在多个任务上，RAFT框架的性能优于现有的基线模型，相对精度提升高达39.52%。这表明RAFT框架能够有效地提升MLLM在agentic多说话人理解方面的能力。实验还表明，RAFT框架具有数据高效性，能够在较少的数据下取得良好的性能。

## 🎯 应用场景

该研究成果可应用于会话视频助手、会议分析、智能客服等领域。通过提升模型在多说话人场景下的理解和推理能力，可以实现更自然、更智能的人机交互。例如，在会议分析中，模型可以自动识别发言人、总结会议内容，并提取关键信息。在智能客服中，模型可以更好地理解用户意图，并提供更准确的回答。

## 📄 摘要（原文）

> Recent multimodal large language models (MLLMs) such as GPT-4o and Qwen3-Omni show strong perception but struggle in multi-speaker, dialogue-centric settings that demand agentic reasoning tracking who speaks, maintaining roles, and grounding events across time. These scenarios are central to multimodal audio-video understanding, where models must jointly reason over audio and visual streams in applications such as conversational video assistants and meeting analytics. We introduce AMUSE, a benchmark designed around tasks that are inherently agentic, requiring models to decompose complex audio-visual interactions into planning, grounding, and reflection steps. It evaluates MLLMs across three modes zero-shot, guided, and agentic and six task families, including spatio-temporal speaker grounding and multimodal dialogue summarization. Across all modes, current models exhibit weak multi-speaker reasoning and inconsistent behavior under both non-agentic and agentic evaluation. Motivated by the inherently agentic nature of these tasks and recent advances in LLM agents, we propose RAFT, a data-efficient agentic alignment framework that integrates reward optimization with intrinsic multimodal self-evaluation as reward and selective parameter adaptation for data and parameter efficient updates. Using RAFT, we achieve up to 39.52\% relative improvement in accuracy on our benchmark. Together, AMUSE and RAFT provide a practical platform for examining agentic reasoning in multimodal models and improving their capabilities.

