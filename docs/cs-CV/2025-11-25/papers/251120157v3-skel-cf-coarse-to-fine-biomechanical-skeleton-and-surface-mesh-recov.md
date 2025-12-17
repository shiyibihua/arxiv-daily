---
layout: default
title: SKEL-CF: Coarse-to-Fine Biomechanical Skeleton and Surface Mesh Recovery
---

# SKEL-CF: Coarse-to-Fine Biomechanical Skeleton and Surface Mesh Recovery

**arXiv**: [2511.20157v3](https://arxiv.org/abs/2511.20157) | [PDF](https://arxiv.org/pdf/2511.20157.pdf)

**作者**: Da Li, Jiping Jin, Xuanlong Yu, Wei Liu, Xiaodong Cun, Kai Chen, Rui Fan, Jiangang Kong, Xi Shen

**分类**: cs.CV

**发布日期**: 2025-11-25 (更新: 2025-11-27)

**备注**: Project page: https://pokerman8.github.io/SKEL-CF/

**🔗 代码/项目**: [PROJECT_PAGE](https://pokerman8.github.io/SKEL-CF/)

---

## 💡 一句话要点

**提出SKEL-CF框架，用于从图像中恢复生物力学骨骼和表面网格，提升人体运动分析的真实性。**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction & Matching)**

**关键词**: `人体姿态估计` `生物力学模型` `参数化人体模型` `Transformer` `由粗到精` `相机建模` `SKEL模型`

## 📋 核心要点

1. 现有基于SMPL的人体姿态估计方法，其简化的运动学结构限制了生物力学真实性，难以进行精确的人体运动分析。
2. SKEL-CF采用由粗到精的框架，利用Transformer架构，先预测粗略参数再逐步细化，并显式建模相机参数以缓解深度和尺度歧义。
3. 通过将4DHuman数据集转换为SKEL对齐的4DHuman-SKEL，为SKEL估计提供高质量训练数据，并在MOYO数据集上显著优于现有方法。

## 📝 摘要（中文）

参数化3D人体模型（如SMPL）推动了人体姿态和形状估计的显著进展，但其简化的运动学限制了生物力学的真实性。最近提出的SKEL模型通过使用解剖学上精确的骨骼重新构建SMPL来解决这一限制。然而，由于训练数据有限、透视歧义以及人体关节固有的复杂性，直接估计SKEL参数仍然具有挑战性。我们引入SKEL-CF，一个用于SKEL参数估计的由粗到精的框架。SKEL-CF采用基于Transformer的编码器-解码器架构，其中编码器预测粗略的相机和SKEL参数，解码器在连续层中逐步细化它们。为了确保解剖学上一致的监督，我们将现有的基于SMPL的数据集4DHuman转换为SKEL对齐的版本4DHuman-SKEL，为SKEL估计提供高质量的训练数据。此外，为了减轻深度和尺度歧义，我们将相机建模显式地纳入SKEL-CF流程中，并证明了其在不同视角下的重要性。大量实验验证了所提出设计的有效性。在具有挑战性的MOYO数据集上，SKEL-CF实现了85.0 MPJPE / 51.4 PA-MPJPE，显著优于之前基于SKEL的最先进方法HSMR（104.5 / 79.6）。这些结果表明SKEL-CF是一个可扩展且解剖学上忠实的人体运动分析框架，弥合了计算机视觉和生物力学之间的差距。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张图像中准确估计人体SKEL模型的参数问题，从而实现更真实的生物力学人体运动分析。现有方法，特别是基于SMPL的模型，在运动学上过于简化，无法满足对人体运动真实性要求高的应用。直接估计SKEL参数面临训练数据不足、透视歧义和人体关节复杂性等挑战。

**核心思路**：论文的核心思路是采用由粗到精的策略，利用Transformer架构的强大建模能力，逐步细化SKEL参数的估计。同时，显式地建模相机参数，以解决深度和尺度上的歧义性。此外，通过转换现有数据集，生成高质量的SKEL对齐训练数据，提升模型的泛化能力。

**技术框架**：SKEL-CF框架包含一个基于Transformer的编码器-解码器架构。编码器接收图像作为输入，预测粗略的相机参数和SKEL参数。解码器则在多个层中逐步细化这些参数。框架还包括一个数据转换模块，用于将SMPL数据集转换为SKEL对齐的数据集。整个流程包括数据预处理、粗略参数预测、参数细化和最终的SKEL模型重建。

**关键创新**：论文的关键创新在于：1) 提出了由粗到精的SKEL参数估计框架，有效利用了Transformer的建模能力；2) 显式地建模相机参数，显著缓解了深度和尺度歧义；3) 创建了SKEL对齐的高质量训练数据集4DHuman-SKEL，为SKEL模型的训练提供了有力支持。与现有方法相比，SKEL-CF更注重生物力学的真实性，并能更准确地估计人体运动。

**关键设计**：在网络结构方面，采用了Transformer编码器-解码器架构，具体层数和维度未知。损失函数方面，可能包括MPJPE（Mean Per Joint Position Error）等用于评估姿态估计准确性的指标。数据集方面，4DHuman-SKEL的转换细节未知，但保证了与SKEL模型的对齐。相机模型的具体参数化方式未知，但能够有效缓解深度和尺度歧义。

## 📊 实验亮点

SKEL-CF在MOYO数据集上取得了显著的性能提升，MPJPE指标达到85.0，PA-MPJPE指标达到51.4，相比于之前的state-of-the-art方法HSMR，分别提升了19.5和28.2。这些结果表明SKEL-CF在人体姿态估计的准确性和生物力学真实性方面都取得了显著进展。

## 🎯 应用场景

该研究成果可应用于虚拟现实、游戏、动画制作、运动分析、医疗康复等领域。通过更精确地捕捉和重建人体运动，可以提升虚拟体验的真实感，为运动员提供更科学的训练指导，辅助医生进行康复治疗方案的制定，并为动画制作提供更逼真的人物模型。

## 📄 摘要（原文）

> Parametric 3D human models such as SMPL have driven significant advances in human pose and shape estimation, yet their simplified kinematics limit biomechanical realism. The recently proposed SKEL model addresses this limitation by re-rigging SMPL with an anatomically accurate skeleton. However, estimating SKEL parameters directly remains challenging due to limited training data, perspective ambiguities, and the inherent complexity of human articulation. We introduce SKEL-CF, a coarse-to-fine framework for SKEL parameter estimation. SKEL-CF employs a transformer-based encoder-decoder architecture, where the encoder predicts coarse camera and SKEL parameters, and the decoder progressively refines them in successive layers. To ensure anatomically consistent supervision, we convert the existing SMPL-based dataset 4DHuman into a SKEL-aligned version, 4DHuman-SKEL, providing high-quality training data for SKEL estimation. In addition, to mitigate depth and scale ambiguities, we explicitly incorporate camera modeling into the SKEL-CF pipeline and demonstrate its importance across diverse viewpoints. Extensive experiments validate the effectiveness of the proposed design. On the challenging MOYO dataset, SKEL-CF achieves 85.0 MPJPE / 51.4 PA-MPJPE, significantly outperforming the previous SKEL-based state-of-the-art HSMR (104.5 / 79.6). These results establish SKEL-CF as a scalable and anatomically faithful framework for human motion analysis, bridging the gap between computer vision and biomechanics. Our implementation is available on the project page: https://pokerman8.github.io/SKEL-CF/.

