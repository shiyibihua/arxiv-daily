---
layout: default
title: SMGeo: Cross-View Object Geo-Localization with Grid-Level Mixture-of-Experts
---

# SMGeo: Cross-View Object Geo-Localization with Grid-Level Mixture-of-Experts

**arXiv**: [2511.14093v1](https://arxiv.org/abs/2511.14093) | [PDF](https://arxiv.org/pdf/2511.14093.pdf)

**作者**: Fan Zhang, Haoyuan Ren, Fei Ma, Qiang Yin, Yongsheng Zhou

**分类**: cs.CV

**发布日期**: 2025-11-18

---

## 💡 一句话要点

**SMGeo：提出基于网格级混合专家模型的跨视角目标地理定位方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `跨视角定位` `地理定位` `Transformer` `混合专家模型` `无人机图像` `卫星图像` `无锚框检测` `目标检测`

## 📋 核心要点

1. 传统跨视角目标地理定位方法易累积误差，难以应对视角和尺度差异以及复杂背景干扰。
2. SMGeo采用端到端Transformer架构，引入网格级稀疏混合专家模块，自适应学习跨视角依赖关系。
3. 实验结果表明，SMGeo在精度上显著优于现有方法，并在消融实验中验证了各模块的有效性。

## 📝 摘要（中文）

本文提出了一种名为SMGeo的、基于Transformer的端到端模型，用于解决跨视角目标地理定位问题，即基于无人机图像精确地定位大规模卫星图像中的同一目标。针对视角和尺度差异大、背景干扰复杂等问题，SMGeo采用可提示的架构，支持点击提示并能实时输出目标地理定位结果。该模型使用Swin-Transformer联合编码无人机和卫星图像特征，并使用无锚框Transformer检测头进行坐标回归。为了更好地捕获模态间和视角内依赖关系，引入了网格级稀疏混合专家(GMoE)模块，自适应地激活特定专家。无锚框检测头通过热图监督直接预测目标位置，避免了锚框带来的尺度偏差和匹配复杂度。在无人机到卫星的定位任务中，SMGeo在IoU=0.25和mIoU指标上取得了领先的性能，显著优于DetGeo等方法。消融实验表明，共享编码、查询引导融合和网格级稀疏混合专家模块均有互补增益。

## 🔬 方法详解

**问题定义**：跨视角目标地理定位旨在根据无人机图像精确地定位大规模卫星图像中的同一目标。现有方法通常采用多阶段“检索-匹配”流程，容易产生累积误差，并且难以有效处理视角、尺度差异以及复杂背景干扰带来的挑战。

**核心思路**：SMGeo的核心思路是构建一个端到端的、可提示的Transformer模型，通过联合编码无人机和卫星图像特征，并引入网格级稀疏混合专家模块，自适应地学习跨视角依赖关系，从而实现精确的目标地理定位。采用无锚框检测头直接回归坐标，避免了锚框带来的偏差。

**技术框架**：SMGeo的整体架构包括：1) Swin-Transformer联合特征编码器，用于提取无人机和卫星图像的特征；2) 网格级稀疏混合专家(GMoE)模块，用于增强跨视角特征融合；3) 无锚框Transformer检测头，用于坐标回归，直接预测目标位置。模型支持点击提示，允许交互式使用。

**关键创新**：SMGeo的关键创新在于：1) 提出了网格级稀疏混合专家(GMoE)模块，能够根据网格的内容、尺度和来源自适应地激活特定专家，从而更好地捕获模态间和视角内的依赖关系；2) 采用了无锚框检测头，避免了传统锚框检测方法中存在的尺度偏差和匹配复杂度。

**关键设计**：GMoE模块的关键设计包括：将图像划分为网格，每个网格对应一组专家；使用稀疏门控机制，根据网格特征选择激活的专家；采用混合专家的方式，融合不同专家的输出。无锚框检测头通过热图监督直接预测目标位置，损失函数包括热图损失和坐标回归损失。

## 📊 实验亮点

SMGeo在无人机到卫星的定位任务中取得了显著的性能提升。在测试集上，SMGeo在IoU=0.25、mIoU等指标上分别达到了87.51%、62.50%和61.45%，显著优于DetGeo等代表性方法（61.97%、57.66%和54.05%）。消融实验表明，共享编码、查询引导融合和网格级稀疏混合专家模块均对性能提升有贡献。

## 🎯 应用场景

SMGeo在智慧城市、灾害监测、环境监测、军事侦察等领域具有广泛的应用前景。例如，在灾害发生后，可以利用无人机图像快速定位受灾区域，并与卫星图像进行比对，评估灾情。在城市规划中，可以利用无人机图像更新城市地图，并与卫星图像进行配准，实现高精度的地理定位。

## 📄 摘要（原文）

> Cross-view object Geo-localization aims to precisely pinpoint the same object across large-scale satellite imagery based on drone images. Due to significant differences in viewpoint and scale, coupled with complex background interference, traditional multi-stage "retrieval-matching" pipelines are prone to cumulative errors. To address this, we present SMGeo, a promptable end-to-end transformer-based model for object Geo-localization. This model supports click prompting and can output object Geo-localization in real time when prompted to allow for interactive use. The model employs a fully transformer-based architecture, utilizing a Swin-Transformer for joint feature encoding of both drone and satellite imagery and an anchor-free transformer detection head for coordinate regression. In order to better capture both inter-modal and intra-view dependencies, we introduce a grid-level sparse Mixture-of-Experts (GMoE) into the cross-view encoder, allowing it to adaptively activate specialized experts according to the content, scale and source of each grid. We also employ an anchor-free detection head for coordinate regression, directly predicting object locations via heat-map supervision in the reference images. This approach avoids scale bias and matching complexity introduced by predefined anchor boxes. On the drone-to-satellite task, SMGeo achieves leading performance in accuracy at IoU=0.25 and mIoU metrics (e.g., 87.51%, 62.50%, and 61.45% in the test set, respectively), significantly outperforming representative methods such as DetGeo (61.97%, 57.66%, and 54.05%, respectively). Ablation studies demonstrate complementary gains from shared encoding, query-guided fusion, and grid-level sparse mixture-of-experts.

