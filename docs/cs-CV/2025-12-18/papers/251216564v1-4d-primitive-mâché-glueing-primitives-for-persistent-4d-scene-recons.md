---
layout: default
title: 4D Primitive-Mâché: Glueing Primitives for Persistent 4D Scene Reconstruction
---

# 4D Primitive-Mâché: Glueing Primitives for Persistent 4D Scene Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16564" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16564v1</a>
  <a href="https://arxiv.org/pdf/2512.16564.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16564v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16564v1', '4D Primitive-Mâché: Glueing Primitives for Persistent 4D Scene Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kirill Mazur, Marwan Taher, Andrew J. Davison

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: For project page, see https://makezur.github.io/4DPM/

---

## 💡 一句话要点

**提出4D Primitive-Mâché，通过拼接基元实现持久化4D场景重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `4D场景重建` `动态重建` `基元分解` `运动估计` `单目视觉`

## 📋 核心要点

1. 现有动态重建方法难以重建所有时间步长的场景，存在信息丢失和不连续性问题。
2. 将场景分解为刚性3D基元，通过优化流程联合推断基元的刚性运动，实现4D场景重建。
3. 引入运动外推机制，利用运动分组技术保持物体在不可见时的运动连续性，提升重建质量。

## 📝 摘要（中文）

本文提出了一种动态重建系统，该系统以单目RGB视频作为输入，输出场景的完整且持久的重建结果。换句话说，我们不仅重建当前可见的场景部分，还重建所有先前观察到的部分，从而能够重放所有时间步长的完整重建。我们的方法将场景分解为一组刚性3D基元，这些基元被认为在整个场景中移动。利用估计的密集2D对应关系，我们通过优化流程联合推断这些基元的刚性运动，从而产生场景的4D重建，即提供随时间动态移动的3D几何体。为此，我们还引入了一种机制来推断不可见物体的运动，采用运动分组技术来保持连续性。该系统实现了4D时空感知，提供了诸如随时间推移的可重放3D铰接物体重建、多物体扫描和物体持久性等功能。在物体扫描和多物体数据集上，我们的系统在定量和定性方面均显著优于现有方法。

## 🔬 方法详解

**问题定义**：现有动态场景重建方法通常只能重建当前时刻可见的部分，无法完整地重建整个时间序列中的场景，导致信息丢失和重建结果不连续。尤其是在物体暂时离开视野或被遮挡的情况下，重建质量会显著下降。因此，如何实现持久化的、完整的4D场景重建是一个关键问题。

**核心思路**：论文的核心思路是将动态场景分解为一组刚性3D基元，并假设这些基元在场景中进行刚性运动。通过估计图像中的2D对应关系，并优化这些基元的运动参数，从而实现对场景的4D重建。这种方法能够有效地处理遮挡和物体离开视野的情况，并通过运动外推机制保持重建结果的连续性。

**技术框架**：该系统的整体框架包括以下几个主要阶段：1) 输入单目RGB视频；2) 估计图像中的密集2D对应关系；3) 将场景分解为一组刚性3D基元；4) 通过优化流程联合推断这些基元的刚性运动；5) 利用运动分组技术对不可见物体进行运动外推；6) 输出完整的4D场景重建结果。

**关键创新**：该论文的关键创新在于提出了一种基于基元的4D场景重建方法，该方法能够实现持久化的重建，即重建所有时间步长的场景，而不仅仅是当前可见的部分。此外，该论文还引入了一种运动外推机制，能够有效地处理遮挡和物体离开视野的情况，并通过运动分组技术保持重建结果的连续性。

**关键设计**：论文中使用了优化方法来估计基元的运动参数，具体的损失函数设计和优化算法选择未知。运动分组技术用于对不可见物体进行运动外推，具体的实现细节未知。此外，如何有效地将场景分解为刚性3D基元也是一个关键的设计问题，但论文中没有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16564v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16564v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16564v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该系统在物体扫描和多物体数据集上进行了实验，结果表明，该系统在定量和定性方面均显著优于现有方法。具体的性能数据和提升幅度未知，但论文强调了该系统在重建完整性和连续性方面的优势。

## 🎯 应用场景

该研究成果可应用于增强现实、虚拟现实、机器人导航、自动驾驶等领域。例如，在AR/VR中，可以提供更真实、更沉浸式的体验，用户可以与过去时刻的场景进行交互。在机器人导航中，可以帮助机器人更好地理解和预测环境变化，从而实现更安全、更高效的导航。在自动驾驶中，可以提高车辆对动态环境的感知能力，从而提高驾驶安全性。

## 📄 摘要（原文）

> We present a dynamic reconstruction system that receives a casual monocular RGB video as input, and outputs a complete and persistent reconstruction of the scene. In other words, we reconstruct not only the the currently visible parts of the scene, but also all previously viewed parts, which enables replaying the complete reconstruction across all timesteps.
>   Our method decomposes the scene into a set of rigid 3D primitives, which are assumed to be moving throughout the scene. Using estimated dense 2D correspondences, we jointly infer the rigid motion of these primitives through an optimisation pipeline, yielding a 4D reconstruction of the scene, i.e. providing 3D geometry dynamically moving through time. To achieve this, we also introduce a mechanism to extrapolate motion for objects that become invisible, employing motion-grouping techniques to maintain continuity.
>   The resulting system enables 4D spatio-temporal awareness, offering capabilities such as replayable 3D reconstructions of articulated objects through time, multi-object scanning, and object permanence. On object scanning and multi-object datasets, our system significantly outperforms existing methods both quantitatively and qualitatively.

