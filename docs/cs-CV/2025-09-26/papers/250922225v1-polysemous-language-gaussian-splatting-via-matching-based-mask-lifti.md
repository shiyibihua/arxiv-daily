---
layout: default
title: Polysemous Language Gaussian Splatting via Matching-based Mask Lifting
---

# Polysemous Language Gaussian Splatting via Matching-based Mask Lifting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22225" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22225v1</a>
  <a href="https://arxiv.org/pdf/2509.22225.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22225v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22225v1', 'Polysemous Language Gaussian Splatting via Matching-based Mask Lifting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayu Ding, Xinpeng Liu, Zhiyi Pan, Shiqiang Long, Ge Li

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出MUSplat，通过匹配的掩码提升实现多义语言高斯溅射，无需场景重训练。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `高斯溅射` `开放词汇` `3D场景理解` `语义分割` `视觉-语言模型`

## 📋 核心要点

1. 现有方法依赖于昂贵的场景重训练，限制了其即插即用性，且无法处理复杂的多概念语义。
2. MUSplat通过预训练的2D分割模型生成多粒度掩码，并利用视觉-语言模型提取鲁棒的文本特征，实现开放词汇查询。
3. 实验表明，MUSplat在开放词汇3D对象选择和语义分割任务中优于现有方法，且无需场景重训练，大大缩短了适应时间。

## 📝 摘要（中文）

将2D开放词汇理解提升到3D高斯溅射(3DGS)场景是一个关键挑战。然而，主流方法存在三个主要缺陷：(i)依赖昂贵的场景重训练，无法即插即用；(ii)单义设计无法表示复杂的多概念语义；(iii)易受跨视角语义不一致的影响，破坏最终语义表示。为克服这些限制，我们引入MUSplat，一个无需训练的框架，完全放弃特征优化。利用预训练的2D分割模型，我们的流程生成多粒度2D掩码并将其提升到3D，估计每个高斯点的先验概率以形成初始对象组。然后，我们使用语义熵和几何不透明度优化这些初始组的模糊边界。随后，通过解释对象在其最具代表性的视角中的外观，视觉-语言模型(VLM)提取鲁棒的文本特征，协调视觉不一致性，从而实现通过语义匹配进行开放词汇查询。通过消除昂贵的场景训练过程，MUSplat将场景适应时间从数小时减少到几分钟。在开放词汇3D对象选择和语义分割的基准任务中，MUSplat优于已建立的基于训练的框架，同时解决了它们的单义性限制。

## 🔬 方法详解

**问题定义**：现有方法在将2D开放词汇理解提升到3D高斯溅射场景时，面临着需要昂贵的场景重训练、无法处理多义语义以及容易受到跨视角语义不一致影响等问题。这些问题限制了3D场景理解的效率和准确性。

**核心思路**：MUSplat的核心思路是避免对每个场景进行耗时的重训练，而是利用预训练的2D分割模型和视觉-语言模型，通过掩码提升和语义匹配来实现3D场景的开放词汇理解。这种方法旨在提高效率，并解决现有方法在处理复杂语义和跨视角一致性方面的不足。

**技术框架**：MUSplat的整体框架包括以下几个主要阶段：1) 利用预训练的2D分割模型生成多粒度2D掩码；2) 将2D掩码提升到3D空间，并估计每个高斯点的先验概率以形成初始对象组；3) 使用语义熵和几何不透明度优化初始对象组的边界；4) 利用视觉-语言模型提取鲁棒的文本特征，用于语义匹配和开放词汇查询。

**关键创新**：MUSplat的关键创新在于其无需场景重训练的设计，以及利用视觉-语言模型来解决跨视角语义不一致性的方法。通过避免耗时的优化过程，MUSplat显著提高了场景适应的速度。此外，通过视觉-语言模型的语义匹配，MUSplat能够更好地处理复杂的多概念语义。

**关键设计**：MUSplat的关键设计包括：1) 使用预训练的2D分割模型来生成初始掩码，避免从头开始训练；2) 利用语义熵和几何不透明度来优化对象组的边界，提高分割的准确性；3) 使用视觉-语言模型提取文本特征，并进行语义匹配，实现开放词汇查询。具体的参数设置和网络结构细节在论文中应该有更详细的描述（未知）。

## 📊 实验亮点

MUSplat在开放词汇3D对象选择和语义分割任务中取得了显著的性能提升，优于现有的基于训练的框架。通过消除场景重训练，MUSplat将场景适应时间从数小时缩短到几分钟。具体的性能数据和提升幅度需要在论文中查找（未知）。

## 🎯 应用场景

MUSplat具有广泛的应用前景，例如机器人导航、自动驾驶、增强现实和虚拟现实等领域。它可以用于理解和操作复杂的3D环境，并支持基于自然语言的交互。该研究的实际价值在于提高了3D场景理解的效率和准确性，并为未来的开放词汇3D场景理解研究奠定了基础。

## 📄 摘要（原文）

> Lifting 2D open-vocabulary understanding into 3D Gaussian Splatting (3DGS) scenes is a critical challenge. However, mainstream methods suffer from three key flaws: (i) their reliance on costly per-scene retraining prevents plug-and-play application; (ii) their restrictive monosemous design fails to represent complex, multi-concept semantics; and (iii) their vulnerability to cross-view semantic inconsistencies corrupts the final semantic representation. To overcome these limitations, we introduce MUSplat, a training-free framework that abandons feature optimization entirely. Leveraging a pre-trained 2D segmentation model, our pipeline generates and lifts multi-granularity 2D masks into 3D, where we estimate a foreground probability for each Gaussian point to form initial object groups. We then optimize the ambiguous boundaries of these initial groups using semantic entropy and geometric opacity. Subsequently, by interpreting the object's appearance across its most representative viewpoints, a Vision-Language Model (VLM) distills robust textual features that reconciles visual inconsistencies, enabling open-vocabulary querying via semantic matching. By eliminating the costly per-scene training process, MUSplat reduces scene adaptation time from hours to mere minutes. On benchmark tasks for open-vocabulary 3D object selection and semantic segmentation, MUSplat outperforms established training-based frameworks while simultaneously addressing their monosemous limitations.

