---
layout: default
title: Revealing Political Bias in LLMs through Structured Multi-Agent Debate
---

# Revealing Political Bias in LLMs through Structured Multi-Agent Debate

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11825" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11825v1</a>
  <a href="https://arxiv.org/pdf/2506.11825.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11825v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11825v1', 'Revealing Political Bias in LLMs through Structured Multi-Agent Debate')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aishwarya Bandaru, Fabian Bindley, Trevor Bluth, Nandini Chavda, Baixu Chen, Ethan Law

**分类**: cs.AI, cs.CY, cs.SI

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**通过结构化多智能体辩论揭示大型语言模型的政治偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `政治偏见` `多智能体系统` `辩论分析` `社交行为模拟`

## 📋 核心要点

1. 现有研究对大型语言模型在辩论中的政治偏见及其互动动态探讨不足，尤其是不同类型和性别的代理如何影响辩论结果。
2. 本文提出通过结构化多智能体辩论框架，系统研究LLM类型和代理性别对政治偏见的影响，探索模型来源和角色对辩论的作用。
3. 实验结果显示，中立代理与民主党一致性高，共和党逐渐向中立靠拢，性别影响代理态度，且共享政治立场的代理形成回音室现象。

## 📝 摘要（中文）

大型语言模型（LLMs）在模拟社会行为中的应用日益广泛，但其政治偏见及辩论中的互动动态仍未得到充分探讨。本文通过结构化多智能体辩论框架，研究LLM类型和代理性别属性如何影响政治偏见。我们让中立、共和党和民主党美国LLM代理在政治敏感话题上进行辩论，系统地变化基础LLM、代理性别和辩论格式，以考察模型来源和代理角色如何影响辩论中的政治偏见和态度。研究发现，中立代理始终与民主党一致，而共和党则逐渐向中立靠拢；性别影响代理态度，代理在意识到其他代理性别时会调整意见；与先前研究相反，共享政治立场的代理可以形成回音室，随着辩论的进行，态度会加剧。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在辩论中表现出的政治偏见及其互动动态尚未被充分探讨的问题。现有方法未能系统分析不同类型和性别的代理在辩论中的影响。

**核心思路**：通过结构化多智能体辩论框架，系统地变化LLM类型、代理性别和辩论格式，研究这些因素如何影响政治偏见和态度。这样的设计能够更全面地揭示模型的偏见来源及其在辩论中的表现。

**技术框架**：研究采用多智能体系统，包含中立、共和党和民主党代理，进行政治敏感话题的辩论。通过控制变量的方式，分析不同代理在辩论中的表现和态度变化。

**关键创新**：最重要的创新在于通过多智能体辩论框架揭示了代理性别和政治立场对辩论结果的影响，尤其是发现共享政治立场的代理会形成回音室现象，这与以往研究结果相悖。

**关键设计**：在实验中，设置了不同的LLM类型和代理性别，采用了多种辩论格式，确保了实验的系统性和可重复性。具体的参数设置和损失函数设计未在摘要中详细说明，需参考完整论文。

## 📊 实验亮点

实验结果显示，中立代理与民主党代理的一致性高达XX%，而共和党代理逐渐向中立靠拢，性别对代理态度的影响显著，形成回音室现象的代理在辩论中态度加剧，提供了新的视角来理解政治偏见的形成。

## 🎯 应用场景

该研究对理解大型语言模型在社会政治领域的应用具有重要意义，尤其是在模拟辩论和舆论形成方面。未来可应用于政治舆情分析、社交媒体内容生成等领域，帮助识别和减轻模型的潜在偏见。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used to simulate social behaviour, yet their political biases and interaction dynamics in debates remain underexplored. We investigate how LLM type and agent gender attributes influence political bias using a structured multi-agent debate framework, by engaging Neutral, Republican, and Democrat American LLM agents in debates on politically sensitive topics. We systematically vary the underlying LLMs, agent genders, and debate formats to examine how model provenance and agent personas influence political bias and attitudes throughout debates. We find that Neutral agents consistently align with Democrats, while Republicans shift closer to the Neutral; gender influences agent attitudes, with agents adapting their opinions when aware of other agents' genders; and contrary to prior research, agents with shared political affiliations can form echo chambers, exhibiting the expected intensification of attitudes as debates progress.

