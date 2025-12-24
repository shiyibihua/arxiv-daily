---
layout: default
title: KG-Augmented Executable CoT for Mathematical Coding
---

# KG-Augmented Executable CoT for Mathematical Coding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04072" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04072v1</a>
  <a href="https://arxiv.org/pdf/2508.04072.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04072v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04072v1', 'KG-Augmented Executable CoT for Mathematical Coding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingyu Chen, Junxiu An, Jun Guo, Li Wang, Jingcai Guo

**分类**: cs.AI

**发布日期**: 2025-08-06

**备注**: 9 pages,2figures,6 tables

---

## 💡 一句话要点

**提出KG-Augmented Executable CoT以解决复杂数学推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `数学推理` `代码生成` `可执行代码` `图神经网络` `深度学习` `自然语言处理`

## 📋 核心要点

1. 现有的大型语言模型在处理复杂数学推理和代码生成时存在显著的局限性，导致生成的代码质量和推理准确性不足。
2. 本文提出的KGA-ECoT框架通过知识图谱和可执行代码的结合，旨在提升代码生成的准确性和数学推理的有效性。
3. 实验结果显示，KGA-ECoT在多个数学推理基准上表现优异，准确率提升幅度达到几到十多个百分点，验证了其有效性。

## 📝 摘要（中文）

近年来，大型语言模型在自然语言处理任务中表现出色，但在复杂推理任务如数学推理和代码生成方面面临重大挑战。为了解决这些局限性，本文提出了KG-Augmented Executable Chain-of-Thought（KGA-ECoT）框架，通过知识图谱增强代码生成，并通过可执行代码改善数学推理。KGA-ECoT将问题分解为结构化任务图，利用高效的GraphRAG从数学库中精确检索知识，并生成可验证的代码以确保计算准确性。在多个数学推理基准上的评估表明，KGA-ECoT显著优于现有提示方法，准确率提升幅度从几个百分点到十多个百分点不等。进一步分析确认了GraphRAG在提升代码质量和外部代码执行确保精度中的关键作用。这些发现共同确立了KGA-ECoT作为复杂数学推理任务的强大且高度可推广的框架。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在复杂数学推理和代码生成中的不足，现有方法在准确性和可验证性方面存在显著挑战。

**核心思路**：KGA-ECoT框架通过将问题分解为结构化任务图，结合知识图谱和可执行代码，提升推理和生成的准确性与可靠性。

**技术框架**：该框架主要包括三个模块：结构化任务图的构建、GraphRAG的知识检索和可执行代码的生成，形成一个闭环的推理与生成流程。

**关键创新**：KGA-ECoT的核心创新在于引入GraphRAG进行高效的知识检索，并通过可执行代码确保数学推理的准确性，这与传统的提示方法有本质区别。

**关键设计**：在设计上，KGA-ECoT采用了特定的参数设置以优化知识检索的效率，并设计了损失函数以确保生成代码的可验证性和准确性。具体的网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，KGA-ECoT在多个数学推理基准上显著优于现有提示方法，准确率提升幅度从几个百分点到十多个百分点，验证了GraphRAG在提升代码质量和执行精度中的关键作用。

## 🎯 应用场景

该研究的潜在应用领域包括教育、科学计算和软件开发等，能够为复杂数学问题的自动求解和代码生成提供有效支持。未来，KGA-ECoT可能在智能助手、自动化编程和在线教育平台中发挥重要作用，推动相关领域的发展。

## 📄 摘要（原文）

> In recent years, large language models (LLMs) have excelled in natural language processing tasks but face significant challenges in complex reasoning tasks such as mathematical reasoning and code generation. To address these limitations, we propose KG-Augmented Executable Chain-of-Thought (KGA-ECoT), a novel framework that enhances code generation through knowledge graphs and improves mathematical reasoning via executable code. KGA-ECoT decomposes problems into a Structured Task Graph, leverages efficient GraphRAG for precise knowledge retrieval from mathematical libraries, and generates verifiable code to ensure computational accuracy. Evaluations on multiple mathematical reasoning benchmarks demonstrate that KGA-ECoT significantly outperforms existing prompting methods, achieving absolute accuracy improvements ranging from several to over ten percentage points. Further analysis confirms the critical roles of GraphRAG in enhancing code quality and external code execution in ensuring precision. These findings collectively establish KGA-ECoT as a robust and highly generalizable framework for complex mathematical reasoning tasks.

