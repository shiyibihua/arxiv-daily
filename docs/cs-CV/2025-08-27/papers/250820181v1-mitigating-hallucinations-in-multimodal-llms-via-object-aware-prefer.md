---
layout: default
title: Mitigating Hallucinations in Multimodal LLMs via Object-aware Preference Optimization
---

# Mitigating Hallucinations in Multimodal LLMs via Object-aware Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20181" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20181v1</a>
  <a href="https://arxiv.org/pdf/2508.20181.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20181v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20181v1', 'Mitigating Hallucinations in Multimodal LLMs via Object-aware Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alberto Compagnoni, Davide Caffagni, Nicholas Moratelli, Lorenzo Baraldi, Marcella Cornia, Rita Cucchiara

**分类**: cs.CV, cs.AI, cs.CL, cs.MM

**发布日期**: 2025-08-27

**备注**: BMVC 2025

**🔗 代码/项目**: [GITHUB](https://github.com/aimagelab/CHAIR-DPO)

---

## 💡 一句话要点

**提出CHAIR-DPO以减少多模态大语言模型的幻觉问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `幻觉问题` `直接偏好优化` `CHAIR指标` `模型微调` `自然语言处理` `计算机视觉`

## 📋 核心要点

1. 多模态大语言模型在处理多种任务时，仍然存在生成与视觉输入不符的幻觉现象，影响其可靠性。
2. 本文提出CHAIR-DPO方法，通过CHAIR指标优化生成答案的偏好，减少幻觉现象的发生。
3. 实验表明，CHAIR-DPO在多个幻觉基准测试中显著降低了幻觉答案的比例，验证了其有效性。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）作为统一接口，能够处理从自然语言处理到计算机视觉的多种任务。尽管在许多基准测试中表现出色，但MLLMs仍然存在幻觉现象，即生成的答案与视觉输入不符。本文将幻觉问题视为对齐问题，旨在引导MLLMs生成不带幻觉的内容。与需要复杂管道构建合成偏好数据的现有方法不同，本文利用CHAIR指标来区分生成答案的优劣，并通过直接偏好优化（DPO）对现成的MLLMs进行微调。实验结果表明，CHAIR-DPO有效减少了多个幻觉基准上的幻觉答案，证明了CHAIR基础奖励的有效性。

## 🔬 方法详解

**问题定义**：本文解决的是多模态大语言模型（MLLMs）在生成答案时出现的幻觉现象，即生成的内容与视觉输入不一致。现有方法通常依赖复杂的管道和合成数据，难以实现有效对齐。

**核心思路**：论文的核心思路是将幻觉问题视为对齐问题，通过CHAIR指标来优化生成内容的偏好，直接引导模型生成更准确的答案。这样的设计旨在简化训练过程，避免依赖复杂的合成数据。

**技术框架**：整体架构包括使用CHAIR指标评估生成答案的优劣，利用直接偏好优化（DPO）对现成的MLLMs进行微调。主要模块包括生成答案的评估、偏好选择和模型微调。

**关键创新**：CHAIR-DPO方法的创新在于利用CHAIR指标进行偏好优化，区别于以往依赖复杂合成数据的对齐方法。这种方法不仅简化了训练流程，还提高了模型生成答案的准确性。

**关键设计**：在技术细节上，CHAIR指标用于评估生成答案的幻觉程度，DPO则通过优化损失函数来调整模型的生成偏好。具体参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，CHAIR-DPO在多个幻觉基准测试中显著降低了幻觉答案的比例，具体提升幅度达到XX%（具体数据需查阅原文），相较于基线方法表现出更优的性能，验证了CHAIR基础奖励的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动内容生成和多模态交互系统等。通过减少幻觉现象，CHAIR-DPO能够提升用户体验和系统的可靠性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) emerge as a unified interface to address a multitude of tasks, ranging from NLP to computer vision. Despite showcasing state-of-the-art results in many benchmarks, a long-standing issue is the tendency of MLLMs to hallucinate, that is to generate answers to the user's query that are not reflected in the visual input. In this paper, we address the problem of hallucinations as an alignment problem, seeking to steer the MLLM so that it prefers generating content without hallucinations. In contrast to recent approaches that require complicated pipelines to build synthetic preference data for alignment training, often relying on proprietary models, we capitalize on the well-known CHAIR metric, originally proposed to gauge the degree of hallucinations in image captioning. Given a pair of generated answers, we leverage CHAIR to distinguish winner and loser options (i.e., non-hallucinated and hallucinated samples) and fine-tune off-the-shelf MLLMs via Direct Preference Optimization (DPO). The resulting method, which we refer to as CHAIR-DPO, effectively diminishes the amount of hallucinated answers on several hallucination benchmarks, demonstrating the effectiveness of fine-tuning the MLLM with a CHAIR-based reward. Source code and trained models are publicly available at https://github.com/aimagelab/CHAIR-DPO.

