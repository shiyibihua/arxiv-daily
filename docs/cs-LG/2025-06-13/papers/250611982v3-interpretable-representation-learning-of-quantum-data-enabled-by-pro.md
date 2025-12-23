---
layout: default
title: Interpretable representation learning of quantum data enabled by probabilistic variational autoencoders
---

# Interpretable representation learning of quantum data enabled by probabilistic variational autoencoders

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11982" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11982v3</a>
  <a href="https://arxiv.org/pdf/2506.11982.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11982v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11982v3', 'Interpretable representation learning of quantum data enabled by probabilistic variational autoencoders')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Paulin de Schoulepnikoff, Gorka Muñoz-Gil, Hendrik Poulsen Nautrup, Hans J. Briegel

**分类**: quant-ph, cond-mat.stat-mech, cs.LG

**发布日期**: 2025-06-13 (更新: 2025-12-17)

**备注**: Main text 10 pages, total document 16 pages, 10 figures

**期刊**: Phys. Rev. A 112, 062423 (2025)

**DOI**: [10.1103/cwb8-y25k](https://doi.org/10.1103/cwb8-y25k)

---

## 💡 一句话要点

**提出基于变分自编码器的量子数据可解释表示学习方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `量子数据` `变分自编码器` `可解释机器学习` `物理特征提取` `无监督学习` `量子态重建` `概率损失函数`

## 📋 核心要点

1. 现有变分自编码器在处理量子数据时，常常忽视其概率特性，导致无法提取有意义的物理描述。
2. 论文提出通过引入一个能够忠实重现量子态的解码器和量身定制的概率损失函数，来改善VAEs的表现。
3. 在基准量子自旋模型和Rydberg原子阵列的实验数据中，提出的方法能够有效揭示相结构，且无需先验知识。

## 📝 摘要（中文）

可解释机器学习正迅速成为科学发现的重要工具。在现有方法中，变分自编码器（VAEs）在提取输入数据的隐藏物理特征方面展现出潜力。然而，VAEs的有效性依赖于其对输入概率分布的准确近似。在处理量子数据时，VAEs必须考虑其内在的随机性和复杂相关性。本文提出两项关键修改，使VAEs能够学习具有物理意义的潜在表示：一个能够忠实重现量子态的解码器和一个针对该任务量身定制的概率损失函数。通过基准量子自旋模型，我们识别出标准方法失效的区域，而我们的方法学习到的表示仍然具有意义和可解释性。该模型在无先验标签、哈密顿细节或相关序参量知识的情况下，能够自主揭示Rydberg原子阵列的相结构，突显其作为无监督和可解释工具在量子系统研究中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决变分自编码器在处理量子数据时未能充分考虑其内在随机性和复杂相关性的问题，导致无法提取有意义的物理特征。

**核心思路**：通过设计一个能够忠实重现量子态的解码器和一个针对量子数据的概率损失函数，提升VAEs对量子数据的表示学习能力，从而获得可解释的物理潜在表示。

**技术框架**：整体架构包括输入量子数据、通过改进的编码器进行潜在表示学习、利用新解码器重建量子态，并通过定制的损失函数优化模型。

**关键创新**：最重要的创新在于引入了一个专门为量子态重建设计的解码器和一个适应量子数据特性的概率损失函数，这与传统VAEs的处理方式有本质区别。

**关键设计**：在网络结构上，解码器采用了适合量子态的特定结构，损失函数则基于量子概率分布进行设计，以确保模型能够有效捕捉量子数据的特性。

## 📊 实验亮点

实验结果表明，提出的方法在基准量子自旋模型中表现优于标准方法，能够在标准方法失效的区域内仍然提取出有意义的物理描述。在Rydberg原子阵列的实验数据中，模型成功揭示了相结构，且无需任何先验标签或系统知识，显示出显著的提升。

## 🎯 应用场景

该研究具有广泛的潜在应用，尤其是在量子计算和量子信息科学领域。通过无监督学习量子系统的相结构，研究人员可以更深入地理解量子现象，并推动量子技术的发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Interpretable machine learning is rapidly becoming a crucial tool for scientific discovery. Among existing approaches, variational autoencoders (VAEs) have shown promise in extracting the hidden physical features of some input data, with no supervision nor prior knowledge of the system at study. Yet, the ability of VAEs to create meaningful, interpretable representations relies on their accurate approximation of the underlying probability distribution of their input. When dealing with quantum data, VAEs must hence account for its intrinsic randomness and complex correlations. While VAEs have been previously applied to quantum data, they have often neglected its probabilistic nature, hindering the extraction of meaningful physical descriptors. Here, we demonstrate that two key modifications enable VAEs to learn physically meaningful latent representations: a decoder capable of faithfully reproduce quantum states and a probabilistic loss tailored to this task. Using benchmark quantum spin models, we identify regimes where standard methods fail while the representations learned by our approach remain meaningful and interpretable. Applied to experimental data from Rydberg atom arrays, the model autonomously uncovers the phase structure without access to prior labels, Hamiltonian details, or knowledge of relevant order parameters, highlighting its potential as an unsupervised and interpretable tool for the study of quantum systems.

