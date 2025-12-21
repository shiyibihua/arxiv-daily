---
layout: default
title: Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation
---

# Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16893" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16893v1</a>
  <a href="https://arxiv.org/pdf/2512.16893.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16893v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16893v1', 'Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project website is https://research.nvidia.com/labs/amri/projects/instant4d

---

## 💡 一句话要点

**提出基于3D感知表达蒸馏的快速高表现力高斯头部头像方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `人像动画` `3D感知` `扩散模型` `知识蒸馏` `高斯溅射` `实时渲染` `局部融合`

## 📋 核心要点

1. 现有2D人像动画方法在3D一致性和速度上存在不足，难以应用于实时场景。
2. 通过将2D扩散模型的知识蒸馏到3D前馈网络中，实现快速且高表现力的3D人像动画。
3. 该方法在动画和姿势控制上达到107.31 FPS，动画质量与SOTA方法相当。

## 📝 摘要（中文）

得益于视频扩散模型的最新进展，人像动画的质量得到了显著提升。然而，这些2D方法通常会牺牲3D一致性和速度，限制了它们在数字孪生或远程呈现等实际场景中的应用。相比之下，基于显式3D表示（如神经辐射场或高斯溅射）的3D感知面部动画前馈方法，可确保3D一致性并实现更快的推理速度，但表达细节较差。本文旨在结合两者的优势，将知识从基于2D扩散的方法提炼到前馈编码器中，该编码器可立即将野外单张图像转换为3D一致、快速且富有表现力的可动画表示。我们的动画表示与面部的3D表示解耦，并从数据中隐式地学习运动，从而消除了对通常限制动画能力的预定义参数模型的依赖。与先前用于融合3D结构和动画信息的计算密集型全局融合机制（例如，多个注意力层）不同，我们的设计采用了一种高效的轻量级局部融合策略，以实现高动画表现力。因此，我们的方法以107.31 FPS的速度运行动画和姿势控制，同时实现了与最先进技术相当的动画质量，超过了在速度和质量之间进行权衡的替代设计。

## 🔬 方法详解

**问题定义**：现有2D人像动画方法虽然在动画质量上有所提升，但往往牺牲了3D一致性和速度，难以满足实时应用的需求。而基于3D表示的方法虽然保证了3D一致性和速度，但在表达细节上有所欠缺。因此，如何兼顾3D一致性、速度和表达能力是本文要解决的问题。

**核心思路**：本文的核心思路是将2D扩散模型的表达能力“蒸馏”到3D前馈网络中。具体来说，利用2D扩散模型生成高质量的动画细节，然后训练一个前馈网络来快速预测这些细节，并将其融合到3D人像表示中。这样既能保证3D一致性和速度，又能获得丰富的动画表达。

**技术框架**：该方法主要包含以下几个模块：1) 2D扩散模型：用于生成高质量的动画细节；2) 前馈编码器：将单张图像转换为3D一致、快速且富有表现力的可动画表示；3) 轻量级局部融合模块：将动画信息融合到3D结构信息中。整个流程是，首先使用2D扩散模型生成动画细节，然后使用前馈编码器预测这些细节，最后使用轻量级局部融合模块将这些细节融合到3D人像表示中。

**关键创新**：该方法最重要的创新点在于使用了一种轻量级的局部融合策略，而不是传统的全局融合机制（如注意力层）。这种局部融合策略可以有效地融合3D结构和动画信息，同时保持较高的计算效率。此外，该方法还解耦了动画表示和3D表示，使得动画的控制更加灵活。

**关键设计**：该方法使用了一种高效的轻量级局部融合策略，具体来说，它将动画特征和3D结构特征在局部区域进行融合，而不是像全局注意力机制那样对所有特征进行融合。这种局部融合策略可以有效地减少计算量，同时保持较高的融合效果。此外，该方法还设计了一种特殊的损失函数，用于训练前馈编码器，使得其能够准确地预测动画细节。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16893v1/fig/expressiveness_vs_consistency_colored.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16893v1/fig/pipeline-2.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16893v1/fig/residual_features.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在动画和姿势控制上达到了107.31 FPS，显著优于其他需要牺牲速度来换取质量的方法。同时，该方法在动画质量上与最先进的2D扩散模型相当，证明了其在速度和质量上的优越性。实验结果表明，该方法能够生成高质量、3D一致且富有表现力的头部头像动画。

## 🎯 应用场景

该研究成果可广泛应用于数字孪生、远程呈现、虚拟现实、增强现实等领域。例如，可以用于创建逼真的虚拟化身，进行远程会议和协作，或者用于游戏和娱乐应用中，提供更具表现力的角色动画。该技术的发展将推动人机交互方式的进步，并为用户带来更沉浸式的体验。

## 📄 摘要（原文）

> Portrait animation has witnessed tremendous quality improvements thanks to recent advances in video diffusion models. However, these 2D methods often compromise 3D consistency and speed, limiting their applicability in real-world scenarios, such as digital twins or telepresence. In contrast, 3D-aware facial animation feedforward methods -- built upon explicit 3D representations, such as neural radiance fields or Gaussian splatting -- ensure 3D consistency and achieve faster inference speed, but come with inferior expression details. In this paper, we aim to combine their strengths by distilling knowledge from a 2D diffusion-based method into a feed-forward encoder, which instantly converts an in-the-wild single image into a 3D-consistent, fast yet expressive animatable representation. Our animation representation is decoupled from the face's 3D representation and learns motion implicitly from data, eliminating the dependency on pre-defined parametric models that often constrain animation capabilities. Unlike previous computationally intensive global fusion mechanisms (e.g., multiple attention layers) for fusing 3D structural and animation information, our design employs an efficient lightweight local fusion strategy to achieve high animation expressivity. As a result, our method runs at 107.31 FPS for animation and pose control while achieving comparable animation quality to the state-of-the-art, surpassing alternative designs that trade speed for quality or vice versa. Project website is https://research.nvidia.com/labs/amri/projects/instant4d

