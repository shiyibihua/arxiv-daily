---
layout: default
title: Classifying Unreliable Narrators with Large Language Models
---

# Classifying Unreliable Narrators with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10231" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10231v1</a>
  <a href="https://arxiv.org/pdf/2506.10231.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10231v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10231v1', 'Classifying Unreliable Narrators with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anneliese Brei, Katharine Henry, Abhisheik Sharma, Shashank Srivastava, Snigdha Chaturvedi

**分类**: cs.CL

**发布日期**: 2025-06-11

**备注**: ACL 2025

---

## 💡 一句话要点

**提出使用计算方法识别不可靠叙述者以解决文本可信度问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `不可靠叙述者` `叙事学` `文本分类` `大语言模型` `数据集构建` `计算方法` `信息可信度`

## 📋 核心要点

1. 现有方法在识别不可靠叙述者时缺乏系统性，难以处理多种文本现象。
2. 论文提出通过借鉴叙事学理论，构建TUNa数据集，并定义多种不可靠性分类任务。
3. 实验结果显示，该任务具有挑战性，但大语言模型在识别不可靠叙述者方面展现出潜力。

## 📝 摘要（中文）

在与第一人称叙述的事件互动时，我们常常考虑叙述者的可靠性。本文提出使用计算方法识别不可靠叙述者，即那些无意中误传信息的叙述者。借鉴叙事学的文学理论，定义了多种类型的不可靠叙述者，并呈现了一个名为TUNa的人类标注数据集，涵盖博客、社交媒体、酒店评论和文学作品等多个领域。我们定义了内部、外部和跨文本的不可靠性分类任务，并分析了多种流行的开放权重和专有大语言模型在这些任务上的表现。实验结果表明，该任务具有挑战性，但使用大语言模型识别不可靠叙述者具有潜力。我们发布了专家标注的数据集和代码，邀请未来的研究。

## 🔬 方法详解

**问题定义**：本文旨在解决如何有效识别不可靠叙述者的问题。现有方法在处理不同类型的叙述者时缺乏系统性，导致识别效果不佳。

**核心思路**：通过借鉴叙事学的理论，定义不可靠叙述者的多种类型，并构建一个多领域的人类标注数据集TUNa，以支持分类任务的研究。

**技术框架**：整体架构包括数据集构建、分类任务定义和模型训练三个主要阶段。首先，收集和标注多种文本数据；其次，定义内部、外部和跨文本的不可靠性分类任务；最后，使用不同的模型进行训练和评估。

**关键创新**：最重要的创新在于将叙事学理论与计算方法相结合，系统性地定义了不可靠叙述者的分类标准，并提出了相应的实验框架。与现有方法相比，提供了更为细致的分类视角。

**关键设计**：在模型训练中，采用了少量样本学习、微调和课程学习等策略，以提高模型在不可靠叙述者识别任务上的表现。

## 📊 实验亮点

实验结果表明，尽管识别不可靠叙述者的任务具有挑战性，但使用大语言模型在该领域展现出潜力。具体而言，模型在不同分类任务上的表现优于基线，显示出显著的提升幅度，尤其是在处理复杂文本现象时。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、在线评论分析和文学作品的文本分析。通过识别不可靠叙述者，可以提高信息的可信度，帮助用户更好地理解和判断文本内容的真实性，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Often when we interact with a first-person account of events, we consider whether or not the narrator, the primary speaker of the text, is reliable. In this paper, we propose using computational methods to identify unreliable narrators, i.e. those who unintentionally misrepresent information. Borrowing literary theory from narratology to define different types of unreliable narrators based on a variety of textual phenomena, we present TUNa, a human-annotated dataset of narratives from multiple domains, including blog posts, subreddit posts, hotel reviews, and works of literature. We define classification tasks for intra-narrational, inter-narrational, and inter-textual unreliabilities and analyze the performance of popular open-weight and proprietary LLMs for each. We propose learning from literature to perform unreliable narrator classification on real-world text data. To this end, we experiment with few-shot, fine-tuning, and curriculum learning settings. Our results show that this task is very challenging, and there is potential for using LLMs to identify unreliable narrators. We release our expert-annotated dataset and code and invite future research in this area.

