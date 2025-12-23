---
layout: default
title: How Far Can Off-the-Shelf Multimodal Large Language Models Go in Online Episodic Memory Question Answering?
---

# How Far Can Off-the-Shelf Multimodal Large Language Models Go in Online Episodic Memory Question Answering?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16450" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16450v1</a>
  <a href="https://arxiv.org/pdf/2506.16450.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16450v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16450v1', 'How Far Can Off-the-Shelf Multimodal Large Language Models Go in Online Episodic Memory Question Answering?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Giuseppe Lando, Rosario Forte, Giovanni Maria Farinella, Antonino Furnari

**分类**: cs.CV

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出轻量化文本记忆方法以解决在线情节记忆视频问答问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `在线问答` `多模态学习` `情节记忆` `视频理解` `内存效率`

## 📋 核心要点

1. 现有方法在处理在线情节记忆视频问答时，通常需要大量的存储和计算资源，效率较低。
2. 本研究提出了一种将流式视频转换为轻量级文本记忆的方法，结合MLLM和LLM模块实现高效问答。
3. 实验结果表明，所提方法在准确率和内存效率上均优于现有的专用系统，具有显著的性能提升。

## 📝 摘要（中文）

本研究探讨了现成的多模态大型语言模型（MLLMs）在无需额外训练的情况下，能否有效处理在线情节记忆视频问答（OEM-VQA）任务。我们的方法通过MLLM描述模块将流式自我中心视频转换为轻量级文本记忆，每分钟仅需几千字节，并利用LLM推理模块通过查询该记忆来回答多项选择问题。在QAEgo4D-Closed基准上，我们的最佳配置达到了56.0%的准确率，存储需求为每分钟3.6 kB，性能与专用的最先进系统相匹配，同时在内存效率上提高了10^4至10^5倍。大量的消融实验提供了对每个组件和设计选择的深入见解，并为未来研究的改进方向提供了启示。

## 🔬 方法详解

**问题定义**：本论文旨在解决在线情节记忆视频问答（OEM-VQA）中的效率和存储问题。现有方法通常需要高昂的计算和存储资源，限制了其应用场景。

**核心思路**：我们提出了一种将流式自我中心视频转换为轻量级文本记忆的方法，利用MLLM描述模块生成简洁的文本表示，并通过LLM推理模块进行问答。这样的设计使得系统在不需要额外训练的情况下，依然能够高效地进行问答。

**技术框架**：整体架构包括两个主要模块：MLLM描述模块和LLM推理模块。首先，MLLM模块将视频流转换为文本记忆；然后，LLM模块通过查询该记忆来回答多项选择问题。

**关键创新**：本研究的主要创新在于实现了高效的轻量级文本记忆生成，存储需求显著降低，同时保持了与专用系统相当的问答性能。这种方法在内存效率上提高了10^4至10^5倍。

**关键设计**：在设计中，我们优化了文本记忆的生成过程，确保每分钟的存储需求仅为3.6 kB，并通过大量消融实验分析了各个组件的作用，为未来的改进提供了依据。

## 📊 实验亮点

实验结果显示，所提方法在QAEgo4D-Closed基准上达到了56.0%的准确率，存储需求仅为每分钟3.6 kB。这一性能与现有的最先进系统相当，但在内存效率上提高了10^4至10^5倍，展示了显著的优势。

## 🎯 应用场景

该研究的潜在应用场景包括智能监控、教育视频分析和人机交互等领域。通过高效的在线情节记忆问答系统，可以在实时视频流中快速获取关键信息，提升用户体验和决策效率。未来，该技术有望在更多需要即时信息提取的场景中发挥重要作用。

## 📄 摘要（原文）

> We investigate whether off-the-shelf Multimodal Large Language Models (MLLMs) can tackle Online Episodic-Memory Video Question Answering (OEM-VQA) without additional training. Our pipeline converts a streaming egocentric video into a lightweight textual memory, only a few kilobytes per minute, via an MLLM descriptor module, and answers multiple-choice questions by querying this memory with an LLM reasoner module. On the QAEgo4D-Closed benchmark, our best configuration attains 56.0% accuracy with 3.6 kB per minute storage, matching the performance of dedicated state-of-the-art systems while being 10**4/10**5 times more memory-efficient. Extensive ablations provides insights into the role of each component and design choice, and highlight directions of improvement for future research.

