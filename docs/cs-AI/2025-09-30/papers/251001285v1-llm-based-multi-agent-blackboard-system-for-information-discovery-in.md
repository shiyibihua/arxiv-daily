---
layout: default
title: LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science
---

# LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01285" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01285v1</a>
  <a href="https://arxiv.org/pdf/2510.01285.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01285v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01285v1', 'LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alireza Salemi, Mihir Parmar, Palash Goyal, Yiwen Song, Jinsung Yoon, Hamed Zamani, Hamid Palangi, Tomas Pfister

**分类**: cs.MA, cs.AI, cs.CL, cs.IR, cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出基于LLM的多智能体黑板系统，解决数据科学中信息发现难题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `黑板架构` `信息发现` `大型语言模型` `数据湖` `数据科学` `自主协作` `可扩展性`

## 📋 核心要点

1. 现有单智能体系统难以处理大型异构数据湖中的信息发现，而主从式多智能体系统依赖于对子智能体能力的精确了解。
2. 论文提出一种基于黑板架构的多智能体通信范式，通过共享黑板实现智能体间的自主协作，提升可扩展性和灵活性。
3. 实验结果表明，该方法在数据发现任务上显著优于RAG和主从式多智能体系统，端到端任务成功率提升13%-57%。

## 📝 摘要（中文）

大型语言模型（LLMs）的快速发展为数据科学带来了新的机遇，但其在实际部署中常受到在大型异构数据湖中发现相关数据的挑战的限制。现有方法难以应对这一问题：单智能体系统很快被大型数据湖中庞大的异构文件所淹没，而基于主从范式的多智能体系统依赖于刚性的中央控制器进行任务分配，这需要精确了解每个子智能体的能力。为了解决这些限制，我们提出了一种受传统AI模型黑板架构启发的新的多智能体通信范式。在该框架中，中央智能体将请求发布到共享黑板上，而负责数据湖分区或通用信息检索的自治子智能体根据其能力自愿响应。这种设计通过消除中央协调器预先了解所有子智能体专业知识的需求，提高了可扩展性和灵活性。我们在需要显式数据发现的三个基准上评估了我们的方法：KramaBench和DS-Bench和DA-Code的修改版本以包含数据发现。实验结果表明，黑板架构显著优于包括RAG和主从多智能体范式在内的基线，在端到端任务成功率方面实现了13%到57%的相对提升，并且在专有和开源LLM上，数据发现的F1得分相对提升高达9%。我们的发现确立了黑板范式作为多智能体系统的一种可扩展且可泛化的通信框架。

## 🔬 方法详解

**问题定义**：论文旨在解决数据科学中，大型异构数据湖中信息发现的难题。现有方法，如单智能体系统，容易被海量数据淹没；主从式多智能体系统则需要中央控制器预先了解所有子智能体的能力，限制了其可扩展性和灵活性。

**核心思路**：论文借鉴了传统AI中的黑板架构，将信息发现过程转化为一个多智能体协作问题。核心思想是构建一个共享的“黑板”，中央智能体发布请求，各个子智能体根据自身能力自主选择并响应请求，从而实现高效的信息发现。

**技术框架**：整体架构包含一个中央智能体和多个自治的子智能体。中央智能体负责接收用户查询，并将查询转化为具体的请求发布到黑板上。子智能体负责监听黑板上的请求，并根据自身能力选择是否响应。响应的子智能体从数据湖中检索相关信息，并将结果写回黑板。中央智能体收集黑板上的结果，并进行整合和排序，最终返回给用户。

**关键创新**：最重要的创新点在于引入了黑板架构，实现了多智能体之间的自主协作。与传统的主从式架构相比，黑板架构无需中央控制器预先了解所有子智能体的能力，从而提高了系统的可扩展性和灵活性。此外，子智能体可以根据自身能力动态地加入或退出系统，进一步增强了系统的鲁棒性。

**关键设计**：论文中，黑板的设计至关重要，需要考虑如何有效地组织和管理黑板上的信息，以及如何设计子智能体的响应机制。具体的技术细节包括：请求的格式、子智能体的注册机制、结果的排序算法等。此外，论文还针对不同的数据湖特点，设计了不同的子智能体，例如，针对文本数据的子智能体、针对图像数据的子智能体等。

## 📊 实验亮点

实验结果表明，基于黑板架构的多智能体系统在KramaBench、DS-Bench和DA-Code三个基准测试中，显著优于RAG和主从式多智能体系统。端到端任务成功率提升了13%到57%，数据发现的F1得分提升高达9%。这些结果验证了黑板架构在数据发现任务中的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于企业级数据湖的信息发现、知识图谱构建、智能问答系统等领域。通过黑板架构实现多智能体协同，能够有效提升数据检索效率和准确性，降低人工成本，加速数据驱动的决策过程，具有广阔的应用前景。

## 📄 摘要（原文）

> The rapid advancement of Large Language Models (LLMs) has opened new opportunities in data science, yet their practical deployment is often constrained by the challenge of discovering relevant data within large heterogeneous data lakes. Existing methods struggle with this: single-agent systems are quickly overwhelmed by large, heterogeneous files in the large data lakes, while multi-agent systems designed based on a master-slave paradigm depend on a rigid central controller for task allocation that requires precise knowledge of each sub-agent's capabilities. To address these limitations, we propose a novel multi-agent communication paradigm inspired by the blackboard architecture for traditional AI models. In this framework, a central agent posts requests to a shared blackboard, and autonomous subordinate agents -- either responsible for a partition of the data lake or general information retrieval -- volunteer to respond based on their capabilities. This design improves scalability and flexibility by eliminating the need for a central coordinator to have prior knowledge of all sub-agents' expertise. We evaluate our method on three benchmarks that require explicit data discovery: KramaBench and modified versions of DS-Bench and DA-Code to incorporate data discovery. Experimental results demonstrate that the blackboard architecture substantially outperforms baselines, including RAG and the master-slave multi-agent paradigm, achieving between 13% to 57% relative improvement in end-to-end task success and up to a 9% relative gain in F1 score for data discovery over the best-performing baselines across both proprietary and open-source LLMs. Our findings establish the blackboard paradigm as a scalable and generalizable communication framework for multi-agent systems.

