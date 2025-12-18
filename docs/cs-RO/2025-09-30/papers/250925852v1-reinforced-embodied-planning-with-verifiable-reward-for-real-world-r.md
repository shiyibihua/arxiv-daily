---
layout: default
title: Reinforced Embodied Planning with Verifiable Reward for Real-World Robotic Manipulation
---

# Reinforced Embodied Planning with Verifiable Reward for Real-World Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25852" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25852v1</a>
  <a href="https://arxiv.org/pdf/2509.25852.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25852v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25852v1', 'Reinforced Embodied Planning with Verifiable Reward for Real-World Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zitong Bo, Yue Hu, Jinming Ma, Mingliang Zhou, Junhui Yin, Yachen Kang, Yuqi Liu, Tong Wu, Diyun Xiang, Hao Chen

**分类**: cs.RO

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**REVER：基于可验证奖励的强化具身规划，用于真实世界机器人操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `机器人操作` `视觉-语言模型` `强化学习` `长程规划` `可验证奖励` `链式思考`

## 📋 核心要点

1. 现有方法缺乏大规模、序列化的操作数据，难以训练视觉-语言模型(VLM)进行长程操作任务规划。
2. REVER框架通过自动化标注引擎生成视觉-指令-计划三元组数据，并设计可验证奖励来微调VLM。
3. 实验表明，RoboFarseer在长程任务中显著提升了机器人操作的成功率，超越了现有方法。

## 📝 摘要（中文）

本文提出REVER框架，旨在解决具身AI中机器人执行自由形式语言指令的长程操作任务的挑战。REVER赋能视觉-语言模型(VLM)在真实世界场景中生成和验证长程操作计划。该框架训练并发布了RoboFarseer，一个VLM，它被激励发出链式思考，执行时间和空间推理，确保物理上合理和逻辑上连贯的计划。为了获得训练数据，利用通用操作界面框架捕获硬件无关的原子技能演示，并使用自动标注引擎将每个演示转换为视觉-指令-计划三元组。引入了一种可验证奖励，通过其与真实技能序列的有序二分匹配重叠来对生成的计划进行评分。在运行时，微调后的VLM既充当规划器又充当监视器，验证逐步完成情况。RoboFarseer的性能与大几个数量级的专有模型相匹配或超过，并且在开放式规划中超过了最佳基线40%以上。在真实世界的长程任务中，与没有规划器的相同低级控制器相比，完整的系统将整体成功率提高了约60%。数据集和训练模型将在发表后开源。

## 🔬 方法详解

**问题定义**：机器人执行长程操作任务，需要根据自由形式的语言指令生成多步动作计划。现有方法缺乏足够规模的、包含自然语言和多步动作计划的序列操作数据，并且缺乏密集、可解释的奖励来微调VLM，导致VLM难以在真实世界中部署。

**核心思路**：利用VLM进行高层规划，生成操作计划，并通过可验证的奖励函数来评估和优化生成的计划。通过链式思考(Chain-of-Thought)的方式，让VLM进行时间和空间推理，生成物理上可行和逻辑上连贯的计划。使用通用操作界面框架获取原子技能演示，并自动标注生成训练数据。

**技术框架**：REVER框架包含以下几个主要模块：1) 数据收集模块：利用通用操作界面框架捕获原子技能演示，并使用自动标注引擎将每个演示转换为视觉-指令-计划三元组。2) VLM训练模块：训练RoboFarseer，一个VLM，使其能够根据语言指令生成操作计划。3) 奖励函数模块：设计可验证奖励，通过其与真实技能序列的有序二分匹配重叠来对生成的计划进行评分。4) 规划与监控模块：微调后的VLM既充当规划器又充当监视器，验证逐步完成情况。

**关键创新**：1) 提出了REVER框架，将VLM应用于长程机器人操作任务规划。2) 设计了可验证奖励，能够对生成的计划进行有效评估和优化。3) 构建了RoboFarseer，一个能够进行时间和空间推理的VLM，生成物理上可行和逻辑上连贯的计划。4) 自动化标注引擎，能够高效地生成训练数据。

**关键设计**：1) 使用链式思考(Chain-of-Thought)提示VLM进行推理。2) 可验证奖励基于生成的计划与真实技能序列的有序二分匹配重叠程度。3) RoboFarseer的训练目标是最大化可验证奖励，使其能够生成高质量的操作计划。

## 📊 实验亮点

RoboFarseer在开放式规划任务中超过了最佳基线40%以上，并且性能与大几个数量级的专有模型相匹配或超过。在真实世界的长程任务中，与没有规划器的相同低级控制器相比，完整的系统将整体成功率提高了约60%。这些结果表明，REVER框架和RoboFarseer在长程机器人操作任务中具有显著优势。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务，例如家庭服务机器人、工业自动化机器人等。通过将自然语言指令转化为可执行的机器人动作计划，可以显著提高机器人的智能化水平和操作效率，降低人工干预的需求。未来，该技术有望在智能家居、智能制造等领域发挥重要作用。

## 📄 摘要（原文）

> Enabling robots to execute long-horizon manipulation tasks from free-form language instructions remains a fundamental challenge in embodied AI. While vision-language models (VLMs) have shown promise as high-level planners, their deployment in the real world is hindered by two gaps: (i) the scarcity of large-scale, sequential manipulation data that couples natural language with multi-step action plans, and (ii) the absence of dense, interpretable rewards for fine-tuning VLMs on planning objectives. To address these issues, we propose REVER, a framework that empowers VLMs to generate and validate long-horizon manipulation plans from natural language instructions in real-world scenarios. Under REVER we train and release RoboFarseer, a VLM incentivized to emit chain-of-thought that perform temporal and spatial reasoning, ensuring physically plausible and logically coherent plans. To obtain training data, we leverage the Universal Manipulation Interface framework to capture hardware-agnostic demonstrations of atomic skills. An automated annotation engine converts each demonstration into vision-instruction-plan triplet. We introduce a verifiable reward that scores the generated plan by its ordered bipartite matching overlap with the ground-truth skill sequence. At run time, the fine-tuned VLM functions both as a planner and as a monitor, verifying step-wise completion. RoboFarseer matches or exceeds the performance of proprietary models that are orders of magnitude larger, while on open-ended planning it surpasses the best baseline by more than 40%. In real-world, long-horizon tasks, the complete system boosts overall success by roughly 60% compared with the same low-level controller without the planner. We will open-source both the dataset and the trained model upon publication.

