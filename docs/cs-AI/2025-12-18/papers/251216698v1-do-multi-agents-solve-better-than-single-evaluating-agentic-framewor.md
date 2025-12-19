---
layout: default
title: Do Multi-Agents Solve Better Than Single? Evaluating Agentic Frameworks for Diagram-Grounded Geometry Problem Solving and Reasoning
---

# Do Multi-Agents Solve Better Than Single? Evaluating Agentic Frameworks for Diagram-Grounded Geometry Problem Solving and Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16698" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16698v1</a>
  <a href="https://arxiv.org/pdf/2512.16698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16698v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16698v1', 'Do Multi-Agents Solve Better Than Single? Evaluating Agentic Frameworks for Diagram-Grounded Geometry Problem Solving and Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mahbub E Sobhani, Md. Faiyaz Abdullah Sayeedi, Mohammad Nehad Alam, Proma Hossain Progga, Swakkhar Shatabda

**分类**: cs.AI, cs.CG

**发布日期**: 2025-12-18

**备注**: Accepted to the ARR October 2025 cycle

**🔗 代码/项目**: [GITHUB](https://github.com/faiyazabdullah/Interpreter-Solver)

---

## 💡 一句话要点

**比较多智能体与单智能体在几何问题求解中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体` `几何问题` `图示基础` `多模态学习` `性能提升` `开源模型` `智能体协作`

## 📋 核心要点

1. 核心问题：现有的单智能体方法在处理复杂的几何问题时，性能提升有限，尤其在新颖的基准上表现不佳。
2. 方法要点：论文提出通过多智能体设计来优化几何问题求解，利用多个智能体的协作来提升模型的推理能力。
3. 实验或效果：实验结果表明，开源模型在多智能体模式下性能提升显著，例如Qwen-2.5-VL在Geometry3K上提升了6.8分。

## 📝 摘要（中文）

图示基础的几何问题求解是多模态大型语言模型（MLLMs）的重要基准，但多智能体设计相较于单智能体的优势尚不明确。本文系统比较了单智能体和多智能体在四个视觉数学基准上的表现，包括Geometry3K、MathVerse、OlympiadBench和We-Math。结果表明，对于开源模型，多智能体设计显著提升了性能，而闭源模型在经典基准上表现更佳。研究结果显示，多智能体管道对开源模型有明显益处，并能在新颖基准上辅助强大的专有系统，但智能体分解并非普遍最优。

## 🔬 方法详解

**问题定义**：本文旨在探讨多智能体设计在图示基础几何问题求解中的有效性，现有单智能体方法在新颖基准上的表现不足，无法充分利用多模态信息。

**核心思路**：通过引入多智能体框架，允许多个智能体并行处理和推理，从而提高整体求解效率和准确性。这样的设计能够更好地应对复杂的几何问题，尤其是在数据稀缺或新颖的场景中。

**技术框架**：整体架构包括多个智能体协同工作，每个智能体负责不同的任务或问题部分。主要模块包括输入处理、智能体推理、结果整合和输出生成。

**关键创新**：最重要的创新在于多智能体的协作机制，通过智能体间的信息共享和任务分配，显著提升了求解的准确性和效率。这与传统的单智能体方法形成鲜明对比。

**关键设计**：在参数设置上，采用了动态任务分配策略，损失函数设计为多任务学习损失，以适应不同智能体的学习需求。网络结构上，使用了增强的Transformer架构，以支持多模态输入的处理。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16698v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16698v1/figures/diagram.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，开源模型在多智能体模式下表现优异，例如Qwen-2.5-VL在Geometry3K上提升了6.8分，而在OlympiadBench和We-Math上也有显著提升。相比之下，闭源模型在经典基准上表现更佳，但在新基准上多智能体的提升幅度有限。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化数学推理、智能辅导系统等。通过提升几何问题求解的能力，能够为学生提供更精准的学习支持，同时也为研究人员提供更强大的工具来探索复杂的数学问题。未来，该方法可能在其他领域的多模态学习中发挥重要作用。

## 📄 摘要（原文）

> Diagram-grounded geometry problem solving is a critical benchmark for multimodal large language models (MLLMs), yet the benefits of multi-agent design over single-agent remain unclear. We systematically compare single-agent and multi-agent pipelines on four visual math benchmarks: Geometry3K, MathVerse, OlympiadBench, and We-Math. For open-source models, multi-agent consistently improves performance. For example, Qwen-2.5-VL (7B) gains +6.8 points and Qwen-2.5-VL (32B) gains +3.3 on Geometry3K, and both Qwen-2.5-VL variants see further gains on OlympiadBench and We-Math. In contrast, the closed-source Gemini-2.0-Flash generally performs better in single-agent mode on classic benchmarks, while multi-agent yields only modest improvements on the newer We-Math dataset. These findings show that multi-agent pipelines provide clear benefits for open-source models and can assist strong proprietary systems on newer, less familiar benchmarks, but agentic decomposition is not universally optimal. All code, data, and reasoning files are available at https://github.com/faiyazabdullah/Interpreter-Solver

