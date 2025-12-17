---
layout: default
title: Physically Aware 360$^\circ$ View Generation from a Single Image using Disentangled Scene Embeddings
---

# Physically Aware 360$^\circ$ View Generation from a Single Image using Disentangled Scene Embeddings

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.10293" target="_blank" class="toolbar-btn">arXiv: 2512.10293v1</a>
    <a href="https://arxiv.org/pdf/2512.10293.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10293v1" 
            onclick="toggleFavorite(this, '2512.10293v1', 'Physically Aware 360$^\circ$ View Generation from a Single Image using Disentangled Scene Embeddings')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Karthikeya KV, Narendra Bandaru

**分类**: cs.CV

**发布日期**: 2025-12-11

---

## 💡 一句话要点

**提出Disentangled360，通过解耦场景嵌入实现单图360度视图生成。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `360度视图生成` `单图重建` `解耦表示` `高斯溅射` `体渲染` `医学成像` `机器人感知`

## 📋 核心要点

1. 现有360度视图生成方法在处理各向异性光照和跨场景泛化能力方面存在不足。
2. Disentangled360通过解耦场景嵌入，区分各向同性和各向异性光照，实现更真实的视图合成。
3. 实验表明，Disentangled360在SSIM和LPIPS指标上优于现有方法，且具有交互式应用潜力。

## 📝 摘要（中文）

Disentangled360是一种创新的3D感知技术，它结合了方向解耦的体渲染与单图像360°独特视图合成的优势，适用于医学成像和自然场景重建。与当前过度简化各向异性光照行为或缺乏跨环境泛化能力的技术不同，我们的框架明确区分了高斯溅射骨干网络中的各向同性和各向异性贡献。我们实现了一个双分支条件框架，一个针对体积数据中CT强度驱动的散射进行优化，另一个通过归一化相机嵌入针对真实世界的RGB场景进行优化。为了解决尺度模糊并保持结构真实感，我们提出了一种混合的姿势无关锚定方法，该方法自适应地采样场景深度和材料过渡，作为场景提炼期间的稳定支点。我们的设计将术前放射线模拟和消费级360°渲染集成到单个推理管道中，从而以固有的方向性促进快速、逼真的视图合成。在Mip-NeRF 360、RealEstate10K和DeepDRR数据集上的评估表明，SSIM和LPIPS性能优越，而运行时评估证实了其在交互式应用中的可行性。Disentangled360促进了混合现实医学监督、机器人感知和沉浸式内容创建，无需针对特定场景进行微调或昂贵的光子模拟。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张图像生成高质量、物理上合理的360度全景视图的问题。现有方法要么过度简化光照模型，无法处理复杂的各向异性光照效果，要么缺乏跨不同场景的泛化能力，需要针对特定场景进行微调。此外，尺度模糊和结构真实感也是现有方法面临的挑战。

**核心思路**：论文的核心思路是将场景表示解耦为各向同性和各向异性两部分，分别处理。通过这种解耦，模型可以更好地理解场景的光照特性，从而生成更逼真的视图。此外，论文还引入了一种混合姿势无关锚定方法，以解决尺度模糊和保持结构真实感。

**技术框架**：Disentangled360采用双分支条件框架。一个分支针对体积数据（如CT扫描）进行优化，利用CT强度驱动的散射；另一个分支针对真实世界的RGB场景进行优化，使用归一化相机嵌入。这两个分支共享一个高斯溅射骨干网络，用于场景的体渲染。混合姿势无关锚定方法用于自适应地采样场景深度和材料过渡，作为场景提炼的稳定支点。

**关键创新**：该方法最重要的创新点在于对场景嵌入进行解耦，区分各向同性和各向异性光照。这种解耦使得模型能够更好地理解和模拟复杂的光照效果，从而生成更逼真的视图。此外，混合姿势无关锚定方法也是一个重要的创新，它解决了尺度模糊和保持结构真实感的问题。

**关键设计**：论文使用高斯溅射作为场景表示，并设计了双分支条件框架来处理不同类型的输入数据。损失函数的设计旨在优化视图合成的质量，包括SSIM和LPIPS等指标。混合姿势无关锚定方法的具体实现涉及自适应采样策略和稳定支点的选择。

## 📊 实验亮点

实验结果表明，Disentangled360在Mip-NeRF 360、RealEstate10K和DeepDRR数据集上取得了优异的性能，在SSIM和LPIPS指标上均优于现有方法。此外，运行时评估表明该技术具有交互式应用的潜力，使其在实际应用中更具竞争力。

## 🎯 应用场景

Disentangled360具有广泛的应用前景，包括混合现实医学监督（例如术前放射线模拟）、机器人感知和沉浸式内容创建。该技术无需针对特定场景进行微调或昂贵的光子模拟，降低了应用成本，提高了效率。未来，该技术有望在虚拟现实、增强现实、游戏开发等领域发挥重要作用。

## 📄 摘要（原文）

> We introduce Disentangled360, an innovative 3D-aware technology that integrates the advantages of direction disentangled volume rendering with single-image 360° unique view synthesis for applications in medical imaging and natural scene reconstruction. In contrast to current techniques that either oversimplify anisotropic light behavior or lack generalizability across various contexts, our framework distinctly differentiates between isotropic and anisotropic contributions inside a Gaussian Splatting backbone. We implement a dual-branch conditioning framework, one optimized for CT intensity driven scattering in volumetric data and the other for real-world RGB scenes through normalized camera embeddings. To address scale ambiguity and maintain structural realism, we present a hybrid pose agnostic anchoring method that adaptively samples scene depth and material transitions, functioning as stable pivots during scene distillation. Our design integrates preoperative radiography simulation and consumer-grade 360° rendering into a singular inference pipeline, facilitating rapid, photorealistic view synthesis with inherent directionality. Evaluations on the Mip-NeRF 360, RealEstate10K, and DeepDRR datasets indicate superior SSIM and LPIPS performance, while runtime assessments confirm its viability for interactive applications. Disentangled360 facilitates mixed-reality medical supervision, robotic perception, and immersive content creation, eliminating the necessity for scene-specific finetuning or expensive photon simulations.

