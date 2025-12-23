---
layout: default
title: Fine-Grained Preference Optimization Improves Spatial Reasoning in VLMs
---

# Fine-Grained Preference Optimization Improves Spatial Reasoning in VLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21656" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21656v2</a>
  <a href="https://arxiv.org/pdf/2506.21656.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21656v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21656v2', 'Fine-Grained Preference Optimization Improves Spatial Reasoning in VLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Shen, Yuanzhe Liu, Jingyuan Zhu, Xu Cao, Xiaofeng Zhang, Yixiao He, Wenming Ye, James Matthew Rehg, Ismini Lourentzou

**分类**: cs.CV, cs.CL

**发布日期**: 2025-06-26 (更新: 2025-10-26)

---

## 💡 一句话要点

**提出SpatialReasoner-R1以解决视觉语言模型的空间推理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `空间推理` `多模型蒙特卡洛树搜索` `细粒度优化` `逻辑推理`

## 📋 核心要点

1. 现有视觉语言模型在细粒度空间推理方面表现不佳，尤其是在复杂逻辑和空间对齐任务中。
2. 本文提出了SpatialReasoner-R1模型，结合多模型蒙特卡洛树搜索和细粒度直接偏好优化，以提升空间推理能力。
3. 实验结果显示，fDPO在空间质量和数量任务上分别提升4.1%和9.0%，并在SPATIALRGPT-Bench上创下新纪录。

## 📝 摘要（中文）

当前的视觉语言模型（VLMs）在细粒度空间推理方面存在困难，尤其是在需要多步逻辑和精确空间对齐时。本文提出了SpatialReasoner-R1，一个旨在解决这些局限性的视觉语言推理模型。为构建高质量的空间推理监督，设计了多模型蒙特卡洛树搜索（M3CTS）方法，生成多样且逻辑一致的长链思维推理轨迹。此外，提出了细粒度直接偏好优化（fDPO），引入了针对描述性基础和逻辑推理的段特定偏好粒度，通过空间奖励机制评估候选响应的视觉一致性、空间基础和逻辑连贯性。实验结果表明，fDPO在空间质量任务上平均提升4.1%，在空间数量任务上提升9.0%。使用fDPO训练的SpatialReasoner-R1在SPATIALRGPT-Bench上设定了新的状态-of-the-art（SoTA），在平均准确率上超越最强基线9.8%，同时在一般视觉语言任务上保持竞争力。

## 🔬 方法详解

**问题定义**：当前视觉语言模型在处理细粒度空间推理时，常常面临多步逻辑推理和空间对齐的挑战，导致推理结果不够准确和一致。

**核心思路**：为了解决这些问题，本文提出SpatialReasoner-R1，通过引入多模型蒙特卡洛树搜索（M3CTS）和细粒度直接偏好优化（fDPO），以生成逻辑一致的推理轨迹并优化模型的空间推理能力。

**技术框架**：整体架构包括两个主要模块：M3CTS用于生成多样的推理轨迹，fDPO则通过空间奖励机制对模型进行细粒度优化，确保输出的视觉一致性和逻辑连贯性。

**关键创新**：最重要的创新在于引入了细粒度的偏好优化机制，使得模型能够在不同的空间推理任务中根据具体段落的需求进行优化，从而显著提升了推理的准确性和一致性。

**关键设计**：在设计中，M3CTS生成的推理轨迹具有多样性和逻辑一致性，fDPO则通过设定特定的损失函数和奖励机制，确保模型在评估候选响应时能够充分考虑视觉和逻辑因素。具体参数设置和网络结构的细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，fDPO在空间质量任务上平均提升4.1%，在空间数量任务上提升9.0%。使用fDPO训练的SpatialReasoner-R1在SPATIALRGPT-Bench上创下新的SoTA，平均准确率超越最强基线9.8%。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动驾驶、机器人导航等需要复杂空间推理的场景。通过提升视觉语言模型的空间推理能力，可以显著改善人机交互的自然性和准确性，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Current Vision-Language Models (VLMs) struggle with fine-grained spatial reasoning, particularly when multi-step logic and precise spatial alignment are required. In this work, we introduce SpatialReasoner-R1, a vision-language reasoning model designed to address these limitations. To construct high-quality supervision for spatial reasoning, we design a Multi-Model Monte Carlo Tree Search (M3CTS) method that generates diverse, logically consistent Long Chain-of-Thought (LongCoT) reasoning trajectories. In addition, we propose fine-grained Direct Preference Optimization (fDPO), which introduces segment-specific preference granularity for descriptive grounding and logical reasoning, guided by a spatial reward mechanism that evaluates candidate responses based on visual consistency, spatial grounding, and logical coherence. Experimental results demonstrate that fDPO achieves an average improvement of 4.1% over standard DPO across spatial quality tasks, and a 9.0% gain in spatial quantity tasks. SpatialReasoner-R1, trained with fDPO, sets a new SoTA on SPATIALRGPT-Bench, outperforming the strongest baseline by 9.8% in average accuracy, while maintaining competitive performance on general vision-language tasks.

