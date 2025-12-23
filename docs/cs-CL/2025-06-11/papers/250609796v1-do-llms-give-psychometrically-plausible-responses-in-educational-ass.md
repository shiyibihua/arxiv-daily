---
layout: default
title: Do LLMs Give Psychometrically Plausible Responses in Educational Assessments?
---

# Do LLMs Give Psychometrically Plausible Responses in Educational Assessments?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09796" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09796v1</a>
  <a href="https://arxiv.org/pdf/2506.09796.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09796v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09796v1', 'Do LLMs Give Psychometrically Plausible Responses in Educational Assessments?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andreas Säuberli, Diego Frassinelli, Barbara Plank

**分类**: cs.CL

**发布日期**: 2025-06-11

**备注**: Accepted for publication at the 20th Workshop on Innovative Use of NLP for Building Educational Applications (BEA) at ACL 2025

---

## 💡 一句话要点

**评估大型语言模型在教育评估中的心理测量合理性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `教育评估` `心理测量` `温度缩放` `多项选择题` `阅读理解` `项目反应理论`

## 📋 核心要点

1. 现有的教育评估方法通常依赖大量人类参与者进行试点研究，效率低下且成本高昂。
2. 本文提出利用大型语言模型（LLMs）作为试点参与者，通过评估其回答的心理测量合理性来加速测试开发。
3. 研究发现，经过温度缩放校准后，LLMs的回答分布更接近人类，尤其在阅读理解题目上表现出更好的相关性。

## 📝 摘要（中文）

了解考生在教育评估中如何回答题目对于测试开发、评估题目质量和提高测试有效性至关重要。然而，这一过程通常需要大量人类参与者的试点研究。如果大型语言模型（LLMs）能够表现出类似人类的回答行为，则可以利用它们作为试点参与者，加速测试开发。本文评估了18个经过指令调优的LLMs在三个学科（阅读、美国历史和经济学）的多项选择题上的人类相似性或心理测量合理性。结果表明，尽管较大的模型过于自信，但经过温度缩放校准后，它们的回答分布更接近人类。此外，LLMs在阅读理解题目上的相关性优于其他学科，但总体相关性并不强，表明LLMs不应在零样本设置中用于教育评估的试点。

## 🔬 方法详解

**问题定义**：本文旨在解决教育评估中对考生回答行为的理解问题，现有方法依赖人类参与者进行试点研究，效率低且成本高。

**核心思路**：通过评估18个指令调优的LLMs在多项选择题上的回答，探索其是否能模拟人类的回答行为，从而作为试点参与者。

**技术框架**：研究基于经典测试理论和项目反应理论，使用两个公开数据集进行评估，涵盖阅读、美国历史和经济学三个学科。

**关键创新**：本文的创新在于将LLMs应用于教育评估的试点研究中，提出了温度缩放校准的方法以提高模型回答的心理测量合理性。

**关键设计**：研究中使用了温度缩放技术来调整模型的回答分布，确保其更接近人类的回答模式，同时评估了不同模型在各学科上的表现和相关性。

## 📊 实验亮点

实验结果显示，经过温度缩放校准的LLMs在回答分布上更接近人类，尤其在阅读理解题目上表现出更好的相关性。尽管较大的模型在自信度上存在过度现象，但整体相关性仍然较弱，表明在零样本设置中不适合用于教育评估的试点。

## 🎯 应用场景

该研究为教育评估领域提供了新的思路，利用大型语言模型作为试点参与者可以显著降低测试开发的时间和成本。未来，随着模型性能的提升，LLMs可能在教育评估中发挥更大的作用，帮助设计更有效的测试工具。

## 📄 摘要（原文）

> Knowing how test takers answer items in educational assessments is essential for test development, to evaluate item quality, and to improve test validity. However, this process usually requires extensive pilot studies with human participants. If large language models (LLMs) exhibit human-like response behavior to test items, this could open up the possibility of using them as pilot participants to accelerate test development. In this paper, we evaluate the human-likeness or psychometric plausibility of responses from 18 instruction-tuned LLMs with two publicly available datasets of multiple-choice test items across three subjects: reading, U.S. history, and economics. Our methodology builds on two theoretical frameworks from psychometrics which are commonly used in educational assessment, classical test theory and item response theory. The results show that while larger models are excessively confident, their response distributions can be more human-like when calibrated with temperature scaling. In addition, we find that LLMs tend to correlate better with humans in reading comprehension items compared to other subjects. However, the correlations are not very strong overall, indicating that LLMs should not be used for piloting educational assessments in a zero-shot setting.

