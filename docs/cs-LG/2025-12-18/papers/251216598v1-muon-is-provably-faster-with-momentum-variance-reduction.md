---
layout: default
title: Muon is Provably Faster with Momentum Variance Reduction
---

# Muon is Provably Faster with Momentum Variance Reduction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16598" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16598v1</a>
  <a href="https://arxiv.org/pdf/2512.16598.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16598v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16598v1', 'Muon is Provably Faster with Momentum Variance Reduction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xun Qian, Hussein Rammal, Dmitry Kovalev, Peter Richtárik

**分类**: math.OC, cs.LG

**发布日期**: 2025-12-18

**备注**: 31 pages, 4 figures

---

## 💡 一句话要点

**通过动量方差减少提升Muon优化器性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度学习` `优化器` `动量方差减少` `Gluon框架` `收敛速率` `非欧几里得优化` `大型语言模型`

## 📋 核心要点

1. 现有的深度学习优化器在训练大型语言模型时存在收敛速度慢的问题，尤其是Adam类方法的表现不尽如人意。
2. 本研究提出将动量方差减少（MVR）技术整合到Gluon框架中，以提升Muon和Scion等优化器的收敛速率。
3. 实验结果表明，所提方法的收敛速率从${	ext{O}}(rac{1}{K^{1/4}})$提升至${	ext{O}}(rac{1}{K^{1/3}})$，并在多项实验中验证了其优越性。

## 📝 摘要（中文）

近期的实证研究表明，基于线性最小化oracle（LMO）并在特定非欧几里得范数球上优化的深度学习优化器，如Muon和Scion，在训练大型语言模型时优于Adam类方法。本研究展示了通过将传统动量替换为动量方差减少（MVR），可以对这些优化器进行可证明的改进。我们将MVR整合到最近提出的Gluon框架中，该框架能够捕捉Muon、Scion及其他特定的非欧几里得LMO方法，并在更一般的平滑性假设下工作，从而更好地捕捉神经网络的层次结构。在非凸情况下，我们以三种不同方式将MVR融入Gluon，所有方法均将收敛速率从${	ext{O}}(rac{1}{K^{1/4}})$提高至${	ext{O}}(rac{1}{K^{1/3}})$，并在星凸情况下提供了改进的速率。最后，我们进行了多项数值实验，验证了所提算法在迭代复杂度上的优越性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有深度学习优化器在训练大型语言模型时收敛速度慢的问题，尤其是Adam类方法在非凸优化中的不足。

**核心思路**：通过将动量方差减少（MVR）技术引入到Gluon框架中，提升优化器的收敛速率，进而提高训练效率。

**技术框架**：整体框架为Gluon，能够统一处理Muon、Scion及其他非欧几里得LMO方法，采用更一般的平滑性假设，分为三个阶段：MVR的引入、收敛速率分析及实验验证。

**关键创新**：最重要的创新在于将MVR与Gluon框架结合，提供了对多种优化器的统一分析和改进，显著提升了收敛速率。

**关键设计**：在设计中，采用了三种不同的方式将MVR融入Gluon，并在星凸情况下提供了改进的收敛速率，具体参数设置和损失函数设计未详细披露，属于未知领域。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16598v1/fig/MVR1gbs512.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16598v1/fig/MVR1gbs128.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16598v1/fig/MVR2gbs512.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，所提算法的收敛速率从${	ext{O}}(rac{1}{K^{1/4}})$提升至${	ext{O}}(rac{1}{K^{1/3}})$，在多项数值实验中验证了其在迭代复杂度上的优越性，相较于基线方法表现出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、计算机视觉等需要高效训练的大型深度学习模型。通过提升优化器的性能，可以显著缩短模型训练时间，提高模型的实际应用价值。未来，随着深度学习模型规模的不断扩大，优化器的改进将对整个领域产生深远影响。

## 📄 摘要（原文）

> Recent empirical research has demonstrated that deep learning optimizers based on the linear minimization oracle (LMO) over specifically chosen Non-Euclidean norm balls, such as Muon and Scion, outperform Adam-type methods in the training of large language models. In this work, we show that such optimizers can be provably improved by replacing their vanilla momentum by momentum variance reduction (MVR). Instead of proposing and analyzing MVR variants of Muon and Scion separately, we incorporate MVR into the recently proposed Gluon framework, which captures Muon, Scion and other specific Non-Euclidean LMO-based methods as special cases, and at the same time works with a more general smoothness assumption which better captures the layer-wise structure of neural networks. In the non-convex case, we incorporate MVR into Gluon in three different ways. All of them improve the convergence rate from ${\cal O} (\frac{1}{K^{1/4}})$ to ${\cal O} (\frac{1}{K^{1/3}})$. Additionally, we provide improved rates in the star-convex case. Finally, we conduct several numerical experiments that verify the superior performance of our proposed algorithms in terms of iteration complexity.

