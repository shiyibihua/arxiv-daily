---
layout: default
title: A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis
---

# A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.02938" class="toolbar-btn" target="_blank">📄 arXiv: 2507.02938v1</a>
  <a href="https://arxiv.org/pdf/2507.02938.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.02938v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.02938v1', 'A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiachen Liu, Ziheng Geng, Ran Cao, Lu Cheng, Paolo Bocchini, Minghui Cheng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-27

---

## 💡 一句话要点

**提出LLM驱动的代理以解决结构分析的可靠性与鲁棒性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `结构分析` `代码生成` `土木工程` `可靠性` `鲁棒性` `OpeeSeesPy` `链式思维`

## 📋 核心要点

1. 现有的LLM在结构分析中的应用缺乏定量可靠性和鲁棒性，无法满足工程需求。
2. 论文提出将结构分析视为代码生成任务，开发LLM驱动的代理以提高分析的准确性和可靠性。
3. 实验结果表明，该代理在基准数据集上实现了超过99.0%的准确率，显著提升了性能。

## 📝 摘要（中文）

大型语言模型（LLMs）在各种开放领域任务中展现出显著能力，但在土木工程等专业领域的应用仍然较少。本文通过评估和增强LLMs在梁的结构分析中的可靠性和鲁棒性，填补了这一空白。研究创建了一个包含八个梁分析问题的基准数据集，以测试Llama-3.3 70B Instruct模型。结果表明，尽管LLM对结构力学有定性理解，但在工程应用中缺乏定量的可靠性和鲁棒性。为了解决这些局限性，本文提出将结构分析重新框定为代码生成任务，并开发了一个LLM驱动的代理，该代理通过链式思维和少量示例提示生成准确的OpeeSeesPy代码，并自动执行代码以产生结构分析结果。实验结果显示，该代理在基准数据集上的准确率超过99.0%，在不同条件下表现出可靠和鲁棒的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在结构分析中的可靠性和鲁棒性不足的问题。现有方法在重复运行相同问题时输出准确性差，且在不同载荷和边界条件下表现不稳定。

**核心思路**：论文提出将结构分析重新定义为代码生成任务，通过生成OpeeSeesPy代码并执行，来提高分析的准确性和可靠性。这种方法利用了LLM的语言理解能力，结合代码生成的优势。

**技术框架**：整体架构包括数据集创建、LLM模型训练、代码生成和执行四个主要模块。首先创建包含八个梁分析问题的基准数据集，然后使用Llama-3.3 70B Instruct模型进行训练，接着生成代码并自动执行以获取分析结果。

**关键创新**：最重要的技术创新在于将结构分析任务转化为代码生成任务，利用链式思维和少量示例提示来提高生成代码的准确性。这一方法与传统的结构分析方法有本质区别，后者通常依赖于手动计算和经验。

**关键设计**：在设计中，使用了链式思维和少量示例提示来引导模型生成代码，确保生成的OpeeSeesPy代码的准确性。此外，实验中还进行了消融研究，表明完整示例和功能使用示例是提升性能的主要因素。

## 📊 实验亮点

实验结果显示，LLM驱动的代理在基准数据集上的准确率超过99.0%，在不同载荷和边界条件下表现出可靠和鲁棒的性能。与传统方法相比，该代理的性能显著提升，尤其是在复杂条件下的分析准确性。

## 🎯 应用场景

该研究的潜在应用领域包括土木工程、建筑设计和结构安全评估等。通过提高结构分析的可靠性和鲁棒性，能够为工程师提供更为精准的分析工具，进而提升工程设计的安全性和经济性。未来，该方法可能推动更多专业领域对大型语言模型的应用，促进跨学科的技术融合。

## 📄 摘要（原文）

> Large language models (LLMs) have exhibited remarkable capabilities across diverse open-domain tasks, yet their application in specialized domains such as civil engineering remains largely unexplored. This paper starts bridging this gap by evaluating and enhancing the reliability and robustness of LLMs in structural analysis of beams. Reliability is assessed through the accuracy of correct outputs under repetitive runs of the same problems, whereas robustness is evaluated via the performance across varying load and boundary conditions. A benchmark dataset, comprising eight beam analysis problems, is created to test the Llama-3.3 70B Instruct model. Results show that, despite a qualitative understanding of structural mechanics, the LLM lacks the quantitative reliability and robustness for engineering applications. To address these limitations, a shift is proposed that reframes the structural analysis as code generation tasks. Accordingly, an LLM-empowered agent is developed that (a) integrates chain-of-thought and few-shot prompting to generate accurate OpeeSeesPy code, and (b) automatically executes the code to produce structural analysis results. Experimental results demonstrate that the agent achieves accuracy exceeding 99.0% on the benchmark dataset, exhibiting reliable and robust performance across diverse conditions. Ablation studies highlight the complete example and function usage examples as the primary contributors to the agent's enhanced performance.

