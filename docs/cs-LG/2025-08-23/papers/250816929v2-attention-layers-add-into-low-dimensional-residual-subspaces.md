---
layout: default
title: Attention Layers Add Into Low-Dimensional Residual Subspaces
---

# Attention Layers Add Into Low-Dimensional Residual Subspaces

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16929" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16929v2</a>
  <a href="https://arxiv.org/pdf/2508.16929.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16929v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16929v2', 'Attention Layers Add Into Low-Dimensional Residual Subspaces')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junxuan Wang, Xuyang Ge, Wentao Shu, Zhengfu He, Xipeng Qiu

**分类**: cs.LG, cs.CL

**发布日期**: 2025-08-23 (更新: 2025-09-28)

---

## 💡 一句话要点

**提出低维残差子空间约束训练以解决稀疏字典学习中的死特征问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏自编码器` `注意力机制` `低维子空间` `字典学习` `特征初始化` `深度学习` `自然语言处理`

## 📋 核心要点

1. 现有的Transformer模型在高维空间中运行，但注意力输出却被限制在低维子空间，导致死特征问题。
2. 论文提出了一种子空间约束训练方法，通过初始化特征方向到激活的有效子空间来解决死特征问题。
3. 实验结果显示，该方法在具有100万特征的注意力输出稀疏自编码器中，死特征比例从87%降至1%以下，效果显著。

## 📝 摘要（中文）

本文探讨了现代大型语言模型中Transformer架构及其注意力机制的低维特性。研究表明，注意力输出被限制在一个低维子空间中，约60%的方向占据99%的方差，这一现象在不同模型和数据集上普遍存在。基于此，提出了一种针对稀疏自编码器的子空间约束训练方法，显著降低了死特征的比例，从87%降至1%以下，并可扩展至其他稀疏字典学习方法。研究为注意力几何提供了新见解，并为大型语言模型的稀疏字典学习提供了实用工具。

## 🔬 方法详解

**问题定义**：本文旨在解决稀疏字典学习中的死特征问题，现有方法在初始化特征时与激活空间的内在几何不匹配，导致大量无效特征的产生。

**核心思路**：通过识别注意力输出的低维结构，提出了一种子空间约束训练方法，初始化特征方向到有效的激活子空间，从而减少死特征的产生。

**技术框架**：整体架构包括特征初始化、子空间约束训练和稀疏自编码器的优化过程。主要模块包括特征方向的初始化和基于低维子空间的训练策略。

**关键创新**：最重要的创新在于识别并利用注意力输出的低维结构，显著改善了稀疏自编码器的特征学习效果，与传统方法相比，减少了死特征的比例。

**关键设计**：在参数设置上，特征方向初始化为注意力输出的有效子空间，损失函数设计为结合重构误差和稀疏性约束，网络结构采用标准的稀疏自编码器架构。

## 📊 实验亮点

实验结果表明，采用子空间约束训练的稀疏自编码器在处理具有100万特征的注意力输出时，死特征比例从87%显著降低至1%以下，展示了该方法在稀疏字典学习中的有效性与优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、计算机视觉和其他需要稀疏表示的任务。通过改善稀疏字典学习的效率和效果，能够提升大型语言模型的性能，推动相关技术的进步与应用。未来，该方法可能在更多领域中得到推广，促进智能系统的优化与发展。

## 📄 摘要（原文）

> Transformer architectures, and their attention mechanisms in particular, form the foundation of modern large language models. While transformer models are widely believed to operate in high-dimensional hidden spaces, we show that attention outputs are confined to a surprisingly low-dimensional subspace, where about 60\% of the directions account for 99\% of the variance--a phenomenon that is consistently observed across diverse model families and datasets, and is induced by the attention output projection matrix. Critically, we find this low-rank structure as a key factor of the prevalent dead feature problem in sparse dictionary learning, where it creates a mismatch between randomly initialized features and the intrinsic geometry of the activation space. Building on this insight, we propose a subspace-constrained training method for sparse autoencoders (SAEs), initializing feature directions into the active subspace of activations. Our approach reduces dead features from 87\% to below 1\% in Attention Output SAEs with 1M features, and can further extend to other sparse dictionary learning methods. Our findings provide both new insights into the geometry of attention and practical tools for improving sparse dictionary learning in large language models.

