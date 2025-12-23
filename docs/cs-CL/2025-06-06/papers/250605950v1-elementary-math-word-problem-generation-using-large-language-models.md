---
layout: default
title: Elementary Math Word Problem Generation using Large Language Models
---

# Elementary Math Word Problem Generation using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05950" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05950v1</a>
  <a href="https://arxiv.org/pdf/2506.05950.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05950v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05950v1', 'Elementary Math Word Problem Generation using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nimesh Ariyarathne, Harshani Bandara, Yasith Heshan, Omega Gamage, Surangika Ranathunga, Dilan Nayanajith, Yutharsan Sivapalan, Gayathri Lihinikaduarachchi, Tharoosha Vihidun, Meenambika Chandirakumar, Sanujen Premakumar, Sanjula Gathsara

**分类**: cs.CL

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**基于大型语言模型的数学文字题生成系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学文字题` `大型语言模型` `自动生成` `教育技术` `深度学习`

## 📋 核心要点

1. 现有的数学文字题生成方法通常需要教师提供初始内容或额外信息，导致效率低下。
2. 本文提出的系统仅需输入题目数量、年级和题型，简化了生成过程，提高了自动化程度。
3. 实验结果表明，生成的数学文字题质量高，拼写和语法问题较少，但在满足特定年级和题型要求上仍有待改进。

## 📝 摘要（中文）

数学常被学生视为复杂的学科，导致考试失败率高。为了提高数学技能，提供样题至关重要。手动创建数学文字题耗时且需遵循语言规则。现有深度学习技术在生成数学文字题时，通常需要教师提供初始内容或额外信息。本文提出了一种基于大型语言模型的数学文字题生成系统，仅需输入所需题目数量、年级和题型。通过广泛实验，验证了生成题目的高质量，尽管在符合年级和题型要求方面仍存在挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决现有数学文字题生成方法的不足，特别是需要教师提供初始内容和额外信息的问题。

**核心思路**：提出一种基于大型语言模型的生成系统，用户只需输入所需题目数量、年级和题型，简化了生成过程。

**技术框架**：系统包括多个模块，首先接收用户输入，然后通过不同的提示策略和技术生成数学文字题，最后进行人类反馈的评估与优化。

**关键创新**：本研究的创新在于无需额外输入即可生成高质量的数学文字题，显著提高了生成的自动化程度。

**关键设计**：在实验中，采用了多种大型语言模型和提示策略，优化了生成的多样性，并引入人类反馈以提升模型性能。

## 📊 实验亮点

实验结果显示，生成的数学文字题在质量上表现优异，拼写和语法错误极少。尽管如此，模型在生成符合特定年级和题型要求的题目时仍面临挑战，需进一步优化。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、在线学习平台和智能辅导系统。通过自动生成高质量的数学文字题，可以有效减轻教师的负担，提高学生的学习效率，促进个性化学习。未来，该技术可能扩展到其他学科的题目生成，具有广泛的实际价值。

## 📄 摘要（原文）

> Mathematics is often perceived as a complex subject by students, leading to high failure rates in exams. To improve Mathematics skills, it is important to provide sample questions for students to practice problem-solving. Manually creating Math Word Problems (MWPs) is time consuming for tutors, because they have to type in natural language while adhering to grammar and spelling rules of the language. Existing Deep Learning techniques for MWP generation either require a tutor to provide the initial portion of the MWP, and/or additional information such as an equation. In this paper, we present an MWP generation system based on Large Language Models (LLMs) that overcome the need for additional input - the only input to our system is the number of MWPs needed, the grade and the type of question (e.g. addition, subtraction). Unlike the existing LLM-based solutions for MWP generation, we carried out an extensive set of experiments involving different LLMs, prompting strategies, techniques to improve the diversity of questions, as well as techniques that employ human feedback to improve LLM performance. Human and automated evaluations confirmed that the generated MWPs are high in quality, with minimal spelling and grammar issues. However, LLMs still struggle to generate questions that adhere to the specified grade and question type requirements.

