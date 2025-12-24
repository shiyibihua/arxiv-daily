---
layout: default
title: Token Homogenization under Positional Bias
---

# Token Homogenization under Positional Bias

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17126" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17126v1</a>
  <a href="https://arxiv.org/pdf/2508.17126.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17126v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17126v1', 'Token Homogenization under Positional Bias')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Viacheslav Yusupov, Danil Maksimov, Ameliia Alaeva, Tatiana Zaitceva, Antipina Anna, Anna Vasileva, Chenlin Liu, Rayuth Chheng, Danil Sazanakov, Andrey Chetvergov, Alina Ermilova, Egor Shvetsov

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-23

---

## 💡 一句话要点

**研究标记均质化与位置偏差的关系**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `标记均质化` `位置偏差` `变换器模型` `语言模型` `深度学习`

## 📋 核心要点

1. 当前大型语言模型在处理过程中，标记表示趋向均质化，导致信息丢失和独特性降低。
2. 本文通过实证分析和控制实验，探讨了位置偏差如何影响标记均质化现象，提出了新的分析框架。
3. 实验结果表明，标记在处理过程中确实会失去独特性，尤其是在偏向极端位置时，验证了均质化的存在。

## 📝 摘要（中文）

本文研究了标记均质化现象，即在变换器层中标记表示向均匀性收敛的过程，以及其与大型语言模型中的位置偏差之间的关系。通过实证分析，我们考察了均质化是否发生以及位置偏差如何放大这一效应。通过逐层相似性分析和控制实验，我们证明了标记在处理过程中系统性地失去独特性，特别是在偏向极端位置时。我们的研究结果确认了均质化的存在及其对位置注意机制的依赖性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中标记均质化的问题，现有方法未能充分揭示位置偏差对标记独特性的影响。

**核心思路**：通过逐层相似性分析，论文探讨了位置偏差如何加剧标记均质化现象，提出了一种新的实验设计来验证这一假设。

**技术框架**：研究采用了分层分析的方法，首先进行标记表示的相似性计算，然后通过控制实验观察位置偏差对均质化的影响。

**关键创新**：论文的创新在于系统性地揭示了位置偏差与标记均质化之间的关系，填补了现有研究的空白。

**关键设计**：实验中采用了多层次的相似性度量，设计了特定的控制实验以确保结果的可靠性，关注极端位置的影响。

## 📊 实验亮点

实验结果显示，在偏向极端位置时，标记的独特性显著降低，均质化现象在多层次分析中得到了验证。通过控制实验，发现位置偏差能够显著放大均质化效应，提供了新的实证证据。

## 🎯 应用场景

该研究为理解大型语言模型的内部机制提供了新的视角，尤其是在处理长文本时的标记表示均质化问题。未来可能在自然语言处理、文本生成和对话系统等领域具有重要应用价值，帮助优化模型性能和提升生成文本的多样性。

## 📄 摘要（原文）

> This paper investigates token homogenization - the convergence of token representations toward uniformity across transformer layers and its relationship to positional bias in large language models. We empirically examine whether homogenization occurs and how positional bias amplifies this effect. Through layer-wise similarity analysis and controlled experiments, we demonstrate that tokens systematically lose distinctiveness during processing, particularly when biased toward extremal positions. Our findings confirm both the existence of homogenization and its dependence on positional attention mechanisms.

