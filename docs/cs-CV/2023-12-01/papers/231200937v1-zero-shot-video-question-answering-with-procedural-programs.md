---
layout: default
title: Zero-Shot Video Question Answering with Procedural Programs
---

# Zero-Shot Video Question Answering with Procedural Programs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00937" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00937v1</a>
  <a href="https://arxiv.org/pdf/2312.00937.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00937v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00937v1', 'Zero-Shot Video Question Answering with Procedural Programs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rohan Choudhury, Koichiro Niinuma, Kris M. Kitani, László A. Jeni

**分类**: cs.CV

**发布日期**: 2023-12-01

**备注**: 16 pages, 7 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://rccchoudhury.github.io/proviq2023)

---

## 💡 一句话要点

**提出ProViQ以解决视频零-shot问答问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频问答` `程序生成` `视觉模块` `多目标跟踪` `视频理解` `零-shot学习` `多模态处理`

## 📋 核心要点

1. 现有方法在视频问答任务中面临挑战，尤其是在零-shot场景下，难以有效处理多样化视频内容。
2. 论文提出的ProViQ通过生成程序化的视觉任务序列，利用大型语言模型实现视频问答，具有较强的通用性。
3. ProViQ在多个基准测试中表现出色，尤其在短视频和长视频问答任务上，性能提升可达25%。

## 📝 摘要（中文）

我们提出了一种通过生成短程序来回答视频的零-shot问题的方法，称为程序化视频查询（ProViQ）。该方法利用大型语言模型从输入问题和视觉模块API生成程序，并执行这些程序以获得输出。虽然类似的程序化方法在图像问答中取得了成功，但视频理解仍然具有挑战性。ProViQ配备了针对视频理解的模块，使其能够广泛适应各种视频。此外，该代码生成框架还使ProViQ能够执行其他视频任务，如多目标跟踪和基本视频编辑。ProViQ在多种基准测试中取得了最先进的结果，在短视频、长视频、开放式和多模态视频问答数据集上提升了多达25%。

## 🔬 方法详解

**问题定义**：本论文旨在解决视频问答中的零-shot问题，现有方法在处理多样化视频内容时存在局限性，难以有效生成答案。

**核心思路**：ProViQ的核心思路是通过生成短程序来分解视频问答任务，将复杂问题转化为一系列可执行的视觉子任务，从而实现更高效的答案生成。

**技术框架**：ProViQ的整体架构包括三个主要模块：输入问题解析、程序生成和执行模块。首先，输入问题通过大型语言模型解析，生成相应的程序；然后，程序在视觉模块API的支持下被执行，最终输出答案。

**关键创新**：ProViQ的最大创新在于其程序生成能力，结合了视频理解模块，使其能够处理更复杂的视觉信息，与传统的图像问答方法相比，具有更强的适应性和灵活性。

**关键设计**：在设计上，ProViQ采用了特定的视觉模块API，确保生成的程序能够有效执行。此外，模型的训练过程中采用了多样化的数据集，以增强其在不同视频场景下的泛化能力。

## 📊 实验亮点

ProViQ在多个视频问答基准测试中取得了最先进的结果，特别是在短视频和长视频问答任务上，性能提升高达25%。与现有方法相比，ProViQ展现了更强的适应性和灵活性，能够处理更复杂的视频内容。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、视频内容分析和自动化视频编辑等。通过实现高效的视频问答，ProViQ能够帮助用户快速获取视频信息，提升信息检索的效率和准确性。未来，随着视频数据量的不断增加，该技术的实际价值将愈加显著。

## 📄 摘要（原文）

> We propose to answer zero-shot questions about videos by generating short procedural programs that derive a final answer from solving a sequence of visual subtasks. We present Procedural Video Querying (ProViQ), which uses a large language model to generate such programs from an input question and an API of visual modules in the prompt, then executes them to obtain the output. Recent similar procedural approaches have proven successful for image question answering, but videos remain challenging: we provide ProViQ with modules intended for video understanding, allowing it to generalize to a wide variety of videos. This code generation framework additionally enables ProViQ to perform other video tasks in addition to question answering, such as multi-object tracking or basic video editing. ProViQ achieves state-of-the-art results on a diverse range of benchmarks, with improvements of up to 25% on short, long, open-ended, and multimodal video question-answering datasets. Our project page is at https://rccchoudhury.github.io/proviq2023.

