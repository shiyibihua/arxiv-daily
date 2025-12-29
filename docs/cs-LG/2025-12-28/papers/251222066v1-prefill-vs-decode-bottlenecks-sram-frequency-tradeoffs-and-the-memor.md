---
layout: default
title: "Prefill vs. Decode Bottlenecks: SRAM-Frequency Tradeoffs and the Memory-Bandwidth Ceiling"
---

# Prefill vs. Decode Bottlenecks: SRAM-Frequency Tradeoffs and the Memory-Bandwidth Ceiling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.22066" class="toolbar-btn" target="_blank">📄 arXiv: 2512.22066v1</a>
  <a href="https://arxiv.org/pdf/2512.22066.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.22066v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.22066v1', 'Prefill vs. Decode Bottlenecks: SRAM-Frequency Tradeoffs and the Memory-Bandwidth Ceiling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hannah Atmer, Yuan Yao, Thiemo Voigt, Stefanos Kaxiras

**分类**: cs.AR, cs.LG, cs.PF

**发布日期**: 2025-12-26

---

## 💡 一句话要点

**研究SRAM频率权衡与内存带宽瓶颈，优化LLM推理能效**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `能效优化` `SRAM` `内存带宽` `推理加速器` `能量延迟积`

## 📋 核心要点

1. 大型语言模型部署的成本和环境影响受限于能耗，现有研究对片上SRAM大小和工作频率的影响分析不足。
2. 通过结合OpenRAM、LLMCompass和ScaleSIM，研究SRAM大小和工作频率对LLM推理预填充和解码阶段能效的影响。
3. 实验表明，高工作频率和小型本地缓冲区（32KB-64KB）的组合能实现最佳的能量延迟积，并揭示了内存带宽的性能上限。

## 📝 摘要（中文）

本文研究了片上SRAM大小和工作频率对大型语言模型（LLM）推理能效和性能的影响，重点关注计算密集型预填充（prefill）和内存密集型解码（decode）阶段的不同行为。研究方法结合了OpenRAM（用于能量建模）、LLMCompass（用于延迟模拟）和ScaleSIM（用于脉动阵列运算强度）。结果表明，总能量消耗主要由两个阶段的SRAM大小决定，较大的缓冲区会显著增加静态能量（由于泄漏），而相应的延迟收益无法抵消。研究定量地探讨了内存带宽瓶颈，表明高工作频率降低了预填充延迟，但其对内存密集型解码延迟的积极影响受到外部内存带宽的限制。反直觉的是，高计算频率可以通过减少执行时间并因此减少静态能量消耗（超过动态功耗的增加）来降低总能量。确定了模拟工作负载的最佳硬件配置：高工作频率（1200MHz-1400MHz）和32KB至64KB的小型本地缓冲区。这种组合实现了最佳的能量延迟积，平衡了低延迟和高能效。此外，证明了内存带宽如何充当性能上限，并且提高计算频率仅在工作负载变为内存密集型时才能产生性能提升。该分析为设计节能LLM加速器提供了具体的架构见解，特别是对于旨在最大限度地减少能源开销的数据中心。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）推理过程中，片上SRAM大小和工作频率对能效和性能的影响问题。现有方法未能充分分析预填充和解码阶段的不同特性，以及内存带宽对性能的限制，导致LLM加速器设计缺乏针对性优化。

**核心思路**：论文的核心思路是通过模拟不同SRAM大小和工作频率下的LLM推理过程，量化分析其对能耗和延迟的影响。重点关注预填充阶段的计算密集型特性和解码阶段的内存密集型特性，并探讨内存带宽对性能的限制。通过找到最佳的SRAM大小和工作频率组合，实现能效和性能的平衡。

**技术框架**：论文采用了一种多工具结合的模拟方法。首先，使用OpenRAM对不同大小的SRAM进行能量建模，获取静态和动态功耗数据。然后，使用LLMCompass进行延迟模拟，评估不同工作频率下的推理延迟。最后，使用ScaleSIM模拟脉动阵列的运算强度，分析计算和内存访问的比例。通过综合分析这些数据，确定最佳的硬件配置。

**关键创新**：论文的关键创新在于：1) 区分了LLM推理的预填充和解码阶段，并针对性地分析了SRAM大小和工作频率的影响；2) 揭示了高工作频率对内存密集型解码阶段的性能提升存在上限，受限于外部内存带宽；3) 提出了高工作频率和小型本地缓冲区的组合是实现最佳能量延迟积的有效策略。

**关键设计**：论文的关键设计包括：1) 选择了OpenRAM、LLMCompass和ScaleSIM等工具进行协同模拟，保证了结果的准确性和可靠性；2) 针对不同的SRAM大小和工作频率进行了大量的实验，获得了充分的数据支持；3) 通过能量延迟积（EDP）作为评估指标，综合考虑了能耗和延迟的影响。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22066v1/images/sysarraygpu.drawio.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22066v1/images/llmcompass.drawio.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22066v1/images/synthesis.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，高工作频率（1200MHz-1400MHz）和小型本地缓冲区（32KB-64KB）的组合能够实现最佳的能量延迟积。同时，实验验证了内存带宽是性能的瓶颈，提高计算频率只有在工作负载变为内存密集型之前才能带来性能提升。

## 🎯 应用场景

该研究成果可应用于数据中心LLM加速器的设计，通过优化SRAM大小和工作频率，降低能耗，提高推理性能。这对于降低LLM部署的成本和环境影响具有重要意义，尤其是在大规模部署LLM的场景下，能显著减少能源开销。

## 📄 摘要（原文）

> Energy consumption dictates the cost and environmental impact of deploying Large Language Models. This paper investigates the impact of on-chip SRAM size and operating frequency on the energy efficiency and performance of LLM inference, focusing on the distinct behaviors of the compute-bound prefill and memory-bound decode phases. Our simulation methodology combines OpenRAM for energy modeling, LLMCompass for latency simulation, and ScaleSIM for systolic array operational intensity. Our findings show that total energy use is predominantly determined by SRAM size in both phases, with larger buffers significantly increasing static energy due to leakage, which is not offset by corresponding latency benefits. We quantitatively explore the memory-bandwidth bottleneck, demonstrating that while high operating frequencies reduce prefill latency, their positive impact on memory-bound decode latency is capped by the external memory bandwidth. Counter-intuitively, high compute frequency can reduce total energy by reducing execution time and consequently decreasing static energy consumption more than the resulting dynamic power increase. We identify an optimal hardware configuration for the simulated workload: high operating frequencies (1200MHz-1400MHz) and a small local buffer size of 32KB to 64KB. This combination achieves the best energy-delay product, balancing low latency with high energy efficiency. Furthermore, we demonstrate how memory bandwidth acts as a performance ceiling, and that increasing compute frequency only yields performance gains up to the point where the workload becomes memory-bound. This analysis provides concrete architectural insights for designing energy-efficient LLM accelerators, especially for datacenters aiming to minimize their energy overhead.

