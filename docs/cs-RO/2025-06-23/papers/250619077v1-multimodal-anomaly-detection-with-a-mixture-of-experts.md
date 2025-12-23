---
layout: default
title: Multimodal Anomaly Detection with a Mixture-of-Experts
---

# Multimodal Anomaly Detection with a Mixture-of-Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19077" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19077v1</a>
  <a href="https://arxiv.org/pdf/2506.19077.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19077v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19077v1', 'Multimodal Anomaly Detection with a Mixture-of-Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christoph Willibald, Daniel Sliwowski, Dongheui Lee

**分类**: cs.RO

**发布日期**: 2025-06-23

**备注**: 8 pages, 5 figures, 1 table, the paper has been accepted for publication in the Proceedings of the 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025)

---

## 💡 一句话要点

**提出混合专家模型以解决多模态异常检测问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态异常检测` `混合专家模型` `视觉-语言模型` `高斯混合回归` `机器人操作` `环境监测`

## 📋 核心要点

1. 现有的异常检测方法通常只关注机器人驱动或环境驱动的异常，无法有效捕捉两者的综合影响。
2. 本文提出的混合专家框架整合了视觉-语言模型与高斯混合回归检测器，以实现多模态异常检测。
3. 实验结果表明，该方法在检测延迟上减少了60%，并且在逐帧异常检测性能上优于单一检测器。

## 📝 摘要（中文）

随着机器人在多种应用中的广泛部署，稳健的多模态异常检测变得愈发重要。在机器人操作中，故障通常源于机器人驱动的异常和环境驱动的异常。传统的异常检测方法通常只关注其中一种来源，导致无法全面捕捉异常。为此，本文提出了一种混合专家框架，结合视觉-语言模型和基于高斯混合回归的检测器，动态选择最可靠的检测器进行融合。通过在家庭和工业任务上的评估，验证了该方法在检测延迟和性能上的显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态异常检测中的不足，现有方法往往只关注机器人驱动或环境驱动的异常，导致无法全面捕捉异常情况。

**核心思路**：提出的混合专家框架通过结合不同的检测机制，利用视觉-语言模型监测环境变化，同时使用高斯混合回归检测器跟踪机器人运动和交互力的偏差，从而实现更全面的异常检测。

**技术框架**：整体架构包括两个主要模块：视觉-语言模型用于环境监测，和高斯混合回归检测器用于跟踪机器人行为。通过信心基础的融合机制，动态选择最可靠的检测器。

**关键创新**：最重要的创新在于引入了信心基础的融合机制，使得在不同情况下能够选择最适合的检测器，提升了检测的准确性和效率。

**关键设计**：在设计中，采用了高斯混合模型进行异常检测，结合了多模态数据的特征，确保了模型在不同环境和任务下的适应性。

## 📊 实验亮点

实验结果显示，提出的方法在家庭和工业任务中相比于单一检测器，检测延迟减少了60%，并且在逐帧异常检测性能上有显著提升，证明了混合专家框架的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括家庭自动化、工业机器人操作及其他需要实时监测和异常检测的场景。通过提高异常检测的准确性和效率，能够显著提升机器人在复杂环境中的操作安全性和可靠性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> With a growing number of robots being deployed across diverse applications, robust multimodal anomaly detection becomes increasingly important. In robotic manipulation, failures typically arise from (1) robot-driven anomalies due to an insufficient task model or hardware limitations, and (2) environment-driven anomalies caused by dynamic environmental changes or external interferences. Conventional anomaly detection methods focus either on the first by low-level statistical modeling of proprioceptive signals or the second by deep learning-based visual environment observation, each with different computational and training data requirements. To effectively capture anomalies from both sources, we propose a mixture-of-experts framework that integrates the complementary detection mechanisms with a visual-language model for environment monitoring and a Gaussian-mixture regression-based detector for tracking deviations in interaction forces and robot motions. We introduce a confidence-based fusion mechanism that dynamically selects the most reliable detector for each situation. We evaluate our approach on both household and industrial tasks using two robotic systems, demonstrating a 60% reduction in detection delay while improving frame-wise anomaly detection performance compared to individual detectors.

