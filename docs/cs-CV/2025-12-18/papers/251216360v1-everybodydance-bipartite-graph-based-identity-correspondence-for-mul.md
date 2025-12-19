---
layout: default
title: EverybodyDance: Bipartite Graph-Based Identity Correspondence for Multi-Character Animation
---

# EverybodyDance: Bipartite Graph-Based Identity Correspondence for Multi-Character Animation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16360" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16360v1</a>
  <a href="https://arxiv.org/pdf/2512.16360.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16360v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16360v1', 'EverybodyDance: Bipartite Graph-Based Identity Correspondence for Multi-Character Animation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haotian Ling, Zequn Chen, Qiuying Chen, Donglin Di, Yongjia Ma, Hao Li, Chen Wei, Zhulin Tao, Xun Yang

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**EverybodyDance：基于二分图的角色匹配方法，解决多角色动画中的身份对应问题。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `多角色动画` `身份对应` `二分图匹配` `姿态驱动` `深度学习`

## 📋 核心要点

1. 现有姿态驱动的角色动画在单角色场景中取得了显著进展，但扩展到多角色场景，尤其是在涉及位置交换时，极具挑战。
2. EverybodyDance的核心思想是将角色间的身份对应关系建模为二分图，并通过优化图结构度量来保证身份对应关系的正确性。
3. 论文提出了身份对应评估基准，并通过大量实验证明EverybodyDance在身份对应和视觉保真度方面均优于现有方法。

## 📝 摘要（中文）

本文提出EverybodyDance，一个针对多角色动画中身份对应（IC）正确性的系统性解决方案。核心是身份匹配图（IMG），它将生成帧和参考帧中的角色建模为加权完全二分图中的两个节点集合。边缘权重通过提出的Mask-Query Attention（MQA）计算，量化每对角色之间的亲和力。论文将IC正确性形式化为图结构度量，并在训练期间对其进行优化。此外，还提出了一系列针对多角色动画的策略，包括身份嵌入引导、多尺度匹配策略和预分类采样。为了评估IC性能，创建了身份对应评估基准。大量实验表明，EverybodyDance在IC和视觉保真度方面均优于现有技术水平。

## 🔬 方法详解

**问题定义**：论文旨在解决多角色动画生成中身份对应（Identity Correspondence, IC）问题。现有方法在处理多角色场景，特别是角色位置发生交换时，难以保证生成动画中角色的身份与参考帧中的角色身份一致。这导致动画效果不自然，角色混乱。

**核心思路**：论文的核心思路是将生成动画帧和参考帧中的角色建模为二分图的节点，通过计算节点之间的相似度（即边的权重）来建立角色之间的对应关系。通过优化二分图的结构，使得相似度高的节点尽可能匹配，从而保证身份对应关系的正确性。

**技术框架**：EverybodyDance主要包含以下几个模块：1) **身份匹配图（IMG）构建**：将参考帧和生成帧中的角色作为节点，构建一个完全二分图。2) **Mask-Query Attention（MQA）**：计算二分图中节点之间的边缘权重，表示角色之间的相似度。MQA利用角色的mask信息作为query，去attention参考帧中的特征，从而得到相似度。3) **图结构优化**：设计损失函数，优化二分图的结构，使得相似度高的节点尽可能匹配。4) **身份嵌入引导**：在生成过程中，利用身份信息引导生成器，提高身份对应关系的准确性。5) **多尺度匹配策略**：在不同尺度上进行角色匹配，提高鲁棒性。6) **预分类采样**：对训练数据进行预分类，提高训练效率。

**关键创新**：论文最重要的技术创新点在于将身份对应问题形式化为图结构优化问题，并提出了Mask-Query Attention（MQA）来计算角色之间的相似度。与现有方法相比，该方法能够更好地处理角色位置交换的情况，并保证身份对应关系的正确性。

**关键设计**：1) **Mask-Query Attention (MQA)**：利用角色的mask作为query，参考帧的特征作为key和value，计算attention score作为角色之间的相似度。2) **图结构损失函数**：设计损失函数，鼓励相似度高的节点匹配，相似度低的节点不匹配。3) **身份嵌入**：将角色的身份信息嵌入到生成器中，引导生成器生成具有正确身份的角色。4) **多尺度匹配**：在多个尺度上计算角色之间的相似度，提高匹配的鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16360v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16360v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16360v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，EverybodyDance在身份对应（IC）和视觉保真度方面均优于现有技术水平。具体而言，在身份对应评估基准上，EverybodyDance的IC指标比最先进的基线方法提高了显著幅度（具体数值未知）。同时，视觉效果也更加自然，角色身份更加明确。

## 🎯 应用场景

该研究成果可广泛应用于虚拟现实、游戏开发、电影制作等领域。例如，可以用于创建多人在线互动动画，允许用户控制多个角色进行互动，而无需担心角色身份混乱的问题。此外，该技术还可以应用于舞蹈教学、运动分析等领域，帮助用户更好地理解和学习动作。

## 📄 摘要（原文）

> Consistent pose-driven character animation has achieved remarkable progress in single-character scenarios. However, extending these advances to multi-character settings is non-trivial, especially when position swap is involved. Beyond mere scaling, the core challenge lies in enforcing correct Identity Correspondence (IC) between characters in reference and generated frames. To address this, we introduce EverybodyDance, a systematic solution targeting IC correctness in multi-character animation. EverybodyDance is built around the Identity Matching Graph (IMG), which models characters in the generated and reference frames as two node sets in a weighted complete bipartite graph. Edge weights, computed via our proposed Mask-Query Attention (MQA), quantify the affinity between each pair of characters. Our key insight is to formalize IC correctness as a graph structural metric and to optimize it during training. We also propose a series of targeted strategies tailored for multi-character animation, including identity-embedded guidance, a multi-scale matching strategy, and pre-classified sampling, which work synergistically. Finally, to evaluate IC performance, we curate the Identity Correspondence Evaluation benchmark, dedicated to multi-character IC correctness. Extensive experiments demonstrate that EverybodyDance substantially outperforms state-of-the-art baselines in both IC and visual fidelity.

