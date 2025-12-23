---
layout: default
title: Enhancing Large Language Models through Structured Reasoning
---

# Enhancing Large Language Models through Structured Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20241" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20241v1</a>
  <a href="https://arxiv.org/pdf/2506.20241.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20241v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20241v1', 'Enhancing Large Language Models through Structured Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yubo Dong, Hehe Fan

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-25

**备注**: Preprint. Under review

---

## 💡 一句话要点

**通过结构化推理增强大型语言模型的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `结构化推理` `监督微调` `群体相对策略优化` `最大流算法` `最长公共子序列` `自然语言处理` `自动决策`

## 📋 核心要点

1. 现有大型语言模型在复杂推理任务中表现不佳，主要由于缺乏结构化知识表示，导致推理能力受限。
2. 本文提出通过显式注释推理步骤将非结构化数据转化为结构化格式，并利用监督微调训练LLMs，增强其推理能力。
3. 实验结果显示，微调后的模型在推理效果和计算复杂度上均有显著提升，验证了结构化推理的有效性。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在自然语言处理和自动决策方面取得了显著进展。然而，这些模型在处理复杂推理任务时仍面临困难，主要是因为它们依赖于隐式统计关系而缺乏结构化知识表示。受认知科学和神经符号人工智能的启发，本文提出了一种通过显式结构化推理增强LLMs的新方法。我们首先将非结构化数据转换为结构化格式，通过显式注释推理步骤来实现。然后，我们利用这一结构化数据集通过监督微调（SFT）训练LLMs。此外，我们还通过引入两种创新算法——最大流（MAX-Flow）和最长公共子序列（LCS），使用群体相对策略优化（GRPO）来增强LLMs的结构化推理能力。实验结果表明，微调后的DeepSeek-R1-Distill-Qwen-1.5B模型在各种场景下表现出简洁的推理能力和强大的性能，验证了结构化推理在LLMs中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在复杂推理任务中表现不佳的问题，现有方法主要依赖隐式统计关系，缺乏有效的结构化知识表示，导致推理能力受限。

**核心思路**：论文提出通过显式结构化推理来增强LLMs的能力，具体方法是将非结构化数据转化为结构化格式，并通过监督微调进行训练，以提高推理的准确性和效率。

**技术框架**：整体架构包括数据预处理、结构化数据集构建、监督微调训练和结构化推理能力增强四个主要模块。首先，进行数据的结构化处理，然后利用构建的结构化数据集对模型进行训练，最后通过群体相对策略优化进一步提升推理能力。

**关键创新**：本文的主要创新在于引入了MAX-Flow和LCS算法，通过群体相对策略优化（GRPO）来增强模型的结构化推理能力，这一方法显著提高了推理的有效性并降低了计算复杂度。

**关键设计**：在模型训练中，采用了特定的损失函数以优化推理步骤的准确性，同时在网络结构上进行了调整，以适应结构化数据的处理需求。

## 📊 实验亮点

实验结果表明，经过微调的DeepSeek-R1-Distill-Qwen-1.5B模型在推理任务中表现出显著提升，推理效果更加简洁，且在多种场景下的性能表现优于基线模型，验证了结构化推理的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、自动决策支持、复杂问题求解等。通过增强大型语言模型的推理能力，可以在更广泛的场景中实现更高效的自动化处理，提升人机交互的智能化水平，未来可能对教育、医疗、金融等行业产生深远影响。

## 📄 摘要（原文）

> Recent Large Language Models (LLMs) have significantly advanced natural language processing and automated decision-making. However, these models still encounter difficulties when performing complex reasoning tasks involving logical deduction and systematic planning, primarily due to their reliance on implicit statistical relationships without structured knowledge representation.Inspired by cognitive science and neurosymbolic AI, we introduce a novel approach to enhance LLMs through explicit structured reasoning. First, we convert unstructured data into structured formats by explicitly annotating reasoning steps. We then employ this structured dataset to train LLMs through Supervised Fine-Tuning (SFT). Additionally, we enhance the structured reasoning capabilities of LLMs using Group Relative Policy Optimization (GRPO), incorporating two innovative algorithms--MAX-Flow and Longest Common Subsequence (LCS)--which notably improve reasoning effectiveness and reduce computational complexity. Experimental results from fine-tuning a DeepSeek-R1-Distill-Qwen-1.5B model demonstrate concise reasoning, robust performance across various scenarios, and improved compatibility with optimization techniques, validating the efficacy of structured reasoning integration in LLMs.

