---
layout: default
title: IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol
---

# IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14166" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14166v1</a>
  <a href="https://arxiv.org/pdf/2512.14166.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14166v1" onclick="toggleFavorite(this, '2512.14166v1', 'IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunhao Yao, Zhiqiang Wang, Haoran Cheng, Yihang Cheng, Haohua Du, Xiang-Yang Li

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-16

**备注**: 12 pages, 6 figures

---

## 💡 一句话要点

**提出IntentMiner，通过分析工具调用在模型上下文协议中实现意图反演攻击。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `意图反演` `模型上下文协议` `隐私攻击` `大型语言模型` `工具调用分析`

## 📋 核心要点

1. 现有基于MCP的LLM Agent架构存在隐私泄露风险，第三方服务器可能通过工具调用日志推断用户意图。
2. 提出IntentMiner框架，通过分层信息隔离和三维语义分析，从工具调用中准确推断用户意图。
3. 实验表明IntentMiner能够高精度还原用户意图，语义对齐度超过85%，验证了该隐私漏洞的存在。

## 📝 摘要（中文）

大型语言模型（LLMs）快速发展为自主代理，模型上下文协议（MCP）已成为发现和调用外部工具的标准。虽然这种架构将推理引擎与工具执行分离，以提高可扩展性，但也引入了一个重要的隐私风险：第三方MCP服务器作为半诚实的中介，可以观察到用户信任边界之外的详细工具交互日志。本文首次识别并形式化了一种新的隐私威胁，称为意图反演，即半诚实的MCP服务器仅通过分析合法的工具调用来尝试重构用户的私有底层意图。为了系统地评估这种漏洞，我们提出了IntentMiner，一个利用分层信息隔离和三维语义分析的框架，整合工具目的、调用语句和返回结果，以在步骤级别准确推断用户意图。大量实验表明，IntentMiner与原始用户查询实现了高度的语义对齐（超过85%），显著优于基线方法。这些结果突出了解耦代理架构中固有的隐私风险，揭示了看似良性的工具执行日志可以作为暴露用户秘密的有效途径。

## 🔬 方法详解

**问题定义**：论文旨在解决在模型上下文协议（MCP）中，半诚实的第三方MCP服务器如何仅通过分析用户发起的合法工具调用，来推断用户的私有底层意图的问题。现有方法缺乏对这种隐私泄露风险的系统性分析和有效防御手段。

**核心思路**：论文的核心思路是利用工具调用日志中蕴含的丰富信息，包括工具的目的、调用语句和返回结果，通过语义分析来重构用户的意图。这种思路基于一个假设：即使工具调用本身是合法的，其组合和上下文信息也可能泄露用户的敏感信息。

**技术框架**：IntentMiner框架主要包含以下几个阶段：1) **数据收集**：收集用户与LLM Agent交互产生的工具调用日志，包括工具名称、调用参数和返回结果。2) **分层信息隔离**：对收集到的数据进行分层处理，隔离不同层级的信息，例如将工具名称、参数和结果分别处理。3) **三维语义分析**：从工具目的、调用语句和返回结果三个维度对数据进行语义分析，提取关键信息。4) **意图推断**：利用提取的信息，通过机器学习模型或规则引擎来推断用户的意图。

**关键创新**：论文的关键创新在于提出了意图反演攻击的概念，并设计了IntentMiner框架来系统性地评估这种攻击的有效性。与现有方法相比，IntentMiner更加关注工具调用日志中蕴含的语义信息，并利用分层信息隔离和三维语义分析来提高意图推断的准确性。

**关键设计**：IntentMiner的关键设计包括：1) **分层信息隔离策略**：如何有效地隔离不同层级的信息，避免信息泄露。2) **三维语义分析方法**：如何从工具目的、调用语句和返回结果三个维度提取关键信息，例如使用自然语言处理技术进行语义分析。3) **意图推断模型**：选择合适的机器学习模型或规则引擎来进行意图推断，例如使用基于Transformer的模型或基于知识图谱的推理引擎。

## 📊 实验亮点

实验结果表明，IntentMiner能够以超过85%的语义对齐度还原用户的原始查询意图，显著优于基线方法。这表明即使在看似安全的MCP架构下，用户的隐私仍然面临严重的威胁。实验还分析了不同因素对意图反演攻击的影响，例如工具调用的数量和质量，为防御策略的设计提供了指导。

## 🎯 应用场景

该研究成果可应用于评估和增强基于LLM Agent的系统的隐私安全性。通过IntentMiner，开发者可以识别潜在的意图泄露风险，并采取相应的防御措施，例如对工具调用日志进行脱敏处理、限制第三方服务器的访问权限等。此外，该研究还可以促进对新型隐私攻击的关注，推动隐私保护技术的发展。

## 📄 摘要（原文）

> The rapid evolution of Large Language Models (LLMs) into autonomous agents has led to the adoption of the Model Context Protocol (MCP) as a standard for discovering and invoking external tools. While this architecture decouples the reasoning engine from tool execution to enhance scalability, it introduces a significant privacy surface: third-party MCP servers, acting as semi-honest intermediaries, can observe detailed tool interaction logs outside the user's trusted boundary. In this paper, we first identify and formalize a novel privacy threat termed Intent Inversion, where a semi-honest MCP server attempts to reconstruct the user's private underlying intent solely by analyzing legitimate tool calls. To systematically assess this vulnerability, we propose IntentMiner, a framework that leverages Hierarchical Information Isolation and Three-Dimensional Semantic Analysis, integrating tool purpose, call statements, and returned results, to accurately infer user intent at the step level. Extensive experiments demonstrate that IntentMiner achieves a high degree of semantic alignment (over 85%) with original user queries, significantly outperforming baseline approaches. These results highlight the inherent privacy risks in decoupled agent architectures, revealing that seemingly benign tool execution logs can serve as a potent vector for exposing user secrets.

