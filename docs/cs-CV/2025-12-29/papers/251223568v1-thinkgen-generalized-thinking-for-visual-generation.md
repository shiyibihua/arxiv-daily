---
layout: default
title: "ThinkGen: Generalized Thinking for Visual Generation"
---

# ThinkGen: Generalized Thinking for Visual Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23568" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23568v1</a>
  <a href="https://arxiv.org/pdf/2512.23568.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23568v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23568v1', 'ThinkGen: Generalized Thinking for Visual Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyu Jiao, Yiheng Lin, Yujie Zhong, Qi She, Wei Zhou, Xiaohan Lan, Zilong Huang, Fei Yu, Yingchen Yu, Yunqing Zhao, Yao Zhao, Yunchao Wei

**分类**: cs.CV

**发布日期**: 2025-12-29

**🔗 代码/项目**: [GITHUB](https://github.com/jiaosiyuu/ThinkGen)

---

## 💡 一句话要点

**ThinkGen：提出基于广义思维的视觉生成框架，提升多场景适应性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉生成` `多模态大语言模型` `思维链` `扩散模型` `强化学习` `图像编辑` `文本到图像生成`

## 📋 核心要点

1. 现有方法在生成任务中应用CoT推理受限于特定场景机制，缺乏泛化性和适应性。
2. ThinkGen利用MLLM的CoT推理能力，通过解耦架构和可分离训练范式实现跨场景的视觉生成。
3. 实验结果表明，ThinkGen在多个生成基准测试中取得了领先的性能表现。

## 📝 摘要（中文）

本文提出ThinkGen，一种基于思维驱动的视觉生成框架，旨在利用多模态大型语言模型（MLLM）的思维链（CoT）推理能力，解决生成任务中场景泛化性不足的问题。ThinkGen采用解耦架构，包含预训练的MLLM和扩散Transformer（DiT）。MLLM根据用户意图生成定制指令，DiT在指令引导下生成高质量图像。此外，论文提出一种可分离的基于GRPO的训练范式（SepGRPO），在MLLM和DiT模块之间交替进行强化学习。这种灵活的设计支持跨多个数据集的联合训练，从而促进CoT推理在各种生成场景中的有效应用。大量实验表明，ThinkGen在多个生成基准测试中实现了稳健的、最先进的性能。

## 🔬 方法详解

**问题定义**：现有视觉生成方法在利用多模态大语言模型（MLLM）的思维链（CoT）推理能力时，往往针对特定场景设计，导致模型在面对不同生成任务时泛化能力不足。这些方法缺乏一种通用的机制，能够有效地利用MLLM的推理能力来指导图像生成，从而限制了其在更广泛场景中的应用。

**核心思路**：ThinkGen的核心思路是将视觉生成过程分解为两个阶段：首先，利用MLLM的CoT推理能力，根据用户意图生成详细的指令；然后，利用扩散Transformer（DiT）在这些指令的引导下生成高质量的图像。这种解耦的设计使得MLLM可以专注于推理，而DiT可以专注于图像生成，从而提高了整体的效率和效果。

**技术框架**：ThinkGen的整体架构包含两个主要模块：一个预训练的MLLM和一个扩散Transformer（DiT）。用户输入文本或图像，MLLM根据输入生成一系列的推理步骤和最终的生成指令。这些指令被传递给DiT，DiT根据指令生成最终的图像。为了更好地训练这两个模块，论文提出了一个可分离的基于GRPO的训练范式（SepGRPO），该范式交替地对MLLM和DiT进行强化学习。

**关键创新**：ThinkGen的关键创新在于其解耦的架构和可分离的训练范式。解耦架构使得MLLM和DiT可以独立地进行优化，从而提高了整体的性能。可分离的训练范式允许在不同的数据集上联合训练MLLM和DiT，从而提高了模型的泛化能力。此外，ThinkGen是第一个显式地利用MLLM的CoT推理能力来指导视觉生成的框架。

**关键设计**：SepGRPO训练范式是关键设计之一，它通过交替强化学习的方式，分别优化MLLM和DiT。具体来说，首先固定DiT，利用强化学习优化MLLM，使其生成更有效的指令；然后固定MLLM，利用强化学习优化DiT，使其更好地理解和执行指令。这种交替优化的方式可以有效地提高整体的性能。此外，损失函数的设计也至关重要，需要平衡生成图像的质量和与指令的一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23568v1/x3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23568v1/x4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23568v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ThinkGen在多个生成基准测试中取得了显著的性能提升。例如，在文本到图像生成任务中，ThinkGen的FID得分优于现有方法，表明其生成的图像质量更高。此外，ThinkGen在图像编辑任务中也表现出色，能够根据用户指令对图像进行精确的修改。实验结果表明，ThinkGen能够有效地利用MLLM的CoT推理能力来指导视觉生成，从而提高了整体的性能。

## 🎯 应用场景

ThinkGen具有广泛的应用前景，包括图像编辑、图像生成、艺术创作、产品设计等领域。它可以用于根据用户提供的文本描述或草图生成高质量的图像，也可以用于对现有图像进行编辑和修改。此外，ThinkGen还可以应用于虚拟现实、游戏开发等领域，为用户提供更加逼真和沉浸式的体验。未来，ThinkGen有望成为视觉生成领域的重要工具，推动相关技术的发展。

## 📄 摘要（原文）

> Recent progress in Multimodal Large Language Models (MLLMs) demonstrates that Chain-of-Thought (CoT) reasoning enables systematic solutions to complex understanding tasks. However, its extension to generation tasks remains nascent and limited by scenario-specific mechanisms that hinder generalization and adaptation. In this work, we present ThinkGen, the first think-driven visual generation framework that explicitly leverages MLLM's CoT reasoning in various generation scenarios. ThinkGen employs a decoupled architecture comprising a pretrained MLLM and a Diffusion Transformer (DiT), wherein the MLLM generates tailored instructions based on user intent, and DiT produces high-quality images guided by these instructions. We further propose a separable GRPO-based training paradigm (SepGRPO), alternating reinforcement learning between the MLLM and DiT modules. This flexible design enables joint training across diverse datasets, facilitating effective CoT reasoning for a wide range of generative scenarios. Extensive experiments demonstrate that ThinkGen achieves robust, state-of-the-art performance across multiple generation benchmarks. Code is available: https://github.com/jiaosiyuu/ThinkGen

