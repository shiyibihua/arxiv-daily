---
layout: default
title: Training-Free Token Pruning via Zeroth-Order Gradient Estimation in Vision-Language Models
---

# Training-Free Token Pruning via Zeroth-Order Gradient Estimation in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24837" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24837v1</a>
  <a href="https://arxiv.org/pdf/2509.24837.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24837v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24837v1', 'Training-Free Token Pruning via Zeroth-Order Gradient Estimation in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youngeun Kim, Youjia Zhang, Huiling Liu, Aecheon Jung, Sunwoo Lee, Sungeun Hong

**分类**: cs.CV

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出训练无关的令牌修剪方法以降低视觉语言模型的推理成本**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `令牌修剪` `多模态推理` `零阶梯度估计` `推理效率` `敏感性评估` `计算机视觉` `深度学习`

## 📋 核心要点

1. 现有的令牌修剪方法在处理冗余视觉令牌时面临稳定性和准确性的问题，导致推理效率低下。
2. 本文提出了一种基于零阶梯度估计的训练无关令牌修剪方法，利用令牌的敏感性来选择对模型输出影响较大的令牌。
3. 实验结果显示，所提方法在多个视觉语言模型上均优于现有方法，能够修剪高达94.4%的令牌，同时提升推理速度至2.30倍。

## 📝 摘要（中文）

大型视觉语言模型（VLMs）在多模态推理中表现出色，但由于冗余视觉令牌导致的推理成本较高，成为了一个主要问题。现有的令牌修剪方法存在局限性，基于注意力的方法依赖于不稳定的原始注意力分数，而基于多样性的方法则可能丢失重要信息。本文提出了一种训练无关的框架，基于简单的直觉：敏感性高的令牌更可能影响模型输出，并应捕获互补的视觉线索。通过在投影层使用零阶扰动估计令牌敏感性，本文的方法能够在不进行反向传播的情况下，通过轻量级的前向传递来近似每个令牌的影响。实验表明，该方法在多个VLM和基准测试中表现优异，最多可修剪94.4%的令牌，同时保持准确性，并显著提高效率，推理速度比基线快2.30倍。

## 🔬 方法详解

**问题定义**：本文旨在解决大型视觉语言模型中由于冗余视觉令牌导致的高推理成本问题。现有方法在选择令牌时存在不稳定性和信息丢失的风险，影响了模型的性能和效率。

**核心思路**：本文提出的框架基于令牌敏感性进行修剪，认为敏感性高的令牌更能影响模型输出，并且应当捕获互补的视觉信息而非重叠信息。

**技术框架**：该方法主要包括两个阶段：首先在投影层进行零阶扰动估计，以评估每个令牌的敏感性；其次根据敏感性选择令牌进行修剪，最终形成优化的令牌集合。

**关键创新**：最重要的创新在于采用零阶扰动估计来评估令牌的敏感性，这一方法避免了传统方法中对注意力分数的依赖，提供了更为稳定和有效的令牌选择机制。

**关键设计**：在技术细节上，本文设计了轻量级的前向传递过程，以实现对令牌敏感性的快速估计，避免了复杂的反向传播过程，确保了高效性和可扩展性。通过这种设计，能够在多个视觉语言模型上实现显著的性能提升。

## 📊 实验亮点

实验结果表明，所提方法在多个视觉语言模型上均表现优异，能够修剪高达94.4%的令牌，同时保持模型的准确性，并实现推理速度提升至基线的2.30倍，显著提高了推理效率。

## 🎯 应用场景

该研究的潜在应用领域包括图像和文本的联合理解、智能搜索引擎、自动图像描述生成等。通过提高视觉语言模型的推理效率，该方法能够在实际应用中降低计算成本，提升用户体验，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large Vision-Language Models (VLMs) enable strong multimodal reasoning but incur heavy inference costs from redundant visual tokens. Token pruning alleviates this issue, yet existing approaches face limitations. Attention-based methods rely on raw attention scores, which are often unstable across layers and heads and can lead to redundant selections. Diversity-based methods improve robustness by selecting tokens far apart in feature space but risk dropping regions needed for accurate prediction. We propose \ours, a training-free framework built on a simple intuition: tokens with higher sensitivity are more likely to influence the model's output, and they should also capture complementary visual cues rather than overlapping information. To achieve this, we estimate token sensitivity using zeroth-order perturbations at the projection layer, a shallow and computationally light component of the model. This approach measures how small random perturbations affect the projection outputs, allowing us to approximate each token's influence through lightweight forward passes without backpropagation. Extensive experiments across multiple VLMs and benchmarks show that \ours consistently outperforms prior methods, pruning up to 94.4\% of tokens while maintaining accuracy and significantly improving efficiency, achieving up to 2.30x faster end-to-end inference over the baseline.

