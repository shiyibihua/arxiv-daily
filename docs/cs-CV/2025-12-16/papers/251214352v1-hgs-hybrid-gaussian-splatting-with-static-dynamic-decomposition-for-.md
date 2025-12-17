---
layout: default
title: HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis
---

# HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.14352" target="_blank" class="toolbar-btn">arXiv: 2512.14352v1</a>
    <a href="https://arxiv.org/pdf/2512.14352.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14352v1" 
            onclick="toggleFavorite(this, '2512.14352v1', 'HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu

**分类**: cs.CV, cs.CG

**发布日期**: 2025-12-16

**备注**: 11 pages, 9 figures

---

## 💡 一句话要点

**提出HGS混合高斯溅射方法，通过静态-动态解耦实现紧凑的动态场景新视角合成。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `动态场景新视角合成` `高斯溅射` `静态-动态解耦` `径向基函数` `实时渲染`

## 📋 核心要点

1. 现有动态新视角合成方法模型复杂、参数冗余，导致模型体积大、渲染速度慢，难以在资源受限设备上实时应用。
2. HGS通过静态-动态解耦策略，利用径向基函数建模高斯基元，对动态区域使用时变RBF，静态区域共享时不变参数，减少冗余。
3. 实验表明，HGS模型大小减少高达98%，在RTX 3090上以4K分辨率实现高达125 FPS的实时渲染，并提升了视觉保真度。

## 📝 摘要（中文）

动态新视角合成（NVS）对于创造沉浸式体验至关重要。现有方法通过引入带有隐式形变场或无差别地分配时变参数的3D高斯溅射（3DGS）来推进动态NVS，超越了基于NeRF的方法。然而，由于过度的模型复杂性和参数冗余，它们导致模型体积庞大和渲染速度缓慢，使得它们在实时应用中效率低下，尤其是在资源受限的设备上。为了获得一个更高效且参数冗余更少的模型，本文提出混合高斯溅射（HGS），这是一个紧凑而高效的框架，专门设计用于在统一表示中解耦场景的静态和动态区域。HGS的核心创新在于我们的静态-动态分解（SDD）策略，该策略利用径向基函数（RBF）建模高斯基元。具体而言，对于动态区域，我们采用时间相关的RBF来有效地捕获时间变化并处理突发的场景变化，而对于静态区域，我们通过共享时间不变参数来减少冗余。此外，我们引入了一种为显式模型量身定制的两阶段训练策略，以增强静态-动态边界处的时间一致性。实验结果表明，我们的方法可将模型大小减少高达98%，并在单个RTX 3090 GPU上以4K分辨率实现高达125 FPS的实时渲染。它还在RTX 3050上以1352 * 1014的分辨率维持160 FPS，并且已集成到VR系统中。此外，HGS在实现与最先进方法相当的渲染质量的同时，为高频细节和突发场景变化提供了显着改善的视觉保真度。

## 🔬 方法详解

**问题定义**：论文旨在解决动态场景新视角合成中，现有基于3D高斯溅射的方法模型体积大、渲染速度慢的问题。现有方法通常采用隐式形变场或直接为每个高斯基元分配时变参数，导致参数冗余，难以在资源受限设备上实现实时渲染。

**核心思路**：论文的核心思路是将场景分解为静态和动态区域，并分别采用不同的参数化方法。对于动态区域，使用时间相关的径向基函数（RBF）来建模形变；对于静态区域，则共享时间不变的参数，从而减少冗余，降低模型复杂度。

**技术框架**：HGS框架包含以下主要模块：1) 静态-动态分解（SDD）：使用RBF建模高斯基元，区分静态和动态区域。2) 参数化：动态区域使用时变RBF，静态区域共享时不变参数。3) 两阶段训练：第一阶段初始化高斯参数，第二阶段优化RBF参数并增强时间一致性。整体流程是从多视角图像输入，经过SDD和参数化后，进行渲染和优化，最终得到紧凑的动态场景表示。

**关键创新**：最重要的技术创新点是静态-动态分解（SDD）策略。与现有方法对所有高斯基元都使用时变参数不同，HGS根据场景内容将高斯基元分为静态和动态两部分，并分别进行参数化。这种方法能够显著减少参数冗余，降低模型复杂度，提高渲染速度。

**关键设计**：关键设计包括：1) 使用径向基函数（RBF）建模高斯基元，方便进行静态-动态分解。2) 设计了两阶段训练策略，第一阶段初始化高斯参数，第二阶段优化RBF参数并增强时间一致性。3) 在损失函数中，考虑了渲染质量和时间一致性，以保证合成视频的视觉效果和流畅度。

## 📊 实验亮点

HGS方法在多个动态场景数据集上进行了评估，实验结果表明，HGS可以将模型大小减少高达98%，并在单个RTX 3090 GPU上以4K分辨率实现高达125 FPS的实时渲染。此外，HGS在RTX 3050上也能达到160 FPS。在视觉质量方面，HGS与最先进的方法相比具有可比性，并且在高频细节和突发场景变化方面表现更佳。

## 🎯 应用场景

HGS方法可应用于虚拟现实（VR）、增强现实（AR）、游戏、机器人等领域。该方法能够以更小的模型体积和更快的渲染速度，实现高质量的动态场景新视角合成，为用户提供更具沉浸感和交互性的体验。未来，该方法有望在移动设备和嵌入式系统上得到广泛应用。

## 📄 摘要（原文）

> Dynamic novel view synthesis (NVS) is essential for creating immersive experiences. Existing approaches have advanced dynamic NVS by introducing 3D Gaussian Splatting (3DGS) with implicit deformation fields or indiscriminately assigned time-varying parameters, surpassing NeRF-based methods. However, due to excessive model complexity and parameter redundancy, they incur large model sizes and slow rendering speeds, making them inefficient for real-time applications, particularly on resource-constrained devices. To obtain a more efficient model with fewer redundant parameters, in this paper, we propose Hybrid Gaussian Splatting (HGS), a compact and efficient framework explicitly designed to disentangle static and dynamic regions of a scene within a unified representation. The core innovation of HGS lies in our Static-Dynamic Decomposition (SDD) strategy, which leverages Radial Basis Function (RBF) modeling for Gaussian primitives. Specifically, for dynamic regions, we employ time-dependent RBFs to effectively capture temporal variations and handle abrupt scene changes, while for static regions, we reduce redundancy by sharing temporally invariant parameters. Additionally, we introduce a two-stage training strategy tailored for explicit models to enhance temporal coherence at static-dynamic boundaries. Experimental results demonstrate that our method reduces model size by up to 98% and achieves real-time rendering at up to 125 FPS at 4K resolution on a single RTX 3090 GPU. It further sustains 160 FPS at 1352 * 1014 on an RTX 3050 and has been integrated into the VR system. Moreover, HGS achieves comparable rendering quality to state-of-the-art methods while providing significantly improved visual fidelity for high-frequency details and abrupt scene changes.

