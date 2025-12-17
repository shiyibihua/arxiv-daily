---
layout: default
title: LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM
---

# LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.16144" target="_blank" class="toolbar-btn">arXiv: 2511.16144v1</a>
    <a href="https://arxiv.org/pdf/2511.16144.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16144v1" 
            onclick="toggleFavorite(this, '2511.16144v1', 'LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Sibaek Lee, Seongbo Ha, Kyeongsu Kang, Joonyeol Choi, Seungjun Tak, Hyeonwoo Yu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-20

**备注**: 18 pages

---

## 💡 一句话要点

**LEGO-SLAM：基于语言嵌入高斯优化的实时开放词汇SLAM系统**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `SLAM` `3D高斯溅射` `语言嵌入` `开放词汇` `场景理解` `机器人导航` `语义SLAM`

## 📋 核心要点

1. 现有基于3DGS的SLAM系统缺乏开放词汇的语义理解能力，难以支持高级机器人交互。
2. LEGO-SLAM提出一种场景自适应的编码器-解码器，将高维语言嵌入压缩到低维空间，实现实时渲染和在线适应。
3. 实验表明，LEGO-SLAM在保证建图质量和跟踪精度的前提下，实现了15FPS的实时开放词汇SLAM。

## 📝 摘要（中文）

本文提出LEGO-SLAM，首个在基于3D高斯溅射(3DGS)的SLAM系统中实现实时、开放词汇建图的框架。该方法使用场景自适应的编码器-解码器，将高维语言嵌入提炼为紧凑的16维特征空间，从而降低了每个高斯的内存占用并加速了渲染，实现了实时性能。与静态方法不同，该编码器能够在线适应未见过的场景。这些紧凑的特征还支持一种语言引导的剪枝策略，可识别语义冗余，在保持渲染质量的同时，将地图的高斯数量减少60%以上。此外，还引入了一种基于语言的闭环检测方法，复用这些映射特征，无需单独的检测模型。实验表明，LEGO-SLAM在提供开放词汇能力的同时，实现了具有竞争力的建图质量和跟踪精度，帧率达到15 FPS。

## 🔬 方法详解

**问题定义**：现有的基于3D高斯溅射(3DGS)的SLAM系统虽然能够构建逼真的3D地图，但缺乏开放词汇的语义理解能力，限制了其在高级机器人交互中的应用。将语言特征集成到SLAM中面临着存储高维特征带来的巨大内存和渲染开销的挑战，而现有的静态模型方法又缺乏对新环境的适应性。

**核心思路**：LEGO-SLAM的核心思路是通过一个场景自适应的编码器-解码器，将高维的语言嵌入压缩到一个紧凑的低维特征空间。这种设计既能保留必要的语义信息，又能显著降低内存占用和渲染开销，从而实现实时性能。同时，编码器能够在线适应新的场景，克服了静态模型的局限性。

**技术框架**：LEGO-SLAM的整体框架包括以下几个主要模块：1) 3DGS SLAM：使用3DGS作为底层地图表示，进行场景重建和相机位姿估计。2) 场景自适应编码器-解码器：将高维语言嵌入编码为紧凑的低维特征，并进行解码。编码器在线适应新场景。3) 语言引导的剪枝策略：利用低维特征识别语义冗余，减少地图中的高斯数量。4) 基于语言的闭环检测：复用低维特征进行闭环检测，无需额外的检测模型。

**关键创新**：LEGO-SLAM的关键创新在于：1) 场景自适应的编码器-解码器，能够将高维语言嵌入压缩到低维空间，实现实时渲染和在线适应。2) 语言引导的剪枝策略，能够有效减少地图中的高斯数量，提高效率。3) 基于语言的闭环检测，避免了对额外检测模型的依赖。

**关键设计**：编码器-解码器将高维语言嵌入压缩到16维特征空间。损失函数包括渲染损失、深度损失和语义一致性损失。语言引导的剪枝策略基于特征相似度进行高斯聚类，并移除冗余的高斯。闭环检测基于全局特征相似度进行候选帧选择，并进行几何验证。

## 📊 实验亮点

LEGO-SLAM在多个数据集上进行了实验，结果表明，该方法在提供开放词汇能力的同时，实现了具有竞争力的建图质量和跟踪精度，帧率达到15 FPS。与现有方法相比，LEGO-SLAM能够将地图的高斯数量减少60%以上，同时保持渲染质量。此外，LEGO-SLAM的闭环检测性能也优于传统的基于视觉特征的方法。

## 🎯 应用场景

LEGO-SLAM具有广泛的应用前景，例如：机器人导航、场景理解、增强现实、虚拟现实等。该技术可以使机器人在未知环境中进行语义理解和交互，例如：在家庭环境中识别物体并执行任务，在仓库中进行物品定位和拣选，在城市环境中进行导航和路径规划。该研究的未来影响在于推动机器人和人工智能技术的发展，使其能够更好地理解和适应真实世界。

## 📄 摘要（原文）

> Recent advances in 3D Gaussian Splatting (3DGS) have enabled Simultaneous Localization and Mapping (SLAM) systems to build photorealistic maps. However, these maps lack the open-vocabulary semantic understanding required for advanced robotic interaction. Integrating language features into SLAM remains a significant challenge, as storing high-dimensional features demands excessive memory and rendering overhead, while existing methods with static models lack adaptability for novel environments. To address these limitations, we propose LEGO-SLAM (Language-Embedded Gaussian Optimization SLAM), the first framework to achieve real-time, open-vocabulary mapping within a 3DGS-based SLAM system. At the core of our method is a scene-adaptive encoder-decoder that distills high-dimensional language embeddings into a compact 16-dimensional feature space. This design reduces the memory per Gaussian and accelerates rendering, enabling real-time performance. Unlike static approaches, our encoder adapts online to unseen scenes. These compact features also enable a language-guided pruning strategy that identifies semantic redundancy, reducing the map's Gaussian count by over 60\% while maintaining rendering quality. Furthermore, we introduce a language-based loop detection approach that reuses these mapping features, eliminating the need for a separate detection model. Extensive experiments demonstrate that LEGO-SLAM achieves competitive mapping quality and tracking accuracy, all while providing open-vocabulary capabilities at 15 FPS.

