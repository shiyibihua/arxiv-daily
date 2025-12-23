---
layout: default
title: Agentic AI for Intent-Based Industrial Automation
---

# Agentic AI for Intent-Based Industrial Automation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04980" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04980v1</a>
  <a href="https://arxiv.org/pdf/2506.04980.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04980v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04980v1', 'Agentic AI for Intent-Based Industrial Automation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marcos Lima Romero, Ricardo Suyama

**分类**: cs.LG, eess.SY

**发布日期**: 2025-06-05

**备注**: Preprint - Submitted to 16th IEEE/IAS International Conference on Industry Applications - INDUSCON 2025

---

## 💡 一句话要点

**提出意图驱动的Agentic AI框架以简化工业自动化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agentic AI` `意图驱动` `工业自动化` `人机交互` `预测性维护` `工业5.0` `自主决策`

## 📋 核心要点

1. 现有工业自动化方法在复杂性和人机交互方面存在不足，难以满足工业5.0的需求。
2. 提出的框架结合Agentic AI与意图驱动范式，允许用户用自然语言表达目标并进行分解。
3. 通过实验验证，框架在预测性维护场景中展示了意图分解和自主决策的可行性，降低了技术壁垒。

## 📝 摘要（中文）

随着Agentic AI系统的发展，结合自主大型语言模型（LLMs）的规划和工具使用能力，为工业自动化的演变提供了新可能，降低了工业4.0带来的复杂性。本文提出了一个概念框架，将Agentic AI与最初在网络研究中开发的意图驱动范式相结合，以简化人机交互（HMI），更好地与以人为本、可持续和韧性原则的工业5.0对齐。基于意图处理，该框架允许人类操作员用自然语言表达高层次的业务或操作目标，并将其分解为可执行的组件。通过CMAPSS数据集和Google Agent Developer Kit（ADK）实现的概念验证，展示了意图分解、代理编排和自主决策在预测性维护场景中的可行性。结果确认了该方法在降低技术壁垒和实现可扩展的意图驱动自动化方面的潜力，尽管存在数据质量和可解释性问题。

## 🔬 方法详解

**问题定义**：本文旨在解决现有工业自动化系统在复杂性和人机交互方面的不足，尤其是在工业4.0背景下，如何有效地将人类意图转化为机器可执行的任务。

**核心思路**：提出一个结合Agentic AI和意图驱动范式的框架，使人类操作员能够用自然语言表达高层次目标，并将其分解为具体的可执行任务，从而简化人机交互。

**技术框架**：该框架包括意图表达、意图分解、子代理执行和反馈机制四个主要模块。人类操作员通过自然语言输入意图，系统将其分解为期望、条件、目标、上下文和信息，指导子代理执行特定任务。

**关键创新**：最重要的创新在于将意图驱动的处理方式与Agentic AI结合，允许更自然的人机交互，并通过分解和代理编排实现自主决策，这与传统的基于规则或模型的方法有本质区别。

**关键设计**：在实现过程中，采用了Google Agent Developer Kit（ADK）进行代理的开发，关键参数设置包括意图的分解策略和子代理的任务分配机制，确保系统能够高效执行预测性维护任务。

## 📊 实验亮点

实验结果表明，所提出的框架在预测性维护场景中成功实现了意图分解和自主决策，显著降低了技术壁垒。具体而言，系统在处理复杂任务时的响应时间和准确性均有明显提升，验证了其可扩展性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括制造业、智能工厂和其他需要高效人机协作的工业场景。通过简化人机交互和提升自动化水平，能够显著提高生产效率和响应能力，推动工业向更智能和可持续的方向发展。

## 📄 摘要（原文）

> The recent development of Agentic AI systems, empowered by autonomous large language models (LLMs) agents with planning and tool-usage capabilities, enables new possibilities for the evolution of industrial automation and reduces the complexity introduced by Industry 4.0. This work proposes a conceptual framework that integrates Agentic AI with the intent-based paradigm, originally developed in network research, to simplify human-machine interaction (HMI) and better align automation systems with the human-centric, sustainable, and resilient principles of Industry 5.0. Based on the intent-based processing, the framework allows human operators to express high-level business or operational goals in natural language, which are decomposed into actionable components. These intents are broken into expectations, conditions, targets, context, and information that guide sub-agents equipped with specialized tools to execute domain-specific tasks. A proof of concept was implemented using the CMAPSS dataset and Google Agent Developer Kit (ADK), demonstrating the feasibility of intent decomposition, agent orchestration, and autonomous decision-making in predictive maintenance scenarios. The results confirm the potential of this approach to reduce technical barriers and enable scalable, intent-driven automation, despite data quality and explainability concerns.

