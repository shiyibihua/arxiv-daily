---
layout: default
title: Analyzing Information Sharing and Coordination in Multi-Agent Planning
---

# Analyzing Information Sharing and Coordination in Multi-Agent Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12981" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12981v1</a>
  <a href="https://arxiv.org/pdf/2508.12981.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12981v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12981v1', 'Analyzing Information Sharing and Coordination in Multi-Agent Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyue Ou, Saujas Vaduguru, Daniel Fried

**分类**: cs.CL

**发布日期**: 2025-08-18

---

## 💡 一句话要点

**构建LLM基础的MAS以解决复杂旅行规划问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `大型语言模型` `信息共享` `协调机制` `旅行规划`

## 📋 核心要点

1. 现有的多智能体系统在处理长时间跨度和多约束的规划任务时，面临信息共享和协调不足的问题。
2. 论文提出了一种基于大型语言模型的多智能体系统，通过引入信息共享笔记本和协调代理来改善信息交流和任务协调。
3. 实验结果显示，结合信息共享和协调机制，最终通过率达到25%，相较于单代理基线提升了17.5%。

## 📝 摘要（中文）

多智能体系统（MAS）在网络研究和软件工程等领域推动了大型语言模型（LLM）代理的边界。然而，长时间跨度的多约束规划任务需要详细信息的条件化和复杂的相互依赖约束的满足，这对这些系统构成了挑战。本研究构建了一个基于LLM的MAS用于旅行规划任务，并评估了信息共享笔记本的影响以及协调代理在自由形式对话中的作用。研究发现，笔记本将由于虚构细节导致的错误减少了18%，而协调者引导MAS专注于特定子领域，进一步减少了高达13.5%的错误。结合这两种机制，最终在TravelPlanner基准测试中实现了25%的通过率，相较于单代理基线的7.5%提升了17.5%。这些结果突显了结构化信息共享和反思性协调在LLM的长时间规划中的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决多智能体系统在长时间跨度和多约束规划任务中信息共享和协调不足的问题。现有方法在处理复杂的相互依赖约束时常常出现错误，导致任务失败。

**核心思路**：论文的核心解决思路是构建一个基于大型语言模型的多智能体系统，利用信息共享笔记本和协调代理来增强信息的传递和任务的协调性。通过这种设计，系统能够更好地处理复杂的规划任务。

**技术框架**：整体架构包括两个主要模块：信息共享笔记本和协调代理。信息共享笔记本用于记录和共享重要信息，而协调代理则负责引导智能体之间的对话，确保信息的有效传递和任务的集中处理。

**关键创新**：最重要的技术创新点在于引入了信息共享笔记本和协调代理的组合机制，这一设计显著提高了多智能体系统在复杂任务中的表现，与传统单一代理方法相比，能够更有效地减少错误和提高任务成功率。

**关键设计**：在设计中，信息共享笔记本的使用减少了虚构细节导致的错误，而协调代理通过引导智能体关注特定子领域，进一步优化了信息处理过程。具体的参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，信息共享笔记本将错误减少了18%，而协调代理进一步减少了13.5%的错误。结合这两种机制，最终通过率达到了25%，相较于单代理基线的7.5%提升了17.5%，展现了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括旅游规划、项目管理和复杂系统的协调任务。通过改进信息共享和协调机制，可以在多个领域提升决策效率和任务成功率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Multi-agent systems (MASs) have pushed the boundaries of large language model (LLM) agents in domains such as web research and software engineering. However, long-horizon, multi-constraint planning tasks involve conditioning on detailed information and satisfying complex interdependent constraints, which can pose a challenge for these systems. In this study, we construct an LLM-based MAS for a travel planning task which is representative of these challenges. We evaluate the impact of a notebook to facilitate information sharing, and evaluate an orchestrator agent to improve coordination in free form conversation between agents. We find that the notebook reduces errors due to hallucinated details by 18%, while an orchestrator directs the MAS to focus on and further reduce errors by up to 13.5% within focused sub-areas. Combining both mechanisms achieves a 25% final pass rate on the TravelPlanner benchmark, a 17.5% absolute improvement over the single-agent baseline's 7.5% pass rate. These results highlight the potential of structured information sharing and reflective orchestration as key components in MASs for long horizon planning with LLMs.

