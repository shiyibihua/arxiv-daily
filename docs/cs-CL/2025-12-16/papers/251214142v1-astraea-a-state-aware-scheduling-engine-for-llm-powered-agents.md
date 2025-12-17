---
layout: default
title: Astraea: A State-Aware Scheduling Engine for LLM-Powered Agents
---

# Astraea: A State-Aware Scheduling Engine for LLM-Powered Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14142" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14142v1</a>
  <a href="https://arxiv.org/pdf/2512.14142.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14142v1" onclick="toggleFavorite(this, '2512.14142v1', 'Astraea: A State-Aware Scheduling Engine for LLM-Powered Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongqiu Ni, Jiabao Zhang, Guopeng Li, Zilong Wang, Ruiqi Wu, Chi Zhang, Haisheng Tan

**分类**: cs.CL

**发布日期**: 2025-12-16

**备注**: 12 pages, 8 figures

---

## 💡 一句话要点

**Astraea：面向LLM智能体的状态感知调度引擎，优化端到端延迟**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM智能体` `状态感知调度` `端到端延迟优化` `分层调度` `KV缓存管理`

## 📋 核心要点

1. 现有LLM推理系统在处理智能代理的多阶段工作流时，无法有效优化端到端延迟，导致全局作业完成时间较长。
2. Astraea通过状态感知的分层调度算法，结合请求历史状态和未来预测，动态分类请求并优化资源分配，从而降低端到端延迟。
3. 实验结果表明，Astraea相比基线方法，平均作业完成时间降低高达25.5%，并在高负载下表现出良好的鲁棒性和稳定性。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地被部署为智能代理。它们的多阶段工作流程在本地计算和调用Web API等外部网络服务之间交替，这导致它们的执行模式与现有推理系统（如vLLM）的调度粒度不匹配。现有系统通常侧重于每个片段的优化，这妨碍了它们最小化完整代理工作流程的端到端延迟，即整个请求生命周期的全局作业完成时间（JCT）。为了解决这个限制，我们提出了Astraea，一种旨在将优化从本地片段转移到全局请求生命周期的服务引擎。Astraea采用了一种状态感知的分层调度算法，该算法将请求的历史状态与未来预测相结合。它根据请求的I/O和计算密集型性质动态地对请求进行分类，并使用增强的HRRN策略来平衡效率和公平性。Astraea还实现了一个自适应KV缓存管理器，该管理器根据系统内存压力智能地处理I/O等待期间的代理状态。大量实验表明，与基线方法相比，Astraea将平均JCT降低了高达25.5%。此外，我们的方法在各种模型规模的高负载下表现出强大的鲁棒性和稳定性。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM驱动的智能代理在多阶段工作流执行过程中，现有推理系统无法有效优化端到端延迟的问题。现有系统通常关注单个计算片段的优化，忽略了全局作业完成时间（JCT），导致整体效率低下。现有方法的痛点在于无法根据请求的状态和未来的资源需求进行动态调度。

**核心思路**：Astraea的核心思路是将优化目标从局部片段转移到全局请求生命周期。通过状态感知的调度算法，系统能够了解请求的历史执行情况和未来的资源需求，从而做出更合理的调度决策，最小化全局JCT。这种设计能够更好地适应智能代理工作流中计算和I/O交替的特点。

**技术框架**：Astraea采用分层调度架构，包含以下主要模块：1) 请求分类器：根据请求的I/O和计算密集程度进行动态分类。2) 状态感知调度器：基于请求的历史状态和未来预测，使用增强的HRRN（Highest Response Ratio Next）策略进行调度，平衡效率和公平性。3) 自适应KV缓存管理器：根据系统内存压力，智能地管理I/O等待期间的代理状态。

**关键创新**：Astraea的关键创新在于其状态感知的调度算法和自适应KV缓存管理。状态感知调度能够根据请求的动态变化调整资源分配，而自适应KV缓存管理则能够有效利用系统内存，减少I/O等待时间。与现有方法相比，Astraea能够更好地适应智能代理工作流的特点，实现全局优化。

**关键设计**：Astraea的关键设计包括：1) 请求分类器的分类标准，例如I/O密集型和计算密集型的区分阈值。2) 增强的HRRN策略的具体实现，例如如何根据历史状态和未来预测调整优先级。3) 自适应KV缓存管理器的缓存替换策略，例如LRU（Least Recently Used）或LFU（Least Frequently Used）的变体，以及如何根据内存压力动态调整缓存大小。

## 📊 实验亮点

实验结果表明，Astraea相比于基线方法，平均作业完成时间（JCT）降低了高达25.5%。此外，Astraea在高负载情况下表现出强大的鲁棒性和稳定性，能够有效应对各种模型规模的需求。这些结果验证了Astraea在优化LLM驱动的智能代理性能方面的有效性。

## 🎯 应用场景

Astraea适用于各种需要LLM驱动的智能代理的场景，例如智能客服、自动化流程管理、智能家居控制等。通过优化端到端延迟，Astraea可以提高用户体验，降低运营成本，并促进智能代理在实际应用中的广泛部署。未来，Astraea可以进一步扩展到支持更复杂的代理工作流和异构计算环境。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly being deployed as intelligent agents. Their multi-stage workflows, which alternate between local computation and calls to external network services like Web APIs, introduce a mismatch in their execution pattern and the scheduling granularity of existing inference systems such as vLLM. Existing systems typically focus on per-segment optimization which prevents them from minimizing the end-to-end latency of the complete agentic workflow, i.e., the global Job Completion Time (JCT) over the entire request lifecycle. To address this limitation, we propose Astraea, a service engine designed to shift the optimization from local segments to the global request lifecycle. Astraea employs a state-aware, hierarchical scheduling algorithm that integrates a request's historical state with future predictions. It dynamically classifies requests by their I/O and compute intensive nature and uses an enhanced HRRN policy to balance efficiency and fairness. Astraea also implements an adaptive KV cache manager that intelligently handles the agent state during I/O waits based on the system memory pressure. Extensive experiments show that Astraea reduces average JCT by up to 25.5\% compared to baseline methods. Moreover, our approach demonstrates strong robustness and stability under high load across various model scales.

