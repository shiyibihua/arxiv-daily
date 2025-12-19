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

**关键词**: `人像动画` `3D感知` `表达蒸馏` `高斯溅射` `实时渲染`

## 📋 核心要点

1. 现有2D扩散模型人像动画方法在3D一致性和速度上存在不足，限制了其在实时场景中的应用。
2. 该论文提出一种基于3D感知表达蒸馏的前馈方法，将2D扩散模型的知识迁移到3D表示，实现快速且高表现力的动画。
3. 实验结果表明，该方法在保证动画质量的同时，实现了107.31 FPS的动画和姿势控制速度，优于现有方法。

## 📝 摘要（中文）

得益于视频扩散模型的最新进展，人像动画的质量得到了显著提高。然而，这些2D方法通常会牺牲3D一致性和速度，限制了它们在数字孪生或远程呈现等实际场景中的应用。相比之下，基于显式3D表示（如神经辐射场或高斯溅射）的3D感知面部动画前馈方法，可确保3D一致性并实现更快的推理速度，但表达细节较差。本文旨在结合两者的优势，将知识从基于2D扩散的方法提炼到前馈编码器中，该编码器可立即将野外单张图像转换为3D一致、快速且富有表现力的可动画表示。我们的动画表示与面部的3D表示解耦，并从数据中隐式学习运动，从而消除了对通常限制动画能力的预定义参数模型的依赖。与先前用于融合3D结构和动画信息的计算密集型全局融合机制（例如，多个注意力层）不同，我们的设计采用了一种高效的轻量级局部融合策略，以实现高动画表现力。因此，我们的方法以107.31 FPS的速度运行动画和姿势控制，同时实现了与最先进技术相当的动画质量，超越了在速度和质量之间进行权衡的替代设计。

## 🔬 方法详解

**问题定义**：现有的人像动画方法，特别是基于2D扩散模型的方法，虽然在动画质量上取得了显著进展，但在3D一致性和推理速度方面存在不足。这限制了它们在需要实时性和3D感知的应用场景中的应用，例如数字孪生和远程呈现。另一方面，基于3D表示（如神经辐射场或高斯溅射）的方法虽然保证了3D一致性和速度，但在表达细节上有所欠缺。

**核心思路**：该论文的核心思路是将2D扩散模型的表达能力“蒸馏”到基于3D表示的前馈网络中。通过这种方式，既能保持3D一致性和速度优势，又能获得高质量的动画表达。关键在于设计一种有效的知识迁移机制，将2D扩散模型的丰富细节融入到3D表示中。

**技术框架**：该方法包含一个前馈编码器，用于将单张图像转换为3D一致且可动画的表示。该表示分为两部分：静态的3D人脸结构和动态的动画信息。动画信息从数据中隐式学习，无需依赖预定义的参数模型。为了融合3D结构和动画信息，该方法采用了一种轻量级的局部融合策略，避免了计算量大的全局融合机制。

**关键创新**：该方法的关键创新在于使用3D感知表达蒸馏，将2D扩散模型的表达能力迁移到3D表示中，从而在保证3D一致性和速度的同时，实现了高质量的动画效果。此外，轻量级的局部融合策略也是一个重要的创新点，它在保证表达能力的同时，降低了计算复杂度。

**关键设计**：该方法的一个关键设计是动画表示与3D人脸结构的解耦。这种解耦使得动画信息可以独立于3D结构进行学习和控制，从而提高了动画的灵活性和可控性。此外，损失函数的设计也至关重要，需要平衡3D一致性、动画质量和推理速度。

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

该方法在动画和姿势控制方面达到了107.31 FPS的速度，同时保持了与最先进技术相当的动画质量。实验结果表明，该方法在速度和质量之间取得了良好的平衡，超越了那些为了提高质量而牺牲速度或为了提高速度而降低质量的替代方案。该方法在表达能力方面也优于现有的基于3D表示的方法。

## 🎯 应用场景

该研究成果可广泛应用于数字孪生、远程呈现、虚拟现实、增强现实、游戏等领域。例如，可以用于创建逼真的虚拟化身，实现实时的人脸动画和表情控制，从而提升用户在虚拟环境中的交互体验。此外，该技术还可以应用于电影制作、广告等领域，用于生成高质量的人像动画。

## 📄 摘要（原文）

> Portrait animation has witnessed tremendous quality improvements thanks to recent advances in video diffusion models. However, these 2D methods often compromise 3D consistency and speed, limiting their applicability in real-world scenarios, such as digital twins or telepresence. In contrast, 3D-aware facial animation feedforward methods -- built upon explicit 3D representations, such as neural radiance fields or Gaussian splatting -- ensure 3D consistency and achieve faster inference speed, but come with inferior expression details. In this paper, we aim to combine their strengths by distilling knowledge from a 2D diffusion-based method into a feed-forward encoder, which instantly converts an in-the-wild single image into a 3D-consistent, fast yet expressive animatable representation. Our animation representation is decoupled from the face's 3D representation and learns motion implicitly from data, eliminating the dependency on pre-defined parametric models that often constrain animation capabilities. Unlike previous computationally intensive global fusion mechanisms (e.g., multiple attention layers) for fusing 3D structural and animation information, our design employs an efficient lightweight local fusion strategy to achieve high animation expressivity. As a result, our method runs at 107.31 FPS for animation and pose control while achieving comparable animation quality to the state-of-the-art, surpassing alternative designs that trade speed for quality or vice versa. Project website is https://research.nvidia.com/labs/amri/projects/instant4d

