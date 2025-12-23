---
layout: default
title: Large Language Model Agent for Modular Task Execution in Drug Discovery
---

# Large Language Model Agent for Modular Task Execution in Drug Discovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.02925" class="toolbar-btn" target="_blank">📄 arXiv: 2507.02925v3</a>
  <a href="https://arxiv.org/pdf/2507.02925.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.02925v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.02925v3', 'Large Language Model Agent for Modular Task Execution in Drug Discovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Janghoon Ock, Radheesh Sharma Meda, Srivathsan Badrinarayanan, Neha S. Aluru, Achuth Chandrasekhar, Amir Barati Farimani

**分类**: cs.LG, cs.CL, q-bio.BM

**发布日期**: 2025-06-26 (更新: 2025-12-12)

---

## 💡 一句话要点

**提出模块化框架以优化药物发现中的关键任务**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `药物发现` `大型语言模型` `模块化框架` `生物医学数据` `分子生成` `属性预测` `3D结构生成` `自动化`

## 📋 核心要点

1. 现有药物发现方法在自动化和任务整合方面存在不足，导致效率低下和信息孤岛。
2. 论文提出的框架结合LLM推理与领域工具，实现了多种药物发现任务的自动化，提升了整体效率。
3. 实验结果表明，经过两轮精炼，符合QED > 0.6的分子数量从34增加到55，显示出显著的优化效果。

## 📝 摘要（中文）

本文提出了一种基于大型语言模型（LLMs）的模块化框架，旨在自动化和简化早期计算药物发现流程中的关键任务。通过将LLM推理与特定领域工具相结合，该框架能够进行生物医学数据检索、文献基础的问题回答、分子生成、多属性预测、属性感知的分子精炼以及3D蛋白-配体结构生成。该代理能够自主检索相关的生物分子信息，并在机制性问题回答中表现出比标准LLMs更高的上下文准确性。实验结果显示，该方法在分子筛选、优先级排序和结构评估方面有效支持药物发现。

## 🔬 方法详解

**问题定义**：本文旨在解决药物发现过程中任务自动化不足的问题，现有方法往往无法有效整合多种任务，导致效率低下和信息孤立。

**核心思路**：通过构建一个模块化框架，将大型语言模型与领域特定工具结合，自动化执行药物发现中的关键任务，从而提高整体工作效率和准确性。

**技术框架**：该框架包括多个主要模块，如生物医学数据检索、文献基础的问题回答、分子生成、多属性预测、分子精炼和3D蛋白-配体结构生成。每个模块协同工作，形成一个完整的药物发现流程。

**关键创新**：最重要的创新在于将LLM推理与领域工具的结合，显著提升了生物分子信息检索和问题回答的准确性，与传统方法相比，能够更好地处理复杂的生物医学问题。

**关键设计**：框架中使用了Boltz-2生成3D蛋白-配体复合物，并快速估算候选化合物的结合亲和力，此外，采用了特定的参数设置和损失函数以优化分子生成和属性预测的效果。

## 📊 实验亮点

实验结果显示，在两轮分子精炼中，符合QED > 0.6的分子数量从34增加到55，且符合Ghose过滤器的分子数量从32增加到55，表明该框架在分子筛选和优化方面具有显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括药物发现、分子设计和生物医学研究。通过自动化关键任务，该框架能够大幅提高药物研发的效率，降低成本，并为新药的快速筛选和优化提供支持，未来可能在制药行业产生深远影响。

## 📄 摘要（原文）

> We present a modular framework powered by large language models (LLMs) that automates and streamlines key tasks across the early-stage computational drug discovery pipeline. By combining LLM reasoning with domain-specific tools, the framework performs biomedical data retrieval, literature-grounded question answering via retrieval-augmented generation, molecular generation, multi-property prediction, property-aware molecular refinement, and 3D protein-ligand structure generation. The agent autonomously retrieved relevant biomolecular information, including FASTA sequences, SMILES representations, and literature, and answered mechanistic questions with improved contextual accuracy compared to standard LLMs. It then generated chemically diverse seed molecules and predicted 75 properties, including ADMET-related and general physicochemical descriptors, which guided iterative molecular refinement. Across two refinement rounds, the number of molecules with QED > 0.6 increased from 34 to 55. The number of molecules satisfying empirical drug-likeness filters also rose; for example, compliance with the Ghose filter increased from 32 to 55 within a pool of 100 molecules. The framework also employed Boltz-2 to generate 3D protein-ligand complexes and provide rapid binding affinity estimates for candidate compounds. These results demonstrate that the approach effectively supports molecular screening, prioritization, and structure evaluation. Its modular design enables flexible integration of evolving tools and models, providing a scalable foundation for AI-assisted therapeutic discovery.

