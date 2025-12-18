---
layout: default
title: Why Do MLLMs Struggle with Spatial Understanding? A Systematic Analysis from Data to Architecture
---

# Why Do MLLMs Struggle with Spatial Understanding? A Systematic Analysis from Data to Architecture

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02359" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02359v1</a>
  <a href="https://arxiv.org/pdf/2509.02359.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02359v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02359v1', 'Why Do MLLMs Struggle with Spatial Understanding? A Systematic Analysis from Data to Architecture')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wanyue Zhang, Yibin Huang, Yangbin Xu, JingJing Huang, Helu Zhi, Shuo Ren, Wang Xu, Jiajun Zhang

**分类**: cs.CV

**发布日期**: 2025-09-02

**备注**: The benchmark MulSeT is available at https://huggingface.co/datasets/WanyueZhang/MulSeT

---

## 💡 一句话要点

**系统分析MLLM空间理解能力瓶颈，提出MulSeT基准并探究数据与架构的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `空间理解` `多视图学习` `基准测试` `位置编码`

## 📋 核心要点

1. 现有MLLM在空间理解方面存在不足，缺乏系统性的评估，通常局限于单一场景。
2. 提出MulSeT基准，从数据和架构角度系统分析MLLM在单视图、多视图和视频场景下的空间理解能力。
3. 实验表明，单纯增加训练数据效果有限，空间理解更依赖视觉编码器的位置编码。

## 📝 摘要（中文）

空间理解对于多模态大型语言模型(MLLM)在具身环境中支持感知、推理和规划至关重要。尽管最近取得了进展，但现有研究表明MLLM在空间理解方面仍然存在困难。然而，现有的研究缺乏对这些局限性的全面和系统的评估，通常仅限于孤立的场景，如单视图或视频。本文从数据和架构的角度，对单视图、多视图和视频三种代表性场景下的空间理解进行了系统分析。我们提出了一个名为MulSeT（多视图空间理解任务）的基准，并设计了一系列实验来分析MLLM的空间推理能力。从数据角度来看，随着训练数据的增加，空间理解的性能迅速收敛，并且上限相对较低，特别是对于需要空间想象的任务。这表明仅仅扩展训练数据不足以获得令人满意的性能。从架构角度来看，我们发现空间理解更依赖于视觉编码器内的位置编码，而不是语言模型内的位置编码，无论是在级联MLLM还是原生MLLM中。此外，我们探索了推理注入，并通过架构设计来优化空间理解，从而展望未来的改进。这些见解揭示了当前MLLM的局限性，并为通过数据缩放和架构调整来提高空间推理能力提出了新的方向。

## 🔬 方法详解

**问题定义**：MLLM在具身环境中进行感知、推理和规划时，需要具备强大的空间理解能力。然而，现有MLLM在处理单视图、多视图以及视频等场景下的空间推理任务时表现不佳。现有研究缺乏对这些局限性的系统性分析，难以指导模型改进。

**核心思路**：本文的核心思路是从数据和架构两个维度，系统性地分析MLLM在空间理解方面的瓶颈。通过构建多视图空间理解任务基准（MulSeT），并设计一系列实验，深入探究数据规模、数据质量以及模型架构对空间理解能力的影响。

**技术框架**：本文提出的MulSeT基准包含单视图、多视图和视频三种场景下的空间理解任务。研究人员首先利用该基准评估现有MLLM的空间推理能力。然后，从数据角度，分析训练数据规模对性能的影响；从架构角度，分析视觉编码器和语言模型中位置编码的重要性。此外，还探索了推理注入方法，并提出了通过架构设计优化空间理解的思路。

**关键创新**：本文最重要的创新在于对MLLM空间理解能力的系统性分析框架。通过MulSeT基准，研究人员可以全面评估MLLM在不同场景下的空间推理能力。此外，本文还揭示了数据规模和模型架构对空间理解能力的不同影响，为未来的模型改进提供了重要指导。

**关键设计**：MulSeT基准包含多种空间理解任务，例如目标定位、场景理解和运动预测。在实验中，研究人员使用了不同的MLLM模型，并调整了训练数据规模和模型架构。他们还探索了不同的位置编码方法和推理注入策略，以提高模型的空间理解能力。

## 📊 实验亮点

实验结果表明，单纯增加训练数据对空间理解能力的提升有限，尤其是在需要空间想象的任务中。研究发现，视觉编码器中的位置编码对空间理解至关重要，其重要性高于语言模型中的位置编码。通过推理注入和架构调整，可以有效提高MLLM的空间理解能力。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、增强现实等领域。通过提升MLLM的空间理解能力，可以使机器人在复杂环境中更好地感知、推理和规划，从而实现更智能、更可靠的自主行为。未来的研究可以进一步探索更有效的模型架构和训练方法，以提高MLLM在更复杂场景下的空间理解能力。

## 📄 摘要（原文）

> Spatial understanding is essential for Multimodal Large Language Models (MLLMs) to support perception, reasoning, and planning in embodied environments. Despite recent progress, existing studies reveal that MLLMs still struggle with spatial understanding. However, existing research lacks a comprehensive and systematic evaluation of these limitations, often restricted to isolated scenarios, such as single-view or video. In this work, we present a systematic analysis of spatial understanding from both data and architectural perspectives across three representative scenarios: single-view, multi-view, and video. We propose a benchmark named MulSeT (Multi-view Spatial Understanding Tasks), and design a series of experiments to analyze the spatial reasoning capabilities of MLLMs. From the data perspective, the performance of spatial understanding converges quickly as the training data increases, and the upper bound is relatively low, especially for tasks that require spatial imagination. This indicates that merely expanding training data is insufficient to achieve satisfactory performance. From the architectural perspective, we find that spatial understanding relies more heavily on the positional encoding within the visual encoder than within the language model, in both cascaded and native MLLMs. Moreover, we explore reasoning injection and envision future improvements through architectural design to optimize spatial understanding. These insights shed light on the limitations of current MLLMs and suggest new directions for improving spatial reasoning capabilities through data scaling and architectural tuning.

