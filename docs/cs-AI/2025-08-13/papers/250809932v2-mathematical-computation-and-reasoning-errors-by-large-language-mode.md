---
layout: default
title: Mathematical Computation and Reasoning Errors by Large Language Models
---

# Mathematical Computation and Reasoning Errors by Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09932" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09932v2</a>
  <a href="https://arxiv.org/pdf/2508.09932.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09932v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09932v2', 'Mathematical Computation and Reasoning Errors by Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liang Zhang, Edith Aurora Graf

**分类**: cs.AI

**发布日期**: 2025-08-13 (更新: 2025-08-14)

---

## 💡 一句话要点

**评估大型语言模型在数学计算中的错误以提升教育效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数学教育` `推理错误` `教育技术` `性能评估`

## 📋 核心要点

1. 现有的LLMs在数学问题解决中存在准确性不足和推理错误的问题，影响教育效果。
2. 本文通过构建具有挑战性的数学任务，评估LLMs的表现，并分析其错误类型，旨在提升其在教育中的应用。
3. 研究发现，增强推理的OpenAI o1模型在数学任务中表现优异，双代理配置显著提高了整体性能。

## 📝 摘要（中文）

大型语言模型（LLMs）在AI驱动的教育中，尤其是数学教育中，越来越多地被应用于教学和评估。本文研究了四种LLMs（OpenAI GPT-4o和o1，DeepSeek-V3和DeepSeek-R1）在解决算术、代数和数论等三类数学任务时的准确性，并识别了解决方案中的逐步推理错误。研究构建了具有挑战性的数学任务，系统分析了最终答案的准确性及个别解题步骤中的错误。结果表明，增强推理能力的OpenAI o1模型在所有三类任务中表现出更高的准确性，而程序性失误是最常见的错误类型。双代理配置显著提升了整体表现。这些发现为提升LLMs性能提供了可行的见解，并强调了将LLMs有效整合到数学教育中的策略。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在数学计算中常见的推理错误和准确性不足的问题。现有方法在处理复杂数学任务时容易出现错误，影响教育反馈的可靠性。

**核心思路**：通过构建具有挑战性的数学任务，系统评估不同LLMs的表现，特别关注逐步推理中的错误，旨在识别并改进这些模型的推理能力。

**技术框架**：研究设计了多种数学任务，分为算术、代数和数论三类，采用单代理和双代理配置进行测试。每个模型的答案准确性和解题步骤中的错误被系统分析和编码。

**关键创新**：最重要的创新在于构建了针对LLMs的挑战性数学任务，并通过系统分析错误类型，提供了改进模型性能的实证依据。这与传统基准测试方法的本质区别在于更具针对性和实用性。

**关键设计**：在实验中，采用了不同的模型配置和任务设计，特别关注程序性失误和概念性误解的分析，双代理配置的引入显著提升了模型的整体表现。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文获取更多技术细节。

## 📊 实验亮点

实验结果显示，增强推理能力的OpenAI o1模型在所有三类数学任务中表现出更高或接近完美的准确性。程序性失误是最常见的错误类型，双代理配置的引入显著提升了整体性能，表明该方法在教育应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和个性化学习平台。通过提升LLMs在数学教育中的表现，可以为学生提供更准确的反馈和指导，进而改善学习效果。未来，研究成果可能推动AI在教育领域的更广泛应用，提升教学质量和效率。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly utilized in AI-driven educational instruction and assessment, particularly within mathematics education. The capability of LLMs to generate accurate answers and detailed solutions for math problem-solving tasks is foundational for ensuring reliable and precise feedback and assessment in math education practices. Our study focuses on evaluating the accuracy of four LLMs (OpenAI GPT-4o and o1, DeepSeek-V3 and DeepSeek-R1) solving three categories of math tasks, including arithmetic, algebra, and number theory, and identifies step-level reasoning errors within their solutions. Instead of relying on standard benchmarks, we intentionally build math tasks (via item models) that are challenging for LLMs and prone to errors. The accuracy of final answers and the presence of errors in individual solution steps were systematically analyzed and coded. Both single-agent and dual-agent configurations were tested. It is observed that the reasoning-enhanced OpenAI o1 model consistently achieved higher or nearly perfect accuracy across all three math task categories. Analysis of errors revealed that procedural slips were the most frequent and significantly impacted overall performance, while conceptual misunderstandings were less frequent. Deploying dual-agent configurations substantially improved overall performance. These findings offer actionable insights into enhancing LLM performance and underscore effective strategies for integrating LLMs into mathematics education, thereby advancing AI-driven instructional practices and assessment precision.

