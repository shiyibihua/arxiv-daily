---
layout: default
title: DPVO-QAT++: Heterogeneous QAT and CUDA Kernel Fusion for High-Performance Deep Patch Visual Odometry
---

# DPVO-QAT++: Heterogeneous QAT and CUDA Kernel Fusion for High-Performance Deep Patch Visual Odometry

**arXiv**: [2511.12653v1](https://arxiv.org/abs/2511.12653) | [PDF](https://arxiv.org/pdf/2511.12653.pdf)

**作者**: Cheng Liao

**分类**: cs.CV

**发布日期**: 2025-11-16

---

## 💡 一句话要点

**DPVO-QAT++：异构量化感知训练与CUDA核融合，提升深度Patch视觉里程计性能。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉里程计` `异构精度量化` `量化感知训练` `CUDA核融合` `深度学习` `嵌入式系统` `自主导航`

## 📋 核心要点

1. 深度学习视觉SLAM系统几何推理能力强，但计算开销大，难以在资源受限平台部署。
2. DPVO-QAT++采用异构精度量化和CUDA核融合，在保证精度的前提下，降低内存占用并加速计算。
3. 实验表明，DPVO-QAT++在TartanAir和EuRoC数据集上显著提升了FPS，降低了延迟和内存占用。

## 📝 摘要（中文）

本文提出了一种分层量化优化框架DPVO-QAT++，旨在解决基于深度学习的视觉SLAM系统计算开销过大，难以在资源受限的自主平台上部署的问题。该框架通过可学习的尺度参数化、视觉里程计（VO）前端和后端的异构精度设计（前端浮点伪量化与FP16/FP32，后端全精度）以及用于伪量化的GPU原生核融合（自定义CUDA核）的协同集成，显著减少了内存占用并提高了处理速度，同时保持了原始模型的轨迹精度。在TartanAir数据集上，该框架实现了平均FPS提高52.1%，中值延迟降低29.1%，峰值GPU内存占用减少64.9%，并在32个验证序列上保持了与原始DPVO模型相当的轨迹精度（ATE）。在EuRoC数据集上，该框架实现了平均FPS提高30.1%，中值延迟降低23.1%，峰值GPU内存占用减少37.7%，并在11个验证序列上保持了相当的轨迹精度（ATE）。实验结果表明，DPVO-QAT++有效地弥合了高精度深度VO与实际部署的效率要求之间的差距，为该技术在现实世界嵌入式平台上的应用提供了一种可行的工程范例。

## 🔬 方法详解

**问题定义**：深度学习视觉里程计（VO）虽然精度高，但计算量大，难以在资源受限的嵌入式平台上实时运行。现有的量化方法虽然可以降低计算量，但通常会牺牲精度，并且对不同的VO模块采用相同的量化策略，忽略了不同模块对精度的不同需求。

**核心思路**：DPVO-QAT++的核心思路是采用异构量化感知训练（QAT）和CUDA核融合，在保证VO精度的前提下，最大限度地降低计算量和内存占用。通过对VO前端和后端采用不同的量化策略，并利用CUDA核融合优化量化过程，实现了性能和精度的平衡。

**技术框架**：DPVO-QAT++框架主要包含三个部分：可学习的尺度参数化、异构精度量化和GPU原生核融合。首先，引入可学习的尺度参数，提高量化模型的表达能力。然后，对VO前端采用低精度量化（FP16/FP32伪量化），对VO后端采用全精度，实现异构精度量化。最后，利用CUDA核融合优化伪量化过程，提高计算效率。

**关键创新**：DPVO-QAT++的关键创新在于异构精度量化和GPU原生核融合。异构精度量化允许对VO的不同模块采用不同的量化策略，从而在保证精度的前提下，最大限度地降低计算量。GPU原生核融合通过自定义CUDA核优化量化过程，进一步提高了计算效率。

**关键设计**：VO前端采用浮点伪量化，使用可学习的scale参数来调整量化范围，并通过QAT来优化这些参数。VO后端保持全精度，以保证关键的几何计算精度。CUDA核融合针对伪量化操作，例如clamp和round，进行优化，减少kernel launch的开销。损失函数包括轨迹误差和量化损失，以平衡精度和量化带来的性能提升。

## 📊 实验亮点

DPVO-QAT++在TartanAir数据集上实现了平均FPS提高52.1%，中值延迟降低29.1%，峰值GPU内存占用减少64.9%，同时保持了与原始DPVO模型相当的轨迹精度。在EuRoC数据集上，实现了平均FPS提高30.1%，中值延迟降低23.1%，峰值GPU内存占用减少37.7%，同样保持了相当的轨迹精度。这些结果表明，DPVO-QAT++在性能提升和精度保持方面都取得了显著的成果。

## 🎯 应用场景

DPVO-QAT++适用于资源受限的自主导航平台，如无人机、机器人等。通过降低计算量和内存占用，该方法可以使高精度的深度学习视觉里程计在这些平台上实时运行，从而提高自主导航系统的性能和可靠性。该研究成果对于推动深度学习在嵌入式系统中的应用具有重要意义。

## 📄 摘要（原文）

> Deep learning-based Visual SLAM (vSLAM) systems exhibit exceptional geometric reasoning capabilities, yet their prohibitive computational overhead severely restricts deployment on resource-constrained autonomous platforms. This paper presents a hierarchical quantization optimization framework, DPVO-QAT++ (DPVO-QAT++: Heterogeneous QAT and CUDA Kernel Fusion for High-Performance Deep Patch Visual Odometry). Through the synergistic integration of learnable scale parameterization, a heterogeneous precision design for the Visual Odometry (VO) front-end and back-end (front-end floating-point fake quantization with FP16/FP32; back-end full precision), and GPU-native kernel fusion for fake quantization (custom CUDA kernels), our framework significantly reduces memory footprint and increases processing speed while preserving the trajectory accuracy of the original model. On the TartanAir dataset, our framework achieves an average FPS increase of 52.1%, a 29.1% reduction in median latency, and a 64.9% reduction in peak GPU memory reservation, while maintaining trajectory accuracy (ATE) comparable to the original DPVO model across 32 validation sequences. On the EuRoC dataset, it realizes an average FPS increase of 30.1%, a 23.1% reduction in median latency, and a 37.7% reduction in peak GPU memory reservation, maintaining comparable trajectory accuracy (ATE) across 11 validation sequences. Experimental results demonstrate that DPVO-QAT++ effectively bridges the gap between high-precision deep VO and the efficiency requirements for practical deployment, offering a viable engineering paradigm for the application of this technology on real-world embedded platforms.
>   Keywords: Visual Odometry, Heterogeneous Precision Architecture, Quantization-Aware Training, CUDA Kernel Fusion, Scale-Only Training, Deep Patch Visual Odometry, GPU-Native Kernel Fusion.

