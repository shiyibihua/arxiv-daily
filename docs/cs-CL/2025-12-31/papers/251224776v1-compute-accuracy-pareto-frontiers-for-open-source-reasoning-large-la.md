---
layout: default
title: Compute-Accuracy Pareto Frontiers for Open-Source Reasoning Large Language Models
---

# Compute-Accuracy Pareto Frontiers for Open-Source Reasoning Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24776" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24776v1</a>
  <a href="https://arxiv.org/pdf/2512.24776.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24776v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24776v1', 'Compute-Accuracy Pareto Frontiers for Open-Source Reasoning Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ákos Prucs, Márton Csutora, Mátyás Antal, Márk Marosi

**分类**: cs.CL

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**针对开源推理大语言模型，构建计算-精度帕累托前沿，优化模型选择。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理能力` `计算成本` `帕累托前沿` `模型选择`

## 📋 核心要点

1. 现有文献忽略了长推理序列带来的巨大计算负担，工业应用中模型选择需兼顾精度与资源约束。
2. 论文通过测试时计算感知的评估，绘制开源LLM在推理基准上的计算-精度帕累托前沿。
3. 实验表明混合专家（MoE）架构在性能和效率之间取得了较好的平衡，并揭示了推理计算的饱和点。

## 📝 摘要（中文）

大型语言模型（LLM）在复杂的推理基准测试中表现出快速的改进，尤其是在允许利用中间推理步骤之后。然而，目前的文献经常忽略与生成长推理序列相关的巨大计算负担。对于工业应用，模型选择不仅取决于原始精度，还取决于资源约束和推理成本。在这项工作中，我们对当代和较早的开源LLM进行了测试时计算感知的评估，绘制了它们在数学和推理密集型基准测试中的帕累托前沿。我们的研究结果表明，混合专家（MoE）架构是在我们的评估环境中平衡性能和效率的有力候选者。此外，我们追踪了帕累托效率随时间的轨迹，以推导出关于单位计算的精度增益的新兴趋势。最后，我们证明了推理时计算存在饱和点。超过某个阈值，精度增益会减少，这表明虽然扩展的推理能力是有益的，但它们无法克服关于特定复杂性的内在模型限制。

## 🔬 方法详解

**问题定义**：现有的大语言模型在复杂推理任务上取得了显著进展，但生成长推理链条需要消耗大量的计算资源。在实际工业应用中，模型选择不仅要考虑精度，还需要考虑计算成本和资源限制。因此，如何在精度和计算成本之间找到平衡点是一个关键问题。

**核心思路**：论文的核心思路是通过构建计算-精度帕累托前沿，来评估不同开源大语言模型在推理任务上的性能。帕累托前沿能够清晰地展示在给定计算资源下，模型能够达到的最高精度，或者在给定精度要求下，模型所需的最小计算资源。这为模型选择提供了有力的依据。

**技术框架**：论文的技术框架主要包括以下几个步骤：1) 选择一系列开源大语言模型，包括不同架构和规模的模型。2) 选择一系列数学和推理密集型基准测试。3) 对每个模型在每个基准测试上进行测试，并记录其精度和计算成本（例如，推理时间、GPU 内存占用）。4) 基于精度和计算成本，构建帕累托前沿。5) 分析帕累托前沿，找出在不同计算资源约束下，性能最优的模型。

**关键创新**：论文的关键创新在于提出了一个测试时计算感知的评估框架，能够全面评估大语言模型在推理任务上的性能和计算成本。通过构建帕累托前沿，能够清晰地展示模型在精度和计算成本之间的权衡关系，为模型选择提供了客观的依据。此外，论文还发现混合专家（MoE）架构在性能和效率之间取得了较好的平衡，并揭示了推理计算的饱和点。

**关键设计**：论文的关键设计包括：1) 选择具有代表性的开源大语言模型，覆盖不同架构和规模。2) 选择具有挑战性的数学和推理密集型基准测试，能够充分评估模型的推理能力。3) 精确测量模型的计算成本，例如，推理时间、GPU 内存占用。4) 使用帕累托前沿分析方法，能够清晰地展示模型在精度和计算成本之间的权衡关系。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24776v1/figs/tflop_vs_accuracy_avg.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24776v1/figs/tflop_vs_accuracy_by_benchmark.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24776v1/figs/trends_multi_aggregated_log10-FLOPS.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，混合专家（MoE）架构在性能和效率之间取得了较好的平衡，是工业应用中一个有潜力的选择。此外，研究还发现推理时计算存在饱和点，超过某个阈值，精度增益会减少。这意味着，过度增加计算资源并不能无限提升模型的推理能力，需要综合考虑模型本身的限制。

## 🎯 应用场景

该研究成果可应用于工业界大语言模型的选型和部署。企业可以根据自身的计算资源约束和精度要求，利用论文提出的评估框架，选择最适合自身需求的模型。此外，该研究还可以指导模型优化，例如，通过调整模型架构或推理策略，在精度和计算成本之间取得更好的平衡。该研究对于推动大语言模型在实际应用中的落地具有重要意义。

## 📄 摘要（原文）

> Large Language Models (LLMs) are demonstrating rapid improvements on complex reasoning benchmarks, particularly when allowed to utilize intermediate reasoning steps before converging on a final solution. However, current literature often overlooks the significant computational burden associated with generating long reasoning sequences. For industrial applications, model selection depends not only on raw accuracy but also on resource constraints and inference costs. In this work, we conduct a test-time-compute aware evaluation of both contemporary and older open-source LLMs, mapping their Pareto frontiers across math- and reasoning-intensive benchmarks. Our findings identify the Mixture of Experts (MoE) architecture as a strong candidate to balance performance and efficiency in our evaluation setting. Furthermore, we trace the trajectory of Pareto efficiency over time to derive an emergent trend regarding accuracy gain per unit of compute. Finally, we demonstrate that there is a saturation point for inference-time compute. Beyond a certain threshold, accuracy gains diminish, indicating that while extended reasoning capabilities are beneficial, they cannot overcome intrinsic model limitations regarding specific complexities.

