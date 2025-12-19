---
layout: default
title: LoPA: Scaling dLLM Inference via Lookahead Parallel Decoding
---

# LoPA: Scaling dLLM Inference via Lookahead Parallel Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16229" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16229v1</a>
  <a href="https://arxiv.org/pdf/2512.16229.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16229v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16229v1', 'LoPA: Scaling dLLM Inference via Lookahead Parallel Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenkai Xu, Yijie Jin, Jiajun Li, Yi Tu, Guoping Long, Dandan Tu, Tianqi Hou, Junchi Yan, Zhijie Deng

**分类**: cs.CL

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/zhijie-group/LoPA)

---

## 💡 一句话要点

**LoPA：通过前瞻并行解码加速扩散大语言模型推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散大语言模型` `并行解码` `推理加速` `Token填充顺序` `前瞻策略`

## 📋 核心要点

1. 现有的扩散大语言模型推理方法受限于置信度驱动的解码策略，并行度较低，导致推理速度慢。
2. LoPA通过并行探索不同的Token填充顺序(TFO)，并基于置信度选择最优TFO，从而提高并行度。
3. 实验表明，LoPA显著提高了D2F模型的解码效率，在GSM8K上实现了更高的TPF和优于基线的性能。

## 📝 摘要（中文）

扩散大语言模型(dLLM)在高速推理方面展现出巨大潜力。然而，当前基于置信度的解码策略受到有限并行性的约束，通常每次前向传播只能实现1-3个token。本文发现dLLM推理过程中的并行度对Token填充顺序(TFO)高度敏感。因此，我们提出了Lookahead PArallel Decoding (LoPA)，一种无需训练、即插即用的算法，用于识别更优的TFO，从而加速推理。LoPA通过并行分支同时探索不同的候选TFO，并根据分支置信度选择未来并行潜力最大的一个。我们将LoPA应用于最先进的D2F模型，观察到解码效率的显著提高。值得注意的是，LoPA在GSM8K上将D2F-Dream的TPF提高到10.1，同时保持优于Dream基线的性能。此外，为了支持这种前所未有的并行度，我们开发了一种专门的多设备推理系统，具有分支并行性(BP)，在多GPU部署下实现了每秒1073.9个token的单样本吞吐量。代码已开源。

## 🔬 方法详解

**问题定义**：扩散大语言模型(dLLM)的推理速度受限于其解码过程的并行度。现有的基于置信度的解码策略，例如D2F，在每一步只能填充少数几个token，导致整体推理速度较慢。问题的核心在于如何找到一种能够最大化并行度的Token填充顺序(TFO)。

**核心思路**：LoPA的核心思路是通过前瞻性的并行探索，找到一个能够最大化未来并行度的TFO。不同于传统的贪心策略，LoPA同时探索多个候选的TFO，并根据这些候选TFO的置信度来评估其未来并行潜力。选择具有最高并行潜力的TFO，从而提高整体的解码效率。

**技术框架**：LoPA的整体框架包括以下几个主要步骤：1) **并行分支探索**：同时生成多个候选的TFO分支。2) **置信度评估**：评估每个分支的置信度，用于预测其未来并行潜力。3) **分支选择**：选择具有最高并行潜力的分支。4) **Token填充**：根据选定的分支填充token。这个过程迭代进行，直到生成完整的序列。为了支持高并行度，论文还开发了一个多设备推理系统，利用分支并行性(BP)在多个GPU上并行执行不同的分支。

**关键创新**：LoPA的关键创新在于其前瞻性的并行解码策略。与传统的贪心解码策略不同，LoPA不是简单地选择当前置信度最高的token，而是通过并行探索多个候选的TFO，并根据其未来并行潜力进行选择。这种前瞻性的策略能够有效地提高解码过程的并行度，从而加速推理。

**关键设计**：LoPA的关键设计包括：1) **分支数量**：控制并行探索的候选TFO的数量。2) **置信度评估函数**：用于评估每个分支的置信度，并预测其未来并行潜力。论文中使用了D2F模型提供的置信度作为评估函数。3) **分支选择策略**：用于选择具有最高并行潜力的分支。论文中使用了基于置信度的选择策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16229v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16229v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16229v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LoPA在D2F-Dream模型上取得了显著的性能提升。在GSM8K数据集上，LoPA将TPF（每前向传播的token数）提高到10.1，显著高于基线模型。同时，LoPA保持了优于Dream基线的性能。此外，通过开发专门的多设备推理系统，LoPA实现了高达1073.9 tokens/秒的单样本吞吐量。

## 🎯 应用场景

LoPA可以应用于各种需要高速推理的扩散大语言模型应用场景，例如实时对话系统、快速文本生成、以及需要低延迟响应的AI助手。通过提高推理速度，LoPA可以降低计算成本，并使dLLM能够部署在资源受限的设备上，从而扩展其应用范围。

## 📄 摘要（原文）

> Diffusion Large Language Models (dLLMs) have demonstrated significant potential for high-speed inference. However, current confidence-driven decoding strategies are constrained by limited parallelism, typically achieving only 1--3 tokens per forward pass (TPF). In this work, we identify that the degree of parallelism during dLLM inference is highly sensitive to the Token Filling Order (TFO). Then, we introduce Lookahead PArallel Decoding LoPA, a training-free, plug-and-play algorithm, to identify a superior TFO and hence accelerate inference. LoPA concurrently explores distinct candidate TFOs via parallel branches, and selects the one with the highest potential for future parallelism based on branch confidence. We apply LoPA to the state-of-the-art D2F model and observe a substantial enhancement in decoding efficiency. Notably, LoPA increases the TPF of D2F-Dream to 10.1 on the GSM8K while maintaining performance superior to the Dream baseline. Furthermore, to facilitate this unprecedented degree of parallelism, we develop a specialized multi-device inference system featuring Branch Parallelism (BP), which achieves a single-sample throughput of 1073.9 tokens per second under multi-GPU deployment. The code is available at https://github.com/zhijie-group/LoPA.

