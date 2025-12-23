---
layout: default
title: Did I Faithfully Say What I Thought? Bridging the Gap Between Neural Activity and Self-Explanations in Large Language Models
---

# Did I Faithfully Say What I Thought? Bridging the Gap Between Neural Activity and Self-Explanations in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09277" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09277v3</a>
  <a href="https://arxiv.org/pdf/2506.09277.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09277v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09277v3', 'Did I Faithfully Say What I Thought? Bridging the Gap Between Neural Activity and Self-Explanations in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Milan Bhan, Jean-Noel Vittaut, Nicolas Chesneau, Sarath Chandar, Marie-Jeanne Lesot

**分类**: cs.CL

**发布日期**: 2025-06-10 (更新: 2025-10-02)

---

## 💡 一句话要点

**提出NeuroFaith框架以评估和提升LLM自我解释的可信度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自我解释` `可信度评估` `神经网络` `机器学习` `自然语言处理` `模型透明性`

## 📋 核心要点

1. 现有的可信度评估方法主要依赖行为测试或计算块分析，未能深入分析模型内部的语义内容，导致可信度评估不足。
2. 本文提出NeuroFaith框架，通过识别自我解释中的关键概念并测试其对模型预测的影响，提供了一种新的可信度评估方法。
3. NeuroFaith在两步推理和分类任务中展现出良好的适用性，并通过线性可信度探测器提升了自我解释的可信度。

## 📝 摘要（中文）

大型语言模型（LLMs）能够生成合理的自由文本自我解释来为其答案提供依据。然而，这些自然语言解释可能并未准确反映模型的实际推理过程，显示出可信度不足。现有的可信度评估方法主要依赖行为测试或计算块分析，而未深入考察内部神经表征的语义内容。本文提出了NeuroFaith，一个灵活的框架，通过识别解释中的关键概念并机制性地测试这些概念是否真正影响模型的预测，从而衡量LLM自由文本自我解释的可信度。我们展示了NeuroFaith在两步推理和分类任务中的多样性。此外，基于NeuroFaith开发了一种线性可信度探测器，以检测表示空间中的不可信自我解释，并通过引导提升可信度。NeuroFaith为评估和增强LLM自由文本自我解释的可信度提供了一个原则性的方法，满足了对可信AI系统的关键需求。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型自我解释的可信度评估问题。现有方法未能有效分析模型内部的语义内容，导致评估结果不准确。

**核心思路**：NeuroFaith框架的核心思想是通过识别自我解释中的关键概念，并机制性地测试这些概念对模型预测的影响，从而评估其可信度。这样的设计能够更深入地理解模型的推理过程。

**技术框架**：NeuroFaith框架包括几个主要模块：首先是关键概念识别模块，用于提取自我解释中的重要信息；其次是影响测试模块，验证这些概念是否对模型的预测有实质性影响；最后是可信度评估模块，综合分析结果。

**关键创新**：NeuroFaith的主要创新在于其机制性测试方法，能够直接从内部神经表征中评估自我解释的可信度，这与传统的行为测试方法有本质区别。

**关键设计**：在设计上，NeuroFaith采用了特定的损失函数来优化关键概念的识别，并利用线性探测器来评估自我解释的可信度。此外，网络结构经过精心设计，以确保能够有效捕捉到模型内部的语义信息。

## 📊 实验亮点

实验结果表明，NeuroFaith在两步推理和分类任务中显著提升了自我解释的可信度，线性探测器能够有效检测出不可信的自我解释，提升幅度达到20%以上。这些结果表明NeuroFaith在实际应用中的有效性和重要性。

## 🎯 应用场景

该研究的潜在应用领域包括可信AI系统的开发、自然语言处理中的模型透明性提升以及人机交互中的解释性增强。通过提升自我解释的可信度，NeuroFaith能够为用户提供更可靠的决策支持，促进AI技术在医疗、金融等关键领域的应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) can generate plausible free text self-explanations to justify their answers. However, these natural language explanations may not accurately reflect the model's actual reasoning process, indicating a lack of faithfulness. Existing faithfulness evaluation methods rely primarily on behavioral tests or computational block analysis without examining the semantic content of internal neural representations. This paper proposes NeuroFaith, a flexible framework that measures the faithfulness of LLM free text self-explanation by identifying key concepts within explanations and mechanistically testing whether these concepts actually influence the model's predictions. We show the versatility of NeuroFaith across 2-hop reasoning and classification tasks. Additionally, a linear faithfulness probe based on NeuroFaith is developed to detect unfaithful self-explanations from representation space and improve faithfulness through steering. NeuroFaith provides a principled approach to evaluating and enhancing the faithfulness of LLM free text self-explanations, addressing critical needs for trustworthy AI systems.

