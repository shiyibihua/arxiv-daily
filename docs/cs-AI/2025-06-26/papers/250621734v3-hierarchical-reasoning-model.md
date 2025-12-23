---
layout: default
title: Hierarchical Reasoning Model
---

# Hierarchical Reasoning Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21734" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21734v3</a>
  <a href="https://arxiv.org/pdf/2506.21734.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21734v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21734v3', 'Hierarchical Reasoning Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guan Wang, Jin Li, Yuhao Sun, Xing Chen, Changling Liu, Yue Wu, Meng Lu, Sen Song, Yasin Abbasi Yadkori

**分类**: cs.AI, cs.LG

**发布日期**: 2025-06-26 (更新: 2025-08-04)

---

## 💡 一句话要点

**提出层次推理模型以解决复杂推理任务的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `层次推理` `复杂推理` `递归神经网络` `人工智能` `通用计算` `样本效率` `智能系统`

## 📋 核心要点

1. 现有的大型语言模型在推理任务中面临任务分解脆弱和高延迟等挑战。
2. 本文提出的层次推理模型通过高低层次的递归模块实现高效的推理过程，灵感来源于人脑的处理方式。
3. HRM在复杂推理任务上仅使用1000个样本，且无需预训练，表现优异，超越了更大模型的性能。

## 📝 摘要（中文）

推理是制定和执行复杂目标导向行动序列的过程，仍然是人工智能中的一项关键挑战。目前的大型语言模型（LLMs）主要采用链式思维（CoT）技术，但存在任务分解脆弱、数据需求庞大和延迟高等问题。受到人脑层次和多时间尺度处理的启发，本文提出了层次推理模型（HRM），这是一种新颖的递归架构，能够在保持训练稳定性和效率的同时实现显著的计算深度。HRM通过两个相互依赖的递归模块执行顺序推理任务：高层模块负责缓慢的抽象规划，低层模块处理快速的详细计算。HRM仅用2700万参数，在仅1000个训练样本的情况下，在复杂推理任务上表现出色。该模型无需预训练或CoT数据，仍在复杂数独和大型迷宫的最优路径寻找等挑战性任务上几乎完美地完成。HRM在抽象与推理语料库（ARC）上超越了更大模型，显示出其在通用计算和通用推理系统方面的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决复杂推理任务中的效率和稳定性问题，现有方法如链式思维（CoT）存在脆弱性和高数据需求的痛点。

**核心思路**：层次推理模型（HRM）通过设计两个相互依赖的递归模块，分别负责高层的抽象规划和低层的快速计算，从而实现高效的推理过程。

**技术框架**：HRM的整体架构包括高层模块和低层模块。高层模块进行缓慢的抽象思考，而低层模块则快速处理具体细节，二者协同工作以完成推理任务。

**关键创新**：HRM的主要创新在于其层次化的递归结构，能够在单次前向传播中执行复杂推理，而不需要显式监督中间过程，这与现有方法有本质区别。

**关键设计**：HRM仅使用2700万参数，且在训练过程中不依赖于预训练或链式思维数据，显示出其在样本效率和计算能力上的优势。

## 📊 实验亮点

HRM在复杂推理任务上仅使用1000个训练样本，且无需预训练，几乎完美地解决了复杂数独和大型迷宫的最优路径问题。此外，HRM在抽象与推理语料库（ARC）上超越了更大模型，显示出其在推理能力上的显著提升。

## 🎯 应用场景

层次推理模型（HRM）在复杂推理任务中的优异表现使其在多个领域具有潜在应用价值，包括智能助手、自动化决策系统和复杂问题求解等。未来，HRM有望推动通用人工智能的发展，提升机器在复杂环境中的推理能力。

## 📄 摘要（原文）

> Reasoning, the process of devising and executing complex goal-oriented action sequences, remains a critical challenge in AI. Current large language models (LLMs) primarily employ Chain-of-Thought (CoT) techniques, which suffer from brittle task decomposition, extensive data requirements, and high latency. Inspired by the hierarchical and multi-timescale processing in the human brain, we propose the Hierarchical Reasoning Model (HRM), a novel recurrent architecture that attains significant computational depth while maintaining both training stability and efficiency. HRM executes sequential reasoning tasks in a single forward pass without explicit supervision of the intermediate process, through two interdependent recurrent modules: a high-level module responsible for slow, abstract planning, and a low-level module handling rapid, detailed computations. With only 27 million parameters, HRM achieves exceptional performance on complex reasoning tasks using only 1000 training samples. The model operates without pre-training or CoT data, yet achieves nearly perfect performance on challenging tasks including complex Sudoku puzzles and optimal path finding in large mazes. Furthermore, HRM outperforms much larger models with significantly longer context windows on the Abstraction and Reasoning Corpus (ARC), a key benchmark for measuring artificial general intelligence capabilities. These results underscore HRM's potential as a transformative advancement toward universal computation and general-purpose reasoning systems.

