---
layout: default
title: Multi-lingual Functional Evaluation for Large Language Models
---

# Multi-lingual Functional Evaluation for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20793" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20793v1</a>
  <a href="https://arxiv.org/pdf/2506.20793.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20793v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20793v1', 'Multi-lingual Functional Evaluation for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Victor Ojewale, Inioluwa Deborah Raji, Suresh Venkatasubramanian

**分类**: cs.CL

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出多语言功能评估基准以提升大语言模型的评估准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言评估` `大语言模型` `功能基准` `自然语言处理` `模型鲁棒性` `跨语言能力` `教育技术`

## 📋 核心要点

1. 现有的多语言评估方法主要依赖静态数据基准，无法全面反映模型的实际表现和鲁棒性。
2. 本文提出了跨语言功能基准，通过翻译现有的功能基准模板，涵盖多种语言以评估模型的多语言能力。
3. 实验结果表明，某些多语言基准在捕捉模型性能方面表现优于其他基准，性能下降幅度在15%至24%之间。

## 📝 摘要（中文）

大语言模型的多语言能力通常通过静态数据基准进行评估，如Belebele、M-MMLU和M-GSM。然而，这些评估未能充分理解模型在多语言环境中的实际表现和鲁棒性。为此，本文创建了多语言功能基准——跨语言小学数学符号（CL-GSM Symbolic）和跨语言指令跟随评估（CL-IFEval），通过将现有功能基准模板从英语翻译成法语、西班牙语、印地语、阿拉伯语和约鲁巴语等五种语言。结果显示，某些静态多语言基准比其他基准更能准确捕捉功能表现，模型在不同语言间的鲁棒性差异显著。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多语言评估方法的不足，特别是静态基准无法准确反映模型在多语言环境中的实际表现和鲁棒性。

**核心思路**：通过创建跨语言功能基准，翻译现有的功能基准模板，使其能够在多种语言中进行有效评估，从而更好地理解模型的多语言能力。

**技术框架**：整体架构包括两个主要模块：跨语言小学数学符号（CL-GSM Symbolic）和跨语言指令跟随评估（CL-IFEval），每个模块均基于翻译的功能基准模板进行设计。

**关键创新**：最重要的创新在于通过翻译现有基准模板，创建了新的多语言功能评估工具，能够更全面地评估模型在不同语言下的表现。

**关键设计**：在设计过程中，关注了翻译的准确性和功能基准的适用性，确保不同语言的评估结果具有可比性，且能够反映模型的真实性能。

## 📊 实验亮点

实验结果显示，CL-GSM Symbolic在英语、法语和西班牙语中的性能下降幅度分别为24%、17%和18%。同时，Belebele与CL-IFEval之间的性能下降幅度为15%至24%，而M-MMLU与CL-IFEval之间的下降幅度仅为0.5%至3%。这些结果表明不同基准在捕捉模型性能方面的差异。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、跨语言自然语言处理和多语言人工智能系统的开发。通过更准确的评估基准，研究者和开发者可以更好地理解和优化大语言模型在多语言环境中的表现，提升其实际应用价值。

## 📄 摘要（原文）

> Multi-lingual competence in large language models is often evaluated via static data benchmarks such as Belebele, M-MMLU and M-GSM. However, these evaluations often fail to provide an adequate understanding of the practical performance and robustness of models across multi-lingual settings. In response, we create multi-lingual functional benchmarks -- Cross-Lingual Grade School Math Symbolic (CL-GSM Symbolic) and Cross-Lingual Instruction-Following Eval (CL-IFEval)-- by translating existing functional benchmark templates from English to five additional languages that span the range of resources available for NLP: French, Spanish, Hindi, Arabic and Yoruba. Our results reveal that some static multi-lingual benchmarks capture functional performance much more closely than others (i.e. across models, there is a 24%, 17% and 18% decrease in performance between M-GSM and CL-GSM Symbolic in English, French and Spanish respectively; similarly there's a 15 - 24% performance drop across languages between Belebele and CL-IFEval, and only a 0.5% to 3% performance drop between M-MMLU and CL-IFEval). Similarly, we find that model robustness across languages varies significantly, with certain languages (eg. Arabic, English) being the most consistently well performing across evaluation iterations.

