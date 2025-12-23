---
layout: default
title: When and How Unlabeled Data Provably Improve In-Context Learning
---

# When and How Unlabeled Data Provably Improve In-Context Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15329" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15329v1</a>
  <a href="https://arxiv.org/pdf/2506.15329.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15329v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15329v1', 'When and How Unlabeled Data Provably Improve In-Context Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingcong Li, Xiangyu Chang, Muti Kara, Xiaofeng Liu, Amit Roy-Chowdhury, Samet Oymak

**分类**: cs.LG, cs.AI, cs.CL, math.OC

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出利用未标记数据提升上下文学习能力的方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文学习` `未标记数据` `半监督学习` `多层变换器` `循环结构` `高斯混合模型`

## 📋 核心要点

1. 现有的单层线性注意力模型无法有效利用未标记数据，导致学习性能受限。
2. 论文提出通过多层或循环变换器，利用未标记数据构建特定形式的估计器，从而提升学习效果。
3. 实验结果表明，所提方法在真实数据集上显著提升了半监督学习的性能，相较于标准单次推理有明显改善。

## 📝 摘要（中文）

近期研究表明，即使演示数据存在缺失或错误标签，上下文学习（ICL）依然有效。本文探讨了在二元高斯混合模型下，部分演示缺失标签的情况。我们通过理论分析表明：一层线性注意力模型无法利用未标记数据，而多层或循环变换器能够有效利用未标记数据，构建特定形式的估计器。我们还将此与常用的半监督学习算法期望最大化建立了联系。最后，我们提出了循环使用现成表格基础模型的方法，以增强其半监督能力，并在真实数据集上进行了广泛评估，结果显示该方法显著提升了半监督学习性能。

## 🔬 方法详解

**问题定义**：本文旨在解决在上下文学习中，如何有效利用未标记数据的问题。现有方法如单层线性注意力模型在面对缺失标签时表现不佳，无法充分利用可用信息。

**核心思路**：论文的核心思路是通过多层或循环变换器，构建能够隐式利用未标记数据的估计器，从而提升模型的学习能力。这样的设计使得模型能够在缺失标签的情况下，仍然进行有效的学习。

**技术框架**：整体架构包括多层或循环变换器，模型通过对输入特征和部分观察标签的处理，构建出特定形式的多项式估计器。主要模块包括特征提取、标签处理和估计器构建。

**关键创新**：最重要的创新在于提出了利用深度和循环结构来构建多项式形式的估计器，这与传统方法的线性估计方式有本质区别，能够更好地利用未标记数据。

**关键设计**：在模型设计中，采用了特定的损失函数和网络结构，确保模型在处理缺失标签时，能够有效地进行学习和推理。

## 📊 实验亮点

实验结果显示，所提方法在多个真实数据集上，相较于标准单次推理，半监督学习性能提升显著，具体提升幅度达到XX%（具体数据需根据实验结果填写），验证了理论分析的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、计算机视觉和其他需要处理不完整数据的机器学习任务。通过提升模型对未标记数据的利用能力，能够在数据稀缺的情况下，依然实现较好的学习效果，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Recent research shows that in-context learning (ICL) can be effective even when demonstrations have missing or incorrect labels. To shed light on this capability, we examine a canonical setting where the demonstrations are drawn according to a binary Gaussian mixture model (GMM) and a certain fraction of the demonstrations have missing labels. We provide a comprehensive theoretical study to show that: (1) The loss landscape of one-layer linear attention models recover the optimal fully-supervised estimator but completely fail to exploit unlabeled data; (2) In contrast, multilayer or looped transformers can effectively leverage unlabeled data by implicitly constructing estimators of the form $\sum_{i\ge 0} a_i (X^\top X)^iX^\top y$ with $X$ and $y$ denoting features and partially-observed labels (with missing entries set to zero). We characterize the class of polynomials that can be expressed as a function of depth and draw connections to Expectation Maximization, an iterative pseudo-labeling algorithm commonly used in semi-supervised learning. Importantly, the leading polynomial power is exponential in depth, so mild amount of depth/looping suffices. As an application of theory, we propose looping off-the-shelf tabular foundation models to enhance their semi-supervision capabilities. Extensive evaluations on real-world datasets show that our method significantly improves the semisupervised tabular learning performance over the standard single pass inference.

