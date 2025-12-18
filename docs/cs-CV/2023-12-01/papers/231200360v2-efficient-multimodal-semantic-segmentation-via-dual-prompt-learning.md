---
layout: default
title: Efficient Multimodal Semantic Segmentation via Dual-Prompt Learning
---

# Efficient Multimodal Semantic Segmentation via Dual-Prompt Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00360" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00360v2</a>
  <a href="https://arxiv.org/pdf/2312.00360.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00360v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00360v2', 'Efficient Multimodal Semantic Segmentation via Dual-Prompt Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaohua Dong, Yunhe Feng, Qing Yang, Yan Huang, Dongfang Liu, Heng Fan

**分类**: cs.CV

**发布日期**: 2023-12-01 (更新: 2023-12-04)

**备注**: 11 pages, 4 figures, 9 tables

---

## 💡 一句话要点

**提出DPLNet以解决多模态语义分割训练效率低的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `语义分割` `深度学习` `轻量级模型` `特征适配` `提示学习` `计算机视觉`

## 📋 核心要点

1. 现有的多模态语义分割方法通常需要对复杂的双分支框架进行全面微调，导致训练成本高且效率低。
2. 本文提出DPLNet，通过引入轻量级的多模态提示生成器和特征适配器，直接适应冻结的预训练模型以提高训练效率。
3. DPLNet在多个数据集上实现了新的最先进性能，且仅引入了少量的可训练参数，展示了其在多模态任务中的广泛适用性。

## 📝 摘要（中文）

多模态（如RGB-深度/RGB-热成像）融合在复杂场景（如室内/低光照条件）下的语义分割中展现出巨大潜力。现有方法通常需要对双分支编码器-解码器框架进行全面微调，导致训练成本高昂。为了解决这一问题，本文提出了一种简单而有效的双提示学习网络（DPLNet），通过直接适应冻结的预训练RGB模型来实现多模态语义分割，从而减少参数更新。DPLNet的核心在于引入了多模态提示生成器（MPG）和多模态特征适配器（MFA），这两个模块轻量且仅引入少量可训练参数。实验结果表明，DPLNet在四个RGB-D/T语义分割数据集上达到了新的最先进性能，并且在其他多模态任务中也表现出色。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态语义分割中的训练效率低下问题。现有方法通常需要对复杂的双分支编码器-解码器框架进行全面微调，导致训练成本高昂且参数更新量大。

**核心思路**：DPLNet的核心思路是通过直接适应冻结的预训练RGB模型来实现多模态语义分割，减少了需要更新的参数数量。通过引入多模态提示生成器（MPG）和多模态特征适配器（MFA），DPLNet能够有效融合不同模态的特征。

**技术框架**：DPLNet的整体架构包括两个主要模块：多模态提示生成器（MPG）和多模态特征适配器（MFA）。MPG负责在不同深度阶段生成多层次的多模态提示，并将其注入到冻结的主干网络中，而MFA则适应这些提示以优化多模态特征的学习。

**关键创新**：DPLNet的最重要创新在于其轻量级设计，仅引入了3.88M的可训练参数（占预训练主干参数的4.4%），显著降低了训练成本，同时保持了良好的性能。与现有复杂方法相比，DPLNet在参数效率上具有明显优势。

**关键设计**：DPLNet采用简单的解码器（3.27M参数），并通过轻量级的MPG和MFA模块实现特征融合和学习。损失函数和网络结构设计上，DPLNet没有特别的设计，使其在多模态任务中表现出色。

## 📊 实验亮点

DPLNet在四个RGB-D/T语义分割数据集上实现了新的最先进性能，且与其他复杂方法相比，参数效率显著提高。具体而言，DPLNet在保持较低参数量的同时，达到了与现有方法相当或更好的性能，展示了其在多模态任务中的广泛适用性。

## 🎯 应用场景

DPLNet在多模态语义分割中的成功应用表明其在其他相关任务中的潜力，如显著目标检测和视频语义分割。其高效的训练方式和较低的参数需求使其在实际应用中具有较高的价值，尤其是在资源受限的环境中。未来，DPLNet的设计理念可能会推动更多轻量级模型的开发，促进多模态学习的广泛应用。

## 📄 摘要（原文）

> Multimodal (e.g., RGB-Depth/RGB-Thermal) fusion has shown great potential for improving semantic segmentation in complex scenes (e.g., indoor/low-light conditions). Existing approaches often fully fine-tune a dual-branch encoder-decoder framework with a complicated feature fusion strategy for achieving multimodal semantic segmentation, which is training-costly due to the massive parameter updates in feature extraction and fusion. To address this issue, we propose a surprisingly simple yet effective dual-prompt learning network (dubbed DPLNet) for training-efficient multimodal (e.g., RGB-D/T) semantic segmentation. The core of DPLNet is to directly adapt a frozen pre-trained RGB model to multimodal semantic segmentation, reducing parameter updates. For this purpose, we present two prompt learning modules, comprising multimodal prompt generator (MPG) and multimodal feature adapter (MFA). MPG works to fuse the features from different modalities in a compact manner and is inserted from shadow to deep stages to generate the multi-level multimodal prompts that are injected into the frozen backbone, while MPG adapts prompted multimodal features in the frozen backbone for better multimodal semantic segmentation. Since both the MPG and MFA are lightweight, only a few trainable parameters (3.88M, 4.4% of the pre-trained backbone parameters) are introduced for multimodal feature fusion and learning. Using a simple decoder (3.27M parameters), DPLNet achieves new state-of-the-art performance or is on a par with other complex approaches on four RGB-D/T semantic segmentation datasets while satisfying parameter efficiency. Moreover, we show that DPLNet is general and applicable to other multimodal tasks such as salient object detection and video semantic segmentation. Without special design, DPLNet outperforms many complicated models. Our code will be available at github.com/ShaohuaDong2021/DPLNet.

