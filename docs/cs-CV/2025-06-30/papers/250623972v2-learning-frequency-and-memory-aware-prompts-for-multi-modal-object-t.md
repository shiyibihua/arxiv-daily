---
layout: default
title: Learning Frequency and Memory-Aware Prompts for Multi-Modal Object Tracking
---

# Learning Frequency and Memory-Aware Prompts for Multi-Modal Object Tracking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23972" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23972v2</a>
  <a href="https://arxiv.org/pdf/2506.23972.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23972v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23972v2', 'Learning Frequency and Memory-Aware Prompts for Multi-Modal Object Tracking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boyue Xu, Ruichao Hou, Tongwei Ren, Dongming zhou, Gangshan Wu, Jinde Cao

**分类**: cs.CV

**发布日期**: 2025-06-30 (更新: 2025-10-01)

**🔗 代码/项目**: [GITHUB](https://github.com/xuboyue1999/mmtrack.git)

---

## 💡 一句话要点

**提出频率与记忆感知提示以解决多模态目标跟踪问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态跟踪` `频率感知` `记忆适配器` `视觉适配器` `时间一致性`

## 📋 核心要点

1. 现有的多模态跟踪方法未能充分利用模态特定的频率结构和长程时间依赖性，导致性能受限。
2. 本文提出的双适配器框架通过频率引导的视觉适配器和多级记忆适配器，增强了跨模态交互和时间一致性。
3. 在RGB-热成像、RGB-深度和RGB-事件基准上，实验结果显示该方法在性能上超越了现有的基线，且具有良好的参数效率。

## 📝 摘要（中文）

基于提示学习的多模态跟踪器通过使用轻量级视觉适配器将辅助模态线索注入冻结的基础模型，取得了显著进展。然而，它们仍然未能充分利用模态特定的频率结构和长程时间依赖性。本文提出了学习频率和记忆感知提示的双适配器框架，向冻结的RGB跟踪器注入轻量级提示。频率引导的视觉适配器通过联合校准空间、通道和频率分量，自适应地跨模态传递互补线索，缩小模态差距而无需完全微调。多级记忆适配器具有短期、长期和永久记忆存储，更新和检索可靠的时间上下文，实现跨帧的一致传播，并在遮挡、运动模糊和光照变化中实现稳健恢复。大量实验表明，在RGB-热成像、RGB-深度和RGB-事件基准上，该方法在参数效率和运行时间上均优于完全微调和基于适配器的基线。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态目标跟踪中模态特定频率结构和长程时间依赖性未被充分利用的问题。现有方法在处理遮挡、运动模糊和光照变化时表现不佳，限制了其应用效果。

**核心思路**：提出的学习频率和记忆感知提示框架通过引入频率引导的视觉适配器和多级记忆适配器，增强了不同模态之间的互补信息传递和时间上下文的保持，从而提高跟踪的鲁棒性和准确性。

**技术框架**：整体架构包含两个主要模块：频率引导的视觉适配器和多级记忆适配器。前者负责跨模态传递信息，后者则用于存储和检索时间上下文信息。

**关键创新**：最重要的创新在于引入了频率引导的适配器设计，使得模态间的互补信息能够在不完全微调的情况下有效传递。此外，多级记忆适配器的设计增强了时间一致性，显著提升了跟踪性能。

**关键设计**：在设计中，频率引导的适配器通过校准空间、通道和频率分量来实现信息的自适应传递。多级记忆适配器则通过短期、长期和永久记忆的结合，确保了时间上下文的有效更新与检索。

## 📊 实验亮点

实验结果表明，提出的方法在RGB-热成像、RGB-深度和RGB-事件基准上均取得了领先的状态，性能超越了完全微调和基于适配器的基线，具体提升幅度达到XX%。此外，该方法在参数效率和运行时间上表现优异，显示出良好的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、自动驾驶、增强现实等多模态交互场景。通过提高多模态目标跟踪的鲁棒性和准确性，该方法可以在复杂环境中实现更可靠的目标识别与跟踪，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Prompt-learning-based multi-modal trackers have made strong progress by using lightweight visual adapters to inject auxiliary-modality cues into frozen foundation models. However, they still underutilize two essentials: modality-specific frequency structure and long-range temporal dependencies. We present Learning Frequency and Memory-Aware Prompts, a dual-adapter framework that injects lightweight prompts into a frozen RGB tracker. A frequency-guided visual adapter adaptively transfers complementary cues across modalities by jointly calibrating spatial, channel, and frequency components, narrowing the modality gap without full fine-tuning. A multilevel memory adapter with short, long, and permanent memory stores, updates, and retrieves reliable temporal context, enabling consistent propagation across frames and robust recovery from occlusion, motion blur, and illumination changes. This unified design preserves the efficiency of prompt learning while strengthening cross-modal interaction and temporal coherence. Extensive experiments on RGB-Thermal, RGB-Depth, and RGB-Event benchmarks show consistent state-of-the-art results over fully fine-tuned and adapter-based baselines, together with favorable parameter efficiency and runtime. Code and models are available at https://github.com/xuboyue1999/mmtrack.git.

