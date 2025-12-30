---
layout: default
title: Post-Training Quantization of OpenPangu Models for Efficient Deployment on Atlas A2
---

# Post-Training Quantization of OpenPangu Models for Efficient Deployment on Atlas A2

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23367" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23367v1</a>
  <a href="https://arxiv.org/pdf/2512.23367.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23367v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23367v1', 'Post-Training Quantization of OpenPangu Models for Efficient Deployment on Atlas A2')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yilun Luo, HuaQing Zheng, Haoqian Meng, Wenyuan Liu, Peng Zhang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**针对昇腾A2，提出低比特量化方案，加速盘古模型推理并降低内存占用。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低比特量化` `大语言模型` `模型部署` `昇腾NPU` `Atlas A2` `思维链推理` `INT8量化` `W4A8量化`

## 📋 核心要点

1. 大语言模型推理计算量大，内存占用高，给部署带来挑战，尤其是在资源受限的Ascend NPU上。
2. 采用低比特量化，将FP16计算转换为更高效的整数运算，降低内存占用和计算复杂度。
3. 在代码生成任务上，INT8量化保持了90%以上的精度，并实现了1.5倍的加速；W4A8量化显著降低了内存消耗。

## 📝 摘要（中文）

华为的openPangu-Embedded-1B和openPangu-Embedded-7B是大语言模型openPangu的变体，集成了三种不同的思维链（CoT）推理范式，即slow_think、auto_think和no_think。虽然这些CoT模式增强了推理能力，但它们生成的扩展推理轨迹带来了大量的内存和延迟开销，给在昇腾NPU上的实际部署带来了挑战。本文通过利用低比特量化来解决这些计算约束，将FP16计算转换为更高效的整数运算。我们引入了一个统一的低比特推理框架，支持INT8 (W8A8) 和 W4A8 量化，专门为Atlas A2上的openPangu-Embedded模型进行了优化。我们对所有三种CoT模式在代码生成基准（HumanEval和MBPP）上进行了全面评估，证明了该方法的有效性。INT8量化始终保持超过90%的FP16基线精度，并在Atlas A2上实现了1.5倍的预填充加速。此外，W4A8量化显著降低了内存消耗，尽管在精度上有所折衷。这些发现共同表明，低比特量化有效地促进了昇腾NPU上高效的CoT推理，同时保持了高模型保真度。

## 🔬 方法详解

**问题定义**：论文旨在解决openPangu-Embedded系列模型在Ascend NPU（特别是Atlas A2）上部署时，由于CoT推理导致的内存和延迟开销过大的问题。现有方法，即FP16精度推理，无法满足资源受限场景下的部署需求，需要寻找更高效的推理方案。

**核心思路**：论文的核心思路是利用低比特量化技术，将FP16精度的模型参数和激活值转换为低比特（INT8或W4A8）表示，从而降低内存占用和计算复杂度。通过量化，可以将浮点运算转化为更快的整数运算，从而加速推理过程。

**技术框架**：论文提出了一个统一的低比特推理框架，该框架支持INT8 (W8A8) 和 W4A8 两种量化方式。该框架针对openPangu-Embedded模型在Atlas A2上的部署进行了优化。具体流程包括：首先，对FP16模型进行量化，得到低比特模型；然后，使用低比特模型在Atlas A2上进行推理。

**关键创新**：论文的关键创新在于针对openPangu-Embedded模型和Atlas A2硬件平台，设计并实现了高效的低比特量化推理框架。该框架能够有效地平衡模型精度、推理速度和内存占用，从而实现模型在资源受限环境下的高效部署。

**关键设计**：论文中未明确说明量化方案的具体细节，例如量化参数的校准方法、量化误差的补偿策略等。这些细节对于量化模型的性能至关重要，但论文中未提供足够的信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23367v1/iclr2026/smooth_hadamard_w4a8_demo.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23367v1/iclr2026/humaneval_mbpp_word_counts.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23367v1/iclr2026/CoT_demo.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，INT8量化在HumanEval和MBPP代码生成基准上保持了超过90%的FP16基线精度，并在Atlas A2上实现了1.5倍的预填充加速。W4A8量化虽然在精度上有所下降，但显著降低了内存消耗。这些结果验证了低比特量化在加速推理和降低内存占用方面的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要高效部署大语言模型的场景，例如边缘计算设备、移动设备等。通过低比特量化，可以在资源受限的硬件平台上运行更大规模的模型，从而提升AI应用的智能化水平。该技术对于推动大语言模型在实际场景中的应用具有重要意义。

## 📄 摘要（原文）

> Huawei's openPangu-Embedded-1B and openPangu-Embedded-7B, variants of the openPangu large language model, integrate three distinct Chain-of-Thought (CoT) reasoning paradigms, namely slow_think, auto_think, and no_think. While these CoT modes enhance reasoning capabilities, their generation of extended reasoning traces introduces substantial memory and latency overheads, posing challenges for practical deployment on Ascend NPUs. This paper addresses these computational constraints by leveraging low-bit quantization, which transforms FP16 computations into more efficient integer arithmetic. We introduce a unified low-bit inference framework, supporting INT8 (W8A8) and W4A8 quantization, specifically optimized for openPangu-Embedded models on the Atlas A2. Our comprehensive evaluation, conducted across all three CoT modes on code generation benchmarks (HumanEval and MBPP), demonstrates the efficacy of this approach. INT8 quantization consistently preserves over 90\% of the FP16 baseline accuracy and achieves a 1.5x prefill speedup on the Atlas A2. Furthermore, W4A8 quantization significantly reduces memory consumption, albeit with a moderate trade-off in accuracy. These findings collectively indicate that low-bit quantization effectively facilitates efficient CoT reasoning on Ascend NPUs, maintaining high model fidelity.

