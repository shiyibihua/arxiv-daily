---
layout: default
title: Incident Analysis for AI Agents
---

# Incident Analysis for AI Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14231" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14231v1</a>
  <a href="https://arxiv.org/pdf/2508.14231.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14231v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14231v1', 'Incident Analysis for AI Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Carson Ezell, Xavier Roberts-Gaal, Alan Chan

**分类**: cs.CY, cs.AI

**发布日期**: 2025-08-19

**备注**: 16 pages (10 pages main text), 4 figures, 3 tables. To be published in the Proceedings of the 2025 AAAI/ACM Conference on AI, Ethics, & Society (AIES)

---

## 💡 一句话要点

**提出AI代理事件分析框架以解决安全隐患问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI代理` `事件分析` `安全管理` `系统安全` `风险评估`

## 📋 核心要点

1. 现有的事件报告流程主要依赖公开数据，无法获取敏感信息，导致对AI代理事件的理解不足。
2. 本文提出了一种事件分析框架，识别系统相关、上下文和认知等因素，以便更好地理解和预防事件。
3. 通过结构化的信息收集和分析，本文为未来AI代理的安全管理提供了新的思路和建议。

## 📝 摘要（中文）

随着AI代理的广泛应用，事件发生的频率可能会增加，这些事件可能直接或间接造成伤害。现有的事件报告流程无法充分理解AI代理事件，尤其是缺乏敏感信息的收集。为此，本文提出了一种事件分析框架，识别出系统相关、上下文和认知等三类因素，旨在通过结构化的信息收集来预防未来事件的发生。我们还提供了关于事件报告应包含的信息和开发者应保留的信息的建议，以帮助事件调查。

## 🔬 方法详解

**问题定义**：本文旨在解决现有AI代理事件报告流程不足的问题，特别是缺乏对敏感信息的收集和分析，导致无法全面理解事件的成因。

**核心思路**：提出了一种基于系统安全方法的事件分析框架，识别出导致事件的三类因素：系统相关因素、上下文因素和认知因素，以便更全面地分析事件原因。

**技术框架**：框架包括三个主要模块：1) 事件数据收集，涵盖用户提示、活动日志等；2) 事件分析，基于识别的因素进行深入分析；3) 事件报告生成，提供结构化的报告以供调查使用。

**关键创新**：最重要的创新在于提出了系统相关、上下文和认知三类因素的分类方法，填补了现有方法在事件分析中的空白。

**关键设计**：框架中强调了活动日志、系统文档和工具信息的收集，确保能够提供全面的事件背景信息，以支持后续的事件调查和分析。

## 📊 实验亮点

本文提出的事件分析框架为AI代理事件的理解提供了新的视角，强调了系统相关、上下文和认知因素的重要性。通过结构化的信息收集，能够显著提高事件调查的效率和准确性，为未来的AI代理安全管理奠定基础。

## 🎯 应用场景

该研究的潜在应用领域包括AI代理的安全审计、事件响应和风险管理。通过建立有效的事件分析框架，可以帮助开发者和部署者更好地理解和应对AI代理使用中的安全隐患，提升整体系统的安全性和可靠性。

## 📄 摘要（原文）

> As AI agents become more widely deployed, we are likely to see an increasing number of incidents: events involving AI agent use that directly or indirectly cause harm. For example, agents could be prompt-injected to exfiltrate private information or make unauthorized purchases. Structured information about such incidents (e.g., user prompts) can help us understand their causes and prevent future occurrences. However, existing incident reporting processes are not sufficient for understanding agent incidents. In particular, such processes are largely based on publicly available data, which excludes useful, but potentially sensitive, information such as an agent's chain of thought or browser history. To inform the development of new, emerging incident reporting processes, we propose an incident analysis framework for agents. Drawing on systems safety approaches, our framework proposes three types of factors that can cause incidents: system-related (e.g., CBRN training data), contextual (e.g., prompt injections), and cognitive (e.g., misunderstanding a user request). We also identify specific information that could help clarify which factors are relevant to a given incident: activity logs, system documentation and access, and information about the tools an agent uses. We provide recommendations for 1) what information incident reports should include and 2) what information developers and deployers should retain and make available to incident investigators upon request. As we transition to a world with more agents, understanding agent incidents will become increasingly crucial for managing risks.

