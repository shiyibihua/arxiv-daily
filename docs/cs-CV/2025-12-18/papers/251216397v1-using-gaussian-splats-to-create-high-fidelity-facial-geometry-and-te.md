---
layout: default
title: Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture
---

# Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16397" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16397v1</a>
  <a href="https://arxiv.org/pdf/2512.16397.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16397v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16397v1', 'Using Gaussian Splats to Create High-Fidelity Facial Geometry and Texture')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haodi He, Jihun Yu, Ronald Fedkiw

**分类**: cs.CV, cs.AI, cs.GR

**发布日期**: 2025-12-18

**备注**: Submitted to CVPR 2026. 21 pages, 22 figures

---

## 💡 一句话要点

**利用高斯溅射重建高保真面部几何与纹理，实现可控人脸生成**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `高斯溅射` `人脸重建` `神经渲染` `三维建模` `纹理生成`

## 📋 核心要点

1. 现有方法难以从少量、未经校准的人脸图像中重建高保真度的三维人脸模型，尤其是在光照条件不一致的情况下。
2. 该方法利用高斯溅射的显式特性，结合语义分割和几何约束，实现从少量图像中重建高质量人脸几何和纹理。
3. 实验表明，该方法能够从仅11张图像中重建出高质量的人脸模型，并能生成可用于标准图形管线的高分辨率纹理。

## 📝 摘要（中文）

本文利用日益流行的三维神经表示，从一组未经校准的人脸图像中构建统一且一致的解释。该方法采用高斯溅射，因为它比NeRF更显式，因此更易于约束。利用分割标注对齐面部的语义区域，从而仅用11张图像即可重建中性姿势（而无需长视频）。软约束高斯分布到一个潜在的三角化表面，以提供更结构化的重建，进而指导后续扰动以提高三角化表面的精度。生成的三角化表面可用于标准图形管线。此外，也是最重要的，展示了精确的几何体如何使高斯溅射转换为纹理空间，在纹理空间中，它们可以被视为与视角相关的神经纹理。这允许在场景中的任何资产上使用高视觉保真度的高斯溅射，而无需修改任何其他资产或图形管线的任何其他方面（几何体、光照、渲染器等）。利用可重新光照的高斯模型将纹理与光照分离，以获得可用于标准图形管线中的高分辨率反照率纹理。系统的灵活性允许使用不同的图像进行训练，即使光照不兼容，也有助于鲁棒的正则化。最后，通过展示其在文本驱动的资产创建管线中的应用，证明了该方法的有效性。

## 🔬 方法详解

**问题定义**：现有方法，如NeRF，在处理少量、未经校准的人脸图像时，难以重建出高保真度的几何和纹理。尤其是在光照条件不一致的情况下，重建质量会显著下降。此外，NeRF的隐式表示使得难以施加几何约束，从而影响重建的精度和可控性。

**核心思路**：论文的核心思路是利用高斯溅射（Gaussian Splatting）的显式特性，结合语义分割和几何约束，实现从少量图像中重建高质量的人脸几何和纹理。通过将高斯分布约束到潜在的三角化表面，可以提高重建的结构性和精度。同时，将高斯溅射转换为纹理空间，可以实现与视角相关的神经纹理，从而提高渲染的真实感。

**技术框架**：该方法主要包含以下几个阶段：1) 使用分割标注对齐面部的语义区域，从而实现中性姿势的重建。2) 将高斯分布软约束到潜在的三角化表面，以提供更结构化的重建。3) 通过扰动三角化表面，提高其精度。4) 将高斯溅射转换为纹理空间，生成与视角相关的神经纹理。5) 利用可重新光照的高斯模型将纹理与光照分离，生成高分辨率的反照率纹理。

**关键创新**：该方法最重要的技术创新点在于将高斯溅射与几何约束相结合，从而实现从少量图像中重建高质量的人脸几何和纹理。与现有方法相比，该方法能够更好地处理光照条件不一致的情况，并能生成可用于标准图形管线的高分辨率纹理。此外，将高斯溅射转换为纹理空间，可以实现与视角相关的神经纹理，从而提高渲染的真实感。

**关键设计**：论文中关键的设计包括：1) 使用软约束将高斯分布约束到三角化表面，约束强度需要仔细调整。2) 使用可重新光照的高斯模型，该模型包含漫反射和镜面反射分量，用于分离纹理和光照。3) 使用L1损失和感知损失来优化高斯溅射的参数。4) 使用Adam优化器进行训练，学习率需要根据数据集进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16397v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16397v1/figs/ablation/vis_gaussians/2_geometry_render.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16397v1/figs/head_poses/00.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在少量图像人脸重建任务上取得了显著成果，仅使用11张图像即可重建出高质量的人脸模型。与现有方法相比，该方法能够更好地处理光照条件不一致的情况，并能生成可用于标准图形管线的高分辨率纹理。实验结果表明，该方法能够生成更逼真、更自然的人脸模型。

## 🎯 应用场景

该研究成果可广泛应用于人脸重建、虚拟现实、增强现实、游戏开发等领域。例如，可以用于创建逼真的虚拟化身，用于在线会议、社交媒体等应用。此外，该方法还可以用于人脸动画、表情迁移等任务，从而实现更自然、更逼真的人机交互。

## 📄 摘要（原文）

> We leverage increasingly popular three-dimensional neural representations in order to construct a unified and consistent explanation of a collection of uncalibrated images of the human face. Our approach utilizes Gaussian Splatting, since it is more explicit and thus more amenable to constraints than NeRFs. We leverage segmentation annotations to align the semantic regions of the face, facilitating the reconstruction of a neutral pose from only 11 images (as opposed to requiring a long video). We soft constrain the Gaussians to an underlying triangulated surface in order to provide a more structured Gaussian Splat reconstruction, which in turn informs subsequent perturbations to increase the accuracy of the underlying triangulated surface. The resulting triangulated surface can then be used in a standard graphics pipeline. In addition, and perhaps most impactful, we show how accurate geometry enables the Gaussian Splats to be transformed into texture space where they can be treated as a view-dependent neural texture. This allows one to use high visual fidelity Gaussian Splatting on any asset in a scene without the need to modify any other asset or any other aspect (geometry, lighting, renderer, etc.) of the graphics pipeline. We utilize a relightable Gaussian model to disentangle texture from lighting in order to obtain a delit high-resolution albedo texture that is also readily usable in a standard graphics pipeline. The flexibility of our system allows for training with disparate images, even with incompatible lighting, facilitating robust regularization. Finally, we demonstrate the efficacy of our approach by illustrating its use in a text-driven asset creation pipeline.

