---
layout: default
title: Mix-of-Language-Experts Architecture for Multilingual Programming
---

# Mix-of-Language-Experts Architecture for Multilingual Programming

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18923" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18923v1</a>
  <a href="https://arxiv.org/pdf/2506.18923.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18923v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18923v1', 'Mix-of-Language-Experts Architecture for Multilingual Programming')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Zong, Yuntian Deng, Pengyu Nie

**分类**: cs.PL, cs.CL, cs.SE

**发布日期**: 2025-06-18

**备注**: Accepted at LLM4Code @ ICSE 2025

---

## 💡 一句话要点

**提出MoLE架构以解决多语言编程中的效率与专业化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言编程` `大型语言模型` `LoRA` `知识共享` `模型微调`

## 📋 核心要点

1. 现有方法在支持多语言编程时面临效率与专业化之间的权衡，导致性能不足。
2. 论文提出MoLE架构，通过共享LoRA模块与语言特定LoRA模块的联合优化，实现知识共享与专业化。
3. 实验结果显示，MoLE在参数效率上优于独立的语言特定LoRA，同时在准确性上超越了单一共享LLM。

## 📝 摘要（中文）

大型语言模型（LLMs）在代码理解、生成和翻译等任务中展现了出色的能力。然而，支持多语言编程通常面临两种选择：一种是对单一LLM进行微调，虽然成本低但牺牲了语言特定的专业化；另一种是为每种编程语言微调独立的LLM，虽然可以实现专业化，但计算和存储成本高。本文提出了MoLE（Mix-of-Language-Experts）架构，旨在平衡多语言编程中的效率与专业化。MoLE由基础模型、共享的LoRA模块和一组语言特定的LoRA模块组成，这些模块在微调过程中共同优化，实现了知识共享与专业化。在推理阶段，MoLE会自动路由到与生成代码标记对应的语言特定LoRA模块。实验结果表明，MoLE在参数效率上优于独立的语言特定LoRA训练，同时在准确性上超越了为所有编程语言微调的单一共享LLM。

## 🔬 方法详解

**问题定义**：本文旨在解决多语言编程中效率与专业化的矛盾。现有方法要么牺牲语言特定的性能，要么导致计算与存储的高成本。

**核心思路**：MoLE架构通过结合共享LoRA模块与语言特定LoRA模块，允许在微调过程中实现知识共享，同时保持每种语言的专业化能力。这样的设计使得模型在推理时能够灵活选择最适合的模块。

**技术框架**：MoLE的整体架构包括一个基础模型、一个共享的LoRA模块和多个语言特定的LoRA模块。在微调阶段，这些模块共同优化，以实现最佳的性能。推理时，模型会根据生成的代码标记自动选择相应的语言特定模块。

**关键创新**：MoLE的主要创新在于其模块化设计，允许在保持参数效率的同时实现语言特定的专业化。这与传统的单一LLM或完全独立的LLM方法有本质区别。

**关键设计**：在设计中，LoRA模块的低秩适应性被用于减少参数量，同时确保模型能够有效地学习每种语言的特性。具体的损失函数和优化策略在微调过程中进行了精心设计，以促进不同模块之间的协同工作。

## 📊 实验亮点

实验结果表明，MoLE在参数效率上显著优于独立训练的语言特定LoRA，且在准确性上超越了为所有编程语言微调的单一共享LLM。具体而言，MoLE在多语言编程任务中的准确性提升幅度达到了XX%（具体数据未知）。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发工具、智能编程助手以及跨语言的代码生成与翻译系统。MoLE架构的高效性和专业化能力将极大提升开发者的生产力，并推动多语言编程的普及与发展。未来，该技术有望在更广泛的编程语言和应用场景中得到应用。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated impressive capabilities in aiding developers with tasks like code comprehension, generation, and translation. Supporting multilingual programming -- i.e., coding tasks across multiple programming languages -- typically requires either (1) finetuning a single LLM across all programming languages, which is cost-efficient but sacrifices language-specific specialization and performance, or (2) finetuning separate LLMs for each programming language, which allows for specialization but is computationally expensive and storage-intensive due to the duplication of parameters. This paper introduces MoLE (Mix-of-Language-Experts), a novel architecture that balances efficiency and specialization for multilingual programming. MoLE is composed of a base model, a shared LoRA (low-rank adaptation) module, and a collection of language-specific LoRA modules. These modules are jointly optimized during the finetuning process, enabling effective knowledge sharing and specialization across programming languages. During inference, MoLE automatically routes to the language-specific LoRA module corresponding to the programming language of the code token being generated. Our experiments demonstrate that MoLE achieves greater parameter efficiency compared to training separate language-specific LoRAs, while outperforming a single shared LLM finetuned for all programming languages in terms of accuracy.

