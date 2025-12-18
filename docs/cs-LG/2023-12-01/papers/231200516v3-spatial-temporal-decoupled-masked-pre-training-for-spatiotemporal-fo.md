---
layout: default
title: Spatial-Temporal-Decoupled Masked Pre-training for Spatiotemporal Forecasting
---

# Spatial-Temporal-Decoupled Masked Pre-training for Spatiotemporal Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00516" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00516v3</a>
  <a href="https://arxiv.org/pdf/2312.00516.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00516v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00516v3', 'Spatial-Temporal-Decoupled Masked Pre-training for Spatiotemporal Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haotian Gao, Renhe Jiang, Zheng Dong, Jinliang Deng, Yuxin Ma, Xuan Song

**分类**: cs.LG

**发布日期**: 2023-12-01 (更新: 2024-04-28)

**备注**: Accepted at IJCAI-2024 Main Track

**🔗 代码/项目**: [GITHUB](https://github.com/Jimmy-7664/STD-MAE)

---

## 💡 一句话要点

**提出空间-时间解耦的掩蔽预训练方法以解决时空预测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `时空预测` `自监督学习` `掩蔽自编码器` `深度学习` `数据重建` `智能交通` `能源管理`

## 📋 核心要点

1. 现有的时空预测模型受到输入长度的限制，容易出现时空幻影现象，导致预测准确性下降。
2. 提出的STD-MAE框架通过两个解耦的掩蔽自编码器分别在空间和时间维度上重建时空序列，从而学习丰富的上下文表示。
3. 在六个基准数据集上进行的实验表明，STD-MAE在时空预测任务中表现出色，显著提升了预测准确性。

## 📝 摘要（中文）

时空预测技术在交通、能源和天气等多个领域具有重要意义。然而，由于复杂的时空异质性，准确预测时空序列仍然面临挑战。现有的端到端模型受到输入长度的限制，常常陷入时空幻影，即相似的输入时间序列后跟不相似的未来值。为了解决这些问题，本文提出了一种新颖的自监督预训练框架——空间-时间解耦掩蔽预训练（STD-MAE），该框架采用两个解耦的掩蔽自编码器在空间和时间维度上重建时空序列。通过这种重建学习到的丰富上下文表示可以无缝集成到下游预测器中，以增强其性能。本文在六个广泛使用的基准数据集上进行了定量和定性评估，验证了STD-MAE的最先进性能。

## 🔬 方法详解

**问题定义**：本文旨在解决时空预测中的时空幻影问题，现有方法因输入长度限制而难以准确预测未来值。

**核心思路**：STD-MAE通过解耦的掩蔽自编码器在空间和时间维度上进行重建，旨在学习更丰富的上下文信息，从而提高预测性能。

**技术框架**：该框架包括两个主要模块：空间掩蔽自编码器和时间掩蔽自编码器。首先，输入的时空序列被掩蔽，然后分别通过两个自编码器进行重建，最终将学习到的表示整合用于下游任务。

**关键创新**：STD-MAE的创新在于其解耦的设计，使得模型能够分别捕捉空间和时间的特征，从而克服了传统方法的局限性。

**关键设计**：在模型设计中，采用了适应性掩蔽策略和多层自编码器结构，损失函数则结合了重建误差和上下文一致性，以确保学习到的表示具有良好的泛化能力。

## 📊 实验亮点

在六个基准数据集（PEMS03、PEMS04、PEMS07、PEMS08、METR-LA和PEMS-BAY）上的实验结果显示，STD-MAE在时空预测任务中达到了最先进的性能，相较于现有基线模型，预测准确性提升了显著的百分比，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、能源管理和气象预测等。通过提高时空预测的准确性，STD-MAE能够为决策支持系统提供更可靠的数据基础，进而优化资源配置和提高效率。未来，该方法可能在更多复杂时空数据分析任务中发挥重要作用。

## 📄 摘要（原文）

> Spatiotemporal forecasting techniques are significant for various domains such as transportation, energy, and weather. Accurate prediction of spatiotemporal series remains challenging due to the complex spatiotemporal heterogeneity. In particular, current end-to-end models are limited by input length and thus often fall into spatiotemporal mirage, i.e., similar input time series followed by dissimilar future values and vice versa. To address these problems, we propose a novel self-supervised pre-training framework Spatial-Temporal-Decoupled Masked Pre-training (STD-MAE) that employs two decoupled masked autoencoders to reconstruct spatiotemporal series along the spatial and temporal dimensions. Rich-context representations learned through such reconstruction could be seamlessly integrated by downstream predictors with arbitrary architectures to augment their performances. A series of quantitative and qualitative evaluations on six widely used benchmarks (PEMS03, PEMS04, PEMS07, PEMS08, METR-LA, and PEMS-BAY) are conducted to validate the state-of-the-art performance of STD-MAE. Codes are available at https://github.com/Jimmy-7664/STD-MAE.

