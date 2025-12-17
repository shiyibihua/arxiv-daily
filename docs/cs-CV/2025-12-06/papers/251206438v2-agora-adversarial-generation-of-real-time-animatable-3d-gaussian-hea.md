---
layout: default
title: AGORA: Adversarial Generation Of Real-time Animatable 3D Gaussian Head Avatars
---

# AGORA: Adversarial Generation Of Real-time Animatable 3D Gaussian Head Avatars

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.06438" target="_blank" class="toolbar-btn">arXiv: 2512.06438v2</a>
    <a href="https://arxiv.org/pdf/2512.06438.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06438v2" 
            onclick="toggleFavorite(this, '2512.06438v2', 'AGORA: Adversarial Generation Of Real-time Animatable 3D Gaussian Head Avatars')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ramazan Fazylov, Sergey Zagoruyko, Aleksandr Parkin, Stamatis Lefkimmiatis, Ivan Laptev

**分类**: cs.CV

**发布日期**: 2025-12-06 (更新: 2025-12-10)

**🔗 代码/项目**: [PROJECT_PAGE](https://ramazan793.github.io/AGORA/)

---

## 💡 一句话要点

**AGORA：提出基于对抗生成网络的实时可控3D高斯头部头像**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D人脸头像` `高斯溅射` `生成对抗网络` `实时渲染` `表情控制`

## 📋 核心要点

1. 现有基于NeRF的头像生成方法渲染速度慢，动态效果不佳，而3DGS方法缺乏动态控制能力。
2. AGORA提出了一种基于生成对抗网络的3DGS扩展框架，通过FLAME条件变形分支实现精细的表情控制。
3. 实验表明，AGORA在表情准确性上优于NeRF方法，并在单GPU上实现了250+ FPS的渲染速度，CPU上也能达到9 FPS。

## 📝 摘要（中文）

生成高保真、可动画的3D人体头像仍然是计算机图形学和视觉领域的核心挑战，其应用涵盖VR、远程呈现和娱乐。现有的基于NeRF等隐式表示的方法渲染速度慢且动态不一致，而3D高斯溅射（3DGS）方法通常仅限于静态头部生成，缺乏动态控制。我们通过引入AGORA来弥合这一差距，AGORA是一个新颖的框架，它在生成对抗网络中扩展了3DGS以生成可动画的头像。我们的主要贡献是一个轻量级的、FLAME条件变形分支，它可以预测每个高斯的残差，从而实现保持身份的、细粒度的表情控制，同时允许实时推理。通过利用参数化网格的合成渲染的双鉴别器训练方案来强制执行表情保真度。AGORA生成的头像不仅在视觉上逼真，而且可以精确控制。在定量方面，我们优于最先进的基于NeRF的方法，在单GPU上以250+ FPS的速度渲染，并且值得注意的是，在仅CPU推理下以〜9 FPS的速度渲染——据我们所知，这是首次展示了实用的仅CPU可动画3DGS头像合成。这项工作代表了迈向实用、高性能数字人的重要一步。

## 🔬 方法详解

**问题定义**：论文旨在解决现有3D人脸头像生成方法在渲染速度、动态控制和真实感方面的不足。现有基于NeRF的方法渲染速度慢，难以实时应用，而3DGS方法虽然渲染速度快，但通常只能生成静态头像，缺乏动态表情控制能力。因此，如何生成既能实时渲染又能精确控制表情的高质量3D人脸头像是一个关键问题。

**核心思路**：论文的核心思路是将3D高斯溅射（3DGS）与生成对抗网络（GAN）相结合，利用3DGS的高效渲染能力和GAN的生成能力，同时引入一个轻量级的FLAME条件变形分支来控制表情。通过预测每个高斯残差，实现身份保持和细粒度的表情控制。

**技术框架**：AGORA的整体框架是一个生成对抗网络，其中生成器基于3DGS，并包含一个FLAME条件变形分支。该分支以FLAME参数作为输入，预测每个高斯分布的残差，从而实现表情控制。判别器则用于区分生成的头像和真实头像，提高生成头像的真实感。训练过程中，使用双判别器结构，一个判别器用于判别渲染图像的真实性，另一个判别器用于保证表情的准确性。

**关键创新**：AGORA的关键创新在于将FLAME模型与3DGS相结合，通过一个轻量级的变形分支实现了对3D高斯分布的精确控制。与现有方法相比，AGORA不仅能够生成高质量的3D人脸头像，还能够实现实时的表情控制，并且在CPU上也能达到可用的帧率。

**关键设计**：AGORA的关键设计包括：1) 轻量级的FLAME条件变形分支，该分支采用MLP结构，以FLAME参数作为输入，预测每个高斯分布的残差；2) 双判别器结构，一个判别器用于判别渲染图像的真实性，另一个判别器用于保证表情的准确性；3) 损失函数的设计，包括对抗损失、表情损失和正则化损失，用于保证生成头像的真实感、表情准确性和几何一致性。

## 📊 实验亮点

AGORA在表情准确性方面优于最先进的基于NeRF的方法，同时在单GPU上实现了250+ FPS的渲染速度。更重要的是，AGORA在仅CPU推理下也能达到〜9 FPS的速度，这是首次展示了实用的仅CPU可动画3DGS头像合成。这些结果表明AGORA在实时性和真实感方面都取得了显著的提升。

## 🎯 应用场景

AGORA在VR/AR、远程呈现、游戏和虚拟化身等领域具有广泛的应用前景。它可以用于创建逼真的虚拟形象，实现更自然的远程交流，提升游戏体验，并为用户提供个性化的虚拟化身定制服务。AGORA的实时渲染能力使其能够应用于对延迟敏感的场景，例如实时视频会议和互动娱乐。

## 📄 摘要（原文）

> The generation of high-fidelity, animatable 3D human avatars remains a core challenge in computer graphics and vision, with applications in VR, telepresence, and entertainment. Existing approaches based on implicit representations like NeRFs suffer from slow rendering and dynamic inconsistencies, while 3D Gaussian Splatting (3DGS) methods are typically limited to static head generation, lacking dynamic control. We bridge this gap by introducing AGORA, a novel framework that extends 3DGS within a generative adversarial network to produce animatable avatars. Our key contribution is a lightweight, FLAME-conditioned deformation branch that predicts per-Gaussian residuals, enabling identity-preserving, fine-grained expression control while allowing real-time inference. Expression fidelity is enforced via a dual-discriminator training scheme leveraging synthetic renderings of the parametric mesh. AGORA generates avatars that are not only visually realistic but also precisely controllable. Quantitatively, we outperform state-of-the-art NeRF-based methods on expression accuracy while rendering at 250+ FPS on a single GPU, and, notably, at $\sim$9 FPS under CPU-only inference - representing, to our knowledge, the first demonstration of practical CPU-only animatable 3DGS avatar synthesis. This work represents a significant step toward practical, high-performance digital humans. Project website: https://ramazan793.github.io/AGORA/

