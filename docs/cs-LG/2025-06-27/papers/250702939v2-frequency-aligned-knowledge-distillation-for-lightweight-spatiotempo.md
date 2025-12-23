---
layout: default
title: Frequency-Aligned Knowledge Distillation for Lightweight Spatiotemporal Forecasting
---

# Frequency-Aligned Knowledge Distillation for Lightweight Spatiotemporal Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.02939" class="toolbar-btn" target="_blank">📄 arXiv: 2507.02939v2</a>
  <a href="https://arxiv.org/pdf/2507.02939.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.02939v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.02939v2', 'Frequency-Aligned Knowledge Distillation for Lightweight Spatiotemporal Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuqi Li, Chuanguang Yang, Hansheng Zeng, Zeyu Dong, Zhulin An, Yongjun Xu, Yingli Tian, Hao Wu

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-06-27 (更新: 2025-07-20)

**备注**: Accepted by ICCV-2025, 11 pages

**🔗 代码/项目**: [GITHUB](https://github.com/itsnotacie/SDKD)

---

## 💡 一句话要点

**提出频率对齐知识蒸馏以解决轻量级时空预测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `时空预测` `知识蒸馏` `轻量级模型` `频率对齐` `深度学习`

## 📋 核心要点

1. 现有的时空预测模型复杂，训练效率低且内存消耗高，难以满足实时应用需求。
2. 提出的SDKD框架通过频率对齐知识蒸馏，将教师模型的多尺度特征有效转移到轻量级学生模型中。
3. 实验结果显示，SDKD在Navier-Stokes方程数据集上显著提升了预测性能，MSE和MAE分别减少了81.3%和52.3%。

## 📝 摘要（中文）

时空预测任务（如交通流、燃烧动态和天气预测）通常需要复杂模型，导致训练效率低和内存消耗高。本文提出了一种轻量级框架，称为谱解耦知识蒸馏（SDKD），该框架将复杂教师模型的多尺度时空表示转移到更高效的轻量级学生网络。教师模型采用编码器-潜在演化-解码器架构，其潜在演化模块通过卷积和Transformer解耦高频细节和低频趋势。为了解决训练缓慢和内存使用高的问题，提出了一种频率对齐知识蒸馏策略，从教师的潜在空间提取多尺度谱特征，指导轻量级学生模型捕捉局部细微变化和全局演化模式。实验结果表明，SDKD在Navier-Stokes方程数据集上显著提高了性能，均方误差（MSE）减少了81.3%，平均绝对误差（MAE）减少了52.3%。

## 🔬 方法详解

**问题定义**：本文旨在解决时空预测任务中复杂模型导致的训练效率低和内存消耗高的问题。现有方法在处理高频细节和低频趋势时存在性能瓶颈，影响了模型的实时应用能力。

**核心思路**：SDKD框架通过频率对齐知识蒸馏策略，从教师模型的潜在空间中提取多尺度谱特征，帮助轻量级学生模型有效捕捉局部变化和全局趋势。这样设计的目的是在保持预测精度的同时，降低计算复杂度。

**技术框架**：SDKD框架包括教师模型和学生模型两个主要部分。教师模型采用编码器-潜在演化-解码器结构，潜在演化模块负责解耦高频和低频信息。学生模型则通过知识蒸馏学习教师模型的特征表示。

**关键创新**：SDKD的核心创新在于频率对齐知识蒸馏策略，能够同时提取高频和低频特征，指导学生模型学习。这一方法与传统的知识蒸馏方法不同，后者通常只关注单一频率特征。

**关键设计**：在SDKD中，教师模型的潜在空间通过卷积和Transformer进行处理，提取多尺度特征。损失函数设计上，结合了高频和低频特征的蒸馏损失，确保学生模型在学习过程中能够平衡局部和全局信息。

## 📊 实验亮点

实验结果表明，SDKD在Navier-Stokes方程数据集上显著提升了模型性能，均方误差（MSE）减少了81.3%，平均绝对误差（MAE）减少了52.3%。这些结果展示了SDKD在捕捉时空变化方面的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括交通流预测、天气预报和工业过程监控等。通过提供高效的时空预测模型，SDKD能够在资源受限的环境中实现实时预测，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Spatiotemporal forecasting tasks, such as traffic flow, combustion dynamics, and weather forecasting, often require complex models that suffer from low training efficiency and high memory consumption. This paper proposes a lightweight framework, Spectral Decoupled Knowledge Distillation (termed SDKD), which transfers the multi-scale spatiotemporal representations from a complex teacher model to a more efficient lightweight student network. The teacher model follows an encoder-latent evolution-decoder architecture, where its latent evolution module decouples high-frequency details and low-frequency trends using convolution and Transformer (global low-frequency modeler). However, the multi-layer convolution and deconvolution structures result in slow training and high memory usage. To address these issues, we propose a frequency-aligned knowledge distillation strategy, which extracts multi-scale spectral features from the teacher's latent space, including both high and low frequency components, to guide the lightweight student model in capturing both local fine-grained variations and global evolution patterns. Experimental results show that SDKD significantly improves performance, achieving reductions of up to 81.3% in MSE and in MAE 52.3% on the Navier-Stokes equation dataset. The framework effectively captures both high-frequency variations and long-term trends while reducing computational complexity. Our codes are available at https://github.com/itsnotacie/SDKD

