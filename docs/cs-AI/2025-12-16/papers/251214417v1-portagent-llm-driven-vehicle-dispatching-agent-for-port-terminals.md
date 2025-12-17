---
layout: default
title: PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals
---

# PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14417" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14417v1</a>
  <a href="https://arxiv.org/pdf/2512.14417.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14417v1" onclick="toggleFavorite(this, '2512.14417v1', 'PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jia Hu, Junqi Li, Weimeng Lin, Peng Jia, Yuxiong Ji, Jintao Lai

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**PortAgent：基于LLM的港口车辆调度智能体，提升跨终端迁移能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `车辆调度系统` `自动化集装箱码头` `大型语言模型` `迁移学习` `检索增强生成`

## 📋 核心要点

1. 现有车辆调度系统(VDS)在不同港口间的迁移性差，高度依赖专家知识和大量特定数据，部署耗时。
2. PortAgent利用大型语言模型(LLM)构建虚拟专家团队(VET)，模拟专家进行VDS迁移，降低对人工和数据的依赖。
3. 通过检索增强生成(RAG)获取少量示例，结合LLM的自我纠正机制，实现VDS的自动设计和快速部署。

## 📝 摘要（中文）

车辆调度系统(VDS)对于自动化集装箱码头(ACT)的运营效率至关重要。然而，由于其在不同码头之间的低迁移性，VDS的广泛商业化受到阻碍。这种迁移性挑战源于三个限制：高度依赖港口运营专家、对特定码头数据的高需求以及耗时的人工部署过程。本文利用大型语言模型(LLM)的兴起，提出了一种由LLM驱动的车辆调度智能体PortAgent，该智能体可以完全自动化VDS的迁移工作流程。它具有三个特点：(1)无需港口运营专家；(2)对数据的需求低；(3)部署速度快。具体来说，通过虚拟专家团队(VET)消除了对专家依赖。VET与四个虚拟专家（包括知识检索器、建模器、编码器和调试器）合作，模拟人类专家团队进行VDS迁移工作流程。这些专家通过少样本示例学习方法专注于终端VDS领域。通过这种方法，专家能够从一些VDS示例中学习VDS领域知识。这些示例通过检索增强生成(RAG)机制检索，从而降低了对终端特定数据的高需求。此外，在这些专家之间建立了一个自动VDS设计工作流程，以避免额外的人工干预。在这个工作流程中，创建了一个受LLM Reflexion框架启发的自我纠正循环。

## 🔬 方法详解

**问题定义**：现有自动化集装箱码头(ACT)的车辆调度系统(VDS)难以在不同码头之间迁移。主要痛点在于：1)高度依赖港口运营专家进行配置和优化；2)需要大量的特定码头数据进行训练和调整；3)人工部署过程耗时且容易出错。这些因素限制了VDS的广泛应用和商业化。

**核心思路**：利用大型语言模型(LLM)的强大能力，构建一个虚拟专家团队(VET)，模拟人类专家进行VDS的迁移和部署。通过少样本学习和检索增强生成(RAG)技术，降低对专家知识和大量数据的依赖。同时，引入自我纠正机制，提高VDS设计的自动化程度和准确性。这样设计的目的是为了实现VDS的快速、低成本、自动化迁移。

**技术框架**：PortAgent的核心是虚拟专家团队(VET)，包含四个虚拟专家：知识检索器、建模器、编码器和调试器。整体流程如下：1)知识检索器通过RAG机制从少量VDS示例中检索相关知识；2)建模器根据检索到的知识构建VDS模型；3)编码器将VDS模型转化为可执行的代码；4)调试器对代码进行测试和调试，并利用自我纠正循环进行优化。整个过程无需人工干预，实现VDS的自动设计和部署。

**关键创新**：主要创新点在于：1)利用LLM构建虚拟专家团队，模拟人类专家进行VDS迁移，降低对人工依赖；2)采用检索增强生成(RAG)技术，从少量示例中学习VDS领域知识，降低对大量数据的需求；3)引入自我纠正循环，提高VDS设计的自动化程度和准确性。与现有方法相比，PortAgent无需人工干预，能够快速、低成本地将VDS迁移到新的码头。

**关键设计**：RAG机制的关键在于如何选择合适的VDS示例进行检索。论文可能使用了某种相似度度量方法来评估示例与目标码头的相关性。自我纠正循环的关键在于如何设计有效的反馈机制，指导LLM进行优化。具体参数设置、损失函数和网络结构等技术细节未知。

## 📊 实验亮点

由于论文中没有提供具体的实验数据，因此无法总结实验亮点。但是，该研究提出了一种新颖的基于LLM的VDS迁移方法，具有重要的理论和实践意义。未来的研究可以关注PortAgent在实际码头环境中的性能评估和优化。

## 🎯 应用场景

PortAgent可应用于自动化集装箱码头(ACT)的车辆调度系统(VDS)的快速部署和迁移。它降低了对港口运营专家和大量数据的依赖，缩短了部署时间，降低了成本。该研究成果有助于推动VDS在更多码头的应用，提高港口运营效率，并可能扩展到其他需要领域知识和自动化部署的智能体系统中。

## 📄 摘要（原文）

> Vehicle Dispatching Systems (VDSs) are critical to the operational efficiency of Automated Container Terminals (ACTs). However, their widespread commercialization is hindered due to their low transferability across diverse terminals. This transferability challenge stems from three limitations: high reliance on port operational specialists, a high demand for terminal-specific data, and time-consuming manual deployment processes. Leveraging the emergence of Large Language Models (LLMs), this paper proposes PortAgent, an LLM-driven vehicle dispatching agent that fully automates the VDS transferring workflow. It bears three features: (1) no need for port operations specialists; (2) low need of data; and (3) fast deployment. Specifically, specialist dependency is eliminated by the Virtual Expert Team (VET). The VET collaborates with four virtual experts, including a Knowledge Retriever, Modeler, Coder, and Debugger, to emulate a human expert team for the VDS transferring workflow. These experts specialize in the domain of terminal VDS via a few-shot example learning approach. Through this approach, the experts are able to learn VDS-domain knowledge from a few VDS examples. These examples are retrieved via a Retrieval-Augmented Generation (RAG) mechanism, mitigating the high demand for terminal-specific data. Furthermore, an automatic VDS design workflow is established among these experts to avoid extra manual interventions. In this workflow, a self-correction loop inspired by the LLM Reflexion framework is created

