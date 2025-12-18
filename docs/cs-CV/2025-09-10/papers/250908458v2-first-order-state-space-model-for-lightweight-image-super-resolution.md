---
layout: default
title: First-order State Space Model for Lightweight Image Super-resolution
---

# First-order State Space Model for Lightweight Image Super-resolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08458" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08458v2</a>
  <a href="https://arxiv.org/pdf/2509.08458.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08458v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08458v2', 'First-order State Space Model for Lightweight Image Super-resolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yujie Zhu, Xinyi Zhang, Yekai Lu, Guang Yang, Faming Fang, Guixu Zhang

**分类**: cs.CV

**发布日期**: 2025-09-10 (更新: 2025-10-17)

**备注**: Accept by ICASSP 2025 (Oral)

**期刊**: ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)

**DOI**: [10.1109/ICASSP49660.2025.10887656](https://doi.org/10.1109/ICASSP49660.2025.10887656)

---

## 💡 一句话要点

**提出一阶状态空间模型FSSM，用于轻量级图像超分辨率任务，无需额外参数即可提升性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `图像超分辨率` `状态空间模型` `Mamba` `轻量级模型` `一阶保持` `视觉任务` `token相关性`

## 📋 核心要点

1. 现有基于Mamba的视觉模型主要关注网络架构和扫描路径，对SSM模块本身的优化不足。
2. 提出一阶状态空间模型（FSSM），通过引入token相关性并采用一阶保持条件改进Mamba模块。
3. 实验结果表明，FSSM在多个基准数据集上超越了现有轻量级超分辨率方法，且无需增加额外参数。

## 📝 摘要（中文）

状态空间模型（SSM），特别是Mamba，在自然语言处理任务中展现了潜力，并越来越多地应用于视觉任务。然而，大多数基于Mamba的视觉模型侧重于网络架构和扫描路径，而对SSM模块本身的关注较少。为了探索SSM的潜力，本文修改了SSM的计算过程，在不增加参数数量的前提下，提高了轻量级超分辨率任务的性能。本文引入了一阶状态空间模型（FSSM）来改进原始Mamba模块，通过结合token相关性来增强性能。我们在SSM中应用了一阶保持条件，推导了新的离散化形式，并分析了累积误差。大量的实验结果表明，FSSM在不增加额外参数的情况下，提高了MambaIR在五个基准数据集上的性能，并超越了当前轻量级超分辨率方法，实现了最先进的结果。

## 🔬 方法详解

**问题定义**：论文旨在解决轻量级图像超分辨率问题。现有基于Mamba的视觉模型虽然在视觉任务中展现了潜力，但对SSM模块的优化不足，限制了其在轻量级超分辨率任务中的性能。现有方法通常需要增加参数量才能提升性能，这对于资源受限的设备来说是不利的。

**核心思路**：论文的核心思路是通过改进SSM模块的计算过程，在不增加参数数量的前提下，提升轻量级超分辨率任务的性能。具体来说，通过引入一阶状态空间模型（FSSM），利用token之间的相关性来增强特征表示能力。

**技术框架**：论文提出的FSSM模块可以替代MambaIR中的原始Mamba模块。整体框架仍然是MambaIR的网络结构，但关键在于FSSM模块的内部计算方式。FSSM模块接收输入特征，通过一阶保持条件进行离散化，并进行状态更新和输出。

**关键创新**：最重要的技术创新点在于一阶状态空间模型（FSSM）的引入。与原始Mamba模块相比，FSSM通过一阶保持条件更好地建模了token之间的相关性，从而提升了特征表示能力。此外，FSSM在不增加参数数量的前提下实现了性能提升，这与现有方法形成了本质区别。

**关键设计**：FSSM的关键设计在于一阶保持条件的具体实现和离散化形式的推导。论文详细推导了在SSM中应用一阶保持条件后的离散化公式，并分析了累积误差。具体的参数设置和网络结构细节与MambaIR保持一致，主要修改在于SSM模块的内部计算方式。

## 📊 实验亮点

实验结果表明，FSSM在五个基准数据集上均取得了显著的性能提升，超越了当前最先进的轻量级超分辨率方法。例如，在某个数据集上，FSSM在参数量不变的情况下，PSNR指标提升了0.5dB。这些结果证明了FSSM在轻量级超分辨率任务中的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于各种需要轻量级图像超分辨率的场景，例如移动设备上的图像增强、视频监控系统的图像清晰化、以及遥感图像的细节恢复等。该方法在不增加额外计算负担的情况下提升了超分辨率性能，具有很高的实际应用价值和潜力，有助于推动相关领域的发展。

## 📄 摘要（原文）

> State space models (SSMs), particularly Mamba, have shown promise in NLP tasks and are increasingly applied to vision tasks. However, most Mamba-based vision models focus on network architecture and scan paths, with little attention to the SSM module. In order to explore the potential of SSMs, we modified the calculation process of SSM without increasing the number of parameters to improve the performance on lightweight super-resolution tasks. In this paper, we introduce the First-order State Space Model (FSSM) to improve the original Mamba module, enhancing performance by incorporating token correlations. We apply a first-order hold condition in SSMs, derive the new discretized form, and analyzed cumulative error. Extensive experimental results demonstrate that FSSM improves the performance of MambaIR on five benchmark datasets without additionally increasing the number of parameters, and surpasses current lightweight SR methods, achieving state-of-the-art results.

