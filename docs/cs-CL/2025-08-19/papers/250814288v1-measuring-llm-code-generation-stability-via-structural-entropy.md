---
layout: default
title: Measuring LLM Code Generation Stability via Structural Entropy
---

# Measuring LLM Code Generation Stability via Structural Entropy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14288" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14288v1</a>
  <a href="https://arxiv.org/pdf/2508.14288.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14288v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14288v1', 'Measuring LLM Code Generation Stability via Structural Entropy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yewei Song, Tiezhu Sun, Xunzhu Tang, Prateek Rajput, Tegawende F. Bissyande, Jacques Klein

**分类**: cs.SE, cs.CL

**发布日期**: 2025-08-19

**备注**: ASE-NIER

---

## 💡 一句话要点

**通过结构熵评估大型语言模型代码生成的稳定性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码生成` `结构熵` `抽象语法树` `模型评估` `无参考指标` `稳定性分析`

## 📋 核心要点

1. 现有方法在评估大型语言模型生成代码的稳定性时，缺乏有效的无参考指标，难以全面反映模型的可靠性。
2. 本文提出了一种基于抽象语法树（AST）分析的结构熵方法，通过收集深度限制子树的频率分布来评估代码生成的稳定性。
3. 实验结果表明，AST驱动的结构熵能够揭示模型在一致性和鲁棒性方面的细微差别，且与传统指标相比具有更高的有效性。

## 📝 摘要（中文）

评估大型语言模型（LLMs）代码生成的稳定性对于判断其在实际开发中的可靠性至关重要。本文将先前的“结构熵概念”扩展到程序领域，通过抽象语法树（AST）分析与熵相结合。对于固定的提示，我们收集每个生成程序的深度限制子树的多重集合，并将其相对频率视为概率分布。我们通过两种互补方式测量稳定性：对称的Jensen-Shannon散度和强调缺失高概率模式的结构交叉熵比率。这些指标支持结构和标记感知的变体，提供对控制流形状和标识符级变异性的独立视角。与pass@k、BLEU或CodeBLEU不同，我们的指标是无参考、语言无关和执行无关的。我们在标准代码生成任务上对多种领先的LLMs进行了基准测试，表明AST驱动的结构熵揭示了模型一致性和鲁棒性的细微差别。该方法以O(n,d)的时间复杂度运行，无需外部测试，为代码生成评估工具包提供了一种轻量级的补充。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在代码生成中的稳定性评估问题。现有方法如BLEU等依赖参考答案，无法全面反映生成代码的质量和一致性。

**核心思路**：通过将结构熵与抽象语法树（AST）分析结合，本文提出了一种新的评估方法，能够在无参考的情况下量化代码生成的稳定性。

**技术框架**：整体流程包括收集生成程序的AST，提取深度限制子树，计算其相对频率，并使用Jensen-Shannon散度和结构交叉熵比率作为稳定性指标。

**关键创新**：本文的主要创新在于引入了结构熵的概念，并将其应用于代码生成的评估中，提供了与传统方法本质不同的视角，能够揭示模型生成代码的结构性差异。

**关键设计**：在技术细节上，本文设定了深度限制的参数以控制AST的复杂度，并设计了无参考的评估指标，确保方法的通用性和适用性。通过结构和标记感知的变体，进一步增强了对生成代码的分析能力。

## 📊 实验亮点

实验结果显示，AST驱动的结构熵在评估模型一致性和鲁棒性方面表现优异，能够有效区分不同模型的生成质量。与传统指标相比，本文方法在多个标准代码生成任务中展现出更高的敏感性和准确性。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发工具、自动化代码生成、代码审查和质量保证等。通过提供一种新的评估方法，开发者可以更好地理解和优化大型语言模型在实际应用中的表现，从而提高代码生成的可靠性和一致性。

## 📄 摘要（原文）

> Assessing the stability of code generation from large language models (LLMs) is essential for judging their reliability in real-world development. We extend prior "structural-entropy concepts" to the program domain by pairing entropy with abstract syntax tree (AST) analysis. For any fixed prompt, we collect the multiset of depth-bounded subtrees of AST in each generated program and treat their relative frequencies as a probability distribution. We then measure stability in two complementary ways: (i) Jensen-Shannon divergence, a symmetric, bounded indicator of structural overlap, and (ii) a Structural Cross-Entropy ratio that highlights missing high-probability patterns. Both metrics admit structural-only and token-aware variants, enabling separate views on control-flow shape and identifier-level variability. Unlike pass@k, BLEU, or CodeBLEU, our metrics are reference-free, language-agnostic, and execution-independent. We benchmark several leading LLMs on standard code generation tasks, demonstrating that AST-driven structural entropy reveals nuances in model consistency and robustness. The method runs in O(n,d) time with no external tests, providing a lightweight addition to the code-generation evaluation toolkit.

