---
layout: default
title: Benchmarking Large Language Models on Homework Assessment in Circuit Analysis
---

# Benchmarking Large Language Models on Homework Assessment in Circuit Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06390" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06390v1</a>
  <a href="https://arxiv.org/pdf/2506.06390.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06390v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06390v1', 'Benchmarking Large Language Models on Homework Assessment in Circuit Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liangliang Chen, Zhihao Qin, Yiming Guo, Jacqueline Rohde, Ying Zhang

**分类**: cs.CY, cs.AI

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**基于大语言模型的电路分析作业评估基准研究**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `电路分析` `作业评估` `工程教育` `数据集构建` `评估指标` `个性化辅导`

## 📋 核心要点

1. 现有方法在电路分析作业评估中存在准确性不足和可靠性问题，可能误导学生。
2. 论文提出通过构建包含真实学生解和参考解的数据集，利用LLMs评估作业，设计了针对五个评估指标的提示模板。
3. 实验结果显示，GPT-4o和Llama 3 70B在评估指标上显著优于GPT-3.5 Turbo，提供了可靠的基准和洞察。

## 📝 摘要（中文）

大语言模型（LLMs）在代码开发、机器人、金融和教育等多个领域具有革命性潜力。本文探讨了如何在工程教育中利用LLMs，特别是评估本科电路分析课程的作业能力。我们开发了一个新数据集，包含官方参考解和真实学生解，并将其转换为LaTeX格式，以克服现有LLMs在图像识别方面的局限性。通过设计提示模板，我们测试了学生解的五个评估指标。结果表明，GPT-4o和Llama 3 70B在所有指标上表现显著优于GPT-3.5 Turbo，并且各自具有不同的优势。此外，我们还探讨了当前LLMs在电路分析中的局限性，为未来开发可靠的个性化辅导系统奠定了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在电路分析作业评估中的准确性和可靠性问题。现有方法在图像识别和评估标准上存在局限，可能导致评估结果不准确。

**核心思路**：通过构建一个包含官方参考解和真实学生解的数据集，并将其转换为LaTeX格式，论文设计了一个提示模板来评估学生解的完整性、方法、最终答案、算术错误和单位等五个指标。

**技术框架**：整体架构包括数据集构建、提示模板设计和评估指标测试三个主要模块。数据集通过真实案例和参考解的结合，确保了评估的全面性和准确性。

**关键创新**：最重要的技术创新在于将学生解转化为LaTeX格式，以克服现有LLMs在图像识别方面的不足，并通过五个具体指标进行全面评估，提供了更为细致的反馈。

**关键设计**：在提示模板中，设置了针对每个评估指标的具体要求，并通过对比不同LLMs的表现，分析了各自的优势和局限性。

## 📊 实验亮点

实验结果显示，GPT-4o和Llama 3 70B在完整性、方法、最终答案、算术错误和单位等五个评估指标上均显著优于GPT-3.5 Turbo，提升幅度明显，验证了新方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括工程教育中的作业评估和个性化学习辅导。通过建立可靠的评估基准，未来可以开发出更智能的教育工具，帮助学生更好地理解电路分析等复杂主题。

## 📄 摘要（原文）

> Large language models (LLMs) have the potential to revolutionize various fields, including code development, robotics, finance, and education, due to their extensive prior knowledge and rapid advancements. This paper investigates how LLMs can be leveraged in engineering education. Specifically, we benchmark the capabilities of different LLMs, including GPT-3.5 Turbo, GPT-4o, and Llama 3 70B, in assessing homework for an undergraduate-level circuit analysis course. We have developed a novel dataset consisting of official reference solutions and real student solutions to problems from various topics in circuit analysis. To overcome the limitations of image recognition in current state-of-the-art LLMs, the solutions in the dataset are converted to LaTeX format. Using this dataset, a prompt template is designed to test five metrics of student solutions: completeness, method, final answer, arithmetic error, and units. The results show that GPT-4o and Llama 3 70B perform significantly better than GPT-3.5 Turbo across all five metrics, with GPT-4o and Llama 3 70B each having distinct advantages in different evaluation aspects. Additionally, we present insights into the limitations of current LLMs in several aspects of circuit analysis. Given the paramount importance of ensuring reliability in LLM-generated homework assessment to avoid misleading students, our results establish benchmarks and offer valuable insights for the development of a reliable, personalized tutor for circuit analysis -- a focus of our future work. Furthermore, the proposed evaluation methods can be generalized to a broader range of courses for engineering education in the future.

