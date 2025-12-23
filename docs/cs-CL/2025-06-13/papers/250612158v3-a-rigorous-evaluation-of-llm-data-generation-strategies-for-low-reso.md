---
layout: default
title: A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages
---

# A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12158" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12158v3</a>
  <a href="https://arxiv.org/pdf/2506.12158.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12158v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12158v3', 'A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tatiana Anikina, Jan Cegin, Jakub Simko, Simon Ostermann

**分类**: cs.CL

**发布日期**: 2025-06-13 (更新: 2025-09-19)

**备注**: Accepted to EMNLP 2025 Main

---

## 💡 一句话要点

**系统评估低资源语言的LLM数据生成策略**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低资源语言` `大型语言模型` `数据生成` `自然语言处理` `合成数据` `模型评估` `智能提示`

## 📋 核心要点

1. 现有的生成策略在低资源语言环境中的有效性尚不明确，缺乏系统比较。
2. 论文提出通过系统评估多种生成策略及其组合，特别关注目标语言演示与LLM修订的结合。
3. 实验结果显示，战略组合能显著提高生成数据的质量，缩小与真实数据的性能差距。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地用于生成合成文本数据，以训练更小的专业模型。然而，针对低资源语言环境的各种生成策略的比较仍然缺乏。本文系统评估了11种类型多样语言中不同生成策略及其组合的性能，使用三项自然语言处理任务和四个开源LLM，评估生成数据与真实数据的下游模型性能。结果表明，特别是目标语言演示与LLM修订的战略组合，能显著缩小与真实数据的差距，某些情况下仅为5%。同时，智能提示技术可以减少大型LLM的优势，突显了在低资源场景中使用小型模型的高效生成策略。

## 🔬 方法详解

**问题定义**：本文旨在解决低资源语言生成策略的有效性缺乏比较的问题，现有方法在不同语言环境中的表现不一，难以选择最佳策略。

**核心思路**：通过系统评估多种生成策略及其组合，特别是目标语言的演示与LLM的自我修订，来提升低资源语言的合成数据质量。

**技术框架**：研究采用了四个开源LLM，结合三项NLP任务，评估生成数据与真实数据在下游模型中的表现，整体流程包括数据生成、模型训练与性能评估。

**关键创新**：最重要的创新点在于提出了目标语言演示与LLM修订的组合策略，显著提高了低资源语言的生成效果，区别于传统单一策略。

**关键设计**：在实验中，采用了多种提示策略和组合，具体参数设置和损失函数设计未详细披露，需进一步研究。

## 📊 实验亮点

实验结果表明，目标语言演示与LLM修订的组合策略在某些情况下将生成数据的性能与真实数据的差距缩小至5%。此外，智能提示技术的应用有效减少了大型LLM的优势，展示了在低资源场景中小型模型的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括低资源语言的自然语言处理任务，如机器翻译、文本生成和信息提取等。通过提高合成数据的质量，可以帮助小型模型在低资源环境中更有效地学习，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly used to generate synthetic textual data for training smaller specialized models. However, a comparison of various generation strategies for low-resource language settings is lacking. While various prompting strategies have been proposed, such as demonstrations, label-based summaries, and self-revision, their comparative effectiveness remains unclear, especially for low-resource languages. In this paper, we systematically evaluate the performance of these generation strategies and their combinations across 11 typologically diverse languages, including several extremely low-resource ones. Using three NLP tasks and four open-source LLMs, we assess downstream model performance on generated versus gold-standard data. Our results show that strategic combinations of generation methods, particularly target-language demonstrations with LLM-based revisions, yield strong performance, narrowing the gap with real data to as little as 5% in some settings. We also find that smart prompting techniques can reduce the advantage of larger LLMs, highlighting efficient generation strategies for synthetic data generation in low-resource scenarios with smaller models.

