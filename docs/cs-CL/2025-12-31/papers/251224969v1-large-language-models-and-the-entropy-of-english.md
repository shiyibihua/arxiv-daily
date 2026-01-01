---
layout: default
title: Large language models and the entropy of English
---

# Large language models and the entropy of English

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24969" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24969v1</a>
  <a href="https://arxiv.org/pdf/2512.24969.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24969v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24969v1', 'Large language models and the entropy of English')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Colin Scheibner, Lindsay M. Smith, William Bialek

**分类**: cond-mat.stat-mech, cs.CL, physics.bio-ph, q-bio.NC

**发布日期**: 2025-12-31

**备注**: 8 pages, 6 figures

---

## 💡 一句话要点

**利用大语言模型揭示英语文本的长程结构**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `条件熵` `长程依赖` `文本分析` `机器学习`

## 📋 核心要点

1. 现有方法在处理长文本时，难以捕捉字符之间的长程依赖关系，导致信息损失。
2. 本研究通过大语言模型分析文本的条件熵，揭示长程结构的存在及其学习过程。
3. 实验结果表明，随着上下文长度的增加，编码长度持续减少，显示出字符间的显著相关性。

## 📝 摘要（中文）

本研究利用大语言模型（LLMs）揭示来自多种来源的英语文本中的长程结构。条件熵或编码长度在许多情况下随着上下文长度的增加而持续减少，至少达到$N	ext{∼}10^4$个字符，这表明在这些距离上存在直接的依赖关系或交互。我们从数据中独立于模型展示了字符之间的小但显著的相关性。编码长度的分布揭示了对大量字符的逐渐增强的确定性。模型训练过程中，我们观察到长短上下文长度的动态差异，表明长程结构的学习是逐步进行的。我们的结果为构建LLMs或语言本身的统计物理模型提供了约束。

## 🔬 方法详解

**问题定义**：本研究旨在揭示英语文本中的长程结构，现有方法在处理长文本时难以捕捉字符之间的长程依赖关系，导致信息损失。

**核心思路**：通过利用大语言模型分析文本的条件熵，研究字符间的依赖关系，展示长程结构的存在及其学习过程。

**技术框架**：整体架构包括数据收集、模型训练和条件熵计算三个主要阶段。首先收集多种来源的英语文本数据，然后训练大语言模型，最后计算不同上下文长度下的条件熵。

**关键创新**：本研究的主要创新在于通过条件熵的分析揭示了长程依赖关系的存在，且展示了长程结构的学习是一个渐进的过程，这与现有方法的短期依赖假设形成对比。

**关键设计**：在模型训练中，采用了适当的上下文窗口大小，并通过调整学习率和损失函数优化模型性能，以确保能够有效捕捉长程依赖。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24969v1/figures/C4_models.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24969v1/figures/GernreFigureV3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24969v1/figures/histogramsV3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，随着上下文长度的增加，条件熵持续降低，表明长程依赖关系的存在。具体而言，在$N	ext{∼}10^4$字符的情况下，编码长度显著减少，展示了字符间的小但显著的相关性。这一发现为理解语言模型的学习过程提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、文本生成和机器翻译等。通过揭示长程结构的学习过程，可以为改进现有语言模型提供理论依据，进而提升模型在复杂文本处理中的表现。未来，研究结果可能推动更高效的语言模型设计和应用。

## 📄 摘要（原文）

> We use large language models (LLMs) to uncover long-ranged structure in English texts from a variety of sources. The conditional entropy or code length in many cases continues to decrease with context length at least to $N\sim 10^4$ characters, implying that there are direct dependencies or interactions across these distances. A corollary is that there are small but significant correlations between characters at these separations, as we show from the data independent of models. The distribution of code lengths reveals an emergent certainty about an increasing fraction of characters at large $N$. Over the course of model training, we observe different dynamics at long and short context lengths, suggesting that long-ranged structure is learned only gradually. Our results constrain efforts to build statistical physics models of LLMs or language itself.

