---
layout: default
title: Large Language Models Show Signs of Alignment with Human Neurocognition During Abstract Reasoning
---

# Large Language Models Show Signs of Alignment with Human Neurocognition During Abstract Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10057" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10057v1</a>
  <a href="https://arxiv.org/pdf/2508.10057.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10057v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10057v1', 'Large Language Models Show Signs of Alignment with Human Neurocognition During Abstract Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christopher Pinier, Sonia Acuña Vargas, Mariia Steeghs-Turchina, Dora Matzke, Claire E. Stevenson, Michael D. Nunez

**分类**: q-bio.NC, cs.AI, cs.CL

**发布日期**: 2025-08-12

**备注**: Presented at the 8th Annual Conference on Cognitive Computational Neuroscience (August 12-15, 2025; Amsterdam, The Netherlands); 20 pages, 11 figures

---

## 💡 一句话要点

**研究大型语言模型与人类抽象推理的神经认知对齐**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `抽象推理` `神经认知` `脑电图` `表征学习` `人工智能` `人机对齐`

## 📋 核心要点

1. 现有方法在抽象推理任务中，LLMs的表现与人类神经认知之间的关系尚不明确，缺乏系统性比较。
2. 本研究通过比较人类与LLMs在抽象模式完成任务中的表现，探讨其神经表征的相似性，揭示潜在的对齐机制。
3. 研究结果表明，只有最大的LLMs在准确性上与人类相当，并且在神经表征上显示出与人类的相似性，提供了新的理解视角。

## 📝 摘要（中文）

本研究探讨大型语言模型（LLMs）在抽象推理过程中是否反映人类神经认知。我们比较了人类参与者与八个开源LLMs在抽象模式完成任务中的表现和神经表征。研究发现，只有最大的LLMs（约700亿参数）达到了与人类相当的准确性，并且在模式特定的难度特征上显示出与人类的相似性。所有测试的LLMs在其中间层中形成了明显聚类的抽象模式类别，且这种聚类的强度与任务表现相关。任务最优LLM层的表征几何与人类前额脑电位（FRPs）之间存在中等正相关。这些结果表明，LLMs可能在抽象推理中反映人类大脑机制，提供了生物智能与人工智能之间共享原则的初步证据。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在抽象推理任务中与人类神经认知的对齐问题。现有方法未能系统比较LLMs与人类在此类任务中的表现及其神经机制。

**核心思路**：通过比较人类参与者与多个LLMs在抽象模式完成任务中的表现，分析其神经表征的相似性，探索LLMs是否能够反映人类的抽象推理机制。

**技术框架**：研究采用了电生理学技术（EEG）记录人类的脑电位，并与LLMs的中间层表征进行比较。主要模块包括任务设计、数据收集、神经表征分析和结果对比。

**关键创新**：本研究的创新点在于首次系统性地比较了LLMs与人类在抽象推理任务中的表现及其神经表征，揭示了两者之间的潜在对齐关系。

**关键设计**：在实验中，使用了不同类型的抽象模式任务，记录了参与者的脑电位，并分析了LLMs中间层的聚类特征。参数设置包括LLMs的规模（如700亿参数）和任务难度的设计，以确保结果的可靠性。

## 📊 实验亮点

实验结果显示，只有约700亿参数的LLMs（如Qwen-2.5-72B和DeepSeek-R1-70B）在抽象推理任务中达到了与人类相当的准确性。此外，LLMs的中间层表征在抽象模式类别的聚类上表现出明显的相似性，与人类的脑电位数据存在中等正相关，表明潜在的共享表征空间。

## 🎯 应用场景

该研究的潜在应用领域包括教育、心理学和人工智能的交叉研究。通过理解LLMs与人类认知的相似性，可以为开发更智能的教育工具和认知辅助系统提供理论基础，推动人工智能在复杂推理任务中的应用。

## 📄 摘要（原文）

> This study investigates whether large language models (LLMs) mirror human neurocognition during abstract reasoning. We compared the performance and neural representations of human participants with those of eight open-source LLMs on an abstract-pattern-completion task. We leveraged pattern type differences in task performance and in fixation-related potentials (FRPs) as recorded by electroencephalography (EEG) during the task. Our findings indicate that only the largest tested LLMs (~70 billion parameters) achieve human-comparable accuracy, with Qwen-2.5-72B and DeepSeek-R1-70B also showing similarities with the human pattern-specific difficulty profile. Critically, every LLM tested forms representations that distinctly cluster the abstract pattern categories within their intermediate layers, although the strength of this clustering scales with their performance on the task. Moderate positive correlations were observed between the representational geometries of task-optimal LLM layers and human frontal FRPs. These results consistently diverged from comparisons with other EEG measures (response-locked ERPs and resting EEG), suggesting a potential shared representational space for abstract patterns. This indicates that LLMs might mirror human brain mechanisms in abstract reasoning, offering preliminary evidence of shared principles between biological and artificial intelligence.

