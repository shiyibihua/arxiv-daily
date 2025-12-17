---
layout: default
title: SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions
---

# SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14277" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14277v1</a>
  <a href="https://arxiv.org/pdf/2512.14277.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14277v1" onclick="toggleFavorite(this, '2512.14277v1', 'SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Panayiotis Smeros, Vincent Emonet, Ruijie Wang, Ana-Claudia Sima, Tarcisio Mendes de Farias

**分类**: cs.IR, cs.AI, cs.CL

**发布日期**: 2025-12-16

**备注**: 17 pages, 8 figures, 1 table. Under Review

---

## 💡 一句话要点

**SPARQL-LLM：一种基于轻量级元数据的实时自然语言到SPARQL查询生成方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言处理` `SPARQL查询生成` `知识图谱` `大型语言模型` `元数据驱动`

## 📋 核心要点

1. 现有方法在自然语言生成SPARQL查询时，侧重于单数据源的准确性，忽略了联邦查询能力、运行时间和成本等关键因素。
2. SPARQL-LLM利用轻量级元数据，构建了一个开源、与三元组存储无关的框架，用于从自然语言文本生成SPARQL查询。
3. 实验结果表明，SPARQL-LLM在F1分数上提升了24%，速度提升高达36倍，且成本极低，适用于实时应用。

## 📝 摘要（中文）

大型语言模型的出现促进了从自然语言生成结构化查询（如SPARQL查询）的新方法。然而，这些方法主要关注单个来源的响应准确性，忽略了其他评估标准，如分布式数据存储上的联邦查询能力，以及生成SPARQL查询的运行时间和成本。因此，它们通常无法直接用于生产环境，或者难以在具有良好准确性的（潜在的联邦）知识图谱上部署。为了解决这些问题，本文扩展了我们之前的工作，描述并系统地评估了SPARQL-LLM，这是一种开源且与三元组存储无关的方法，它由轻量级元数据驱动，可以从自然语言文本生成SPARQL查询。我们首先描述了它的架构，该架构由用于元数据索引、提示构建以及查询生成和执行的专用组件组成。然后，我们基于最先进的多语言问题挑战以及来自生物信息学领域中最流行的三个知识图谱的问题集合对其进行评估。结果表明，在最先进的挑战中，F1分数显着提高了24％，对英语和西班牙语等高资源语言的适应性强，并且能够形成复杂的联邦生物信息学查询。此外，我们表明SPARQL-LLM比参与挑战的其他系统快36倍，每个问题的成本最高为0.01美元，使其适用于实时、低成本的文本到SPARQL应用程序。可以在https://www.expasy.org/chat上找到一个部署在真实世界分散知识图谱上的此类应用程序。

## 🔬 方法详解

**问题定义**：现有方法在将自然语言转换为SPARQL查询时，主要关注单数据源的准确性，而忽略了在分布式知识图谱上的联邦查询能力、查询生成的速度和成本。这使得这些方法难以在实际生产环境中部署，尤其是在需要实时响应和处理大规模知识图谱时。

**核心思路**：SPARQL-LLM的核心思路是利用轻量级的元数据来指导大型语言模型生成SPARQL查询。通过对知识图谱的元数据进行索引，并将其融入到提示构建过程中，可以有效地约束语言模型的输出，使其生成更准确、更高效的SPARQL查询。这种方法旨在平衡查询准确性、查询速度和部署成本。

**技术框架**：SPARQL-LLM的整体架构包含以下几个主要模块：1) **元数据索引模块**：负责从知识图谱中提取和索引元数据，例如实体、关系和属性。2) **提示构建模块**：根据自然语言问题和索引的元数据，构建用于输入到大型语言模型的提示。3) **查询生成模块**：利用大型语言模型生成SPARQL查询。4) **查询执行模块**：执行生成的SPARQL查询，并返回结果。

**关键创新**：SPARQL-LLM的关键创新在于其轻量级元数据驱动的方法。与直接使用大型语言模型生成SPARQL查询的方法相比，SPARQL-LLM通过元数据约束，提高了查询的准确性和效率，降低了生成成本。此外，该方法具有与三元组存储无关的特性，可以灵活地应用于不同的知识图谱。

**关键设计**：SPARQL-LLM的关键设计包括：1) **元数据索引策略**：选择合适的元数据类型和索引方法，以平衡索引的效率和覆盖范围。2) **提示构建策略**：设计有效的提示模板，将自然语言问题和元数据信息有效地融合到提示中。3) **语言模型选择**：选择合适的语言模型，以平衡生成质量和计算成本。4) **查询优化策略**：对生成的SPARQL查询进行优化，以提高查询执行效率。

## 📊 实验亮点

SPARQL-LLM在多语言问题挑战中，F1分数提升了24%，显著优于现有方法。在生物信息学知识图谱上的实验表明，SPARQL-LLM能够生成复杂的联邦查询。此外，SPARQL-LLM的查询速度比其他系统快36倍，每个问题的成本最高仅为0.01美元，使其具有很高的实用价值。

## 🎯 应用场景

SPARQL-LLM可应用于多种场景，例如智能问答系统、知识图谱检索、生物信息学数据分析等。它能够帮助用户通过自然语言快速准确地查询知识图谱，降低了知识获取的门槛，并为构建智能化的知识服务提供了有力支持。未来，该技术有望在医疗、金融、教育等领域发挥重要作用。

## 📄 摘要（原文）

> The advent of large language models is contributing to the emergence of novel approaches that promise to better tackle the challenge of generating structured queries, such as SPARQL queries, from natural language. However, these new approaches mostly focus on response accuracy over a single source while ignoring other evaluation criteria, such as federated query capability over distributed data stores, as well as runtime and cost to generate SPARQL queries. Consequently, they are often not production-ready or easy to deploy over (potentially federated) knowledge graphs with good accuracy. To mitigate these issues, in this paper, we extend our previous work and describe and systematically evaluate SPARQL-LLM, an open-source and triplestore-agnostic approach, powered by lightweight metadata, that generates SPARQL queries from natural language text. First, we describe its architecture, which consists of dedicated components for metadata indexing, prompt building, and query generation and execution. Then, we evaluate it based on a state-of-the-art challenge with multilingual questions, and a collection of questions from three of the most prevalent knowledge graphs within the field of bioinformatics. Our results demonstrate a substantial increase of 24% in the F1 Score on the state-of-the-art challenge, adaptability to high-resource languages such as English and Spanish, as well as ability to form complex and federated bioinformatics queries. Furthermore, we show that SPARQL-LLM is up to 36x faster than other systems participating in the challenge, while costing a maximum of $0.01 per question, making it suitable for real-time, low-cost text-to-SPARQL applications. One such application deployed over real-world decentralized knowledge graphs can be found at https://www.expasy.org/chat.

