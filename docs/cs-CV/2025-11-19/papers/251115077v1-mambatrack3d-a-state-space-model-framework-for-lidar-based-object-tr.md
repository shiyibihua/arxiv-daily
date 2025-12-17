---
layout: default
title: MambaTrack3D: A State Space Model Framework for LiDAR-Based Object Tracking under High Temporal Variation
---

# MambaTrack3D: A State Space Model Framework for LiDAR-Based Object Tracking under High Temporal Variation

**arXiv**: [2511.15077v1](https://arxiv.org/abs/2511.15077) | [PDF](https://arxiv.org/pdf/2511.15077.pdf)

**作者**: Shengjing Tian, Yinan Han, Xiantong Zhao, Xuehu Liu, Qi Lang

**分类**: cs.CV

**发布日期**: 2025-11-19

**备注**: This work has been submitted to a journal for possible publication

---

## 💡 一句话要点

**MambaTrack3D：基于状态空间模型的LiDAR高时间变化目标跟踪框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D目标跟踪` `LiDAR点云` `状态空间模型` `Mamba` `高时间变化` `帧间传播` `特征增强`

## 📋 核心要点

1. 现有基于记忆的3D目标跟踪方法在高时间变化场景下计算复杂度高，存在时间冗余，且对几何先验利用不足。
2. MambaTrack3D利用状态空间模型Mamba，通过帧间传播建模时序关系，并设计分组特征增强模块减少时间冗余。
3. 实验表明，MambaTrack3D在HTV和标准数据集上均优于现有方法，实现了精度和效率的平衡。

## 📝 摘要（中文）

本文提出MambaTrack3D，一个面向高时间变化(HTV)场景的LiDAR点云单目标跟踪框架，该框架基于状态空间模型Mamba构建。针对现有基于记忆的跟踪器计算复杂度高、时间冗余以及几何先验利用不足等问题，设计了基于Mamba的帧间传播(MIP)模块，以高效的帧间传播取代传统的单帧特征提取，实现近线性复杂度，并显式地建模跨历史帧的空间关系。此外，引入分组特征增强模块(GFEM)在通道级别分离前景和背景语义，从而减少记忆库中的时间冗余。在KITTI-HTV和nuScenes-HTV基准测试上的大量实验表明，MambaTrack3D始终优于面向HTV和正常场景的跟踪器，在中等时间间隔下，成功率和精度分别比HVTrack提高了6.5%和9.5%。在标准KITTI数据集上，MambaTrack3D与最先进的正常场景跟踪器相比仍具有很强的竞争力，证实了其强大的泛化能力。总体而言，MambaTrack3D实现了卓越的精度-效率权衡，在专门的HTV和传统跟踪场景中均表现出强大的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决LiDAR点云中，在高时间变化（HTV）场景下的单目标跟踪问题。现有基于记忆的跟踪器，如HVTrack，在处理HTV数据时，面临计算复杂度高（通常是二次的）、时间冗余以及对几何先验信息利用不足的挑战。这些问题导致跟踪精度下降和计算效率降低。

**核心思路**：MambaTrack3D的核心思路是利用状态空间模型Mamba的优势，进行高效的帧间信息传播，并减少特征中的时间冗余。Mamba模型具有线性复杂度，能够有效建模长时序依赖关系。通过显式地建模跨帧的空间关系，并分离前景和背景语义，可以提升跟踪的鲁棒性和效率。

**技术框架**：MambaTrack3D的整体框架包含两个主要模块：Mamba-based Inter-frame Propagation (MIP)模块和Grouped Feature Enhancement Module (GFEM)。首先，MIP模块利用Mamba模型进行帧间特征传播，提取时序信息。然后，GFEM模块在通道级别分离前景和背景语义，减少时间冗余。最后，利用提取的特征进行目标状态估计。

**关键创新**：MambaTrack3D的关键创新在于将状态空间模型Mamba引入到3D目标跟踪领域，并设计了MIP模块来实现高效的帧间传播。与传统的单帧特征提取方法相比，MIP模块能够更好地建模时序关系，并降低计算复杂度。GFEM模块通过分组特征增强，有效减少了特征中的时间冗余，提升了跟踪精度。

**关键设计**：MIP模块使用Mamba模型进行特征传播，具体结构细节未知（论文未详细描述Mamba的具体配置）。GFEM模块将特征通道分为多个组，分别处理前景和背景语义。损失函数的设计也未知，但推测会包含跟踪损失和可能的分组损失，以优化模型的性能。具体的参数设置和网络结构细节在论文中可能有所补充。

## 📊 实验亮点

MambaTrack3D在KITTI-HTV和nuScenes-HTV基准测试上显著优于现有方法。与HVTrack相比，在中等时间间隔下，成功率和精度分别提高了6.5%和9.5%。此外，在标准KITTI数据集上，MambaTrack3D也表现出很强的竞争力，证明了其良好的泛化能力。这些实验结果表明，MambaTrack3D在精度和效率之间取得了良好的平衡。

## 🎯 应用场景

MambaTrack3D在自动驾驶、机器人导航、智能监控等领域具有广泛的应用前景。尤其是在需要处理高动态环境和快速变化场景的应用中，例如城市交通、无人机跟踪等，该方法能够提供更准确、更高效的目标跟踪能力，从而提升系统的整体性能和安全性。

## 📄 摘要（原文）

> Dynamic outdoor environments with high temporal variation (HTV) pose significant challenges for 3D single object tracking in LiDAR point clouds. Existing memory-based trackers often suffer from quadratic computational complexity, temporal redundancy, and insufficient exploitation of geometric priors. To address these issues, we propose MambaTrack3D, a novel HTV-oriented tracking framework built upon the state space model Mamba. Specifically, we design a Mamba-based Inter-frame Propagation (MIP) module that replaces conventional single-frame feature extraction with efficient inter-frame propagation, achieving near-linear complexity while explicitly modeling spatial relations across historical frames. Furthermore, a Grouped Feature Enhancement Module (GFEM) is introduced to separate foreground and background semantics at the channel level, thereby mitigating temporal redundancy in the memory bank. Extensive experiments on KITTI-HTV and nuScenes-HTV benchmarks demonstrate that MambaTrack3D consistently outperforms both HTV-oriented and normal-scenario trackers, achieving improvements of up to 6.5 success and 9.5 precision over HVTrack under moderate temporal gaps. On the standard KITTI dataset, MambaTrack3D remains highly competitive with state-of-the-art normal-scenario trackers, confirming its strong generalization ability. Overall, MambaTrack3D achieves a superior accuracy-efficiency trade-off, delivering robust performance across both specialized HTV and conventional tracking scenarios.

