---
layout: default
title: FusionFM: All-in-One Multi-Modal Image Fusion with Flow Matching
---

# FusionFM: All-in-One Multi-Modal Image Fusion with Flow Matching

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.13794" target="_blank" class="toolbar-btn">arXiv: 2511.13794v1</a>
    <a href="https://arxiv.org/pdf/2511.13794.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13794v1" 
            onclick="toggleFavorite(this, '2511.13794v1', 'FusionFM: All-in-One Multi-Modal Image Fusion with Flow Matching')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Huayi Zhu, Xiu Shu, Youqiang Xiong, Qiao Liu, Rui Chen, Di Yuan, Xiaojun Chang, Zhenyu He

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-17

**🔗 代码/项目**: [GITHUB](https://github.com/Ist-Zhy/FusionFM)

---

## 💡 一句话要点

**提出FusionFM，利用Flow Matching实现高效多模态图像融合**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多模态图像融合` `Flow Matching` `概率传输` `伪标签学习` `持续学习`

## 📋 核心要点

1. 现有图像融合方法依赖于特定任务模型，存在训练成本高、泛化性差的问题，生成式方法推理速度慢。
2. 本文提出FusionFM，将图像融合建模为概率传输过程，利用Flow Matching提高采样效率和结构一致性。
3. 实验结果表明，FusionFM在多种融合任务上表现出色，显著提升采样效率，并保持模型轻量化。

## 📝 摘要（中文）

当前的多模态图像融合方法通常依赖于特定任务的模型，导致训练成本高且可扩展性有限。生成式方法提供了一个统一的建模视角，但由于从噪声到图像的复杂采样轨迹，通常存在推理速度慢的问题。为了解决这个问题，本文将图像融合定义为从源模态到融合图像分布的直接概率传输，利用Flow Matching范式来提高采样效率和结构一致性。为了缓解缺乏高质量融合图像进行监督的问题，我们收集了多个最先进模型的融合结果作为先验，并采用任务感知的选择函数来选择每个任务最可靠的伪标签。我们进一步引入了一个Fusion Refiner模块，该模块采用分而治之的策略来系统地识别、分解和增强所选伪标签中退化的组件。对于多任务场景，我们整合了弹性权重巩固和经验回放机制，从参数稳定性和记忆保持的角度来保持跨任务性能并增强持续学习能力。我们的方法在不同的融合任务中实现了有竞争力的性能，同时显著提高了采样效率并保持了轻量级的模型设计。

## 🔬 方法详解

**问题定义**：现有的多模态图像融合方法通常针对特定任务设计，缺乏通用性，训练成本高昂。生成式方法虽然提供了一种统一的建模框架，但由于其复杂的采样过程，推理速度较慢，难以满足实时性要求。此外，缺乏高质量的融合图像作为监督信号也是一个挑战。

**核心思路**：本文的核心思路是将图像融合问题转化为一个概率传输问题，即如何将源模态的图像分布直接映射到融合图像的分布。通过引入Flow Matching范式，可以学习一个连续的向量场，使得从源模态到融合图像的传输过程更加高效和稳定，从而提高采样效率和结构一致性。

**技术框架**：FusionFM的整体框架主要包括三个部分：首先，利用多个先进的融合模型生成伪标签；然后，通过一个任务感知的选择函数，选择最可靠的伪标签作为训练目标；最后，使用一个Fusion Refiner模块来精细化伪标签，提升融合质量。对于多任务学习，采用弹性权重巩固和经验回放机制来保持跨任务性能。

**关键创新**：该论文的关键创新在于将Flow Matching范式引入到多模态图像融合领域，并提出了一种基于伪标签和Fusion Refiner的训练策略。Flow Matching能够显著提高采样效率，而伪标签和Fusion Refiner则能够缓解缺乏高质量监督信号的问题。此外，针对多任务学习，采用了弹性权重巩固和经验回放机制，提升了模型的泛化能力。

**关键设计**：任务感知的选择函数用于选择最可靠的伪标签，其具体实现方式未知。Fusion Refiner模块采用分而治之的策略，具体如何分解和增强退化组件也未知。弹性权重巩固和经验回放机制的具体参数设置和实现细节未知。损失函数的设计也未知。

## 📊 实验亮点

该方法在多种图像融合任务上取得了有竞争力的性能，并在显著提高了采样效率的同时，保持了模型设计的轻量化。具体的性能数据和对比基线未在摘要中明确给出，但强调了在效率和模型大小上的优势。

## 🎯 应用场景

该研究成果可应用于医学影像融合（如CT与MRI融合）、遥感图像融合（如可见光与红外图像融合）、以及自动驾驶中的多传感器数据融合等领域。通过提高融合效率和质量，可以辅助医生诊断、提升遥感图像解译精度、增强自动驾驶系统的环境感知能力，具有重要的实际应用价值。

## 📄 摘要（原文）

> Current multi-modal image fusion methods typically rely on task-specific models, leading to high training costs and limited scalability. While generative methods provide a unified modeling perspective, they often suffer from slow inference due to the complex sampling trajectories from noise to image. To address this, we formulate image fusion as a direct probabilistic transport from source modalities to the fused image distribution, leveraging the flow matching paradigm to improve sampling efficiency and structural consistency. To mitigate the lack of high-quality fused images for supervision, we collect fusion results from multiple state-of-the-art models as priors, and employ a task-aware selection function to select the most reliable pseudo-labels for each task. We further introduce a Fusion Refiner module that employs a divide-and-conquer strategy to systematically identify, decompose, and enhance degraded components in selected pseudo-labels. For multi-task scenarios, we integrate elastic weight consolidation and experience replay mechanisms to preserve cross-task performance and enhance continual learning ability from both parameter stability and memory retention perspectives. Our approach achieves competitive performance across diverse fusion tasks, while significantly improving sampling efficiency and maintaining a lightweight model design. The code will be available at: https://github.com/Ist-Zhy/FusionFM.

