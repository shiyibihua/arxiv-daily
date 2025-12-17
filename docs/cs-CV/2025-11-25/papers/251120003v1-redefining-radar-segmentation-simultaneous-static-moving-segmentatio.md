---
layout: default
title: Redefining Radar Segmentation: Simultaneous Static-Moving Segmentation and Ego-Motion Estimation using Radar Point Clouds
---

# Redefining Radar Segmentation: Simultaneous Static-Moving Segmentation and Ego-Motion Estimation using Radar Point Clouds

**arXiv**: [2511.20003v1](https://arxiv.org/abs/2511.20003) | [PDF](https://arxiv.org/pdf/2511.20003.pdf)

**作者**: Simin Zhu, Satish Ravindran, Alexander Yarovoy, Francesco Fioranelli

**分类**: eess.SP, cs.CV

**发布日期**: 2025-11-25

**备注**: 16 pages, 9 figures, under review at IEEE Transactions on Radar Systems

---

## 💡 一句话要点

**提出基于雷达点云的静态-动态分割与自运动估计同步方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `雷达点云` `静态-动态分割` `自运动估计` `深度学习` `循环神经网络`

## 📋 核心要点

1. 传统雷达分割侧重于物体类别识别，但区分静态与动态物体是自动驾驶等任务的基础，现有方法在可靠性和一致性方面存在挑战。
2. 该方法利用神经网络直接从原始雷达点云中同步分割静态和动态物体，并估计自运动，无需复杂的预处理步骤。
3. 实验结果表明，该方法在静态-动态分割和自运动估计方面表现良好，并具有应用于其他雷达感知任务的潜力。

## 📝 摘要（中文）

本研究提出了一种基于神经网络的解决方案，能够同时从雷达点云中分割静态和移动物体。与传统雷达分割研究侧重于学习不同移动物体的类别标签不同，本研究关注移动或静态物体的区分，这是许多汽车雷达感知任务的前提。此外，由于静态物体的径向速度与雷达的运动相关，该方法还可以估计移动平台或车辆的瞬时二维速度（自运动）。该方法采用多层感知器（MLP）和循环神经网络（RNN）进行特征提取，无需云聚合、多普勒补偿、运动补偿或任何其他中间信号处理步骤，直接从原始点云中提取信息。为了评估性能，本研究引入了一组新的评估指标，并使用具有挑战性的真实世界雷达数据集RadarScenes对该方法进行了测试。结果表明，该方法不仅在双重任务上表现良好，而且在其他雷达感知任务中也具有广泛的应用潜力。

## 🔬 方法详解

**问题定义**：现有雷达分割方法主要集中在识别物体的具体类别，例如行人、车辆等。然而，在许多实际应用中，例如自动驾驶，首先需要区分场景中的物体是静态的还是动态的。现有方法在雷达数据上进行精确和一致的类别预测面临挑战，且忽略了静态物体速度与自运动之间的关系。

**核心思路**：该论文的核心思路是利用神经网络同时进行静态-动态分割和自运动估计。通过分析雷达点云中点的径向速度，可以判断该点属于静态物体还是动态物体。同时，静态物体的径向速度与雷达自身的运动状态相关，因此可以反过来估计雷达的自运动。

**技术框架**：该方法直接以原始雷达点云作为输入，首先通过多层感知器（MLP）提取每个点的特征，然后使用循环神经网络（RNN）对点云序列进行处理，以捕捉时间上的依赖关系。最后，通过分类器进行静态-动态分割，并回归雷达的自运动速度。整个框架无需复杂的预处理步骤，例如点云聚合、多普勒补偿等。

**关键创新**：该方法的主要创新在于将静态-动态分割和自运动估计两个任务结合起来，利用静态物体速度与自运动之间的关系，实现同步优化。此外，该方法直接处理原始雷达点云，避免了传统方法中复杂的预处理步骤，简化了整个流程。

**关键设计**：该方法使用MLP进行点特征提取，RNN进行序列建模，并设计了专门的损失函数来优化静态-动态分割和自运动估计两个任务。具体的网络结构和参数设置在论文中进行了详细描述。论文还提出了一套新的评估指标，用于衡量静态-动态分割和自运动估计的性能。

## 📊 实验亮点

该方法在RadarScenes数据集上进行了评估，结果表明其在静态-动态分割和自运动估计方面均取得了良好的性能。论文引入了新的评估指标，并与现有方法进行了对比，验证了该方法的有效性。具体性能数据在论文中有详细展示，证明了该方法在真实场景中的应用潜力。

## 🎯 应用场景

该研究成果可广泛应用于自动驾驶、机器人导航、智能交通等领域。通过准确分割静态和动态物体，可以提高自动驾驶系统的环境感知能力，从而提升行驶安全性。同时，精确的自运动估计可以帮助机器人更好地定位和导航。该方法无需复杂的预处理，易于部署和应用，具有重要的实际价值。

## 📄 摘要（原文）

> Conventional radar segmentation research has typically focused on learning category labels for different moving objects. Although fundamental differences between radar and optical sensors lead to differences in the reliability of predicting accurate and consistent category labels, a review of common radar perception tasks in automotive reveals that determining whether an object is moving or static is a prerequisite for most tasks. To fill this gap, this study proposes a neural network based solution that can simultaneously segment static and moving objects from radar point clouds. Furthermore, since the measured radial velocity of static objects is correlated with the motion of the radar, this approach can also estimate the instantaneous 2D velocity of the moving platform or vehicle (ego motion). However, despite performing dual tasks, the proposed method employs very simple yet effective building blocks for feature extraction: multi layer perceptrons (MLPs) and recurrent neural networks (RNNs). In addition to being the first of its kind in the literature, the proposed method also demonstrates the feasibility of extracting the information required for the dual task directly from unprocessed point clouds, without the need for cloud aggregation, Doppler compensation, motion compensation, or any other intermediate signal processing steps. To measure its performance, this study introduces a set of novel evaluation metrics and tests the proposed method using a challenging real world radar dataset, RadarScenes. The results show that the proposed method not only performs well on the dual tasks, but also has broad application potential in other radar perception tasks.

