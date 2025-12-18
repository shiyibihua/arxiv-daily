---
layout: default
title: A Structured Framework for Evaluating and Enhancing Interpretive Capabilities of Multimodal LLMs in Culturally Situated Tasks
---

# A Structured Framework for Evaluating and Enhancing Interpretive Capabilities of Multimodal LLMs in Culturally Situated Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23208" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23208v1</a>
  <a href="https://arxiv.org/pdf/2509.23208.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23208v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23208v1', 'A Structured Framework for Evaluating and Enhancing Interpretive Capabilities of Multimodal LLMs in Culturally Situated Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haorui Yu, Ramon Ruiz-Dolz, Qiufeng Yi

**分类**: cs.CL

**发布日期**: 2025-09-27

**备注**: EMNLP 2025 submission, 10 pages, 6 figures, 5 tables

**🔗 代码/项目**: [GITHUB](https://github.com/yha9806/VULCA-EMNLP2025)

---

## 💡 一句话要点

**提出结构化框架，评估并提升多模态LLM在中国文化情境下的理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `视觉语言模型` `文化情境理解` `艺术评论生成` `零样本分类`

## 📋 核心要点

1. 现有VLM在文化情境下的理解能力不足，尤其是在艺术评论等需要深度语义理解的任务中。
2. 论文提出一种结构化框架，通过量化专家评论特征，定义评论角色，引导VLM生成多角度评论。
3. 实验评估了Llama、Qwen、Gemini等VLM在生成中国绘画评论方面的表现，揭示了其优势与不足。

## 📝 摘要（中文）

本研究旨在测试和评估当前主流视觉语言模型（VLM）在生成中国传统绘画评论方面的能力和特点。为此，我们首先开发了一个用于中国绘画评论的量化框架。该框架通过使用零样本分类模型，从人类专家评论中提取多维评估特征构建而成，这些特征涵盖评估立场、特征关注点和评论质量。基于这些特征，定义并量化了几个具有代表性的评论角色。然后，该框架被用于评估选定的VLM，如Llama、Qwen或Gemini。实验设计包括角色引导提示，以评估VLM从不同角度生成评论的能力。我们的研究结果揭示了VLM在艺术评论领域的当前性能水平、优势和改进领域，从而深入了解它们在复杂语义理解和内容生成任务中的潜力和局限性。实验代码可在https://github.com/yha9806/VULCA-EMNLP2025公开获取。

## 🔬 方法详解

**问题定义**：现有视觉语言模型（VLM）在理解和生成具有文化背景的评论方面存在局限性，尤其是在中国传统绘画等领域。现有的方法难以捕捉专家评论的多维度特征，无法有效引导VLM生成高质量、多视角的评论。

**核心思路**：本研究的核心思路是构建一个量化的评估框架，该框架能够从专家评论中提取关键特征，并定义不同的评论角色。通过角色引导提示，可以评估VLM在不同视角下的评论生成能力，从而揭示其优势和不足。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) **专家评论数据收集**：收集中国绘画专家的评论数据。2) **特征提取**：使用零样本分类模型从专家评论中提取多维评估特征，包括评估立场、特征关注点和评论质量。3) **评论角色定义**：基于提取的特征，定义并量化具有代表性的评论角色。4) **VLM评估**：使用角色引导提示，评估选定的VLM（如Llama、Qwen、Gemini）生成评论的能力。5) **结果分析**：分析VLM生成的评论，评估其性能水平、优势和改进领域。

**关键创新**：本研究的关键创新在于提出了一个结构化的量化框架，用于评估和提升VLM在文化情境下的理解能力。该框架能够从专家评论中提取多维特征，并定义评论角色，从而为VLM提供更明确的指导，使其能够生成更具深度和广度的评论。

**关键设计**：在特征提取阶段，使用了零样本分类模型，该模型能够直接对评论文本进行分类，无需额外的训练数据。在角色引导提示阶段，设计了不同的提示语，以引导VLM从不同的角度生成评论。具体的参数设置和网络结构细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，该框架能够有效评估VLM在生成中国绘画评论方面的能力。通过角色引导提示，VLM能够生成具有不同视角的评论，但仍存在改进空间，尤其是在深度语义理解和文化背景知识方面。具体的性能数据和提升幅度在摘要中未提及，属于未知信息。

## 🎯 应用场景

该研究成果可应用于艺术评论生成、文化遗产保护、跨文化交流等领域。通过提升VLM在文化情境下的理解能力，可以帮助人们更好地理解和欣赏不同文化的艺术作品，促进文化交流和理解。此外，该框架还可以推广到其他文化领域，例如文学、音乐等。

## 📄 摘要（原文）

> This study aims to test and evaluate the capabilities and characteristics of current mainstream Visual Language Models (VLMs) in generating critiques for traditional Chinese painting. To achieve this, we first developed a quantitative framework for Chinese painting critique. This framework was constructed by extracting multi-dimensional evaluative features covering evaluative stance, feature focus, and commentary quality from human expert critiques using a zero-shot classification model. Based on these features, several representative critic personas were defined and quantified. This framework was then employed to evaluate selected VLMs such as Llama, Qwen, or Gemini. The experimental design involved persona-guided prompting to assess the VLM's ability to generate critiques from diverse perspectives. Our findings reveal the current performance levels, strengths, and areas for improvement of VLMs in the domain of art critique, offering insights into their potential and limitations in complex semantic understanding and content generation tasks. The code used for our experiments can be publicly accessed at: https://github.com/yha9806/VULCA-EMNLP2025.

