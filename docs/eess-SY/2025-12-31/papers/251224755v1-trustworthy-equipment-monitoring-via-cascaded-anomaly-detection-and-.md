---
layout: default
title: Trustworthy Equipment Monitoring via Cascaded Anomaly Detection and Thermal Localization
---

# Trustworthy Equipment Monitoring via Cascaded Anomaly Detection and Thermal Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24755" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24755v1</a>
  <a href="https://arxiv.org/pdf/2512.24755.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24755v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24755v1', 'Trustworthy Equipment Monitoring via Cascaded Anomaly Detection and Thermal Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sungwoo Kang

**分类**: eess.SY

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**提出级联异常检测框架，用于设备状态监测与可信故障定位。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `异常检测` `故障定位` `多模态融合` `时间序列分析` `可解释性AI` `预测性维护` `LSTM` `CNN`

## 📋 核心要点

1. 现有设备监测方法在多模态融合时存在性能下降问题，简单融合可能引入模态偏差。
2. 提出级联异常检测框架，解耦检测与定位任务，利用传感器数据进行精确检测，热图像数据进行故障定位。
3. 实验表明，该方法在轴承数据集上优于传统融合方法，F1分数提升8.3%，并提供可解释性分析。

## 📝 摘要（中文）

预测性维护需要准确的异常检测和可信的解释。虽然传感器时序数据和热图像的多模态融合显示出潜力，但我们证明了简单的融合策略可能会适得其反，降低性能。本文介绍了一种级联异常检测框架，该框架将检测和定位解耦。第一阶段采用基于LSTM的传感器编码器，结合时间注意力机制，实现高精度检测；第二阶段激活基于CNN的热编码器，用于检测后的故障定位。结果表明，仅使用传感器进行检测的性能优于完全融合，F1分数提高了8.3个百分点（93.08% vs. 84.79%），挑战了额外模态总能提高性能的假设。我们进一步贡献了一个可解释性流程，集成了SHAP、时间/空间注意力以及门权重分析。该分析揭示了一种“模态偏差”，即融合模型将65-87%的权重分配给较弱的热模态。在真实轴承数据集（78,397个样本）上的验证表明，我们的级联方法实现了最先进的精度，同时为维护决策提供可操作的诊断。

## 🔬 方法详解

**问题定义**：现有方法在设备异常检测中，简单地融合来自不同模态（如传感器数据和热图像）的信息，期望获得更好的性能。然而，这种简单的融合策略可能会由于模态之间的差异和噪声，导致性能下降，甚至不如仅使用单一模态的效果。特别是，当某些模态的信息质量较低时，融合反而会引入偏差，影响检测的准确性。

**核心思路**：本文的核心思路是将异常检测和故障定位这两个任务解耦，采用级联的方式进行处理。首先，利用高质量的传感器数据进行精确的异常检测，然后再利用热图像数据进行故障定位。这种解耦的方式可以避免低质量模态对检测精度的干扰，同时充分利用不同模态的优势。

**技术框架**：该框架包含两个主要阶段：异常检测阶段和故障定位阶段。在异常检测阶段，使用基于LSTM的传感器编码器，并引入时间注意力机制，以捕捉传感器时序数据中的关键信息。在故障定位阶段，使用基于CNN的热编码器，对检测到的异常进行定位，确定故障发生的具体位置。整个流程是先检测，后定位，形成一个级联的结构。

**关键创新**：该方法最重要的创新点在于提出了级联的异常检测框架，将检测和定位任务分离，避免了简单融合带来的模态偏差问题。此外，该方法还引入了可解释性分析流程，通过SHAP、时间/空间注意力以及门权重分析，揭示了模型决策的过程，提高了模型的可信度。

**关键设计**：在异常检测阶段，LSTM编码器采用时间注意力机制，能够自动学习不同时间步的重要性，从而更好地捕捉时序数据中的异常模式。在故障定位阶段，CNN编码器能够有效地提取热图像中的空间特征，从而实现精确的故障定位。此外，可解释性分析流程通过SHAP值来评估不同特征对预测结果的贡献，通过注意力权重来分析模型关注的关键区域，通过门权重来评估不同模态的重要性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24755v1/figures/cascaded_pipeline.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24755v1/figures/ablation_comparison.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24755v1/figures/shap_sensor_importance.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该级联异常检测框架在轴承数据集上取得了显著的性能提升。仅使用传感器数据的检测F1分数达到93.08%，优于多模态融合的84.79%，提升了8.3个百分点。同时，可解释性分析揭示了融合模型中存在的模态偏差，为模型优化提供了重要依据。

## 🎯 应用场景

该研究成果可广泛应用于工业设备的状态监测和预测性维护领域，例如轴承、电机、泵等关键设备的健康管理。通过早期发现设备异常并精确定位故障，可以有效降低设备停机时间，减少维护成本，提高生产效率，并为维护决策提供可靠依据。

## 📄 摘要（原文）

> Predictive maintenance demands accurate anomaly detection and trustable explanations. Although multimodal fusion of sensor time-series and thermal imagery shows promise, we demonstrate that naive fusion strategies can paradoxically degrade performance. This paper introduces a Cascaded Anomaly Detection framework that decouples detection and localization. Stage 1 employs an LSTM-based sensor encoder with temporal attention for high-accuracy detection, while Stage 2 activates a CNN-based thermal encoder for post-detection fault localization. Our results reveal that sensor-only detection outperforms full fusion by 8.3 percentage points (93.08% vs. 84.79% F1-score), challenging the assumption that additional modalities invariably improve performance. We further contribute an explainability pipeline integrating SHAP, temporal/spatial attention, and gate weight analysis. This analysis uncovers a "modality bias" where fusion models assign 65-87% weight to the weaker thermal modality. Validated on a real-world bearing dataset (78,397 samples), our cascaded approach achieves state-of-the-art accuracy while providing actionable diagnostics for maintenance decision-making.

