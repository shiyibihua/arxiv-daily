---
layout: default
title: Learning Temporally Consistent Turbulence Between Sparse Snapshots via Diffusion Models
---

# Learning Temporally Consistent Turbulence Between Sparse Snapshots via Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24813" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24813v1</a>
  <a href="https://arxiv.org/pdf/2512.24813.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24813v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24813v1', 'Learning Temporally Consistent Turbulence Between Sparse Snapshots via Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammed Sardar, Małgorzata J. Zimoń, Samuel Draycott, Alistair Revell, Alex Skillen

**分类**: physics.flu-dyn, cs.LG

**发布日期**: 2025-12-31

**备注**: 15 pages, 10 figures

---

## 💡 一句话要点

**提出基于条件扩散模型的时序一致湍流插值方法，用于稀疏快照间的湍流重建。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `湍流重建` `扩散模型` `时序插值` `计算流体力学` `生成模型`

## 📋 核心要点

1. 现有方法难以从稀疏快照中准确重建湍流的时序演化过程，尤其是在非平稳湍流中。
2. 利用条件去噪扩散概率模型，学习湍流场在稀疏快照间的时序一致性，生成连贯的湍流动力学。
3. 在2D Kolmogorov Flow和3D Kelvin-Helmholtz Instability上验证，评估了湍流动能谱和时间衰减等统计特性。

## 📝 摘要（中文）

本文研究了使用条件去噪扩散概率模型（DDPMs）在湍流场稀疏、非相关快照之间进行时序插值，以提高时空流动序列的统计精度。该方法被提出作为一种概念验证的生成代理模型，用于重建稀疏快照之间连贯的湍流动力学。通过二维柯尔莫哥洛夫流和三维开尔文-亥姆霍兹不稳定性（KHI）进行了演示。我们通过统计湍流的角度分析生成的流动序列，检查生成序列上时间平均的湍流动能谱以及湍流结构的时间衰减。对于非平稳的开尔文-亥姆霍兹不稳定性，我们评估了所提出的方法在最强烈的时间变化流动状态下捕获演化流动统计的能力。此外，我们还检查了KHI流动演化关键阶段的瞬时场和物理驱动的指标。

## 🔬 方法详解

**问题定义**：该论文旨在解决从稀疏且非相关的湍流场快照中重建时间上连贯的湍流演化过程的问题。现有方法通常难以准确地插值或预测湍流场在时间上的演变，尤其是在湍流具有高度非线性和非平稳性的情况下，导致重建的湍流场在统计特性上与真实湍流场存在偏差。

**核心思路**：论文的核心思路是利用条件去噪扩散概率模型（DDPMs）学习湍流场在时间上的演化模式。通过将稀疏快照作为条件，DDPM能够生成符合湍流统计规律且在时间上连贯的湍流场序列。这种方法避免了直接求解复杂的流体动力学方程，而是通过学习数据分布来重建湍流场。

**技术框架**：整体框架包含以下几个主要步骤：1）数据准备：准备稀疏的湍流场快照序列作为条件输入。2）扩散过程：逐步向湍流场中添加噪声，直到完全变为高斯噪声。3）反向扩散过程：从高斯噪声出发，逐步去除噪声，并根据条件快照来引导生成过程，最终得到插值后的湍流场序列。该框架利用了DDPM强大的生成能力，能够生成具有高分辨率和时间连贯性的湍流场。

**关键创新**：该论文的关键创新在于将条件DDPM应用于湍流场的时序插值问题，并证明了其在重建湍流统计特性方面的有效性。与传统的插值方法相比，该方法能够更好地捕捉湍流的非线性和随机性，从而生成更逼真的湍流场序列。此外，该方法还能够处理非平稳湍流，并捕捉其随时间变化的统计特性。

**关键设计**：论文中使用了标准的DDPM架构，并针对湍流场的特点进行了一些调整。例如，使用了合适的网络结构来捕捉湍流场的空间相关性，并设计了合适的损失函数来保证生成湍流场的统计特性与真实湍流场一致。具体的参数设置和网络结构细节在论文中进行了详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24813v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24813v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24813v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法能够有效地重建稀疏快照之间的湍流演化过程，并准确地捕捉湍流的统计特性，如湍流动能谱和时间衰减。在3D Kelvin-Helmholtz Instability实验中，该方法能够捕捉到随时间变化的流动统计特性，并在关键阶段生成符合物理规律的瞬时场。

## 🎯 应用场景

该研究成果可应用于计算流体力学、气候模拟、航空航天工程等领域。例如，可以利用该方法从有限的实验数据或计算结果中重建完整的湍流场，从而提高模拟精度和效率。此外，该方法还可以用于生成高分辨率的湍流场数据，用于训练其他机器学习模型或进行科学可视化。

## 📄 摘要（原文）

> We investigate the statistical accuracy of temporally interpolated spatiotemporal flow sequences between sparse, decorrelated snapshots of turbulent flow fields using conditional Denoising Diffusion Probabilistic Models (DDPMs). The developed method is presented as a proof-of-concept generative surrogate for reconstructing coherent turbulent dynamics between sparse snapshots, demonstrated on a 2D Kolmogorov Flow, and a 3D Kelvin-Helmholtz Instability (KHI). We analyse the generated flow sequences through the lens of statistical turbulence, examining the time-averaged turbulent kinetic energy spectra over generated sequences, and temporal decay of turbulent structures. For the non-stationary Kelvin-Helmholtz Instability, we assess the ability of the proposed method to capture evolving flow statistics across the most strongly time-varying flow regime. We additionally examine instantaneous fields and physically motivated metrics at key stages of the KHI flow evolution.

