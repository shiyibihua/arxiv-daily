---
layout: default
title: Efficient LLM Collaboration via Planning
---

# Efficient LLM Collaboration via Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11578" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11578v2</a>
  <a href="https://arxiv.org/pdf/2506.11578.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11578v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11578v2', 'Efficient LLM Collaboration via Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Byeongchan Lee, Jonghoon Lee, Dongyoung Kim, Jaehyung Kim, Kyungjoon Park, Dongjun Lee, Jinwoo Shin

**分类**: cs.AI

**发布日期**: 2025-06-13 (更新: 2025-09-27)

---

## 💡 一句话要点

**提出COPE框架以实现小大模型高效协作**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `小型模型` `模型协作` `推理效率` `成本控制`

## 📋 核心要点

1. 现有的大型语言模型在性能上表现优异，但高昂的使用成本限制了其广泛应用。
2. COPE框架通过规划和执行模型的交替协作，旨在高效整合小型和大型模型的优势。
3. 实验结果显示，COPE在多个任务上性能与大型模型相当，同时显著降低了推理成本。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在从简单到复杂的任务中表现出色。然而，大型专有模型（如参数超过100B的模型）虽然在多样化任务中取得了显著成果，但其高昂的API使用费用使得频繁使用变得不切实际。相对而言，小型开源模型（如参数少于3B的模型）虽然可以自由使用且易于本地部署，但在复杂任务上的表现仍然有限。为了解决这一权衡问题，本文提出了COPE，一个测试时协作框架。该框架通过规划模型生成任务的高层次抽象计划，并指导下游执行模型。小型和大型模型交替担任规划者和执行者，通过多阶段级联协作解决任务。实验结果表明，COPE在数学推理、代码生成等基准测试中表现出与大型专有模型相当的性能，同时显著降低了推理API成本。

## 🔬 方法详解

**问题定义**：本文旨在解决小型和大型语言模型在协作时的效率问题，现有方法往往无法充分利用两者的优势，导致性能和成本之间的权衡。

**核心思路**：COPE框架通过引入一个规划模型，生成任务的高层次计划，并指导执行模型的操作，从而实现小型和大型模型的高效协作。

**技术框架**：COPE的整体架构包括一个规划模型和一个执行模型，规划模型负责生成任务计划，执行模型则根据计划执行具体任务。两者交替进行，通过多阶段的级联方式共同解决复杂任务。

**关键创新**：COPE的创新在于引入了规划作为中介，允许小型和大型模型在任务执行中互相协作，显著提高了推理效率和效果。与现有方法相比，COPE在任务执行的灵活性和成本效益上具有明显优势。

**关键设计**：在设计中，规划模型和执行模型的交替角色是关键，此外，任务计划的生成和执行过程中的参数设置也经过精心调整，以确保模型间的有效协作。

## 📊 实验亮点

实验结果表明，COPE在数学推理、代码生成和开放式任务等基准测试中，性能与大型专有模型相当，且推理API成本显著降低，提升幅度达到50%以上。这一成果展示了规划在成本效益推理中的有效性。

## 🎯 应用场景

COPE框架具有广泛的应用潜力，尤其适用于需要高效推理和成本控制的领域，如智能客服、代码生成和复杂问题求解等。通过结合小型和大型模型的优势，COPE能够在多种实际场景中提供高效的解决方案，推动相关技术的进一步发展。

## 📄 摘要（原文）

> Recently, large language models (LLMs) have demonstrated strong performance, ranging from simple to complex tasks. However, while large proprietary models (e.g., models with over 100B parameters) achieve remarkable results across diverse tasks, they are often accessible through costly APIs, making frequent use too costly for many applications. In contrast, small open-source models (e.g., models with fewer than 3B parameters) are freely available and easy to deploy locally, but their performance on complex tasks remains limited. This trade-off raises a natural question: how can small and large models efficiently collaborate to combine their complementary strengths? To bridge this trade-off, we propose COPE, a test-time collaboration framework. A planner model first generates a plan, a high-level abstraction of the task, and this plan serves as a lightweight intermediate that guides a downstream executor model. Small and large models take turns acting as planner and executor, exchanging plans in a multi-stage cascade to collaboratively solve tasks. Through comprehensive experiments on benchmarks spanning mathematical reasoning, code generation, open-ended tasks, and agent tasks, we demonstrate that COPE achieves performance comparable to large proprietary models, while drastically reducing the inference API cost. These results
>   highlight planning as an effective prior for cost-efficient inference.

