---
layout: default
title: Block-wise Adaptive Caching for Accelerating Diffusion Policy
---

# Block-wise Adaptive Caching for Accelerating Diffusion Policy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13456" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13456v1</a>
  <a href="https://arxiv.org/pdf/2506.13456.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13456v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13456v1', 'Block-wise Adaptive Caching for Accelerating Diffusion Policy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kangye Ji, Yuan Meng, Hanyun Cui, Ye Li, Shengjia Hua, Lei Chen, Zhi Wang

**分类**: cs.AI, cs.RO

**发布日期**: 2025-06-16

---

## 💡 一句话要点

**提出块级自适应缓存方法以加速扩散策略**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散策略` `自适应缓存` `机器人控制` `推理加速` `特征重用` `错误传播` `变换器模型`

## 📋 核心要点

1. 现有的扩散加速技术未能有效适用于扩散策略，导致高计算成本限制了其实时应用。
2. 本文提出块级自适应缓存（BAC）方法，通过缓存中间动作特征来加速扩散策略，提升计算效率。
3. 在多个机器人基准测试中，BAC实现了最高3倍的推理加速，显著提升了扩散策略的实时性能。

## 📝 摘要（中文）

扩散策略在视觉运动建模方面展现了强大的能力，但其高计算成本使其在实时机器人控制中不够实用。现有的扩散加速技术未能有效适用于扩散策略，原因在于架构和数据的根本差异。本文提出块级自适应缓存（BAC）方法，通过缓存中间动作特征来加速扩散策略。BAC通过在块级别自适应更新和重用缓存特征，实现无损的动作生成加速。我们还提出自适应缓存调度器，以最大化缓存特征与跳过特征之间的全局相似性。然而，针对每个块应用该调度器会导致显著的错误传播。为此，我们开发了气泡联合算法，以在下游FFN之前更新上游块，从而减小错误。BAC作为一个无训练插件，可以与现有的基于变换器的扩散策略和视觉-语言-动作模型无缝集成。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散策略在实时机器人控制中的高计算成本问题。现有的扩散加速技术由于架构和数据的差异，无法有效应用于扩散策略，导致计算效率低下。

**核心思路**：论文的核心思路是通过块级自适应缓存（BAC）方法，缓存中间动作特征并在块级别自适应更新和重用这些特征，从而实现无损的动作生成加速。

**技术框架**：BAC的整体架构包括自适应缓存调度器和气泡联合算法两个主要模块。自适应缓存调度器用于识别最佳更新时刻，而气泡联合算法则用于减少错误传播。

**关键创新**：BAC的关键创新在于其块级特征缓存机制和错误传播的控制策略。与现有方法相比，BAC能够有效减少计算冗余并提高推理速度。

**关键设计**：BAC的设计包括自适应缓存调度器的参数设置，以最大化缓存特征与跳过特征之间的相似性，以及气泡联合算法的实现，以确保上游块在下游FFN之前更新，从而减少错误。

## 📊 实验亮点

在多个机器人基准测试中，BAC方法实现了最高3倍的推理速度提升，相较于基线方法表现出显著的性能优势。这一结果表明BAC在加速扩散策略方面的有效性，具有广泛的应用潜力。

## 🎯 应用场景

该研究的潜在应用场景包括实时机器人控制、自动驾驶、智能制造等领域。BAC方法的高效性和可集成性使其在需要快速决策和响应的场景中具有重要价值，未来可能推动更多智能系统的实时应用。

## 📄 摘要（原文）

> Diffusion Policy has demonstrated strong visuomotor modeling capabilities, but its high computational cost renders it impractical for real-time robotic control. Despite huge redundancy across repetitive denoising steps, existing diffusion acceleration techniques fail to generalize to Diffusion Policy due to fundamental architectural and data divergences. In this paper, we propose Block-wise Adaptive Caching(BAC), a method to accelerate Diffusion Policy by caching intermediate action features. BAC achieves lossless action generation acceleration by adaptively updating and reusing cached features at the block level, based on a key observation that feature similarities vary non-uniformly across timesteps and locks. To operationalize this insight, we first propose the Adaptive Caching Scheduler, designed to identify optimal update timesteps by maximizing the global feature similarities between cached and skipped features. However, applying this scheduler for each block leads to signiffcant error surges due to the inter-block propagation of caching errors, particularly within Feed-Forward Network (FFN) blocks. To mitigate this issue, we develop the Bubbling Union Algorithm, which truncates these errors by updating the upstream blocks with signiffcant caching errors before downstream FFNs. As a training-free plugin, BAC is readily integrable with existing transformer-based Diffusion Policy and vision-language-action models. Extensive experiments on multiple robotic benchmarks demonstrate that BAC achieves up to 3x inference speedup for free.

