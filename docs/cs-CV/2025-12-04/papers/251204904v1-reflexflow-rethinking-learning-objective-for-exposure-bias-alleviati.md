---
layout: default
title: ReflexFlow: Rethinking Learning Objective for Exposure Bias Alleviation in Flow Matching
---

# ReflexFlow: Rethinking Learning Objective for Exposure Bias Alleviation in Flow Matching

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.04904" target="_blank" class="toolbar-btn">arXiv: 2512.04904v1</a>
    <a href="https://arxiv.org/pdf/2512.04904.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04904v1" 
            onclick="toggleFavorite(this, '2512.04904v1', 'ReflexFlow: Rethinking Learning Objective for Exposure Bias Alleviation in Flow Matching')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Guanbo Huang, Jingjia Mao, Fanding Huang, Fengkai Liu, Xiangyang Luo, Yaoyuan Liang, Jiasheng Lu, Xiaoe Wang, Pei Liu, Ruiliu Fu, Shao-Lun Huang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-04

---

## 💡 一句话要点

**ReflexFlow：通过反思式优化Flow Matching学习目标，缓解生成模型的暴露偏差**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Flow Matching` `暴露偏差` `生成模型` `反思学习` `图像生成`

## 📋 核心要点

1. Flow Matching方法受暴露偏差影响，训练与推理存在差异，导致生成质量下降。
2. ReflexFlow通过反思式优化学习目标，动态纠正暴露偏差，提升模型对有偏差输入的泛化能力。
3. 实验表明，ReflexFlow在多个数据集上优于现有方法，显著降低了FID，提升了生成质量。

## 📝 摘要（中文）

尽管Flow Matching方法最近取得了显著进展，但由于训练和推理之间的差异，仍然存在暴露偏差问题。本文研究了Flow Matching中暴露偏差的根本原因，包括：（1）模型在训练期间缺乏对有偏差输入的泛化能力；（2）早期去噪过程中捕获的低频内容不足，导致偏差累积。基于这些见解，我们提出了ReflexFlow，这是一种简单有效的Flow Matching学习目标的反思式改进，可以动态纠正暴露偏差。ReflexFlow由两个组件组成：（1）反漂移校正（ADR），它利用训练时程采样下重新设计的损失函数，反思性地调整有偏差输入的预测目标；（2）频率补偿（FC），它反思缺失的低频分量，并通过使用暴露偏差重新加权损失来补偿它们。ReflexFlow是模型无关的，与所有Flow Matching框架兼容，并提高了跨数据集的生成质量。在CIFAR-10、CelebA-64和ImageNet-256上的实验表明，ReflexFlow在缓解暴露偏差方面优于现有方法，在CelebA-64上实现了35.65%的FID降低。

## 🔬 方法详解

**问题定义**：Flow Matching方法在图像生成任务中表现出色，但训练和推理阶段存在暴露偏差，即模型在训练时只接触真实数据分布，而在推理时需要处理模型自身生成的、可能存在偏差的数据分布。这种偏差导致模型在推理时性能下降，生成质量降低。现有方法难以有效解决这一问题，尤其是在早期去噪阶段，低频信息捕获不足会导致偏差累积。

**核心思路**：ReflexFlow的核心思路是通过反思式学习目标来动态纠正暴露偏差。具体来说，它通过两个关键组件：反漂移校正（ADR）和频率补偿（FC），分别解决模型对有偏差输入的泛化能力不足和早期去噪过程中低频信息缺失的问题。这种反思式设计使得模型能够更好地适应推理阶段的数据分布，从而缓解暴露偏差。

**技术框架**：ReflexFlow可以集成到现有的Flow Matching框架中。其整体流程如下：首先，使用ADR模块，在训练过程中，通过scheduled sampling引入一定比例的生成样本，并利用重新设计的损失函数，反思性地调整这些有偏差输入的预测目标，从而提高模型对有偏差输入的鲁棒性。然后，使用FC模块，反思缺失的低频分量，并通过使用暴露偏差重新加权损失来补偿它们，从而确保模型能够捕获足够的低频信息。这两个模块共同作用，缓解暴露偏差，提高生成质量。

**关键创新**：ReflexFlow的关键创新在于其反思式学习目标的设计。与现有方法不同，ReflexFlow不是简单地对数据进行增强或正则化，而是通过动态调整学习目标，使模型能够更好地适应推理阶段的数据分布。ADR模块和FC模块分别从不同的角度缓解暴露偏差，共同提升了生成模型的性能。此外，ReflexFlow是模型无关的，可以方便地集成到各种Flow Matching框架中。

**关键设计**：ADR模块的关键设计在于重新设计的损失函数和scheduled sampling策略。损失函数的设计考虑了有偏差输入的特点，能够更有效地引导模型学习。scheduled sampling策略则控制了训练过程中生成样本的比例，避免模型过度拟合生成数据。FC模块的关键设计在于如何准确估计缺失的低频分量，并根据估计结果对损失函数进行重新加权。具体的参数设置和网络结构需要根据具体的Flow Matching框架进行调整。

## 📊 实验亮点

ReflexFlow在CIFAR-10、CelebA-64和ImageNet-256等数据集上进行了实验，结果表明其优于现有方法。特别是在CelebA-64数据集上，ReflexFlow实现了35.65%的FID降低，显著提升了生成质量。实验结果验证了ReflexFlow在缓解暴露偏差方面的有效性。

## 🎯 应用场景

ReflexFlow可应用于图像生成、图像编辑、视频生成等领域。通过缓解暴露偏差，可以提高生成模型的稳定性和生成质量，从而在艺术创作、内容生成、数据增强等领域发挥重要作用。未来，该方法有望扩展到其他生成模型和任务中，例如文本生成、音频生成等。

## 📄 摘要（原文）

> Despite tremendous recent progress, Flow Matching methods still suffer from exposure bias due to discrepancies in training and inference. This paper investigates the root causes of exposure bias in Flow Matching, including: (1) the model lacks generalization to biased inputs during training, and (2) insufficient low-frequency content captured during early denoising, leading to accumulated bias. Based on these insights, we propose ReflexFlow, a simple and effective reflexive refinement of the Flow Matching learning objective that dynamically corrects exposure bias. ReflexFlow consists of two components: (1) Anti-Drift Rectification (ADR), which reflexively adjusts prediction targets for biased inputs utilizing a redesigned loss under training-time scheduled sampling; and (2) Frequency Compensation (FC), which reflects on missing low-frequency components and compensates them by reweighting the loss using exposure bias. ReflexFlow is model-agnostic, compatible with all Flow Matching frameworks, and improves generation quality across datasets. Experiments on CIFAR-10, CelebA-64, and ImageNet-256 show that ReflexFlow outperforms prior approaches in mitigating exposure bias, achieving a 35.65% reduction in FID on CelebA-64.

