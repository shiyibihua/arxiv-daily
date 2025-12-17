---
layout: default
title: ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking
---

# ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14654" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14654v1</a>
  <a href="https://arxiv.org/pdf/2512.14654.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14654v1" onclick="toggleFavorite(this, '2512.14654v1', 'ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lihong Wang, Liangqi Li, Weiwei Feng, Jiamin Wu, Changtao Miao, Tieru Wu, Rui Ma, Bo Zhang, Zhe Li

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Code is available at https://github.com/Leon-LihongWang/ViRC

**🔗 代码/项目**: [GITHUB](https://github.com/Leon-LihongWang/ViRC)

---

## 💡 一句话要点

**提出ViRC框架，通过Reason Chunking增强多模态数学问题中的视觉推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `数学推理` `视觉推理` `链式思考` `Reason Chunking` `关键推理单元` `渐进式训练`

## 📋 核心要点

1. 现有MLLM在多模态数学问题中，缺乏对动态视觉信息的有效利用，限制了推理能力。
2. ViRC框架引入Reason Chunking机制，将推理过程分解为关键推理单元CRU，模拟人类专家解题模式。
3. 通过CRUX数据集和渐进式训练策略，ViRC-7B模型在多个数学基准测试中取得了显著的性能提升。

## 📝 摘要（中文）

本文提出ViRC框架，旨在提升大型语言模型在多模态数学任务中的推理能力。现有多模态LLM通常仅基于静态数学图像进行文本推理，忽略了推理过程中动态视觉信息的获取。ViRC框架受到认知科学中米勒定律的启发，引入Reason Chunking机制，将多模态数学CoT分解为连续的关键推理单元(CRU)，模拟人类专家解决问题的模式。CRU确保单元内文本连贯性，用于中间命题验证，同时整合跨单元的视觉信息，以生成后续命题并支持结构化推理。为此，本文构建了CRUX数据集，使用三种视觉工具和四种推理模式，为每个数学问题提供显式标注的CRU。利用CRUX数据集，提出了一种受人类认知学习启发的渐进式训练策略，包括Instructional SFT、Practice SFT和Strategic RL，旨在进一步加强模型的Reason Chunking能力。最终的ViRC-7B模型在多个数学基准测试中实现了平均18.8%的性能提升。

## 🔬 方法详解

**问题定义**：现有的多模态大型语言模型（MLLM）在解决数学问题时，主要依赖于对单一静态图像的文本推理，忽略了人类在解决此类问题时，会反复观察图像并逐步推理的动态过程。这种静态推理方式无法充分利用视觉信息，导致推理能力受限。此外，现有方法缺乏对中间推理步骤的显式建模，难以保证推理过程的连贯性和可解释性。

**核心思路**：ViRC框架的核心思路是模拟人类专家解决数学问题的模式，将复杂的推理过程分解为一系列关键推理单元（CRU）。每个CRU专注于验证一个中间命题，并利用视觉信息生成后续命题。这种Reason Chunking机制借鉴了认知科学中的米勒定律，认为将问题分解为小的逻辑单元有助于提高认知效率。通过显式地建模中间推理步骤，ViRC框架旨在提高推理的连贯性、准确性和可解释性。

**技术框架**：ViRC框架包含以下主要组成部分：1) CRUX数据集：一个包含显式标注CRU的多模态数学问题数据集，用于训练和评估模型。2) Reason Chunking机制：将推理过程分解为一系列CRU，每个CRU包含文本和视觉信息。3) 渐进式训练策略：包括Instructional SFT、Practice SFT和Strategic RL三个阶段，逐步提升模型的Reason Chunking能力。整体流程是，首先使用Instructional SFT让模型学习基本的推理能力，然后使用Practice SFT让模型熟悉CRU的结构和推理模式，最后使用Strategic RL优化模型的推理策略。

**关键创新**：ViRC框架的关键创新在于引入了Reason Chunking机制，将多模态数学推理过程分解为一系列CRU。与现有方法相比，ViRC框架能够更好地利用视觉信息，显式地建模中间推理步骤，并提高推理的连贯性和可解释性。此外，CRUX数据集的构建和渐进式训练策略也为模型的训练提供了有效的支持。

**关键设计**：CRUX数据集包含三种视觉工具（例如，绘制几何图形、标注图像）和四种推理模式（例如，演绎推理、归纳推理）。渐进式训练策略中的Instructional SFT使用人工标注的CRU进行训练，Practice SFT使用自动生成的CRU进行训练，Strategic RL使用奖励函数来优化模型的推理策略。奖励函数的设计考虑了推理的准确性、连贯性和效率。

## 📊 实验亮点

ViRC-7B模型在多个数学基准测试中取得了显著的性能提升，平均提升幅度达到18.8%。具体而言，在某些数据集上，ViRC-7B模型的性能超过了现有最佳模型，证明了Reason Chunking机制的有效性。实验结果表明，ViRC框架能够更好地利用视觉信息，提高推理的准确性和连贯性。

## 🎯 应用场景

ViRC框架具有广泛的应用前景，可应用于教育、科研等领域。例如，可以开发智能辅导系统，帮助学生理解和解决数学问题。此外，该框架还可以扩展到其他多模态推理任务，例如视觉问答、图像描述等，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> CoT has significantly enhanced the reasoning ability of LLMs while it faces challenges when extended to multimodal domains, particularly in mathematical tasks. Existing MLLMs typically perform textual reasoning solely from a single static mathematical image, overlooking dynamic visual acquisition during reasoning. In contrast, humans repeatedly examine visual image and employ step-by-step reasoning to prove intermediate propositions. This strategy of decomposing the problem-solving process into key logical nodes adheres to Miller's Law in cognitive science. Inspired by this insight, we propose a ViRC framework for multimodal mathematical tasks, introducing a Reason Chunking mechanism that structures multimodal mathematical CoT into consecutive Critical Reasoning Units (CRUs) to simulate human expert problem-solving patterns. CRUs ensure intra-unit textual coherence for intermediate proposition verification while integrating visual information across units to generate subsequent propositions and support structured reasoning. To this end, we present CRUX dataset by using three visual tools and four reasoning patterns to provide explicitly annotated CRUs across multiple reasoning paths for each mathematical problem. Leveraging the CRUX dataset, we propose a progressive training strategy inspired by human cognitive learning, which includes Instructional SFT, Practice SFT, and Strategic RL, aimed at further strengthening the Reason Chunking ability of the model.The resulting ViRC-7B model achieves a 18.8\% average improvement over baselines across multiple mathematical benchmarks. Code is available at https://github.com/Leon-LihongWang/ViRC.

