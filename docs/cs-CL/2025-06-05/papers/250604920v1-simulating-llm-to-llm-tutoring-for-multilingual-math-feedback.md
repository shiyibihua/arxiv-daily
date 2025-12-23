---
layout: default
title: Simulating LLM-to-LLM Tutoring for Multilingual Math Feedback
---

# Simulating LLM-to-LLM Tutoring for Multilingual Math Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04920" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04920v1</a>
  <a href="https://arxiv.org/pdf/2506.04920.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04920v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04920v1', 'Simulating LLM-to-LLM Tutoring for Multilingual Math Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-05

**备注**: Preprint, in submission

---

## 💡 一句话要点

**提出多语言LLM辅导模拟以提升数学反馈效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多语言教育` `数学推理` `反馈机制` `低资源语言` `教育工具` `跨语言学习`

## 📋 核心要点

1. 现有的LLM在多语言教育中的应用尚未充分探讨，特别是在数学推理任务中，缺乏有效的跨语言反馈机制。
2. 本文提出了一种模拟多语言辅导的框架，通过强模型生成反馈，弱模型模拟学生，探索不同语言间的互动效果。
3. 实验结果显示，多语言提示在低资源语言中显著提高学习效果，尤其是当反馈与学生母语一致时，学习收益更为明显。

## 📝 摘要（中文）

大型语言模型（LLMs）在生成英语的形成性反馈和教学提示方面表现出色，但其在不同语言中提供有效教学支持的能力，尤其是在数学推理任务中，尚未得到充分研究。本文首次大规模模拟了多语言的辅导-学生互动，强模型作为辅导者生成提示，而弱模型模拟学生。我们探索了352种实验设置，涵盖11种语言、四种先进的LLM和多种提示策略，以评估语言特定反馈是否能带来可测量的学习收益。研究结果表明，当反馈与学生的母语一致时，多语言提示能显著改善学习效果，尤其是在低资源语言中。这些发现为开发有效且包容的多语言LLM教育工具提供了实用见解。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多语言教育中，尤其是数学推理任务中的反馈有效性不足的问题。现有方法缺乏对不同语言的有效支持，导致学习效果不佳。

**核心思路**：通过模拟多语言的辅导-学生互动，利用强模型生成针对性的反馈，弱模型模拟学生的学习过程，以评估语言特定反馈的影响。

**技术框架**：整体架构包括强模型和弱模型的协作，强模型负责生成多语言提示，弱模型则根据提示进行学习反馈。实验设计涵盖352种设置，涉及11种语言和多种提示策略。

**关键创新**：本研究的创新点在于首次大规模模拟多语言LLM辅导，探索了不同语言间的反馈效果，尤其是在低资源语言中的应用潜力。

**关键设计**：实验中设置了多种参数，包括模型选择、提示策略和语言资源水平，采用不同的损失函数来优化反馈生成的质量。

## 📊 实验亮点

实验结果表明，多语言提示在低资源语言中显著提高学习效果，尤其是当反馈与学生的母语一致时，学习收益提升幅度可达显著水平。这一发现为多语言教育工具的设计提供了重要依据。

## 🎯 应用场景

该研究的潜在应用领域包括多语言教育工具的开发，尤其是在数学和科学教育中。通过有效的反馈机制，可以帮助不同语言背景的学生更好地理解和掌握知识，从而提升教育的公平性和包容性。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated the ability to generate formative feedback and instructional hints in English, making them increasingly relevant for AI-assisted education. However, their ability to provide effective instructional support across different languages, especially for mathematically grounded reasoning tasks, remains largely unexamined. In this work, we present the first large-scale simulation of multilingual tutor-student interactions using LLMs. A stronger model plays the role of the tutor, generating feedback in the form of hints, while a weaker model simulates the student. We explore 352 experimental settings across 11 typologically diverse languages, four state-of-the-art LLMs, and multiple prompting strategies to assess whether language-specific feedback leads to measurable learning gains. Our study examines how student input language, teacher feedback language, model choice, and language resource level jointly influence performance. Results show that multilingual hints can significantly improve learning outcomes, particularly in low-resource languages when feedback is aligned with the student's native language. These findings offer practical insights for developing multilingual, LLM-based educational tools that are both effective and inclusive.

