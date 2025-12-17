---
layout: default
title: LeCoT: revisiting network architecture for two-view correspondence pruning
---

# LeCoT: revisiting network architecture for two-view correspondence pruning

**arXiv**: [2511.07078v1](https://arxiv.org/abs/2511.07078) | [PDF](https://arxiv.org/pdf/2511.07078.pdf)

**作者**: Luanyuan Dai, Xiaoyu Du, Jinhui Tang

**分类**: cs.CV

**发布日期**: 2025-11-10

**备注**: Just accepted at SCIENCE CHINA Information Sciences

**DOI**: [10.1007/s11432-024-4555-x](https://doi.org/10.1007/s11432-024-4555-x)

**🔗 代码/项目**: [GITHUB](https://github.com/Dailuanyuan2024/LeCoT-Revisiting-Network-Architecture-for-Two-View-Correspondence-Pruning)

---

## 💡 一句话要点

**LeCoT：通过空间-通道融合Transformer改进双视图对应关系剪枝**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `对应关系剪枝` `双视图几何` `Transformer` `全局上下文` `视觉定位`

## 📋 核心要点

1. 现有双视图对应关系剪枝方法依赖MLP，缺乏有效利用全局上下文信息的能力。
2. LeCoT通过空间-通道融合Transformer块，在不同阶段自然地利用全局上下文信息。
3. 实验表明，LeCoT在多个视觉任务中超越了现有最优方法，例如相对姿态估计。

## 📝 摘要（中文）

双视图对应关系剪枝旨在从初始对应关系中准确移除错误对应关系（外点），并广泛应用于各种计算机视觉任务。目前流行的策略采用多层感知机（MLP）作为骨干网络，并辅以额外的模块来增强网络处理上下文信息的能力，而这正是MLP的已知局限性。与此相反，我们引入了一种新颖的视角，无需额外的设计模块即可捕获对应关系上下文信息。为此，我们设计了一个名为LeCoT的双视图对应关系剪枝网络，该网络可以自然地利用不同阶段的全局上下文信息。具体来说，LeCoT的核心设计是空间-通道融合Transformer块，这是一种新提出的组件，可有效利用稀疏对应关系中的空间和通道全局上下文信息。此外，我们集成了所提出的预测块，该预测块利用来自中间阶段的对应关系特征来生成概率集，该概率集充当后续学习阶段的指导信息，从而使网络能够更有效地捕获鲁棒的全局上下文信息。值得注意的是，此预测块会逐步细化概率集，从而缓解传统方法中常见的信息丢失问题。大量的实验证明，所提出的LeCoT在对应关系剪枝、相对姿态估计、单应性估计、视觉定位和3D重建任务中均优于最先进的方法。代码已在https://github.com/Dailuanyuan2024/LeCoT-Revisiting-Network-Architecture-for-Two-View-Correspondence-Pruning提供。

## 🔬 方法详解

**问题定义**：双视图对应关系剪枝旨在从两幅图像的初始匹配关系中去除错误匹配（外点），从而提高后续任务的精度。现有方法，特别是基于MLP的方法，难以有效地捕捉和利用全局上下文信息，导致剪枝效果不佳。

**核心思路**：LeCoT的核心思路是通过设计一种新的网络架构，使其能够自然地、有效地利用全局上下文信息。该架构的核心是空间-通道融合Transformer块，它能够同时考虑空间和通道维度的全局信息，从而更好地理解对应关系之间的相互依赖性。

**技术框架**：LeCoT的整体架构包含多个阶段，每个阶段都包含空间-通道融合Transformer块。网络首先提取对应关系的特征，然后通过多个Transformer块进行处理，逐步提取全局上下文信息。此外，LeCoT还包含一个预测块，该块利用中间阶段的特征来生成概率集，指导后续学习。概率集会逐步细化，缓解信息丢失问题。

**关键创新**：LeCoT的关键创新在于空间-通道融合Transformer块的设计。与传统的Transformer只关注空间或通道维度不同，该模块同时考虑了两个维度，从而更全面地捕捉全局上下文信息。此外，逐步细化的预测块也是一个创新点，它能够更有效地利用中间阶段的特征，提高剪枝的准确性。

**关键设计**：空间-通道融合Transformer块的具体实现细节未知，但可以推测其采用了某种形式的注意力机制，以便在空间和通道维度上选择性地关注重要信息。预测块的具体结构和损失函数也未知，但可以推测其目标是最小化预测概率与真实标签之间的差异。

## 📊 实验亮点

LeCoT在多个任务上取得了显著的性能提升。在对应关系剪枝任务上，LeCoT优于现有最优方法。在相对姿态估计、单应性估计、视觉定位和3D重建等下游任务中，LeCoT也取得了更好的结果，证明了其有效性和泛化能力。具体的性能数据和提升幅度需要在论文中查找。

## 🎯 应用场景

LeCoT在机器人导航、增强现实、三维重建、视觉定位等领域具有广泛的应用前景。准确的对应关系剪枝能够提高这些应用中位姿估计、地图构建等关键任务的精度和鲁棒性，从而提升整体系统性能。该研究的未来影响在于推动计算机视觉领域对上下文信息利用的深入研究。

## 📄 摘要（原文）

> Two-view correspondence pruning aims to accurately remove incorrect correspondences (outliers) from initial ones and is widely applied to various computer vision tasks. Current popular strategies adopt multilayer perceptron (MLP) as the backbone, supplemented by additional modules to enhance the network ability to handle context information, which is a known limitation of MLPs. In contrast, we introduce a novel perspective for capturing correspondence context information without extra design modules. To this end, we design a two-view correspondence pruning network called LeCoT, which can naturally leverage global context information at different stages. Specifically, the core design of LeCoT is the Spatial-Channel Fusion Transformer block, a newly proposed component that efficiently utilizes both spatial and channel global context information among sparse correspondences. In addition, we integrate the proposed prediction block that utilizes correspondence features from intermediate stages to generate a probability set, which acts as guiding information for subsequent learning phases, allowing the network to more effectively capture robust global context information. Notably, this prediction block progressively refines the probability set, thereby mitigating the issue of information loss that is common in the traditional one. Extensive experiments prove that the proposed LeCoT outperforms state-of-the-art methods in correspondence pruning, relative pose estimation, homography estimation, visual localization, and $3$D~reconstruction tasks. The code is provided in https://github.com/Dailuanyuan2024/LeCoT-Revisiting-Network-Architecture-for-Two-View-Correspondence-Pruning.

