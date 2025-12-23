---
layout: default
title: Noise Fusion-based Distillation Learning for Anomaly Detection in Complex Industrial Environments
---

# Noise Fusion-based Distillation Learning for Anomaly Detection in Complex Industrial Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16050" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16050v1</a>
  <a href="https://arxiv.org/pdf/2506.16050.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16050v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16050v1', 'Noise Fusion-based Distillation Learning for Anomaly Detection in Complex Industrial Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiawen Yu, Jieji Ren, Yang Chang, Qiaojun Yu, Xuan Tong, Boyang Wang, Yan Song, You Li, Xinji Mai, Wenqiang Zhang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-06-19

**备注**: IROS 2025 Oral

**🔗 代码/项目**: [PROJECT_PAGE](https://zihuatanejoyu.github.io/HetNet/)

---

## 💡 一句话要点

**提出基于噪声融合的蒸馏学习以解决复杂工业环境中的异常检测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `异常检测` `蒸馏学习` `工业环境` `特征融合` `高斯噪声` `深度学习` `机器视觉`

## 📋 核心要点

1. 现有方法在复杂和非结构化的工业环境中检测工件缺陷时面临视角、姿态和光照变化的挑战。
2. 本文提出的HetNet框架结合了协作蒸馏网络和噪声生成模块，旨在处理扰动模式的输入数据。
3. 实验结果显示，HetNet在多个基准测试中表现优异，尤其在MSC-AD上提升约10%，验证了其在实际工业环境中的有效性。

## 📝 摘要（中文）

在自动化工业制造中，异常检测和定位能够显著提升生产效率和产品质量。现有方法在预定义或受控的成像环境中能够检测表面缺陷，但在复杂和非结构化的工业环境中，面对不同视角、姿态和光照条件，准确检测工件缺陷仍然具有挑战性。本文提出了一种新颖的异常检测和定位方法，专门设计用于处理具有扰动模式的输入。我们的方法引入了一个基于协作蒸馏的异构教师网络（HetNet）、自适应局部-全局特征融合模块和局部多元高斯噪声生成模块。HetNet能够利用有限的局部干扰变化信息来建模正常模式的复杂特征分布。实验结果表明，HetNet在工业条件下的MSC-AD评估指标上提升约10%，并在其他数据集上取得了最先进的结果，验证了其对环境波动的鲁棒性及在多样场景中增强工业异常检测系统可靠性的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂工业环境中进行异常检测时，现有方法对环境变化的敏感性和鲁棒性不足的问题。现有技术在多变的视角、姿态和光照条件下难以准确检测工件缺陷。

**核心思路**：论文提出了一种基于协作蒸馏的异构教师网络（HetNet），通过自适应特征融合和噪声生成来增强模型对扰动模式的适应能力，从而提高异常检测的准确性和可靠性。

**技术框架**：HetNet框架主要包括三个模块：协作蒸馏异构教师网络、局部-全局特征融合模块和局部多元高斯噪声生成模块。该框架通过整合不同层次的特征信息，提升模型对复杂模式的学习能力。

**关键创新**：HetNet的主要创新在于其协作蒸馏机制和噪声生成模块的结合，使得模型能够在有限的局部信息下有效学习正常模式的复杂特征分布，这在现有方法中尚属首次。

**关键设计**：在网络结构上，HetNet采用了多层次特征提取和融合策略，损失函数设计上则结合了蒸馏损失和重构损失，以优化模型的学习效果。

## 📊 实验亮点

实验结果表明，HetNet在MSC-AD基准测试中提升了约10%的性能，并在其他数据集上取得了最先进的结果，验证了其在复杂工业环境中的鲁棒性和有效性，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括自动化制造、质量控制和工业监测等。通过在生产线中集成HetNet，企业能够实现实时的异常检测，从而提高生产效率和产品质量，降低损失和返工率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Anomaly detection and localization in automated industrial manufacturing can significantly enhance production efficiency and product quality. Existing methods are capable of detecting surface defects in pre-defined or controlled imaging environments. However, accurately detecting workpiece defects in complex and unstructured industrial environments with varying views, poses and illumination remains challenging. We propose a novel anomaly detection and localization method specifically designed to handle inputs with perturbative patterns. Our approach introduces a new framework based on a collaborative distillation heterogeneous teacher network (HetNet), an adaptive local-global feature fusion module, and a local multivariate Gaussian noise generation module. HetNet can learn to model the complex feature distribution of normal patterns using limited information about local disruptive changes. We conducted extensive experiments on mainstream benchmarks. HetNet demonstrates superior performance with approximately 10% improvement across all evaluation metrics on MSC-AD under industrial conditions, while achieving state-of-the-art results on other datasets, validating its resilience to environmental fluctuations and its capability to enhance the reliability of industrial anomaly detection systems across diverse scenarios. Tests in real-world environments further confirm that HetNet can be effectively integrated into production lines to achieve robust and real-time anomaly detection. Codes, images and videos are published on the project website at: https://zihuatanejoyu.github.io/HetNet/

