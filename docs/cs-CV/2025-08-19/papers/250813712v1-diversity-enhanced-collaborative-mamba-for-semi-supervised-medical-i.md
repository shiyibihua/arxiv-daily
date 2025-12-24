---
layout: default
title: Diversity-enhanced Collaborative Mamba for Semi-supervised Medical Image Segmentation
---

# Diversity-enhanced Collaborative Mamba for Semi-supervised Medical Image Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13712" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13712v1</a>
  <a href="https://arxiv.org/pdf/2508.13712.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13712v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13712v1', 'Diversity-enhanced Collaborative Mamba for Semi-supervised Medical Image Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shumeng Li, Jian Zhang, Lei Qi, Luping Zhou, Yinghuan Shi, Yang Gao

**分类**: cs.CV

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出Diversity-enhanced Collaborative Mamba以解决半监督医学图像分割问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `半监督学习` `医学图像分割` `多样性增强` `对比学习` `状态空间模型`

## 📋 核心要点

1. 现有的医学图像分割方法依赖于大量标注数据，获取过程繁琐且成本高昂，限制了其应用。
2. 本文提出的DCMamba框架通过多样性增强技术，从数据、网络和特征三个方面提升半监督分割的效果。
3. 实验结果显示，DCMamba在Synapse数据集上相较于最新的SSM方法提升了6.69%，验证了其有效性。

## 📝 摘要（中文）

获取高质量的医学图像分割标注数据既繁琐又昂贵。半监督分割技术通过利用未标记数据生成伪标签来减轻这一负担。最近，Mamba等先进的状态空间模型在处理长距离依赖方面表现出色。本文提出了一种新颖的Diversity-enhanced Collaborative Mamba框架（DCMamba），从数据、网络和特征三个角度探索和利用多样性。我们开发了基于Mamba扫描建模特征的补丁级弱强混合增强；引入了多样化扫描协作模块，以利用不同扫描方向带来的预测差异；采用不确定性加权对比学习机制增强特征表示的多样性。实验结果表明，DCMamba在半监督医学图像分割中显著优于其他方法，在Synapse数据集上以20%标记数据提升了6.69%。

## 🔬 方法详解

**问题定义**：本文旨在解决医学图像分割中对高质量标注数据的依赖问题。现有方法在处理未标记数据时效果有限，导致分割性能不足。

**核心思路**：DCMamba框架通过引入多样性增强技术，利用未标记数据生成伪标签，从而提升分割性能。设计上强调数据、网络和特征的多样性，以更好地捕捉图像特征。

**技术框架**：DCMamba整体架构包括三个主要模块：1) 基于Mamba的补丁级弱强混合增强；2) 多样化扫描协作模块；3) 不确定性加权对比学习机制。各模块协同工作，提升模型的学习能力。

**关键创新**：最重要的创新点在于通过多样性增强技术，尤其是引入不同扫描方向的预测差异，显著提升了模型的分割性能。这一设计与传统方法的单一视角处理形成鲜明对比。

**关键设计**：在参数设置上，采用了适应性增强策略，损失函数设计上结合了对比学习和不确定性加权，网络结构则基于Mamba模型进行优化，确保了模型在处理长距离依赖时的有效性。

## 📊 实验亮点

实验结果表明，DCMamba在Synapse数据集上以20%标记数据的情况下，较最新的SSM方法提升了6.69%的分割性能，显示出其在半监督医学图像分割中的显著优势。

## 🎯 应用场景

该研究在医学图像分割领域具有广泛的应用潜力，尤其是在需要快速处理大量未标记数据的场景中。通过提升半监督学习的效果，DCMamba能够帮助医疗机构更高效地进行图像分析，降低人工标注成本，推动智能医疗的发展。

## 📄 摘要（原文）

> Acquiring high-quality annotated data for medical image segmentation is tedious and costly. Semi-supervised segmentation techniques alleviate this burden by leveraging unlabeled data to generate pseudo labels. Recently, advanced state space models, represented by Mamba, have shown efficient handling of long-range dependencies. This drives us to explore their potential in semi-supervised medical image segmentation. In this paper, we propose a novel Diversity-enhanced Collaborative Mamba framework (namely DCMamba) for semi-supervised medical image segmentation, which explores and utilizes the diversity from data, network, and feature perspectives. Firstly, from the data perspective, we develop patch-level weak-strong mixing augmentation with Mamba's scanning modeling characteristics. Moreover, from the network perspective, we introduce a diverse-scan collaboration module, which could benefit from the prediction discrepancies arising from different scanning directions. Furthermore, from the feature perspective, we adopt an uncertainty-weighted contrastive learning mechanism to enhance the diversity of feature representation. Experiments demonstrate that our DCMamba significantly outperforms other semi-supervised medical image segmentation methods, e.g., yielding the latest SSM-based method by 6.69% on the Synapse dataset with 20% labeled data.

