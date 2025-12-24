---
layout: default
title: Coherent Multimodal Reasoning with Iterative Self-Evaluation for Vision-Language Models
---

# Coherent Multimodal Reasoning with Iterative Self-Evaluation for Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02886" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02886v1</a>
  <a href="https://arxiv.org/pdf/2508.02886.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02886v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02886v1', 'Coherent Multimodal Reasoning with Iterative Self-Evaluation for Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenjie Luo, Ruocheng Li, Shanshan Zhu, Julian Perry

**分类**: cs.CL

**发布日期**: 2025-08-04

---

## 💡 一句话要点

**提出一致性多模态推理框架以解决复杂推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `视觉语言模型` `自我评估` `推理分解` `上下文推理` `一致性评估` `深度学习` `人工智能`

## 📋 核心要点

1. 现有的大型语言模型和视觉语言模型在复杂的跨模态推理任务中表现不佳，缺乏深度推理能力。
2. 本文提出了一致性多模态推理框架（CMRF），通过迭代自我评估机制提升推理能力，模拟人类的推理过程。
3. CMRF在多个基准测试中表现优异，平均准确率达到69.4%，超越最佳开源基线2.4个百分点，尤其在复杂推理场景中表现突出。

## 📝 摘要（中文）

尽管大型语言模型和视觉语言模型取得了显著进展，但在复杂的多步骤跨模态常识推理任务中仍然存在不足，常表现为缺乏深度推理能力。为此，本文提出了一种一致性多模态推理框架（CMRF），通过迭代自我评估推理机制，增强了视觉语言模型的常识推理能力。CMRF通过分解复杂查询、逐步生成推理并自我纠正错误，模拟人类问题解决过程。该框架集成了三个关键模块：推理分解单元、上下文推理引擎和一致性评估模块，并结合自适应迭代优化策略，系统性地改进推理路径。基于LLaVA-1.6-34B并在新颖的多模态日常活动推理数据集上训练，CMRF在VCR、A-OKVQA和DailyLife-MRC等基准测试中实现了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉语言模型在复杂多步骤跨模态常识推理任务中的不足，尤其是缺乏深度推理和自我纠错能力的问题。

**核心思路**：提出一致性多模态推理框架（CMRF），通过分解问题、逐步推理和自我评估，模拟人类的推理过程，从而提升模型的推理能力。

**技术框架**：CMRF框架包括三个主要模块：推理分解单元（RDU）用于将复杂问题分解为子问题；上下文推理引擎（CIE）用于进行上下文推理；一致性评估模块（CAM）用于评估推理的逻辑一致性和置信度。此外，结合自适应迭代优化策略，系统性地改进推理路径。

**关键创新**：CMRF的核心创新在于其迭代自我评估机制，通过分解和逐步推理的方式，显著提升了推理的连贯性和准确性，与现有方法相比，提供了更深层次的推理能力。

**关键设计**：在模型训练中，采用了新颖的多模态日常活动推理数据集，设计了适应性迭代优化策略，确保推理过程中的逻辑一致性和置信度评估，提升了整体性能。

## 📊 实验亮点

CMRF在多个基准测试中表现出色，平均准确率达到69.4%，超越最佳开源基线2.4个百分点，尤其在复杂推理场景中展现出显著优势。大量消融实验和人工评估验证了各模块的关键贡献及迭代优化的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、自动化客服、教育辅助工具等，能够帮助系统更好地理解和处理复杂的多模态信息，提高用户交互体验。未来，该框架可能在更广泛的人工智能应用中发挥重要作用，推动跨模态推理技术的发展。

## 📄 摘要（原文）

> Despite significant advancements, current large language models (LLMs) and vision-language models (LVLMs) continue to struggle with complex, multi-step, cross-modal common sense reasoning tasks, often exhibiting a lack of "deliberative thinking." They tend to rely on superficial associations rather than deep, chained inference, particularly when integrating visual information with abstract concepts. To address this, we propose the Coherent Multimodal Reasoning Framework (CMRF), a novel approach that enhances LVLMs' common sense reasoning capabilities through an iterative, self-evaluating inference mechanism. CMRF mimics human problem-solving by decomposing complex queries, generating step-by-step inferences, and self-correcting errors. Our framework integrates three key modules: a Reasoning Decomposition Unit (RDU) for breaking down problems into sub-questions, a Contextual Inference Engine (CIE) for contextual inference, and a Coherence Assessment Module (CAM) for evaluating logical consistency and confidence. Coupled with an Adaptive Iterative Refinement strategy, CMRF systematically refines its reasoning paths. Built upon LLaVA-1.6-34B and trained on a novel Multimodal Daily Activity Reasoning (MDAR) dataset, CMRF achieves state-of-the-art performance among open-source LVLMs on challenging benchmarks like VCR, A-OKVQA, and DailyLife-MRC. It attains an average accuracy of 69.4%, surpassing the best open-source baseline by +2.4 percentage points, with particular strength in complex reasoning scenarios. Extensive ablation studies and human evaluations confirm the critical contributions of each module and the effectiveness of iterative refinement in fostering more coherent and accurate reasoning.

