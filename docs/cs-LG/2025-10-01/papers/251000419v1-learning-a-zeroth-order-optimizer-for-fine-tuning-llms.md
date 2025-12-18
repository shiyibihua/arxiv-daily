---
layout: default
title: Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs
---

# Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00419" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00419v1</a>
  <a href="https://arxiv.org/pdf/2510.00419.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00419v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00419v1', 'Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kairun Zhang, Haoyu Li, Yanjun Zhao, Yifan Sun, Huan Zhang

**分类**: cs.LG

**发布日期**: 2025-10-01

**🔗 代码/项目**: [GITHUB](https://github.com/ASTRAL-Group/ZO_Fine_tuner.git)

---

## 💡 一句话要点

**提出ZO Fine-tuner，一种学习型零阶优化器，用于高效微调大语言模型。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零阶优化` `大语言模型` `微调` `学习迁移` `元学习`

## 📋 核心要点

1. 现有零阶优化器依赖手工静态采样策略，无法适应不同LLM的结构特性，限制了微调效率。
2. ZO Fine-tuner通过学习高效扰动策略，为每个LLM定制优化器，实现一次训练，多次复用。
3. 实验表明，ZO Fine-tuner在多种LLM和数据集上超越现有零阶方法，展现了优越的性能和可扩展性。

## 📝 摘要（中文）

零阶优化器最近作为一种微调大型语言模型（LLMs）的实用方法而出现，与传统的一阶方法相比，显著降低了GPU内存消耗。然而，现有的零阶方法依赖于手工制作的、静态的采样策略，这些策略不能适应模型特定的结构。为了解决这个问题，我们提出了ZO Fine-tuner，一种基于学习的LLM零阶优化器，它通过紧凑且内存高效的设计自动学习高效的扰动策略。至关重要的是，我们的方法受到以下观察的推动：只有少数基础模型及其衍生物在实践中被广泛采用。因此，对于给定的LLM学习一次优化器，并在不同的下游任务中重复使用它是可行且非常理想的。因此，ZO Fine-tuner旨在通过支持每个LLM一次性训练且开销最小的方式，将学习迁移到学习（L2L）扩展到基础模型时代。在4个LLM和7个数据集上的实验表明，ZO Fine-tuner在82.1%的任务-模型组合中优于先前的零阶基线，从而证明了其在高效LLM微调方面的强大性能和可扩展性。

## 🔬 方法详解

**问题定义**：现有零阶优化器在微调大型语言模型时，采用固定的、人工设计的采样策略，无法根据不同模型的特性进行调整，导致优化效率低下。此外，针对每个下游任务都重新训练优化器会带来巨大的计算开销。

**核心思路**：论文的核心思路是利用学习迁移（L2L）的思想，为每个基础LLM学习一个定制的零阶优化器。该优化器能够自动学习高效的扰动策略，并在不同的下游任务中重复使用，从而降低计算成本并提高微调效率。这种方法基于一个关键观察：实际应用中广泛使用的基础模型数量有限。

**技术框架**：ZO Fine-tuner的整体框架包含两个主要阶段：优化器训练阶段和微调阶段。在优化器训练阶段，使用一个元学习框架，通过在多个任务上训练，使优化器能够学习到适应特定LLM结构的扰动策略。在微调阶段，将训练好的优化器应用于新的下游任务，以高效地微调LLM。

**关键创新**：ZO Fine-tuner的关键创新在于将学习迁移的思想引入到零阶优化器的设计中。与传统的静态采样策略不同，ZO Fine-tuner能够自动学习适应模型结构的扰动策略，从而提高优化效率。此外，通过一次训练，多次复用的方式，显著降低了计算成本。

**关键设计**：ZO Fine-tuner的具体设计细节包括：使用紧凑且内存高效的网络结构来表示优化器，以降低训练开销；设计合适的损失函数，以鼓励优化器学习到高效的扰动策略；采用特定的采样方法，以平衡探索和利用，从而提高优化效率。具体的参数设置和网络结构细节在论文中进行了详细描述（具体细节未知）。

## 📊 实验亮点

实验结果表明，ZO Fine-tuner在4个LLM和7个数据集上的表现优于现有的零阶优化器基线。在82.1%的任务-模型组合中，ZO Fine-tuner取得了更好的性能，证明了其在高效LLM微调方面的强大性能和可扩展性。具体的性能提升幅度在不同任务和模型上有所不同（具体数值未知）。

## 🎯 应用场景

ZO Fine-tuner可广泛应用于各种需要高效微调大型语言模型的场景，例如自然语言处理、文本生成、机器翻译等。该方法能够显著降低微调成本，加速模型迭代，并提高模型在特定任务上的性能。尤其适用于资源受限的环境，例如边缘计算设备。

## 📄 摘要（原文）

> Zeroth-order optimizers have recently emerged as a practical approach for fine-tuning large language models (LLMs), significantly reducing GPU memory consumption compared to traditional first-order methods. Yet, existing zeroth-order methods rely on hand-crafted, static sampling strategies that are not adaptable to model-specific structures. To address this, we propose ZO Fine-tuner, a learning-based zeroth-order optimizer for LLMs that automatically learns efficient perturbation strategies through a compact and memory-efficient design. Crucially, our approach is motivated by the observation that only a small number of foundation models and their derivatives are widely adopted in practice. Therefore, learning the optimizer once for a given LLM and reusing it across diverse downstream tasks is both feasible and highly desirable. Accordingly, ZO Fine-tuner is designed to scale learning to learn (L2L) to the foundation-model era by supporting one-time training per LLM with minimal overhead. Experiments on 4 LLMs and 7 datasets show that ZO Fine-tuner outperforms prior zeroth-order baselines in 82.1\% of task-model combinations, thereby demonstrating strong performance and scalability for efficient LLM fine-tuning. Our code is available at https://github.com/ASTRAL-Group/ZO_Fine_tuner.git.

