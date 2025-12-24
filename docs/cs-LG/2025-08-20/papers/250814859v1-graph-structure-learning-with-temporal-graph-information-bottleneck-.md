---
layout: default
title: Graph Structure Learning with Temporal Graph Information Bottleneck for Inductive Representation Learning
---

# Graph Structure Learning with Temporal Graph Information Bottleneck for Inductive Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14859" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14859v1</a>
  <a href="https://arxiv.org/pdf/2508.14859.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14859v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14859v1', 'Graph Structure Learning with Temporal Graph Information Bottleneck for Inductive Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiafeng Xiong, Rizos Sakellariou

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-20

**备注**: Accepted in the 28th European Conference on Artificial Intelligence (ECAI), 2025

---

## 💡 一句话要点

**提出GTGIB框架以解决动态网络中的节点表示问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `动态图学习` `归纳表示学习` `图结构学习` `信息瓶颈` `节点表示` `机器学习` `网络优化`

## 📋 核心要点

1. 现有的归纳表示学习方法在动态网络中难以有效处理未见节点和冗余信息，导致性能下降。
2. 本文提出GTGIB框架，结合图结构学习与时间图信息瓶颈，通过优化节点邻域和正则化图信息来解决上述问题。
3. 实验结果表明，GTGIB在四个真实数据集上的链接预测任务中均优于现有方法，尤其在传导设置下表现出显著提升。

## 📝 摘要（中文）

动态图学习在节点和边随时间演变的网络中至关重要，尤其是在新节点不断加入的情况下。现有的归纳表示学习面临两个主要挑战：有效表示未见节点以及减轻噪声或冗余图信息。为此，本文提出了GTGIB框架，结合了图结构学习（GSL）与时间图信息瓶颈（TGIB）。通过理论证明和实验验证，我们设计了一种新颖的两步GSL结构增强器，以丰富和优化节点邻域。TGIB通过扩展信息瓶颈原理至时间图，基于可变近似推导的TGIB目标函数，正则化边和特征，从而实现稳定高效的优化。GTGIB模型在四个真实数据集上进行链接预测，结果显示在归纳设置下优于现有方法，并在传导设置下也有显著且一致的提升。

## 🔬 方法详解

**问题定义**：本文旨在解决动态网络中归纳表示学习的挑战，特别是如何有效表示未见节点及处理冗余信息的问题。现有方法在这方面存在明显不足，导致性能受限。

**核心思路**：GTGIB框架通过结合图结构学习（GSL）与时间图信息瓶颈（TGIB），提出了一种新颖的两步结构增强器，旨在优化节点邻域并减少噪声信息。这样的设计使得模型能够更好地适应动态变化的网络环境。

**技术框架**：GTGIB的整体架构包括两个主要模块：首先是GSL结构增强器，用于丰富和优化节点的邻域信息；其次是TGIB模块，通过信息瓶颈原理对优化后的图进行正则化，确保边和特征的稳定性。

**关键创新**：GTGIB的核心创新在于将信息瓶颈原理扩展到时间图，提出了可变近似的TGIB目标函数，从而实现了对动态图的有效优化。这一方法与传统静态图学习方法有本质区别。

**关键设计**：在模型设计中，关键参数设置包括邻域大小的选择、损失函数的设计以及网络结构的深度。特别是在TGIB模块中，正则化策略的选择对模型的稳定性和优化效率至关重要。

## 📊 实验亮点

在四个真实数据集上的实验结果表明，GTGIB模型在链接预测任务中均优于现有方法，尤其在归纳设置下，性能提升幅度达到显著水平，且在传导设置下也展现出一致的改进，验证了其有效性和稳定性。

## 🎯 应用场景

GTGIB框架在社交网络分析、交通流量预测和金融网络建模等动态网络场景中具有广泛的应用潜力。通过有效处理未见节点和冗余信息，该方法能够提升动态网络的表示能力，进而推动相关领域的研究与应用发展。

## 📄 摘要（原文）

> Temporal graph learning is crucial for dynamic networks where nodes and edges evolve over time and new nodes continuously join the system. Inductive representation learning in such settings faces two major challenges: effectively representing unseen nodes and mitigating noisy or redundant graph information. We propose GTGIB, a versatile framework that integrates Graph Structure Learning (GSL) with Temporal Graph Information Bottleneck (TGIB). We design a novel two-step GSL-based structural enhancer to enrich and optimize node neighborhoods and demonstrate its effectiveness and efficiency through theoretical proofs and experiments. The TGIB refines the optimized graph by extending the information bottleneck principle to temporal graphs, regularizing both edges and features based on our derived tractable TGIB objective function via variational approximation, enabling stable and efficient optimization. GTGIB-based models are evaluated to predict links on four real-world datasets; they outperform existing methods in all datasets under the inductive setting, with significant and consistent improvement in the transductive setting.

