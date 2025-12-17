---
layout: default
title: CADTrack: Learning Contextual Aggregation with Deformable Alignment for Robust RGBT Tracking
---

# CADTrack: Learning Contextual Aggregation with Deformable Alignment for Robust RGBT Tracking

**arXiv**: [2511.17967v1](https://arxiv.org/abs/2511.17967) | [PDF](https://arxiv.org/pdf/2511.17967.pdf)

**作者**: Hao Li, Yuhao Wang, Xiantao Hu, Wenning Hao, Pingping Zhang, Dong Wang, Huchuan Lu

**分类**: cs.CV

**发布日期**: 2025-11-22

**备注**: Accepted by AAAI2026. More modifications may be performed

**🔗 代码/项目**: [GITHUB](https://github.com/IdolLab/CADTrack)

---

## 💡 一句话要点

**CADTrack：面向鲁棒RGBT跟踪，提出基于可变形对齐的上下文聚合方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `RGBT跟踪` `跨模态融合` `可变形对齐` `上下文聚合` `Mamba` `混合专家模型` `目标跟踪`

## 📋 核心要点

1. 现有RGBT跟踪器难以有效处理模态差异，导致跨模态信息融合受阻，影响跟踪精度。
2. CADTrack通过Mamba特征交互、上下文聚合和可变形对齐，实现鲁棒的跨模态特征表示和融合。
3. 实验表明，CADTrack在多个RGBT跟踪基准上表现出色，验证了其有效性和优越性。

## 📝 摘要（中文）

RGB-Thermal (RGBT) 跟踪旨在利用可见光和热红外模态进行鲁棒的全天候目标跟踪。然而，现有的RGBT跟踪器难以解决模态差异，这对鲁棒的特征表示提出了巨大的挑战。这种限制阻碍了有效的跨模态信息传播和融合，从而显著降低了跟踪精度。为了解决这个限制，我们提出了一个新颖的基于可变形对齐的上下文聚合框架，称为CADTrack，用于RGBT跟踪。具体来说，我们首先部署了基于Mamba的特征交互（MFI），它通过状态空间模型建立高效的特征交互。该交互模块可以以线性复杂度运行，降低计算成本并提高特征辨别能力。然后，我们提出了上下文聚合模块（CAM），该模块通过基于混合专家（MoE）的稀疏门控动态激活骨干网络层。该模块可以编码来自跨层特征的互补上下文信息。最后，我们提出了可变形对齐模块（DAM），以集成可变形采样和时间传播，从而减轻空间错位和定位漂移。通过上述组件，我们的CADTrack在复杂场景中实现了鲁棒而准确的跟踪。在五个RGBT跟踪基准上的大量实验验证了我们提出的方法的有效性。

## 🔬 方法详解

**问题定义**：RGBT跟踪旨在利用可见光和热红外图像进行全天候目标跟踪。现有方法的主要痛点在于如何有效处理RGB和Thermal图像之间的模态差异，这种差异会导致特征表示不准确，进而影响跨模态信息融合和跟踪性能。现有方法在处理模态差异和空间错位方面存在不足，容易导致跟踪失败。

**核心思路**：CADTrack的核心思路是通过可变形对齐的上下文聚合来增强特征表示的鲁棒性。具体来说，利用Mamba结构进行高效的特征交互，利用混合专家模型进行上下文聚合，并利用可变形采样和时间传播进行空间对齐。这种设计旨在缓解模态差异和空间错位带来的影响，从而提高跟踪精度和鲁棒性。

**技术框架**：CADTrack的整体框架包含三个主要模块：Mamba-based Feature Interaction (MFI)、Contextual Aggregation Module (CAM) 和 Deformable Alignment Module (DAM)。首先，MFI模块利用Mamba结构进行跨模态特征交互，增强特征的辨别能力。然后，CAM模块通过混合专家模型动态聚合来自不同骨干网络层的上下文信息，丰富特征表示。最后，DAM模块利用可变形采样和时间传播进行空间对齐，减少定位漂移。

**关键创新**：CADTrack的关键创新在于三个方面：1) 引入Mamba结构进行高效的特征交互，降低计算成本；2) 提出基于混合专家模型的上下文聚合模块，动态选择和聚合不同层的特征；3) 设计可变形对齐模块，通过可变形采样和时间传播来缓解空间错位。这些创新使得CADTrack能够更有效地处理模态差异和空间错位，从而提高跟踪性能。

**关键设计**：MFI模块采用Mamba结构，通过状态空间模型进行特征交互，复杂度为线性级别。CAM模块使用混合专家模型，通过稀疏门控动态选择骨干网络层，实现上下文信息的有效聚合。DAM模块采用可变形卷积进行采样，并结合时间传播来预测目标位置的变化。损失函数方面，可能采用了常见的跟踪损失函数，如IoU损失或中心点距离损失，具体细节未知。

## 📊 实验亮点

CADTrack在五个RGBT跟踪基准上进行了大量实验，验证了其有效性。论文中提到该方法在复杂场景中实现了鲁棒而准确的跟踪，但具体的性能数据和提升幅度未知。开源代码的发布也为后续研究提供了便利。

## 🎯 应用场景

CADTrack在安防监控、自动驾驶、机器人导航等领域具有广泛的应用前景。该方法能够有效应对复杂光照条件和恶劣天气环境下的目标跟踪挑战，提高系统的可靠性和智能化水平。未来，可以进一步探索其在无人机巡检、搜救等领域的应用。

## 📄 摘要（原文）

> RGB-Thermal (RGBT) tracking aims to exploit visible and thermal infrared modalities for robust all-weather object tracking. However, existing RGBT trackers struggle to resolve modality discrepancies, which poses great challenges for robust feature representation. This limitation hinders effective cross-modal information propagation and fusion, which significantly reduces the tracking accuracy. To address this limitation, we propose a novel Contextual Aggregation with Deformable Alignment framework called CADTrack for RGBT Tracking. To be specific, we first deploy the Mamba-based Feature Interaction (MFI) that establishes efficient feature interaction via state space models. This interaction module can operate with linear complexity, reducing computational cost and improving feature discrimination. Then, we propose the Contextual Aggregation Module (CAM) that dynamically activates backbone layers through sparse gating based on the Mixture-of-Experts (MoE). This module can encode complementary contextual information from cross-layer features. Finally, we propose the Deformable Alignment Module (DAM) to integrate deformable sampling and temporal propagation, mitigating spatial misalignment and localization drift. With the above components, our CADTrack achieves robust and accurate tracking in complex scenarios. Extensive experiments on five RGBT tracking benchmarks verify the effectiveness of our proposed method. The source code is released at https://github.com/IdolLab/CADTrack.

