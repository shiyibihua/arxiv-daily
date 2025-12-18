---
layout: default
title: Improving the Efficiency of LLM Agent Systems through Trajectory Reduction
---

# Improving the Efficiency of LLM Agent Systems through Trajectory Reduction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23586" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23586v1</a>
  <a href="https://arxiv.org/pdf/2509.23586.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23586v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23586v1', 'Improving the Efficiency of LLM Agent Systems through Trajectory Reduction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuan-An Xiao, Pengfei Gao, Chao Peng, Yingfei Xiong

**分类**: cs.SE, cs.AI

**发布日期**: 2025-09-28

**备注**: 20 pages, 4 figures

---

## 💡 一句话要点

**AgentDiet：通过轨迹缩减提升LLM Agent系统效率，降低计算成本。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM Agent` `轨迹缩减` `效率优化` `计算成本` `推理优化`

## 📋 核心要点

1. 现有LLM Agent系统在软件工程任务中表现出色，但由于轨迹不断增长，输入token的计算成本高昂，效率问题日益突出。
2. AgentDiet通过分析Agent轨迹，自动移除无用、冗余和过期信息，从而在推理时缩减轨迹，降低计算成本。
3. 实验表明，AgentDiet在保持Agent性能不变的情况下，能够显著减少输入token和计算成本，验证了轨迹缩减的有效性。

## 📝 摘要（中文）

本文针对基于大型语言模型（LLM）的多轮Agent系统在软件工程任务中面临的效率问题，提出了一种推理时轨迹缩减方法AgentDiet。通过分析现有Agent轨迹，发现其中存在大量无用、冗余和过期信息，这些信息可以在不影响Agent性能的前提下被识别和缩减。AgentDiet能够自动移除这些冗余信息。在两个LLM和两个基准测试上的评估结果表明，AgentDiet能够减少39.9% ~ 59.7%的输入token，或降低21.1% ~ 35.9%的最终计算成本，同时保持Agent的性能不变。这表明轨迹缩减是Agent系统一个有前景的研究方向。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM Agent系统中因轨迹长度不断增加而导致的计算成本高昂问题。现有方法通常忽略了Agent轨迹中存在的冗余信息，导致效率低下。痛点在于如何在不影响Agent性能的前提下，降低计算资源消耗。

**核心思路**：论文的核心思路是通过识别并移除Agent轨迹中的无用、冗余和过期信息，从而缩减轨迹长度，降低输入token数量，最终降低计算成本。这种方法基于观察到Agent轨迹中存在大量此类冗余信息，且移除这些信息不会显著影响Agent的决策能力。

**技术框架**：AgentDiet 的整体框架包含轨迹分析和轨迹缩减两个主要阶段。首先，通过分析Agent的交互历史，识别出可以安全移除的信息类型。然后，根据预定义的规则或策略，自动从轨迹中移除这些信息。这个过程在推理时进行，不会影响Agent的训练过程。

**关键创新**：AgentDiet 的关键创新在于提出了一种简单而有效的轨迹缩减方法，能够在不影响Agent性能的前提下显著降低计算成本。与现有方法相比，AgentDiet 专注于优化推理效率，而无需修改Agent的训练过程或模型结构。

**关键设计**：AgentDiet 的关键设计包括：(1) 定义了不同类型的冗余信息，例如无用信息、冗余信息和过期信息；(2) 设计了相应的规则或策略来识别和移除这些信息；(3) 通过实验评估了不同缩减策略对Agent性能和计算成本的影响，并选择了最优的策略。

## 📊 实验亮点

实验结果表明，AgentDiet 在两个 LLM 和两个基准测试上均表现出色，能够减少 39.9% ~ 59.7% 的输入 token，或降低 21.1% ~ 35.9% 的最终计算成本，同时保持 Agent 的性能不变。这些数据有力地证明了 AgentDiet 的有效性和实用性。

## 🎯 应用场景

该研究成果可广泛应用于各种基于LLM的Agent系统，尤其是在资源受限或对延迟敏感的应用场景中，例如移动设备上的智能助手、边缘计算环境下的自动化任务执行等。通过降低计算成本，可以使LLM Agent系统更易于部署和使用，加速其在实际应用中的普及。

## 📄 摘要（原文）

> Multi-turn agent systems based on Large Language Models (LLMs) have been increasingly popular for software engineering tasks. While LLM agents show decent effectiveness, the high computational cost of input tokens due to the ever-growing trajectory remains an efficiency concern for their applications. Efficiency is largely neglected in existing studies and agent products, and this paper fills the gap by introducing an inference-time trajectory reduction approach to reduce the cost of agents.
>   Through analyzing existing agent trajectories, we demonstrate that useless, redundant, and expired information is widespread in all trajectories, which can be identified and reduced without harming the agent's performance. We then design a simple yet effective trajectory reduction approach, AgentDiet, which automatically removes such waste information. We implement AgentDiet on a top-performing coding agent, and the evaluation on two LLMs and two benchmarks shows that AgentDiet can reduce input tokens by 39.9% ~ 59.7%, or the final computational cost by 21.1% ~ 35.9%, while maintaining the same agent performance. This indicates that trajectory reduction is a promising direction for agent systems.

