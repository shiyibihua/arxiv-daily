---
layout: default
title: Multimodal Chain of Continuous Thought for Latent-Space Reasoning in Vision-Language Models
---

# Multimodal Chain of Continuous Thought for Latent-Space Reasoning in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12587" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12587v2</a>
  <a href="https://arxiv.org/pdf/2508.12587.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12587v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12587v2', 'Multimodal Chain of Continuous Thought for Latent-Space Reasoning in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tan-Hanh Pham, Chris Ngo

**分类**: cs.CV

**发布日期**: 2025-08-18 (更新: 2025-09-23)

**🔗 代码/项目**: [GITHUB](https://github.com/Hanhpt23/OmniMod)

---

## 💡 一句话要点

**提出多模态连续思维链以解决多模态推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `连续思维链` `潜在空间` `跨模态对齐` `反思认知` `语言模型` `深度学习`

## 📋 核心要点

1. 现有的多模态推理方法主要依赖于语言模型，难以有效整合视觉、文本和音频信息，导致推理效果不佳。
2. 本文提出的MCOUT方法通过在联合潜在空间中进行推理，使用连续隐藏向量表示推理状态，克服了传统方法的局限性。
3. 实验结果显示，MCOUT在多个基准上相较于强基线提高了最高8.23%的准确率，并在多项选择和开放式任务中BLEU分数提升了8.27%。

## 📝 摘要（中文）

许多大型多模态模型的推理技术采用语言模型方法，如链式思维提示，这些方法在文本上有效，但在多模态上下文中表现不佳，难以动态对齐音频、视觉和文本信息。为此，本文提出了多模态连续思维链（MCOUT），该方法直接在联合潜在空间中进行推理，而非自然语言。MCOUT通过将推理状态表示为连续的隐藏向量，迭代地与视觉和文本嵌入对齐，灵感来源于人类的反思认知。实验结果表明，MCOUT在多个基准测试中显著提高了多模态推理的准确性，展现出其作为人类反思式多模态推理的可扩展框架的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态推理方法在动态对齐音频、视觉和文本信息时的不足，尤其是链式思维提示在多模态上下文中的局限性。

**核心思路**：MCOUT方法的核心在于直接在联合潜在空间中进行推理，使用连续的隐藏向量来表示推理状态，灵感来源于人类的反思认知过程。

**技术框架**：MCOUT包括两个主要变体：MCOUT-Base和MCOUT-Multi。MCOUT-Base重用语言模型的最后隐藏状态作为连续思维进行迭代推理，而MCOUT-Multi则集成了多模态潜在注意力，以增强视觉和文本特征之间的跨模态对齐。

**关键创新**：MCOUT的主要创新在于其在潜在空间中进行连续推理的能力，区别于传统的基于语言的推理方法，提供了一种更自然的推理方式。

**关键设计**：在MCOUT中，采用了连续隐藏向量的迭代更新机制，结合视觉和文本嵌入进行对齐，设计了适应多模态特征的损失函数和网络结构，以优化推理效果。

## 📊 实验亮点

实验结果表明，MCOUT在MMM、ScienceQA和MMStar等基准测试中，准确率提高了最高8.23%，在多项选择和开放式任务中的BLEU分数提升了8.27%，显示出其在多模态推理中的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化内容生成和多模态数据分析等。通过提升多模态推理能力，MCOUT能够在更复杂的场景中实现更自然的人机交互，推动人工智能在实际应用中的发展。

## 📄 摘要（原文）

> Many reasoning techniques for large multimodal models adapt language model approaches, such as Chain-of-Thought (CoT) prompting, which express reasoning as word sequences. While effective for text, these methods are suboptimal for multimodal contexts, struggling to align audio, visual, and textual information dynamically. To explore an alternative paradigm, we propose the Multimodal Chain of Continuous Thought (MCOUT), which enables reasoning directly in a joint latent space rather than in natural language. In MCOUT, the reasoning state is represented as a continuous hidden vector, iteratively refined and aligned with visual and textual embeddings, inspired by human reflective cognition. We develop two variants: MCOUT-Base, which reuses the language model`s last hidden state as the continuous thought for iterative reasoning, and MCOUT-Multi, which integrates multimodal latent attention to strengthen cross-modal alignment between visual and textual features. Experiments on benchmarks including MMMU, ScienceQA, and MMStar show that MCOUT consistently improves multimodal reasoning, yielding up to 8.23% accuracy gains over strong baselines and improving BLEU scores up to 8.27% across multiple-choice and open-ended tasks. These findings highlight latent continuous reasoning as a promising direction for advancing LMMs beyond language-bound CoT, offering a scalable framework for human-like reflective multimodal inference. Code is available at https://github.com/Hanhpt23/OmniMod.

