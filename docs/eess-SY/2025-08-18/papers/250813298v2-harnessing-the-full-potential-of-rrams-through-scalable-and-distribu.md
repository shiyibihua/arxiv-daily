---
layout: default
title: Harnessing the Full Potential of RRAMs through Scalable and Distributed In-Memory Computing with Integrated Error Correction
---

# Harnessing the Full Potential of RRAMs through Scalable and Distributed In-Memory Computing with Integrated Error Correction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13298" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13298v2</a>
  <a href="https://arxiv.org/pdf/2508.13298.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13298v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13298v2', 'Harnessing the Full Potential of RRAMs through Scalable and Distributed In-Memory Computing with Integrated Error Correction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huynh Q. N. Vo, Md Tawsif Rahman Chowdhury, Paritosh Ramanan, Murat Yildirim, Gozde Tutuncuoglu

**分类**: cs.DC, cs.AR, cs.ET, cs.PF, eess.SY

**发布日期**: 2025-08-18 (更新: 2025-08-26)

---

## 💡 一句话要点

**提出MELISO+以解决RRAM计算中的能效与精度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内存计算` `电阻随机存取存储器` `错误校正` `分布式计算` `高维计算` `能效提升` `算法硬件协同设计`

## 📋 核心要点

1. 现有的内存计算方法在处理大规模计算任务时面临设备非理想性和可扩展性不足的问题。
2. 本文提出MELISO+框架，结合双层错误校正机制和分布式RRAM计算，提升能效与计算精度。
3. 实验结果表明，MELISO+将算术错误减少90%以上，能效提升三到五个数量级，延迟降低100倍。

## 📝 摘要（中文）

全球计算需求的指数增长加剧了传统架构的能量需求，主要由于数据移动的高能耗。通过将内存与处理集成的电阻随机存取存储器（RRAM）进行内存计算，尽管可以解决这一问题，但在设备级非理想性和大规模计算任务的可扩展性方面面临重大挑战。本文提出了MELISO+（内存线性求解器），这是一个全栈分布式框架，旨在实现能效高的内存计算。MELISO+引入了一种新颖的双层错误校正机制，以减轻设备非理想性，并开发了一个分布式RRAM计算框架，使得矩阵计算超过65,000×65,000的维度。该方法将由于设备非理想性引起的一阶和二阶算术错误减少了90%以上，能效提高了三到五个数量级，延迟降低了100倍。因此，MELISO+使得低精度的RRAM设备在准确性、能效和延迟指标上超越高精度设备。通过将算法与硬件的共同设计与可扩展架构相结合，MELISO+显著推动了适用于大语言模型和生成式AI等应用的可持续高维计算。

## 🔬 方法详解

**问题定义**：本文旨在解决RRAM计算中的设备非理想性和可扩展性不足的问题。现有方法在处理大规模矩阵计算时，常常受到算术错误和高能耗的限制。

**核心思路**：MELISO+通过引入双层错误校正机制来减轻设备非理想性，同时采用分布式计算架构以支持大规模矩阵运算，从而提高能效和计算精度。

**技术框架**：MELISO+的整体架构包括错误校正模块和分布式计算模块。错误校正模块负责实时监测和修正算术错误，而分布式计算模块则将计算任务分配到多个RRAM设备上，以实现高效的并行处理。

**关键创新**：MELISO+的双层错误校正机制是其最重要的技术创新，能够有效减少由于设备非理想性引起的算术错误，与现有方法相比，显著提升了计算的准确性和能效。

**关键设计**：在设计中，MELISO+采用了特定的参数设置和损失函数，以优化错误校正过程，并通过精心设计的网络结构实现高效的分布式计算。

## 📊 实验亮点

实验结果显示，MELISO+在处理大规模矩阵计算时，算术错误减少超过90%，能效提升三到五个数量级，延迟降低100倍。这些结果表明，MELISO+在准确性、能效和延迟方面超越了传统高精度设备。

## 🎯 应用场景

MELISO+框架在大语言模型和生成式AI等高维计算任务中具有广泛的应用潜力。其能效和精度的提升，使得在资源受限的环境中也能进行复杂的计算，推动了智能计算的可持续发展。

## 📄 摘要（原文）

> Exponential growth in global computing demand is exacerbated due to the higher-energy requirements of conventional architectures, primarily due to energy-intensive data movement. In-memory computing with Resistive Random Access Memory (RRAM) addresses this by co-integrating memory and processing, but faces significant hurdles related to device-level non-idealities and poor scalability for large computing tasks. Here, we introduce MELISO+ (In-Memory Linear Solver), a full-stack, distributed framework for energy-efficient in-memory computing. MELISO+ proposes a novel two-tier error correction mechanism to mitigate device non-idealities and develops a distributed RRAM computing framework to enable matrix computations exceeding dimensions of $65,000\times65,000$. This approach reduces first- and second-order arithmetic errors due to device non-idealities by over $90\%$, enhances energy efficiency by three to five orders of magnitude, and decreases latency 100-fold. Hence, MELISO+ allows lower-precision RRAM devices to outperform high-precision device alternatives in accuracy, energy and latency metrics. By unifying algorithm-hardware co-design with scalable architecture, MELISO+ significantly advances sustainable, high-dimensional computing suitable for applications like large language models and generative AI.

