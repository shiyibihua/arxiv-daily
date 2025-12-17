---
layout: default
title: StreamSTGS: Streaming Spatial and Temporal Gaussian Grids for Real-Time Free-Viewpoint Video
---

# StreamSTGS: Streaming Spatial and Temporal Gaussian Grids for Real-Time Free-Viewpoint Video

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.06046" target="_blank" class="toolbar-btn">arXiv: 2511.06046v1</a>
    <a href="https://arxiv.org/pdf/2511.06046.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06046v1" 
            onclick="toggleFavorite(this, '2511.06046v1', 'StreamSTGS: Streaming Spatial and Temporal Gaussian Grids for Real-Time Free-Viewpoint Video')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhihui Ke, Yuyang Liu, Xiaobo Zhou, Tie Qiu

**分类**: cs.CV

**发布日期**: 2025-11-08

**备注**: Accepted by AAAI 2026. Code will be released at https://www.github.com/kkkzh/StreamSTGS

**🔗 代码/项目**: [GITHUB](https://github.com/kkkzh/StreamSTGS)

---

## 💡 一句话要点

**提出StreamSTGS，用于实时自由视点视频的流式传输，兼顾性能与效率。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `自由视点视频` `3D高斯溅射` `实时渲染` `流式传输` `视频压缩` `变形场` `Transformer`

## 📋 核心要点

1. 现有基于3DGS的自由视点视频方法虽然渲染效果好，但存储需求高，难以实现实时流式传输。
2. StreamSTGS使用规范3D高斯、时间特征和变形场表示动态场景，并对高斯属性和时间特征进行高效编码。
3. 实验表明，StreamSTGS在保证性能的同时，显著降低了帧大小，并支持自适应码率控制。

## 📝 摘要（中文）

实时流式自由视点视频（FVV）在训练、渲染和传输效率方面面临巨大挑战。受益于3D高斯溅射（3DGS）的卓越性能，最近基于3DGS的FVV方法在训练和渲染方面取得了显著突破。然而，这些方法的存储需求高达每帧10MB，使得实时流式FVV成为不可能。为了解决这个问题，我们提出了一种新颖的FVV表示，称为StreamSTGS，专为实时流式传输而设计。StreamSTGS使用规范3D高斯、时间特征和变形场来表示动态场景。为了实现高压缩效率，我们将规范高斯属性编码为2D图像，并将时间特征编码为视频。这种设计不仅支持实时流式传输，而且还固有地支持基于网络状况的自适应比特率控制，而无需任何额外的训练。此外，我们提出了一种滑动窗口方案来聚合相邻的时间特征以学习局部运动，然后引入一个Transformer引导的辅助训练模块来学习全局运动。在不同的FVV基准测试中，与最先进的方法相比，StreamSTGS在所有指标上都表现出具有竞争力的性能。值得注意的是，StreamSTGS将PSNR平均提高了1dB，同时将平均帧大小降低到仅170KB。

## 🔬 方法详解

**问题定义**：论文旨在解决实时自由视点视频流式传输中，现有基于3DGS的方法存储需求过高的问题。这些方法虽然渲染质量高，但每帧需要高达10MB的存储空间，严重限制了其在实时流式传输场景中的应用。

**核心思路**：论文的核心思路是通过将3D高斯属性编码为2D图像，时间特征编码为视频，从而实现对自由视点视频数据的高效压缩。同时，利用滑动窗口和Transformer学习局部和全局运动信息，以保持渲染质量。这种设计使得视频数据能够以更小的体积进行传输，从而支持实时流式传输。

**技术框架**：StreamSTGS的整体框架包括以下几个主要模块：1) 规范3D高斯表示：使用规范的3D高斯来表示场景的几何和外观信息。2) 时间特征编码：将时间特征编码为视频，以捕捉场景的动态变化。3) 变形场：使用变形场来描述高斯随时间的运动。4) 滑动窗口：使用滑动窗口来聚合相邻的时间特征，以学习局部运动。5) Transformer引导的辅助训练模块：使用Transformer来学习全局运动。

**关键创新**：该论文的关键创新在于将3D高斯属性和时间特征分别编码为2D图像和视频，从而实现了对自由视点视频数据的高效压缩。与现有方法相比，StreamSTGS能够在保证渲染质量的同时，显著降低帧大小，从而支持实时流式传输。此外，StreamSTGS还支持基于网络状况的自适应比特率控制，而无需额外的训练。

**关键设计**：论文中关键的设计包括：1) 使用滑动窗口来聚合相邻的时间特征，以学习局部运动。滑动窗口的大小和步长需要根据具体的场景和应用进行调整。2) 使用Transformer来学习全局运动。Transformer的结构和参数需要根据具体的场景和应用进行调整。3) 使用合适的损失函数来训练模型。损失函数需要能够平衡渲染质量和压缩效率。

## 📊 实验亮点

实验结果表明，StreamSTGS在多个FVV基准测试中取得了与最先进方法相当的性能。更重要的是，StreamSTGS能够将平均帧大小降低到仅170KB，同时将PSNR平均提高了1dB。这表明StreamSTGS在保证渲染质量的同时，显著提高了压缩效率，为实时自由视点视频流式传输提供了可行的解决方案。

## 🎯 应用场景

StreamSTGS在实时自由视点视频流式传输领域具有广泛的应用前景，例如VR/AR直播、远程协作、游戏直播等。该技术能够显著降低视频传输的带宽需求，提高用户体验，并为相关应用带来新的可能性。未来，该技术有望应用于更多需要实时渲染和传输的场景。

## 📄 摘要（原文）

> Streaming free-viewpoint video~(FVV) in real-time still faces significant challenges, particularly in training, rendering, and transmission efficiency. Harnessing superior performance of 3D Gaussian Splatting~(3DGS), recent 3DGS-based FVV methods have achieved notable breakthroughs in both training and rendering. However, the storage requirements of these methods can reach up to $10$MB per frame, making stream FVV in real-time impossible. To address this problem, we propose a novel FVV representation, dubbed StreamSTGS, designed for real-time streaming. StreamSTGS represents a dynamic scene using canonical 3D Gaussians, temporal features, and a deformation field. For high compression efficiency, we encode canonical Gaussian attributes as 2D images and temporal features as a video. This design not only enables real-time streaming, but also inherently supports adaptive bitrate control based on network condition without any extra training. Moreover, we propose a sliding window scheme to aggregate adjacent temporal features to learn local motions, and then introduce a transformer-guided auxiliary training module to learn global motions. On diverse FVV benchmarks, StreamSTGS demonstrates competitive performance on all metrics compared to state-of-the-art methods. Notably, StreamSTGS increases the PSNR by an average of $1$dB while reducing the average frame size to just $170$KB. The code is publicly available on https://github.com/kkkzh/StreamSTGS.

