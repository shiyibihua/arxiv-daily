---
layout: default
title: Instruction-tuning Aligns LLMs to the Human Brain
---

# Instruction-tuning Aligns LLMs to the Human Brain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00575" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00575v2</a>
  <a href="https://arxiv.org/pdf/2312.00575.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00575v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00575v2', 'Instruction-tuning Aligns LLMs to the Human Brain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Khai Loong Aw, Syrielle Montariol, Badr AlKhamissi, Martin Schrimpf, Antoine Bosselut

**分类**: cs.CL

**发布日期**: 2023-12-01 (更新: 2024-08-09)

**备注**: COLM 2024

---

## 💡 一句话要点

**研究指令微调以提升大型语言模型与人脑的对齐性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `指令微调` `大型语言模型` `脑对齐` `行为对齐` `自然语言处理` `世界知识理解` `模型评估`

## 📋 核心要点

1. 现有方法未能证明指令微调能有效教会LLMs以人类方式处理语言，缺乏实证支持。
2. 论文通过分析LLM内部表征与人类神经活动的相似性，提出了脑对齐和行为对齐的评估方法。
3. 实验结果显示，指令微调提升了脑对齐约6%，但对行为对齐无显著影响，且模型大小与脑对齐高度相关。

## 📝 摘要（中文）

指令微调是一种广泛采用的微调方法，使大型语言模型（LLMs）生成更接近人类反应的输出。然而，尚无研究表明指令微调确实教会LLMs以类似人类的方式处理语言。本文通过脑对齐和行为对齐两种方式，探讨指令微调对LLM与人类语言处理机制的对齐效果。研究发现，指令微调通常提升了脑对齐（约6%），但对行为对齐没有显著影响。此外，模型大小和世界知识理解与脑对齐之间存在强正相关，表明指令微调不仅改善了世界知识的表征，也增强了与人脑的对齐。

## 🔬 方法详解

**问题定义**：本文旨在解决指令微调是否能有效教会大型语言模型以类似人类的方式处理语言的问题。现有方法缺乏对微调效果的实证分析，尤其是在与人类语言处理机制的对齐方面。

**核心思路**：研究通过评估LLM内部表征与人类语言系统神经活动的相似性，探讨指令微调对脑对齐和行为对齐的影响。通过比较25个原始和指令微调的LLMs，分析其在阅读任务中的表现。

**技术框架**：研究分为两个主要模块：脑对齐评估和行为对齐评估。脑对齐通过计算LLM内部表征与人类神经活动的相似性来实现，行为对齐则通过比较LLM和人类在阅读任务中的表现来评估。

**关键创新**：本研究的创新在于首次系统性地探讨指令微调对LLM与人类语言处理机制对齐的影响，揭示了模型大小和世界知识理解与脑对齐之间的强相关性。

**关键设计**：研究中使用了多个数据集，评估了不同模型的表现，特别关注模型大小、问题解决能力和世界知识理解等因素对脑对齐的影响。

## 📊 实验亮点

实验结果表明，指令微调显著提升了脑对齐约6%，而在行为对齐方面未见显著变化。模型大小与脑对齐之间的相关性高达0.95，世界知识理解的相关性为0.81，显示出指令微调在提升世界知识表征方面的潜力。

## 🎯 应用场景

该研究为大型语言模型的微调方法提供了新的视角，尤其是在提升模型与人类语言处理机制对齐方面。其结果可应用于自然语言处理、教育技术和人机交互等领域，推动更智能的语言理解系统的发展。

## 📄 摘要（原文）

> Instruction-tuning is a widely adopted finetuning method that enables large language models (LLMs) to generate output that more closely resembles human responses. However, no studies have shown that instruction-tuning actually teaches LLMs to process language in a similar manner as humans. We investigate the effect of instruction-tuning on aligning LLM and human language processing mechanisms in two ways: (1) brain alignment, the similarity of LLM internal representations to neural activity in the human language system, and (2) behavioral alignment, the similarity of LLM and human behavior on a reading task. We assess 25 vanilla and instruction-tuned LLMs on three datasets involving humans reading naturalistic stories and sentences, and find that instruction-tuning generally enhances brain alignment (~6%), but has no similar effect on behavioral alignment. To identify factors underlying this improvement in brain alignment, we compute correlations between brain alignment and various LLM properties, such as model size, problem-solving, and world knowledge understanding. Notably, we find a strong positive correlation between brain alignment and model size (r = 0.95), as well as performance on tasks requiring world knowledge (r = 0.81). Our results demonstrate that instruction-tuning LLMs improves both world knowledge representations and brain alignment, suggesting that the mechanisms that encode world knowledge in LLMs also improve representational alignment to the human brain.

