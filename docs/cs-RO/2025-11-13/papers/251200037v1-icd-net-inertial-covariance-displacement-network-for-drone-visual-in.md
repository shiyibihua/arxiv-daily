---
layout: default
title: ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM
---

# ICD-Net: Inertial Covariance Displacement Network for Drone Visual-Inertial SLAM

**arXiv**: [2512.00037v1](https://arxiv.org/abs/2512.00037) | [PDF](https://arxiv.org/pdf/2512.00037.pdf)

**作者**: Tali Orlev Shapira, Itzik Klein

**分类**: cs.RO, cs.CV

**发布日期**: 2025-11-13

---

## 💡 一句话要点

**ICD-Net：用于无人机视觉惯性SLAM的惯性协方差位移网络**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉惯性SLAM` `无人机` `深度学习` `惯性导航` `不确定性量化`

## 📋 核心要点

1. 视觉惯性SLAM在无人机应用中面临传感器校准误差、噪声、快速运动和光照不足等挑战。
2. ICD-Net通过学习原始惯性测量数据，直接预测位移和不确定性，无需依赖解析惯性传感器模型。
3. 实验表明，ICD-Net显著提高了无人机SLAM的轨迹估计精度，平均APE提升超过38%。

## 📝 摘要（中文）

本文提出了一种名为ICD-Net的新框架，旨在通过学习处理原始惯性测量数据并生成带有不确定性量化的位移估计，从而提升视觉惯性SLAM系统的性能。该方法不依赖于传统惯性传感器模型的解析形式，而是直接从传感器数据中提取位移图，并同时预测反映估计置信度的测量协方差。ICD-Net的输出作为附加残差约束集成到VINS-Fusion优化框架中，预测的不确定性根据神经网络的贡献程度，适当地权衡了传统视觉和惯性项。学习到的位移约束提供了补充信息，补偿了SLAM流程中的各种误差源。该方法既可用于正常运行条件，也可用于相机不一致或视觉退化的情况。在具有挑战性的高速无人机序列上的实验评估表明，与标准VINS-Fusion相比，该方法显著提高了轨迹估计精度，平均APE提高了38%以上，并且不确定性估计对于保持系统鲁棒性至关重要。该方法表明，神经网络增强可以有效地解决SLAM性能下降的多个来源，同时保持实时性能要求。

## 🔬 方法详解

**问题定义**：现有的视觉惯性SLAM系统在无人机应用中，由于传感器标定误差、噪声、快速运动、低光照以及传统惯性导航积分方法的局限性，导致性能不佳。传统方法依赖于解析的惯性传感器模型，难以应对真实世界中传感器的各种缺陷。

**核心思路**：ICD-Net的核心思路是通过神经网络直接从原始惯性测量数据中学习位移估计和对应的不确定性。这种方法避免了对精确传感器模型的依赖，能够更好地适应实际传感器的非理想特性。同时，预测的不确定性可以用于指导SLAM优化过程，提高系统的鲁棒性。

**技术框架**：ICD-Net作为一个附加模块集成到现有的VINS-Fusion框架中。整体流程如下：首先，ICD-Net接收原始惯性测量数据作为输入，通过神经网络预测位移估计和协方差矩阵。然后，将这些预测结果作为额外的残差项添加到VINS-Fusion的优化问题中。VINS-Fusion利用所有可用的信息（视觉、惯性和ICD-Net的输出）进行全局优化，得到最终的位姿估计。

**关键创新**：ICD-Net的关键创新在于使用神经网络直接学习惯性测量数据到位移的映射，并同时预测不确定性。这与传统方法依赖于解析传感器模型形成了鲜明对比。通过学习的方式，ICD-Net能够更好地适应实际传感器的非理想特性，并提供有用的不确定性信息，从而提高SLAM系统的鲁棒性和精度。

**关键设计**：ICD-Net的网络结构未知，但可以推断其输入为原始IMU数据，输出为位移估计和协方差矩阵。损失函数的设计至关重要，可能包括位移估计的误差项和协方差矩阵的正则化项，以保证预测的准确性和可靠性。协方差矩阵的预测需要保证其正定性，可能通过Cholesky分解等方法实现。

## 📊 实验亮点

实验结果表明，ICD-Net显著提高了无人机SLAM的轨迹估计精度，与标准VINS-Fusion相比，平均APE降低了38%以上。此外，ICD-Net预测的不确定性估计对于保持系统鲁棒性至关重要，尤其是在视觉信息不足或质量较差的情况下，能够有效抑制SLAM系统的漂移。

## 🎯 应用场景

ICD-Net可广泛应用于无人机自主导航、机器人定位、增强现实等领域。特别是在高动态、低光照等复杂环境下，ICD-Net能够有效提升SLAM系统的鲁棒性和精度，从而提高无人机或机器人的自主作业能力。未来，该技术有望应用于物流配送、环境监测、灾害救援等场景。

## 📄 摘要（原文）

> Visual-inertial SLAM systems often exhibit suboptimal performance due to multiple confounding factors including imperfect sensor calibration, noisy measurements, rapid motion dynamics, low illumination, and the inherent limitations of traditional inertial navigation integration methods. These issues are particularly problematic in drone applications where robust and accurate state estimation is critical for safe autonomous operation. In this work, we present ICD-Net, a novel framework that enhances visual-inertial SLAM performance by learning to process raw inertial measurements and generating displacement estimates with associated uncertainty quantification. Rather than relying on analytical inertial sensor models that struggle with real-world sensor imperfections, our method directly extracts displacement maps from sensor data while simultaneously predicting measurement covariances that reflect estimation confidence. We integrate ICD-Net outputs as additional residual constraints into the VINS-Fusion optimization framework, where the predicted uncertainties appropriately weight the neural network contributions relative to traditional visual and inertial terms. The learned displacement constraints provide complementary information that compensates for various error sources in the SLAM pipeline. Our approach can be used under both normal operating conditions and in situations of camera inconsistency or visual degradation. Experimental evaluation on challenging high-speed drone sequences demonstrated that our approach significantly improved trajectory estimation accuracy compared to standard VINS-Fusion, with more than 38% improvement in mean APE and uncertainty estimates proving crucial for maintaining system robustness. Our method shows that neural network enhancement can effectively address multiple sources of SLAM degradation while maintaining real-time performance requirements.

