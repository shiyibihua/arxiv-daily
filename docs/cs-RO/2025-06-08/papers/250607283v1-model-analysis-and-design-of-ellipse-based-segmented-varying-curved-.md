---
layout: default
title: Model Analysis And Design Of Ellipse Based Segmented Varying Curved Foot For Biped Robot Walking
---

# Model Analysis And Design Of Ellipse Based Segmented Varying Curved Foot For Biped Robot Walking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.07283" class="toolbar-btn" target="_blank">📄 arXiv: 2506.07283v1</a>
  <a href="https://arxiv.org/pdf/2506.07283.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.07283v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.07283v1', 'Model Analysis And Design Of Ellipse Based Segmented Varying Curved Foot For Biped Robot Walking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boyang Chen, Xizhe Zang, Chao Song, Yue Zhang, Jie Zhao

**分类**: cs.RO

**发布日期**: 2025-06-08

---

## 💡 一句话要点

**提出基于椭圆的分段变曲足以提高双足机器人行走能效**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `双足机器人` `能量效率` `椭圆设计` `行走控制` `仿生设计` `非线性规划` `接触模型`

## 📋 核心要点

1. 现有双足机器人足部设计多为平面或简单曲面，无法有效模拟人类足部的复杂形状，导致能量效率低下。
2. 论文提出的ESVC足通过椭圆段的空间变换建立接触模型，并利用非线性规划优化足部参数，提升行走效率。
3. 实验结果显示，ESVC足在多种行走任务中能显著降低能量消耗，尤其在侧向行走中提升幅度达到18.52%。

## 📝 摘要（中文）

本文提出了一种基于椭圆的分段变曲足（ESVC）设计，旨在提高双足机器人行走的能量效率，同时保持足部位置控制的分析可行性。通过使用基本函数推导出完整的接触模型，采用非线性规划方法优化足部参数，并引入误差补偿方法解决近似计算问题。实验结果表明，ESVC足在多项行走任务中相比于传统平足，能量消耗降低了最多18.52%。该设计为未来数据驱动的足形优化奠定了基础。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有双足机器人足部设计在能量效率和控制可行性方面的不足，特别是无法有效模拟人类足部的复杂曲线形状。

**核心思路**：论文的核心思路是通过椭圆段的分段变曲设计，建立一个完整的接触模型，并通过优化算法提升足部的行走性能。这样的设计灵感来源于人类足部的分段曲率特性，能够更好地适应地面变化。

**技术框架**：整体架构包括三个主要模块：首先是椭圆段的空间变换模型，其次是基于非线性规划的足部参数优化，最后是与混合线性倒立摆模型结合的行走控制器。

**关键创新**：最重要的技术创新在于提出了基于椭圆的分段变曲足设计，利用简单函数推导出接触模型，解决了传统方法中复杂计算的问题。

**关键设计**：在设计过程中，采用了非线性规划方法来确定后足和前足的最佳椭圆参数，并引入误差补偿方法以提高接触模型的准确性。

## 📊 实验亮点

实验结果表明，ESVC足在标记时间、矢状面和侧向行走任务中，能量消耗相比于传统平足降低了最多18.52%。这一显著提升验证了ESVC足在实际双足行走中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括双足机器人、仿生机器人以及人机交互系统等。通过提高行走能效，ESVC足能够在实际应用中延长机器人的工作时间，提升其在复杂环境中的适应能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This paper presents the modeling, design, and experimental validation of an Ellipse-based Segmented Varying Curvature (ESVC) foot for bipedal robots. Inspired by the segmented curvature rollover shape of human feet, the ESVC foot aims to enhance gait energy efficiency while maintaining analytical tractability for foot location based controller. First, we derive a complete analytical contact model for the ESVC foot by formulating spatial transformations of elliptical segments only using elementary functions. Then a nonlinear programming approach is engaged to determine optimal elliptical parameters of hind foot and fore foot based on a known mid-foot. An error compensation method is introduced to address approximation inaccuracies in rollover length calculation. The proposed ESVC foot is then integrated with a Hybrid Linear Inverted Pendulum model-based walking controller and validated through both simulation and physical experiments on the TT II biped robot. Experimental results across marking time, sagittal, and lateral walking tasks show that the ESVC foot consistently reduces energy consumption compared to line, and flat feet, with up to 18.52\% improvement in lateral walking. These findings demonstrate that the ESVC foot provides a practical and energy-efficient alternative for real-world bipedal locomotion. The proposed design methodology also lays a foundation for data-driven foot shape optimization in future research.

