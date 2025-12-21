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

**对比单智能体与多智能体框架，评估其在图解几何问题求解中的性能差异**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `图解几何问题求解` `多模态大语言模型` `视觉推理` `智能教育`

## 📋 核心要点

1. 现有的多模态大语言模型在图解几何问题求解中面临挑战，尤其是在复杂推理和视觉信息利用方面。
2. 论文对比单智能体和多智能体框架，旨在探究多智能体架构是否能有效提升几何问题求解能力。
3. 实验结果表明，多智能体框架对开源模型有显著提升，对闭源模型在较新数据集上也有一定帮助。

## 📝 摘要（中文）

图解几何问题求解是多模态大型语言模型（MLLM）的关键基准，但多智能体设计相对于单智能体的优势尚不明确。本文系统地比较了单智能体和多智能体流程在四个视觉数学基准（Geometry3K、MathVerse、OlympiadBench 和 We-Math）上的性能。对于开源模型，多智能体方法始终能提高性能。例如，Qwen-2.5-VL (7B) 在 Geometry3K 上获得了 +6.8 的提升，Qwen-2.5-VL (32B) 获得了 +3.3 的提升，并且两种 Qwen-2.5-VL 变体在 OlympiadBench 和 We-Math 上都获得了进一步的提升。相比之下，闭源模型 Gemini-2.0-Flash 在经典基准测试中通常在单智能体模式下表现更好，而多智能体仅在新数据集 We-Math 上产生了适度的改进。这些发现表明，多智能体流程为开源模型提供了明显的优势，并且可以帮助强大的专有系统处理较新的、不太熟悉的基准，但智能体分解并非普遍最佳。

## 🔬 方法详解

**问题定义**：论文旨在解决图解几何问题，即给定几何图形和问题描述，求解几何问题。现有方法，特别是单智能体方法，在处理复杂几何问题时，推理能力和视觉信息利用效率存在瓶颈，难以达到理想的准确率。

**核心思路**：论文的核心思路是利用多智能体系统，将复杂的几何问题分解为多个子任务，每个智能体负责不同的子任务，例如理解问题、提取图形信息、进行数学推理等。通过智能体之间的协作，提高问题求解的效率和准确性。这种分解的目的是为了更好地利用每个智能体的专长，并减少单个智能体的认知负担。

**技术框架**：整体框架包含单智能体和多智能体两种pipeline。单智能体pipeline直接使用MLLM模型进行问题求解。多智能体pipeline将问题分解为多个步骤，每个步骤由一个智能体负责。这些智能体之间通过消息传递进行协作，最终得到问题的答案。具体模块可能包括：问题解析模块、图形理解模块、推理模块和答案生成模块。

**关键创新**：论文的关键创新在于系统性地对比了单智能体和多智能体框架在图解几何问题求解中的性能。通过实验，揭示了多智能体框架在开源模型上的优势，并发现其在处理新数据集时对闭源模型也有帮助。与现有方法相比，该研究更全面地评估了多智能体架构在几何问题求解中的有效性。

**关键设计**：论文的关键设计包括：1) 针对不同类型的几何问题，设计不同的智能体角色和协作方式；2) 使用合适的提示工程（prompt engineering）来引导智能体的行为；3) 设计有效的消息传递机制，确保智能体之间的信息交流顺畅；4) 针对不同的模型，调整智能体的数量和功能分配。

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

实验结果表明，对于开源模型，多智能体框架在Geometry3K上取得了显著的性能提升，例如Qwen-2.5-VL (7B) 提升了6.8个点，Qwen-2.5-VL (32B) 提升了3.3个点。此外，在OlympiadBench和We-Math数据集上，开源模型也获得了进一步的提升。对于闭源模型Gemini-2.0-Flash，多智能体框架在We-Math数据集上表现出一定的优势。

## 🎯 应用场景

该研究成果可应用于智能教育、自动几何定理证明、机器人视觉等领域。通过多智能体协作，可以构建更智能的几何问题求解系统，辅助学生学习，提高几何定理证明的效率，并为机器人提供更强大的视觉推理能力。未来，该技术有望扩展到其他需要复杂推理和多模态信息融合的领域。

## 📄 摘要（原文）

> Diagram-grounded geometry problem solving is a critical benchmark for multimodal large language models (MLLMs), yet the benefits of multi-agent design over single-agent remain unclear. We systematically compare single-agent and multi-agent pipelines on four visual math benchmarks: Geometry3K, MathVerse, OlympiadBench, and We-Math. For open-source models, multi-agent consistently improves performance. For example, Qwen-2.5-VL (7B) gains +6.8 points and Qwen-2.5-VL (32B) gains +3.3 on Geometry3K, and both Qwen-2.5-VL variants see further gains on OlympiadBench and We-Math. In contrast, the closed-source Gemini-2.0-Flash generally performs better in single-agent mode on classic benchmarks, while multi-agent yields only modest improvements on the newer We-Math dataset. These findings show that multi-agent pipelines provide clear benefits for open-source models and can assist strong proprietary systems on newer, less familiar benchmarks, but agentic decomposition is not universally optimal. All code, data, and reasoning files are available at https://github.com/faiyazabdullah/Interpreter-Solver

