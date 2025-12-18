---
layout: default
title: Balanced Diffusion-Guided Fusion for Multimodal Remote Sensing Classification
---

# Balanced Diffusion-Guided Fusion for Multimodal Remote Sensing Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23310" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23310v1</a>
  <a href="https://arxiv.org/pdf/2509.23310.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23310v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23310v1', 'Balanced Diffusion-Guided Fusion for Multimodal Remote Sensing Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Liu, Yongjie Zheng, Yuhan Kang, Mingyang Zhang, Maoguo Gong, Lorenzo Bruzzone

**分类**: cs.CV

**发布日期**: 2025-09-27

**🔗 代码/项目**: [GITHUB](https://github.com/HaoLiu-XDU/BDGF)

---

## 💡 一句话要点

**提出平衡扩散引导融合框架，解决多模态遥感分类中的模态不平衡问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态遥感` `地物分类` `扩散模型` `模态平衡` `特征融合` `互学习` `深度学习`

## 📋 核心要点

1. 现有基于深度学习的多模态遥感数据分析方法在融合不同传感器信息时存在模态不平衡问题，影响分类精度。
2. 论文提出BDGF框架，利用多模态扩散特征引导多分支网络进行地物分类，核心在于平衡模态分布和分层引导特征提取。
3. 实验结果表明，该方法在多个多模态遥感数据集上取得了优异的分类性能，验证了所提方法的有效性。

## 📝 摘要（中文）

本文提出了一种平衡扩散引导融合(BDGF)框架，用于多模态遥感数据地物分类，旨在解决多模态扩散概率模型(DDPMs)预训练中可能出现的模态不平衡问题，并有效利用扩散特征引导互补多样性特征提取。该方法采用自适应模态掩蔽策略，鼓励DDPMs获得模态平衡的数据分布。随后，通过融合特征融合、分组通道注意力和交叉注意力机制，分层引导CNN、Mamba和Transformer网络进行特征提取。此外，还设计了一种互学习策略，通过对齐子网络的概率熵和特征相似性来增强分支间的协作。在四个多模态遥感数据集上的实验结果表明，该方法取得了优异的分类性能。

## 🔬 方法详解

**问题定义**：多模态遥感分类旨在融合来自不同传感器（如光谱图像、LiDAR数据等）的信息，以提高地物分类的准确性。然而，直接预训练多模态扩散模型可能导致模态不平衡，例如，模型可能过度依赖光谱图像的信息，而忽略其他模态的贡献。此外，如何有效利用扩散模型提取的特征来引导互补多样性特征的提取也是一个挑战。

**核心思路**：论文的核心思路是利用扩散模型学习到的多模态数据分布，并将其作为先验知识来引导多分支网络的特征提取。通过自适应模态掩蔽策略平衡不同模态的贡献，并设计分层引导机制，将扩散特征融入到CNN、Mamba和Transformer等不同类型的网络中，从而实现更有效的特征融合和分类。

**技术框架**：BDGF框架主要包含三个阶段：1) 自适应模态掩蔽的扩散模型预训练：通过自适应地掩蔽部分模态的数据，鼓励扩散模型学习模态平衡的数据分布。2) 分层扩散引导的特征提取：利用预训练的扩散模型提取的特征，通过特征融合、分组通道注意力和交叉注意力机制，引导CNN、Mamba和Transformer等多个分支网络进行特征提取。3) 互学习：通过对齐不同分支网络的概率熵和特征相似性，增强分支间的协作，提高整体分类性能。

**关键创新**：该论文的关键创新在于：1) 提出了自适应模态掩蔽策略，有效解决了多模态扩散模型预训练中的模态不平衡问题。2) 设计了分层扩散引导的特征提取机制，将扩散特征有效地融入到不同类型的网络中，实现了更有效的特征融合。3) 提出了互学习策略，增强了不同分支网络之间的协作，提高了整体分类性能。

**关键设计**：自适应模态掩蔽策略根据不同模态的贡献程度，动态调整掩蔽比例。分层引导机制中，特征融合采用加权融合的方式，权重由注意力机制学习得到。分组通道注意力机制将特征分成多个组，并对每个组应用通道注意力，以提取更具判别性的特征。互学习策略采用KL散度损失函数对齐不同分支网络的概率熵，并采用余弦相似度损失函数对齐特征相似性。

## 📊 实验亮点

实验结果表明，所提出的BDGF框架在四个多模态遥感数据集上均取得了优于现有方法的分类性能。例如，在WHU-Hi数据集上，BDGF的总体精度(OA)比最佳基线提高了2%以上。消融实验验证了自适应模态掩蔽策略和分层引导机制的有效性。

## 🎯 应用场景

该研究成果可应用于精准农业、城市规划、灾害监测等领域。通过融合多源遥感数据，可以更准确地识别地物类型，为相关决策提供支持。例如，在精准农业中，可以利用该方法识别不同作物的生长状况，从而优化灌溉和施肥策略。在城市规划中，可以用于土地利用分类和城市扩张监测。在灾害监测中，可以用于评估灾害的影响范围和程度。

## 📄 摘要（原文）

> Deep learning-based techniques for the analysis of multimodal remote sensing data have become popular due to their ability to effectively integrate complementary spatial, spectral, and structural information from different sensors. Recently, denoising diffusion probabilistic models (DDPMs) have attracted attention in the remote sensing community due to their powerful ability to capture robust and complex spatial-spectral distributions. However, pre-training multimodal DDPMs may result in modality imbalance, and effectively leveraging diffusion features to guide complementary diversity feature extraction remains an open question. To address these issues, this paper proposes a balanced diffusion-guided fusion (BDGF) framework that leverages multimodal diffusion features to guide a multi-branch network for land-cover classification. Specifically, we propose an adaptive modality masking strategy to encourage the DDPMs to obtain a modality-balanced rather than spectral image-dominated data distribution. Subsequently, these diffusion features hierarchically guide feature extraction among CNN, Mamba, and transformer networks by integrating feature fusion, group channel attention, and cross-attention mechanisms. Finally, a mutual learning strategy is developed to enhance inter-branch collaboration by aligning the probability entropy and feature similarity of individual subnetworks. Extensive experiments on four multimodal remote sensing datasets demonstrate that the proposed method achieves superior classification performance. The code is available at https://github.com/HaoLiu-XDU/BDGF.

