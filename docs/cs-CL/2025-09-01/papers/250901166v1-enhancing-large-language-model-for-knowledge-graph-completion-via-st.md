---
layout: default
title: Enhancing Large Language Model for Knowledge Graph Completion via Structure-Aware Alignment-Tuning
---

# Enhancing Large Language Model for Knowledge Graph Completion via Structure-Aware Alignment-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01166" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01166v1</a>
  <a href="https://arxiv.org/pdf/2509.01166.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01166v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01166v1', 'Enhancing Large Language Model for Knowledge Graph Completion via Structure-Aware Alignment-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Liu, Yanan Cao, Xixun Lin, Yanmin Shang, Shi Wang, Shirui Pan

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-01

**备注**: EMNLP 2025, Main, Long Paper

---

## 💡 一句话要点

**提出SAT框架，通过结构感知对齐微调增强LLM的知识图谱补全能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱补全` `大型语言模型` `结构感知对齐` `对比学习` `指令微调`

## 📋 核心要点

1. 现有LLM增强的知识图谱补全方法忽略了自然语言和图结构表示空间的不一致性，且任务指令设计冗余。
2. SAT框架通过分层知识对齐和结构指令微调，将图嵌入与自然语言空间对齐，并统一不同KGC任务的指令。
3. 实验结果表明，SAT在链接预测任务中显著优于现有方法，性能提升范围为8.7%到29.8%。

## 📝 摘要（中文）

知识图谱补全(KGC)旨在从知识图谱中推断新知识并进行预测。最近，大型语言模型(LLM)展现出了卓越的推理能力。LLM增强的KGC方法主要侧重于设计特定于任务的指令，并取得了可喜的进展。然而，仍然存在两个关键挑战。首先，现有方法通常忽略了自然语言和图结构之间不一致的表示空间。其次，大多数方法为不同的KGC任务设计单独的指令，导致重复工作和耗时的过程。为了应对这些挑战，我们提出了一种新颖的框架SAT，通过结构感知对齐微调来增强LLM的KGC能力。具体来说，我们首先引入分层知识对齐，通过多任务对比学习将图嵌入与自然语言空间对齐。然后，我们提出结构指令微调，使用统一的图指令结合轻量级知识适配器，引导LLM在KG上执行结构感知推理。在四个基准数据集上的两个KGC任务的实验结果表明，SAT显著优于最先进的方法，尤其是在链接预测任务中，改进范围从8.7%到29.8%。

## 🔬 方法详解

**问题定义**：知识图谱补全旨在预测知识图谱中缺失的关系三元组。现有基于LLM的方法主要依赖于设计特定任务的指令，但忽略了自然语言和图结构表示空间的差异，导致LLM难以有效利用图结构信息进行推理。此外，为每个KGC任务单独设计指令导致了大量重复工作。

**核心思路**：SAT框架的核心思路是通过结构感知对齐微调，弥合自然语言和图结构表示空间之间的差距，并利用统一的指令来处理不同的KGC任务。通过对齐表示空间，LLM可以更好地理解和利用图结构信息，从而提高知识图谱补全的性能。统一指令的设计减少了任务相关的指令工程，提高了效率。

**技术框架**：SAT框架包含两个主要阶段：分层知识对齐和结构指令微调。在分层知识对齐阶段，使用多任务对比学习将图嵌入与自然语言空间对齐。在结构指令微调阶段，使用统一的图指令结合轻量级知识适配器，引导LLM在知识图谱上执行结构感知推理。

**关键创新**：SAT的关键创新在于结构感知对齐微调。具体来说，分层知识对齐通过多任务对比学习，显式地将图嵌入与自然语言空间对齐，从而使LLM能够更好地理解图结构信息。结构指令微调使用统一的图指令，避免了为每个KGC任务单独设计指令的需要，提高了效率。

**关键设计**：分层知识对齐使用多任务对比学习，包含实体对齐和关系对齐两个任务。结构指令微调使用统一的图指令，该指令包含实体和关系的描述信息。轻量级知识适配器用于将图结构信息融入到LLM中。损失函数包括对比学习损失和知识图谱补全损失。

## 📊 实验亮点

实验结果表明，SAT框架在四个基准数据集上的两个KGC任务中显著优于现有方法。尤其是在链接预测任务中，SAT的性能提升范围从8.7%到29.8%。这些结果表明，结构感知对齐微调能够有效提高LLM的知识图谱补全能力。

## 🎯 应用场景

该研究成果可应用于智能问答、推荐系统、信息检索等领域，通过增强LLM对知识图谱的理解和推理能力，提高这些应用的准确性和效率。未来，该方法可以扩展到更复杂的知识图谱结构和更多的KGC任务，并应用于其他需要知识推理的场景。

## 📄 摘要（原文）

> Knowledge graph completion (KGC) aims to infer new knowledge and make predictions from knowledge graphs. Recently, large language models (LLMs) have exhibited remarkable reasoning capabilities. LLM-enhanced KGC methods primarily focus on designing task-specific instructions, achieving promising advancements. However, there are still two critical challenges. First, existing methods often ignore the inconsistent representation spaces between natural language and graph structures. Second, most approaches design separate instructions for different KGC tasks, leading to duplicate works and time-consuming processes. To address these challenges, we propose SAT, a novel framework that enhances LLMs for KGC via structure-aware alignment-tuning. Specifically, we first introduce hierarchical knowledge alignment to align graph embeddings with the natural language space through multi-task contrastive learning. Then, we propose structural instruction tuning to guide LLMs in performing structure-aware reasoning over KGs, using a unified graph instruction combined with a lightweight knowledge adapter. Experimental results on two KGC tasks across four benchmark datasets demonstrate that SAT significantly outperforms state-of-the-art methods, especially in the link prediction task with improvements ranging from 8.7% to 29.8%.

