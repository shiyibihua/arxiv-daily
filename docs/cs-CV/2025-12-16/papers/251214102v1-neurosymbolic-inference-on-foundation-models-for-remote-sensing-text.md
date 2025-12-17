---
layout: default
title: Neurosymbolic Inference On Foundation Models For Remote Sensing Text-to-image Retrieval With Complex Queries
---

# Neurosymbolic Inference On Foundation Models For Remote Sensing Text-to-image Retrieval With Complex Queries

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14102" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14102v1</a>
  <a href="https://arxiv.org/pdf/2512.14102.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14102v1" onclick="toggleFavorite(this, '2512.14102v1', 'Neurosymbolic Inference On Foundation Models For Remote Sensing Text-to-image Retrieval With Complex Queries')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Emanuele Mezzi, Gertjan Burghouts, Maarten Kruithof

**分类**: cs.CV, cs.AI, cs.IR

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出RUNE，结合神经符号推理与大模型，解决遥感图像复杂查询的文本到图像检索问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感图像检索` `神经符号推理` `大型语言模型` `文本到图像` `复杂查询` `可解释性` `逻辑推理`

## 📋 核心要点

1. 现有遥感文本到图像检索方法缺乏可解释性，难以处理复杂的空间关系，限制了实际应用。
2. RUNE方法结合大语言模型和神经符号AI，通过显式推理图像实体与查询逻辑表达式的兼容性进行检索。
3. 实验表明，RUNE在复杂查询和图像不确定性下，性能优于现有遥感视觉语言模型，并提升了可解释性。

## 📝 摘要（中文）

本文提出了一种名为RUNE（Reasoning Using Neurosymbolic Entities）的方法，它结合了大型语言模型（LLMs）和神经符号AI，通过推理检测到的实体与从文本查询导出的First-Order Logic（FOL）表达式之间的兼容性来检索图像。与依赖隐式联合嵌入的遥感大型视觉语言模型（RS-LVLMS）不同，RUNE执行显式推理，从而提高性能和可解释性。为了可扩展性，本文提出了一种逻辑分解策略，该策略在检测到的实体的条件子集上运行，与神经方法相比，保证了更短的执行时间。本文没有使用基础模型进行端到端检索，而是仅利用它们来生成FOL表达式，并将推理委托给神经符号推理模块。通过重新利用DOTA数据集，并使用比现有基准更复杂的查询来增强它，进行评估。结果表明，LLM在文本到逻辑翻译方面的有效性，并将RUNE与最先进的RS-LVLMs进行了比较，证明了其卓越的性能。本文引入了两个指标，查询复杂度的检索鲁棒性（RRQC）和图像不确定性的检索鲁棒性（RRIU），评估了相对于查询复杂度和图像不确定性的性能。RUNE在复杂的RS检索任务中优于联合嵌入模型，在性能、鲁棒性和可解释性方面都有所提高。通过洪水后卫星图像检索的用例，展示了RUNE在实际RS应用中的潜力。

## 🔬 方法详解

**问题定义**：遥感领域文本到图像检索任务面临的挑战是现有方法难以处理复杂查询，特别是涉及空间关系的查询，并且缺乏可解释性。现有的遥感视觉语言模型（RS-LVLMs）依赖于隐式的联合嵌入，难以进行显式的推理，导致在复杂场景下的检索效果不佳。

**核心思路**：RUNE的核心思路是将文本查询转化为一阶逻辑（FOL）表达式，然后通过神经符号推理模块来判断图像中检测到的实体是否满足这些逻辑表达式。这种方法将检索过程分解为文本理解、逻辑推理和实体匹配三个步骤，从而提高了可解释性和处理复杂查询的能力。通过将推理过程显式化，RUNE能够更好地应对复杂空间关系和不确定性。

**技术框架**：RUNE的整体框架包括以下几个主要模块：1) **文本到逻辑转换模块**：使用大型语言模型（LLMs）将文本查询转换为一阶逻辑（FOL）表达式。2) **实体检测模块**：使用目标检测模型检测遥感图像中的实体。3) **神经符号推理模块**：该模块接收FOL表达式和检测到的实体作为输入，通过推理判断图像是否满足查询条件。为了提高可扩展性，RUNE采用了一种逻辑分解策略，将复杂的FOL表达式分解为更小的子表达式，并在检测到的实体的子集上进行推理。

**关键创新**：RUNE的关键创新在于将神经符号推理引入到遥感文本到图像检索任务中。与传统的基于联合嵌入的方法不同，RUNE通过显式的逻辑推理来判断图像是否满足查询条件，从而提高了可解释性和处理复杂查询的能力。此外，RUNE还提出了一种逻辑分解策略，提高了推理效率。

**关键设计**：RUNE的关键设计包括：1) 使用预训练的大型语言模型（LLMs）进行文本到逻辑的转换，利用LLMs强大的语义理解能力。2) 设计了一种逻辑分解策略，将复杂的FOL表达式分解为更小的子表达式，并在检测到的实体的子集上进行推理，从而提高推理效率。3) 引入了两个新的评估指标，即查询复杂度的检索鲁棒性（RRQC）和图像不确定性的检索鲁棒性（RRIU），用于评估模型在复杂查询和图像不确定性下的性能。

## 📊 实验亮点

实验结果表明，RUNE在DOTA数据集上，通过引入更复杂的查询，性能优于现有的遥感视觉语言模型。RUNE在查询复杂度的检索鲁棒性（RRQC）和图像不确定性的检索鲁棒性（RRIU）方面均表现出色，证明了其在复杂查询和图像不确定性下的鲁棒性。此外，RUNE在洪水后卫星图像检索的用例中也取得了良好的效果，验证了其在实际应用中的潜力。

## 🎯 应用场景

RUNE在遥感图像分析领域具有广泛的应用前景，例如灾害监测（如洪水后的建筑物识别）、城市规划（如建筑物类型识别）、农业监测（如作物类型识别）等。通过结合文本查询和图像信息，RUNE可以帮助用户快速准确地检索到所需的遥感图像，为决策提供支持。未来，RUNE可以进一步扩展到其他领域，如医学图像分析、自动驾驶等。

## 📄 摘要（原文）

> Text-to-image retrieval in remote sensing (RS) has advanced rapidly with the rise of large vision-language models (LVLMs) tailored for aerial and satellite imagery, culminating in remote sensing large vision-language models (RS-LVLMS). However, limited explainability and poor handling of complex spatial relations remain key challenges for real-world use. To address these issues, we introduce RUNE (Reasoning Using Neurosymbolic Entities), an approach that combines Large Language Models (LLMs) with neurosymbolic AI to retrieve images by reasoning over the compatibility between detected entities and First-Order Logic (FOL) expressions derived from text queries. Unlike RS-LVLMs that rely on implicit joint embeddings, RUNE performs explicit reasoning, enhancing performance and interpretability. For scalability, we propose a logic decomposition strategy that operates on conditioned subsets of detected entities, guaranteeing shorter execution time compared to neural approaches. Rather than using foundation models for end-to-end retrieval, we leverage them only to generate FOL expressions, delegating reasoning to a neurosymbolic inference module. For evaluation we repurpose the DOTA dataset, originally designed for object detection, by augmenting it with more complex queries than in existing benchmarks. We show the LLM's effectiveness in text-to-logic translation and compare RUNE with state-of-the-art RS-LVLMs, demonstrating superior performance. We introduce two metrics, Retrieval Robustness to Query Complexity (RRQC) and Retrieval Robustness to Image Uncertainty (RRIU), which evaluate performance relative to query complexity and image uncertainty. RUNE outperforms joint-embedding models in complex RS retrieval tasks, offering gains in performance, robustness, and explainability. We show RUNE's potential for real-world RS applications through a use case on post-flood satellite image retrieval.

