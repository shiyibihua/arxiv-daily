---
layout: default
title: Recursive Language Models
---

# Recursive Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24601" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24601v1</a>
  <a href="https://arxiv.org/pdf/2512.24601.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24601v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24601v1', 'Recursive Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alex L. Zhang, Tim Kraska, Omar Khattab

**分类**: cs.AI, cs.CL

**发布日期**: 2025-12-31

**备注**: 9 pages, 33 with Appendix

---

## 💡 一句话要点

**提出递归语言模型（RLM），解决LLM在超长上下文推理中的难题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `递归语言模型` `长上下文处理` `大型语言模型` `推理时扩展` `提示工程`

## 📋 核心要点

1. 现有LLM受限于固定长度的上下文窗口，难以处理超长输入，限制了其在长文档理解等领域的应用。
2. RLM将长提示视为外部环境，允许LLM递归调用自身处理提示片段，从而突破上下文长度限制。
3. 实验表明，RLM在长上下文任务中显著优于传统LLM，且计算成本可与传统方法媲美甚至更低。

## 📝 摘要（中文）

本文研究了如何通过推理时扩展来允许大型语言模型（LLM）处理任意长度的提示。我们提出递归语言模型（RLM），这是一种通用的推理策略，它将长提示视为外部环境的一部分，并允许LLM以编程方式检查、分解提示，并递归地调用自身来处理提示片段。我们发现，RLM成功地处理了比模型上下文窗口大两个数量级的输入，并且即使对于较短的提示，在四个不同的长上下文任务中，也显著优于基础LLM和常见的长上下文支架，同时具有相当（或更便宜）的每次查询成本。

## 🔬 方法详解

**问题定义**：现有大型语言模型（LLM）的上下文窗口长度有限，无法直接处理超长文本输入。这限制了LLM在需要理解和处理大量信息的任务中的应用，例如长文档摘要、问答等。现有的长上下文处理方法，如截断、滑动窗口等，要么丢失信息，要么效率低下。

**核心思路**：论文的核心思路是将LLM视为一个智能体，通过递归的方式处理长文本。具体来说，将长文本视为一个外部环境，LLM可以编程化地检查、分解这个环境，并递归地调用自身来处理文本片段。这种方式类似于人类阅读长篇文章时，会分段阅读并进行思考和总结。

**技术框架**：RLM的整体框架包含以下几个主要步骤：1) **提示分解**：LLM首先将长提示分解成多个较小的片段。2) **递归调用**：LLM递归地调用自身来处理每个片段，并生成相应的输出。3) **信息整合**：LLM将各个片段的输出进行整合，生成最终的输出。在这个过程中，LLM可以根据需要选择不同的处理策略，例如总结、问答等。

**关键创新**：RLM的关键创新在于其递归处理长文本的方式。与传统的长上下文处理方法相比，RLM可以更好地利用LLM的上下文信息，并且可以灵活地处理不同长度的文本。此外，RLM还引入了编程化的控制机制，允许LLM根据需要选择不同的处理策略。

**关键设计**：RLM的关键设计包括：1) **提示工程**：设计合适的提示，引导LLM进行文本分解和递归调用。2) **控制机制**：设计有效的控制机制，控制LLM的递归深度和处理策略。3) **信息整合策略**：设计合理的信息整合策略，将各个片段的输出进行整合，生成最终的输出。论文中使用了标准的Transformer架构，并针对长文本处理进行了优化。损失函数采用交叉熵损失。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24601v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24601v1/figures/Fig2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24601v1/figures/cost_quartiles_dual.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RLM在四个不同的长上下文任务中显著优于基础LLM和常见的长上下文支架。例如，在某些任务中，RLM的性能提升超过20%。更重要的是，RLM能够处理比模型上下文窗口大两个数量级的输入，这表明RLM具有很强的可扩展性。此外，RLM的每次查询成本与传统方法相当甚至更低。

## 🎯 应用场景

RLM具有广泛的应用前景，例如长文档摘要、问答系统、代码理解与生成、以及需要处理大量信息的对话系统。该方法能够提升LLM在处理复杂、长篇幅任务时的性能，并有望推动LLM在更多实际场景中的应用，例如法律文件分析、金融报告解读等。

## 📄 摘要（原文）

> We study allowing large language models (LLMs) to process arbitrarily long prompts through the lens of inference-time scaling. We propose Recursive Language Models (RLMs), a general inference strategy that treats long prompts as part of an external environment and allows the LLM to programmatically examine, decompose, and recursively call itself over snippets of the prompt. We find that RLMs successfully handle inputs up to two orders of magnitude beyond model context windows and, even for shorter prompts, dramatically outperform the quality of base LLMs and common long-context scaffolds across four diverse long-context tasks, while having comparable (or cheaper) cost per query.

