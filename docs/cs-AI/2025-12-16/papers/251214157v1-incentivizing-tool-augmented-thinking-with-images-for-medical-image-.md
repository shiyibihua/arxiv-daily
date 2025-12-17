---
layout: default
title: Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis
---

# Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14157" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14157v1</a>
  <a href="https://arxiv.org/pdf/2512.14157.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14157v1" onclick="toggleFavorite(this, '2512.14157v1', 'Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yankai Jiang, Yujie Zhang, Peng Zhang, Yichen Li, Jintai Chen, Xiaoming Shi, Shihui Zhen

**分类**: cs.AI, cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出Ophiuchus框架以增强医学图像分析中的工具辅助推理**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学图像分析` `多模态大语言模型` `工具增强推理` `动态视觉关注` `反思微调` `强化学习` `诊断辅助`

## 📋 核心要点

1. 现有的医学多模态大语言模型在复杂任务中表现不佳，尤其是在需要细粒度视觉关注的情况下。
2. Ophiuchus框架通过工具增强推理，能够动态决定何时需要额外视觉证据，并有效整合相关信息。
3. 实验结果显示，Ophiuchus在VQA、检测和基于推理的分割等多项医学基准测试中均优于现有方法。

## 📝 摘要（中文）

近年来，基于推理的医学多模态大语言模型（MLLMs）在生成逐步文本推理链方面取得了一定进展。然而，它们在处理复杂任务时仍面临挑战，尤其是在需要动态和迭代关注细粒度视觉区域以实现精确定位和诊断的情况下。为此，本文提出了Ophiuchus，一个多功能的工具增强框架，使MLLM能够决定何时需要额外的视觉证据、确定在医学图像中探测和定位的区域，并将相关子图像内容无缝融入多模态推理链中。Ophiuchus通过整合模型的固有定位和感知能力与外部工具，促进了更高层次的推理。实验结果表明，Ophiuchus在多个医学基准测试中持续超越现有的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有医学多模态大语言模型在复杂任务中动态和迭代关注细粒度视觉区域的不足，导致精确定位和诊断能力不足的问题。

**核心思路**：Ophiuchus框架通过工具增强推理，允许模型在需要时主动获取额外的视觉证据，并将其与文本推理链结合，从而提升推理能力。

**技术框架**：Ophiuchus的整体架构包括三个主要阶段：冷启动训练、反思微调和工具强化学习。冷启动训练使用工具集成的推理数据以实现基本的工具选择和适应；反思微调阶段强化反思推理，鼓励模型重新审视工具输出；最后，工具强化学习阶段直接优化任务特定奖励，模拟专家级诊断行为。

**关键创新**：Ophiuchus的主要创新在于其三阶段训练策略，特别是将工具集成与模型的固有能力结合，突破了以往方法对专用工具性能的限制。

**关键设计**：在训练过程中，采用了特定的损失函数以优化工具选择的准确性，并设计了适应性网络结构以支持多模态信息的融合。

## 📊 实验亮点

Ophiuchus在多个医学基准测试中表现优异，尤其是在VQA、检测和基于推理的分割任务中，均超越了现有的闭源和开源最先进方法，展示了显著的性能提升，具体提升幅度未知。

## 🎯 应用场景

Ophiuchus框架在医学图像分析领域具有广泛的应用潜力，能够帮助医生在复杂的诊断过程中更有效地利用视觉信息。其工具增强的推理能力将推动医学人工智能的发展，提升临床决策的准确性和效率，未来可能在远程医疗和辅助诊断系统中发挥重要作用。

## 📄 摘要（原文）

> Recent reasoning based medical MLLMs have made progress in generating step by step textual reasoning chains. However, they still struggle with complex tasks that necessitate dynamic and iterative focusing on fine-grained visual regions to achieve precise grounding and diagnosis. We introduce Ophiuchus, a versatile, tool-augmented framework that equips an MLLM to (i) decide when additional visual evidence is needed, (ii) determine where to probe and ground within the medical image, and (iii) seamlessly weave the relevant sub-image content back into an interleaved, multimodal chain of thought. In contrast to prior approaches limited by the performance ceiling of specialized tools, Ophiuchus integrates the model's inherent grounding and perception capabilities with external tools, thereby fostering higher-level reasoning. The core of our method is a three-stage training strategy: cold-start training with tool-integrated reasoning data to achieve basic tool selection and adaptation for inspecting key regions; self-reflection fine-tuning to strengthen reflective reasoning and encourage revisiting tool outputs; and Agentic Tool Reinforcement Learning to directly optimize task-specific rewards and emulate expert-like diagnostic behavior. Extensive experiments show that Ophiuchus consistently outperforms both closed-source and open-source SOTA methods across diverse medical benchmarks, including VQA, detection, and reasoning-based segmentation. Our approach illuminates a path toward medical AI agents that can genuinely "think with images" through tool-integrated reasoning. Datasets, codes, and trained models will be released publicly.

