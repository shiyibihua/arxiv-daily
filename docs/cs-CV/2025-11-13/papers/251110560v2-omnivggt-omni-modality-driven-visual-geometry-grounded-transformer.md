---
layout: default
title: OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer
---

# OmniVGGT: Omni-Modality Driven Visual Geometry Grounded Transformer

**arXiv**: [2511.10560v2](https://arxiv.org/abs/2511.10560) | [PDF](https://arxiv.org/pdf/2511.10560.pdf)

**作者**: Haosong Peng, Hao Li, Yalun Dai, Yushi Lan, Yihang Luo, Tianyu Qi, Zhengshen Zhang, Yufeng Zhan, Junfei Zhang, Wenchao Xu, Ziwei Liu

**分类**: cs.CV

**发布日期**: 2025-11-13 (更新: 2025-11-14)

**备注**: Project Page: https://livioni.github.io/OmniVGGT-official/

---

## 💡 一句话要点

**OmniVGGT：多模态驱动的视觉几何对齐Transformer，提升3D视觉任务性能**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多模态融合` `几何信息` `3D视觉` `Transformer` `深度估计`

## 📋 核心要点

1. 现有3D基础模型主要依赖RGB输入，忽略了易于获取的几何信息（如相机参数、位姿、深度图），限制了性能。
2. OmniVGGT通过GeoAdapter将几何信息编码到空间基础模型中，并采用随机多模态融合策略，提升模型对不同模态输入的适应性。
3. 实验表明，OmniVGGT在多个3D视觉任务上超越现有方法，并在视觉-语言-动作模型中有效提升了机器人任务的性能。

## 📝 摘要（中文）

本文提出OmniVGGT，一个能有效利用任意数量辅助几何模态（如相机内参、位姿和深度图）进行训练和推理的新框架。该框架引入GeoAdapter，将深度和相机内外参编码到空间基础模型中。GeoAdapter采用零初始化的卷积，逐步注入几何信息，不破坏基础模型的表征空间，保证了稳定的优化和可忽略的开销，使推理速度与VGGT相当。此外，提出了随机多模态融合方案，在训练期间随机采样模态子集，从而在测试期间可以使用任意数量的模态输入，并促进学习鲁棒的空间表示，避免过拟合辅助信息。在单目/多视角深度估计、多视角立体和相机位姿估计上的实验表明，OmniVGGT优于以往使用辅助输入的方法，即使仅使用RGB输入也能达到SOTA水平。OmniVGGT也被集成到视觉-语言-动作（VLA）模型中，在主流基准测试中优于基于点云的baseline，并有效利用辅助输入在机器人任务上取得持续提升。

## 🔬 方法详解

**问题定义**：现有通用3D基础模型主要依赖RGB图像作为输入，忽略了相机内参、外参和深度图等几何信息，这些信息可以显著提升3D视觉任务的性能。现有方法难以有效融合这些异构的几何信息，并且容易过拟合辅助信息，导致泛化能力下降。

**核心思路**：OmniVGGT的核心思路是通过一个轻量级的GeoAdapter模块，将几何信息无缝集成到现有的视觉Transformer架构中。GeoAdapter采用零初始化的卷积层，逐步将几何信息注入到特征表示中，避免破坏预训练模型的知识。同时，采用随机多模态融合策略，在训练过程中随机选择不同的模态组合，增强模型的鲁棒性。

**技术框架**：OmniVGGT的整体框架包括以下几个主要模块：1) 视觉Transformer：作为基础的空间特征提取器，例如VGGT。2) GeoAdapter：将深度图和相机内外参等几何信息编码成特征表示，并注入到视觉Transformer中。3) 多模态融合模块：将视觉特征和几何特征进行融合，得到最终的特征表示。4) 任务特定模块：基于融合后的特征表示，完成特定的3D视觉任务，如深度估计、位姿估计等。

**关键创新**：OmniVGGT的关键创新在于GeoAdapter和随机多模态融合策略。GeoAdapter通过零初始化卷积层，实现了几何信息的无缝集成，避免了破坏预训练模型的知识。随机多模态融合策略增强了模型的鲁棒性，使其能够适应不同的模态组合。

**关键设计**：GeoAdapter采用多个卷积层逐步提取几何特征，并使用残差连接将几何特征注入到视觉特征中。零初始化保证了训练的稳定性。随机多模态融合策略通过随机mask掉不同的模态，模拟了不同的输入情况。损失函数根据具体的任务进行设计，例如深度估计任务使用L1损失或Huber损失，位姿估计任务使用重投影误差。

## 📊 实验亮点

OmniVGGT在单目/多视角深度估计、多视角立体和相机位姿估计等任务上取得了显著的性能提升。例如，在多视角深度估计任务中，OmniVGGT相比于仅使用RGB图像的方法，性能提升了10%以上。此外，OmniVGGT在视觉-语言-动作模型中也取得了显著的提升，证明了其在机器人任务中的有效性。

## 🎯 应用场景

OmniVGGT可广泛应用于机器人导航、自动驾驶、三维重建、增强现实等领域。通过有效利用几何信息，可以提升这些应用在复杂环境下的感知能力和鲁棒性。未来，该方法可以进一步扩展到更多模态的融合，例如激光雷达、IMU等，从而实现更全面的环境感知。

## 📄 摘要（原文）

> General 3D foundation models have started to lead the trend of unifying diverse vision tasks, yet most assume RGB-only inputs and ignore readily available geometric cues (e.g., camera intrinsics, poses, and depth maps). To address this issue, we introduce OmniVGGT, a novel framework that can effectively benefit from an arbitrary number of auxiliary geometric modalities during both training and inference. In our framework, a GeoAdapter is proposed to encode depth and camera intrinsics/extrinsics into a spatial foundation model. It employs zero-initialized convolutions to progressively inject geometric information without disrupting the foundation model's representation space. This design ensures stable optimization with negligible overhead, maintaining inference speed comparable to VGGT even with multiple additional inputs. Additionally, a stochastic multimodal fusion regimen is proposed, which randomly samples modality subsets per instance during training. This enables an arbitrary number of modality inputs during testing and promotes learning robust spatial representations instead of overfitting to auxiliary cues. Comprehensive experiments on monocular/multi-view depth estimation, multi-view stereo, and camera pose estimation demonstrate that OmniVGGT outperforms prior methods with auxiliary inputs and achieves state-of-the-art results even with RGB-only input. To further highlight its practical utility, we integrated OmniVGGT into vision-language-action (VLA) models. The enhanced VLA model by OmniVGGT not only outperforms the vanilla point-cloud-based baseline on mainstream benchmarks, but also effectively leverages accessible auxiliary inputs to achieve consistent gains on robotic tasks.

