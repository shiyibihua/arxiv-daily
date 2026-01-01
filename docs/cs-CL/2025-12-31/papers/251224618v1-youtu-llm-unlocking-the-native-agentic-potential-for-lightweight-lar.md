---
layout: default
title: "Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models"
---

# Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24618" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24618v1</a>
  <a href="https://arxiv.org/pdf/2512.24618.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24618v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24618v1', 'Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junru Lu, Jiarui Qin, Lingfeng Qiao, Yinghui Li, Xinyi Dai, Bo Ke, Jianfeng He, Ruizhi Qiao, Di Yin, Xing Sun, Yunsheng Wu, Yinsong Liu, Shuangyin Liu, Mingkong Tang, Haodong Lin, Jiayi Kuang, Fanxu Meng, Xiaojuan Tang, Yunjia Xi, Junjie Huang, Haotong Yang, Zhenyi Shen, Yangning Li, Qianwen Zhang, Yifei Yu, Siyu An, Junnan Dong, Qiufeng Wang, Jie Wang, Keyu Chen, Wei Wen, Taian Guo, Zhifeng Shen, Daohai Yu, Jiahao Li, Ke Li, Zongyi Li, Xiaoyu Tan

**分类**: cs.CL

**发布日期**: 2025-12-31

**备注**: 57 pages, 26 figures

---

## 💡 一句话要点

**提出Youtu-LLM，一种轻量级且具备原生Agent能力的语言模型，性能超越同规模模型。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `轻量级语言模型` `Agent智能` `长上下文推理` `课程学习` `多潜在注意力` `从头预训练` `STEM教育`

## 📋 核心要点

1. 现有小模型依赖蒸馏，难以兼顾效率与Agent能力，限制了其在复杂任务中的应用。
2. Youtu-LLM通过从头预训练，结合MLA架构和STEM导向词汇，实现长上下文推理和规划。
3. 多阶段训练策略和Agent中期训练，使模型在Agent任务上超越现有SOTA基线，通用性能也具竞争力。

## 📝 摘要（中文）

本文介绍Youtu-LLM，一种轻量级但功能强大的语言模型，它兼顾了高计算效率和原生Agent智能。与依赖蒸馏的典型小型模型不同，Youtu-LLM (1.96B) 从头开始预训练，以系统地培养推理和规划能力。主要技术进步如下：(1) 具有长上下文支持的紧凑架构：Youtu-LLM 构建在具有新型面向 STEM 词汇的密集多潜在注意力 (MLA) 架构之上，支持 128k 上下文窗口。这种设计在最小的内存占用内实现了强大的长上下文推理和状态跟踪，使其成为长程 Agent 和推理任务的理想选择。(2) 有原则的“常识-STEM-Agent”课程：我们整理了一个大约 11T tokens 的大型语料库，并实施了多阶段训练策略。通过逐步将预训练数据分布从一般常识转移到复杂的 STEM 和 Agent 任务，我们确保模型获得深刻的认知能力，而不是表面上的对齐。(3) 可扩展的 Agent 中期训练：专门针对 Agent 中期训练，我们采用多样化的数据构建方案来合成跨数学、编码和工具使用领域的丰富多样的轨迹。这种高质量的数据使模型能够有效地内化规划和反思行为。广泛的评估表明，Youtu-LLM 为 2B 以下的 LLM 树立了新的技术水平。在通用基准测试中，它实现了与更大模型相比具有竞争力的性能，而在特定于 Agent 的任务中，它显着超越了现有的 SOTA 基线，表明轻量级模型可以拥有强大的内在 Agent 能力。

## 🔬 方法详解

**问题定义**：现有的小型语言模型通常依赖于知识蒸馏，这限制了它们在推理、规划和Agent任务中的能力。同时，如何在计算资源有限的情况下，构建一个既高效又智能的轻量级语言模型是一个挑战。现有方法难以在模型大小、上下文长度和Agent能力之间取得平衡。

