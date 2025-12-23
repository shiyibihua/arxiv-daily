---
layout: default
title: Reinforcing Spatial Reasoning in Vision-Language Models with Interwoven Thinking and Visual Drawing
---

# Reinforcing Spatial Reasoning in Vision-Language Models with Interwoven Thinking and Visual Drawing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09965" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09965v2</a>
  <a href="https://arxiv.org/pdf/2506.09965.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09965v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09965v2', 'Reinforcing Spatial Reasoning in Vision-Language Models with Interwoven Thinking and Visual Drawing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junfei Wu, Jian Guan, Kaituo Feng, Qiang Liu, Shu Wu, Liang Wang, Wei Wu, Tieniu Tan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-11 (更新: 2025-06-19)

---

## 💡 一句话要点

**提出通过绘图增强视觉语言模型的空间推理能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空间推理` `视觉语言模型` `多模态推理` `绘图操作` `强化学习` `几何理解` `自我反思`

## 📋 核心要点

1. 现有的多模态推理方法主要依赖文本，无法有效处理需要精确空间理解的任务。
2. 本文提出通过基本绘图操作进行空间推理，使模型能够直接在视觉空间中进行操作和分析。
3. 实验结果显示，VILASR模型在多种空间推理任务中表现优于现有方法，平均提升18.4%。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在文本推理方面的显著进展，增强大型视觉语言模型（LVLMs）的多模态推理能力的兴趣日益增长。然而，现有方法主要以文本为中心，导致在需要精确几何理解和连续空间跟踪的空间推理任务中遇到基本限制。为了解决这些限制，本文提出了一种新颖的通过基本绘图操作进行空间推理的范式，使LVLMs能够通过直接的视觉操作表达和分析空间关系。我们开发了一个三阶段的训练框架，实验结果表明，所提出的模型VILASR在多种空间推理基准测试中表现优异，平均提升幅度达到18.4%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态推理方法在空间推理任务中的不足，特别是缺乏对几何关系的精确理解和空间跟踪能力。

**核心思路**：提出通过基本绘图操作（如标注边界框和绘制辅助线）来增强LVLMs的空间推理能力，使其能够通过视觉操作直接分析空间关系。

**技术框架**：整体架构包括三个主要阶段：使用合成数据进行冷启动训练以建立基本绘图能力；通过反思拒绝采样增强模型的自我反思行为；使用强化学习直接优化目标奖励。

**关键创新**：最重要的创新在于引入绘图操作作为推理工具，使得模型能够在视觉空间中进行直接操作，突破了以往方法的性能瓶颈。

**关键设计**：在训练过程中，采用合成数据进行初步训练，设计了特定的损失函数以优化绘图能力，并通过强化学习调整模型参数以实现最佳性能。

## 📊 实验亮点

实验结果表明，VILASR模型在迷宫导航、静态空间推理、基于视频的推理和多视角推理任务中均表现优异，平均提升幅度达到18.4%，显著优于现有基线方法。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、增强现实和视频理解等场景，能够有效提升机器在复杂环境中的空间推理能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> As textual reasoning with large language models (LLMs) has advanced significantly, there has been growing interest in enhancing the multimodal reasoning capabilities of large vision-language models (LVLMs). However, existing methods primarily approach multimodal reasoning in a straightforward, text-centric manner, where both reasoning and answer derivation are conducted purely through text, with the only difference being the presence of multimodal input. As a result, these methods often encounter fundamental limitations in spatial reasoning tasks that demand precise geometric understanding and continuous spatial tracking-capabilities that humans achieve through mental visualization and manipulation. To address the limitations, we propose drawing to reason in space, a novel paradigm that enables LVLMs to reason through elementary drawing operations in the visual space. By equipping models with basic drawing operations, including annotating bounding boxes and drawing auxiliary lines, we empower them to express and analyze spatial relationships through direct visual manipulation, meanwhile avoiding the performance ceiling imposed by specialized perception tools in previous tool-integrated reasoning approaches. To cultivate this capability, we develop a three-stage training framework: cold-start training with synthetic data to establish basic drawing abilities, reflective rejection sampling to enhance self-reflection behaviors, and reinforcement learning to directly optimize for target rewards. Extensive experiments demonstrate that our model, named VILASR, consistently outperforms existing methods across diverse spatial reasoning benchmarks, involving maze navigation, static spatial reasoning, video-based reasoning, and multi-view-based reasoning tasks, with an average improvement of 18.4%.

