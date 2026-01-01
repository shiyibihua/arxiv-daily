---
layout: default
title: Understanding and Steering the Cognitive Behaviors of Reasoning Models at Test-Time
---

# Understanding and Steering the Cognitive Behaviors of Reasoning Models at Test-Time

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24574" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24574v1</a>
  <a href="https://arxiv.org/pdf/2512.24574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24574v1', 'Understanding and Steering the Cognitive Behaviors of Reasoning Models at Test-Time')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenyu Zhang, Xiaoxia Wu, Zhongzhu Zhou, Qingyang Wu, Yineng Zhang, Pragaash Ponnusamy, Harikaran Subbaraj, Jue Wang, Shuaiwen Leon Song, Ben Athiwaratkun

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**提出CREST，通过干预注意力头引导LLM推理，提升效率和准确率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `链式推理` `注意力机制` `认知引导` `测试时干预`

## 📋 核心要点

1. 现有LLM推理过程存在效率问题，表现为token生成过多、推理不稳定，在欠思考和过度思考间切换。
2. CREST通过离线校准识别与特定认知行为相关的注意力头，并在推理时干预这些头，抑制低效行为。
3. 实验表明，CREST在提升准确率的同时，显著降低了token使用量，实现了更高效可靠的推理。

## 📝 摘要（中文）

大型语言模型(LLM)通常依赖于长链思维(CoT)推理来解决复杂任务。虽然有效，但这些轨迹常常效率低下，导致过多的token生成带来的高延迟，或不稳定的推理，在欠思考(浅薄、不一致的步骤)和过度思考(重复、冗长的推理)之间交替。本文研究了推理轨迹的结构，并发现了与验证和回溯等不同认知行为相关的特定注意力头。通过在推理时对这些头进行轻微干预，我们可以引导模型远离低效模式。基于此，我们提出了CREST，一种用于测试时认知推理引导的无训练方法。CREST包含两个部分：(1)离线校准步骤，用于识别认知头并导出特定于头的引导向量；(2)推理时程序，用于旋转隐藏表示以抑制沿这些向量的分量。CREST自适应地抑制了无益的推理行为，从而提高了准确性并降低了计算成本。在不同的推理基准和模型上，CREST将准确率提高了高达17.5%，同时减少了37.6%的token使用量，为更快、更可靠的LLM推理提供了一种简单有效的途径。

## 🔬 方法详解

**问题定义**：现有大型语言模型在进行复杂推理时，依赖于链式思维(CoT)，但推理过程常常效率低下。具体表现为：生成过多的token导致高延迟；推理过程不稳定，在浅薄的欠思考和冗余的过度思考之间摇摆。这些问题限制了LLM在实际应用中的性能和效率。

**核心思路**：论文的核心思路是，通过分析推理轨迹的结构，发现与特定认知行为（如验证、回溯）相关的注意力头。然后，在推理过程中，对这些注意力头进行干预，抑制模型产生低效的推理行为。这种方法无需额外的训练，可以在测试时直接应用，从而提高推理效率和准确率。

**技术框架**：CREST包含两个主要阶段：离线校准阶段和推理时引导阶段。在离线校准阶段，首先分析推理轨迹，识别与特定认知行为相关的注意力头，并为每个头计算一个引导向量。在推理时引导阶段，对于每个推理步骤，CREST旋转隐藏层表示，以抑制沿着引导向量方向的分量，从而抑制与该向量相关的认知行为。

**关键创新**：CREST的关键创新在于，它提出了一种无需训练的测试时认知推理引导方法。通过分析注意力头与认知行为之间的关联，实现了对LLM推理过程的细粒度控制。与传统的微调或提示工程方法相比，CREST更加轻量级，易于部署，并且能够自适应地抑制不必要的推理行为。

**关键设计**：CREST的关键设计包括：(1)认知头的识别方法，通过分析注意力权重与特定认知行为之间的相关性来确定；(2)引导向量的计算方法，基于校准数据，计算每个认知头的引导向量，用于在推理时抑制相应的认知行为；(3)隐藏层表示的旋转方法，通过旋转隐藏层表示，抑制沿着引导向量方向的分量，从而实现对认知行为的干预。具体旋转操作通常使用正交投影或类似的线性变换。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24574v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24574v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24574v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，CREST在多个推理基准测试中显著提高了LLM的性能。例如，在某些任务上，CREST将准确率提高了高达17.5%，同时减少了37.6%的token使用量。这些结果表明，CREST是一种简单而有效的LLM推理优化方法，具有很强的实用价值。

## 🎯 应用场景

CREST可应用于各种需要复杂推理的场景，例如问答系统、代码生成、数学问题求解等。通过提高推理效率和准确率，CREST可以降低LLM的使用成本，并提升用户体验。未来，该方法有望扩展到其他类型的认知任务，并与其他推理优化技术相结合，进一步提升LLM的性能。

## 📄 摘要（原文）

> Large Language Models (LLMs) often rely on long chain-of-thought (CoT) reasoning to solve complex tasks. While effective, these trajectories are frequently inefficient, leading to high latency from excessive token generation, or unstable reasoning that alternates between underthinking (shallow, inconsistent steps) and overthinking (repetitive, verbose reasoning). In this work, we study the structure of reasoning trajectories and uncover specialized attention heads that correlate with distinct cognitive behaviors such as verification and backtracking. By lightly intervening on these heads at inference time, we can steer the model away from inefficient modes. Building on this insight, we propose CREST, a training-free method for Cognitive REasoning Steering at Test-time. CREST has two components: (1) an offline calibration step that identifies cognitive heads and derives head-specific steering vectors, and (2) an inference-time procedure that rotates hidden representations to suppress components along those vectors. CREST adaptively suppresses unproductive reasoning behaviors, yielding both higher accuracy and lower computational cost. Across diverse reasoning benchmarks and models, CREST improves accuracy by up to 17.5% while reducing token usage by 37.6%, offering a simple and effective pathway to faster, more reliable LLM reasoning.

