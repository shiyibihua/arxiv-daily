---
layout: default
title: "TexAvatars : Hybrid Texel-3D Representations for Stable Rigging of Photorealistic Gaussian Head Avatars"
---

# TexAvatars : Hybrid Texel-3D Representations for Stable Rigging of Photorealistic Gaussian Head Avatars

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21099" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21099v1</a>
  <a href="https://arxiv.org/pdf/2512.21099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21099v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21099v1', 'TexAvatars : Hybrid Texel-3D Representations for Stable Rigging of Photorealistic Gaussian Head Avatars')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaeseong Lee, Junyeong Ahn, Taewoong Kang, Jaegul Choo

**分类**: cs.GR, cs.AI, cs.CV

**发布日期**: 2025-12-24

**备注**: 3DV 2026, Project page with videos: https://summertight.github.io/TexAvatars/

---

## 💡 一句话要点

**TexAvatars：结合Texel和3D表示，实现逼真高斯头部头像的稳定绑定**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `3D头部头像` `高斯表示` `解析绑定` `纹素空间` `神经渲染` `AR/XR` `表情重演`

## 📋 核心要点

1. 现有头部头像方法在极端姿势和表情下泛化性差，且过度依赖神经回归器，导致几何一致性弱，难以处理复杂变形。
2. TexAvatars结合解析绑定的几何基础和纹素空间的空间连续性，通过网格感知的雅可比矩阵驱动3D变形，实现平滑过渡。
3. TexAvatars在极端姿势和表情变化下实现了最先进的性能，能够捕捉细粒度的表情效果，具有强大的泛化能力。

## 📝 摘要（中文）

构建可驱动且逼真的3D头部头像已成为AR/XR的核心任务，能够实现沉浸式和富有表现力的用户体验。随着3D高斯等高保真和高效表示的出现，最近的研究已转向超细节的头部头像。现有方法通常分为两类：基于规则的解析绑定或基于神经网络的变形场。虽然在受限设置中有效，但两种方法通常无法推广到未见过的表情和姿势，尤其是在极端的重演场景中。其他方法将高斯约束到3DMM的全局纹素空间，以降低渲染复杂度。然而，这些基于纹素的头像往往未能充分利用底层网格结构。它们应用最少的解析变形，并严重依赖UV空间中的神经回归器和启发式正则化，这削弱了几何一致性，并限制了外推到复杂的、超出分布的变形。为了解决这些限制，我们引入了TexAvatars，一种混合头像表示，它将解析绑定的显式几何基础与纹素空间的空间连续性相结合。我们的方法通过CNN预测UV空间中的局部几何属性，但通过网格感知的雅可比矩阵驱动3D变形，从而实现跨三角形边界的平滑和语义上有意义的过渡。这种混合设计将语义建模与几何控制分离，从而提高了泛化性、可解释性和稳定性。此外，TexAvatars以高保真度捕捉细粒度的表情效果，包括肌肉引起的皱纹、眉间纹和逼真的口腔几何形状。我们的方法在极端的姿势和表情变化下实现了最先进的性能，在具有挑战性的头部重演设置中表现出强大的泛化能力。

## 🔬 方法详解

**问题定义**：现有3D头部头像构建方法，如基于规则的解析绑定和基于神经网络的变形场，在处理极端姿势和表情时泛化能力不足。基于纹素的方法虽然降低了渲染复杂度，但过度依赖神经回归器和启发式正则化，削弱了几何一致性，限制了对复杂变形的外推能力。

**核心思路**：TexAvatars的核心思路是结合解析绑定的显式几何基础和纹素空间的空间连续性，提出一种混合头像表示。通过在UV空间预测局部几何属性，并利用网格感知的雅可比矩阵驱动3D变形，从而实现平滑且语义上有意义的变形。这种混合设计将语义建模与几何控制分离，提升了泛化性、可解释性和稳定性。

**技术框架**：TexAvatars的技术框架主要包含以下几个阶段：1) 在UV空间使用CNN预测局部几何属性；2) 利用网格结构计算网格感知的雅可比矩阵；3) 使用雅可比矩阵驱动3D变形，从而实现头部头像的姿势和表情控制。该框架的关键在于将语义建模（CNN预测几何属性）与几何控制（雅可比矩阵驱动变形）解耦。

**关键创新**：TexAvatars最重要的技术创新点在于其混合表示方法，它结合了解析绑定的几何基础和纹素空间的空间连续性。与完全依赖神经回归器的方法不同，TexAvatars利用网格感知的雅可比矩阵进行变形，从而保证了几何一致性，并提高了对复杂变形的泛化能力。

**关键设计**：TexAvatars的关键设计包括：1) 使用CNN在UV空间预测局部几何属性，例如顶点位移；2) 设计网格感知的雅可比矩阵，用于将UV空间的变形转换为3D空间的变形；3) 使用合适的损失函数来训练CNN，例如L1损失或L2损失，以保证预测的几何属性的准确性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21099v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21099v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21099v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TexAvatars在极端姿势和表情变化下实现了最先进的性能，能够捕捉细粒度的表情效果，例如肌肉引起的皱纹和逼真的口腔几何形状。实验结果表明，TexAvatars在具有挑战性的头部重演设置中表现出强大的泛化能力，优于现有的基于规则和基于神经网络的方法。

## 🎯 应用场景

TexAvatars在AR/XR领域具有广泛的应用前景，可以用于创建逼真且可驱动的3D头部头像，从而提升用户在虚拟会议、游戏和社交互动中的沉浸感和表达能力。该技术还可以应用于虚拟形象定制、数字内容创作和远程呈现等领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Constructing drivable and photorealistic 3D head avatars has become a central task in AR/XR, enabling immersive and expressive user experiences. With the emergence of high-fidelity and efficient representations such as 3D Gaussians, recent works have pushed toward ultra-detailed head avatars. Existing approaches typically fall into two categories: rule-based analytic rigging or neural network-based deformation fields. While effective in constrained settings, both approaches often fail to generalize to unseen expressions and poses, particularly in extreme reenactment scenarios. Other methods constrain Gaussians to the global texel space of 3DMMs to reduce rendering complexity. However, these texel-based avatars tend to underutilize the underlying mesh structure. They apply minimal analytic deformation and rely heavily on neural regressors and heuristic regularization in UV space, which weakens geometric consistency and limits extrapolation to complex, out-of-distribution deformations. To address these limitations, we introduce TexAvatars, a hybrid avatar representation that combines the explicit geometric grounding of analytic rigging with the spatial continuity of texel space. Our approach predicts local geometric attributes in UV space via CNNs, but drives 3D deformation through mesh-aware Jacobians, enabling smooth and semantically meaningful transitions across triangle boundaries. This hybrid design separates semantic modeling from geometric control, resulting in improved generalization, interpretability, and stability. Furthermore, TexAvatars captures fine-grained expression effects, including muscle-induced wrinkles, glabellar lines, and realistic mouth cavity geometry, with high fidelity. Our method achieves state-of-the-art performance under extreme pose and expression variations, demonstrating strong generalization in challenging head reenactment settings.

