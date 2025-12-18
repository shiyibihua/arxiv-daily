---
layout: default
title: Generalizable Skill Learning for Construction Robots with Crowdsourced Natural Language Instructions, Composable Skills Standardization, and Large Language Model
---

# Generalizable Skill Learning for Construction Robots with Crowdsourced Natural Language Instructions, Composable Skills Standardization, and Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02876" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02876v1</a>
  <a href="https://arxiv.org/pdf/2509.02876.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02876v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02876v1', 'Generalizable Skill Learning for Construction Robots with Crowdsourced Natural Language Instructions, Composable Skills Standardization, and Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongrui Yu, Vineet R. Kamat, Carol C. Menassa

**分类**: cs.RO

**发布日期**: 2025-09-02

**备注**: Under review for ASCE OPEN: Multidisciplinary Journal of Civil Engineering

---

## 💡 一句话要点

**提出基于众包自然语言指令和LLM的通用建筑机器人技能学习方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `建筑机器人` `技能学习` `自然语言指令` `大型语言模型` `多任务学习`

## 📋 核心要点

1. 现有建筑机器人编程缺乏通用性，难以适应不同任务，需要大量人工重新编程。
2. 提出一种基于众包自然语言指令和大型语言模型（LLM）的通用技能学习架构，实现多任务技能迁移。
3. 通过石膏板安装实验验证了所提方案，结果表明该方案能以最小的努力和高质量实现多任务重新编程。

## 📝 摘要（中文）

建筑工作的准重复性以及由此导致的建筑机器人编程缺乏通用性，对机器人在建筑行业的广泛应用提出了持续的挑战。由于从一个领域学习到的技能无法轻易转移到另一个工作领域或直接用于执行不同的任务，机器人无法实现通用能力。人工需要费力地重新编程其场景理解、路径规划和操作组件，以使机器人能够执行替代工作任务。本文提出的方法通过提出一种通用的学习架构，直接通过众包在线自然语言指令来教导机器人执行多功能任务，从而解决了很大一部分此类重新编程工作量。开发了一个大型语言模型（LLM）、一种标准化和模块化的分层建模方法以及建筑信息模型-机器人语义数据管道，以解决多任务技能转移问题。所提出的技能标准化方案和基于LLM的分层技能学习框架通过使用全尺寸工业机器人机械臂的长期石膏板安装实验进行了测试。由此产生的机器人任务学习方案以最小的努力和高质量实现了多任务重新编程。

## 🔬 方法详解

**问题定义**：论文旨在解决建筑机器人技能学习中缺乏通用性的问题。现有方法需要针对每个新任务进行繁琐的重新编程，包括场景理解、路径规划和操作等模块，导致部署成本高昂且效率低下。痛点在于无法将从一个任务中学到的技能迁移到其他任务，限制了建筑机器人的广泛应用。

**核心思路**：论文的核心思路是利用众包的自然语言指令来直接训练机器人，使其能够执行多样的任务。通过将任务分解为标准化的、模块化的技能，并借助大型语言模型（LLM）理解自然语言指令，机器人可以学习如何组合这些技能来完成不同的任务，从而实现技能的通用性和可迁移性。

**技术框架**：整体框架包含以下几个主要模块：1) **众包自然语言指令收集**：收集人类工人提供的关于如何执行特定任务的自然语言指令。2) **Building Information Modeling (BIM)-Robot 语义数据管道**：用于提供机器人操作环境的语义信息。3) **标准化和模块化的技能建模**：将机器人操作分解为一系列标准化的、可复用的技能模块。4) **基于 LLM 的分层技能学习框架**：利用 LLM 理解自然语言指令，并将其映射到相应的技能序列。5) **机器人控制与执行**：根据 LLM 生成的技能序列，控制机器人执行任务。

**关键创新**：论文的关键创新在于将大型语言模型（LLM）引入到建筑机器人的技能学习中，利用 LLM 的自然语言理解能力，实现了从自然语言指令到机器人技能的自动映射。此外，提出的标准化和模块化的技能建模方法，使得技能可以被复用和组合，大大提高了技能的通用性和可迁移性。

**关键设计**：论文的关键设计包括：1) **技能标准化方案**：定义了一套标准化的技能接口，使得不同的技能模块可以无缝集成。2) **LLM 的训练和微调**：使用建筑领域的知识对 LLM 进行训练和微调，以提高其对建筑任务相关指令的理解能力。3) **分层技能学习框架**：将任务分解为多个层次的技能，从高层到低层逐步执行，提高了任务的复杂度和灵活性。

## 📊 实验亮点

该研究通过全尺寸工业机器人机械臂的石膏板安装实验验证了所提方案的有效性。实验结果表明，该方案能够以最小的努力和高质量实现多任务重新编程，显著降低了人工干预的需求。具体的性能数据和对比基线在论文中未明确给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于各种建筑机器人任务，例如砌砖、粉刷、管道安装等。通过众包自然语言指令，可以快速部署机器人执行新的任务，降低了机器人编程的成本和难度。未来，该技术有望实现建筑工地的自动化和智能化，提高施工效率和质量，并减少人工劳动强度。

## 📄 摘要（原文）

> The quasi-repetitive nature of construction work and the resulting lack of generalizability in programming construction robots presents persistent challenges to the broad adoption of robots in the construction industry. Robots cannot achieve generalist capabilities as skills learnt from one domain cannot readily transfer to another work domain or be directly used to perform a different set of tasks. Human workers have to arduously reprogram their scene-understanding, path-planning, and manipulation components to enable the robots to perform alternate work tasks. The methods presented in this paper resolve a significant proportion of such reprogramming workload by proposing a generalizable learning architecture that directly teaches robots versatile task-performance skills through crowdsourced online natural language instructions. A Large Language Model (LLM), a standardized and modularized hierarchical modeling approach, and Building Information Modeling-Robot sematic data pipeline are developed to address the multi-task skill transfer problem. The proposed skill standardization scheme and LLM-based hierarchical skill learning framework were tested with a long-horizon drywall installation experiment using a full-scale industrial robotic manipulator. The resulting robot task learning scheme achieves multi-task reprogramming with minimal effort and high quality.

