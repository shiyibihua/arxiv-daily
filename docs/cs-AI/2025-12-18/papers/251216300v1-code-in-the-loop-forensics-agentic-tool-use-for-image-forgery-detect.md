---
layout: default
title: Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection
---

# Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16300" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16300v1</a>
  <a href="https://arxiv.org/pdf/2512.16300.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16300v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16300v1', 'Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fanrui Zhang, Qiang Zhang, Sizhuo Zhou, Jianwen Sun, Chuanhao Li, Jiaxin Ai, Yukang Feng, Yujie Zhang, Wenjie Li, Zizhen Li, Yifan Chang, Jiawei Liu, Kaipeng Zhang

**分类**: cs.AI

**发布日期**: 2025-12-18

**备注**: 11 pages, 6 figures

---

## 💡 一句话要点

**提出ForenAgent以解决图像伪造检测中的信息流不统一问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像伪造检测` `多模态大语言模型` `动态推理循环` `工具交互` `冷启动` `强化微调` `数据集构建` `反思推理`

## 📋 核心要点

1. 现有图像伪造检测方法在信息流的统一性和交互建模上存在显著不足，难以有效结合低级特征与高级语义知识。
2. 本文提出ForenAgent框架，通过多轮交互使MLLMs能够生成和优化低级工具，从而实现灵活的伪造检测。
3. 实验结果显示，ForenAgent在复杂的图像伪造检测任务中表现出色，具备工具使用能力和反思推理能力，推动了该领域的发展。

## 📝 摘要（中文）

现有的图像伪造检测方法要么利用低级、无语义的伪造特征，要么依赖于具有高级语义知识的多模态大语言模型（MLLMs）。这两种信息流在范式和推理上高度异质，使得现有方法难以统一或有效建模它们的跨层次交互。为了解决这一问题，本文提出了ForenAgent，一个多轮交互的图像伪造检测框架，能够自主生成、执行并迭代优化基于Python的低级工具，从而实现更灵活和可解释的伪造分析。ForenAgent采用了结合冷启动和强化微调的两阶段训练流程，逐步增强其工具交互能力和推理适应性。通过构建FABench数据集，实验表明ForenAgent在低级工具的辅助下，展现出工具使用能力和反思推理能力，为通用图像伪造检测开辟了新的方向。

## 🔬 方法详解

**问题定义**：本文旨在解决现有图像伪造检测方法在低级特征与高级语义知识之间的异质性问题，导致信息流难以统一和交互建模的痛点。

**核心思路**：ForenAgent框架通过多轮交互，使得多模态大语言模型能够自主生成、执行和优化低级工具，从而实现更灵活和可解释的伪造分析。该设计灵感来源于人类的推理过程，强调动态推理循环。

**技术框架**：ForenAgent采用两阶段训练流程，包括冷启动和强化微调，增强工具交互能力和推理适应性。动态推理循环包含全球感知、局部聚焦、迭代探测和整体裁决，作为数据采样策略和任务对齐过程奖励的实例。

**关键创新**：最重要的创新在于引入了动态推理循环和多轮交互机制，使得低级工具与高级语义知识能够有效结合，提升了图像伪造检测的灵活性和可解释性。

**关键设计**：在训练过程中，FABench数据集的构建提供了100k张图像和约200k个代理交互问答对，确保了系统的系统性训练和评估。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16300v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16300v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16300v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ForenAgent在图像伪造检测任务中展现出显著的性能提升，尤其是在低级工具的辅助下，表现出工具使用能力和反思推理能力。具体性能数据尚未披露，但实验表明其在复杂任务中的有效性，为通用图像伪造检测提供了新的可能性。

## 🎯 应用场景

该研究的潜在应用领域包括数字图像取证、社交媒体内容验证以及新闻报道的真实性检查等。通过提升图像伪造检测的灵活性和准确性，ForenAgent能够在打击虚假信息和保护数字内容的真实性方面发挥重要作用，具有显著的实际价值和未来影响。

## 📄 摘要（原文）

> Existing image forgery detection (IFD) methods either exploit low-level, semantics-agnostic artifacts or rely on multimodal large language models (MLLMs) with high-level semantic knowledge. Although naturally complementary, these two information streams are highly heterogeneous in both paradigm and reasoning, making it difficult for existing methods to unify them or effectively model their cross-level interactions. To address this gap, we propose ForenAgent, a multi-round interactive IFD framework that enables MLLMs to autonomously generate, execute, and iteratively refine Python-based low-level tools around the detection objective, thereby achieving more flexible and interpretable forgery analysis. ForenAgent follows a two-stage training pipeline combining Cold Start and Reinforcement Fine-Tuning to enhance its tool interaction capability and reasoning adaptability progressively. Inspired by human reasoning, we design a dynamic reasoning loop comprising global perception, local focusing, iterative probing, and holistic adjudication, and instantiate it as both a data-sampling strategy and a task-aligned process reward. For systematic training and evaluation, we construct FABench, a heterogeneous, high-quality agent-forensics dataset comprising 100k images and approximately 200k agent-interaction question-answer pairs. Experiments show that ForenAgent exhibits emergent tool-use competence and reflective reasoning on challenging IFD tasks when assisted by low-level tools, charting a promising route toward general-purpose IFD. The code will be released after the review process is completed.

