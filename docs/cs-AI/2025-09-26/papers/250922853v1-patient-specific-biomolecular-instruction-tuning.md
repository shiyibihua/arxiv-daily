---
layout: default
title: Patient-specific Biomolecular Instruction Tuning
---

# Patient-specific Biomolecular Instruction Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22853" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22853v1</a>
  <a href="https://arxiv.org/pdf/2509.22853.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22853v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22853v1', 'Patient-specific Biomolecular Instruction Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Irsyad Adam, Zekai Chen, David Laub, Shaun Porwal, Arda Pekis, Kevin Brown

**分类**: q-bio.QM, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出KRONOS图-LLM框架，结合CPTAC-PROTSTRUCT数据集，提升肿瘤精准医疗中患者个体化蛋白质组学理解。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `蛋白质组学` `大型语言模型` `图神经网络` `指令调优` `精准医疗`

## 📋 核心要点

1. 现有方法缺乏从蛋白质组学数据进行临床解释的指令调优数据集，限制了LLM在肿瘤精准医疗中的应用。
2. KRONOS框架结合分子相互作用拓扑结构与蛋白质组学，学习患者特定的图表示，增强LLM的临床推理能力。
3. 实验结果表明，KRONOS在分子分类、时间轨迹建模和肿瘤分期预测等任务中表现出色，提升了精准医疗水平。

## 📝 摘要（中文）

蛋白质组学数据对于理解疾病的致病机制至关重要。在癌症研究中，分子特征分析能够通过识别驱动个体化肿瘤进展、治疗抵抗和临床异质性的生物过程，实现精准医疗。多模态大型语言模型（LLMs）的最新进展展现了整合和推理异构数据的卓越能力。然而，由于缺乏能够从蛋白质组学数据进行临床解释的指令调优数据集，以及缺乏旨在捕获分子数据丰富异质性的语言建模架构，因此对患者特定蛋白质组学进行多模态语言建模仍然是一个重大挑战。本文提出了CPTAC-PROTSTRUCT，这是首个用于肿瘤分子理解的指令调优数据集，包含超过40万个开放式示例，这些示例来源于国家蛋白质组学癌症研究（CPTAC）中个体化的蛋白质组学谱。此外，我们提出了KRONOS（通过结构化调优实现肿瘤患者组学网络知识表示），这是一个新颖的图-LLM框架，它利用分子相互作用拓扑结构与蛋白质组学来学习患者特定的图表示，以增强临床推理能力。实验表明，KRONOS在基准临床任务（包括分子分类、时间轨迹建模和蛋白质组学肿瘤分期预测）中取得了具有竞争力的性能。最终，这种方法使LLM能够理解患者层面的发病机制，通过更准确的诊断、预后和治疗分层来推进精准医疗。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在理解患者特定蛋白质组学数据，并将其应用于肿瘤精准医疗时面临的两个主要问题：一是缺乏合适的指令调优数据集，二是缺乏能够有效处理分子数据异质性的语言建模架构。现有方法难以充分利用蛋白质组学数据中的信息，限制了LLMs在临床诊断、预后和治疗分层方面的应用。

**核心思路**：论文的核心思路是构建一个大规模的指令调优数据集（CPTAC-PROTSTRUCT），并设计一个图-LLM框架（KRONOS），将蛋白质组学数据与分子相互作用网络相结合，从而使LLMs能够更好地理解患者层面的发病机制，并进行更准确的临床推理。通过指令调优，LLM可以学习如何从蛋白质组学数据中提取有用的临床信息。通过图结构，LLM可以更好地理解分子之间的相互作用关系。

**技术框架**：KRONOS框架包含以下主要模块：1) 数据预处理模块，用于处理蛋白质组学数据和分子相互作用网络数据；2) 图表示学习模块，用于学习患者特定的图表示；3) LLM推理模块，用于基于图表示进行临床推理，例如分子分类、时间轨迹建模和肿瘤分期预测。CPTAC-PROTSTRUCT数据集用于指令调优LLM，使其能够更好地理解蛋白质组学数据。

**关键创新**：论文的关键创新点在于：1) 提出了CPTAC-PROTSTRUCT数据集，这是首个用于肿瘤分子理解的指令调优数据集；2) 提出了KRONOS框架，该框架将图神经网络与LLM相结合，能够更好地处理分子数据的异质性，并进行更准确的临床推理。与现有方法相比，KRONOS能够更好地利用蛋白质组学数据中的信息，并进行更准确的临床预测。

**关键设计**：KRONOS框架使用图神经网络（GNN）来学习患者特定的图表示。GNN的结构和参数需要根据具体任务进行调整。LLM可以使用预训练的语言模型，例如BERT或GPT。损失函数可以使用交叉熵损失或均方误差损失。指令调优过程需要仔细设计指令，以确保LLM能够学习到有用的临床信息。

## 📊 实验亮点

KRONOS在分子分类、时间轨迹建模和肿瘤分期预测等基准临床任务中取得了具有竞争力的性能。具体性能数据和对比基线在论文中详细给出，表明KRONOS能够有效提升LLM在蛋白质组学数据分析中的临床推理能力，为精准医疗提供更可靠的技术支持。

## 🎯 应用场景

该研究成果可应用于肿瘤精准医疗领域，通过分析患者的蛋白质组学数据，结合分子相互作用网络，实现更准确的诊断、预后和治疗分层。该技术还有潜力扩展到其他疾病领域，例如神经退行性疾病和自身免疫性疾病，从而推动个体化医疗的发展。

## 📄 摘要（原文）

> Proteomics data is essential to pathogenic understanding of a disease phenotype. In cancer, analysis of molecular signatures enables precision medicine through the identification of biological processes that drive individualized tumor progression, therapeutic resistance, and clinical heterogeneity. Recent advances in multimodal large language models (LLMs) have shown remarkable capacity to integrate and reason across heterogeneous data modalities. However, performing multi-modal language modeling for molecular understanding of patient-specific proteomics remains a significant challenge due to two barriers: (1) the lack of instruction-tuning datasets that enable clinical interpretation from proteomics data, and (2) the absence of language modeling architectures designed to capture the rich heterogeneity of molecular data. In this work, we introduce CPTAC-PROTSTRUCT, the first instruction tuning dataset for molecular understanding of oncology, comprising over 400k open-ended examples derived from individualized proteomic profiles curated from the largest national proteomics cancer study (CPTAC). Additionally, we propose KRONOS (Knowledge Representation of patient Omics Networks in Oncology via Structured tuning), a novel graph-LLM framework that leverages molecular interaction topology with proteomics to learn patient-specific graph representations for enhanced clinical reasoning. We show that KRONOS achieves competitive performance across benchmark clinical tasks, including molecular classification, temporal trajectory modeling, and tumor stage prediction from proteomics data. Ultimately, this approach empowers LLMs to understand patient-level pathogenesis, advancing precision medicine through more accurate diagnosis, prognosis, and treatment stratification.

