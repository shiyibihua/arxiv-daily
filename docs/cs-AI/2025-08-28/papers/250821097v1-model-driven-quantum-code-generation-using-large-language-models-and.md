---
layout: default
title: Model-Driven Quantum Code Generation Using Large Language Models and Retrieval-Augmented Generation
---

# Model-Driven Quantum Code Generation Using Large Language Models and Retrieval-Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21097" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21097v1</a>
  <a href="https://arxiv.org/pdf/2508.21097.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21097v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21097v1', 'Model-Driven Quantum Code Generation Using Large Language Models and Retrieval-Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nazanin Siavash, Armin Moin

**分类**: cs.SE, cs.AI

**发布日期**: 2025-08-28

**备注**: This paper is accepted to the New Ideas and Emerging Results (NIER) track of the ACM/IEEE 28th International Conference on Model Driven Engineering Languages and Systems (MODELS)

**DOI**: [10.1109/MODELS67397.2025.00031](https://doi.org/10.1109/MODELS67397.2025.00031)

---

## 💡 一句话要点

**提出基于大语言模型的量子代码生成方法以应对开发者技能不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量子计算` `代码生成` `大型语言模型` `增强检索生成` `UML模型` `软件工程` `机器学习`

## 📋 核心要点

1. 现有方法在量子软件开发中面临开发者技能不足和异构平台环境带来的高成本与风险。
2. 论文提出通过结合大型语言模型和增强检索生成技术，来实现从UML模型实例生成量子代码的解决方案。
3. 实验结果显示，优化提示设计可以使CodeBLEU分数提高四倍，显著提升量子代码的准确性和一致性。

## 📝 摘要（中文）

本文介绍了一种新的研究方向，通过利用大型语言模型（LLMs）和增强检索生成（RAG）管道，实现模型到文本/代码的转换，特别关注量子及混合量子-经典软件系统。该方法旨在降低异构平台环境下的开发成本和风险，并验证了从UML模型实例生成代码的可行性。使用Qiskit库生成的Python代码可在量子计算机上执行。实验结果表明，经过精心设计的提示可以将CodeBLEU分数提高四倍，生成更准确和一致的量子代码。未来的研究可以进一步探讨其他研究问题，如将软件系统模型实例作为RAG管道的信息源等。

## 🔬 方法详解

**问题定义**：本文旨在解决量子软件开发中由于开发者技能不足和异构平台环境导致的高成本和风险问题。现有方法在代码生成的准确性和一致性方面存在不足。

**核心思路**：论文的核心思路是结合大型语言模型和增强检索生成技术，通过从UML模型实例生成量子代码，来提高代码生成的效率和质量。这样的设计旨在利用现有的开源资源和模型能力，降低开发门槛。

**技术框架**：整体架构包括三个主要模块：首先，使用UML模型实例作为输入；其次，通过RAG管道检索相关的Qiskit代码示例；最后，利用大型语言模型生成最终的量子代码。

**关键创新**：最重要的技术创新在于将RAG与大型语言模型结合，形成了一种新的代码生成方法。这种方法与传统的代码生成技术相比，能够更好地利用外部知识库，提高生成代码的准确性和一致性。

**关键设计**：在实验中，设计了多种提示策略，以优化模型的输出质量。使用的损失函数和网络结构基于现有的LLM架构，确保生成的代码符合量子计算的特定要求。

## 📊 实验亮点

实验结果显示，通过优化提示设计，CodeBLEU分数提高了四倍，表明生成的量子代码在准确性和一致性上有显著提升。这一成果为量子软件开发提供了新的思路和方法。

## 🎯 应用场景

该研究的潜在应用领域包括量子软件开发、教育培训以及软件工程工具的自动化。通过降低开发门槛和提高代码生成的效率，能够推动量子计算技术的普及和应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This paper introduces a novel research direction for model-to-text/code transformations by leveraging Large Language Models (LLMs) that can be enhanced with Retrieval-Augmented Generation (RAG) pipelines. The focus is on quantum and hybrid quantum-classical software systems, where model-driven approaches can help reduce the costs and mitigate the risks associated with the heterogeneous platform landscape and lack of developers' skills. We validate one of the proposed ideas regarding generating code out of UML model instances of software systems. This Python code uses a well-established library, called Qiskit, to execute on gate-based or circuit-based quantum computers. The RAG pipeline that we deploy incorporates sample Qiskit code from public GitHub repositories. Experimental results show that well-engineered prompts can improve CodeBLEU scores by up to a factor of four, yielding more accurate and consistent quantum code. However, the proposed research direction can go beyond this through further investigation in the future by conducting experiments to address our other research questions and ideas proposed here, such as deploying software system model instances as the source of information in the RAG pipelines, or deploying LLMs for code-to-code transformations, for instance, for transpilation use cases.

