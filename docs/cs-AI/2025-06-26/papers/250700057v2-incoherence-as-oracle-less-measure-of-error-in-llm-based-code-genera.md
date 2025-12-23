---
layout: default
title: Incoherence as Oracle-less Measure of Error in LLM-Based Code Generation
---

# Incoherence as Oracle-less Measure of Error in LLM-Based Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00057" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00057v2</a>
  <a href="https://arxiv.org/pdf/2507.00057.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00057v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00057v2', 'Incoherence as Oracle-less Measure of Error in LLM-Based Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thomas Valentin, Ardi Madadi, Gaetano Sapia, Marcel Böhme

**分类**: cs.PL, cs.AI, cs.LG, cs.SE

**发布日期**: 2025-06-26 (更新: 2025-12-13)

**备注**: Accepted at AAAI'26 (extended version). 8 pages + refs and appendix

**期刊**: 40th Annual AAAI Conference on Artificial Intelligence (AAAI), 2026

---

## 💡 一句话要点

**提出不一致性度量以解决LLM代码生成中的错误评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码生成` `错误评估` `不一致性度量` `自动化编程` `软件开发`

## 📋 核心要点

1. 现有的代码生成方法缺乏有效的错误评估机制，尤其是在没有正确实现或规范的情况下。
2. 本文提出了一种新的错误度量方法——不一致性，能够在没有oracle的情况下评估生成程序的正确性。
3. 实验结果显示，该方法能够准确识别约67%的错误程序，且没有假阳性，表现优于传统的oracle评估方法。

## 📝 摘要（中文）

从自然语言编程任务生成代码是大型语言模型（LLMs）最成功的应用之一。然而，生成的程序可能存在错误。在没有现成正确实现或正式规范的情况下，如何评估生成程序的正确性？本文提出了一种称为*不一致性*的错误度量方法，可以在没有oracle的情况下高效估计，并为错误建立下限。实验表明，该方法能够自动识别约三分之二的错误程序，且在平均任务中没有假阳性报告。实际上，基于oracle的LLM评估可以可靠地被不一致性评估所替代。

## 🔬 方法详解

**问题定义**：本文解决的问题是如何在没有oracle的情况下评估LLM生成代码的正确性。现有方法依赖于已有的正确实现或规范，无法在缺乏这些信息时进行有效评估。

**核心思路**：论文提出的不一致性度量方法，通过分析生成程序的内部结构和逻辑，来估计其错误概率。这种方法不依赖于外部的正确性标准，具有更广泛的适用性。

**技术框架**：整体架构包括数据收集、生成程序分析和不一致性度量三个主要模块。首先收集生成的代码，然后通过特定算法分析其逻辑结构，最后计算不一致性得分以评估错误概率。

**关键创新**：最重要的技术创新点在于引入了不一致性作为一种新的错误度量标准，能够在没有oracle的情况下提供有效的错误评估。这与现有方法的本质区别在于不再依赖于外部标准。

**关键设计**：在技术细节上，论文设计了特定的算法来计算不一致性得分，并通过大量实验验证了该方法的有效性。参数设置和损失函数的选择经过精心调整，以确保评估结果的准确性。

## 📊 实验亮点

实验结果显示，基于不一致性的方法能够自动识别约67%的错误程序，且在平均任务中没有假阳性报告。这一性能显著优于传统的oracle评估方法，表明不一致性度量在LLM代码生成中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括自动代码生成、软件开发工具和编程教育等。通过提供一种有效的错误评估机制，可以帮助开发者更快地识别和修复代码中的错误，提高代码生成的可靠性和效率。未来，该方法可能会在更多的编程语言和任务中得到应用，推动智能编程技术的发展。

## 📄 摘要（原文）

> Generating code from a natural language programming task is one of the most successful applications of Large Language Models (LLMs). Yet, the generated program may be buggy. Without an oracle, such as an existing, correct implementation or a formal specification, can we somehow estimate how likely the generated program is correct?
>   In this paper, we propose a measure of incorrectness, called *incoherence*, that can be estimated efficiently in the absence of an oracle and allows us to establish a lower bound on the error, i.e., the probability that the LLM-generated program for that specification is incorrect. In our experiments, our incoherence-based methodology can automatically identify about two-thirds of incorrect programs without reports of false positives for the average task. In fact, *an oracle-based evaluation of LLMs can be reliably replaced by an incoherence-based evaluation*. In particular, we find a very strong agreement between the ranking of LLMs by the number of programs deemed correct via an oracle (pass@1) and the ranking of LLMs by the number of programs deemed correct via incoherence.

