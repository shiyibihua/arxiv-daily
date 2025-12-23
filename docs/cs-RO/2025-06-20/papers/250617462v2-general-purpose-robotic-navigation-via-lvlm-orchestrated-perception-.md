---
layout: default
title: General-Purpose Robotic Navigation via LVLM-Orchestrated Perception, Reasoning, and Acting
---

# General-Purpose Robotic Navigation via LVLM-Orchestrated Perception, Reasoning, and Acting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17462" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17462v2</a>
  <a href="https://arxiv.org/pdf/2506.17462.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17462v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17462v2', 'General-Purpose Robotic Navigation via LVLM-Orchestrated Perception, Reasoning, and Acting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bernard Lange, Anil Yildiz, Mansur Arief, Shehryar Khattak, Mykel Kochenderfer, Georgios Georgakis

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-06-20 (更新: 2025-10-17)

---

## 💡 一句话要点

**提出ARNA框架以解决未知环境中的通用导航问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `通用导航` `视觉语言模型` `机器人技术` `自主决策` `多模态输入`

## 📋 核心要点

1. 现有机器人导航系统通常依赖于特定任务的神经网络，缺乏在未知环境中的通用性和灵活性。
2. 本文提出的ARNA框架通过结合LVLM与现代机器人工具库，使代理人能够自主定义和执行任务特定的工作流。
3. 在Habitat Lab的实验中，ARNA在HM-EQA基准测试中超越了现有的最先进方法，展示了其强大的泛化能力。

## 📝 摘要（中文）

在机器人技术中，为未知环境开发通用导航策略仍然是一个核心挑战。现有系统通常依赖于特定任务的神经网络和固定的信息流，限制了其通用性。大型视觉语言模型（LVLMs）通过嵌入类人知识为推理和规划提供了有希望的替代方案，但之前的LVLM-机器人集成主要依赖于预先映射的空间和硬编码的表示。本文提出了Agentic Robotic Navigation Architecture（ARNA），这是一个通用框架，赋予基于LVLM的代理人一套来自现代机器人栈的感知、推理和导航工具。ARNA在Habitat Lab的HM-EQA基准测试中表现优于现有的EQA特定方法，展示了其在广泛导航挑战中的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在未知环境中的通用导航问题。现有方法通常依赖于特定任务的神经网络和固定的信息流，限制了其在新环境中的适应能力。

**核心思路**：ARNA框架通过结合大型视觉语言模型（LVLM）与现代机器人技术，赋予代理人自主定义和执行任务特定工作流的能力，从而实现更灵活的导航和推理。

**技术框架**：ARNA的整体架构包括感知、推理和导航模块，代理人在运行时通过查询这些模块来处理多模态输入，并选择合适的导航动作。

**关键创新**：ARNA的主要创新在于其代理人能够在未映射的环境中自主执行任务，突破了以往依赖于硬编码和预映射空间的限制。

**关键设计**：ARNA的设计包括模块化的感知和推理工具，允许代理人根据实时输入动态调整导航策略，具体参数设置和损失函数的细节在论文中进行了详细讨论。

## 📊 实验亮点

在Habitat Lab的HM-EQA基准测试中，ARNA框架的表现超越了当前最先进的EQA特定方法，展示了显著的性能提升，具体数据在实验中进行了详细对比，证明了其在多种导航挑战中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、自动驾驶、无人机导航等。ARNA框架的灵活性和通用性使其能够适应各种复杂环境，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Developing general-purpose navigation policies for unknown environments remains a core challenge in robotics. Most existing systems rely on task-specific neural networks and fixed information flows, limiting their generalizability. Large Vision-Language Models (LVLMs) offer a promising alternative by embedding human-like knowledge for reasoning and planning, but prior LVLM-robot integrations have largely depended on pre-mapped spaces, hard-coded representations, and rigid control logic. We introduce the Agentic Robotic Navigation Architecture (ARNA), a general-purpose framework that equips an LVLM-based agent with a library of perception, reasoning, and navigation tools drawn from modern robotic stacks. At runtime, the agent autonomously defines and executes task-specific workflows that iteratively query modules, reason over multimodal inputs, and select navigation actions. This agentic formulation enables robust navigation and reasoning in previously unmapped environments, offering a new perspective on robotic stack design. Evaluated in Habitat Lab on the HM-EQA benchmark, ARNA outperforms state-of-the-art EQA-specific approaches. Qualitative results on RxR and custom tasks further demonstrate its ability to generalize across a broad range of navigation challenges.

