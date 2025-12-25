---
layout: default
title: "AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences"
---

# AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20943" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20943v1</a>
  <a href="https://arxiv.org/pdf/2512.20943.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20943v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20943v1', 'AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhe Wang, Jinghang Li, Yifei Zhu

**分类**: cs.GR, cs.DC, cs.LG, cs.MM, cs.NI, eess.IV

**发布日期**: 2025-12-24

**备注**: This paper is accepted by IEEE International Conference on Computer Communications (INFOCOM), 2026

---

## 💡 一句话要点

**AirGS：面向自由视点视频的实时4D高斯流传输框架**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `自由视点视频` `4D高斯溅射` `流传输` `实时渲染` `带宽优化`

## 📋 核心要点

1. 现有4DGS方法在长序列中存在质量下降问题，且带宽和存储开销大，限制了其在实时和大规模部署中的应用。
2. AirGS通过重构训练和传输流程，将高斯视频流转换为多通道2D格式，并结合关键帧选择、时间一致性和膨胀损失等技术，优化了4DGS的流传输。
3. 实验结果表明，AirGS在质量、训练速度和传输大小方面均优于现有方法，尤其是在场景变化时能显著降低质量偏差。

## 📝 摘要（中文）

本文提出AirGS，一个流传输优化的4D高斯溅射（4DGS）框架，旨在实现高质量、低延迟的自由视点视频（FVV）体验。AirGS将高斯视频流转换为多通道2D格式，并智能地识别关键帧以增强帧重建质量。它结合了时间一致性和膨胀损失，以减少训练时间和表示大小。为了支持通信高效的传输，AirGS将4DGS传输建模为一个整数线性规划问题，并设计了一种轻量级的剪枝级别选择算法，自适应地剪枝待传输的高斯更新，从而平衡重建质量和带宽消耗。实验表明，AirGS在场景变化时，PSNR的质量偏差降低了20%以上，帧级别PSNR始终保持在30以上，训练速度提高了6倍，并且与SOTA 4DGS方法相比，每帧传输大小减少了近50%。

## 🔬 方法详解

**问题定义**：现有4D高斯溅射（4DGS）方法在处理长时间序列的自由视点视频时，面临着两个主要问题：一是随着时间推移，重建质量会逐渐下降；二是需要大量的带宽和存储空间，这使得它们难以应用于实时和大规模的部署场景。这些问题限制了自由视点视频技术的广泛应用。

**核心思路**：AirGS的核心思路是通过优化4DGS的训练和传输流程，使其更适合流传输。具体来说，它通过将高斯视频流转换为多通道2D格式，并智能地选择关键帧来提高重建质量。同时，利用时间一致性和膨胀损失来减少训练时间和表示大小。在传输方面，AirGS将4DGS的传输建模为一个整数线性规划问题，并设计了一种轻量级的剪枝算法，以平衡重建质量和带宽消耗。

**技术框架**：AirGS的整体框架包含以下几个主要模块：1) **数据转换模块**：将4D高斯视频流转换为多通道2D格式，以便更有效地进行处理和传输。2) **关键帧选择模块**：智能地选择关键帧，以提高帧重建质量。3) **训练优化模块**：利用时间一致性和膨胀损失来减少训练时间和表示大小。4) **传输优化模块**：将4DGS传输建模为一个整数线性规划问题，并设计轻量级的剪枝算法。

**关键创新**：AirGS的关键创新在于其针对流传输场景的优化策略。与传统的4DGS方法相比，AirGS更加注重在有限带宽下实现高质量的自由视点视频体验。它通过数据转换、关键帧选择、训练优化和传输优化等多种手段，实现了在质量、训练速度和传输大小方面的显著提升。

**关键设计**：AirGS的关键设计包括：1) **多通道2D格式**：将高斯视频流转换为多通道2D格式，以便更有效地进行处理和传输。具体实现方式未知。2) **关键帧选择算法**：智能地选择关键帧，以提高帧重建质量。具体算法细节未知。3) **膨胀损失**：用于减少训练时间和表示大小。具体公式和实现方式未知。4) **整数线性规划模型**：用于优化4DGS传输，平衡重建质量和带宽消耗。具体模型参数和约束条件未知。5) **轻量级剪枝算法**：自适应地剪枝待传输的高斯更新，以减少传输大小。具体算法细节未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20943v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20943v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20943v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，AirGS在多个方面均优于现有方法。在场景变化时，AirGS的PSNR质量偏差降低了20%以上，帧级别PSNR始终保持在30以上。此外，AirGS的训练速度提高了6倍，每帧传输大小减少了近50%。这些数据表明，AirGS在质量、效率和带宽利用率方面均具有显著优势。

## 🎯 应用场景

AirGS具有广泛的应用前景，包括沉浸式远程呈现、虚拟现实/增强现实(VR/AR)游戏、在线教育、数字孪生等领域。它能够提供高质量、低延迟的自由视点视频体验，使用户能够从任意角度观看场景，从而增强沉浸感和交互性。AirGS的优化策略使其更适合在带宽受限的环境中使用，为大规模部署自由视点视频技术提供了可能。

## 📄 摘要（原文）

> Free-viewpoint video (FVV) enables immersive viewing experiences by allowing users to view scenes from arbitrary perspectives. As a prominent reconstruction technique for FVV generation, 4D Gaussian Splatting (4DGS) models dynamic scenes with time-varying 3D Gaussian ellipsoids and achieves high-quality rendering via fast rasterization. However, existing 4DGS approaches suffer from quality degradation over long sequences and impose substantial bandwidth and storage overhead, limiting their applicability in real-time and wide-scale deployments. Therefore, we present AirGS, a streaming-optimized 4DGS framework that rearchitects the training and delivery pipeline to enable high-quality, low-latency FVV experiences. AirGS converts Gaussian video streams into multi-channel 2D formats and intelligently identifies keyframes to enhance frame reconstruction quality. It further combines temporal coherence with inflation loss to reduce training time and representation size. To support communication-efficient transmission, AirGS models 4DGS delivery as an integer linear programming problem and design a lightweight pruning level selection algorithm to adaptively prune the Gaussian updates to be transmitted, balancing reconstruction quality and bandwidth consumption. Extensive experiments demonstrate that AirGS reduces quality deviation in PSNR by more than 20% when scene changes, maintains frame-level PSNR consistently above 30, accelerates training by 6 times, reduces per-frame transmission size by nearly 50% compared to the SOTA 4DGS approaches.

