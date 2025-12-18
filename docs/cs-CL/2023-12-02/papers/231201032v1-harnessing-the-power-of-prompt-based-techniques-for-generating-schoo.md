---
layout: default
title: Harnessing the Power of Prompt-based Techniques for Generating School-Level Questions using Large Language Models
---

# Harnessing the Power of Prompt-based Techniques for Generating School-Level Questions using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.01032" class="toolbar-btn" target="_blank">📄 arXiv: 2312.01032v1</a>
  <a href="https://arxiv.org/pdf/2312.01032.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.01032v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.01032v1', 'Harnessing the Power of Prompt-based Techniques for Generating School-Level Questions using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Subhankar Maity, Aniket Deroy, Sudeshna Sarkar

**分类**: cs.CL, cs.AI

**发布日期**: 2023-12-02

**🔗 代码/项目**: [GITHUB](https://github.com/my625/PromptQG)

---

## 💡 一句话要点

**利用提示学习技术，使用大型语言模型生成学校级别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `问题生成` `提示学习` `大型语言模型` `教育数据集` `EduProbe`

## 📋 核心要点

1. 高质量教育问题设计耗时且具挑战性，现有方法难以有效生成描述性和推理性的问题。
2. 提出利用提示学习技术，通过长短提示引导大型语言模型生成高质量问题。
3. 构建了新的学校级别问题生成数据集EduProbe，实验表明T5模型表现最佳，但仍低于人工水平。

## 📝 摘要（中文）

设计高质量的教育问题是一项具有挑战性且耗时的任务。本文提出了一种新颖的方法，该方法利用基于提示的技术来生成描述性和基于推理的问题。然而，当前的问答（QA）数据集不足以在教育环境中进行基于提示的问题生成（QG）实验。因此，我们利用NCERT教科书的丰富内容，为学校级别的科目整理了一个新的QG数据集，名为EduProbe。我们仔细地将此数据集标注为四元组：1）上下文：形成问题的片段；2）长提示：问题的长文本提示（即，覆盖上下文主要主题的较长单词或短语序列）；3）短提示：问题的短文本提示（即，上下文的关键信息或焦点的浓缩表示）；4）问题：与上下文对齐并与提示一致的深度问题。我们通过微调预训练的基于Transformer的大型语言模型（LLM），即PEGASUS、T5、MBART和BART，研究了几种基于提示的QG方法。此外，我们还探索了两个通用预训练LLM（如Text-Davinci-003和GPT-3.5-Turbo）在没有任何进一步训练的情况下的性能。通过执行自动评估，我们表明T5（使用长提示）优于所有其他模型，但仍未达到人工基线。在人工评估标准下，TextDavinci-003在各种提示设置下通常表现出比其他模型更好的结果。即使在人工评估标准的情况下，QG模型也大多未达到人工基线。我们的代码和数据集可在https://github.com/my625/PromptQG获得。

## 🔬 方法详解

**问题定义**：论文旨在解决自动生成高质量学校级别教育问题的问题。现有方法或数据集在生成需要推理和描述的问题方面存在不足，缺乏针对教育场景的有效提示机制。

**核心思路**：论文的核心思路是利用提示学习（Prompt-based Learning）的强大能力，通过设计合适的提示（包括长提示和短提示）来引导大型语言模型（LLMs）生成与上下文相关的、具有深度和推理能力的教育问题。这种方法旨在克服传统方法在问题生成方面的局限性。

**技术框架**：整体框架包括以下几个主要步骤：1) 构建高质量的教育问题生成数据集EduProbe，包含上下文、长提示、短提示和问题四元组；2) 选择预训练的Transformer-based LLMs，如PEGASUS、T5、MBART和BART，以及通用LLMs，如Text-Davinci-003和GPT-3.5-Turbo；3) 使用EduProbe数据集对部分LLMs进行微调，并直接评估通用LLMs的性能；4) 使用自动评估指标和人工评估方法对生成的问题进行评估。

**关键创新**：论文的关键创新在于：1) 提出了利用长短提示相结合的方式来引导LLMs生成高质量教育问题；2) 构建了专门针对学校级别教育场景的问题生成数据集EduProbe；3) 系统地比较了多种预训练LLMs在问题生成任务上的性能，包括微调模型和零样本模型。

**关键设计**：EduProbe数据集的关键设计在于四元组的构建，特别是长提示和短提示的设计，旨在提供不同粒度的上下文信息，引导LLMs生成更准确、更具推理能力的问题。实验中，针对不同的LLMs，采用了不同的微调策略和超参数设置。评估指标包括自动评估指标（如BLEU、ROUGE）和人工评估指标（如相关性、流畅性、深度）。

## 📊 实验亮点

实验结果表明，经过微调的T5模型（使用长提示）在自动评估指标上表现最佳，但仍低于人工基线。在人工评估中，TextDavinci-003在各种提示设置下通常表现出更好的结果。总体而言，即使在人工评估标准下，QG模型也大多未达到人工基线，表明该领域仍有很大的提升空间。

## 🎯 应用场景

该研究成果可应用于智能教育系统、在线学习平台和教育资源生成工具中，帮助教师和学生更高效地创建和获取高质量的教育问题。通过自动化问题生成，可以减轻教师的工作负担，并为学生提供个性化的学习体验。未来，该技术有望进一步扩展到其他教育领域和学科。

## 📄 摘要（原文）

> Designing high-quality educational questions is a challenging and time-consuming task. In this work, we propose a novel approach that utilizes prompt-based techniques to generate descriptive and reasoning-based questions. However, current question-answering (QA) datasets are inadequate for conducting our experiments on prompt-based question generation (QG) in an educational setting. Therefore, we curate a new QG dataset called EduProbe for school-level subjects, by leveraging the rich content of NCERT textbooks. We carefully annotate this dataset as quadruples of 1) Context: a segment upon which the question is formed; 2) Long Prompt: a long textual cue for the question (i.e., a longer sequence of words or phrases, covering the main theme of the context); 3) Short Prompt: a short textual cue for the question (i.e., a condensed representation of the key information or focus of the context); 4) Question: a deep question that aligns with the context and is coherent with the prompts. We investigate several prompt-based QG methods by fine-tuning pre-trained transformer-based large language models (LLMs), namely PEGASUS, T5, MBART, and BART. Moreover, we explore the performance of two general-purpose pre-trained LLMs such as Text-Davinci-003 and GPT-3.5-Turbo without any further training. By performing automatic evaluation, we show that T5 (with long prompt) outperforms all other models, but still falls short of the human baseline. Under human evaluation criteria, TextDavinci-003 usually shows better results than other models under various prompt settings. Even in the case of human evaluation criteria, QG models mostly fall short of the human baseline. Our code and dataset are available at: https://github.com/my625/PromptQG

