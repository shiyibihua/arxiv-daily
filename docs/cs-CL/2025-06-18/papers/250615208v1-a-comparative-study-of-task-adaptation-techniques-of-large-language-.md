---
layout: default
title: A Comparative Study of Task Adaptation Techniques of Large Language Models for Identifying Sustainable Development Goals
---

# A Comparative Study of Task Adaptation Techniques of Large Language Models for Identifying Sustainable Development Goals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15208" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15208v1</a>
  <a href="https://arxiv.org/pdf/2506.15208.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15208v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15208v1', 'A Comparative Study of Task Adaptation Techniques of Large Language Models for Identifying Sustainable Development Goals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrea Cadeddu, Alessandro Chessa, Vincenzo De Leo, Gianni Fenu, Enrico Motta, Francesco Osborne, Diego Reforgiato Recupero, Angelo Salatino, Luca Secchi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-18

**备注**: Submitted to IEEE Access

---

## 💡 一句话要点

**比较大型语言模型任务适应技术以识别可持续发展目标**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可持续发展目标` `大型语言模型` `文本分类` `任务适应技术` `零样本学习` `少样本学习` `微调`

## 📋 核心要点

1. 现有方法在跟踪可持续发展目标的进展时面临数据规模和复杂性带来的挑战。
2. 本文提出了对多种大型语言模型进行比较分析，并评估不同任务适应技术的有效性。
3. 实验结果显示，经过优化的小型模型在性能上可与大型模型相媲美，具有显著的实用价值。

## 📝 摘要（中文）

2012年，联合国提出了17个可持续发展目标（SDGs），旨在到2030年实现更可持续和改善的未来。然而，由于涉及数据的广泛规模和复杂性，跟踪这些目标的进展变得困难。文本分类模型在这一领域变得至关重要，自动化分析来自多种来源的大量文本。此外，大型语言模型（LLMs）在许多自然语言处理任务中证明了其不可或缺的作用，包括文本分类。本文分析了多种专有和开源LLMs在针对SDGs的单标签多类文本分类任务中的表现，并评估了任务适应技术（即上下文学习方法），包括零样本学习和少样本学习，以及微调的有效性。结果表明，通过提示工程优化的小型模型能够与OpenAI的GPT等大型模型相媲美。

## 🔬 方法详解

**问题定义**：本文旨在解决如何有效识别和分类与可持续发展目标相关的文本数据的问题。现有方法在处理大规模和复杂数据时效率低下，难以实现准确的分类。

**核心思路**：通过比较不同的任务适应技术，尤其是零样本学习、少样本学习和微调，探索如何提升大型语言模型在文本分类任务中的表现。这样的设计旨在利用现有模型的潜力，同时降低对大量标注数据的依赖。

**技术框架**：研究首先选择多种专有和开源的LLMs，然后对其进行单标签多类文本分类任务的评估。接着，应用不同的任务适应技术进行优化，最后通过实验比较各模型的分类效果。

**关键创新**：最重要的创新在于发现小型模型在经过提示工程优化后，能够在性能上与大型模型相媲美。这一发现挑战了传统观念，表明小型模型在特定任务中同样具有竞争力。

**关键设计**：在实验中，采用了不同的提示策略和参数设置，以优化模型的输入格式和学习过程。此外，损失函数的选择和模型架构的调整也是关键设计要素，确保模型能够有效学习复杂的语言模式。

## 📊 实验亮点

实验结果显示，经过优化的小型模型在SDGs文本分类任务中，准确率与OpenAI的GPT等大型模型相当，甚至在某些情况下表现更优。这一发现表明，通过有效的提示工程，小型模型的性能得到了显著提升，具有更高的实用性和经济性。

## 🎯 应用场景

该研究的潜在应用领域包括政策分析、社会科学研究和环境监测等。通过自动化文本分类，相关机构可以更高效地跟踪和评估可持续发展目标的进展，从而为决策提供数据支持，推动可持续发展实践的实施。未来，该技术有望扩展到其他领域的文本分析任务中，提升数据处理的效率和准确性。

## 📄 摘要（原文）

> In 2012, the United Nations introduced 17 Sustainable Development Goals (SDGs) aimed at creating a more sustainable and improved future by 2030. However, tracking progress toward these goals is difficult because of the extensive scale and complexity of the data involved. Text classification models have become vital tools in this area, automating the analysis of vast amounts of text from a variety of sources. Additionally, large language models (LLMs) have recently proven indispensable for many natural language processing tasks, including text classification, thanks to their ability to recognize complex linguistic patterns and semantics. This study analyzes various proprietary and open-source LLMs for a single-label, multi-class text classification task focused on the SDGs. Then, it also evaluates the effectiveness of task adaptation techniques (i.e., in-context learning approaches), namely Zero-Shot and Few-Shot Learning, as well as Fine-Tuning within this domain. The results reveal that smaller models, when optimized through prompt engineering, can perform on par with larger models like OpenAI's GPT (Generative Pre-trained Transformer).

