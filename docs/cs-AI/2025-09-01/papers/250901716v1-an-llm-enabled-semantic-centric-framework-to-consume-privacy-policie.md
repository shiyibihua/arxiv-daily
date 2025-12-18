---
layout: default
title: An LLM-enabled semantic-centric framework to consume privacy policies
---

# An LLM-enabled semantic-centric framework to consume privacy policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01716" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01716v1</a>
  <a href="https://arxiv.org/pdf/2509.01716.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01716v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01716v1', 'An LLM-enabled semantic-centric framework to consume privacy policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Zhao, Vladyslav Melnychuk, Jun Zhao, Jesse Wright, Nigel Shadbolt

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-01

---

## 💡 一句话要点

**提出一种基于LLM的语义中心框架，用于解析隐私政策并构建知识图谱。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐私政策分析` `大型语言模型` `知识图谱` `数据隐私` `语义理解` `自动化分析` `合规性审计`

## 📋 核心要点

1. 用户普遍忽略难以理解的隐私政策，导致数据隐私实践模糊，阻碍了用户中心Web的发展。
2. 利用大型语言模型自动从隐私政策中提取关键信息，构建基于数据隐私词汇表的知识图谱。
3. 通过法律专家增强数据集，对不同LLM进行基准测试，验证了该方法在隐私政策分析中的有效性。

## 📝 摘要（中文）

现代社会，人们拥有大量的在线账户，但由于理解上的困难，很少有人真正阅读服务条款或隐私政策。数据隐私实践的模糊性成为了以用户为中心的Web方法以及在代理世界中数据共享和重用的主要障碍。现有研究提出了使用形式化语言和推理来验证指定策略合规性的方法，作为解决忽略隐私政策问题的潜在方案。然而，大规模创建或获取此类形式化策略仍然存在关键差距。我们提出了一种以语义为中心的方法，利用最先进的大型语言模型（LLM），自动识别隐私政策中的关键信息，并构建 $\mathit{Pr}^2\mathit{Graph}$，这是一个基于数据隐私词汇表（DPV）的知识图谱，用于支持下游任务。我们发布了包含该pipeline的，针对前100个热门网站的$\mathit{Pr}^2\mathit{Graph}$作为公共资源。我们还展示了如何使用$\mathit{Pr}^2\mathit{Graph}$通过构建形式化策略表示（如开放数字版权语言（ODRL）或长期语义数据使用条款（psDToU））来支持下游任务。为了评估技术能力，我们聘请法律专家创建自定义注释，从而丰富了Policy-IE数据集。我们对不同大型语言模型在我们的pipeline中的性能进行了基准测试，并验证了它们的能力。总的来说，它们揭示了大规模分析在线服务隐私实践的可能性，这是一个有希望的Web和互联网审计方向。我们将所有数据集和源代码作为公共资源发布，以方便重用和改进。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模自动化分析隐私政策的难题。现有方法依赖人工或小规模的分析，无法有效应对互联网上大量且复杂的隐私政策。现有方法在创建或获取大规模形式化策略方面存在关键差距，难以实现对隐私政策的合规性验证。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的强大语义理解和信息抽取能力，自动从隐私政策中提取关键信息，并将其转化为结构化的知识图谱。这种方法旨在克服人工分析的局限性，实现对隐私政策的大规模自动化分析。

**技术框架**：该框架主要包含以下几个阶段：1) 使用LLM从隐私政策文本中提取关键信息，例如数据收集、数据使用、数据共享等。2) 将提取的信息映射到数据隐私词汇表（DPV），实现语义标准化。3) 基于DPV构建知识图谱$\mathit{Pr}^2\mathit{Graph}$，其中节点表示隐私实践的概念，边表示概念之间的关系。4) 利用$\mathit{Pr}^2\mathit{Graph}$支持下游任务，例如生成形式化策略表示（ODRL, psDToU）。

**关键创新**：该论文的关键创新在于将大型语言模型应用于隐私政策的自动化分析，并构建了基于数据隐私词汇表的知识图谱。与传统方法相比，该方法能够更有效地处理大规模的隐私政策文本，并提取出更准确、更全面的隐私实践信息。此外，该方法还能够将提取的信息转化为结构化的知识表示，方便后续的推理和分析。

**关键设计**：论文的关键设计包括：1) 使用特定的prompt工程来指导LLM进行信息抽取，以提高抽取精度。2) 基于数据隐私词汇表（DPV）构建知识图谱，确保知识表示的标准化和可互操作性。3) 使用法律专家进行数据标注，以提高模型的训练质量和泛化能力。4) 针对不同的LLM进行基准测试，以评估其在隐私政策分析任务中的性能。

## 📊 实验亮点

论文通过实验验证了该方法的有效性。通过法律专家增强Policy-IE数据集，并对不同LLM进行了基准测试。实验结果表明，该方法能够有效地从隐私政策中提取关键信息，并构建高质量的知识图谱。具体性能数据和对比基线在论文中进行了详细描述。

## 🎯 应用场景

该研究成果可应用于多个领域，包括：隐私合规性审计、用户隐私风险评估、个性化隐私设置推荐、以及开发更透明和用户友好的在线服务。通过大规模分析隐私政策，可以帮助监管机构更好地监管互联网服务，保护用户的数据隐私权益。

## 📄 摘要（原文）

> In modern times, people have numerous online accounts, but they rarely read the Terms of Service or Privacy Policy of those sites, despite claiming otherwise, due to the practical difficulty in comprehending them. The mist of data privacy practices forms a major barrier for user-centred Web approaches, and for data sharing and reusing in an agentic world. Existing research proposed methods for using formal languages and reasoning for verifying the compliance of a specified policy, as a potential cure for ignoring privacy policies. However, a critical gap remains in the creation or acquisition of such formal policies at scale. We present a semantic-centric approach for using state-of-the-art large language models (LLM), to automatically identify key information about privacy practices from privacy policies, and construct $\mathit{Pr}^2\mathit{Graph}$, knowledge graph with grounding from Data Privacy Vocabulary (DPV) for privacy practices, to support downstream tasks. Along with the pipeline, the $\mathit{Pr}^2\mathit{Graph}$ for the top-100 popular websites is also released as a public resource, by using the pipeline for analysis. We also demonstrate how the $\mathit{Pr}^2\mathit{Graph}$ can be used to support downstream tasks by constructing formal policy representations such as Open Digital Right Language (ODRL) or perennial semantic Data Terms of Use (psDToU). To evaluate the technology capability, we enriched the Policy-IE dataset by employing legal experts to create custom annotations. We benchmarked the performance of different large language models for our pipeline and verified their capabilities. Overall, they shed light on the possibility of large-scale analysis of online services' privacy practices, as a promising direction to audit the Web and the Internet. We release all datasets and source code as public resources to facilitate reuse and improvement.

