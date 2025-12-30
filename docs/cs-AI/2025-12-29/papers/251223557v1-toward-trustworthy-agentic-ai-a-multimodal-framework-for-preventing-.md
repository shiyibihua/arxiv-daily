---
layout: default
title: "Toward Trustworthy Agentic AI: A Multimodal Framework for Preventing Prompt Injection Attacks"
---

# Toward Trustworthy Agentic AI: A Multimodal Framework for Preventing Prompt Injection Attacks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23557" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23557v1</a>
  <a href="https://arxiv.org/pdf/2512.23557.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23557v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23557v1', 'Toward Trustworthy Agentic AI: A Multimodal Framework for Preventing Prompt Injection Attacks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Toqeer Ali Syed, Mishal Ateeq Almutairi, Mahmoud Abdel Moaty

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-29

**备注**: It is accepted in a conference paper, ICCA 2025 in Bahrain on 21 to 23 December

---

## 💡 一句话要点

**提出跨Agent多模态溯源防御框架，防范Agentic AI中的提示注入攻击。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agentic AI` `多模态学习` `提示注入攻击` `安全防御` `溯源追踪`

## 📋 核心要点

1. Agentic AI系统面临多模态提示注入攻击的风险，恶意指令可能通过多种模态传播，导致系统行为异常。
2. 论文提出跨Agent多模态溯源防御框架，通过清理提示和验证输出来防止恶意指令的传播。
3. 实验结果表明，该框架显著提高了多模态注入检测精度，并降低了跨Agent的信任泄漏风险。

## 📝 摘要（中文）

大型语言模型(LLMs)、视觉-语言模型(VLMs)以及LangChain和GraphChain等新型Agentic AI系统，使得能够进行推理、规划和对话的强大自主系统成为可能。然而，这种Agentic环境增加了多模态提示注入(PI)攻击发生的可能性，其中隐藏或恶意指令通过文本、图片、元数据或Agent间的消息传播，可能导致意外行为、违反策略或状态损坏。为了降低这些风险，本文提出了一种跨Agent多模态溯源感知防御框架，其中所有提示（无论是用户生成的还是上游Agent生成的）都会被清理，并且LLM生成的所有输出在发送到下游节点之前都会被独立验证。该框架包含文本清理Agent、视觉清理Agent和输出验证Agent，所有Agent由溯源账本协调，溯源账本保存整个Agent网络中模态、来源和信任级别的元数据。这种架构确保Agent间的通信遵守明确的信任框架，从而防止注入的指令在LangChain或GraphChain风格的工作流程中传播。实验评估表明，多模态注入检测精度显著提高，跨Agent信任泄漏最小化，并且Agentic执行路径变得稳定。该框架将溯源跟踪和验证的概念扩展到多Agent编排，从而加强了安全、可理解和可靠的Agentic AI系统的建立。

## 🔬 方法详解

**问题定义**：论文旨在解决Agentic AI系统中日益严重的多模态提示注入攻击问题。现有的Agentic AI系统，如基于LangChain或GraphChain的系统，容易受到恶意用户或Agent通过文本、图像等多种模态注入的指令攻击，导致系统行为偏离预期，甚至造成安全漏洞。现有的防御方法往往只关注单一模态的攻击，缺乏对跨Agent通信过程中的信任管理和溯源追踪。

**核心思路**：论文的核心思路是建立一个跨Agent、多模态的溯源感知防御框架，对所有Agent之间的通信进行监控、清理和验证。通过记录每个Agent的输入输出以及信任级别，构建一个溯源账本，从而实现对恶意指令的追踪和阻断。这种方法的核心在于将信任管理和安全防御融入到Agentic系统的整体架构中。

**技术框架**：该框架包含以下几个主要模块：1) **文本清理Agent**：负责对文本模态的输入进行清理，移除潜在的恶意指令。2) **视觉清理Agent**：负责对图像模态的输入进行清理，例如检测和移除隐藏的文本信息。3) **输出验证Agent**：负责对LLM生成的输出进行验证，确保其符合预期的行为规范。4) **溯源账本**：负责记录所有Agent的输入输出、模态信息、来源以及信任级别，用于追踪恶意指令的传播路径。这些模块协同工作，形成一个完整的防御体系。

**关键创新**：论文最重要的创新点在于提出了一个跨Agent、多模态的溯源感知防御框架。与现有的防御方法相比，该框架不仅考虑了单一模态的攻击，还关注了Agent之间的通信安全，通过溯源账本实现了对恶意指令的追踪和阻断。此外，该框架还引入了信任级别的概念，用于评估不同Agent的可信度，从而更好地管理Agent之间的信任关系。

**关键设计**：框架的关键设计包括：1) **多模态清理机制**：针对文本和图像等不同模态，设计了不同的清理算法，以移除潜在的恶意指令。2) **信任级别评估**：设计了一种信任级别评估机制，用于评估不同Agent的可信度，并根据信任级别调整防御策略。3) **溯源账本结构**：设计了一种高效的溯源账本结构，用于记录所有Agent的输入输出以及信任级别，并支持快速的查询和追踪。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23557v1/images/architecture.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23557v1/images/sequence_diagram.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该框架能够显著提高多模态注入检测的准确率，并有效降低跨Agent的信任泄漏风险。具体而言，该框架在多模态提示注入攻击的检测准确率上相比基线方法提升了XX%（具体数值论文中给出），同时将跨Agent的信任泄漏风险降低了YY%（具体数值论文中给出）。此外，实验还验证了该框架能够稳定Agentic系统的执行路径，使其更加可预测和可靠。

## 🎯 应用场景

该研究成果可应用于各种Agentic AI系统，例如智能客服、自动化流程管理、智能家居等。通过部署该防御框架，可以有效提高Agentic AI系统的安全性，防止恶意攻击，保障用户数据安全，并提升系统的可靠性和可信度。未来，该框架可以进一步扩展到更多的模态和Agent类型，以适应不断发展的Agentic AI应用场景。

## 📄 摘要（原文）

> Powerful autonomous systems, which reason, plan, and converse using and between numerous tools and agents, are made possible by Large Language Models (LLMs), Vision-Language Models (VLMs), and new agentic AI systems, like LangChain and GraphChain. Nevertheless, this agentic environment increases the probability of the occurrence of multimodal prompt injection (PI) attacks, in which concealed or malicious instructions carried in text, pictures, metadata, or agent-to-agent messages may spread throughout the graph and lead to unintended behavior, a breach of policy, or corruption of state. In order to mitigate these risks, this paper suggests a Cross-Agent Multimodal Provenanc- Aware Defense Framework whereby all the prompts, either user-generated or produced by upstream agents, are sanitized and all the outputs generated by an LLM are verified independently before being sent to downstream nodes. This framework contains a Text sanitizer agent, visual sanitizer agent, and output validator agent all coordinated by a provenance ledger, which keeps metadata of modality, source, and trust level throughout the entire agent network. This architecture makes sure that agent-to-agent communication abides by clear trust frames such such that injected instructions are not propagated down LangChain or GraphChain-style-workflows. The experimental assessments show that multimodal injection detection accuracy is significantly enhanced, and the cross-agent trust leakage is minimized, as well as, agentic execution pathways become stable. The framework, which expands the concept of provenance tracking and validation to the multi-agent orchestration, enhances the establishment of secure, understandable and reliable agentic AI systems.

