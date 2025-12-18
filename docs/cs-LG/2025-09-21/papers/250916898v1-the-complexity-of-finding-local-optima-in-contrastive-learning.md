---
layout: default
title: The Complexity of Finding Local Optima in Contrastive Learning
---

# The Complexity of Finding Local Optima in Contrastive Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16898" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16898v1</a>
  <a href="https://arxiv.org/pdf/2509.16898.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16898v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16898v1', 'The Complexity of Finding Local Optima in Contrastive Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingming Yan, Yiyuan Luo, Vaggos Chatziafratis, Ioannis Panageas, Parnian Shahkar, Stelios Stavroulakis

**分类**: cs.LG, cs.CC, math.OC

**发布日期**: 2025-09-21

**备注**: To appear as a conference paper in NeurIPS 2025

---

## 💡 一句话要点

**证明对比学习中局部最优解的复杂性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `对比学习` `局部最优解` `复杂性理论` `优化算法` `计算机视觉`

## 📋 核心要点

1. 现有对比学习方法在寻找局部最优解时面临复杂性挑战，尤其是在离散和连续设置中。
2. 论文通过证明局部最优解的$	extsf{PLS}$-困难性和$	extsf{CLS}$-困难性，明确了这一问题的复杂性。
3. 研究结果表明，除非特定复杂性类关系成立，否则无法在多项式时间内找到局部最优解。

## 📝 摘要（中文）

对比学习是一种通过优化基于对比信息的目标来发现有意义数据表示的强大技术。本文解决了在各种对比学习问题中寻找局部最优解的复杂性，证明了在离散设置下的$	extsf{PLS}$-困难性和在连续设置下的$	extsf{CLS}$-困难性。这意味着，除非$	extsf{PLS}	ext{或}	extsf{CLS}$属于多项式时间类，否则不存在多项式时间算法能够找到局部最优解。即使在$	extsf{PLS}	ext{或}	extsf{CLS}$属于多项式时间类的情况下，局部搜索算法在某些实例中仍需指数时间才能达到局部最优解。

## 🔬 方法详解

**问题定义**：本文聚焦于对比学习中局部最优解的寻找复杂性，现有方法在此方面的复杂性尚未明确，尤其是在离散和连续优化问题中。

**核心思路**：通过构建特定的优化问题，论文证明了在对比学习中寻找局部最优解的$	extsf{PLS}$和$	extsf{CLS}$-困难性，从而揭示了局部搜索算法的局限性。

**技术框架**：研究首先定义了对比学习中的局部最优解问题，然后通过构造实例和复杂性归约，展示了在不同设置下的困难性。

**关键创新**：论文的主要创新在于明确了对比学习中局部最优解的复杂性，提供了理论基础，表明在多项式时间内无法找到局部最优解的条件。

**关键设计**：在研究中，作者使用了加权三元组的形式来定义对比学习目标，并通过构造特定的实例来证明复杂性，涉及的损失函数包括Triplet Loss等。

## 📊 实验亮点

研究结果表明，寻找局部最优解的复杂性在离散和连续设置中均为$	extsf{PLS}$-困难和$	extsf{CLS}$-困难，意味着在多项式时间内无法找到局部最优解。即使在复杂性类关系成立的情况下，某些实例仍需指数时间才能达到局部最优解。

## 🎯 应用场景

该研究为对比学习的理论基础提供了重要贡献，特别是在优化算法设计和复杂性分析方面。未来，理解局部最优解的复杂性将有助于开发更有效的学习算法，推动计算机视觉和自然语言处理等领域的应用。

## 📄 摘要（原文）

> Contrastive learning is a powerful technique for discovering meaningful data representations by optimizing objectives based on $\textit{contrastive information}$, often given as a set of weighted triplets $\{(x_i, y_i^+, z_{i}^-)\}_{i = 1}^m$ indicating that an "anchor" $x_i$ is more similar to a "positive" example $y_i$ than to a "negative" example $z_i$. The goal is to find representations (e.g., embeddings in $\mathbb{R}^d$ or a tree metric) where anchors are placed closer to positive than to negative examples. While finding $\textit{global}$ optima of contrastive objectives is $\mathsf{NP}$-hard, the complexity of finding $\textit{local}$ optima -- representations that do not improve by local search algorithms such as gradient-based methods -- remains open. Our work settles the complexity of finding local optima in various contrastive learning problems by proving $\mathsf{PLS}$-hardness in discrete settings (e.g., maximize satisfied triplets) and $\mathsf{CLS}$-hardness in continuous settings (e.g., minimize Triplet Loss), where $\mathsf{PLS}$ (Polynomial Local Search) and $\mathsf{CLS}$ (Continuous Local Search) are well-studied complexity classes capturing local search dynamics in discrete and continuous optimization, respectively. Our results imply that no polynomial time algorithm (local search or otherwise) can find a local optimum for various contrastive learning problems, unless $\mathsf{PLS}\subseteq\mathsf{P}$ (or $\mathsf{CLS}\subseteq \mathsf{P}$ for continuous problems). Even in the unlikely scenario that $\mathsf{PLS}\subseteq\mathsf{P}$ (or $\mathsf{CLS}\subseteq \mathsf{P}$), our reductions imply that there exist instances where local search algorithms need exponential time to reach a local optimum, even for $d=1$ (embeddings on a line).

