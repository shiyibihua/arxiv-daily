---
layout: default
title: MoLT: Mixture of Layer-Wise Tokens for Efficient Audio-Visual Learning
---

# MoLT: Mixture of Layer-Wise Tokens for Efficient Audio-Visual Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.00115" target="_blank" class="toolbar-btn">arXiv: 2512.00115v1</a>
    <a href="https://arxiv.org/pdf/2512.00115.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00115v1" 
            onclick="toggleFavorite(this, '2512.00115v1', 'MoLT: Mixture of Layer-Wise Tokens for Efficient Audio-Visual Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kyeongha Rho, Hyeongkeun Lee, Jae Won Cho, Joon Son Chung

**分类**: cs.SD, cs.CV, cs.MM

**发布日期**: 2025-11-27

**备注**: 10 pages, 5 figures

---

## 💡 一句话要点

**提出MoLT，通过混合层级Token实现高效的音视频学习。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `音视频学习` `多模态融合` `Transformer` `自适应学习` `层级Token`

## 📋 核心要点

1. 现有音视频学习方法在Transformer的每一层进行串行自适应，计算量大，效率低。
2. MoLT通过并行的轻量级方案，仅从Transformer的后期层提取和融合层级Token，实现高效自适应。
3. 实验表明，MoLT在音视频问答、分割和事件定位等任务上优于现有方法，同时保持参数和内存效率。

## 📝 摘要（中文）

本文提出了一种名为混合层级Token（MoLT）的参数和内存高效的音视频学习自适应框架。MoLT的核心思想是用并行的轻量级方案取代传统Transformer中计算量大的串行自适应，该方案仅从后期的Transformer层提取和融合层级Token。我们采用两种类型的适配器，将模态特定信息和跨模态交互提炼成紧凑的潜在Token。然后，Token融合模块通过考虑它们的相对重要性来动态地融合这些层级Token。为了防止潜在Token的冗余，我们在训练期间对潜在Token应用正交正则化。通过对预训练Transformer中自适应位置的系统分析，我们仅从Transformer的后期层提取潜在Token。这种策略性的自适应方法避免了来自易失的早期层特征的误差传播，从而在保持参数和内存效率的同时，最大化了自适应性能。通过大量的实验，我们证明了MoLT在各种音视频基准测试中优于现有方法，包括音视频问答、音视频分割和音视频事件定位。

## 🔬 方法详解

**问题定义**：现有音视频学习方法通常在Transformer的每一层进行串行自适应，导致计算量大、参数效率低，难以部署到资源受限的设备上。此外，早期层的特征可能不稳定，容易导致误差传播，影响最终性能。

**核心思路**：MoLT的核心思路是采用一种并行的、轻量级的自适应方案，仅从Transformer的后期层提取和融合层级Token。通过这种方式，可以避免对每一层都进行复杂的计算，同时利用后期层更稳定的特征，从而提高效率和性能。

**技术框架**：MoLT的整体架构包含以下几个主要模块：1) 模态特定适配器：用于提取音频和视频模态的特定信息，并将其转换为紧凑的潜在Token。2) 跨模态交互适配器：用于捕捉音频和视频模态之间的交互信息，并将其转换为潜在Token。3) Token融合模块：用于动态地融合来自不同层的潜在Token，该模块会根据Token的相对重要性进行加权融合。4) 正交正则化：用于防止潜在Token的冗余，提高模型的泛化能力。

**关键创新**：MoLT的关键创新在于其混合层级Token的提取和融合机制。与传统的串行自适应方法不同，MoLT采用并行的轻量级方案，仅从Transformer的后期层提取Token，从而显著降低了计算复杂度。此外，Token融合模块能够动态地调整不同层Token的权重，从而更好地利用不同层的信息。

**关键设计**：MoLT的关键设计包括：1) 适配器的类型和数量：论文采用了两种类型的适配器，分别用于提取模态特定信息和跨模态交互信息。2) Token融合模块的权重计算方式：论文采用了一种基于注意力的机制来计算Token的权重。3) 正交正则化的强度：论文通过实验确定了正交正则化的最佳强度。

## 📊 实验亮点

实验结果表明，MoLT在音视频问答、音视频分割和音视频事件定位等任务上均取得了显著的性能提升。例如，在Audio-Visual Question Answering任务上，MoLT的性能优于现有方法，并且参数量更少。这些结果证明了MoLT的有效性和高效性。

## 🎯 应用场景

MoLT具有广泛的应用前景，例如视频会议中的语音增强、智能监控中的事件检测、以及自动驾驶中的环境感知。该方法可以部署在资源受限的设备上，实现高效的音视频处理，具有重要的实际应用价值和商业潜力。

## 📄 摘要（原文）

> In this paper, we propose Mixture of Layer-Wise Tokens (MoLT), a parameter- and memory-efficient adaptation framework for audio-visual learning. The key idea of MoLT is to replace conventional, computationally heavy sequential adaptation at every transformer layer with a parallel, lightweight scheme that extracts and fuses layer-wise tokens only from the late layers. We adopt two types of adapters to distill modality-specific information and cross-modal interaction into compact latent tokens in a layer-wise manner. A token fusion module then dynamically fuses these layer-wise tokens by taking into account their relative significance. To prevent the redundancy of latent tokens, we apply an orthogonality regularization between latent tokens during training. Through the systematic analysis of the position of adaptation in the pre-trained transformers, we extract latent tokens only from the late layers of the transformers. This strategic adaptation approach avoids error propagation from the volatile early-layer features, thereby maximizing the adaptation performance while maintaining parameter and memory efficiency. Through extensive experiments, we demonstrate that MoLT outperforms existing methods on diverse audio-visual benchmarks, including Audio-Visual Question Answering, Audio-Visual Segmentation, and Audio-Visual Event Localization.

