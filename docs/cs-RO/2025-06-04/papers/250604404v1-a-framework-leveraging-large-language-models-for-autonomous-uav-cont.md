---
layout: default
title: A Framework Leveraging Large Language Models for Autonomous UAV Control in Flying Networks
---

# A Framework Leveraging Large Language Models for Autonomous UAV Control in Flying Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04404" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04404v1</a>
  <a href="https://arxiv.org/pdf/2506.04404.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04404v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04404v1', 'A Framework Leveraging Large Language Models for Autonomous UAV Control in Flying Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Diana Nunes, Ricardo Amorim, Pedro Ribeiro, André Coelho, Rui Campos

**分类**: cs.NI, cs.RO

**发布日期**: 2025-06-04

**备注**: 6 pages, 3 figures, 6 tables

---

## 💡 一句话要点

**提出FLUC框架以实现无人机在飞行网络中的自主控制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机控制` `大型语言模型` `自主飞行` `自然语言处理` `任务生成`

## 📋 核心要点

1. 现有无人机控制方法难以有效理解和执行高层次自然语言命令，导致操作员与无人机之间的沟通障碍。
2. FLUC框架通过将大型语言模型与无人机自动驾驶系统结合，能够将自然语言命令转化为可执行的任务代码，从而实现自主控制。
3. 实验结果显示，Qwen 2.5在多步推理方面表现最佳，Gemma 2在准确性和延迟上取得良好平衡，LLaMA 3.2则在响应速度上更具优势。

## 📝 摘要（中文）

本文提出了FLUC，一个模块化框架，将开源的大型语言模型（LLMs）与无人机（UAV）自动驾驶系统集成，以实现飞行网络中的自主控制。FLUC能够将高层自然语言命令转换为可执行的无人机任务代码，弥合操作员意图与无人机行为之间的差距。通过对三种开源LLM（Qwen 2.5、Gemma 2和LLaMA 3.2）的评估，结果表明Qwen 2.5在多步推理中表现优异，Gemma 2在准确性和延迟之间取得平衡，而LLaMA 3.2则提供了更快的响应但逻辑一致性较低。能源感知无人机定位的案例研究确认了FLUC在解释结构化提示和自主执行领域特定逻辑方面的能力，展示了其在实时任务驱动控制中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决无人机控制中对高层自然语言命令理解不足的问题，现有方法往往无法有效桥接操作员意图与无人机行为之间的差距。

**核心思路**：FLUC框架的核心思想是利用大型语言模型的自然语言处理能力，将操作员的高层命令转化为无人机可执行的任务代码，从而实现自主控制。

**技术框架**：FLUC框架由多个模块组成，包括自然语言理解模块、任务生成模块和无人机控制模块。自然语言理解模块负责解析命令，任务生成模块将解析结果转化为代码，控制模块则执行生成的任务。

**关键创新**：FLUC的主要创新在于将开源大型语言模型与无人机控制系统相结合，形成了一个高效的命令转化机制，显著提升了无人机的自主控制能力。

**关键设计**：在设计中，FLUC采用了多种开源LLM进行评估，重点关注其在多步推理、准确性和响应速度等方面的表现，确保框架在不同场景下的适用性和有效性。

## 📊 实验亮点

实验结果表明，Qwen 2.5在多步推理任务中表现最佳，Gemma 2在准确性与延迟之间取得了良好平衡，而LLaMA 3.2则在响应速度上具有优势。FLUC框架的有效性在能源感知无人机定位的案例研究中得到了验证，展示了其在实时任务驱动控制中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括无人机自主飞行、智能物流、灾害监测等。FLUC框架能够提高无人机在复杂环境中的自主决策能力，具有重要的实际价值和广泛的应用前景，未来可能推动无人机技术的进一步发展。

## 📄 摘要（原文）

> This paper proposes FLUC, a modular framework that integrates open-source Large Language Models (LLMs) with Unmanned Aerial Vehicle (UAV) autopilot systems to enable autonomous control in Flying Networks (FNs). FLUC translates high-level natural language commands into executable UAV mission code, bridging the gap between operator intent and UAV behaviour.
>   FLUC is evaluated using three open-source LLMs - Qwen 2.5, Gemma 2, and LLaMA 3.2 - across scenarios involving code generation and mission planning. Results show that Qwen 2.5 excels in multi-step reasoning, Gemma 2 balances accuracy and latency, and LLaMA 3.2 offers faster responses with lower logical coherence. A case study on energy-aware UAV positioning confirms FLUC's ability to interpret structured prompts and autonomously execute domain-specific logic, showing its effectiveness in real-time, mission-driven control.

