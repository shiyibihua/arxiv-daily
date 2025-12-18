---
layout: default
title: Aerial Path Planning for Urban Geometry and Texture Co-Capture
---

# Aerial Path Planning for Urban Geometry and Texture Co-Capture

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22227" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22227v1</a>
  <a href="https://arxiv.org/pdf/2509.22227.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22227v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22227v1', 'Aerial Path Planning for Urban Geometry and Texture Co-Capture')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weidan Xiong, Bochuan Zeng, Ziyu Hu, Jianwei Guo, Ke Xie, Hui Huang

**分类**: cs.GR, cs.CV

**发布日期**: 2025-09-26

**备注**: ACM TOG and SIGGRAPH Asia 2025 (Patent Protected); Project page: https://vcc.tech/research/2025/DroneTex

**DOI**: [10.1145/3763292](https://doi.org/10.1145/3763292)

---

## 💡 一句话要点

**提出一种城市几何与纹理协同捕获的无人机路径规划方法**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `无人机路径规划` `城市重建` `纹理捕获` `几何重建` `多目标优化` `三维建模` `视觉质量评估`

## 📋 核心要点

1. 现有城市重建技术往往忽略纹理质量，导致纹理模型存在明显的视觉伪影，需要同时考虑几何与纹理的协同捕获。
2. 提出一种创新的无人机路径规划框架，通过生成垂直倾斜和水平平面视图，协同优化纹理保真度、几何精度和飞行成本。
3. 在合成和真实数据集上验证，该方法能有效生成高质量图像集，用于并发的几何与纹理重建，降低运营成本。

## 📝 摘要（中文）

本文提出了一种在有限先验知识下，针对城市几何与纹理协同捕获问题的无人机路径规划框架。输入仅为目标区域的2D建筑轮廓图和安全飞行高度。该框架旨在生成高质量的垂直倾斜视图和水平平面视图，以有效捕获几何和纹理细节。同时，提出了一个多目标优化策略，联合最大化纹理保真度、提高几何精度并最小化飞行成本。此外，还提出了一种考虑纹理一致性的序列路径规划算法。在合成和真实城市数据集上的大量实验表明，该方法能够有效地生成适用于并发几何和纹理重建的图像集，从而以低运营成本创建逼真的纹理场景代理。

## 🔬 方法详解

**问题定义**：论文旨在解决城市环境中，在有限先验知识下，如何通过无人机航拍图像重建高质量的几何结构和逼真纹理的问题。现有方法通常只关注几何重建，忽略了纹理质量，导致重建模型存在视觉瑕疵。此外，如何在保证几何精度的同时，优化纹理质量和降低航拍成本也是一个挑战。

**核心思路**：论文的核心思路是通过优化无人机的飞行路径，协同捕获高质量的几何和纹理信息。具体而言，通过生成垂直倾斜视图捕获建筑的几何结构，通过水平平面视图捕获建筑的纹理细节。同时，设计多目标优化策略，平衡纹理保真度、几何精度和飞行成本。

**技术框架**：该方法包含以下主要阶段：1) 视图生成：根据2D建筑轮廓图和安全飞行高度，生成垂直倾斜视图和水平平面视图。2) 纹理质量评估：提出一种综合的纹理质量评估系统，包括针对建筑立面的新型指标。3) 多目标优化：设计多目标优化策略，联合最大化纹理保真度、提高几何精度并最小化飞行成本。4) 序列路径规划：提出一种考虑纹理一致性的序列路径规划算法。

**关键创新**：该方法最重要的创新点在于提出了城市几何与纹理的协同捕获框架，并设计了针对建筑立面的纹理质量评估指标。与现有方法相比，该方法能够同时优化几何精度和纹理质量，从而生成更逼真的城市重建模型。此外，多目标优化策略和序列路径规划算法也提高了效率和纹理一致性。

**关键设计**：论文提出了两个针对建筑立面的纹理质量评估指标（具体指标名称未知）。多目标优化策略中，需要定义纹理保真度、几何精度和飞行成本的量化指标，并设计合适的权重系数。序列路径规划算法需要考虑相邻图像之间的纹理一致性，避免出现明显的纹理跳变。

## 📊 实验亮点

该方法在合成和真实城市数据集上进行了验证，实验结果表明，该方法能够有效地生成适用于并发几何和纹理重建的图像集，从而以低运营成本创建逼真的纹理场景代理。具体的性能数据和对比基线未知，但论文强调了该方法在纹理质量和几何精度方面的提升。

## 🎯 应用场景

该研究成果可应用于城市建模、虚拟现实、游戏开发、城市规划、自动驾驶等领域。通过无人机航拍快速生成高质量的城市三维模型，可以为城市管理、旅游推广、灾害评估等提供重要的数据支持。未来，结合深度学习技术，可以进一步提高重建效率和模型质量。

## 📄 摘要（原文）

> Recent advances in image acquisition and scene reconstruction have enabled the generation of high-quality structural urban scene geometry, given sufficient site information. However, current capture techniques often overlook the crucial importance of texture quality, resulting in noticeable visual artifacts in the textured models. In this work, we introduce the urban geometry and texture co-capture problem under limited prior knowledge before a site visit. The only inputs are a 2D building contour map of the target area and a safe flying altitude above the buildings. We propose an innovative aerial path planning framework designed to co-capture images for reconstructing both structured geometry and high-fidelity textures. To evaluate and guide view planning, we introduce a comprehensive texture quality assessment system, including two novel metrics tailored for building facades. Firstly, our method generates high-quality vertical dipping views and horizontal planar views to effectively capture both geometric and textural details. A multi-objective optimization strategy is then proposed to jointly maximize texture fidelity, improve geometric accuracy, and minimize the cost associated with aerial views. Furthermore, we present a sequential path planning algorithm that accounts for texture consistency during image capture. Extensive experiments on large-scale synthetic and real-world urban datasets demonstrate that our approach effectively produces image sets suitable for concurrent geometric and texture reconstruction, enabling the creation of realistic, textured scene proxies at low operational cost.

