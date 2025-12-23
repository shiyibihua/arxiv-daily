---
layout: default
title: Large Language Models Acing Chartered Accountancy
---

# Large Language Models Acing Chartered Accountancy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21031" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21031v1</a>
  <a href="https://arxiv.org/pdf/2506.21031.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21031v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21031v1', 'Large Language Models Acing Chartered Accountancy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jatin Gupta, Akhil Sharma, Saransh Singhania, Mohammad Adnan, Sakshi Deo, Ali Imam Abidi, Keshav Gupta

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-26

**备注**: Accepted for publication at MoStart 2025: International Conference on Digital Transformation in Education and Applications of Artificial Intelligence, Bosnia and Herzegovina, 2025

---

## 💡 一句话要点

**提出CA-Ben基准以评估大型语言模型在会计领域的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `注册会计师` `金融知识` `法律推理` `定量分析` `自然语言处理` `模型评估`

## 📋 核心要点

1. 现有大型语言模型在特定金融领域知识的捕捉和应用效果不佳，尤其是在会计和法律推理方面。
2. 本文提出CA-Ben基准，专门用于评估LLMs在财务、法律和定量推理能力的表现，填补了印度金融领域的研究空白。
3. 实验结果显示，Claude 3.5 Sonnet和GPT-4o在概念和法律推理方面表现优异，但在数值计算和法律解释上仍面临挑战。

## 📝 摘要（中文）

先进的智能系统，尤其是大型语言模型（LLMs），正在通过自然语言处理（NLP）的进步显著改变金融实践。然而，这些模型在捕捉和应用特定领域的金融知识方面的有效性仍然不确定。为填补这一关键空白，本文介绍了CA-Ben，一个专门设计用于评估LLMs在财务、法律和定量推理能力的注册会计师基准。CA-Ben包含来自印度注册会计师协会（ICAI）严格考试的结构化问答数据集，涵盖基础、中级和高级CA课程阶段。通过标准化协议评估了六个主要的LLMs，结果显示表现存在差异，Claude 3.5 Sonnet和GPT-4o的表现优于其他模型，尤其在概念和法律推理方面。研究结果强调了当前LLMs的优势和局限性，并建议通过混合推理和检索增强生成方法进行未来改进，特别是在定量分析和准确的法律解释方面。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在会计领域的知识应用不足的问题，尤其是在法律推理和数值计算方面的挑战。现有方法未能有效评估LLMs在特定领域的能力。

**核心思路**：论文提出CA-Ben基准，通过结构化问答数据集评估LLMs的财务、法律和定量推理能力，旨在提供一个标准化的评估框架。

**技术框架**：整体架构包括数据集构建、模型评估和结果分析三个主要模块。数据集来源于ICAI的考试，涵盖不同CA课程阶段。

**关键创新**：CA-Ben基准的提出是本文的核心创新，填补了现有LLMs评估的空白，特别是在会计和法律领域的应用。

**关键设计**：数据集设计采用了结构化问答形式，确保涵盖财务、法律和定量推理的多样性，评估过程中使用标准化协议以确保结果的可比性。实验中对六个LLMs的评估采用了统一的测试标准。

## 📊 实验亮点

实验结果显示，Claude 3.5 Sonnet和GPT-4o在概念和法律推理方面的表现优于其他模型，尤其在准确性上有显著提升。尽管如此，所有模型在数值计算和法律解释方面仍存在明显挑战，表明未来研究的方向。

## 🎯 应用场景

该研究的潜在应用领域包括会计教育、金融咨询和法律服务等。通过评估LLMs在这些领域的能力，能够为金融行业的智能化转型提供支持，提升决策效率和准确性。未来，随着技术的进步，LLMs在会计和法律领域的应用将更加广泛，推动行业的发展。

## 📄 摘要（原文）

> Advanced intelligent systems, particularly Large Language Models (LLMs), are significantly reshaping financial practices through advancements in Natural Language Processing (NLP). However, the extent to which these models effectively capture and apply domain-specific financial knowledge remains uncertain. Addressing a critical gap in the expansive Indian financial context, this paper introduces CA-Ben, a Chartered Accountancy benchmark specifically designed to evaluate the financial, legal, and quantitative reasoning capabilities of LLMs. CA-Ben comprises structured question-answer datasets derived from the rigorous examinations conducted by the Institute of Chartered Accountants of India (ICAI), spanning foundational, intermediate, and advanced CA curriculum stages. Six prominent LLMs i.e. GPT 4o, LLAMA 3.3 70B, LLAMA 3.1 405B, MISTRAL Large, Claude 3.5 Sonnet, and Microsoft Phi 4 were evaluated using standardized protocols. Results indicate variations in performance, with Claude 3.5 Sonnet and GPT-4o outperforming others, especially in conceptual and legal reasoning. Notable challenges emerged in numerical computations and legal interpretations. The findings emphasize the strengths and limitations of current LLMs, suggesting future improvements through hybrid reasoning and retrieval-augmented generation methods, particularly for quantitative analysis and accurate legal interpretation.

