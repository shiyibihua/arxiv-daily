---
layout: default
title: Self-Supervised Sparse Sensor Fusion for Long Range Perception
---

# Self-Supervised Sparse Sensor Fusion for Long Range Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13995" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13995v1</a>
  <a href="https://arxiv.org/pdf/2508.13995.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13995v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13995v1', 'Self-Supervised Sparse Sensor Fusion for Long Range Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Edoardo Palladin, Samuel Brucker, Filippo Ghilotti, Praveen Narayanan, Mario Bijelic, Felix Heide

**分类**: cs.CV

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出自监督稀疏传感器融合以解决长距离感知问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `长距离感知` `自监督学习` `稀疏表示` `多模态融合` `自动驾驶` `激光雷达` `目标检测` `数据预处理`

## 📋 核心要点

1. 现有感知方法主要集中在短距离，无法满足长途高速驾驶的需求，导致安全性和规划能力不足。
2. 本文提出了一种基于稀疏表示的3D编码方法，并结合自监督预训练，能够有效处理多模态数据。
3. 实验结果显示，该方法在目标检测上提升了26.6%的mAP，并在激光雷达预测中减少了30.5%的Chamfer距离，显著提高了感知性能。

## 📝 摘要（中文）

在城市以外，自主驾驶汽车和卡车需要掌握在城际高速公路上的驾驶。安全的长途高速旅行要求至少250米的感知距离，这大约是城市驾驶中通常处理的50-100米的五倍。现有感知方法主要集中在较短的距离，并依赖鸟瞰图（BEV）表示，随着距离的增加，内存和计算成本呈二次增长。为了解决这一限制，本文基于稀疏表示，提出了一种高效的多模态和时间特征的3D编码，以及一种新颖的自监督预训练方案，使得能够从未标记的相机-激光雷达数据中进行大规模学习。该方法将感知距离扩展至250米，在目标检测中实现了26.6%的mAP提升，并在激光雷达预测中减少了30.5%的Chamfer距离，相较于现有方法表现更佳。

## 🔬 方法详解

**问题定义**：本文旨在解决自主驾驶在长距离高速公路上的感知问题。现有方法多集中于短距离感知，无法满足250米以上的感知需求，导致规划和安全性不足。

**核心思路**：论文提出了一种基于稀疏表示的3D编码方法，结合自监督学习，从未标记的相机-激光雷达数据中提取多模态特征，以提高长距离感知能力。

**技术框架**：整体架构包括数据预处理、特征提取、3D编码和自监督学习模块。通过稀疏表示，减少计算和内存开销，同时保持感知精度。

**关键创新**：最重要的创新在于引入自监督预训练方案，使得模型能够在没有标注数据的情况下进行有效学习，突破了传统方法的限制。

**关键设计**：在模型设计中，采用了特定的损失函数以优化多模态特征的融合，并通过稀疏编码技术降低了计算复杂度，提升了模型的实时性和准确性。

## 📊 实验亮点

实验结果表明，所提出的方法在目标检测任务中实现了26.6%的mAP提升，并在激光雷达预测中减少了30.5%的Chamfer距离，相较于现有方法表现出显著的性能改进，成功将感知距离扩展至250米。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车、物流运输和智能交通系统。通过提升长距离感知能力，能够显著提高高速公路行驶的安全性和效率，推动自动驾驶技术的广泛应用。

## 📄 摘要（原文）

> Outside of urban hubs, autonomous cars and trucks have to master driving on intercity highways. Safe, long-distance highway travel at speeds exceeding 100 km/h demands perception distances of at least 250 m, which is about five times the 50-100m typically addressed in city driving, to allow sufficient planning and braking margins. Increasing the perception ranges also allows to extend autonomy from light two-ton passenger vehicles to large-scale forty-ton trucks, which need a longer planning horizon due to their high inertia. However, most existing perception approaches focus on shorter ranges and rely on Bird's Eye View (BEV) representations, which incur quadratic increases in memory and compute costs as distance grows. To overcome this limitation, we built on top of a sparse representation and introduced an efficient 3D encoding of multi-modal and temporal features, along with a novel self-supervised pre-training scheme that enables large-scale learning from unlabeled camera-LiDAR data. Our approach extends perception distances to 250 meters and achieves an 26.6% improvement in mAP in object detection and a decrease of 30.5% in Chamfer Distance in LiDAR forecasting compared to existing methods, reaching distances up to 250 meters. Project Page: https://light.princeton.edu/lrs4fusion/

