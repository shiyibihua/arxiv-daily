---
layout: default
title: "UniC-Lift: Unified 3D Instance Segmentation via Contrastive Learning"
---

# UniC-Lift: Unified 3D Instance Segmentation via Contrastive Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24763" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24763v1</a>
  <a href="https://arxiv.org/pdf/2512.24763.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24763v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24763v1', 'UniC-Lift: Unified 3D Instance Segmentation via Contrastive Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ankit Dhiman, Srinath R, Jaswanth Reddy, Lokesh R Boregowda, Venkatesh Babu Radhakrishnan

**分类**: cs.CV

**发布日期**: 2025-12-31

**备注**: Accepted to AAAI 2026. Project Page: https://unic-lift.github.io/

---

## 💡 一句话要点

**UniC-Lift：通过对比学习实现统一的3D实例分割**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D实例分割` `对比学习` `高斯溅射` `神经辐射场` `统一框架`

## 📋 核心要点

1. 现有3D实例分割方法受限于多视角2D标签不一致性，导致3D预测效果不佳，且通常采用两阶段流程，效率较低。
2. UniC-Lift提出统一框架，通过可学习的特征嵌入和“嵌入到标签”过程，将对比学习和标签优化集成，提升分割性能。
3. 为解决物体边界伪影问题，提出在光栅化特征嵌入上进行硬样本挖掘，稳定训练并显著提升ScanNet等数据集上的分割效果。

## 📝 摘要（中文）

3D高斯溅射(3DGS)和神经辐射场(NeRF)推动了新视角合成的发展。最近的方法将多视角2D分割扩展到3D，从而实现实例/语义分割，以更好地理解场景。一个关键的挑战是2D实例标签在不同视角下的一致性问题，导致较差的3D预测。现有方法采用两阶段方法，一些依赖于对超参数敏感的对比学习聚类，而另一些则预处理标签以保证一致性。我们提出了一个统一的框架，它合并了这些步骤，通过引入用于高斯基元分割的可学习特征嵌入，从而减少了训练时间并提高了性能。然后，通过一种新颖的“嵌入到标签”过程，将该嵌入有效地解码为实例标签，从而有效地集成了优化。虽然这个统一的框架提供了显著的好处，但我们观察到物体边界处存在伪影。为了解决物体边界问题，我们提出了沿这些边界进行硬样本挖掘。然而，直接将硬挖掘应用于特征嵌入被证明是不稳定的。因此，我们在计算三元组损失之前，将线性层应用于光栅化的特征嵌入，这稳定了训练并显著提高了性能。我们的方法在ScanNet、Replica3D和Messy-Rooms数据集上，在质量和数量上都优于基线。

## 🔬 方法详解

**问题定义**：现有3D实例分割方法面临的关键问题是多视角2D实例标签的不一致性，这会导致3D预测的准确性下降。此外，许多现有方法采用两阶段流程，例如先进行对比学习聚类，然后再进行标签优化，这增加了训练的复杂性和时间成本。这些方法通常对超参数敏感，且需要对标签进行预处理以保证一致性。

**核心思路**：UniC-Lift的核心思路是将对比学习和标签优化集成到一个统一的框架中。通过学习一个特征嵌入，使得属于同一实例的高斯基元在嵌入空间中更接近，而属于不同实例的基元更远离。然后，利用一个“嵌入到标签”的过程，将学习到的嵌入直接解码为实例标签，从而避免了传统两阶段方法中的分离优化问题。

**技术框架**：UniC-Lift的整体框架包括以下几个主要模块：1) 特征嵌入模块：用于学习高斯基元的特征嵌入，该嵌入能够区分不同的实例。2) “嵌入到标签”模块：将学习到的特征嵌入解码为实例标签。3) 损失函数：包括对比损失（例如三元组损失）和分割损失，用于优化特征嵌入和标签预测。4) 硬样本挖掘模块：用于解决物体边界处的伪影问题，通过挖掘边界附近的困难样本来提升分割精度。

**关键创新**：UniC-Lift最重要的创新点在于其统一的框架，它将对比学习和标签优化集成到一个端到端的流程中。与现有方法相比，UniC-Lift避免了复杂的两阶段优化，减少了训练时间和超参数调整的难度。此外，提出的“嵌入到标签”过程能够更有效地利用学习到的特征嵌入进行实例分割。

**关键设计**：为了解决物体边界处的伪影问题，UniC-Lift采用了一种硬样本挖掘策略。具体来说，首先对特征嵌入进行光栅化，然后应用一个线性层。在光栅化后的特征上计算三元组损失，而不是直接在原始特征嵌入上进行计算，这有助于稳定训练过程并提高性能。此外，损失函数的设计也至关重要，需要平衡对比损失和分割损失，以获得最佳的分割效果。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24763v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24763v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24763v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

UniC-Lift在ScanNet、Replica3D和Messy-Rooms数据集上取得了显著的性能提升。相较于基线方法，UniC-Lift在实例分割精度方面取得了明显的优势，尤其是在物体边界区域。通过硬样本挖掘策略，有效地减少了物体边界处的伪影，进一步提升了分割质量。实验结果表明，UniC-Lift是一种高效且准确的3D实例分割方法。

## 🎯 应用场景

UniC-Lift在三维场景理解领域具有广泛的应用前景，例如机器人导航、自动驾驶、虚拟现实和增强现实。该方法可以用于构建更精确的三维场景模型，从而使机器人能够更好地理解周围环境并进行自主导航。此外，该方法还可以用于改善虚拟现实和增强现实体验，例如通过对场景中的物体进行精确分割，可以实现更逼真的交互效果。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) and Neural Radiance Fields (NeRF) have advanced novel-view synthesis. Recent methods extend multi-view 2D segmentation to 3D, enabling instance/semantic segmentation for better scene understanding. A key challenge is the inconsistency of 2D instance labels across views, leading to poor 3D predictions. Existing methods use a two-stage approach in which some rely on contrastive learning with hyperparameter-sensitive clustering, while others preprocess labels for consistency. We propose a unified framework that merges these steps, reducing training time and improving performance by introducing a learnable feature embedding for segmentation in Gaussian primitives. This embedding is then efficiently decoded into instance labels through a novel "Embedding-to-Label" process, effectively integrating the optimization. While this unified framework offers substantial benefits, we observed artifacts at the object boundaries. To address the object boundary issues, we propose hard-mining samples along these boundaries. However, directly applying hard mining to the feature embeddings proved unstable. Therefore, we apply a linear layer to the rasterized feature embeddings before calculating the triplet loss, which stabilizes training and significantly improves performance. Our method outperforms baselines qualitatively and quantitatively on the ScanNet, Replica3D, and Messy-Rooms datasets.

