---
layout: default
title: Discrete Optimization of Min-Max Violation and its Applications Across Computational Sciences
---

# Discrete Optimization of Min-Max Violation and its Applications Across Computational Sciences

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13437" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13437v1</a>
  <a href="https://arxiv.org/pdf/2508.13437.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13437v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13437v1', 'Discrete Optimization of Min-Max Violation and its Applications Across Computational Sciences')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheikh Ahmed, Mahdi Mostajabdaveh, Samin Aref, Zirui Zhou

**分类**: cs.AI

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出离散最小-最大违例优化以解决多领域问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `离散优化` `最小-最大违例` `GPU加速` `启发式算法` `量化` `离散断层成像` `滤波器设计`

## 📋 核心要点

1. 现有方法在处理最坏情况性能要求时，往往无法有效地最小化约束违例，导致优化效果不佳。
2. 本文提出的DMMV问题通过离散值分配来优化约束违例，结合GPU加速的启发式算法显著提升求解效率。
3. 实验结果表明，该方法在量化、离散断层成像和FIR滤波器设计中均取得了显著的性能提升。

## 📝 摘要（中文）

本文提出了离散最小-最大违例（DMMV）作为一种通用优化问题，旨在为变量分配离散值，以最小化最大的约束违例。这种无上下文的数学表述适用于具有最坏情况性能要求的广泛应用场景。通过数学定义DMMV问题，探索其性质以建立基础理解。为解决具有实际意义的DMMV实例规模，开发了一种GPU加速的启发式算法，利用DMMV的数学性质加速求解过程。通过解决三个优化问题（语言模型的后训练量化、离散断层成像和有限冲激响应滤波器设计），展示了该启发式算法的广泛适用性。量化中，该启发式算法在现有方法上平均提高了14%；在离散断层成像中，重建误差降低了16%，计算速度提升了6倍；在FIR滤波器设计中，涟漪减少近50%。

## 🔬 方法详解

**问题定义**：本文解决的具体问题是如何在离散优化中最小化最大约束违例。现有方法在处理此类问题时，常常面临计算效率低和结果不理想的挑战。

**核心思路**：论文的核心解决思路是引入离散最小-最大违例（DMMV）问题，通过优化算法为变量分配离散值，从而有效地控制最大违例。设计上结合GPU加速，旨在提高求解速度。

**技术框架**：整体架构包括问题定义、性质分析、启发式算法设计和GPU加速模块。主要阶段为：数学建模、算法实现、性能评估和应用验证。

**关键创新**：最重要的技术创新点在于提出了DMMV作为一种通用的优化框架，并结合GPU加速的启发式算法，显著提高了求解效率和准确性。与现有方法相比，DMMV提供了更灵活的优化策略。

**关键设计**：在关键设计上，算法参数设置经过精心调整，损失函数设计为最大违例的形式，确保优化目标明确。网络结构上，采用了适合离散优化的启发式策略，结合GPU并行计算能力，提升了整体性能。

## 📊 实验亮点

实验结果显示，在量化任务中，该启发式算法平均提升了14%的性能；在离散断层成像中，重建误差降低了16%，计算速度提升了6倍；在FIR滤波器设计中，涟漪减少近50%，相较于商业整数优化求解器Gurobi表现出显著优势。

## 🎯 应用场景

该研究的潜在应用领域广泛，包括自然语言处理中的模型量化、医学成像中的离散断层成像以及信号处理中的滤波器设计。其实际价值在于提供了一种高效的优化方法，能够在多个领域中提升性能，未来可能推动相关技术的进步与应用。

## 📄 摘要（原文）

> We introduce the Discrete Min-Max Violation (DMMV) as a general optimization problem which seeks an assignment of discrete values to variables that minimizes the largest constraint violation. This context-free mathematical formulation is applicable to a wide range of use cases that have worst-case performance requirements. After defining the DMMV problem mathematically, we explore its properties to establish a foundational understanding. To tackle DMMV instance sizes of practical relevance, we develop a GPU-accelerated heuristic that takes advantage of the mathematical properties of DMMV for speeding up the solution process. We demonstrate the versatile applicability of our heuristic by solving three optimization problems as use cases: (1) post-training quantization of language models, (2) discrete tomography, and (3) Finite Impulse Response (FIR) filter design. In quantization without outlier separation, our heuristic achieves 14% improvement on average over existing methods. In discrete tomography, it reduces reconstruction error by 16% under uniform noise and accelerates computations by a factor of 6 on GPU. For FIR filter design, it nearly achieves 50% ripple reduction compared to using the commercial integer optimization solver, Gurobi. Our comparative results point to the benefits of studying DMMV as a context-free optimization problem and the advantages that our proposed heuristic offers on three distinct problems. Our GPU-accelerated heuristic will be made open-source to further stimulate research on DMMV and its other applications. The code is available at https://anonymous.4open.science/r/AMVM-5F3E/

