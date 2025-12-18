---
layout: default
title: Towards General Agentic Intelligence via Environment Scaling
---

# Towards General Agentic Intelligence via Environment Scaling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13311" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13311v1</a>
  <a href="https://arxiv.org/pdf/2509.13311.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13311v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13311v1', 'Towards General Agentic Intelligence via Environment Scaling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Runnan Fang, Shihao Cai, Baixuan Li, Jialong Wu, Guangyu Li, Wenbiao Yin, Xinyu Wang, Xiaobin Wang, Liangcai Su, Zhen Zhang, Shibin Wu, Zhengwei Tao, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou

**分类**: cs.CL

**发布日期**: 2025-09-16

**备注**: https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/

---

## 💡 一句话要点

**AgentScaler：通过环境扩展提升通用Agent智能，增强函数调用能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agent智能` `函数调用` `环境扩展` `模拟环境` `两阶段微调`

## 📋 核心要点

1. 现有Agent在复杂、多样化的真实世界API交互中，函数调用能力不足，难以满足实际应用需求。
2. 提出AgentScaler框架，通过自动构建异构模拟环境，扩展Agent的训练场景，提升其函数调用能力。
3. 实验表明，AgentScaler在多个Agent基准测试中显著提升了模型的函数调用能力，验证了其有效性。

## 📝 摘要（中文）

为了在实际应用中部署大型语言模型，需要高级的Agent智能。多样化的真实世界API需要精确、鲁棒的函数调用智能，这需要Agent通过在不同环境中交互来发展这些能力。函数调用能力的广度与Agent训练环境的多样性密切相关。本文通过扩展环境来提升通用Agent智能。这带来了两个核心挑战：(i) 如何以一种有原则的方式扩展环境，以及 (ii) 如何有效地从与这些环境交互中获得的经验中训练Agent能力。为了解决这些问题，我们设计了一个可扩展的框架，该框架自动构建完全模拟的异构环境，系统地扩展了函数调用场景的空间。我们进一步采用了一种两阶段的Agent微调策略：首先赋予Agent基本的Agent能力，然后针对特定领域的上下文进行专门化。在Agent基准测试tau-bench、tau2-Bench和ACEBench上的大量实验表明，我们训练的模型AgentScaler显著增强了模型的函数调用能力。

## 🔬 方法详解

**问题定义**：现有Agent在面对真实世界中复杂且多样化的API时，函数调用能力不足，泛化性较差。主要痛点在于缺乏足够多样化的训练环境，导致Agent无法充分学习和适应各种函数调用场景。

**核心思路**：论文的核心思路是通过扩展Agent的训练环境来提升其函数调用能力。具体而言，设计一个可扩展的框架，能够自动构建异构的模拟环境，从而系统性地增加函数调用场景的多样性。通过在这些多样化的环境中进行训练，Agent可以学习到更鲁棒和泛化的函数调用策略。

**技术框架**：AgentScaler框架包含以下主要模块：1) **环境生成模块**：负责自动构建异构的模拟环境，涵盖各种函数调用场景。2) **Agent训练模块**：采用两阶段微调策略，首先赋予Agent基本的Agent能力，然后针对特定领域的上下文进行专门化训练。3) **评估模块**：使用多个Agent基准测试（tau-bench、tau2-Bench和ACEBench）来评估Agent的函数调用能力。整体流程是，首先通过环境生成模块构建多样化的训练环境，然后利用Agent训练模块在这些环境中训练Agent，最后通过评估模块评估Agent的性能。

**关键创新**：最重要的技术创新点在于自动构建异构模拟环境的方法。与以往手动设计环境的方法相比，该方法可以更高效、更系统地扩展Agent的训练环境，从而提升Agent的泛化能力。此外，两阶段微调策略也有助于Agent更好地学习和适应不同领域的函数调用场景。

**关键设计**：环境生成模块的具体实现细节未知，但其核心目标是生成多样化的函数调用场景。两阶段微调策略中，第一阶段可能采用通用的Agent训练目标，如模仿学习或强化学习，以赋予Agent基本的Agent能力。第二阶段则针对特定领域的上下文，采用领域相关的训练数据和目标，以提升Agent在该领域的函数调用能力。具体的参数设置、损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

AgentScaler在tau-bench、tau2-Bench和ACEBench等Agent基准测试中取得了显著的性能提升，表明其能够有效增强模型的函数调用能力。具体的性能数据和提升幅度在摘要中未给出，属于未知信息，需要在论文正文中查找。

## 🎯 应用场景

该研究成果可广泛应用于智能助手、自动化运维、智能客服等领域。通过提升Agent的函数调用能力，可以实现更智能、更高效的任务自动化，降低人工成本，提高用户体验。未来，该技术有望进一步扩展到更复杂的真实世界场景，例如智能家居、自动驾驶等。

## 📄 摘要（原文）

> Advanced agentic intelligence is a prerequisite for deploying Large Language Models in practical, real-world applications. Diverse real-world APIs demand precise, robust function-calling intelligence, which needs agents to develop these capabilities through interaction in varied environments. The breadth of function-calling competence is closely tied to the diversity of environments in which agents are trained. In this work, we scale up environments as a step towards advancing general agentic intelligence. This gives rise to two central challenges: (i) how to scale environments in a principled manner, and (ii) how to effectively train agentic capabilities from experiences derived through interactions with these environments. To address these, we design a scalable framework that automatically constructs heterogeneous environments that are fully simulated, systematically broadening the space of function-calling scenarios. We further adapt a two-phase agent fine-tuning strategy: first endowing agents with fundamental agentic capabilities, then specializing them for domain-specific contexts. Extensive experiments on agentic benchmarks, tau-bench, tau2-Bench, and ACEBench, demonstrate that our trained model, AgentScaler, significantly enhances the function-calling capability of models.

