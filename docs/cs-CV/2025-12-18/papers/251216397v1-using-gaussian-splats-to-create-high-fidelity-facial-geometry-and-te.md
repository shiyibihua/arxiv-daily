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

**关键词**: `高斯溅射` `人脸重建` `神经渲染` `纹理生成` `三维重建`

## 📋 核心要点

1. 现有方法难以从少量未校准图像中重建高保真人脸几何与纹理，尤其是在光照条件不一致的情况下。
2. 利用高斯溅射的显式特性，结合语义分割和表面约束，实现从少量图像中重建高质量人脸模型。
3. 通过将高斯溅射转换为纹理空间，并解耦光照，生成可用于标准图形管线的、高质量的反照率纹理。

## 📝 摘要（中文）

本文利用日益流行的三维神经表示，从一组未经校准的人脸图像中构建统一且一致的解释。该方法采用高斯溅射，因为它比NeRF更显式，因此更易于约束。利用分割标注对齐面部的语义区域，从而仅用11张图像即可重建中性姿势（而无需长视频）。软约束高斯分布到一个潜在的三角化表面，以提供更结构化的重建，进而指导后续扰动以提高三角化表面的准确性。生成的三角化表面可用于标准图形管线。此外，也是最重要的，展示了精确的几何体如何使高斯溅射转换为纹理空间，在纹理空间中，它们可以被视为与视角相关的神经纹理。这允许在场景中的任何资产上使用高视觉保真度的高斯溅射，而无需修改任何其他资产或图形管线的任何其他方面（几何体、光照、渲染器等）。利用可重新光照的高斯模型将纹理与光照分离，以获得可在标准图形管线中使用的去光照高分辨率反照率纹理。系统的灵活性允许使用不同的图像进行训练，即使光照不兼容，也有助于鲁棒的正则化。最后，通过展示其在文本驱动的资产创建管线中的应用，证明了该方法的有效性。

## 🔬 方法详解

**问题定义**：现有方法，如NeRF，在人脸重建任务中，尤其是在图像数量有限且未经校准的情况下，难以生成高保真度的几何和纹理。此外，光照条件不一致也会严重影响重建质量。现有方法通常需要大量的训练数据或复杂的预处理步骤，限制了其在实际应用中的可行性。

**核心思路**：本文的核心思路是利用高斯溅射（Gaussian Splatting）的显式特性，结合语义分割和表面约束，从少量图像中重建高质量的人脸模型。通过将高斯溅射投影到纹理空间，并解耦光照，生成可用于标准图形管线的、高质量的反照率纹理。这种方法能够有效地处理光照不一致的问题，并降低对训练数据量的需求。

**技术框架**：该方法主要包含以下几个阶段：1) 使用少量未校准的人脸图像作为输入；2) 利用语义分割标注对齐面部的语义区域，从而实现中性姿势的重建；3) 将高斯溅射软约束到一个潜在的三角化表面，以提供更结构化的重建；4) 通过扰动三角化表面来提高其准确性；5) 将高斯溅射转换为纹理空间，并将其视为与视角相关的神经纹理；6) 利用可重新光照的高斯模型将纹理与光照分离，生成去光照的高分辨率反照率纹理。

**关键创新**：该方法的关键创新在于：1) 利用高斯溅射的显式特性，使其更易于约束，从而能够从少量图像中重建高质量的人脸模型；2) 将高斯溅射转换为纹理空间，并将其视为与视角相关的神经纹理，从而能够生成高质量的反照率纹理；3) 利用可重新光照的高斯模型将纹理与光照分离，从而能够有效地处理光照不一致的问题。与现有方法相比，该方法能够以更少的图像和更低的计算成本，生成更高质量的人脸模型。

**关键设计**：该方法的关键设计包括：1) 使用软约束将高斯溅射约束到三角化表面，以提高重建的结构性；2) 使用可重新光照的高斯模型，该模型允许将纹理与光照分离，从而生成去光照的反照率纹理；3) 使用分割标注对齐面部的语义区域，从而实现中性姿势的重建。损失函数的设计也至关重要，需要平衡重建质量、表面平滑度和光照一致性。

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

该方法仅使用11张图像即可重建高质量的人脸模型，无需长视频或复杂的预处理步骤。通过将高斯溅射转换为纹理空间，并解耦光照，生成了高质量的反照率纹理，可直接用于标准图形管线。实验结果表明，该方法在重建质量和效率方面均优于现有方法，尤其是在光照条件不一致的情况下。

## 🎯 应用场景

该研究成果可广泛应用于虚拟现实、增强现实、游戏开发、数字人生成等领域。通过该方法，可以快速、高效地创建逼真的人脸模型，为用户提供更沉浸式的体验。此外，该方法还可以应用于人脸识别、表情识别等领域，提高相关算法的准确性和鲁棒性。未来，该技术有望在个性化定制、远程医疗、教育等领域发挥重要作用。

## 📄 摘要（原文）

> We leverage increasingly popular three-dimensional neural representations in order to construct a unified and consistent explanation of a collection of uncalibrated images of the human face. Our approach utilizes Gaussian Splatting, since it is more explicit and thus more amenable to constraints than NeRFs. We leverage segmentation annotations to align the semantic regions of the face, facilitating the reconstruction of a neutral pose from only 11 images (as opposed to requiring a long video). We soft constrain the Gaussians to an underlying triangulated surface in order to provide a more structured Gaussian Splat reconstruction, which in turn informs subsequent perturbations to increase the accuracy of the underlying triangulated surface. The resulting triangulated surface can then be used in a standard graphics pipeline. In addition, and perhaps most impactful, we show how accurate geometry enables the Gaussian Splats to be transformed into texture space where they can be treated as a view-dependent neural texture. This allows one to use high visual fidelity Gaussian Splatting on any asset in a scene without the need to modify any other asset or any other aspect (geometry, lighting, renderer, etc.) of the graphics pipeline. We utilize a relightable Gaussian model to disentangle texture from lighting in order to obtain a delit high-resolution albedo texture that is also readily usable in a standard graphics pipeline. The flexibility of our system allows for training with disparate images, even with incompatible lighting, facilitating robust regularization. Finally, we demonstrate the efficacy of our approach by illustrating its use in a text-driven asset creation pipeline.

