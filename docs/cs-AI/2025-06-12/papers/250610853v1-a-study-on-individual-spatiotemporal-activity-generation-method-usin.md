---
layout: default
title: A Study on Individual Spatiotemporal Activity Generation Method Using MCP-Enhanced Chain-of-Thought Large Language Models
---

# A Study on Individual Spatiotemporal Activity Generation Method Using MCP-Enhanced Chain-of-Thought Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10853" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10853v1</a>
  <a href="https://arxiv.org/pdf/2506.10853.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10853v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10853v1', 'A Study on Individual Spatiotemporal Activity Generation Method Using MCP-Enhanced Chain-of-Thought Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Zhang, Yang Hu, De Wang

**分类**: cs.AI, cs.CY

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出MCP增强的链式思维模型以解决城市行为模拟问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `城市行为模拟` `链式思维` `模型上下文协议` `时空推理` `智能城市` `数据生成` `交通预测` `环境感知`

## 📋 核心要点

1. 现有的基于规则和统计的方法在城市行为模拟中面临高计算成本和有限的可推广性等挑战。
2. 本文提出了一种结合链式思维推理与模型上下文协议的框架，以增强LLMs在时空行为模拟中的能力。
3. 实验结果显示，生成样本与真实数据高度相似，且生成效率显著提高，处理时间从1.30分钟降至0.17分钟。

## 📝 摘要（中文）

人类时空行为模拟对城市规划研究至关重要，但传统的基于规则和统计的方法在计算成本、可推广性和可扩展性方面存在不足。虽然大型语言模型（LLMs）作为“世界模拟器”展现出潜力，但在时空推理方面面临空间认知有限、缺乏物理约束理解和群体同质化倾向等挑战。本文提出了一种将链式思维（CoT）推理与模型上下文协议（MCP）相结合的框架，以增强LLMs在模拟与验证数据模式相符的时空行为的能力。该方法通过五阶段的认知框架实现人类般的渐进推理，并结合六类专门的MCP工具进行全面数据处理。实验结果表明，该框架在上海陆家嘴地区生成的1000个样本与真实移动信号数据高度相似，生成质量评分在7.86到8.36之间，且并行处理实验显示效率显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决传统城市行为模拟方法在计算成本、可扩展性和可推广性方面的不足，尤其是在时空推理能力上的局限性。

**核心思路**：通过将链式思维推理与模型上下文协议相结合，设计出一种新的框架，以提升LLMs在模拟人类时空行为时的准确性和效率。

**技术框架**：该框架包括五个认知阶段，结合六类MCP工具，分别为时间管理、空间导航、环境感知、个人记忆、社会协作和经验评估，形成一个全面的数据处理流程。

**关键创新**：本研究的创新在于将CoT推理与MCP结合，突破了LLMs在时空推理中的局限，提供了一种新的思路来处理复杂的城市行为模拟问题。

**关键设计**：在设计中，采用了多阶段的认知推理过程，并通过六类MCP工具进行数据处理，确保生成的时空行为与真实数据相符。

## 📊 实验亮点

实验结果显示，生成的1000个样本与真实移动信号数据的相似度高，生成质量评分在7.86到8.36之间。此外，通过并行处理，生成效率显著提升，处理时间从1.30分钟降至0.17分钟，表明该方法在实际应用中的可行性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能城市规划、交通预测和参与式城市设计等。通过提供更准确的时空行为模拟，该框架能够为城市管理者和规划者提供有价值的决策支持，推动城市可持续发展。

## 📄 摘要（原文）

> Human spatiotemporal behavior simulation is critical for urban planning research, yet traditional rule-based and statistical approaches suffer from high computational costs, limited generalizability, and poor scalability. While large language models (LLMs) show promise as "world simulators," they face challenges in spatiotemporal reasoning including limited spatial cognition, lack of physical constraint understanding, and group homogenization tendencies. This paper introduces a framework integrating chain-of-thought (CoT) reasoning with Model Context Protocol (MCP) to enhance LLMs' capability in simulating spatiotemporal behaviors that correspond with validation data patterns. The methodology combines human-like progressive reasoning through a five-stage cognitive framework with comprehensive data processing via six specialized MCP tool categories: temporal management, spatial navigation, environmental perception, personal memory, social collaboration, and experience evaluation. Experiments in Shanghai's Lujiazui district validate the framework's effectiveness across 1,000 generated samples. Results demonstrate high similarity with real mobile signaling data, achieving generation quality scores of 7.86 to 8.36 across different base models. Parallel processing experiments show efficiency improvements, with generation times decreasing from 1.30 to 0.17 minutes per sample when scaling from 2 to 12 processes. This work contributes to integrating CoT reasoning with MCP for urban behavior modeling, advancing LLMs applications in urban computing and providing a practical approach for synthetic mobility data generation. The framework offers a foundation for smart city planning, transportation forecasting, and participatory urban design applications.

