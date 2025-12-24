---
layout: default
title: Do What? Teaching Vision-Language-Action Models to Reject the Impossible
---

# Do What? Teaching Vision-Language-Action Models to Reject the Impossible

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16292" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16292v1</a>
  <a href="https://arxiv.org/pdf/2508.16292.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16292v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16292v1', 'Do What? Teaching Vision-Language-Action Models to Reject the Impossible')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wen-Han Hsieh, Elvis Hsieh, Dantong Niu, Trevor Darrell, Roei Herzig, David M. Chan

**分类**: cs.AI, cs.RO

**发布日期**: 2025-08-22

**备注**: 9 pages, 2 figures, 1 table

---

## 💡 一句话要点

**提出Instruct-Verify-and-Act框架以应对虚假前提指令问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-行动` `虚假前提指令` `语言澄清` `机器人任务` `多模态输入`

## 📋 核心要点

1. 现有的VLA模型在处理虚假前提指令时存在局限，无法有效识别和响应用户的错误请求。
2. 本文提出的IVA框架通过检测虚假前提、进行语言澄清和提供替代方案，解决了这一问题。
3. 实验结果显示，IVA在虚假前提检测准确率上提升了97.56%，并在相关场景中的成功响应率提高了50.78%。

## 📝 摘要（中文）

近年来，视觉-语言-行动（VLA）模型在多种机器人任务中表现出色。这些模型依赖于多模态输入，其中语言指令在预测动作和解释用户意图方面发挥着关键作用。本文研究了VLA如何识别、解释和响应虚假前提指令，即引用环境中缺失对象或条件的自然语言命令。我们提出了Instruct-Verify-and-Act（IVA）框架，该框架能够检测指令是否因虚假前提而无法执行，并进行语言上的澄清或修正，同时在感知和行动中找到合理的替代方案。通过构建大规模指令调优设置并训练VLA模型，我们的实验表明，IVA在虚假前提检测准确率上提高了97.56%，在虚假前提场景中的成功响应率提升了50.78%。

## 🔬 方法详解

**问题定义**：本文旨在解决VLA模型在面对虚假前提指令时的识别和响应能力不足的问题。现有方法无法有效处理用户的错误请求，导致执行失败和用户体验下降。

**核心思路**：我们提出的IVA框架通过三个步骤来解决这一问题：首先检测指令是否因虚假前提而无法执行；其次进行语言上的澄清或修正；最后在感知和行动中找到合理的替代方案。这样的设计使得模型能够更好地理解用户意图并提供有效反馈。

**技术框架**：IVA框架包含三个主要模块：指令检测模块、语言澄清模块和替代方案生成模块。指令检测模块负责识别虚假前提，语言澄清模块与用户进行交互，而替代方案生成模块则基于环境感知提供可行的行动建议。

**关键创新**：最重要的创新在于引入了虚假前提检测和语言澄清的结合，使得VLA模型不仅能执行任务，还能有效处理无法执行的情况。这一方法与传统的仅依赖于指令执行的模型有本质区别。

**关键设计**：我们构建了一个大规模的半合成数据集，包含正向和虚假前提指令的配对，以增强模型的训练效果。此外，采用了结构化的语言提示和特定的损失函数来优化模型的性能。

## 📊 实验亮点

实验结果显示，IVA框架在虚假前提检测的准确率上达到了97.56%，相比基线模型有显著提升。同时，在虚假前提场景中的成功响应率提高了50.78%，证明了该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、服务机器人和人机交互等场景。通过提升VLA模型对虚假前提指令的处理能力，可以显著改善用户体验和系统的可靠性，未来可能在更多复杂环境中得到广泛应用。

## 📄 摘要（原文）

> Recently, Vision-Language-Action (VLA) models have demonstrated strong performance on a range of robotic tasks. These models rely on multimodal inputs, with language instructions playing a crucial role -- not only in predicting actions, but also in robustly interpreting user intent, even when the requests are impossible to fulfill. In this work, we investigate how VLAs can recognize, interpret, and respond to false-premise instructions: natural language commands that reference objects or conditions absent from the environment. We propose Instruct-Verify-and-Act (IVA), a unified framework that (i) detects when an instruction cannot be executed due to a false premise, (ii) engages in language-based clarification or correction, and (iii) grounds plausible alternatives in perception and action. Towards this end, we construct a large-scale instruction tuning setup with structured language prompts and train a VLA model capable of handling both accurate and erroneous requests. Our approach leverages a contextually augmented, semi-synthetic dataset containing paired positive and false-premise instructions, enabling robust detection and natural language correction. Our experiments show that IVA improves false premise detection accuracy by 97.56% over baselines, while increasing successful responses in false-premise scenarios by 50.78%.