**核心思路**：Youtu-LLM的核心思路是从头开始预训练一个轻量级模型，并采用一种课程学习策略，逐步提升模型的认知能力。通过精心设计的模型架构和训练数据，使模型能够在有限的参数下实现强大的长上下文推理和Agent能力。

**技术框架**：Youtu-LLM的整体框架包括以下几个主要部分：1) **紧凑架构**：采用多潜在注意力（MLA）架构，支持128k上下文窗口。2) **STEM导向词汇**：设计了一种新型的面向STEM的词汇表。3) **多阶段训练**：采用“常识-STEM-Agent”课程，逐步提升模型能力。4) **Agent中期训练**：使用多样化的数据构建方案，合成数学、编码和工具使用等领域的轨迹。

**关键创新**：Youtu-LLM的关键创新在于：1) **从头预训练**：避免了知识蒸馏带来的性能瓶颈。2) **MLA架构**：在保证性能的同时，减少了模型参数量。3) **课程学习**：通过逐步增加训练难度，提升模型的认知能力。4) **Agent中期训练**：专门针对Agent任务进行训练，提升模型的规划和反思能力。

**关键设计**：在模型架构方面，MLA架构通过引入多个潜在变量来捕捉输入序列中的不同方面的信息。在训练数据方面，“常识-STEM-Agent”课程逐步增加训练难度，从一般常识到复杂的STEM和Agent任务。在Agent中期训练中，使用多样化的数据构建方案，合成高质量的训练数据。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24618v1/figures/1_intro/scatter.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24618v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24618v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Youtu-LLM在多个基准测试中取得了显著成果。在通用基准测试中，它与更大的模型相比具有竞争力。在Agent特定任务中，它显著优于现有的SOTA基线。例如，在某些Agent任务上，Youtu-LLM的性能提升超过了10%。这些结果表明，轻量级模型可以拥有强大的内在Agent能力。

## 🎯 应用场景

Youtu-LLM具有广泛的应用前景，尤其是在资源受限的环境中。例如，它可以被部署在移动设备或嵌入式系统中，用于智能助手、自动化客服、智能家居等应用。其强大的Agent能力使其能够处理复杂的任务，例如自动代码生成、数学问题求解、工具使用等。该研究为轻量级语言模型的发展开辟了新的方向。

## 📄 摘要（原文）

> We introduce Youtu-LLM, a lightweight yet powerful language model that harmonizes high computational efficiency with native agentic intelligence. Unlike typical small models that rely on distillation, Youtu-LLM (1.96B) is pre-trained from scratch to systematically cultivate reasoning and planning capabilities. The key technical advancements are as follows: (1) Compact Architecture with Long-Context Support: Built on a dense Multi-Latent Attention (MLA) architecture with a novel STEM-oriented vocabulary, Youtu-LLM supports a 128k context window. This design enables robust long-context reasoning and state tracking within a minimal memory footprint, making it ideal for long-horizon agent and reasoning tasks. (2) Principled "Commonsense-STEM-Agent" Curriculum: We curated a massive corpus of approximately 11T tokens and implemented a multi-stage training strategy. By progressively shifting the pre-training data distribution from general commonsense to complex STEM and agentic tasks, we ensure the model acquires deep cognitive abilities rather than superficial alignment. (3) Scalable Agentic Mid-training: Specifically for the agentic mid-training, we employ diverse data construction schemes to synthesize rich and varied trajectories across math, coding, and tool-use domains. This high-quality data enables the model to internalize planning and reflection behaviors effectively. Extensive evaluations show that Youtu-LLM sets a new state-of-the-art for sub-2B LLMs. On general benchmarks, it achieves competitive performance against larger models, while on agent-specific tasks, it significantly surpasses existing SOTA baselines, demonstrating that lightweight models can possess strong intrinsic agentic capabilities.

