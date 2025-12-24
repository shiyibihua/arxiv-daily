---
layout: default
title: Scene-Agnostic Traversability Labeling and Estimation via a Multimodal Self-supervised Framework
---

# Scene-Agnostic Traversability Labeling and Estimation via a Multimodal Self-supervised Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18249" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18249v1</a>
  <a href="https://arxiv.org/pdf/2508.18249.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18249v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18249v1', 'Scene-Agnostic Traversability Labeling and Estimation via a Multimodal Self-supervised Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zipeng Fang, Yanbo Wang, Lei Zhao, Weidong Chen

**分类**: cs.RO, cs.CV

**发布日期**: 2025-08-25

---

## 💡 一句话要点

**提出多模态自监督框架以解决可通行性估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可通行性估计` `自监督学习` `多模态融合` `激光雷达` `机器人导航`

## 📋 核心要点

1. 现有自监督学习方法在捕捉不可通行区域特征方面存在不足，且多集中于单一模态。
2. 本文提出的多模态自监督框架通过整合多种传感器数据，提升了可通行性标注和估计的准确性。
3. 实验结果显示，所提方法在多个数据集上实现了约88%的IoU，相较于现有方法提升了1.6-3.5%。

## 📝 摘要（中文）

可通行性估计对于使机器人能够在多样化的地形和环境中导航至关重要。尽管近期的自监督学习方法取得了良好的效果，但它们往往无法捕捉不可通行区域的特征。此外，大多数先前的研究集中于单一模态，忽视了整合异构传感器模态所带来的互补优势。为了解决这些局限性，本文提出了一种多模态自监督框架用于可通行性标注和估计。首先，我们的标注流程整合了足迹、激光雷达和相机数据，生成考虑语义和几何线索的可通行性标签。然后，利用这些标签，我们训练了一个双流网络，以解耦的方式共同学习不同模态，增强其识别多样化可通行性模式的能力。最后，在城市、越野和校园环境中进行的广泛实验表明了我们方法的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有可通行性估计方法无法有效捕捉不可通行区域特征的问题，且大多数方法仅依赖单一模态，导致估计结果的鲁棒性不足。

**核心思路**：提出一种多模态自监督框架，通过整合足迹、激光雷达和相机数据，生成更全面的可通行性标签，从而提升模型对多样化地形的适应能力。

**技术框架**：整体架构包括数据标注流程和双流网络。标注流程整合不同模态数据生成标签，双流网络则解耦学习不同模态的信息，以增强对可通行性模式的识别能力。

**关键创新**：最重要的创新在于引入多模态数据的整合与自监督学习的结合，显著提升了对复杂环境中可通行性区域的识别能力，与传统单模态方法相比，具有更高的准确性和鲁棒性。

**关键设计**：在网络结构上，采用双流网络设计，分别处理不同模态数据；损失函数设计上，结合稀疏激光雷达监督以减少伪标签引入的噪声，确保模型学习的准确性。

## 📊 实验亮点

实验结果表明，所提自动标注方法在多个数据集上实现了约88%的IoU，相较于现有自监督最先进方法，所提多模态可通行性估计网络在所有评估数据集上均提升了1.6-3.5%的IoU，显示出显著的性能优势。

## 🎯 应用场景

该研究的潜在应用领域包括自主导航机器人、无人驾驶汽车和智能城市基础设施等。通过提升可通行性估计的准确性，能够显著增强机器人在复杂环境中的导航能力，推动相关技术的实际应用和发展。未来，该方法有望在更广泛的场景中得到应用，促进智能交通和自动化系统的进步。

## 📄 摘要（原文）

> Traversability estimation is critical for enabling robots to navigate across diverse terrains and environments. While recent self-supervised learning methods achieve promising results, they often fail to capture the characteristics of non-traversable regions. Moreover, most prior works concentrate on a single modality, overlooking the complementary strengths offered by integrating heterogeneous sensory modalities for more robust traversability estimation. To address these limitations, we propose a multimodal self-supervised framework for traversability labeling and estimation. First, our annotation pipeline integrates footprint, LiDAR, and camera data as prompts for a vision foundation model, generating traversability labels that account for both semantic and geometric cues. Then, leveraging these labels, we train a dual-stream network that jointly learns from different modalities in a decoupled manner, enhancing its capacity to recognize diverse traversability patterns. In addition, we incorporate sparse LiDAR-based supervision to mitigate the noise introduced by pseudo labels. Finally, extensive experiments conducted across urban, off-road, and campus environments demonstrate the effectiveness of our approach. The proposed automatic labeling method consistently achieves around 88% IoU across diverse datasets. Compared to existing self-supervised state-of-the-art methods, our multimodal traversability estimation network yields consistently higher IoU, improving by 1.6-3.5% on all evaluated datasets.

