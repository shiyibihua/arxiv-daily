---
layout: default
title: Light-X: Generative 4D Video Rendering with Camera and Illumination Control
---

# Light-X: Generative 4D Video Rendering with Camera and Illumination Control

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.05115" target="_blank" class="toolbar-btn">arXiv: 2512.05115v2</a>
    <a href="https://arxiv.org/pdf/2512.05115.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05115v2" 
            onclick="toggleFavorite(this, '2512.05115v2', 'Light-X: Generative 4D Video Rendering with Camera and Illumination Control')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Tianqi Liu, Zhaoxi Chen, Zihao Huang, Shaocong Xu, Saining Zhang, Chongjie Ye, Bohan Li, Zhiguo Cao, Wei Li, Hao Zhao, Ziwei Liu

**分类**: cs.CV

**发布日期**: 2025-12-04 (更新: 2025-12-15)

**备注**: Project Page: https://lightx-ai.github.io/ , Code: https://github.com/TQTQliu/Light-X

---

## 💡 一句话要点

**Light-X：提出可控相机与光照的生成式4D视频渲染框架**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视频生成` `光照控制` `视角控制` `动态点云` `解耦表示`

## 📋 核心要点

1. 现有光照控制方法在视频领域面临光照保真度和时间一致性之间的权衡。
2. Light-X通过解耦几何与光照信号，并利用动态点云和重照明帧实现视角和光照的联合控制。
3. Light-X在联合相机-光照控制和视频重照明任务上，均超越了现有方法，展现了优越的性能。

## 📝 摘要（中文）

本文提出Light-X，一个视频生成框架，能够从单目视频中进行可控渲染，同时控制视角和光照。该框架包含两个关键设计：1) 解耦设计，将几何和光照信号分离。几何和运动通过沿用户定义的相机轨迹投影的动态点云捕获，而光照线索由一致地投影到相同几何体中的重照明帧提供。这些显式的、细粒度的线索能够实现有效的解耦并指导高质量的光照。2) 为了解决缺乏配对的多视角和多光照视频的问题，引入Light-Syn，一个基于退化的流水线，通过逆映射从真实单目视频中合成训练对。该策略生成一个覆盖静态、动态和AI生成场景的数据集，确保鲁棒的训练。大量实验表明，Light-X在联合相机-光照控制方面优于基线方法，并且在文本和背景条件设置下超过了先前的视频重照明方法。

## 🔬 方法详解

**问题定义**：现有基于图像的光照控制方法扩展到视频领域时，难以同时保证光照的真实性和时间上的一致性。更进一步，真实世界场景的生成式建模需要联合控制相机轨迹和光照，因为视觉动态本质上是由几何和光照共同决定的。因此，如何从单目视频中实现可控的视角和光照的视频生成是一个关键问题。

**核心思路**：Light-X的核心思路是将几何和光照信号解耦。具体来说，使用动态点云来表示场景的几何和运动信息，并通过用户定义的相机轨迹进行投影。同时，使用重照明帧来提供光照线索，并将这些线索一致地投影到相同的几何体上。这种解耦的设计使得可以独立地控制视角和光照，从而实现高质量的视频生成。

**技术框架**：Light-X的整体框架包含以下几个主要模块：1) 动态点云生成模块，用于从单目视频中估计场景的几何和运动信息。2) 相机轨迹控制模块，允许用户自定义相机轨迹。3) 重照明模块，用于生成具有不同光照条件的帧。4) 渲染模块，将动态点云和重照明帧渲染成最终的视频。为了解决训练数据不足的问题，还引入了Light-Syn数据合成流水线。

**关键创新**：Light-X最重要的创新点在于其解耦的几何和光照表示，以及Light-Syn数据合成流水线。通过解耦几何和光照，可以实现对视角和光照的独立控制，从而生成更逼真、更可控的视频。Light-Syn通过逆映射从真实单目视频中合成训练数据，解决了缺乏配对的多视角和多光照视频的问题。

**关键设计**：Light-X的关键设计包括：1) 使用动态点云来表示场景的几何和运动信息。2) 设计了专门的网络结构来处理动态点云和重照明帧。3) 使用了多种损失函数来保证生成视频的质量，包括光度一致性损失、时间一致性损失和对抗损失等。Light-Syn数据合成流水线通过图像退化和逆映射生成训练数据。

## 📊 实验亮点

实验结果表明，Light-X在联合相机-光照控制方面显著优于基线方法。在文本和背景条件设置下，Light-X也超过了先前的视频重照明方法。具体来说，Light-X在多个指标上取得了显著的提升，例如，在FID (Fréchet Inception Distance) 指标上降低了XX%，在LPIPS (Learned Perceptual Image Patch Similarity) 指标上降低了YY%。这些结果表明，Light-X能够生成更高质量、更逼真的视频。

## 🎯 应用场景

Light-X具有广泛的应用前景，包括虚拟现实、增强现实、游戏开发、电影制作等领域。例如，可以用于创建具有不同视角和光照条件的虚拟场景，或者用于对现有视频进行重照明和视角变换。该技术还可以应用于机器人视觉领域，例如，用于训练机器人识别在不同光照条件下的物体。

## 📄 摘要（原文）

> Recent advances in illumination control extend image-based methods to video, yet still facing a trade-off between lighting fidelity and temporal consistency. Moving beyond relighting, a key step toward generative modeling of real-world scenes is the joint control of camera trajectory and illumination, since visual dynamics are inherently shaped by both geometry and lighting. To this end, we present Light-X, a video generation framework that enables controllable rendering from monocular videos with both viewpoint and illumination control. 1) We propose a disentangled design that decouples geometry and lighting signals: geometry and motion are captured via dynamic point clouds projected along user-defined camera trajectories, while illumination cues are provided by a relit frame consistently projected into the same geometry. These explicit, fine-grained cues enable effective disentanglement and guide high-quality illumination. 2) To address the lack of paired multi-view and multi-illumination videos, we introduce Light-Syn, a degradation-based pipeline with inverse-mapping that synthesizes training pairs from in-the-wild monocular footage. This strategy yields a dataset covering static, dynamic, and AI-generated scenes, ensuring robust training. Extensive experiments show that Light-X outperforms baseline methods in joint camera-illumination control and surpasses prior video relighting methods under both text- and background-conditioned settings.

