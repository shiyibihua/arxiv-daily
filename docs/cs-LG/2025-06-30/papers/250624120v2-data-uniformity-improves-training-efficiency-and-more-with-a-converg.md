---
layout: default
title: Data Uniformity Improves Training Efficiency and More, with a Convergence Framework Beyond the NTK Regime
---

# Data Uniformity Improves Training Efficiency and More, with a Convergence Framework Beyond the NTK Regime

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24120" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24120v2</a>
  <a href="https://arxiv.org/pdf/2506.24120.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24120v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24120v2', 'Data Uniformity Improves Training Efficiency and More, with a Convergence Framework Beyond the NTK Regime')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuqing Wang, Shangding Gu

**分类**: cs.LG, cs.AI, math.OC, stat.ML

**发布日期**: 2025-06-30 (更新: 2025-09-29)

**🔗 代码/项目**: [GITHUB](https://github.com/SafeRL-Lab/data-uniformity)

---

## 💡 一句话要点

**提出数据均匀性选择以提升训练效率和性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据选择` `训练效率` `神经网络` `均匀分布` `收敛框架` `深度学习` `大型语言模型`

## 📋 核心要点

1. 现有的数据选择方法通常依赖于任务特性，缺乏通用性，导致在复杂任务中性能提升有限。
2. 本文提出通过选择均匀分布的数据来提高训练效率，建立了一个新的收敛框架，适用于多种神经网络架构。
3. 实验结果表明，最大化数据点之间的成对距离显著加速了训练过程，并在大型语言模型上取得了优异的性能。

## 📝 摘要（中文）

数据选择在数据驱动决策中至关重要，尤其是在大型语言模型（LLMs）中，通常依赖于具体任务。尽管数据质量和多样性已被广泛研究并被认为能提升模型性能，但是否存在其他定量和通用的数据选择原则仍不明确。本文展示了选择更均匀分布的数据可以提高训练效率并增强性能。我们证明了更均匀的分布导致数据点之间的最小成对距离增大，并且较小的最小成对距离会减缓梯度下降的训练动态。此外，我们理论上表明，神经网络的近似误差随着最小成对距离的增加而减少。我们的分析引入了一个超越神经切线核（NTK）范畴的收敛框架，适用于包括变换器在内的广泛架构。最后，我们在多种设置下进行了全面的实验，结果表明通过最大化成对距离选择数据显著加速训练并在不同数据集上实现了可比或更好的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决数据选择在复杂任务中的通用性不足问题，现有方法往往依赖于特定任务的特性，导致性能提升不稳定。

**核心思路**：论文提出选择均匀分布的数据，以增大数据点之间的最小成对距离，从而提高训练效率和模型性能。通过理论分析，证明了最小成对距离与训练动态和近似误差之间的关系。

**技术框架**：研究建立了一个超越神经切线核（NTK）范畴的收敛框架，适用于多种神经网络架构，包括变换器。该框架不要求Lipschitz光滑性，提供了对残差连接和函数组合的理论支持。

**关键创新**：最重要的创新在于提出了通过均匀选择数据来优化训练过程的理论框架，明确了最小成对距离对训练动态的影响，这在现有研究中尚未得到充分探讨。

**关键设计**：在实验中，选择数据时最大化成对距离的策略被应用于不同的优化策略、模型规模和训练数据集，确保了实验结果的广泛适用性。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文获取更多细节。

## 📊 实验亮点

实验结果显示，通过选择均匀分布的数据，训练速度显著加快，且在大型语言模型上实现了与基线模型相当或更好的性能。具体而言，最大化成对距离的策略在多种数据集上均表现出色，提升幅度明显。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、计算机视觉等数据驱动的任务，尤其是在需要处理复杂数据集的场景中。通过优化数据选择策略，可以显著提升模型的训练效率和最终性能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Data selection plays a crucial role in data-driven decision-making, including in large language models (LLMs), and is typically task-dependent. Properties such as data quality and diversity have been extensively studied and are known to enhance model performance. However, it remains unclear whether there exist other quantitative and general principles of data selection that can consistently improve performance, especially for complicated tasks. In this paper, we demonstrate that selecting more uniformly distributed data can improve training efficiency while enhancing performance. Specifically, we establish that more uniform (less biased) distribution leads to a larger minimum pairwise distance between data points, denoted by $h_{\min}$, and prove that a smaller $h_{\min}$ can slow down the training dynamics of gradient descent (GD). Moreover, we theoretically show that the approximation error of neural networks decreases as $h_{\min}$ increases. Our analysis introduces a convergence framework for GD beyond the Neural Tangent Kernel (NTK) regime, applicable to a broad class of architectures, including transformers, without requiring Lipschitz smoothness. This framework further provides theoretical justification for the use of residual connection and function composition in deep neural architectures. In the end, we conduct comprehensive experiments for supervised fine-tuning across various settings, including different optimization strategies, model sizes, and training datasets. The results consistently demonstrate that selecting data by maximizing pairwise distance significantly accelerates training and achieves comparable or better performance in LLMs across diverse datasets. Code and Datasets are available at the link: https://github.com/SafeRL-Lab/data-uniformity.

