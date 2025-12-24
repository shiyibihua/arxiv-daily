---
layout: default
title: Test Set Quality in Multilingual LLM Evaluation
---

# Test Set Quality in Multilingual LLM Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02635" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02635v2</a>
  <a href="https://arxiv.org/pdf/2508.02635.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02635v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02635v2', 'Test Set Quality in Multilingual LLM Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chalamalasetti Kranti, Gabriel Bernier-Colborne, Yvan Gauthier, Sowmya Vajjala

**分类**: cs.CL

**发布日期**: 2025-08-04 (更新: 2025-11-13)

**备注**: to appear in the proceedings of Eval4NLP workshop at AACL 2025. Camera ready version

---

## 💡 一句话要点

**提出多语言LLM评估数据集质量分析方法以提升评估准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言评估` `数据集质量` `大型语言模型` `法语` `泰卢固语` `性能比较` `错误识别`

## 📋 核心要点

1. 现有多语言评估数据集的质量未受到足够重视，可能影响大型语言模型的评估结果。
2. 通过手动分析法语和泰卢固语的评估集，识别并修正数据集中的错误，以提高评估的准确性。
3. 实验结果显示，修订后的数据集在多个大型语言模型上的性能提升可达近10%，强调了数据集质量的重要性。

## 📝 摘要（中文）

近年来，多个多语言基准数据集以半自动方式开发，用于衡量大型语言模型的多语言能力。然而，尽管已有研究指出完全人工标注测试集中的错误，数据集质量问题仍未受到足够重视。本文手动分析了法语和泰卢固语的多语言评估集，识别出多个错误，并比较了不同大型语言模型在原始和修订版本数据集上的表现，发现两种语言的性能差异可达近10%。基于这些结果，作者主张测试集应被视为可变的，需定期检查和修订。最后，提出了针对数据集创建者和使用者的质量改进建议。

## 🔬 方法详解

**问题定义**：本文旨在解决多语言评估数据集质量不足的问题，现有方法未能有效识别和修正数据集中的错误，导致评估结果不准确。

**核心思路**：通过手动分析法语和泰卢固语的多语言评估集，识别数据集中的错误，并比较不同大型语言模型在原始和修订版本数据集上的表现，以验证数据集质量对评估结果的影响。

**技术框架**：研究流程包括数据集的手动分析、错误识别、数据集修订以及性能比较。主要模块包括数据集分析工具、错误分类标准和模型评估指标。

**关键创新**：最重要的创新在于提出了对多语言评估数据集进行系统性质量检查的方法，强调了数据集的可变性和定期修订的重要性，与现有方法相比，提供了更为全面的评估视角。

**关键设计**：在数据集分析中，采用了多种错误识别标准，并设计了修订流程，确保修订后的数据集能够更准确地反映模型性能。

## 📊 实验亮点

实验结果表明，修订后的数据集在多个大型语言模型上的性能提升显著，某些情况下性能差异接近10%。这一发现强调了数据集质量对模型评估的重要性，并为未来的数据集构建提供了实证依据。

## 🎯 应用场景

该研究的潜在应用领域包括多语言自然语言处理、机器翻译和跨语言信息检索等。通过提升评估数据集的质量，可以更准确地评估和比较不同大型语言模型的性能，从而推动多语言技术的发展和应用。未来，该方法可能影响数据集创建和使用的标准，促进更高质量的多语言模型研究。

## 📄 摘要（原文）

> Several multilingual benchmark datasets have been developed in a semi-automatic manner in the recent past to measure progress and understand the state-of-the-art in the multilingual capabilities of Large Language Models. However, there is not a lot of attention paid to the quality of the datasets themselves, despite the existence of previous work in identifying errors in even fully human-annotated test sets. In this paper, we manually analyze recent multilingual evaluation sets in two languages - French and Telugu, identifying several errors in the process. We compare the performance difference across several LLMs with the original and revised versions of the datasets and identify large differences (almost 10% in some cases) in both languages). Based on these results, we argue that test sets should not be considered immutable and should be revisited, checked for correctness, and potentially versioned. We end with some recommendations for both the dataset creators as well as consumers on addressing the dataset quality issues.

