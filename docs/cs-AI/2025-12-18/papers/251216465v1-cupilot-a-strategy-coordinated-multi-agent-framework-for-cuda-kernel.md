---
layout: default
title: cuPilot: A Strategy-Coordinated Multi-agent Framework for CUDA Kernel Evolution
---

# cuPilot: A Strategy-Coordinated Multi-agent Framework for CUDA Kernel Evolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16465" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16465v1</a>
  <a href="https://arxiv.org/pdf/2512.16465.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16465v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16465v1', 'cuPilot: A Strategy-Coordinated Multi-agent Framework for CUDA Kernel Evolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinwu Chen, Qidie Wu, Bin Li, Lin Ma, Xin Si, Yang Hu, Shouyi Yin, Jun Yang

**分类**: cs.AI

**发布日期**: 2025-12-18

**🔗 代码/项目**: [GITHUB](https://github.com/champloo2878/cuPilot-Kernels.git)

---

## 💡 一句话要点

**cuPilot：一种策略协调的多智能体框架，用于CUDA内核演化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `CUDA内核优化` `多智能体系统` `进化算法` `大型语言模型` `屋顶线模型` `策略协调` `自动代码生成`

## 📋 核心要点

1. 现有CUDA内核自动优化方法在智能体设计和演化表示上存在不足，导致性能受限。
2. cuPilot提出策略协调的多智能体框架，将策略作为内核演化的中间语义表示，解决上述问题。
3. 实验表明，cuPilot在多个基准测试中显著提升了CUDA内核的性能，平均加速比达到3.09倍。

## 📝 摘要（中文）

优化CUDA内核是一项具有挑战性且劳动密集型的工作，需要软硬件协同设计专业知识和高性能内核库的专有性质。虽然最近的大型语言模型（LLM）与进化算法相结合在自动内核优化方面显示出希望，但由于其次优的智能体设计和不匹配的演化表示，现有方法通常在性能方面表现不佳。这项工作识别了这些不匹配之处，并提出了cuPilot，这是一个策略协调的多智能体框架，它引入策略作为内核演化的中间语义表示。主要贡献包括策略协调的进化算法、屋顶线引导的提示和策略级种群初始化。实验结果表明，cuPilot生成的内核在100个内核的基准测试中，相对于PyTorch实现了平均3.09倍的加速。在GEMM任务中，cuPilot展示了复杂的优化，并实现了关键硬件单元的高利用率。生成的内核已在https://github.com/champloo2878/cuPilot-Kernels.git上开源。

## 🔬 方法详解

**问题定义**：CUDA内核优化需要专业的软硬件协同设计知识，且高性能内核库通常是专有的，这使得自动优化极具挑战性。现有方法，如直接使用LLM结合进化算法，由于智能体设计不佳和演化表示不匹配，难以达到理想的优化效果。这些方法无法有效地探索CUDA内核的优化空间，导致性能提升有限。

**核心思路**：cuPilot的核心思路是将CUDA内核的优化过程分解为一系列策略，例如循环展开、内存重排等。通过引入“策略”作为中间语义表示，使得LLM能够更好地理解和控制内核的演化过程。这种策略级的抽象允许智能体在更高的层次上进行推理和决策，从而更有效地探索优化空间。

**技术框架**：cuPilot采用多智能体框架，每个智能体负责不同的优化策略。整体流程包括：1) 策略级种群初始化：根据屋顶线模型指导，初始化一组有潜力的策略组合。2) 策略协调的进化算法：多个智能体协同工作，根据当前内核的性能和硬件特性，选择合适的策略进行演化。3) 屋顶线引导的提示：利用屋顶线模型为LLM提供提示，引导其生成更高效的CUDA代码。框架通过迭代演化，不断优化内核性能。

**关键创新**：cuPilot的关键创新在于引入了“策略”作为CUDA内核演化的中间语义表示。与直接操作CUDA代码相比，策略级的抽象更易于LLM理解和控制，从而提高了优化效率。此外，策略协调的进化算法和屋顶线引导的提示进一步增强了框架的优化能力。

**关键设计**：cuPilot的关键设计包括：1) 策略库的设计：定义了一系列常用的CUDA内核优化策略，例如循环展开、向量化、共享内存优化等。2) 策略选择机制：根据当前内核的性能瓶颈和硬件特性，选择合适的策略进行演化。3) 屋顶线模型的应用：利用屋顶线模型分析内核的性能瓶颈，并为LLM提供优化方向的指导。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16465v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16465v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16465v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

cuPilot在100个CUDA内核的基准测试中，相对于PyTorch实现了平均3.09倍的加速。在GEMM任务中，cuPilot生成的内核能够充分利用硬件资源，展现了其强大的优化能力。这些实验结果表明，cuPilot在CUDA内核自动优化方面具有显著优势。

## 🎯 应用场景

cuPilot可应用于各种需要高性能计算的领域，如深度学习、科学计算、图像处理等。它可以帮助开发者自动优化CUDA内核，提高应用程序的性能，降低开发成本。该研究的成果有助于推动高性能计算的普及，加速相关领域的发展。

## 📄 摘要（原文）

> Optimizing CUDA kernels is a challenging and labor-intensive task, given the need for hardware-software co-design expertise and the proprietary nature of high-performance kernel libraries. While recent large language models (LLMs) combined with evolutionary algorithms show promise in automatic kernel optimization, existing approaches often fall short in performance due to their suboptimal agent designs and mismatched evolution representations. This work identifies these mismatches and proposes cuPilot, a strategy-coordinated multi-agent framework that introduces strategy as an intermediate semantic representation for kernel evolution. Key contributions include a strategy-coordinated evolution algorithm, roofline-guided prompting, and strategy-level population initialization. Experimental results show that the generated kernels by cuPilot achieve an average speed up of 3.09$\times$ over PyTorch on a benchmark of 100 kernels. On the GEMM tasks, cuPilot showcases sophisticated optimizations and achieves high utilization of critical hardware units. The generated kernels are open-sourced at https://github.com/champloo2878/cuPilot-Kernels.git.

