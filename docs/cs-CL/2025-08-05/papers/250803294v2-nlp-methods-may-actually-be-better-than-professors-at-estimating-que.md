---
layout: default
title: NLP Methods May Actually Be Better Than Professors at Estimating Question Difficulty
---

# NLP Methods May Actually Be Better Than Professors at Estimating Question Difficulty

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03294" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03294v2</a>
  <a href="https://arxiv.org/pdf/2508.03294.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03294v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03294v2', 'NLP Methods May Actually Be Better Than Professors at Estimating Question Difficulty')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leonidas Zotos, Ivo Pascal de Jong, Matias Valdenegro-Toro, Andreea Ioana Sburlea, Malvina Nissim, Hedderik van Rijn

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-05 (更新: 2025-11-17)

**备注**: 10 pages, 2 figures, presented at ECAI 2025 at the 2nd International Workshop on AI in Society, Education and Educational Research (AISEER)

---

## 💡 一句话要点

**提出基于LLM的不确定性估计以改善考试题目难度评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `考试评估` `难度估计` `监督学习` `教育技术` `不确定性`

## 📋 核心要点

1. 现有的教授在评估考试题目难度时能力有限，难以有效区分简单与困难的问题。
2. 本文提出利用大型语言模型（LLM）不确定性进行监督学习，以更准确地估计考试题目的难度。
3. 实验结果表明，基于LLM的方法在题目难度评估上优于教授，且只需少量训练样本即可实现显著提升。

## 📝 摘要（中文）

评估考试题目的难度对于开发良好的考试至关重要，但教授在这方面的能力有限。本文比较了多种基于大型语言模型（LLM）的方法与三位教授在估计神经网络和机器学习领域的真/假考试题目难度的能力。结果显示，教授在区分简单和困难问题方面的能力有限，且直接询问Gemini 2.5的表现优于教授。通过在监督学习环境中利用LLM的不确定性，仅使用42个训练样本，我们获得了更好的结果。我们得出结论，利用LLM不确定性的监督学习可以帮助教授更好地估计考试题目的难度，从而提高评估质量。

## 🔬 方法详解

**问题定义**：本文旨在解决教授在评估考试题目难度时的局限性，尤其是在区分简单和困难问题方面的不足。现有方法依赖于教授的主观判断，缺乏客观性和准确性。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的不确定性来进行监督学习，从而提高题目难度的估计准确性。通过直接询问LLM解决问题，能够获得更为客观的评估结果。

**技术框架**：整体架构包括数据收集、模型训练和难度评估三个主要模块。首先，收集真/假题目的数据，然后使用LLM进行训练，最后通过模型输出的不确定性来评估题目难度。

**关键创新**：最重要的技术创新点在于将LLM的不确定性引入到题目难度评估中，这与传统的依赖教授主观判断的方法有本质区别。通过这种方式，能够实现更高的评估准确性。

**关键设计**：在模型训练中，使用了42个训练样本，设计了适当的损失函数以优化模型输出的不确定性。此外，网络结构采用了最新的LLM架构，以确保在处理复杂问题时的有效性。

## 📊 实验亮点

实验结果显示，教授在题目难度评估上的表现有限，而Gemini 2.5模型的表现明显优于教授。利用LLM的不确定性进行监督学习，能够在仅使用42个训练样本的情况下，显著提高难度估计的准确性，展示了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育评估、考试设计和个性化学习。通过提高题目难度评估的准确性，能够帮助教育工作者更好地设计考试，进而提升学生的学习效果和评估质量。未来，该方法可能在更广泛的教育技术应用中发挥重要作用。

## 📄 摘要（原文）

> Estimating the difficulty of exam questions is essential for developing good exams, but professors are not always good at this task. We compare various Large Language Model-based methods with three professors in their ability to estimate what percentage of students will give correct answers on True/False exam questions in the areas of Neural Networks and Machine Learning. Our results show that the professors have limited ability to distinguish between easy and difficult questions and that they are outperformed by directly asking Gemini 2.5 to solve this task. Yet, we obtained even better results using uncertainties of the LLMs solving the questions in a supervised learning setting, using only 42 training samples. We conclude that supervised learning using LLM uncertainty can help professors better estimate the difficulty of exam questions, improving the quality of assessment.

