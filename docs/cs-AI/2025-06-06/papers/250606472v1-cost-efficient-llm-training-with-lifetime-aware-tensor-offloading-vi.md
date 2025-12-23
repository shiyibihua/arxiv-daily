---
layout: default
title: Cost-Efficient LLM Training with Lifetime-Aware Tensor Offloading via GPUDirect Storage
---

# Cost-Efficient LLM Training with Lifetime-Aware Tensor Offloading via GPUDirect Storage

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06472" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06472v1</a>
  <a href="https://arxiv.org/pdf/2506.06472.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06472v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06472v1', 'Cost-Efficient LLM Training with Lifetime-Aware Tensor Offloading via GPUDirect Storage')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziqi Yuan, Haoyang Zhang, Yirui Eric Zhou, Apoorve Mohan, I-Hsin Chung, Seetharami Seelam, Jian Huang

**分类**: cs.DC, cs.AI, cs.LG, cs.PF

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出TERAIO以解决GPU内存扩展的成本效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `GPU内存优化` `张量卸载` `固态硬盘` `性能提升`

## 📋 核心要点

1. 现有方法在大型语言模型训练中，GPU内存利用率低，导致资源浪费和性能瓶颈。
2. TERAIO通过生命周期感知的张量卸载策略，优化了GPU内存的使用，提升了训练效率。
3. 实验结果显示，TERAIO在多种LLM训练中平均提升了1.47倍的性能，接近理想性能的80.7%。

## 📝 摘要（中文）

我们提出了一种新的生命周期感知张量卸载框架TERAIO，旨在利用低成本的基于PCIe的固态硬盘（SSD）扩展GPU内存。该框架专为多GPU和多SSD的大型语言模型（LLM）训练而设计。研究表明，在每次LLM训练迭代中，活跃张量仅占分配GPU内存的1.7%，而不活跃张量通常较大且长时间不使用，这为将张量卸载到慢速SSD提供了机会。TERAIO通过分析训练过程中的前几次迭代，准确估计每个张量的生命周期，并生成优化的卸载/预取计划，集成到PyTorch编译的LLM程序中。该框架通过GPUDirect存储实现张量的直接迁移，缓解CPU瓶颈，最大化SSD带宽利用率。与现有方法相比，TERAIO在多种LLM训练中平均提升了1.47倍的性能，达到了理想性能的80.7%。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型训练中GPU内存利用率低的问题，现有方法未能有效利用不活跃张量的内存，导致资源浪费和性能瓶颈。

**核心思路**：TERAIO通过分析张量的生命周期，识别活跃与不活跃张量，制定卸载和预取策略，从而优化GPU内存的使用效率。

**技术框架**：TERAIO的整体架构包括张量生命周期分析模块、卸载/预取计划生成模块和运行时张量迁移引擎，支持通过GPUDirect存储实现GPU与SSD之间的直接数据迁移。

**关键创新**：TERAIO的核心创新在于生命周期感知的张量卸载策略，能够动态调整张量在GPU和SSD之间的存储位置，显著提高了内存利用率和训练性能。

**关键设计**：在设计中，TERAIO通过对训练初期的张量使用情况进行分析，准确估计每个张量的活跃时间，并基于此生成优化的卸载计划，确保GPU训练过程不被阻塞。具体的参数设置和损失函数在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，TERAIO在多种大型语言模型训练中平均提升了1.47倍的性能，相较于现有的ZeRO-Offload和ZeRO-Infinity方法，展现了显著的优势。此外，TERAIO达到了理想性能的80.7%，显示出其在GPU内存扩展方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的训练和推理，尤其是在资源受限的环境中。通过优化GPU内存的使用，TERAIO能够降低训练成本，提高训练效率，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> We present the design and implementation of a new lifetime-aware tensor offloading framework for GPU memory expansion using low-cost PCIe-based solid-state drives (SSDs). Our framework, TERAIO, is developed explicitly for large language model (LLM) training with multiple GPUs and multiple SSDs. Its design is driven by our observation that the active tensors take only a small fraction (1.7% on average) of allocated GPU memory in each LLM training iteration, the inactive tensors are usually large and will not be used for a long period of time, creating ample opportunities for offloading/prefetching tensors to/from slow SSDs without stalling the GPU training process. TERAIO accurately estimates the lifetime (active period of time in GPU memory) of each tensor with the profiling of the first few iterations in the training process. With the tensor lifetime analysis, TERAIO will generate an optimized tensor offloading/prefetching plan and integrate it into the compiled LLM program via PyTorch. TERAIO has a runtime tensor migration engine to execute the offloading/prefetching plan via GPUDirect storage, which allows direct tensor migration between GPUs and SSDs for alleviating the CPU bottleneck and maximizing the SSD bandwidth utilization. In comparison with state-of-the-art studies such as ZeRO-Offload and ZeRO-Infinity, we show that TERAIO improves the training performance of various LLMs by 1.47x on average, and achieves 80.7% of the ideal performance assuming unlimited GPU memory.

