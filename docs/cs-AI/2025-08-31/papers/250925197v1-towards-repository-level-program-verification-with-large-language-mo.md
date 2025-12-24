---
layout: default
title: Towards Repository-Level Program Verification with Large Language Models
---

# Towards Repository-Level Program Verification with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25197" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25197v1</a>
  <a href="https://arxiv.org/pdf/2509.25197.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25197v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25197v1', 'Towards Repository-Level Program Verification with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Si Cheng Zhong, Xujie Si

**分类**: cs.SE, cs.AI, cs.PL

**发布日期**: 2025-08-31

**备注**: Accepted to LMPL 2025

**DOI**: [10.1145/3759425.3763382](https://doi.org/10.1145/3759425.3763382)

---

## 💡 一句话要点

**提出RVBench与RagVerus以解决软件仓库级程序验证问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `程序验证` `大型语言模型` `软件仓库` `自动化验证` `开源项目` `多模块合成` `RVBench` `RagVerus`

## 📋 核心要点

1. 现有方法主要集中于孤立的函数级验证，未能有效处理跨模块依赖和全局上下文问题。
2. 本文提出RVBench作为仓库级验证基准，并引入RagVerus框架以实现多模块证明合成的自动化。
3. RagVerus在现有基准上证明通过率提升三倍，并在RVBench基准上实现27%的相对提升，展示了其有效性。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展在代码和证明生成方面展现出巨大潜力。然而，将自动化形式验证扩展到真实项目中，需要解决跨模块依赖和全局上下文等关键挑战，这些问题在现有LLM方法中往往被忽视。为系统性地探索和解决验证整个软件仓库的重大挑战，本文提出了RVBench，这是第一个专门为仓库级评估设计的验证基准，构建于四个多样且复杂的开源Verus项目之上。此外，本文还介绍了RagVerus，这是一个可扩展的框架，结合了检索增强生成与上下文感知提示，以自动化多模块仓库的证明合成。RagVerus在现有基准下的证明通过率提高了三倍，并在更具挑战性的RVBench基准上实现了27%的相对提升，展示了一种可扩展且样本高效的验证解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型在软件仓库级程序验证中的不足，尤其是跨模块依赖和全局上下文的处理问题。现有方法多集中于函数级验证，无法有效应对复杂的真实项目。

**核心思路**：论文提出RVBench作为新的验证基准，并设计RagVerus框架，通过检索增强生成和上下文感知提示，自动化多模块仓库的证明合成。这样的设计旨在提高验证的效率和准确性。

**技术框架**：RagVerus框架包含多个模块，首先是检索模块，用于获取相关的上下文信息；其次是生成模块，负责生成证明；最后是验证模块，确保生成的证明符合要求。整体流程通过上下文信息的引入，增强了生成的准确性。

**关键创新**：本文的主要创新在于引入了RVBench基准和RagVerus框架，前者为仓库级验证提供了标准化的评估工具，后者则通过上下文感知的生成方法显著提升了证明合成的效率。与现有方法相比，RagVerus在处理复杂依赖关系时表现出更高的灵活性和准确性。

**关键设计**：在RagVerus中，关键设计包括上下文检索的算法优化、生成模型的参数调整，以及损失函数的选择，确保生成的证明不仅准确且高效。

## 📊 实验亮点

在实验中，RagVerus在现有基准下的证明通过率提高了三倍，并在RVBench基准上实现了27%的相对提升，显示出其在处理复杂软件仓库验证任务中的优越性。这些结果表明，RagVerus在样本效率和可扩展性方面具有显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发中的自动化验证、开源项目的质量保证以及大型系统的安全性分析。通过提高程序验证的效率和准确性，RagVerus框架能够帮助开发者更快地识别和修复潜在的错误，从而提升软件的整体质量和可靠性。

## 📄 摘要（原文）

> Recent advancements in large language models (LLMs) suggest great promises in code and proof generations. However, scaling automated formal verification to real-world projects requires resolving cross-module dependencies and global contexts, which are crucial challenges overlooked by existing LLM-based methods with a special focus on targeting isolated, function-level verification tasks. To systematically explore and address the significant challenges of verifying entire software repositories, we introduce RVBench, the first verification benchmark explicitly designed for repository-level evaluation, constructed from four diverse and complex open-source Verus projects.
>   We further introduce RagVerus, an extensible framework that synergizes retrieval-augmented generation with context-aware prompting to automate proof synthesis for multi-module repositories. RagVerus triples proof pass rates on existing benchmarks under constrained model inference budgets, and achieves a 27% relative improvement on the more challenging RVBench benchmark, demonstrating a scalable and sample-efficient verification solution.

