---
layout: default
title: "AKG kernel Agent: A Multi-Agent Framework for Cross-Platform Kernel Synthesis"
---

# AKG kernel Agent: A Multi-Agent Framework for Cross-Platform Kernel Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23424" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23424v1</a>
  <a href="https://arxiv.org/pdf/2512.23424.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23424v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23424v1', 'AKG kernel Agent: A Multi-Agent Framework for Cross-Platform Kernel Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinye Du, Quan Yuan, Zuyao Zhang, Yanzhi Yi, Jiahui Hu, Wangyi Chen, Yiyang Zhu, Qishui Zheng, Wenxiang Zou, Xiangyu Chang, Zuohe Zheng, Zichun Ye, Chao Liu, Shanni Li, Renwei Zhang, Yiping Deng, Xinwei Hu, Xuefeng Jin, Jie Zhao

**分类**: cs.AI, cs.LG

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出AKG kernel Agent，一个用于跨平台内核合成的多智能体框架。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内核生成` `多智能体系统` `领域特定语言` `AI自动化` `性能优化`

## 📋 核心要点

1. 现有AI模型对高性能内核需求激增，但手动优化难以跟上硬件更新和架构多样性，成为AI系统开发的瓶颈。
2. AKG kernel agent是一个多智能体系统，通过自动化内核生成、迁移和调优，支持多种DSL和硬件后端，解决内核开发瓶颈。
3. 实验表明，在GPU和NPU后端上，AKG kernel agent使用Triton DSL在KernelBench上实现了平均1.46倍的加速。

## 📝 摘要（中文）

现代AI模型对高性能计算内核的需求日益增长。LLM、多模态架构和推荐系统复杂性的增加，以及稀疏性和量化等技术的应用，带来了巨大的计算挑战。此外，频繁的硬件更新和多样化的芯片架构进一步复杂化了这一局面，需要为每个平台定制内核实现。然而，手动优化无法跟上这些需求，成为AI系统开发的关键瓶颈。LLM代码生成能力的最新进展为自动化内核开发开辟了新的可能性。本文提出了AKG kernel agent（AI驱动的内核生成器），一个多智能体系统，可以自动生成、迁移和性能调优内核。AKG kernel agent旨在支持多种领域特定语言（DSL），包括Triton、TileLang、CPP和CUDA-C，使其能够针对不同的硬件后端，同时保持正确性和可移植性。该系统的模块化设计允许快速集成新的DSL和硬件目标。在使用Triton DSL在GPU和NPU后端上评估KernelBench时，AKG kernel agent比PyTorch Eager基线实现平均加速1.46倍，证明了其在加速现代AI工作负载的内核开发方面的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决现代AI模型对高性能计算内核日益增长的需求与手动内核优化速度无法满足硬件快速迭代之间的矛盾。现有方法，即手动优化内核，耗时且容易出错，无法适应快速变化的硬件架构和AI模型需求。这导致AI系统开发效率低下，成为一个关键瓶颈。

**核心思路**：论文的核心思路是利用LLM的代码生成能力，构建一个多智能体系统，自动化内核的生成、迁移和性能调优。通过支持多种领域特定语言（DSL），该系统可以针对不同的硬件后端生成优化的内核，从而提高AI模型的计算效率。这种自动化方法旨在克服手动优化的局限性，加速AI系统的开发过程。

**技术框架**：AKG kernel agent的技术框架是一个多智能体系统，包含以下主要模块：1) **任务分解模块**：将高层次的内核生成任务分解为更小的、可管理的子任务。2) **代码生成模块**：利用LLM生成初步的内核代码，支持多种DSL，如Triton、TileLang、CPP和CUDA-C。3) **代码验证模块**：验证生成的代码的正确性，确保其功能符合预期。4) **性能调优模块**：通过自动搜索和优化技术，提升内核的性能。5) **部署模块**：将优化后的内核部署到目标硬件平台上。这些模块协同工作，实现内核的自动化生成和优化。

**关键创新**：最重要的技术创新点在于将LLM的代码生成能力与多智能体系统相结合，实现内核开发的自动化。与传统的基于规则或模板的内核生成方法相比，AKG kernel agent能够生成更复杂、更优化的内核代码，并且可以更容易地适应新的硬件架构和AI模型需求。此外，该系统支持多种DSL，使其具有更广泛的适用性。

**关键设计**：AKG kernel agent的关键设计包括：1) **智能体之间的协作机制**：定义了智能体之间如何通信和协作，以完成复杂的内核生成任务。2) **LLM的选择和训练**：选择了合适的LLM，并对其进行微调，以提高其代码生成能力。3) **性能调优算法**：采用了高效的性能调优算法，如遗传算法或强化学习，以自动搜索最优的内核配置。4) **代码验证方法**：设计了有效的代码验证方法，以确保生成的代码的正确性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23424v1/media/Framework.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23424v1/media/ConductorWorkflow.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23424v1/media/RAG.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，AKG kernel agent在使用Triton DSL在GPU和NPU后端上评估KernelBench时，相比于PyTorch Eager基线实现，平均加速了1.46倍。这一显著的性能提升证明了AKG kernel agent在加速现代AI工作负载的内核开发方面的有效性。该结果表明，通过自动化内核生成和优化，可以显著提高AI模型的计算效率。

## 🎯 应用场景

AKG kernel agent可广泛应用于各种需要高性能计算内核的AI领域，如深度学习、计算机视觉、自然语言处理和推荐系统。它能够加速AI模型的训练和推理过程，提高AI应用的性能和效率。该研究的潜在价值在于降低了内核开发的门槛，使得AI开发者能够更专注于模型设计和算法创新，而无需过多关注底层硬件细节。未来，AKG kernel agent有望成为AI系统开发的重要工具，推动AI技术的普及和应用。

## 📄 摘要（原文）

> Modern AI models demand high-performance computation kernels. The growing complexity of LLMs, multimodal architectures, and recommendation systems, combined with techniques like sparsity and quantization, creates significant computational challenges. Moreover, frequent hardware updates and diverse chip architectures further complicate this landscape, requiring tailored kernel implementations for each platform. However, manual optimization cannot keep pace with these demands, creating a critical bottleneck in AI system development. Recent advances in LLM code generation capabilities have opened new possibilities for automating kernel development. In this work, we propose AKG kernel agent (AI-driven Kernel Generator), a multi-agent system that automates kernel generation, migration, and performance tuning. AKG kernel agent is designed to support multiple domain-specific languages (DSLs), including Triton, TileLang, CPP, and CUDA-C, enabling it to target different hardware backends while maintaining correctness and portability. The system's modular design allows rapid integration of new DSLs and hardware targets. When evaluated on KernelBench using Triton DSL across GPU and NPU backends, AKG kernel agent achieves an average speedup of 1.46$\times$ over PyTorch Eager baselines implementations, demonstrating its effectiveness in accelerating kernel development for modern AI workloads.

