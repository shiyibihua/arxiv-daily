---
layout: default
title: S$^2$-MLLM: Boosting Spatial Reasoning Capability of MLLMs for 3D Visual Grounding with Structural Guidance
---

# S$^2$-MLLM: Boosting Spatial Reasoning Capability of MLLMs for 3D Visual Grounding with Structural Guidance

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.01223" target="_blank" class="toolbar-btn">arXiv: 2512.01223v1</a>
    <a href="https://arxiv.org/pdf/2512.01223.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.01223v1" 
            onclick="toggleFavorite(this, '2512.01223v1', 'S$^2$-MLLM: Boosting Spatial Reasoning Capability of MLLMs for 3D Visual Grounding with Structural Guidance')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Beining Xu, Siting Zhu, Zhao Jin, Junxian Li, Hesheng Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-01

**备注**: 18 pages, 9 figures

---

## 💡 一句话要点

**S$^2$-MLLM：通过结构引导增强MLLM在3D视觉定位中的空间推理能力**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D视觉定位` `多模态大语言模型` `空间推理` `结构引导` `具身智能`

## 📋 核心要点

1. 现有3D视觉定位方法依赖于点云重建和视角渲染，效率低且空间推理能力有限，无法充分利用MLLM的潜力。
2. S$^2$-MLLM通过引入空间引导策略，利用前馈3D重建的结构感知能力，使MLLM能够隐式地进行3D空间推理。
3. 实验结果表明，S$^2$-MLLM在ScanRefer、Nr3D和Sr3D数据集上显著优于现有方法，展现了卓越的性能、泛化性和效率。

## 📝 摘要（中文）

3D视觉定位(3DVG)旨在根据自然语言描述在3D场景中定位物体，是具身智能和机器人技术的基础任务。多模态大型语言模型(MLLM)的最新进展推动了将其扩展到3DVG的研究。然而，MLLM主要处理2D视觉输入，难以仅从这些有限的视角理解场景的3D空间结构。现有方法主要利用重建点云的视角相关渲染，为MLLM在3DVG任务中提供显式结构引导，导致效率低下和空间推理受限。为了解决这个问题，我们提出了S$^2$-MLLM，一个通过隐式空间推理增强MLLM空间推理能力的高效框架。我们引入了一种空间引导策略，利用前馈3D重建的结构感知能力。通过在训练期间获得3D结构理解，我们的模型可以隐式地推理3D场景，而无需依赖低效的点云重建。此外，我们提出了一个结构增强模块(SE)，该模块首先采用视图内和视图间注意力机制来捕获视图内的依赖关系和视图间的对应关系。该模块进一步集成了多级位置编码，将视觉表示与空间位置和视点信息相关联，从而实现更准确的结构理解。大量实验表明，S$^2$-MLLM统一了卓越的性能、泛化性和效率，在ScanRefer、Nr3D和Sr3D数据集上实现了优于现有方法的显著性能。

## 🔬 方法详解

**问题定义**：3D视觉定位任务旨在根据自然语言描述在3D场景中定位目标物体。现有方法主要依赖于从多个视角渲染的3D点云，为多模态大语言模型(MLLM)提供显式的结构信息。然而，这种方法计算成本高昂，且受限于点云重建的质量，导致空间推理能力不足。

**核心思路**：S$^2$-MLLM的核心思路是通过隐式的方式引导MLLM学习3D场景的结构信息，避免显式的点云重建。具体来说，利用前馈3D重建的结构感知能力，使模型在训练过程中学习到3D场景的结构信息，从而在推理阶段能够隐式地进行空间推理。这样可以提高效率，并增强模型的空间推理能力。

**技术框架**：S$^2$-MLLM框架主要包含以下几个模块：1) 视觉特征提取模块：用于从多视角图像中提取视觉特征。2) 空间引导模块：利用前馈3D重建的结构感知能力，为MLLM提供空间引导。3) 结构增强模块(SE)：通过视图内和视图间注意力机制，捕获视图内的依赖关系和视图间的对应关系，并结合多级位置编码，将视觉表示与空间位置和视点信息相关联。4) 多模态融合模块：将视觉特征、空间引导和语言特征进行融合，用于最终的3D目标定位。

**关键创新**：S$^2$-MLLM的关键创新在于提出了隐式的空间推理方法，避免了显式的点云重建，从而提高了效率和空间推理能力。此外，结构增强模块(SE)通过视图内和视图间注意力机制以及多级位置编码，更有效地利用了多视角信息，进一步提升了模型的性能。

**关键设计**：结构增强模块(SE)是关键设计之一。它包含intra-view attention和inter-view attention两个部分，分别用于捕获视图内的依赖关系和视图间的对应关系。多级位置编码将视觉特征与空间位置和视点信息关联起来，从而增强了模型的结构感知能力。损失函数方面，可能采用了交叉熵损失或类似的损失函数，用于训练模型进行3D目标定位。

## 📊 实验亮点

S$^2$-MLLM在ScanRefer、Nr3D和Sr3D数据集上取得了显著的性能提升。例如，在ScanRefer数据集上，S$^2$-MLLM的性能超过了现有最佳方法，实现了显著的性能提升。实验结果表明，S$^2$-MLLM具有卓越的性能、泛化性和效率。

## 🎯 应用场景

S$^2$-MLLM在具身智能、机器人导航、虚拟现实和增强现实等领域具有广泛的应用前景。它可以帮助机器人在复杂的三维环境中理解自然语言指令，并准确地定位目标物体，从而实现更智能、更高效的人机交互。

## 📄 摘要（原文）

> 3D Visual Grounding (3DVG) focuses on locating objects in 3D scenes based on natural language descriptions, serving as a fundamental task for embodied AI and robotics. Recent advances in Multi-modal Large Language Models (MLLMs) have motivated research into extending them to 3DVG. However, MLLMs primarily process 2D visual inputs and struggle with understanding 3D spatial structure of scenes solely from these limited perspectives. Existing methods mainly utilize viewpoint-dependent rendering of reconstructed point clouds to provide explicit structural guidance for MLLMs in 3DVG tasks, leading to inefficiency and limited spatial reasoning. To address this issue, we propose S$^2$-MLLM, an efficient framework that enhances spatial reasoning in MLLMs through implicit spatial reasoning. We introduce a spatial guidance strategy that leverages the structure awareness of feed-forward 3D reconstruction. By acquiring 3D structural understanding during training, our model can implicitly reason about 3D scenes without relying on inefficient point cloud reconstruction. Moreover, we propose a structure-enhanced module (SE), which first employs intra-view and inter-view attention mechanisms to capture dependencies within views and correspondences across views. The module further integrates multi-level position encoding to associate visual representations with spatial positions and viewpoint information, enabling more accurate structural understanding. Extensive experiments demonstrate that S$^2$-MLLM unifies superior performance, generalization, and efficiency, achieving significant performance over existing methods across the ScanRefer, Nr3D, and Sr3D datasets. Code will be available upon acceptance.

