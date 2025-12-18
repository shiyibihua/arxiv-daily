---
layout: default
title: Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction
---

# Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18497" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18497v2</a>
  <a href="https://arxiv.org/pdf/2509.18497.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18497v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18497v2', 'Differentiable Light Transport with Gaussian Surfels via Adapted Radiosity for Efficient Relighting and Geometry Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi

**分类**: cs.GR, cs.CV

**发布日期**: 2025-09-23 (更新: 2025-09-29)

---

## 💡 一句话要点

**提出基于高斯Surfels的可微光传输方法，实现高效的Relighting和几何重建。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `可微渲染` `光传输` `高斯Surfels` `辐射度` `全局光照`

## 📋 核心要点

1. 现有方法在辐射场中忽略材质反射属性和光照条件建模，导致几何歧义，难以进行Relighting。
2. 论文采用高斯Surfels作为图元，构建可微光传输框架，在球谐函数空间中进行光照计算，支持漫反射和镜面反射。
3. 实验结果表明，该方法在几何重建、视角合成和Relighting方面优于现有方法，尤其是在数据稀疏的情况下。

## 📝 摘要（中文）

本文提出了一种基于高斯Surfels的可微光传输高效框架，用于实现高效的Relighting和几何重建。该框架灵感来源于经典辐射度理论，并在球谐函数的系数空间中运行，支持漫反射和镜面反射材质。论文将经典辐射度扩展到非二元可见性和半透明图元，提出了高效求解光传输的新型求解器，并推导了梯度优化的反向传播，其效率高于自动微分。在推理阶段，实现了与视角无关的渲染，光传输无需因视角变化而重新计算，从而实现了数百FPS的全局光照效果，包括使用球谐函数表示的视角相关反射。通过大量的定性和定量实验，证明了该方法在几何重建、视角合成和Relighting方面优于以往的逆渲染基线或数据驱动基线，尤其是在已知或未知光照条件下相对稀疏的数据集上。

## 🔬 方法详解

**问题定义**：现有基于辐射场的方法，如高斯溅射，虽然在novel view synthesis和几何重建上取得了成功，但牺牲了材质反射属性和光照条件的建模。这导致几何重建存在歧义，并且难以进行光照重定向(relighting)。虽然基于物理的渲染可以解决这些问题，但将全局光照纳入优化循环的计算成本过高，导致现有方法为了效率而牺牲了精度。

**核心思路**：本文的核心思路是借鉴经典的辐射度理论，利用高斯Surfels作为基本图元，构建一个高效且可微的光传输框架。通过在球谐函数系数空间中进行计算，可以同时处理漫反射和镜面反射材质。该方法旨在在保证全局光照效果的同时，提高计算效率，从而实现快速的relighting和高质量的几何重建。

**技术框架**：该框架主要包含以下几个阶段：1) 使用高斯Surfels表示场景几何；2) 基于辐射度理论建立光传输方程，并在球谐函数空间中表示；3) 提出新的求解器来高效求解光传输方程，该求解器能够处理非二元可见性和半透明图元；4) 推导光传输过程的反向传播，用于梯度优化；5) 在推理阶段，利用预先计算的光传输结果，实现与视角无关的快速渲染。

**关键创新**：该方法的关键创新在于：1) 将经典辐射度理论扩展到非二元可见性和半透明图元，使其能够处理更复杂的场景；2) 提出了高效的光传输求解器，避免了昂贵的自动微分，提高了优化效率；3) 实现了与视角无关的渲染，使得在改变视角时无需重新计算光传输，从而实现了实时的全局光照效果。

**关键设计**：该方法使用球谐函数来表示光照和材质属性，并通过球谐函数系数的乘积来计算光照效果。为了处理非二元可见性，论文提出了一种基于高斯函数的可见性模型。此外，论文还设计了一种新的损失函数，用于优化高斯Surfels的参数，包括位置、法线、颜色和不透明度等。

## 📊 实验亮点

实验结果表明，该方法在几何重建、视角合成和relighting方面均优于现有方法。尤其是在稀疏数据集上，该方法能够重建出更准确的几何结构，并生成更逼真的光照效果。在推理阶段，该方法能够实现数百FPS的渲染速度，支持实时的全局光照效果，包括视角相关的反射。

## 🎯 应用场景

该研究成果可广泛应用于虚拟现实、增强现实、游戏开发、电影制作等领域。通过高效的relighting技术，可以方便地调整虚拟场景的光照效果，提高渲染质量和真实感。此外，高质量的几何重建能力也有助于创建更逼真的3D模型，提升用户体验。该方法在机器人视觉和自动驾驶领域也有潜在应用价值，例如用于模拟不同光照条件下的传感器数据，提高算法的鲁棒性。

## 📄 摘要（原文）

> Radiance fields have gained tremendous success with applications ranging from novel view synthesis to geometry reconstruction, especially with the advent of Gaussian splatting. However, they sacrifice modeling of material reflective properties and lighting conditions, leading to significant geometric ambiguities and the inability to easily perform relighting. One way to address these limitations is to incorporate physically-based rendering, but it has been prohibitively expensive to include full global illumination within the inner loop of the optimization. Therefore, previous works adopt simplifications that make the whole optimization with global illumination effects efficient but less accurate. In this work, we adopt Gaussian surfels as the primitives and build an efficient framework for differentiable light transport, inspired from the classic radiosity theory. The whole framework operates in the coefficient space of spherical harmonics, enabling both diffuse and specular materials. We extend the classic radiosity into non-binary visibility and semi-opaque primitives, propose novel solvers to efficiently solve the light transport, and derive the backward pass for gradient optimizations, which is more efficient than auto-differentiation. During inference, we achieve view-independent rendering where light transport need not be recomputed under viewpoint changes, enabling hundreds of FPS for global illumination effects, including view-dependent reflections using a spherical harmonics representation. Through extensive qualitative and quantitative experiments, we demonstrate superior geometry reconstruction, view synthesis and relighting than previous inverse rendering baselines, or data-driven baselines given relatively sparse datasets with known or unknown lighting conditions.

