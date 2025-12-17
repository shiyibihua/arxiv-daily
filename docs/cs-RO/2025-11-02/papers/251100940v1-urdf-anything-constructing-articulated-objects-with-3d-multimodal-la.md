---
layout: default
title: URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model
---

# URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.00940" target="_blank" class="toolbar-btn">arXiv: 2511.00940v1</a>
    <a href="https://arxiv.org/pdf/2511.00940.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00940v1" 
            onclick="toggleFavorite(this, '2511.00940v1', 'URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhe Li, Xiang Bai, Jieyu Zhang, Zhuangzhe Wu, Che Xu, Ying Li, Chengkai Hou, Shanghang Zhang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-11-02

**备注**: Accepted to the 39th Conference on Neural Information Processing Systems (NeurIPS 2025)

---

## 💡 一句话要点

**URDF-Anything：基于3D多模态语言模型构建可动对象**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `可动对象` `数字孪生` `3D多模态LLM` `点云处理` `运动学参数估计`

## 📋 核心要点

1. 现有方法在构建可动对象数字孪生时，需要耗时的人工建模或复杂的多阶段流程，效率低下。
2. URDF-Anything利用3D多模态LLM，通过点云和文本输入，自回归预测几何分割和运动学参数，实现端到端自动重建。
3. 实验表明，URDF-Anything在几何分割、运动学参数预测和物理可执行性方面均显著优于现有方法，并具有良好的泛化能力。

## 📝 摘要（中文）

本文提出URDF-Anything，一个基于3D多模态大型语言模型(MLLM)的端到端自动重建框架，用于构建可动对象的精确数字孪生。该框架采用基于点云和文本多模态输入的自回归预测，联合优化几何分割和运动学参数预测。它实现了一种特殊的$[SEG]$ token机制，直接与点云特征交互，实现细粒度的部件级分割，同时保持与运动学参数预测的一致性。在模拟和真实世界数据集上的实验表明，该方法在几何分割（mIoU提升17%）、运动学参数预测（平均误差降低29%）和物理可执行性（超过基线50%）方面显著优于现有方法。该方法表现出良好的泛化能力，即使在训练集之外的对象上也能表现良好。这项工作为机器人仿真构建数字孪生提供了一种有效的解决方案，显著增强了sim-to-real的迁移能力。

## 🔬 方法详解

**问题定义**：论文旨在解决可动对象数字孪生构建的问题，现有方法主要依赖于人工建模或复杂的多阶段流程，成本高昂且效率低下。这些方法难以自动、精确地重建对象的几何结构和运动学参数，限制了机器人在仿真环境中的训练和具身智能世界模型的构建。

**核心思路**：论文的核心思路是利用3D多模态大型语言模型(MLLM)，将几何信息（点云）和语义信息（文本描述）融合，通过自回归预测的方式，同时优化几何分割和运动学参数预测。这种端到端的方法避免了传统方法中复杂的中间步骤，提高了重建效率和精度。

**技术框架**：URDF-Anything的整体框架包括以下几个主要模块：1) 多模态输入模块：接收点云和文本描述作为输入；2) 特征提取模块：提取点云和文本的特征表示；3) 自回归预测模块：基于提取的特征，自回归地预测部件分割结果和运动学参数；4) $[SEG]$ token机制：通过特殊的token与点云特征交互，实现细粒度的部件级分割。整个流程是端到端可训练的。

**关键创新**：该论文最重要的技术创新点在于将3D多模态LLM应用于可动对象的数字孪生构建，并提出了$[SEG]$ token机制。与现有方法相比，该方法能够同时处理几何和语义信息，实现更精确的部件分割和运动学参数预测。$[SEG]$ token机制允许模型直接操作点云特征，从而实现细粒度的分割控制。

**关键设计**：在技术细节方面，论文可能采用了Transformer架构作为LLM的基础，并设计了特定的损失函数来联合优化几何分割和运动学参数预测。$[SEG]$ token的具体实现方式（例如，如何与点云特征进行交互，如何影响分割结果）是关键的设计细节。具体的参数设置和网络结构需要在论文中进一步查找。

## 📊 实验亮点

URDF-Anything在模拟和真实世界数据集上均取得了显著的性能提升。在几何分割方面，mIoU指标提升了17%。在运动学参数预测方面，平均误差降低了29%。在物理可执行性方面，超过基线方法50%。这些结果表明，URDF-Anything能够有效地构建可动对象的精确数字孪生，并具有良好的泛化能力。

## 🎯 应用场景

URDF-Anything在机器人仿真训练、具身智能世界模型构建等领域具有广泛的应用前景。它可以用于快速构建各种可动对象的数字孪生，从而加速机器人的开发和部署。此外，该方法还可以应用于虚拟现实、增强现实等领域，为用户提供更逼真的交互体验。未来，该技术有望进一步扩展到更复杂的场景和对象，例如人体建模、工业自动化等。

## 📄 摘要（原文）

> Constructing accurate digital twins of articulated objects is essential for robotic simulation training and embodied AI world model building, yet historically requires painstaking manual modeling or multi-stage pipelines. In this work, we propose \textbf{URDF-Anything}, an end-to-end automatic reconstruction framework based on a 3D multimodal large language model (MLLM). URDF-Anything utilizes an autoregressive prediction framework based on point-cloud and text multimodal input to jointly optimize geometric segmentation and kinematic parameter prediction. It implements a specialized $[SEG]$ token mechanism that interacts directly with point cloud features, enabling fine-grained part-level segmentation while maintaining consistency with the kinematic parameter predictions. Experiments on both simulated and real-world datasets demonstrate that our method significantly outperforms existing approaches regarding geometric segmentation (mIoU 17\% improvement), kinematic parameter prediction (average error reduction of 29\%), and physical executability (surpassing baselines by 50\%). Notably, our method exhibits excellent generalization ability, performing well even on objects outside the training set. This work provides an efficient solution for constructing digital twins for robotic simulation, significantly enhancing the sim-to-real transfer capability.

