---
layout: default
title: Modelling and Classifying the Components of a Literature Review
---

# Modelling and Classifying the Components of a Literature Review

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04337" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04337v1</a>
  <a href="https://arxiv.org/pdf/2508.04337.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04337v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04337v1', 'Modelling and Classifying the Components of a Literature Review')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Francisco Bolaños, Angelo Salatino, Francesco Osborne, Enrico Motta

**分类**: cs.CL, cs.AI, cs.HC, cs.IR

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出新注释方案以提升文献综述生成质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文献综述` `修辞角色` `大型语言模型` `注释方案` `文本分析` `自动标注` `机器学习`

## 📋 核心要点

1. 现有文献分析方法缺乏有效的注释方案，导致生成的文献综述质量不高。
2. 本文提出了一种专门为文献综述生成设计的新注释方案，并评估了多种LLMs在该方案下的分类能力。
3. 实验结果表明，经过微调的LLMs在修辞角色分类任务上表现出色，某些轻量级开源模型也取得了良好效果。

## 📝 摘要（中文）

以往研究表明，AI方法在分析科学文献时，通过根据修辞角色对句子进行注释能显著提升效果，如研究空白、结果、局限性等。本文提出了一种新颖的注释方案，旨在支持文献综述的生成，并对多种前沿大型语言模型（LLMs）在该注释方案下的修辞角色分类进行了全面评估。我们还推出了Sci-Sentence基准，包含700个专家手动注释的句子和2240个自动标注的句子。实验结果显示，经过高质量数据微调的LLMs在此任务上表现优异，F1得分超过96%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有文献分析方法中缺乏有效注释方案的问题，导致文献综述生成质量低下。现有方法在识别句子修辞角色方面存在不足，限制了AI在文献分析中的应用。

**核心思路**：论文提出了一种新颖的注释方案，专门针对文献综述生成设计，旨在通过清晰的修辞角色分类来提升文献分析的准确性和效率。通过对多种LLMs的评估，探索其在这一新注释方案下的表现。

**技术框架**：整体架构包括两个主要模块：1) 新注释方案的设计，明确修辞角色及其分类；2) 对37种LLMs的评估，采用零样本学习和微调方法进行性能测试。

**关键创新**：最重要的创新点在于提出了一个专门针对文献综述生成的注释方案，并通过Sci-Sentence基准进行全面评估，填补了现有研究的空白。与传统方法相比，该方案提供了更细致的修辞角色分类。

**关键设计**：在实验中，使用了700个手动注释的句子和2240个自动标注的句子，评估了不同模型的性能，特别关注了数据的质量和多样性对模型表现的影响。

## 📊 实验亮点

实验结果显示，经过高质量数据微调的LLMs在修辞角色分类任务上表现优异，F1得分超过96%。大型模型如GPT-4o表现最佳，但一些轻量级开源模型也展现了出色的性能。此外，使用LLMs生成的半合成示例丰富训练数据，显著提升了小型编码器和多个开源解码器模型的表现。

## 🎯 应用场景

该研究的潜在应用领域包括学术研究、文献综述自动生成工具以及科学知识管理系统。通过提升文献分析的准确性和效率，能够帮助研究人员更快地获取相关信息，推动科学研究的进展。未来，该方法还可能扩展到其他领域的文本分析任务中。

## 📄 摘要（原文）

> Previous work has demonstrated that AI methods for analysing scientific literature benefit significantly from annotating sentences in papers according to their rhetorical roles, such as research gaps, results, limitations, extensions of existing methodologies, and others. Such representations also have the potential to support the development of a new generation of systems capable of producing high-quality literature reviews. However, achieving this goal requires the definition of a relevant annotation schema and effective strategies for large-scale annotation of the literature. This paper addresses these challenges by 1) introducing a novel annotation schema specifically designed to support literature review generation and 2) conducting a comprehensive evaluation of a wide range of state-of-the-art large language models (LLMs) in classifying rhetorical roles according to this schema. To this end, we also present Sci-Sentence, a novel multidisciplinary benchmark comprising 700 sentences manually annotated by domain experts and 2,240 sentences automatically labelled using LLMs. We evaluate 37 LLMs on this benchmark, spanning diverse model families and sizes, using both zero-shot learning and fine-tuning approaches. The experiments yield several novel insights that advance the state of the art in this challenging domain. First, the current generation of LLMs performs remarkably well on this task when fine-tuned on high-quality data, achieving performance levels above 96\% F1. Second, while large proprietary models like GPT-4o achieve the best results, some lightweight open-source alternatives also demonstrate excellent performance. Finally, enriching the training data with semi-synthetic examples generated by LLMs proves beneficial, enabling small encoders to achieve robust results and significantly enhancing the performance of several open decoder models.

