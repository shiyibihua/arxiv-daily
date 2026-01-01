---
layout: default
title: "SynRAG: A Large Language Model Framework for Executable Query Generation in Heterogeneous SIEM System"
---

# SynRAG: A Large Language Model Framework for Executable Query Generation in Heterogeneous SIEM System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24571" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24571v1</a>
  <a href="https://arxiv.org/pdf/2512.24571.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24571v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24571v1', 'SynRAG: A Large Language Model Framework for Executable Query Generation in Heterogeneous SIEM System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md Hasan Saju, Austin Page, Akramul Azim, Jeff Gardiner, Farzaneh Abazari, Frank Eargle

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-31

**期刊**: https://conf.researchr.org/home/cascon-2025

---

## 💡 一句话要点

**SynRAG：用于异构SIEM系统中可执行查询生成的大语言模型框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `安全信息和事件管理` `SIEM` `大型语言模型` `查询生成` `威胁检测` `事件调查` `异构系统`

## 📋 核心要点

1. 现有SIEM系统多样性导致安全分析师需要针对不同平台进行专门培训，增加了工作负担和企业成本。
2. SynRAG框架通过平台无关的规范，自动生成适用于多种SIEM系统的威胁检测和事件调查查询，简化了跨平台操作。
3. 实验结果表明，SynRAG在跨SIEM威胁检测和事件调查方面，显著优于GPT、Llama等先进语言模型。

## 📝 摘要（中文）

安全信息和事件管理（SIEM）系统对于大型企业监控其IT基础设施至关重要，它们每天摄取和分析数百万的日志和事件。安全运营中心（SOC）分析师负责监控和分析这些海量数据，以识别潜在威胁并采取预防措施来保护企业资产。然而，Palo Alto Networks Qradar、Google SecOps、Splunk、Microsoft Sentinel和Elastic Stack等SIEM平台之间的多样性带来了重大挑战。由于这些系统在属性、架构和查询语言上存在差异，使得分析师难以有效地监控多个平台，除非经过广泛的培训或企业被迫扩大员工队伍。为了解决这个问题，我们引入了SynRAG，一个统一的框架，可以从平台无关的规范中自动生成针对多个SIEM平台的威胁检测或事件调查查询。SynRAG可以从分析师编写的单个高级规范生成特定于平台的查询。如果没有SynRAG，分析师将需要为每个SIEM平台手动编写单独的查询，因为查询语言在不同系统之间差异很大。该框架实现了跨异构SIEM环境的无缝威胁检测和事件调查，减少了对专门培训和手动查询转换的需求。我们使用Qradar和SecOps作为代表性的SIEM系统，针对包括GPT、Llama、DeepSeek、Gemma和Claude在内的最先进的语言模型评估了SynRAG。我们的结果表明，与最先进的基础模型相比，SynRAG为跨SIEM威胁检测和事件调查生成了明显更好的查询。

## 🔬 方法详解

**问题定义**：现有安全信息和事件管理（SIEM）系统种类繁多，例如Qradar、SecOps、Splunk等，它们使用不同的查询语言和数据结构。安全分析师需要针对每个平台编写不同的查询，这既耗时又需要专业的平台知识。现有方法缺乏一个统一的查询生成框架，导致效率低下和学习成本高昂。

**核心思路**：SynRAG的核心思路是利用大型语言模型（LLM）的自然语言理解和生成能力，将平台无关的高级查询规范转换为特定于SIEM平台的查询语言。通过这种方式，分析师只需要编写一次查询，SynRAG就能自动生成适用于不同平台的版本。

**技术框架**：SynRAG框架包含以下主要模块：1) 接收分析师编写的平台无关查询规范；2) 利用LLM将该规范转换为特定SIEM平台的查询语言；3) 输出可执行的查询语句。该框架的关键在于LLM的训练和微调，使其能够理解安全领域的概念，并准确地生成符合SIEM平台语法的查询。

**关键创新**：SynRAG的关键创新在于它提供了一个统一的、基于LLM的查询生成框架，能够自动处理不同SIEM平台之间的差异。与传统的手动查询编写或基于规则的转换方法相比，SynRAG具有更高的灵活性和可扩展性，能够适应新的SIEM平台和查询需求。

**关键设计**：SynRAG的关键设计包括：1) 使用高质量的安全领域数据对LLM进行预训练，使其具备安全知识；2) 使用特定SIEM平台的查询示例对LLM进行微调，提高其查询生成准确性；3) 设计有效的提示工程（Prompt Engineering）策略，引导LLM生成符合要求的查询语句。具体的参数设置和损失函数选择取决于所使用的LLM架构和训练数据。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24571v1/MyRAGL.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24571v1/Result-ComparisonAll.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SynRAG在Qradar和SecOps两个代表性SIEM系统上的实验结果表明，其生成的查询质量显著优于GPT、Llama、DeepSeek、Gemma和Claude等先进语言模型。具体性能提升数据未知，但论文强调了SynRAG在跨SIEM威胁检测和事件调查方面的优越性。

## 🎯 应用场景

SynRAG可应用于各种需要跨多个异构SIEM系统进行威胁检测和事件调查的场景。它可以帮助安全运营中心（SOC）提高效率，降低培训成本，并更快地响应安全事件。此外，该框架还可以用于自动化安全审计和合规性检查，提升整体安全态势。

## 📄 摘要（原文）

> Security Information and Event Management (SIEM) systems are essential for large enterprises to monitor their IT infrastructure by ingesting and analyzing millions of logs and events daily. Security Operations Center (SOC) analysts are tasked with monitoring and analyzing this vast data to identify potential threats and take preventive actions to protect enterprise assets. However, the diversity among SIEM platforms, such as Palo Alto Networks Qradar, Google SecOps, Splunk, Microsoft Sentinel and the Elastic Stack, poses significant challenges. As these systems differ in attributes, architecture, and query languages, making it difficult for analysts to effectively monitor multiple platforms without undergoing extensive training or forcing enterprises to expand their workforce. To address this issue, we introduce SynRAG, a unified framework that automatically generates threat detection or incident investigation queries for multiple SIEM platforms from a platform-agnostic specification. SynRAG can generate platformspecific queries from a single high-level specification written by analysts. Without SynRAG, analysts would need to manually write separate queries for each SIEM platform, since query languages vary significantly across systems. This framework enables seamless threat detection and incident investigation across heterogeneous SIEM environments, reducing the need for specialized training and manual query translation. We evaluate SynRAG against state-of-the-art language models, including GPT, Llama, DeepSeek, Gemma, and Claude, using Qradar and SecOps as representative SIEM systems. Our results demonstrate that SynRAG generates significantly better queries for crossSIEM threat detection and incident investigation compared to the state-of-the-art base models.

