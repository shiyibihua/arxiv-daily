---
layout: default
title: BronchOpt : Vision-Based Pose Optimization with Fine-Tuned Foundation Models for Accurate Bronchoscopy Navigation
---

# BronchOpt : Vision-Based Pose Optimization with Fine-Tuned Foundation Models for Accurate Bronchoscopy Navigation

**arXiv**: [2511.09443v1](https://arxiv.org/abs/2511.09443) | [PDF](https://arxiv.org/pdf/2511.09443.pdf)

**作者**: Hongchao Shu, Roger D. Soberanis-Mukul, Jiru Xu, Hao Ding, Morgan Ringel, Mali Shen, Saif Iftekar Sayed, Hedyeh Rafii-Tari, Mathias Unberath

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-12

---

## 💡 一句话要点

**BronchOpt：基于视觉和微调基础模型的支气管镜导航位姿优化**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `支气管镜导航` `位姿优化` `视觉配准` `深度学习` `医学影像` `合成数据` `域泛化`

## 📋 核心要点

1. 现有基于视觉的支气管镜导航方法难以在不同领域和患者之间泛化，导致配准误差。
2. 提出基于视觉的位姿优化框架，通过微调的基础模型实现内窥镜图像与CT图像的直接相似度计算。
3. 构建了公开的合成基准数据集，模型仅在合成数据上训练，即可在真实数据上实现良好的泛化性能。

## 📝 摘要（中文）

本研究针对支气管镜术中定位难题，即呼吸运动、解剖变异和CT-体表差异导致的术中视图与术前CT配准误差，提出了一个通用的、基于视觉的支气管镜导航框架。该框架利用微调的模态和域不变编码器，直接计算真实内窥镜RGB图像与CT渲染深度图之间的相似性，并通过可微渲染模块迭代优化相机位姿，实现帧间2D-3D配准。此外，为了提高可重复性，我们发布了首个用于支气管镜导航的合成基准数据集。模型仅在合成数据上训练，在基准测试中实现了平均2.65mm的平移误差和0.19rad的旋转误差，证明了其准确性和稳定性。在真实患者数据上的定性结果进一步证实了其强大的跨域泛化能力，无需特定领域的适应即可实现一致的帧间2D-3D对齐。总而言之，该框架通过迭代的视觉优化实现了鲁棒的、域不变的定位，而新的基准为基于视觉的支气管镜导航标准化进展奠定了基础。

## 🔬 方法详解

**问题定义**：支气管镜术中，由于呼吸运动、解剖结构差异以及CT扫描与实际体表之间的偏差，导致术中内窥镜图像与术前CT图像之间存在错位，难以实现精准定位。现有基于视觉的方法泛化能力不足，无法有效解决跨患者和跨域的配准问题。

**核心思路**：利用深度学习模型学习内窥镜图像和CT图像之间的域不变特征表达，从而实现两种模态图像的直接相似度计算。通过可微渲染技术，将位姿优化问题转化为图像相似度最大化问题，并进行迭代优化。

**技术框架**：该框架主要包含三个模块：1) 微调的模态和域不变编码器，用于提取内窥镜图像和CT渲染深度图的特征；2) 可微渲染模块，用于根据相机位姿将CT图像渲染成深度图；3) 位姿优化模块，通过迭代优化相机位姿，使得渲染的深度图与内窥镜图像的特征相似度最大化。

**关键创新**：该方法的核心创新在于：1) 提出了一个微调的模态和域不变编码器，能够有效提取内窥镜图像和CT图像的共享特征，从而实现跨模态和跨域的图像配准；2) 构建了首个公开的支气管镜导航合成基准数据集，为该领域的研究提供了标准化的评估平台。

**关键设计**：编码器采用预训练的视觉Transformer模型，并在合成数据上进行微调，以适应内窥镜图像和CT图像的特征。损失函数采用图像特征的余弦相似度，用于衡量渲染深度图与内窥镜图像之间的相似程度。位姿优化采用Adam优化器，迭代更新相机位姿。

## 📊 实验亮点

该模型在合成数据集上训练，并在公开的支气管镜导航基准数据集上进行了评估，实现了平均2.65mm的平移误差和0.19rad的旋转误差。在真实患者数据上的定性结果表明，该方法具有良好的跨域泛化能力，无需针对特定领域进行调整。

## 🎯 应用场景

该研究成果可应用于临床支气管镜导航，辅助医生进行精准定位和手术操作，减少手术风险，提高手术成功率。此外，该方法也可推广到其他医学影像引导手术，如腹腔镜手术、神经外科手术等，具有广阔的应用前景。

## 📄 摘要（原文）

> Accurate intra-operative localization of the bronchoscope tip relative to patient anatomy remains challenging due to respiratory motion, anatomical variability, and CT-to-body divergence that cause deformation and misalignment between intra-operative views and pre-operative CT. Existing vision-based methods often fail to generalize across domains and patients, leading to residual alignment errors. This work establishes a generalizable foundation for bronchoscopy navigation through a robust vision-based framework and a new synthetic benchmark dataset that enables standardized and reproducible evaluation. We propose a vision-based pose optimization framework for frame-wise 2D-3D registration between intra-operative endoscopic views and pre-operative CT anatomy. A fine-tuned modality- and domain-invariant encoder enables direct similarity computation between real endoscopic RGB frames and CT-rendered depth maps, while a differentiable rendering module iteratively refines camera poses through depth consistency. To enhance reproducibility, we introduce the first public synthetic benchmark dataset for bronchoscopy navigation, addressing the lack of paired CT-endoscopy data. Trained exclusively on synthetic data distinct from the benchmark, our model achieves an average translational error of 2.65 mm and a rotational error of 0.19 rad, demonstrating accurate and stable localization. Qualitative results on real patient data further confirm strong cross-domain generalization, achieving consistent frame-wise 2D-3D alignment without domain-specific adaptation. Overall, the proposed framework achieves robust, domain-invariant localization through iterative vision-based optimization, while the new benchmark provides a foundation for standardized progress in vision-based bronchoscopy navigation.

