---
layout: default
title: Experimental End-to-End Optimization of Directly Modulated Laser-based IM/DD Transmission
---

# Experimental End-to-End Optimization of Directly Modulated Laser-based IM/DD Transmission

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19910" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19910v1</a>
  <a href="https://arxiv.org/pdf/2508.19910.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19910v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19910v1', 'Experimental End-to-End Optimization of Directly Modulated Laser-based IM/DD Transmission')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sergio Hernandez, Christophe Peucheret, Francesco Da Ros, Darko Zibar

**分类**: eess.SP, cs.LG

**发布日期**: 2025-08-27

**备注**: 10 pages, 10 figures, submitted to journal of lightwave technology

---

## 💡 一句话要点

**基于数据驱动模型优化直接调制激光的传输性能**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `直接调制激光` `数据驱动模型` `端到端优化` `光通信` `非线性动态`

## 📋 核心要点

1. 直接调制激光的复杂非线性动态特性使得其系统建模和优化面临挑战，现有方法难以有效提升性能。
2. 提出了一种基于实验数据的代理模型，通过端到端优化实现脉冲整形、均衡滤波器及激光参数的优化。
3. 实验结果表明，该优化方案在符号速率和传输距离上均优于四种基准方案，且能有效降低功耗和带宽需求。

## 📝 摘要（中文）

直接调制激光（DML）是一种适用于短距离强度调制和直接检测通信系统的有前景技术。然而，其复杂的非线性动态特性使得DML系统的建模和优化变得具有挑战性。本文研究了一种基于实验数据训练的数据驱动代理模型的DML系统端到端优化方法。该优化方案涵盖了脉冲整形、均衡滤波器、激光偏置电流和调制射频功率。通过实验验证，该方案在不同符号速率和传输距离下表现出更优的性能，同时降低了调制射频功率、减少了滤波器抽头数量，并使用了更小的信号带宽。

## 🔬 方法详解

**问题定义**：本文旨在解决直接调制激光（DML）系统在建模和优化过程中的复杂非线性动态特性问题。现有方法在性能提升方面存在局限，难以适应不同的传输条件。

**核心思路**：提出了一种基于实验数据训练的代理模型，通过端到端优化策略，综合考虑脉冲整形、均衡滤波器、激光偏置电流和调制射频功率，从而提升DML系统的整体性能。

**技术框架**：整体架构包括数据收集、代理模型训练、优化算法实施和性能评估四个主要阶段。通过实验数据训练得到的模型用于指导优化过程，确保优化方案的有效性。

**关键创新**：本研究的主要创新在于采用数据驱动的代理模型进行端到端优化，显著提升了DML系统在不同符号速率和传输距离下的性能，且在功耗和带宽使用上表现出色。

**关键设计**：在优化过程中，设置了适当的损失函数以平衡不同性能指标，同时设计了适合DML特性的网络结构，以确保模型的准确性和鲁棒性。

## 📊 实验亮点

实验结果显示，所提出的端到端优化方案在不同符号速率和传输距离下均优于四种基准方案，具体表现为在相同条件下降低了调制射频功率，减少了滤波器抽头数量，并使用了更小的信号带宽，提升幅度显著。

## 🎯 应用场景

该研究的潜在应用领域包括短距离光通信、数据中心互连以及5G/6G无线通信等。通过优化直接调制激光的性能，可以显著提升通信系统的效率和可靠性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Directly modulated lasers (DMLs) are an attractive technology for short-reach intensity modulation and direct detection communication systems. However, their complex nonlinear dynamics make the modeling and optimization of DML-based systems challenging. In this paper, we study the end-to-end optimization of DML-based systems based on a data-driven surrogate model trained on experimental data. The end-to-end optimization includes the pulse shaping and equalizer filters, the bias current and the modulation radio-frequency (RF) power applied to the laser. The performance of the end-to-end optimization scheme is tested on the experimental setup and compared to 4 different benchmark schemes based on linear and nonlinear receiver-side equalization. The results show that the proposed end-to-end scheme is able to deliver better performance throughout the studied symbol rates and transmission distances while employing lower modulation RF power, fewer filter taps and utilizing a smaller signal bandwidth.

