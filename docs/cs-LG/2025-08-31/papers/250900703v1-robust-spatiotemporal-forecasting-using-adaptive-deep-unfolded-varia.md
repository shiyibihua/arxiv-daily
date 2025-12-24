---
layout: default
title: Robust Spatiotemporal Forecasting Using Adaptive Deep-Unfolded Variational Mode Decomposition
---

# Robust Spatiotemporal Forecasting Using Adaptive Deep-Unfolded Variational Mode Decomposition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00703" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00703v1</a>
  <a href="https://arxiv.org/pdf/2509.00703.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00703v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00703v1', 'Robust Spatiotemporal Forecasting Using Adaptive Deep-Unfolded Variational Mode Decomposition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Osama Ahmad, Lukas Wesemann, Fabian Waschkowski, Zubair Khalid

**分类**: cs.LG

**发布日期**: 2025-08-31

**备注**: Under review in IEEE Signal Processing Letter

---

## 💡 一句话要点

**提出模式自适应图网络以解决时空预测中的计算效率问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `时空预测` `图神经网络` `变分模式分解` `深度学习` `计算效率` `可学习参数` `信号处理`

## 📋 核心要点

1. 现有方法在处理复杂的时空预测时面临计算效率低和手动超参数调优的挑战。
2. 本文提出的模式自适应图网络（MAGN）通过将迭代VMD转化为可训练模块，显著提高了计算效率。
3. 在LargeST基准测试中，MAGN在预测误差上实现了85-95%的减少，表现优于现有最先进的方法。

## 📝 摘要（中文）

准确的时空预测对许多复杂系统至关重要，但由于传统图神经网络（GNN）中的复杂波动模式和谱纠缠，这一任务仍然具有挑战性。尽管集成分解的方法如变分模式图卷积网络（VMGCN）通过信号分解提高了准确性，但在计算效率和手动超参数调优方面存在不足。为了解决这些局限性，本文提出了模式自适应图网络（MAGN），将迭代变分模式分解（VMD）转化为可训练的神经模块。我们的关键创新包括：1）展开的VMD（UVMD）模块，用固定深度网络替代迭代优化，减少了分解时间（在LargeST基准上减少250倍）；2）特定模式的可学习带宽约束（αk），适应空间异质性，消除手动调优，同时防止谱重叠。在LargeST基准上（6902个传感器，2.41亿个观测值），MAGN在预测误差上实现了85-95%的减少，超越了最先进的基线。

## 🔬 方法详解

**问题定义**：本文旨在解决传统图神经网络在时空预测中面临的计算效率低和手动超参数调优的问题。现有的变分模式图卷积网络（VMGCN）虽然提高了预测准确性，但在计算上仍然效率不高。

**核心思路**：论文提出的模式自适应图网络（MAGN）通过将迭代的变分模式分解（VMD）转化为一个可训练的神经网络模块，避免了传统方法中的迭代优化过程，从而提高了计算效率。

**技术框架**：MAGN的整体架构包括展开的VMD（UVMD）模块和模式特定的可学习带宽约束。UVMD模块用固定深度的网络结构替代了迭代优化，带宽约束则适应了空间异质性。

**关键创新**：MAGN的主要创新在于将VMD转化为可训练模块，显著减少了分解时间（在LargeST基准上减少250倍），并通过可学习的带宽约束消除了手动调优的需求。

**关键设计**：在设计中，MAGN使用了特定模式的可学习带宽约束（αk），以适应不同的空间特性，并防止谱重叠，确保了模型的有效性和准确性。该模型在LargeST基准上经过了大量的实验验证，显示出其优越性。

## 📊 实验亮点

在LargeST基准测试中，MAGN在预测误差上实现了85-95%的减少，相较于变分模式图卷积网络（VMGCN）表现出显著的性能提升，且在计算效率上减少了250倍，展示了其在时空预测领域的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括交通流量预测、气象预报、环境监测等复杂系统的时空数据分析。通过提高时空预测的准确性和效率，MAGN能够为城市管理、灾害预警等实际应用提供重要支持，具有显著的社会和经济价值。

## 📄 摘要（原文）

> Accurate spatiotemporal forecasting is critical for numerous complex systems but remains challenging due to complex volatility patterns and spectral entanglement in conventional graph neural networks (GNNs). While decomposition-integrated approaches like variational mode graph convolutional network (VMGCN) improve accuracy through signal decomposition, they suffer from computational inefficiency and manual hyperparameter tuning. To address these limitations, we propose the mode adaptive graph network (MAGN) that transforms iterative variational mode decomposition (VMD) into a trainable neural module. Our key innovations include (1) an unfolded VMD (UVMD) module that replaces iterative optimization with a fixed-depth network to reduce the decomposition time (by 250x for the LargeST benchmark), and (2) mode-specific learnable bandwidth constraints (αk ) adapt spatial heterogeneity and eliminate manual tuning while preventing spectral overlap. Evaluated on the LargeST benchmark (6,902 sensors, 241M observations), MAGN achieves an 85-95% reduction in the prediction error over VMGCN and outperforms state-of-the-art baselines.

