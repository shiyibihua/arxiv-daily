---
layout: default
title: Toward an Unbiased Collective Memory for Efficient LLM-Based Agentic 6G Cross-Domain Management
---

# Toward an Unbiased Collective Memory for Efficient LLM-Based Agentic 6G Cross-Domain Management

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26200" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26200v1</a>
  <a href="https://arxiv.org/pdf/2509.26200.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26200v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26200v1', 'Toward an Unbiased Collective Memory for Efficient LLM-Based Agentic 6G Cross-Domain Management')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hatim Chergui, Miguel Catalan Cid, Pouria Sayyad Khodashenas, Daniel Camps Mur, Christos Verikoukis

**分类**: cs.NI, cs.AI

**发布日期**: 2025-09-30

**备注**: 12 pages, 8 figures

**🔗 代码/项目**: [GITHUB](https://github.com/HatimChergui/unbiased-collective-memory)

---

## 💡 一句话要点

**提出一种无偏集体记忆框架，用于高效的基于LLM的Agent 6G跨域管理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `6G网络管理` `LLM Agent` `跨域资源编排` `认知偏差` `无偏集体记忆`

## 📋 核心要点

1. 现有基于LLM的Agent在6G跨域资源管理中存在认知偏差，影响决策质量和效率。
2. 提出无偏集体记忆框架，通过语义检索、失败学习、多样性增强和时间加权缓解认知偏差。
3. 实验表明，该框架显著减少未解决协商，完全消除SLA违规，并改善延迟和节能。

## 📝 摘要（中文）

本文提出了一种新颖的框架，用于6G RAN-Edge网络中基于大语言模型（LLM）增强Agent的主动跨域资源编排。该系统包含专门的RAN（能源效率）和Edge（延迟保证）Agent，它们进行迭代协商，并由高级推理和规划能力提供支持。Agent与数字孪生（DT）动态交互以测试其提案，并利用长期集体记忆，其中他们联合成功和失败的协议以及相关的网络上下文被提炼成策略，以遵循或避免，并随后存储。考虑到Agent在检索这些过去的经验时会受到大量的认知偏差的影响——例如首因效应、近因效应、确认偏差和可得性偏差——我们在本文中提出了一种新颖的无偏记忆设计，其特点是：（i）通过Jaccard相似性进行过去策略的语义检索；（ii）通过放大SLA违规的权重和强制包含失败的协商案例来减轻确认偏差，从而从失败中学习；（iii）强制多样性以最小化可得性偏差；以及（iv）具有缓慢衰减的近因和首因加权以抵消时间偏差。评估结果展示了现有偏差的影响，以及无偏记忆如何通过学习成功和失败的策略来解决这些偏差，从而分别减少了$	imes 4.5$和$	imes 3.5$倍的未解决协商，与非记忆和原始记忆基线相比，同时完全减轻了SLA违规，并改善了延迟和节能分布。

## 🔬 方法详解

**问题定义**：论文旨在解决6G RAN-Edge网络中，基于LLM的Agent在跨域资源编排时，由于认知偏差（如首因效应、近因效应、确认偏差和可得性偏差）导致决策失误和效率降低的问题。现有方法未能有效消除这些偏差，导致Agent无法充分利用历史经验，做出最优决策。

**核心思路**：论文的核心思路是构建一个“无偏集体记忆”，该记忆能够存储和检索Agent的成功和失败经验，并采取措施减轻认知偏差的影响。通过让Agent从更全面、更客观的历史数据中学习，提高其决策的准确性和效率。

**技术框架**：该框架包含以下主要模块：1) RAN Agent和Edge Agent，负责能源效率和延迟保证的协商；2) 数字孪生(DT)，用于测试Agent的提案；3) 无偏集体记忆，存储Agent的协商历史，并提供策略检索功能。Agent首先与DT交互进行方案测试，然后利用无偏集体记忆检索相似的历史策略，并根据检索结果进行决策。

**关键创新**：最重要的技术创新点在于无偏集体记忆的设计，它通过以下机制来减轻认知偏差：1) 语义检索：使用Jaccard相似性进行策略检索，避免简单匹配带来的偏差；2) 失败学习：放大SLA违规的权重，强制包含失败案例，克服确认偏差；3) 多样性增强：鼓励检索多样化的策略，减少可得性偏差；4) 时间加权：使用缓慢衰减的近因和首因加权，平衡新旧经验的影响。

**关键设计**：无偏集体记忆的关键设计包括：Jaccard相似性阈值的设置，用于控制语义检索的范围；SLA违规权重的具体数值，用于放大失败案例的影响；多样性增强的具体算法，例如使用聚类或采样方法选择代表性策略；以及近因和首因加权的衰减系数，用于控制时间因素的影响。论文中开源了无偏记忆的mockup版本。

## 📊 实验亮点

实验结果表明，与非记忆和原始记忆基线相比，该无偏集体记忆框架分别减少了$	imes 4.5$和$	imes 3.5$倍的未解决协商，同时完全消除了SLA违规。此外，该框架还改善了延迟和节能的分布，表明其在提高网络性能方面的有效性。

## 🎯 应用场景

该研究成果可应用于未来的6G网络管理，实现更智能、高效的资源分配和优化。通过消除认知偏差，Agent能够做出更合理的决策，提高网络性能，降低运营成本，并为用户提供更好的服务体验。此外，该方法也可推广到其他多Agent协作的复杂系统中。

## 📄 摘要（原文）

> This paper introduces a novel framework for proactive cross-domain resource orchestration in 6G RAN-Edge networks, featuring large language model (LLM)-augmented agents. The system comprises specialized RAN (energy efficiency) and Edge (latency assurance) agents that engage in iterative negotiation, supported by advanced reasoning and planning capabilities. Agents dynamically interact with a digital twin (DT) to test their proposals and leverage a long-term collective memory where their joint successful and failed agreements along with the related network contexts are distilled into strategies to either follow or avoid and subsequently stored. Given that agents are subject to a plethora of cognitive distortions when retrieving those past experiences -- such as primacy, recency, confirmation and availability biases -- we propose in this work a novel unbiased memory design (A reusable mockup version of the unbiased memory source code is available for non-commercial use at https://github.com/HatimChergui/unbiased-collective-memory). featuring (i) semantic retrieval of past strategies via Jaccard similarity; (ii) learning from failures through amplified weighting of SLA violations and mandatory inclusion of failed negotiation cases to mitigate confirmation bias; (iii) diversity enforcement to minimize availability bias and (iv) recency and primacy weighting with slow decay to counteract temporal biases. Evaluation results showcase the impact of existing biases and how the unbiased memory allows to tackle them by learning from both successful and failed strategies, either present or old, resulting in $\times 4.5$ and $\times 3.5$ reductions of unresolved negotiations compared to non-memory and vanilla memory baselines, respectively, while totally mitigating SLA violations as well as improving latency and energy saving distributions.

