---
layout: default
title: Integrating LLMs and Digital Twins for Adaptive Multi-Robot Task Allocation in Construction
---

# Integrating LLMs and Digital Twins for Adaptive Multi-Robot Task Allocation in Construction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18178" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18178v1</a>
  <a href="https://arxiv.org/pdf/2506.18178.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18178v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18178v1', 'Integrating LLMs and Digital Twins for Adaptive Multi-Robot Task Allocation in Construction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Min Deng, Bo Fu, Lingyao Li, Xi Wang

**分类**: cs.RO

**发布日期**: 2025-06-22

---

## 💡 一句话要点

**提出自适应任务分配框架以解决建筑工地多机器人协调问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多机器人系统` `任务分配` `数字双胞胎` `大型语言模型` `自适应调度` `建筑工地` `整数规划` `动态环境`

## 📋 核心要点

1. 现有多机器人系统在动态建筑环境中协调时面临诸多不确定因素，如材料延误和天气变化，导致任务分配效率低下。
2. 本文提出了一种结合数字双胞胎和大型语言模型的自适应任务分配框架，能够实时更新任务分配和调度策略。
3. 实验结果显示，优化算法的计算效率和大型语言模型的推理性能显著提升，部分模型在约束提取中的准确率超过97%。

## 📝 摘要（中文）

多机器人系统在工业领域日益受到关注，但在动态和不确定的环境中有效协调多个机器人仍然面临挑战，尤其是在建筑工地上。为此，本文提出了一种自适应任务分配框架，结合数字双胞胎、整数规划和大型语言模型的优势，解决任务依赖性、机器人异质性、调度约束和重新规划需求等问题。通过引入叙事驱动的调度适应机制，利用大型语言模型解析自然语言输入并自动更新优化约束，实现了人机协作的灵活性。此外，开发的数字双胞胎系统实现了物理操作与数字表示之间的实时同步，确保系统动态响应现场变化。案例研究表明，优化算法的计算效率和大型语言模型的推理性能显著提升，部分模型在约束和参数提取中的准确率超过97%。

## 🔬 方法详解

**问题定义**：本文旨在解决建筑工地多机器人系统在动态环境中任务分配的挑战，现有方法难以应对不确定性和复杂性，导致效率低下。

**核心思路**：通过结合数字双胞胎、整数规划和大型语言模型，提出一种自适应任务分配框架，能够实时响应现场变化并优化任务调度。

**技术框架**：整体架构包括任务依赖性建模、机器人异质性处理、调度约束管理和基于自然语言的调度适应机制，形成闭环反馈系统。

**关键创新**：引入叙事驱动的调度适应机制，利用大型语言模型解析自然语言输入并自动更新优化约束，实现人机协作的灵活性，这是与现有方法的本质区别。

**关键设计**：在整数规划模型中考虑了任务依赖性和调度约束，设计了适应性强的参数设置，确保系统能够在变化的环境中保持高效运行。

## 📊 实验亮点

实验结果表明，优化算法的计算效率显著提升，部分大型语言模型在约束和参数提取中的准确率超过97%，显示出该框架在实际应用中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括建筑、制造和物流等多个工业场景，能够显著提升多机器人系统在动态环境中的任务分配效率和灵活性，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> Multi-robot systems are emerging as a promising solution to the growing demand for productivity, safety, and adaptability across industrial sectors. However, effectively coordinating multiple robots in dynamic and uncertain environments, such as construction sites, remains a challenge, particularly due to unpredictable factors like material delays, unexpected site conditions, and weather-induced disruptions. To address these challenges, this study proposes an adaptive task allocation framework that strategically leverages the synergistic potential of Digital Twins, Integer Programming (IP), and Large Language Models (LLMs). The multi-robot task allocation problem is formally defined and solved using an IP model that accounts for task dependencies, robot heterogeneity, scheduling constraints, and re-planning requirements. A mechanism for narrative-driven schedule adaptation is introduced, in which unstructured natural language inputs are interpreted by an LLM, and optimization constraints are autonomously updated, enabling human-in-the-loop flexibility without manual coding. A digital twin-based system has been developed to enable real-time synchronization between physical operations and their digital representations. This closed-loop feedback framework ensures that the system remains dynamic and responsive to ongoing changes on site. A case study demonstrates both the computational efficiency of the optimization algorithm and the reasoning performance of several LLMs, with top-performing models achieving over 97% accuracy in constraint and parameter extraction. The results confirm the practicality, adaptability, and cross-domain applicability of the proposed methods.

