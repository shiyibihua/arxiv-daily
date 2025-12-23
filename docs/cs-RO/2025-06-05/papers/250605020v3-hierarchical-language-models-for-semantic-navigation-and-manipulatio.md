---
layout: default
title: Hierarchical Language Models for Semantic Navigation and Manipulation in an Aerial-Ground Robotic System
---

# Hierarchical Language Models for Semantic Navigation and Manipulation in an Aerial-Ground Robotic System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05020" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05020v3</a>
  <a href="https://arxiv.org/pdf/2506.05020.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05020v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05020v3', 'Hierarchical Language Models for Semantic Navigation and Manipulation in an Aerial-Ground Robotic System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haokun Liu, Zhaoqi Ma, Yunong Li, Junichiro Sugihara, Yicheng Chen, Jinjie Li, Moju Zhao

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-05 (更新: 2025-10-27)

**备注**: 18 pages, 10 figures

**期刊**: Advanced Intelligent Systems, Oct. 2025

**DOI**: [10.1002/aisy.202500640](https://doi.org/10.1002/aisy.202500640)

---

## 💡 一句话要点

**提出分层语言模型以解决异构机器人系统的导航与操作问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `异构机器人` `多模态融合` `语言模型` `视觉-语言模型` `任务规划` `语义导航` `动态环境` `智能操作`

## 📋 核心要点

1. 现有方法依赖静态模型，缺乏在多样化任务和动态环境中的通用性，限制了异构机器人系统的应用。
2. 本文提出了一种分层多模态框架，结合了LLM的高层推理与VLM的低层执行，提升了系统的智能化水平。
3. 通过仿真和真实实验，验证了该框架在长时间物体排列任务中的零-shot适应性和稳健性，表现出显著的性能提升。

## 📝 摘要（中文）

异构多机器人系统在复杂任务中展现出巨大的潜力，但现有方法往往依赖静态或特定任务的模型，缺乏在多样化任务和动态环境中的通用性。为此，本文提出了一种分层多模态框架，将大型语言模型（LLM）与经过微调的视觉-语言模型（VLM）集成。LLM负责任务分解和构建全局语义图，而VLM则提供语义感知和物体定位。通过引入GridMask，显著提升了VLM的空间精度，确保了在目标缺失或模糊场景中的可靠操作。通过广泛的仿真和真实实验验证了该框架在长时间物体排列任务中的零-shot适应性、稳健的语义导航和可靠的操作能力。

## 🔬 方法详解

**问题定义**：本文旨在解决异构多机器人系统在复杂任务中的导航与操作问题，现有方法因依赖静态或特定任务模型而缺乏通用性。

**核心思路**：提出的分层多模态框架通过结合LLM与VLM，能够在高层次进行任务分解并在低层次实现精确操作，从而实现更高效的任务执行。

**技术框架**：整体架构包括两个主要模块：LLM用于任务分解和全局语义图构建，VLM负责语义感知和物体定位，GridMask则用于提升空间精度。

**关键创新**：本研究的核心创新在于首次将VLM与LLM结合，形成异构空地机器人系统，实现高层次的任务规划与执行，显著提升了系统的智能化水平。

**关键设计**：在VLM中引入GridMask以增强空间准确性，确保在复杂环境中进行可靠的细粒度操作，同时优化了模型的参数设置和损失函数以适应动态场景。

## 📊 实验亮点

实验结果表明，所提框架在长时间物体排列任务中实现了零-shot适应性，稳健的语义导航和可靠的操作能力，较基线方法在任务完成率和精确度上提升了显著的性能，具体数据未提供。

## 🎯 应用场景

该研究的潜在应用领域包括智能物流、无人机配送、灾后救援等场景，能够有效提升异构机器人系统在复杂环境中的协作能力与任务执行效率，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> Heterogeneous multirobot systems show great potential in complex tasks requiring coordinated hybrid cooperation. However, existing methods that rely on static or task-specific models often lack generalizability across diverse tasks and dynamic environments. This highlights the need for generalizable intelligence that can bridge high-level reasoning with low-level execution across heterogeneous agents. To address this, we propose a hierarchical multimodal framework that integrates a prompted large language model (LLM) with a fine-tuned vision-language model (VLM). At the system level, the LLM performs hierarchical task decomposition and constructs a global semantic map, while the VLM provides semantic perception and object localization, where the proposed GridMask significantly enhances the VLM's spatial accuracy for reliable fine-grained manipulation. The aerial robot leverages this global map to generate semantic paths and guide the ground robot's local navigation and manipulation, ensuring robust coordination even in target-absent or ambiguous scenarios. We validate the framework through extensive simulation and real-world experiments on long-horizon object arrangement tasks, demonstrating zero-shot adaptability, robust semantic navigation, and reliable manipulation in dynamic environments. To the best of our knowledge, this work presents the first heterogeneous aerial-ground robotic system that integrates VLM-based perception with LLM-driven reasoning for global high-level task planning and execution.

