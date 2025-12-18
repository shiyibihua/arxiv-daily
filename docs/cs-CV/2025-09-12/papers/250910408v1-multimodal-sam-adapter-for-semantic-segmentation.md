---
layout: default
title: Multimodal SAM-adapter for Semantic Segmentation
---

# Multimodal SAM-adapter for Semantic Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10408" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10408v1</a>
  <a href="https://arxiv.org/pdf/2509.10408.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10408v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10408v1', 'Multimodal SAM-adapter for Semantic Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Iacopo Curti, Pierluigi Zama Ramirez, Alioscia Petrelli, Luigi Di Stefano

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-12

**🔗 代码/项目**: [GITHUB](https://github.com/iacopo97/Multimodal-SAM-Adapter)

---

## 💡 一句话要点

**提出MM SAM-adapter，用于提升多模态语义分割在复杂环境下的鲁棒性。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语义分割` `多模态融合` `Segment Anything Model` `Adapter网络` `鲁棒性` `自动驾驶` `深度学习`

## 📋 核心要点

1. 现有语义分割方法在复杂环境下表现不佳，如光照不足、遮挡和恶劣天气等。
2. MM SAM-adapter通过adapter网络将融合的多模态特征注入SAM，提升模型对复杂环境的适应性。
3. 在DeLiVER、FMB和MUSES数据集上，MM SAM-adapter取得了state-of-the-art的性能。

## 📝 摘要（中文）

语义分割是计算机视觉中的关键任务，在自动驾驶、医学成像和机器人等领域有着广泛的应用。尽管深度学习取得了显著进展，但现有方法在光照不足、遮挡和恶劣天气等复杂条件下仍然脆弱。为了解决这些局限性，最近出现了集成辅助传感器数据（如LiDAR、红外）的多模态方法，它们提供互补信息以增强鲁棒性。本文提出了MM SAM-adapter，这是一个新颖的框架，扩展了Segment Anything Model (SAM)在多模态语义分割方面的能力。该方法采用adapter网络，将融合的多模态特征注入到SAM丰富的RGB特征中。这种设计使模型能够保持RGB特征强大的泛化能力，同时仅在辅助模态提供额外线索时才选择性地合并它们。因此，MM SAM-adapter实现了多模态信息的平衡和有效利用。我们在DeLiVER、FMB和MUSES三个具有挑战性的基准上评估了我们的方法，MM SAM-adapter实现了最先进的性能。为了进一步分析模态贡献，我们将DeLiVER和FMB划分为RGB-easy和RGB-hard子集。结果一致表明，我们的框架在有利和不利条件下均优于竞争方法，突出了多模态自适应在鲁棒场景理解方面的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决语义分割在复杂环境下的鲁棒性问题。现有方法在光照不足、遮挡和恶劣天气等情况下表现不佳，无法充分利用多模态数据提供的互补信息。

**核心思路**：论文的核心思路是利用Segment Anything Model (SAM)强大的泛化能力，并通过一个adapter网络将多模态信息选择性地融入SAM的RGB特征中。这样既能保留SAM在RGB图像上的优势，又能利用其他模态的信息来提升在复杂环境下的性能。

**技术框架**：MM SAM-adapter的整体架构包括：1) RGB图像输入SAM；2) 其他模态数据（如LiDAR、红外）进行特征提取；3) 多模态特征融合；4) Adapter网络将融合后的特征注入SAM的图像特征中；5) SAM进行语义分割预测。

**关键创新**：关键创新在于使用adapter网络将多模态信息注入SAM。这种方式避免了直接从头训练一个多模态分割模型，而是利用了SAM预训练的强大能力，并通过adapter网络进行微调，从而更有效地利用多模态信息。

**关键设计**：Adapter网络的设计是关键。具体结构未知，但其目标是学习一个映射，将融合的多模态特征转换为与SAM的RGB特征兼容的形式，并选择性地融合这些特征。损失函数用于优化adapter网络，使其能够有效地利用多模态信息来提升分割性能。具体的融合方式和adapter网络结构在论文中可能有所描述，但摘要中未提及。

## 📊 实验亮点

MM SAM-adapter在DeLiVER、FMB和MUSES三个数据集上取得了state-of-the-art的性能。通过将数据集划分为RGB-easy和RGB-hard子集，验证了该方法在复杂环境下的有效性。结果表明，MM SAM-adapter在各种条件下均优于现有方法，证明了多模态自适应在鲁棒场景理解方面的优势。

## 🎯 应用场景

该研究成果可广泛应用于自动驾驶、机器人、医学图像分析等领域。在自动驾驶中，可以提高车辆在恶劣天气和光照条件下的环境感知能力。在机器人领域，可以增强机器人在复杂环境下的导航和操作能力。在医学图像分析中，可以辅助医生进行更准确的病灶分割和诊断。

## 📄 摘要（原文）

> Semantic segmentation, a key task in computer vision with broad applications in autonomous driving, medical imaging, and robotics, has advanced substantially with deep learning. Nevertheless, current approaches remain vulnerable to challenging conditions such as poor lighting, occlusions, and adverse weather. To address these limitations, multimodal methods that integrate auxiliary sensor data (e.g., LiDAR, infrared) have recently emerged, providing complementary information that enhances robustness. In this work, we present MM SAM-adapter, a novel framework that extends the capabilities of the Segment Anything Model (SAM) for multimodal semantic segmentation. The proposed method employs an adapter network that injects fused multimodal features into SAM's rich RGB features. This design enables the model to retain the strong generalization ability of RGB features while selectively incorporating auxiliary modalities only when they contribute additional cues. As a result, MM SAM-adapter achieves a balanced and efficient use of multimodal information. We evaluate our approach on three challenging benchmarks, DeLiVER, FMB, and MUSES, where MM SAM-adapter delivers state-of-the-art performance. To further analyze modality contributions, we partition DeLiVER and FMB into RGB-easy and RGB-hard subsets. Results consistently demonstrate that our framework outperforms competing methods in both favorable and adverse conditions, highlighting the effectiveness of multimodal adaptation for robust scene understanding. The code is available at the following link: https://github.com/iacopo97/Multimodal-SAM-Adapter.

