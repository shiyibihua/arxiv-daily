---
layout: default
title: Make-It-Poseable: Feed-forward Latent Posing Model for 3D Humanoid Character Animation
---

# Make-It-Poseable: Feed-forward Latent Posing Model for 3D Humanoid Character Animation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16767" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16767v1</a>
  <a href="https://arxiv.org/pdf/2512.16767.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16767v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16767v1', 'Make-It-Poseable: Feed-forward Latent Posing Model for 3D Humanoid Character Animation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyang Guo, Ori Zhang, Jax Xiang, Alan Zhao, Wengang Zhou, Houqiang Li

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project page: https://jasongzy.github.io/Make-It-Poseable/

---

## 💡 一句话要点

**提出Make-It-Poseable，用于解决3D人形角色动画中姿态控制难题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `3D角色动画` `姿态控制` `潜在空间变换` `Transformer网络` `人形建模`

## 📋 核心要点

1. 现有3D角色姿态控制方法在皮肤权重预测、拓扑结构和姿态一致性方面存在不足，影响了其鲁棒性和泛化性。
2. Make-It-Poseable将姿态控制问题转化为潜在空间变换，通过操纵潜在表示而非直接变形顶点来重建角色。
3. 该方法引入了潜在姿态Transformer、密集姿态表示、潜在空间监督和自适应补全模块，提升了姿态质量。

## 📝 摘要（中文）

本文提出了一种名为Make-It-Poseable的新型前馈框架，旨在解决3D角色姿态控制问题。现有方法如自动绑定和姿态条件生成，常面临皮肤权重预测不准确、拓扑结构缺陷和姿态一致性差等挑战，限制了其鲁棒性和泛化能力。Make-It-Poseable将角色姿态控制重新定义为潜在空间变换问题。该方法不直接变形网格顶点，而是通过操纵角色的潜在表示来重建新的姿态。核心是一个潜在姿态Transformer，它根据骨骼运动来操纵形状token。密集姿态表示用于实现精确控制。为了确保高保真几何形状并适应拓扑变化，还引入了潜在空间监督策略和自适应补全模块。实验表明，该方法在姿态质量方面表现出色，并且可以自然地扩展到3D编辑应用，如部件替换和优化。

## 🔬 方法详解

**问题定义**：论文旨在解决3D人形角色动画中，现有方法在姿态控制方面存在的不足。具体来说，现有方法如自动绑定和姿态条件生成，在预测精确的皮肤权重、处理拓扑结构变化以及保证姿态一致性方面存在困难，导致动画效果不佳，鲁棒性和泛化能力受限。

**核心思路**：论文的核心思路是将3D角色姿态控制问题转化为潜在空间中的变换问题。不再直接操作3D模型的顶点，而是将3D模型编码到潜在空间，通过在潜在空间中进行操作，然后解码回3D模型，从而实现姿态的改变。这种方法可以更好地处理拓扑结构变化，并提高姿态控制的精度。

**技术框架**：Make-It-Poseable框架主要包含以下几个模块：1) 编码器：将3D角色模型编码到潜在空间。2) 潜在姿态Transformer：根据输入的骨骼运动信息，在潜在空间中对形状token进行变换，实现姿态的改变。3) 解码器：将变换后的潜在表示解码回3D模型。4) 自适应补全模块：用于处理拓扑结构变化，保证生成模型的完整性。

**关键创新**：该方法最重要的创新点在于将姿态控制问题转化为潜在空间变换。与直接操作3D模型顶点的方法相比，这种方法可以更好地处理拓扑结构变化，并提高姿态控制的精度。此外，潜在姿态Transformer的设计也使得模型能够更好地理解骨骼运动信息，并将其转化为潜在空间中的变换。

**关键设计**：论文中使用了密集姿态表示，以便更精确地控制角色的姿态。同时，为了保证生成模型的质量，论文还引入了潜在空间监督策略，即在潜在空间中对生成模型进行约束。此外，自适应补全模块的设计也考虑了拓扑结构变化，保证生成模型的完整性。具体的损失函数设计和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16767v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16767v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16767v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Make-It-Poseable在姿态质量方面优于现有方法。该方法能够生成更逼真、更自然的3D角色动画，并且能够更好地处理拓扑结构变化。此外，该方法还可以自然地扩展到3D编辑应用，例如部件替换和优化。具体的性能数据和对比基线在论文中有详细描述。

## 🎯 应用场景

该研究成果可广泛应用于游戏开发、电影制作、虚拟现实和增强现实等领域。它可以帮助艺术家和动画师更轻松地创建逼真的3D角色动画，并提高动画制作的效率。此外，该方法还可以应用于3D角色编辑，例如部件替换和优化，为用户提供更灵活的创作工具。未来，该技术有望进一步发展，实现更复杂、更自然的3D角色动画。

## 📄 摘要（原文）

> Posing 3D characters is a fundamental task in computer graphics and vision. However, existing methods like auto-rigging and pose-conditioned generation often struggle with challenges such as inaccurate skinning weight prediction, topological imperfections, and poor pose conformance, limiting their robustness and generalizability. To overcome these limitations, we introduce Make-It-Poseable, a novel feed-forward framework that reformulates character posing as a latent-space transformation problem. Instead of deforming mesh vertices as in traditional pipelines, our method reconstructs the character in new poses by directly manipulating its latent representation. At the core of our method is a latent posing transformer that manipulates shape tokens based on skeletal motion. This process is facilitated by a dense pose representation for precise control. To ensure high-fidelity geometry and accommodate topological changes, we also introduce a latent-space supervision strategy and an adaptive completion module. Our method demonstrates superior performance in posing quality. It also naturally extends to 3D editing applications like part replacement and refinement.

