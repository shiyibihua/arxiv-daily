---
layout: default
title: Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding
---

# Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.03601" target="_blank" class="toolbar-btn">arXiv: 2512.03601v1</a>
    <a href="https://arxiv.org/pdf/2512.03601.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.03601v1" 
            onclick="toggleFavorite(this, '2512.03601v1', 'Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Haoran Zhou, Gim Hee Lee

**分类**: cs.CV

**发布日期**: 2025-12-03

**备注**: Accepted to NeurIPS 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://hrzhou2.github.io/motion4d-web/)

---

## 💡 一句话要点

**Motion4D：学习3D一致的运动和语义信息，用于4D场景理解**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `4D场景理解` `动态场景分析` `3D一致性` `高斯溅射` `运动估计` `语义分割` `单目视频` `基础模型`

## 📋 核心要点

1. 现有2D视觉基础模型在动态场景分析中表现出色，但缺乏3D一致性，导致空间错位和时间闪烁。
2. Motion4D将2D先验知识融入4D高斯溅射表示，通过顺序和全局优化，实现3D一致的运动和语义理解。
3. 实验表明，Motion4D在点云跟踪、视频分割和新视角合成等任务中，显著优于现有2D和3D方法。

## 📝 摘要（中文）

本文提出Motion4D，一个新颖的框架，旨在解决单目视频动态场景分析中，现有2D基础模型缺乏3D一致性的问题。Motion4D将2D基础模型的先验知识整合到统一的4D高斯溅射表示中。该方法包含一个两阶段迭代优化框架：1) 顺序优化，分阶段更新运动和语义场，以保持局部一致性；2) 全局优化，联合优化所有属性，以实现长期连贯性。为了提高运动精度，引入了3D置信度图，动态调整运动先验，并采用自适应重采样过程，基于像素RGB和语义误差，在欠表示区域插入新的高斯分布。此外，通过迭代优化语义场和更新SAM的提示，增强语义连贯性。大量实验表明，Motion4D在基于点的跟踪、视频对象分割和新视角合成等多种场景理解任务中，显著优于2D基础模型和现有3D方法。

## 🔬 方法详解

**问题定义**：现有方法，特别是基于2D视觉基础模型的方法，在处理单目视频的动态场景理解时，虽然具有很强的泛化能力，但缺乏3D一致性。这导致在复杂的3D环境中出现严重的几何错位和时间上的闪烁现象，限制了其在需要精确3D信息的任务中的应用。因此，需要一种能够保证3D一致性的动态场景理解方法。

**核心思路**：Motion4D的核心思路是将2D视觉基础模型的强大先验知识与3D场景表示相结合，利用高斯溅射（Gaussian Splatting）作为统一的4D表示，并通过迭代优化框架来保证运动和语义的3D一致性。通过这种方式，可以有效地利用2D模型的优势，同时克服其在3D空间中的不足。

**技术框架**：Motion4D的整体框架包含两个主要的迭代优化阶段：顺序优化和全局优化。顺序优化首先更新运动场，然后更新语义场，以保持局部一致性。全局优化则联合优化所有属性，以实现长期连贯性。此外，该框架还包括一个3D置信度图，用于动态调整运动先验，以及一个自适应重采样过程，用于在欠表示区域插入新的高斯分布。

**关键创新**：Motion4D的关键创新在于其将2D视觉基础模型的先验知识有效地融入到3D场景表示中，并设计了一个两阶段的迭代优化框架，以保证运动和语义的3D一致性。此外，3D置信度图和自适应重采样过程进一步提高了运动精度和场景表示的完整性。与现有方法相比，Motion4D能够更好地处理复杂的3D动态场景，并提供更精确的场景理解。

**关键设计**：3D置信度图的设计用于动态调整运动先验，其具体实现方式未知。自适应重采样过程基于像素RGB和语义误差来确定需要插入新高斯分布的区域，具体的误差计算方式和阈值设置未知。语义一致性通过迭代优化语义场和更新SAM的提示来实现，具体的提示更新策略未知。损失函数的设计细节未知。

## 📊 实验亮点

Motion4D在多个场景理解任务中表现出色。在点云跟踪、视频对象分割和新视角合成任务中，Motion4D显著优于现有的2D基础模型和3D方法。具体的性能提升数据未知，但摘要强调了其在多种任务中的优越性，表明了该方法具有很强的泛化能力和实用价值。

## 🎯 应用场景

Motion4D的研究成果可应用于自动驾驶、机器人导航、增强现实等领域。通过提供3D一致的动态场景理解，可以提升自动驾驶系统的环境感知能力，增强机器人在复杂环境中的导航能力，并为AR应用提供更逼真的场景交互体验。该研究还有助于推动虚拟现实、游戏开发等领域的发展。

## 📄 摘要（原文）

> Recent advancements in foundation models for 2D vision have substantially improved the analysis of dynamic scenes from monocular videos. However, despite their strong generalization capabilities, these models often lack 3D consistency, a fundamental requirement for understanding scene geometry and motion, thereby causing severe spatial misalignment and temporal flickering in complex 3D environments. In this paper, we present Motion4D, a novel framework that addresses these challenges by integrating 2D priors from foundation models into a unified 4D Gaussian Splatting representation. Our method features a two-part iterative optimization framework: 1) Sequential optimization, which updates motion and semantic fields in consecutive stages to maintain local consistency, and 2) Global optimization, which jointly refines all attributes for long-term coherence. To enhance motion accuracy, we introduce a 3D confidence map that dynamically adjusts the motion priors, and an adaptive resampling process that inserts new Gaussians into under-represented regions based on per-pixel RGB and semantic errors. Furthermore, we enhance semantic coherence through an iterative refinement process that resolves semantic inconsistencies by alternately optimizing the semantic fields and updating prompts of SAM2. Extensive evaluations demonstrate that our Motion4D significantly outperforms both 2D foundation models and existing 3D-based approaches across diverse scene understanding tasks, including point-based tracking, video object segmentation, and novel view synthesis. Our code is available at https://hrzhou2.github.io/motion4d-web/.

