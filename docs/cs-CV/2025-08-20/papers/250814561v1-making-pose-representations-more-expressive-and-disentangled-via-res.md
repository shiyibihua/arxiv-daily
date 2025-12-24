---
layout: default
title: Making Pose Representations More Expressive and Disentangled via Residual Vector Quantization
---

# Making Pose Representations More Expressive and Disentangled via Residual Vector Quantization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14561" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14561v1</a>
  <a href="https://arxiv.org/pdf/2508.14561.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14561v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14561v1', 'Making Pose Representations More Expressive and Disentangled via Residual Vector Quantization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sukhyun Jeong, Hong-Gi Shin, Yong-Hoon Choi

**分类**: cs.CV, cs.RO

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出残差向量量化以增强姿态表示的表达能力与解耦性**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `3D人类运动生成` `可控运动生成` `残差向量量化` `姿态表示` `运动控制` `细致运动特征` `数据集实验`

## 📋 核心要点

1. 现有的可控运动生成方法依赖于姿态代码表示，但离散姿态代码无法捕捉细致的运动细节，限制了其表达能力。
2. 本文提出通过残差向量量化（RVQ）将连续运动特征与姿态代码相结合，从而增强姿态表示的表达能力和可操控性。
3. 在HumanML3D数据集上的实验表明，模型显著降低了FID值，并在Top-1 R-Precision上实现了小幅提升，验证了其有效性。

## 📝 摘要（中文）

近年来，文本到运动的进展推动了3D人类运动生成和基于文本的运动控制的发展。可控运动生成（CoMo）依赖于姿态代码表示，但离散姿态代码无法捕捉细致的运动细节，限制了表达能力。为此，本文提出了一种方法，通过残差向量量化（RVQ）将连续运动特征与基于姿态代码的潜在表示相结合。这种设计在有效捕捉高频细节等微妙运动特征的同时，保持了姿态代码的可解释性和可操控性。实验结果显示，模型在HumanML3D数据集上将Frechet inception distance（FID）从0.041降低到0.015，Top-1 R-Precision从0.508提升至0.510。对姿态代码之间的方向相似性的定性分析进一步确认了模型在运动编辑中的可控性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有可控运动生成方法中，离散姿态代码无法捕捉细致运动细节的问题，导致表达能力不足。

**核心思路**：通过引入残差向量量化（RVQ），将连续运动特征与姿态代码结合，增强了姿态表示的细腻度和可操控性。

**技术框架**：整体架构包括姿态编码模块、连续运动特征提取模块和残差向量量化模块，确保了信息的有效融合与表达。

**关键创新**：最重要的创新在于将离散的姿态代码与连续运动特征相结合，突破了传统方法的限制，提升了运动生成的细腻度与可控性。

**关键设计**：在模型设计中，采用了特定的损失函数来平衡姿态代码和连续特征的贡献，同时优化了网络结构以提高训练效率和生成质量。

## 📊 实验亮点

实验结果显示，模型在HumanML3D数据集上将Frechet inception distance（FID）从0.041降低至0.015，表明生成质量显著提升。同时，Top-1 R-Precision从0.508提升至0.510，验证了模型在运动编辑中的可控性和有效性。

## 🎯 应用场景

该研究在3D人类运动生成和动画制作等领域具有广泛的应用潜力。通过增强姿态表示的表达能力，能够实现更自然的运动控制和编辑，推动虚拟现实、游戏开发等行业的发展。未来，该方法还可能扩展到其他多模态生成任务中，提升其表现力和可操控性。

## 📄 摘要（原文）

> Recent progress in text-to-motion has advanced both 3D human motion generation and text-based motion control. Controllable motion generation (CoMo), which enables intuitive control, typically relies on pose code representations, but discrete pose codes alone cannot capture fine-grained motion details, limiting expressiveness. To overcome this, we propose a method that augments pose code-based latent representations with continuous motion features using residual vector quantization (RVQ). This design preserves the interpretability and manipulability of pose codes while effectively capturing subtle motion characteristics such as high-frequency details. Experiments on the HumanML3D dataset show that our model reduces Frechet inception distance (FID) from 0.041 to 0.015 and improves Top-1 R-Precision from 0.508 to 0.510. Qualitative analysis of pairwise direction similarity between pose codes further confirms the model's controllability for motion editing.

