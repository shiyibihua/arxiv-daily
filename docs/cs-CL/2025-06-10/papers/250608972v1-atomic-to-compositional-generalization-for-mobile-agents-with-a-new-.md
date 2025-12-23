---
layout: default
title: Atomic-to-Compositional Generalization for Mobile Agents with A New Benchmark and Scheduling System
---

# Atomic-to-Compositional Generalization for Mobile Agents with A New Benchmark and Scheduling System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08972" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08972v1</a>
  <a href="https://arxiv.org/pdf/2506.08972.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08972v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08972v1', 'Atomic-to-Compositional Generalization for Mobile Agents with A New Benchmark and Scheduling System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuan Guo, Tingjia Miao, Zheng Wu, Pengzhou Cheng, Ming Zhou, Zhuosheng Zhang

**分类**: cs.CL

**发布日期**: 2025-06-10

---

## 💡 一句话要点

**提出UI-NEXUS基准与AGENT-NEXUS调度系统以解决移动代理的组合任务泛化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `移动代理` `组合任务` `任务调度` `多模态学习` `基准测试` `智能助手` `性能优化`

## 📋 核心要点

1. 现有方法主要关注原子任务，缺乏对组合任务的泛化能力，导致在实际应用中表现不佳。
2. 论文提出UI-NEXUS基准和AGENT-NEXUS调度系统，通过动态分解任务来提升移动代理的组合任务处理能力。
3. 实验结果显示，AGENT-NEXUS在UI-NEXUS基准上提高了24%至40%的任务成功率，且推理开销未显著增加。

## 📝 摘要（中文）

自主代理通过多模态大语言模型得以发展，以便在移动设备上执行任务。然而，现有研究主要集中在原子任务上，忽视了组合任务的泛化能力，这对于实际应用至关重要。本研究引入了UI-NEXUS，一个全面的基准，旨在评估移动代理在简单连接、上下文转换和深度挖掘三类组合操作上的表现。UI-NEXUS支持在20个完全可控的本地应用环境和30个在线服务应用中进行交互评估。实验结果表明，现有代理在组合任务中面临显著挑战。为此，提出AGENT-NEXUS，一个轻量高效的调度系统，通过动态分解长时间任务为一系列自包含的原子子任务，显著提高了任务成功率。

## 🔬 方法详解

**问题定义**：本论文旨在解决移动代理在组合任务中的泛化能力不足的问题。现有方法在处理复杂任务时，常常出现执行不足、执行过度和注意力漂移等失败模式，导致原子任务与组合任务之间的泛化差距。

**核心思路**：论文提出AGENT-NEXUS调度系统，通过动态分解长时间任务为多个自包含的原子子任务，从而提升现有移动代理在组合任务上的表现。这样的设计能够有效地利用现有代理的能力，减少任务执行中的复杂性。

**技术框架**：AGENT-NEXUS的整体架构包括任务分解模块、执行调度模块和反馈优化模块。任务分解模块负责将长时间任务拆分为原子子任务，执行调度模块则根据当前环境和任务需求动态安排子任务的执行顺序，反馈优化模块则用于根据执行结果调整后续任务的策略。

**关键创新**：AGENT-NEXUS的核心创新在于其动态任务分解能力，能够根据任务的复杂性和环境变化灵活调整子任务的执行策略。这一方法与传统的静态任务执行方式有本质区别，显著提升了组合任务的处理效率。

**关键设计**：在设计上，AGENT-NEXUS采用了轻量级的调度算法，确保在不显著增加推理开销的情况下提升任务成功率。同时，损失函数的设计考虑了任务执行的效率与准确性之间的平衡，确保代理在执行过程中能够快速适应变化的任务需求。

## 📊 实验亮点

实验结果表明，AGENT-NEXUS在UI-NEXUS基准上显著提高了现有移动代理在组合操作任务上的成功率，提升幅度在24%至40%之间，且在推理开销方面未显著增加，展示了其高效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能手机助手、自动化客服和智能家居系统等。通过提升移动代理在组合任务上的处理能力，能够显著改善用户体验，增强系统的智能化水平。未来，该技术有望在更多复杂场景中得到应用，推动移动智能代理的发展。

## 📄 摘要（原文）

> Autonomous agents powered by multimodal large language models have been developed to facilitate task execution on mobile devices. However, prior work has predominantly focused on atomic tasks -- such as shot-chain execution tasks and single-screen grounding tasks -- while overlooking the generalization to compositional tasks, which are indispensable for real-world applications. This work introduces UI-NEXUS, a comprehensive benchmark designed to evaluate mobile agents on three categories of compositional operations: Simple Concatenation, Context Transition, and Deep Dive. UI-NEXUS supports interactive evaluation in 20 fully controllable local utility app environments, as well as 30 online Chinese and English service apps. It comprises 100 interactive task templates with an average optimal step count of 14.05. Experimental results across a range of mobile agents with agentic workflow or agent-as-a-model show that UI-NEXUS presents significant challenges. Specifically, existing agents generally struggle to balance performance and efficiency, exhibiting representative failure modes such as under-execution, over-execution, and attention drift, causing visible atomic-to-compositional generalization gap. Inspired by these findings, we propose AGENT-NEXUS, a lightweight and efficient scheduling system to tackle compositional mobile tasks. AGENT-NEXUS extrapolates the abilities of existing mobile agents by dynamically decomposing long-horizon tasks to a series of self-contained atomic subtasks. AGENT-NEXUS achieves 24% to 40% task success rate improvement for existing mobile agents on compositional operation tasks within the UI-NEXUS benchmark without significantly sacrificing inference overhead. The demo video, dataset, and code are available on the project page at https://ui-nexus.github.io.

