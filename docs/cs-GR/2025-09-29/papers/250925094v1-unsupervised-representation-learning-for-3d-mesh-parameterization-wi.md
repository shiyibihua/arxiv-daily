---
layout: default
title: Unsupervised Representation Learning for 3D Mesh Parameterization with Semantic and Visibility Objectives
---

# Unsupervised Representation Learning for 3D Mesh Parameterization with Semantic and Visibility Objectives

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25094" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25094v1</a>
  <a href="https://arxiv.org/pdf/2509.25094.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25094v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25094v1', 'Unsupervised Representation Learning for 3D Mesh Parameterization with Semantic and Visibility Objectives')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: AmirHossein Zamani, Bruno Roy, Arianna Rampini

**分类**: cs.GR, cs.CV

**发布日期**: 2025-09-29

**🔗 代码/项目**: [GITHUB](https://github.com/AHHHZ975/Semantic-Visibility-UV-Param)

---

## 💡 一句话要点

**提出一种无监督3D网格参数化学习框架，优化语义对齐和可见性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `3D网格参数化` `无监督学习` `UV映射` `语义分割` `可见性感知` `环境光遮蔽` `纹理生成`

## 📋 核心要点

1. 现有3D生成模型依赖于手动UV映射，该过程耗时且需要专业技能，成为3D内容创作的瓶颈。
2. 论文提出一种无监督学习框架，通过语义分割和可见性感知，自动生成高质量的UV映射，无需人工干预。
3. 实验结果表明，该方法生成的UV图集在纹理生成和减少缝合线伪影方面优于现有方法。

## 📝 摘要（中文）

本文提出了一种无监督可微框架，用于自动进行3D网格参数化，旨在克服现有方法对人工UV映射的依赖以及忽略语义和可见性感知的缺点。该框架通过语义和可见性感知目标来增强标准的几何保持UV学习。在语义感知方面，该流程首先将网格分割成语义3D部分，然后应用无监督学习的逐部分UV参数化骨干网络，最后将各部分的图表聚合为统一的UV图集。在可见性感知方面，使用环境光遮蔽（AO）作为曝光代理，并通过反向传播一个软可微的AO加权缝合线目标，引导切割缝合线朝向遮挡区域。通过与最先进方法进行定性和定量评估，结果表明该方法生成的UV图集能够更好地支持纹理生成，并减少了与现有基线相比可感知的缝合线伪影。

## 🔬 方法详解

**问题定义**：现有3D网格纹理生成方法严重依赖于手动创建的UV映射，这是一个耗时且需要专业知识的过程，极大地限制了3D内容创作的效率。现有的自动UV映射方法通常忽略了两个重要的感知标准：语义一致性（UV图表应在形状之间对齐语义相似的3D部分）和可见性感知（切割缝合线应位于不太可能被看到的区域）。

**核心思路**：本文的核心思路是通过无监督学习的方式，同时优化UV映射的语义一致性和可见性，从而自动生成高质量的UV图集。通过将网格分割成语义部分，并学习每个部分的UV参数化，保证了语义一致性。利用环境光遮蔽（AO）信息引导切割缝合线位于遮挡区域，提高了视觉效果。

**技术框架**：该框架包含三个主要阶段：1) 语义分割：将3D网格分割成具有语义意义的部分。2) 逐部分UV参数化：对每个语义部分应用无监督学习的UV参数化骨干网络，生成该部分的UV图表。3) 图集聚合：将各个部分的UV图表聚合为一个统一的UV图集。此外，利用环境光遮蔽信息，通过可微的AO加权缝合线损失函数，引导切割缝合线位于遮挡区域。

**关键创新**：该方法的主要创新在于：1) 提出了一种无监督的UV参数化学习框架，无需人工标注的UV映射。2) 引入了语义感知和可见性感知的目标函数，提高了UV图集的质量。3) 使用环境光遮蔽信息来引导切割缝合线的位置，减少了视觉伪影。

**关键设计**：语义分割可以使用现有的3D分割算法。逐部分UV参数化可以使用现有的几何保持UV学习方法，并进行无监督训练。AO加权缝合线损失函数的设计是关键，它通过计算缝合线周围区域的AO值，并将其作为权重，引导缝合线移动到AO值较高的区域（即遮挡区域）。具体实现上，AO值可以通过渲染网格得到，缝合线损失函数可以使用交叉熵损失或类似的损失函数。

## 📊 实验亮点

实验结果表明，该方法生成的UV图集在纹理生成方面优于现有方法，能够产生更清晰、更自然的纹理效果。与现有基线方法相比，该方法能够显著减少可感知的缝合线伪影，提高了视觉质量。代码已开源。

## 🎯 应用场景

该研究成果可广泛应用于3D内容创作领域，例如游戏开发、电影制作、虚拟现实和增强现实等。它可以显著减少人工UV映射的工作量，提高3D资产的生产效率，并提升最终产品的视觉质量。此外，该方法还可以应用于3D模型检索、形状分析等领域。

## 📄 摘要（原文）

> Recent 3D generative models produce high-quality textures for 3D mesh objects. However, they commonly rely on the heavy assumption that input 3D meshes are accompanied by manual mesh parameterization (UV mapping), a manual task that requires both technical precision and artistic judgment. Industry surveys show that this process often accounts for a significant share of asset creation, creating a major bottleneck for 3D content creators. Moreover, existing automatic methods often ignore two perceptually important criteria: (1) semantic awareness (UV charts should align semantically similar 3D parts across shapes) and (2) visibility awareness (cutting seams should lie in regions unlikely to be seen). To overcome these shortcomings and to automate the mesh parameterization process, we present an unsupervised differentiable framework that augments standard geometry-preserving UV learning with semantic- and visibility-aware objectives. For semantic-awareness, our pipeline (i) segments the mesh into semantic 3D parts, (ii) applies an unsupervised learned per-part UV-parameterization backbone, and (iii) aggregates per-part charts into a unified UV atlas. For visibility-awareness, we use ambient occlusion (AO) as an exposure proxy and back-propagate a soft differentiable AO-weighted seam objective to steer cutting seams toward occluded regions. By conducting qualitative and quantitative evaluations against state-of-the-art methods, we show that the proposed method produces UV atlases that better support texture generation and reduce perceptible seam artifacts compared to recent baselines. Our implementation code is publicly available at: https://github.com/AHHHZ975/Semantic-Visibility-UV-Param.

